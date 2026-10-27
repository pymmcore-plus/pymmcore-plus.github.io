"""Generate de-duplicated API reference pages for the composed site.

Members declare a native `api-autonav` block in their zensical.toml.  zensical's
own api-autonav renders every public location of an object (so re-exported names
are documented several times), and allows only one api root per build.  Here we
emulate it per member, with two extra rules:

1. **Highest-level name wins.**  Each object is rendered once, at its public
   location with the fewest dotted parts.  Other modules exporting it get a
   "Re-exports" table linking there.
2. **Hand-written pages claim objects.**  Any `::: identifier` block in a
   member's own pages means that page documents the object; the generated module
   page links to it instead of rendering it again.  A hand-written page at a
   module's generated path (e.g. `api/pkg/sub/index.md`) replaces that page.
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any

import griffe

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

MOD_PREFIX = "<code class='doc-symbol doc-symbol-nav doc-symbol-module'></code>"
KIND_PREFIX = "<code class='doc-symbol doc-symbol-nav doc-symbol-{kind}'></code>"
_AUTODOC = re.compile(r"^\s*:::\s*([\w.]+)", re.MULTILINE)
_TITLE = re.compile(
    r"^title:\s*\"?([^\"\n]+)\"?\s*$|^#\s+(.+?)(?:\s*\{.*\})?\s*$", re.MULTILINE
)


@dataclass
class ApiConfig:
    """A member's api-autonav settings (the subset we honor)."""

    member: str
    root: Path  # member checkout
    modules: list[str]
    exclude: list[str] = field(default_factory=list)
    module_options: dict[str, dict[str, Any]] = field(default_factory=dict)
    api_root_uri: str = "api"
    exclude_private: bool = True
    edit_base: str = ""  # e.g. https://github.com/<repo>/edit/main/ (for edit links)

    @classmethod
    def from_member(cls, member: str, root: Path, cfg: dict) -> ApiConfig | None:
        if not (cfg and cfg.get("enabled", True)):
            return None
        return cls(
            member=member,
            root=root,
            modules=list(cfg.get("modules", [])),
            exclude=list(cfg.get("exclude", [])),
            module_options=dict(cfg.get("module_options", {})),
            api_root_uri=cfg.get("api_root_uri", "api"),
            exclude_private=cfg.get("exclude_private", True),
        )


@dataclass
class Claim:
    """An object documented on a hand-written page."""

    name: str
    path: str  # identifier rendered by the page
    page: str  # docs-relative path of the claiming page (incl. mount)
    title: str
    kind: str
    summary: str


@dataclass
class ModulePage:
    config: ApiConfig
    module: griffe.Module
    members: list[str] = field(default_factory=list)
    reexports: list[tuple[str, str, str]] = field(default_factory=list)
    claimed: list[Claim] = field(default_factory=list)
    children: list[ModulePage] = field(default_factory=list)  # submodule pages

    @property
    def path(self) -> str:
        return self.module.path

    @property
    def is_package(self) -> bool:
        return self.module.is_init_module

    def rel_path(self) -> str:
        """Member-docs-relative page path, mirroring api-autonav's layout."""
        parts = self.path.split(".")
        if self.is_package:
            return "/".join([self.config.api_root_uri, *parts, "index.md"])
        return "/".join([self.config.api_root_uri, *parts[:-1], f"{parts[-1]}.md"])

    def rel_dir(self) -> str:
        return self.rel_path().rsplit("/", 1)[0]


# ---------------------------------------------------------------------------
# discovery
# ---------------------------------------------------------------------------


def _excluded(path: str, cfg: ApiConfig) -> bool:
    if cfg.exclude_private and any(p.startswith("_") for p in path.split(".")):
        return True
    for pattern in cfg.exclude:
        if pattern.startswith("re:"):
            if re.search(pattern[3:], path):
                return True
        elif path == pattern or path.startswith(pattern + "."):
            return True
    return False


def _iter_modules(mod: griffe.Module, cfg: ApiConfig) -> Iterator[griffe.Module]:
    if _excluded(mod.path, cfg):
        return
    yield mod
    for sub in sorted(mod.modules.values(), key=lambda m: m.name):
        if not sub.is_alias:
            yield from _iter_modules(sub, cfg)  # type: ignore[arg-type]


def _summary(obj: griffe.Object | griffe.Alias) -> str:
    try:
        doc = obj.docstring
    except griffe.AliasResolutionError:
        return ""
    if not doc:
        return ""
    line = doc.value.strip().split("\n\n")[0].replace("\n", " ").strip()
    return line.replace("|", "\\|")


def _target_path(obj: griffe.Object | griffe.Alias) -> str | None:
    if not obj.is_alias:
        return obj.path
    try:
        return obj.final_target.path  # type: ignore[union-attr]
    except (griffe.AliasResolutionError, griffe.CyclicAliasError):
        return None


def _kind(obj: griffe.Object | griffe.Alias) -> str:
    try:
        return obj.kind.value
    except griffe.AliasResolutionError:
        return "attribute"


def _page_title(text: str, fallback: str) -> str:
    match = _TITLE.search(text)
    return (match[1] or match[2]).strip() if match else fallback


def find_claims(docs: Path, mount: str) -> tuple[dict[str, tuple[str, str]], set[str]]:
    """Scan a member's (copied, snippet-expanded) docs for claims.

    Returns `{identifier: (page, title)}` for every `:::` block on a hand-written
    page (page paths relative to the mount), and the set of hand-written pages.
    """
    identifiers: dict[str, tuple[str, str]] = {}
    pages: set[str] = set()
    for md in sorted((docs / mount).rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        if "\ngenerated: true\n" in text[:300]:
            continue
        rel = md.relative_to(docs / mount).as_posix()
        pages.add(rel)
        title = _page_title(text, md.stem)
        for ident in _AUTODOC.findall(text):
            identifiers.setdefault(ident, (rel, title))
    return identifiers, pages


def load(configs: Sequence[ApiConfig], loader: griffe.GriffeLoader) -> None:
    for cfg in configs:
        for mod_path in cfg.modules:
            loader.load(Path(mod_path).name)
    loader.resolve_aliases(implicit=False, external=None)


# ---------------------------------------------------------------------------
# planning
# ---------------------------------------------------------------------------


def plan(
    configs: Sequence[ApiConfig],
    loader: griffe.GriffeLoader,
    claims: dict[str, tuple[str, str]],
) -> tuple[dict[str, list[ModulePage]], dict[str, str]]:
    """Decide, for every public object, the single page that documents it.

    `claims` maps identifiers rendered by hand-written pages to (page, title).
    Returns module pages per member, and a map of every other public path of an
    object to the path it is documented at (so references to those resolve).
    """
    pages: dict[str, list[ModulePage]] = defaultdict(list)
    # target path -> [(public location, module page, name)]
    locations: dict[str, list[tuple[str, ModulePage, str]]] = defaultdict(list)
    for cfg in configs:
        for mod_path in cfg.modules:
            pkg = loader.modules_collection[Path(mod_path).name]
            for mod in _iter_modules(pkg, cfg):
                page = ModulePage(cfg, mod)
                pages[cfg.member].append(page)
                for name, obj in mod.members.items():
                    if name.startswith("_") or name in NOT_API:
                        continue  # e.g. __version__, or a private name in __all__
                    try:
                        if not obj.is_public or obj.is_module:
                            continue
                    except griffe.AliasResolutionError:
                        continue  # e.g. a stdlib import that isn't loaded
                    if (target := _target_path(obj)) is None:
                        print(
                            f"[api] unresolved alias {mod.path}.{name}", file=sys.stderr
                        )
                        continue
                    if "_deprecated" in target.split("."):
                        continue  # still importable, but not to be documented
                    locations[target].append((f"{mod.path}.{name}", page, name))

    aliases: dict[str, str] = {}
    for target, locs in locations.items():
        defining_module = target.rsplit(".", 1)[0]

        def rank(
            loc: tuple[str, ModulePage, str], defining: str = defining_module
        ) -> tuple[int, int, int, str]:
            path, page, _ = loc
            return (
                0 if path in claims else 1,  # claimed by a hand-written page
                path.count("."),  # highest-level public name
                0 if page.path == defining else 1,  # where it's defined
                path,
            )

        best_path, best_page, best_name = min(locs, key=rank)
        best_obj = best_page.module.members[best_name]
        summary = _summary(best_obj)
        if claim := claims.get(best_path) or claims.get(target):
            best_page.claimed.append(
                Claim(
                    best_name, best_path, claim[0], claim[1], _kind(best_obj), summary
                )
            )
        else:
            best_page.members.append(best_name)
        for path, page, name in locs:
            if path != best_path:
                page.reexports.append((name, best_path, summary))
                aliases[path] = best_path
    return pages, aliases


# ---------------------------------------------------------------------------
# rendering
# ---------------------------------------------------------------------------


# module-level names that are never API, even when griffe considers them public
NOT_API = {"logger", "log"}
GROUPS = {"class": "Classes", "function": "Functions"}  # anything else: Attributes


def _options(page: ModulePage, **overrides: Any) -> dict[str, Any]:
    options: dict[str, Any] = {}
    for pattern, local in page.config.module_options.items():
        if re.match(pattern, page.path):
            options.update(local)
    return {**options, **overrides}


def _member_rows(page: ModulePage) -> dict[str, list[tuple[str, str, str]]]:
    """(name, identifier, summary) of everything in the module, grouped by kind."""
    groups: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for name in page.members:
        obj = page.module.members[name]
        group = GROUPS.get(_kind(obj), "Attributes")
        groups[group].append((name, f"{page.path}.{name}", _summary(obj)))
    for c in page.claimed:
        groups[GROUPS.get(c.kind, "Attributes")].append((c.name, c.path, c.summary))
    return {
        g: sorted(groups[g])
        for g in ("Classes", "Functions", "Attributes")
        if g in groups
    }


def render(page: ModulePage) -> str:
    lines = [
        "---",
        f"title: {json.dumps(page.path)}",
        f"package: {json.dumps(page.config.member)}",
        "generated: true",
    ]
    # "edit" opens the module's source: that's where its docs (docstrings) live
    filepath = page.module.filepath
    if page.config.edit_base and isinstance(filepath, Path):
        rel = filepath.resolve().relative_to(page.config.root.resolve()).as_posix()
        lines.append(f"edit_url: {json.dumps(page.config.edit_base + rel)}")
    # the module itself: heading and docstring
    root = _options(
        page,
        heading_level=1,
        show_root_heading=True,
        members=False,
        show_submodules=False,
    )
    lines += ["---", "", f"::: {page.path}", f"    options: {json.dumps(root)}", ""]

    # an index of the package: submodules, then everything in it by kind (linking
    # to where each object is documented: below, or on a page of its own)
    def table(label: str, rows: list[tuple[str, str, str]]) -> None:
        lines.extend([f"**{label}**", "", "| Name | Description |", "| --- | --- |"])
        lines.extend(f"| [`{n}`][{ident}] | {summary} |" for n, ident, summary in rows)
        lines.append("")

    if page.children:
        subs = sorted(page.children, key=lambda p: p.path)
        table(
            "Submodules",
            [(c.path.rsplit(".", 1)[-1], c.path, _summary(c.module)) for c in subs],
        )
    groups = _member_rows(page)
    for label, rows in groups.items():
        table(label, rows)

    # then the full documentation of what's documented here, in source order
    slug = page.path.replace(".", "-")
    member = _options(
        page, heading_level=3, show_root_heading=True, show_root_full_path=False
    )
    for label in groups:
        names = [n for n in page.module.members if n in page.members]
        names = [
            n
            for n in names
            if GROUPS.get(_kind(page.module.members[n]), "Attributes") == label
        ]
        if not names:
            continue
        lines += [f"## {label} {{#{slug}--{label.lower()}}}", ""]
        for name in names:
            lines += [
                f"::: {page.path}.{name}",
                f"    options: {json.dumps(member)}",
                "",
            ]

    if page.reexports:
        lines += [
            f"## Re-exports {{#{slug}--reexports}}",
            "",
            "These can also be imported from this module, but each is documented "
            "under its shortest import path (linked below).",
            "",
            "| Name | Description |",
            "| --- | --- |",
        ]
        for name, target, summary in sorted(page.reexports):
            lines.append(f"| [`{name}`][{target}] | {summary} |")
        lines.append("")
    return "\n".join(lines)


def write(
    pages: list[ModulePage], out_docs: Path, mount: str, handwritten: set[str]
) -> list[str]:
    """Write generated module pages (and `.nav.yml` files) under out_docs/mount.

    Pages that a member wrote by hand at the same path are left alone.  Returns
    the docs-relative paths written.
    """
    written: list[str] = []
    # drop pages that would only list re-exports (their names still resolve, via
    # aliases); a package page stays if any submodule page does.  Deepest first.
    kept: list[ModulePage] = []
    for page in sorted(pages, key=lambda p: -p.path.count(".")):
        page.children = [c for c in kept if c.path.rsplit(".", 1)[0] == page.path]
        if (
            page.members
            or page.claimed
            or page.children
            or "." not in page.path
            or page.rel_path() in handwritten
        ):
            kept.append(page)
    kept_ids = {id(p) for p in kept}
    pages = [p for p in pages if id(p) in kept_ids]

    dirs: dict[str, dict[str, Any]] = defaultdict(
        lambda: {"index": None, "modules": [], "subdirs": set(), "objects": []}
    )
    for page in pages:
        rel = page.rel_path()
        entry = dirs[page.rel_dir()]
        if page.is_package:
            entry["index"] = page
            if "." in page.path:
                parent, leaf = page.rel_dir().rsplit("/", 1)
                dirs[parent]["subdirs"].add(leaf)
            # hand-written object pages living in this package's directory (not
            # the package page itself, when a hand-written one replaces it)
            for c in page.claimed:
                folder, name = c.page.rsplit("/", 1)
                if folder == f"{mount}/{page.rel_dir()}" and name != "index.md":
                    entry["objects"].append(c)
        else:
            entry["modules"].append(page)
        if rel in handwritten:
            continue
        dest = out_docs / mount / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(page), encoding="utf-8")
        written.append(f"{mount}/{rel}")

    for rel_dir, entry in dirs.items():
        if entry["index"] is None:
            continue
        nav: list[Any] = ["index.md"]
        for c in sorted(entry["objects"], key=lambda c: c.name):
            nav.append(
                {KIND_PREFIX.format(kind=c.kind) + c.name: c.page.rsplit("/", 1)[1]}
            )
        # modules and subpackages together, alphabetically
        children = {mod.path.rsplit(".", 1)[-1]: mod for mod in entry["modules"]}
        for leaf in sorted({*children, *entry["subdirs"]}):
            if leaf in children:
                nav.append({f"{MOD_PREFIX}{leaf}": f"{leaf}.md"})
            else:
                nav.append(leaf)
        title = MOD_PREFIX + entry["index"].path.rsplit(".", 1)[-1]
        nav_file = out_docs / mount / rel_dir / ".nav.yml"
        nav_file.write_text(
            json.dumps({"title": title, "nav": nav}, indent=2), encoding="utf-8"
        )
    return written
