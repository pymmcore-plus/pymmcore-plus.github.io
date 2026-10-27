# Contributing

Thanks for thinking of a way to help! Remember that contributions come in all shapes and sizes beyond writing bug fixes. Improving documentation, opening issues for bugs, asking for clarification on things you find unclear, and requesting new features are all super valuable contributions.

## Where things live

Each package has its own repository, issue tracker, and contributing notes:

| Package | Repository | Contributing notes |
| --- | --- | --- |
| pymmcore-plus | [pymmcore-plus/pymmcore-plus](<https://github.com/pymmcore-plus/pymmcore-plus>) | [Contributing to pymmcore-plus](<https://pymmcore-plus.github.io/pymmcore-plus/contributing/index.md>) |
| useq-schema | [pymmcore-plus/useq-schema](<https://github.com/pymmcore-plus/useq-schema>) |  |
| pymmcore-widgets | [pymmcore-plus/pymmcore-widgets](<https://github.com/pymmcore-plus/pymmcore-widgets>) | [Contributing to pymmcore-widgets](<https://pymmcore-plus.github.io/pymmcore-widgets/contributing/index.md>) |
| pymmcore-gui | [pymmcore-plus/pymmcore-gui](<https://github.com/pymmcore-plus/pymmcore-gui>) | [CONTRIBUTING.md](<https://github.com/pymmcore-plus/pymmcore-gui/blob/main/CONTRIBUTING.md>) |
| napari-micromanager | [pymmcore-plus/napari-micromanager](<https://github.com/pymmcore-plus/napari-micromanager>) |  |
| this website | [pymmcore-plus/pymmcore-plus.github.io](<https://github.com/pymmcore-plus/pymmcore-plus.github.io>) | [How these docs work](<https://pymmcore-plus.github.io/contributing/docs/index.md>) |

Not sure where something belongs? Open it wherever seems closest (we can move issues between repositories), or ask us on the [image.sc forum](<https://forum.image.sc/tag/pymmcore-plus>) or [Zulip](<https://imagesc.zulipchat.com/#narrow/channel/442785-pymmcore.5B-plus.5D>).

## Development setup

We use [uv](<https://docs.astral.sh/uv/>) in all of the repositories (but any virtual environment manager should work), and [prek](<https://github.com/j178/prek>) (or pre-commit) for linting:

```sh
git clone <your fork>
cd <repo>
uv sync
uv run prek install  # or: uv run pre-commit install
uv run pytest
```

Most of the tests need Micro-Manager's demo device adapters, so run `uv run mmcore install` once if you haven't already.

## Improving the docs

Most pages have an edit button (top right) that opens the source file in the right repository. (Pages in the API reference are generated from docstrings, so edit those in the package's `src/` folder.) Each package's docs live in its own `docs/` folder, so a pull request that changes code can update the documentation at the same time. To preview the full site locally, see [How these docs work](<https://pymmcore-plus.github.io/contributing/docs/index.md>).
