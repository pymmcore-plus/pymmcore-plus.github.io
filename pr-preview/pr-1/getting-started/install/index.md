# Installation

Installation has two parts:

1. **The Python packages** you want (they pull in everything they build on).
2. **Micro-Manager's device adapters**: the C++ drivers for your hardware, including a set of demo devices that let you try everything without a microscope.

## 1\. Install the packages

Pick what you need and copy the command:

```sh
pip install "pymmcore-plus[cli]"
```

```sh
uv add "pymmcore-plus[cli]"
```

> [!NOTE]
>
> **All the options, spelled out**
>
> | You want | Command |
> | --- | --- |
> | The core library and the `mmcore` CLI | `pip install "pymmcore-plus[cli]"` |
> | … plus saving to OME-Zarr / OME-TIFF | `pip install "pymmcore-plus[cli,io]"` |
> | Qt widgets (choose a Qt backend) | `pip install "pymmcore-widgets[PyQt6]"` or `"pymmcore-widgets[PySide6]"` |
> | The pymmcore-gui application | `pip install git+https://github.com/pymmcore-plus/pymmcore-gui` |
> | The napari plugin | `pip install "napari-micromanager[pyqt6]"` |
>
> Packages are on [PyPI](<https://pypi.org/user/tlambert03/>) and [conda-forge](<https://anaconda.org/conda-forge/pymmcore-plus>). Python 3.10 or newer is required.

## 2\. Install the device adapters

The `mmcore` command (installed with the `cli` extra above) downloads the latest compatible Micro-Manager device adapters for your platform:

```sh
mmcore install
```

That's it: `CMMCorePlus` finds them automatically. For details (choosing a version, using an existing Micro-Manager installation, Linux, and what "device interface version" means) see [Micro-Manager device adapters](<https://pymmcore-plus.github.io/pymmcore-plus/install/index.md>).

> [!TIP]
>
> **Check your setup**
>
> ```sh
> mmcore info     # show versions and the active Micro-Manager installation
> mmcore bench    # run a quick benchmark with the demo devices
> ```

## Next steps

- : script the core
-
-
