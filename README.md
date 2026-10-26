# pymmcore-plus.github.io

Source for **<https://pymmcore-plus.github.io>**: the unified documentation for
the pymmcore-plus ecosystem.

The site combines docs from several repositories into one site (one navigation,
one search, cross-references everywhere), built with
[zensical](https://zensical.org):

| Member | Mounted at |
| --- | --- |
| [pymmcore-plus](https://github.com/pymmcore-plus/pymmcore-plus) | `/pymmcore-plus/` |
| [useq-schema](https://github.com/pymmcore-plus/useq-schema) | `/useq-schema/` |
| [pymmcore-widgets](https://github.com/pymmcore-plus/pymmcore-widgets) | `/pymmcore-widgets/` |
| [pymmcore-gui](https://github.com/pymmcore-plus/pymmcore-gui) | `/pymmcore-gui/` |
| [napari-micromanager](https://github.com/pymmcore-plus/napari-micromanager) | `/napari-micromanager/` |

Each member keeps its docs in its own `docs/` folder (so PRs can change code and
docs together).  This repository holds the theme, the landing page, *Getting
Started*, the site-wide navigation, and the tooling that composes everything.

## Quick start

Requires [uv](https://docs.astral.sh/uv/) and [just](https://just.systems).

```sh
just serve      # clone members into .repos/, assemble, serve on localhost:8000
just build      # build into site/
just check      # strict build: fails on any warning
```

`uv run tools/compose.py serve --only pymmcore-plus,useq-schema --no-gen` gives
a faster preview of just some members, skipping their generation scripts.

To work on a member's docs (or code) with live reload, make `.repos/<member>` a
git worktree of your own clone:

```sh
git -C ~/dev/pymmcore-plus worktree add "$PWD/.repos/pymmcore-plus" -b my-docs-branch
```

## How it works

```text
compose.toml          members (name, GitHub repo, branch)
zensical.base.toml    theme, markdown extensions, plugins, global mkdocstrings options
redirects.toml        old URL -> new URL, for pages that moved
docs/                 hub pages, docs/.nav.yml (site navigation), assets/
overrides/            theme template overrides (edit links, package badge, banner)
tools/repos.py        clone / update / worktree member repos into .repos/
tools/compose.py      generate -> copy -> API pages -> zensical.toml -> build
tools/api.py          de-duplicated API reference generation
tools/pymm_mdx.py     Markdown extension (re-export anchors, small HTML tweaks)
tools/check_urls.py   verify every URL of the old sites still resolves
```

`tools/compose.py`:

1. runs each member's optional `docs/_gen.py` (generated content, screenshots);
2. copies the hub's `docs/` and each member's `docs/` into `build/docs/`,
   expanding `--8<--` snippets relative to each member's repository and adding
   `edit_url` / `package` front matter;
3. generates API reference pages from each member's `api-autonav` settings,
   documenting every object once, at its highest-level public name;
4. merges member `zensical.toml` contributions (mkdocstrings `paths`, griffe
   `extensions`, inventories) into `zensical.base.toml` -> `zensical.toml`;
5. builds with zensical, then writes per-member `objects.inv` files.

See [How these docs work](https://pymmcore-plus.github.io/contributing/docs/)
for the member-facing contract.  When zensical gains native support for
composing projects, steps 2-4 are what it should replace.

## Deployment

- `.github/workflows/deploy.yml` builds from every member's `main` and deploys
  to GitHub Pages: on push here, when a member merges to `main` (members call
  `gh workflow run deploy.yml`), and nightly.
- `.github/workflows/preview.yml` builds pull requests to this repo (on macOS
  and Windows, reporting build times) and publishes the macOS build at
  `https://pymmcore-plus.github.io/pr-preview/pr-<number>/`, via the `gh-pages`
  branch.
- `.github/workflows/build.yml` is the reusable build, also called by member
  PRs to build the whole site with the PR's changes (uploaded as an artifact).
- `compose.overrides.toml` (temporary) points CI at members' unmerged
  `zensical-docs` branches; delete it once those are merged.

Members need an org-level GitHub App (`DOCS_APP_ID` variable +
`DOCS_APP_PRIVATE_KEY` secret) with `actions: write` on this repository to
trigger deploys.
