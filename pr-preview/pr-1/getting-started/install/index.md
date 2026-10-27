# Installation

There are two things to install: the Python package(s) you want, and Micro-Manager's device adapters (the C++ drivers for your hardware). The device adapters include a set of demo devices, so you can try out the examples in these docs without a microscope.

You'll need Python 3.11 or newer.

> [!NOTE]
>
> **Where do I type these commands?**
>
> In a terminal (on Windows, PowerShell or the Anaconda Prompt). We recommend installing into a fresh environment rather than into your system Python. For example, with [conda](<https://conda-forge.org/download/>):
>
> ```sh
> conda create -n pymm python=3.12
> conda activate pymm
> ```
>
> ... or with [uv](<https://docs.astral.sh/uv/>), in the folder you'll be working in:
>
> ```sh
> uv venv  # creates a .venv folder here
> ```
>
> The `uv add` command in the uv tab below adds a dependency to a uv *project* (a folder with a `pyproject.toml`, which `uv init` creates). If you just made an environment with `uv venv`, use `uv pip install` in place of `uv add`. Either way, `uv run <command>` runs a command in that environment (e.g. `uv run python my_script.py`).

## Installing the packages

Pick what you need, and copy the commands:

```sh
pip install "pymmcore-plus[cli]"
```

```sh
uv add "pymmcore-plus[cli]"
```

The parts in square brackets are optional *extras*. `cli` makes sure you get the `mmcore` command line tool (it's currently included anyway), and `io` adds support for saving OME-TIFF files. (Saving to OME-Zarr works without it.)

> [!NOTE]
>
> **All install options**
>
> | You want | Command |
> | --- | --- |
> | The core library and the `mmcore` CLI | `pip install "pymmcore-plus[cli]"` |
> | … plus OME-TIFF writing (and `tifffile`) | `pip install "pymmcore-plus[cli,io]"` |
> | Qt widgets (choose a Qt backend) | `pip install "pymmcore-widgets[PyQt6]"` or `"pymmcore-widgets[PySide6]"` |
> | The pymmcore-gui application (needs `git`) | `pip install git+https://github.com/pymmcore-plus/pymmcore-gui` |
> | The napari plugin | `pip install "napari-micromanager[PyQt6]"` |
>
> Each package brings in everything it builds on, so you only need the top-most one: `pymmcore-gui` already includes `pymmcore-widgets`, `pymmcore-plus[cli,io]` and PyQt6; `napari-micromanager` and `pymmcore-widgets` include `pymmcore-plus[cli]`.
>
> All of these are on [PyPI](<https://pypi.org/user/tlambert03/>). (Some are on conda-forge too, but those packages are currently out of date, so please use `pip` inside your conda environment.)

## Installing the device adapters

The `mmcore` command downloads the latest compatible Micro-Manager device adapters for your platform:

```sh
mmcore install
```

(If you used `uv venv`, that's `uv run mmcore install`.)

They go into a folder in your user data directory, where `pymmcore-plus` will find them automatically. For more details (choosing a version, using an existing Micro-Manager installation, and what the "device interface version" is), see [Micro-Manager device adapters](<https://pymmcore-plus.github.io/pymmcore-plus/install/index.md>).

> [!NOTE]
>
> **Apple Silicon and Linux**
>
> On Apple Silicon Macs and on Linux, `mmcore install` currently downloads only Micro-Manager's test adapters (the demo camera and a few others). That's all you need for the examples in these docs. For real hardware on those platforms, see [Using your own microscope](<https://pymmcore-plus.github.io/guide/own-microscope/#getting-the-device-adapters>).

## Checking your setup

`mmcore info` prints the versions of the relevant packages, and the folder that the device adapters will be loaded from:

```console
$ mmcore info
python            : 3.14.2 (main, Dec  9 2025, 19:29:30) [Clang 21.1.4 ]
platform          : macOS-27.0.1-arm64-arm-64bit-Mach-O
pymmcore-plus     : 0.18.1
pymmcore          : 12.5.1.75.0
pymmcore-nano     :
core-version-info : MMCore version 12.5.1
api-version-info  : Device API version 75, Module API version 10
adapter-path      : ~/Library/Application Support/pymmcore-plus/mm/Micro-Manager-75.20260226
useq-schema       : 0.9.2
```

If `adapter-path` says `not found`, `pymmcore-plus` can't find any device adapters (did `mmcore install` work?). If something else went wrong, have a look at [Troubleshooting](<https://pymmcore-plus.github.io/pymmcore-plus/troubleshooting/index.md>), and please let us know on [image.sc](<https://forum.image.sc/tag/pymmcore-plus>) if that doesn't help.

## Next steps

Once that's done, head to [First steps](<https://pymmcore-plus.github.io/getting-started/first-steps/index.md>) to start controlling the demo devices from Python, or jump straight to [your first acquisition](<https://pymmcore-plus.github.io/getting-started/first-acquisition/index.md>) or [your first GUI](<https://pymmcore-plus.github.io/getting-started/first-gui/index.md>).
