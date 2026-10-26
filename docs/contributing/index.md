---
title: Contributing
---

# Contributing

Thanks for thinking of a way to help!  Contributions come in many shapes:
reporting bugs, asking questions where something is unclear, improving
documentation, and writing code are all valuable.

## Where things live

Each package has its own repository, issue tracker, and contributing notes:

| Package | Repository | Contributing notes |
| --- | --- | --- |
| pymmcore-plus | [pymmcore-plus/pymmcore-plus](https://github.com/pymmcore-plus/pymmcore-plus) | [Contributing to pymmcore-plus](../pymmcore-plus/contributing.md) |
| useq-schema | [pymmcore-plus/useq-schema](https://github.com/pymmcore-plus/useq-schema) | |
| pymmcore-widgets | [pymmcore-plus/pymmcore-widgets](https://github.com/pymmcore-plus/pymmcore-widgets) | [Contributing to pymmcore-widgets](../pymmcore-widgets/contributing.md) |
| pymmcore-gui | [pymmcore-plus/pymmcore-gui](https://github.com/pymmcore-plus/pymmcore-gui) | [CONTRIBUTING.md](https://github.com/pymmcore-plus/pymmcore-gui/blob/main/CONTRIBUTING.md) |
| napari-micromanager | [pymmcore-plus/napari-micromanager](https://github.com/pymmcore-plus/napari-micromanager) | |
| this website | [pymmcore-plus/pymmcore-plus.github.io](https://github.com/pymmcore-plus/pymmcore-plus.github.io) | [How these docs work](docs.md) |

Not sure where something belongs?  Ask on the
[image.sc forum](https://forum.image.sc/tag/pymmcore-plus) or
[Zulip](https://imagesc.zulipchat.com/#narrow/channel/442785-pymmcore.5B-plus.5D).

## Development setup

All repositories use [uv](https://docs.astral.sh/uv/) and
[prek](https://github.com/j178/prek) (or pre-commit):

```sh
git clone https://github.com/pymmcore-plus/<repo>
cd <repo>
uv sync
prek install
uv run pytest
```

Most tests need the Micro-Manager demo device adapters: `uv run mmcore install`.

## Improving the docs

Every page has an :material-file-edit-outline: **edit** button (top right) that
opens the source file in the right repository.  Each package's docs live in its
own `docs/` folder (and in its docstrings), so a pull request that changes code
can update the documentation at the same time.  To preview the full site
locally, see [How these docs work](docs.md).
