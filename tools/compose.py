"""Compose the unified pymmcore-plus docs from member repositories.

Pipeline (see docs/contributing/docs.md for the full story):

1. generate  run each member's `docs/_gen.py` (optional)
2. copy      hub docs -> build/docs, member docs -> build/docs/<member>/,
             expanding `--8<--` snippets relative to each member's root
3. api       write de-duplicated API pages (tools/api.py)
4. config    merge member zensical.toml contributions into zensical.base.toml
5. build     run zensical, then post-process (per-member objects.inv)

This is a stopgap until zensical supports project composition natively; members
keep self-contained configs so that switch should be cheap.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tomllib
from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path
from typing import Any

import tomli_w

sys.path.insert(0, str(Path(__file__).parent))
import api

ROOT = Path(__file__).resolve().parent.parent
REPOS = ROOT / ".repos"
HUB_DOCS = ROOT / "docs"
OUT_DOCS = ROOT / "build" / "docs"
STAGE = ROOT / "build" / "stage"  # assembled here, then synced into OUT_DOCS
SITE = ROOT / "site"
HUB_REPO = "pymmcore-plus/pymmcore-plus.github.io"
SKIP_NAMES = {"__pycache__", "_generated", ".DS_Store", "_gen.py"}
# mkdocstrings handler keys a member may contribute; any other option must match
# the hub's value (there is a single shared handler for the whole site).
MEMBER_HANDLER_KEYS = {"paths", "inventories"}
MEMBER_OPTION_KEYS = {"extensions", "preload_modules"}


class ComposeError(RuntimeError):
    pass


@dataclass
class Member:
    name: str
    repo: str
    title: str
    pypi: str = ""
    branch: str = "main"
    extra: dict[str, Any] = field(default_factory=dict)

    @property
    def root(self) -> Path:
        return REPOS / self.name

    @property
    def docs(self) -> Path:
        return self.root / "docs"

    @cached_property
    def config(self) -> dict[str, Any]:
        path = self.root / "zensical.toml"
        if not path.exists():
            return {}
        return tomllib.loads(path.read_text(encoding="utf-8")).get("project", {})

    @property
    def plugins(self) -> dict[str, Any]:
        return self.config.get("plugins", {})

    @property
    def edit_base(self) -> str:
        return f"https://github.com/{self.repo}/edit/{self.branch}/docs/"


def load_members(only: str | None = None) -> list[Member]:
    data = tomllib.loads((ROOT / "compose.toml").read_text(encoding="utf-8"))
    members = [Member(**m) for m in data["member"]]
    if only := only or os.environ.get("PYMM_DOCS_ONLY"):
        members = [m for m in members if m.name in only.split(",")]
    missing = [m.name for m in members if not m.root.exists()]
    if missing:
        raise ComposeError(
            f"missing checkouts in .repos/: {missing} (run tools/repos.py)"
        )
    return members


# ---------------------------------------------------------------------------
# 1. generate
# ---------------------------------------------------------------------------


def generate(members: list[Member], only: set[str] | None = None) -> None:
    # offscreen by default (no windows popping up); CI may choose a native platform
    env = {"QT_QPA_PLATFORM": "offscreen", **os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    for m in members:
        script = m.docs / "_gen.py"
        if script.exists() and (only is None or m.name in only):
            print(f"[compose] generate {m.name}")
            subprocess.run(
                [sys.executable, str(script)], cwd=m.root, env=env, check=True
            )


# ---------------------------------------------------------------------------
# 2. copy
# ---------------------------------------------------------------------------

_FRONT_MATTER = re.compile(r"\A---\n(.*?\n)?---\n", re.DOTALL)


def _snippet_processor(base_paths: list[Path]) -> Any:
    import markdown

    md = markdown.Markdown(
        extensions=["pymdownx.snippets"],
        extension_configs={
            "pymdownx.snippets": {
                "base_path": [str(p) for p in base_paths],
                "check_paths": True,
            }
        },
    )
    return md.preprocessors["snippet"]


def _with_meta(text: str, meta: dict[str, str]) -> str:
    if m := _FRONT_MATTER.match(text):
        body = m.group(1) or ""
        extra = "".join(
            f"{k}: {json.dumps(v)}\n"
            for k, v in meta.items()
            if f"\n{k}:" not in f"\n{body}"
        )
        if "generated: true" in body:  # generated pages have no source to edit
            extra = "".join(
                line for line in extra.splitlines(True) if "edit_url" not in line
            )
        return f"---\n{body}{extra}---\n{text[m.end() :]}"
    head = "".join(f"{k}: {json.dumps(v)}\n" for k, v in meta.items())
    return f"---\n{head}---\n{text}"


def copy_tree(
    src: Path, dest: Path, base_paths: list[Path], meta: dict[str, str], edit_base: str
) -> int:
    """Copy a docs folder, expanding snippets and injecting front matter."""
    snippets = _snippet_processor(base_paths)
    count = 0
    for path in sorted(src.rglob("*")):
        rel = path.relative_to(src)
        if any(part in SKIP_NAMES or part.endswith(".py") for part in rel.parts):
            continue
        out = dest / rel
        if path.is_dir():
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix == ".md":
            out.write_text(
                render_page(path, rel, snippets, meta, edit_base), encoding="utf-8"
            )
            count += 1
        else:
            shutil.copy2(path, out)
    return count


def render_page(
    path: Path, rel: Path, snippets: Any, meta: dict[str, str], edit_base: str
) -> str:
    text = path.read_text(encoding="utf-8")
    if "--8<--" in text:
        text = "\n".join(snippets.run(text.split("\n")))
    return _with_meta(text, {**meta, "edit_url": edit_base + rel.as_posix()})


def copy_all(members: list[Member]) -> None:
    if STAGE.exists():
        shutil.rmtree(STAGE)
    n = copy_tree(
        HUB_DOCS,
        STAGE,
        [ROOT, REPOS],
        {},
        f"https://github.com/{HUB_REPO}/edit/main/docs/",
    )
    print(f"[compose] copied {n} hub pages")
    for m in members:
        if not m.docs.exists():
            continue
        n = copy_tree(
            m.docs, STAGE / m.name, [m.root], {"package": m.name}, m.edit_base
        )
        print(f"[compose] copied {n} pages from {m.name}")


def sync_tree(src: Path, dest: Path) -> None:
    """Make `dest` identical to `src`, touching only files that changed.

    Rewriting everything would make a running `zensical serve` rebuild (and
    possibly read half-written files) on every re-assembly.
    """
    src_files = {p.relative_to(src) for p in src.rglob("*") if p.is_file()}
    dest_files = {p.relative_to(dest) for p in dest.rglob("*") if p.is_file()}
    for rel in dest_files - src_files:
        (dest / rel).unlink()
    for rel in src_files:
        a, b = src / rel, dest / rel
        if not b.exists() or a.read_bytes() != b.read_bytes():
            b.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(a, b)
    for d in sorted((p for p in dest.rglob("*") if p.is_dir()), reverse=True):
        if not any(d.iterdir()):
            d.rmdir()


# ---------------------------------------------------------------------------
# 3. api
# ---------------------------------------------------------------------------


def api_configs(members: list[Member]) -> list[api.ApiConfig]:
    out = []
    for m in members:
        if cfg := api.ApiConfig.from_member(
            m.name, m.root, m.plugins.get("api-autonav", {})
        ):
            cfg.modules = [str(m.root / p) for p in cfg.modules]
            cfg.edit_base = f"https://github.com/{m.repo}/edit/{m.branch}/"
            out.append(cfg)
    return out


def write_api(members: list[Member], config: dict[str, Any]) -> None:
    import griffe

    configs = api_configs(members)
    if not configs:
        return
    handler = config["plugins"]["mkdocstrings"]["handlers"]["python"]
    options = handler["options"]
    extensions = [_abs_ext(e) for e in options["extensions"] if not _is_fieldz(e)]
    loader = griffe.GriffeLoader(
        extensions=griffe.load_extensions(*extensions),
        search_paths=[str(ROOT / p) for p in handler["paths"]] + sys.path,
        allow_inspection=options.get("allow_inspection", True),
    )
    for mod in options.get("preload_modules", []):
        loader.load(mod)
    api.load(configs, loader)
    claims: dict[str, tuple[str, str]] = {}
    handwritten: dict[str, set[str]] = {}
    for m in members:
        ids, pages = api.find_claims(STAGE, m.name)
        claims.update(
            {k: (f"{m.name}/{page}", title) for k, (page, title) in ids.items()}
        )
        handwritten[m.name] = pages
    by_member, aliases = api.plan(configs, loader, claims)
    (ROOT / "build" / "aliases.json").write_text(
        json.dumps(aliases, indent=1), encoding="utf-8"
    )
    for m in members:
        if pages := by_member.get(m.name):
            written = api.write(pages, STAGE, m.name, handwritten[m.name])
            print(f"[compose] wrote {len(written)} API pages for {m.name}")


def _abs_ext(ext: Any) -> Any:
    if isinstance(ext, str) and ".py" in ext:
        return str(ROOT / ext)
    if isinstance(ext, dict):
        return {(str(ROOT / k) if ".py" in k else k): v for k, v in ext.items()}
    return ext


def _is_fieldz(ext: Any) -> bool:
    return (isinstance(ext, dict) and "griffe_fieldz" in ext) or ext == "griffe_fieldz"


# ---------------------------------------------------------------------------
# 4. config
# ---------------------------------------------------------------------------


def _prefix(member: Member, path: str) -> str:
    return (Path(".repos") / member.name / path).as_posix()


def _merge_extension(member: Member, ext: Any) -> Any:
    """Make file-based griffe extensions (`docs/x.py:Cls`) hub-relative."""
    if isinstance(ext, str) and ".py" in ext:
        return _prefix(member, ext)
    if isinstance(ext, dict):
        return {(_prefix(member, k) if ".py" in k else k): v for k, v in ext.items()}
    return ext


def build_config(members: list[Member]) -> dict[str, Any]:
    base = tomllib.loads((ROOT / "zensical.base.toml").read_text(encoding="utf-8"))
    project = base["project"]
    handler = project["plugins"]["mkdocstrings"]["handlers"]["python"]
    options = handler["options"]
    own_urls = {
        f"https://pymmcore-plus.github.io/{m.name}/objects.inv" for m in members
    }

    for m in members:
        mcfg = m.plugins.get("mkdocstrings", {}).get("handlers", {}).get("python", {})
        for key in mcfg:
            if key != "options" and key not in MEMBER_HANDLER_KEYS:
                raise ComposeError(
                    f"{m.name}: handler key {key!r} must be set in the hub"
                )
        handler["paths"] += [_prefix(m, p) for p in mcfg.get("paths", [])]
        for inv in mcfg.get("inventories", []):
            url = inv if isinstance(inv, str) else inv.get("url")
            if url not in own_urls and inv not in handler["inventories"]:
                handler["inventories"].append(inv)
        for key, value in mcfg.get("options", {}).items():
            if key == "extensions":
                options["extensions"] += [
                    e
                    for e in (_merge_extension(m, x) for x in value)
                    if e not in options["extensions"]
                ]
            elif key == "preload_modules":
                options["preload_modules"] += [
                    v for v in value if v not in options["preload_modules"]
                ]
            elif options.get(key) != value:
                raise ComposeError(
                    f"{m.name}: mkdocstrings option {key}={value!r} differs from the "
                    f"hub ({options.get(key)!r}); set it per `:::` block instead"
                )
        for plugin in m.plugins:
            if plugin not in project["plugins"] and plugin != "api-autonav":
                raise ComposeError(
                    f"{m.name}: plugin {plugin!r} must be enabled in the hub"
                )

    # api pages are generated by tools/api.py, not zensical's api-autonav
    project["plugins"].pop("api-autonav", None)
    _check_plugins(project["plugins"])

    redirects_file = ROOT / "redirects.toml"
    if redirects_file.exists():
        maps = tomllib.loads(redirects_file.read_text(encoding="utf-8")).get(
            "redirects", {}
        )
        project["plugins"]["redirects"]["redirect_maps"] = maps
    project.setdefault("extra", {})["members"] = {
        m.name: {"title": m.title, "repo": m.repo, "pypi": m.pypi} for m in members
    }
    project["watch"] = [p for p in handler["paths"]] + ["docs", "overrides"]
    return project


def _check_plugins(plugins: dict[str, Any]) -> None:
    try:
        from zensical.config import _PLUGIN_UNSUPPORTED_OPTIONS as supported
    except ImportError:  # private API; skip the check if it moves
        return
    if unknown := set(plugins) - set(supported):
        raise ComposeError(
            f"plugins not supported by zensical (silently ignored): {unknown}"
        )


def write_config(project: dict[str, Any]) -> Path:
    path = ROOT / "zensical.toml"
    tmp = path.with_suffix(".tmp")
    header = "# generated by tools/compose.py -- do not edit\n"
    tmp.write_text(header + tomli_w.dumps({"project": project}), encoding="utf-8")
    tmp.replace(path)  # atomic, so `zensical serve` never sees a partial file
    return path


# ---------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------

_HEADING_ID = re.compile(r"^#{1,6} .*\{[^}]*#([\w.:-]+)[^}]*\}\s*$", re.MULTILINE)
_AUTODOC = re.compile(r"^\s*:::\s*([\w.]+)", re.MULTILINE)


def check_sources() -> list[str]:
    """Catch problems that zensical's --strict doesn't."""
    problems: list[str] = []
    ids: dict[str, str] = {}
    autodocs: dict[str, str] = {}
    for md in OUT_DOCS.rglob("*.md"):
        rel = md.relative_to(OUT_DOCS).as_posix()
        text = md.read_text(encoding="utf-8")
        for match in _HEADING_ID.finditer(text):
            if (prev := ids.setdefault(match[1], rel)) != rel:
                problems.append(f"duplicate heading id #{match[1]}: {prev} and {rel}")
        for match in _AUTODOC.finditer(text):
            # same object rendered on two pages (claims may split blocks on one page)
            if (prev := autodocs.setdefault(match[1], rel)) != rel:
                problems.append(f"`::: {match[1]}` rendered in {prev} and {rel}")
    problems += _check_nav_duplicates()
    return list(dict.fromkeys(problems))


def _check_nav_duplicates() -> list[str]:
    import yaml

    seen: dict[str, str] = {}
    problems = []

    def walk(items: Any, base: Path, src: str) -> None:
        for item in items or []:
            values = item.values() if isinstance(item, dict) else [item]
            for v in values:
                if isinstance(v, list):
                    walk(v, base, src)
                elif isinstance(v, str) and v.endswith(".md") and "*" not in v:
                    target = (base / v).resolve().relative_to(OUT_DOCS).as_posix()
                    if (prev := seen.setdefault(target, src)) != src:
                        problems.append(f"{target} listed in both {prev} and {src}")

    for nav in OUT_DOCS.rglob(".nav.yml"):
        data = yaml.safe_load(nav.read_text(encoding="utf-8")) or {}
        walk(data.get("nav"), nav.parent, nav.relative_to(OUT_DOCS).as_posix())
    return problems


def check_orphans() -> list[str]:
    """Built pages that are not reachable from the navigation."""
    orphans = []
    for html in SITE.rglob("index.html"):
        rel = html.relative_to(SITE).as_posix()
        text = html.read_text(encoding="utf-8", errors="ignore")
        if 'http-equiv="refresh"' in text:  # redirect stub
            continue
        if "md-nav__item--active" not in text and rel != "index.html":
            orphans.append(rel)
    return [f"not in nav: {o}" for o in sorted(orphans)]


# ---------------------------------------------------------------------------
# 5. postbuild
# ---------------------------------------------------------------------------


def split_inventory(members: list[Member]) -> None:
    """Write /<member>/objects.inv so existing intersphinx/mkdocstrings users work."""
    from mkdocstrings import Inventory

    root_inv = SITE / "objects.inv"
    if not root_inv.exists():
        return
    with root_inv.open("rb") as f:
        inventory = Inventory.parse_sphinx(f)
    for m in members:
        sub = Inventory(project=m.title, version="latest")
        prefix = f"{m.name}/"
        for item in inventory.values():
            if item.uri.startswith(prefix):
                item.uri = item.uri[len(prefix) :]
                sub[item.name] = item
        if len(sub):
            (SITE / m.name).mkdir(exist_ok=True)
            (SITE / m.name / "objects.inv").write_bytes(sub.format_sphinx())
            print(f"[compose] {m.name}/objects.inv: {len(sub)} objects")


# symbol badges (e.g. "mod", "c") in the API nav titles, possibly escaped
NAV_SYMBOL = re.compile(r"\\?<code class='doc-symbol[^']*'\\?>\\?</code\\?>")


def clean_llms_txt() -> None:
    """Strip markup that the llmstxt plugin copies from nav titles."""
    for name in ("llms.txt", "llms-full.txt"):
        path = SITE / name
        if path.exists():
            text = NAV_SYMBOL.sub("", path.read_text(encoding="utf-8"))
            path.write_text(text.replace("&amp;amp;", "&"), encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def assemble(members: list[Member], *, regenerate: bool = True) -> dict[str, Any]:
    if regenerate:
        generate(members)
    copy_all(members)
    project = build_config(members)
    write_api(members, project)
    OUT_DOCS.mkdir(parents=True, exist_ok=True)
    sync_tree(STAGE, OUT_DOCS)
    write_config(project)
    return project


def _zensical_env() -> dict[str, str]:
    # tools/ on the path so `pymm_mdx` and `pymm_griffe` (our Markdown and griffe
    # extensions) are importable
    path = os.pathsep.join(
        filter(None, [str(ROOT / "tools"), os.environ.get("PYTHONPATH")])
    )
    return {**os.environ, "PYTHONPATH": path, "PYTHONDONTWRITEBYTECODE": "1"}


def _zensical(*args: str) -> list[str]:
    exe = shutil.which("zensical", path=str(Path(sys.executable).parent))
    return [exe or "zensical", *args]


def cmd_build(ns: argparse.Namespace) -> int:
    members = load_members(ns.only)
    assemble(members, regenerate=not ns.no_gen)
    problems = check_sources()
    args = ["build", "--clean"] + (["--strict"] if ns.strict and not ns.scope else [])
    proc = subprocess.run(
        _zensical(*args), cwd=ROOT, text=True, capture_output=True, env=_zensical_env()
    )
    output = proc.stdout + proc.stderr
    print(output, end="")
    if proc.returncode:
        return proc.returncode
    split_inventory(members)
    clean_llms_txt()
    problems += check_orphans()
    if ns.scope:
        problems += [w for w in _warnings(output) if _in_scope(w, ns.scope, members)]
    for p in problems:
        print(f"[compose] PROBLEM: {p}", file=sys.stderr)
    return 1 if (problems and (ns.strict or ns.scope)) else 0


_ANSI = re.compile(r"\x1b\[[0-9;]*m")


def _warnings(output: str) -> list[str]:
    """Warnings from zensical (incl. their source location) and griffe."""
    lines = [_ANSI.sub("", line) for line in output.splitlines()]
    found = []
    for i, line in enumerate(lines):
        if line.startswith("Warning"):
            # the location may be on the next lines: "╭─[ member/page.md:1:2 ]"
            found.append(" ".join(x.strip() for x in lines[i : i + 3]))
        elif line.startswith("griffe:"):
            found.append(line)
    return found


def _in_scope(warning: str, scope: str, members: list[Member]) -> bool:
    if scope == "hub":
        return not any(f"{m.name}/" in warning for m in members)
    return f"{scope}/" in warning


def cmd_serve(ns: argparse.Namespace) -> int:
    from watchfiles import watch

    members = load_members(ns.only)
    assemble(members, regenerate=not ns.no_gen)
    serve = _zensical("serve", "-a", ns.addr)
    proc = subprocess.Popen(serve, cwd=ROOT, env=_zensical_env())
    watched = [HUB_DOCS, ROOT / "zensical.base.toml", ROOT / "redirects.toml"]
    for m in members:
        watched += [
            m.docs,
            m.root / "zensical.toml",
            m.root / "src",
            m.root / "examples",
            m.root / "README.md",
        ]
    paths = [p for p in watched if p.exists()]
    try:
        for changes in watch(
            *paths, watch_filter=_watch_filter, yield_on_timeout=True, rust_timeout=2000
        ):
            if changes:
                _on_change({Path(p) for _, p in changes}, members)
            if proc.poll() is not None:  # zensical died (e.g. files vanished mid-build)
                print("[compose] zensical exited; restarting")
                proc = subprocess.Popen(serve, cwd=ROOT, env=_zensical_env())
    except KeyboardInterrupt:
        pass
    finally:
        proc.terminate()
    return 0


def _watch_filter(change: Any, path: str) -> bool:
    return not any(s in path for s in ("__pycache__", "/_generated/", ".DS_Store", "~"))


def _on_change(paths: set[Path], members: list[Member]) -> None:
    configs = {ROOT / "zensical.base.toml", ROOT / "redirects.toml"}
    src_changed = {
        m.name for m in members for p in paths if p.is_relative_to(m.root / "src")
    }
    if paths & configs or any(p.name == "zensical.toml" for p in paths) or src_changed:
        # src changes can affect generated pages (e.g. the CMMCorePlus table)
        for m in members:
            m.__dict__.pop("config", None)
        if src_changed:
            generate(members, only=src_changed)
        assemble(members, regenerate=False)
        print("[compose] re-assembled")
        return
    for path in paths:
        _recopy(path, members)


def _recopy(path: Path, members: list[Member]) -> None:
    if path.is_relative_to(HUB_DOCS):
        src_root, dest, bases, meta, edit = (
            HUB_DOCS,
            OUT_DOCS,
            [ROOT, REPOS],
            {},
            f"https://github.com/{HUB_REPO}/edit/main/docs/",
        )
    else:
        m = next((m for m in members if path.is_relative_to(m.root)), None)
        if m is None:
            return
        if not path.is_relative_to(m.docs):
            # an example/README changed: re-render pages that may include it
            copy_tree(
                m.docs, OUT_DOCS / m.name, [m.root], {"package": m.name}, m.edit_base
            )
            print(f"[compose] re-copied {m.name} (snippet source changed)")
            return
        src_root, dest, bases, meta, edit = (
            m.docs,
            OUT_DOCS / m.name,
            [m.root],
            {"package": m.name},
            m.edit_base,
        )
    rel = path.relative_to(src_root)
    out = dest / rel
    if not path.exists():
        out.unlink(missing_ok=True)
    elif path.suffix == ".md":
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            render_page(path, rel, _snippet_processor(bases), meta, edit),
            encoding="utf-8",
        )
    elif path.is_file() and not any(p in SKIP_NAMES for p in rel.parts):
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, out)
    print(f"[compose] updated {out.relative_to(OUT_DOCS)}")


def cmd_check(ns: argparse.Namespace) -> int:
    members = load_members(ns.only)
    assemble(members, regenerate=not ns.no_gen)
    problems = check_sources()
    for p in problems:
        print(f"[compose] PROBLEM: {p}", file=sys.stderr)
    return 1 if problems else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="assemble and build the site")
    b.add_argument("--strict", action="store_true", help="fail on any warning")
    b.add_argument("--scope", help="fail only on warnings from this member (or 'hub')")
    s = sub.add_parser("serve", help="assemble, serve, and live-reload")
    s.add_argument("-a", "--addr", default="localhost:8000")
    c = sub.add_parser("check", help="assemble and run source checks only")
    for p in (b, s, c):
        p.add_argument(
            "--no-gen", action="store_true", help="skip member _gen.py scripts"
        )
        p.add_argument(
            "--only", help="comma-separated members to include (quick previews)"
        )
    ns = parser.parse_args(argv)
    try:
        return {"build": cmd_build, "serve": cmd_serve, "check": cmd_check}[ns.cmd](ns)
    except ComposeError as e:
        print(f"[compose] error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
