# /// script
# requires-python = ">=3.11"
# ///
"""Check out the member repositories listed in compose.toml into .repos/.

    uv run tools/repos.py                       # shallow-clone missing members
    uv run tools/repos.py --update              # also pull existing clones
    uv run tools/repos.py --worktrees ~/dev     # git worktrees from local clones
    uv run tools/repos.py --pr pymmcore-plus=someone/pymmcore-plus@<sha>

`--worktrees DIR` expects existing clones at DIR/<member> and creates a worktree
of each in .repos/<member> (on a `docs` branch from the clone's default
upstream), so you can edit docs and source while previewing the whole site.
`--pr` checks out one member at a specific repository and ref (used by CI to
build a pull request).

An optional `compose.overrides.toml` (`[overrides] name = "owner/repo@ref"`)
changes where *fresh* clones come from, e.g. to preview unmerged member branches.
It never touches existing checkouts.
"""

from __future__ import annotations

import argparse
import subprocess
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPOS = ROOT / ".repos"


def git(*args: str, cwd: Path | None = None) -> None:
    print("+ git", " ".join(args))
    subprocess.run(["git", *args], cwd=cwd, check=True)


def clone(dest: Path, repo: str, ref: str, upstream: str) -> None:
    """Clone `repo` at `ref`, with full (blob-less) history and upstream's tags.

    Members get their version from git tags (hatch-vcs), and pymmcore-widgets
    requires a recent pymmcore-plus, so shallow clones (version 0.1.dev1) or
    forks without recent tags would not resolve.
    """
    git("init", "-q", str(dest))
    git("remote", "add", "origin", f"https://github.com/{repo}.git", cwd=dest)
    git("fetch", "-q", "--filter=blob:none", "origin", ref, cwd=dest)
    git("checkout", "-q", "FETCH_HEAD", cwd=dest)
    tags = f"https://github.com/{upstream}.git"
    git("fetch", "-q", "--filter=blob:none", "--tags", tags, cwd=dest)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--update", action="store_true", help="pull existing clones")
    parser.add_argument(
        "--worktrees",
        type=Path,
        metavar="DIR",
        help="create worktrees from local clones in DIR",
    )
    parser.add_argument(
        "--pr",
        action="append",
        default=[],
        metavar="NAME=REPO@REF",
        help="check out a member at a specific repository/ref",
    )
    ns = parser.parse_args()

    members = tomllib.loads((ROOT / "compose.toml").read_text(encoding="utf-8"))[
        "member"
    ]

    def parse(target: str) -> tuple[str, str]:
        repo, _, ref = target.partition("@")
        return repo, ref or "main"

    file_overrides = {}
    if (path := ROOT / "compose.overrides.toml").exists():
        data = tomllib.loads(path.read_text(encoding="utf-8")).get("overrides", {})
        file_overrides = {name: parse(target) for name, target in data.items()}
    overrides = {}
    for spec in ns.pr:
        name, _, target = spec.partition("=")
        overrides[name] = parse(target)

    REPOS.mkdir(exist_ok=True)
    for m in members:
        name, dest = m["name"], REPOS / m["name"]
        default = file_overrides.get(name, (m["repo"], m.get("branch", "main")))
        repo, ref = overrides.get(name, default)
        if name in overrides and dest.exists():
            url = f"https://github.com/{repo}.git"
            git("fetch", "-q", "--filter=blob:none", url, ref, cwd=dest)
            git("checkout", "-q", "FETCH_HEAD", cwd=dest)
        elif dest.exists():
            if ns.update and not ns.worktrees:
                git("pull", "-q", "--ff-only", cwd=dest)
        elif ns.worktrees:
            local = ns.worktrees.expanduser() / name
            git("worktree", "add", str(dest), "-b", "docs", cwd=local)
        else:
            clone(dest, repo, ref, upstream=m["repo"])


if __name__ == "__main__":
    main()
