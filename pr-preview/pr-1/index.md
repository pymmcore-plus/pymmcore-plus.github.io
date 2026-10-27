# pymmcore-plus

These docs cover `pymmcore-plus` and the packages built around it, which let you control a microscope from Python by talking directly to [Micro-Manager](<https://micro-manager.org>)'s C++ core and device adapters (with no Java process involved). You can use them to script your hardware and run multi-dimensional acquisitions, or to build your own GUI (or just use one of ours).

[Get started](<https://pymmcore-plus.github.io/getting-started/which-package/index.md>) [User guide](<https://pymmcore-plus.github.io/guide/index.md>)

```python
import useq
from pymmcore_plus import CMMCorePlus

core = CMMCorePlus()
core.loadSystemConfiguration()  # demo devices

sequence = useq.MDASequence(
    channels=["DAPI", "FITC"],
    time_plan={"interval": 1, "loops": 5},
)
core.mda.run(sequence, output="data.ome.zarr")
```

## Where to start

If you're new here, [Getting Started](<https://pymmcore-plus.github.io/getting-started/which-package/index.md>) walks you through installing things, controlling Micro-Manager's demo devices from Python, running a first acquisition, and putting together a small GUI (no microscope required). If you already know Micro-Manager, have a look at [Coming from Micro-Manager](<https://pymmcore-plus.github.io/getting-started/from-micro-manager/index.md>), which maps what you know onto these packages.

If you'd rather not write any code, [pymmcore-gui](<https://pymmcore-plus.github.io/pymmcore-gui/index.md>) is our (work in progress) desktop application, and [napari-micromanager](<https://pymmcore-plus.github.io/napari-micromanager/index.md>) controls a microscope from inside [napari](<https://napari.org>).

## How the pieces fit together

Each package builds on the ones below it. You only need to go as far up the stack as you want (`pymmcore-plus` on its own is enough to script a microscope).

Applications

[**pymmcore-gui**](<https://pymmcore-plus.github.io/pymmcore-gui/index.md>) · [**napari-micromanager**](<https://pymmcore-plus.github.io/napari-micromanager/index.md>)

Desktop applications for running a microscope.

Widgets

[**pymmcore-widgets**](<https://pymmcore-plus.github.io/pymmcore-widgets/widgets/index.md>)

Qt widgets for devices, properties, configurations and acquisitions.

Control &amp; acquisition

[**pymmcore-plus**](<https://pymmcore-plus.github.io/pymmcore-plus/index.md>) · [**useq-schema**](<https://pymmcore-plus.github.io/useq-schema/index.md>)

The core, extended with events and an acquisition engine, and a schema for describing experiments.

Micro-Manager

[**pymmcore**](<https://github.com/micro-manager/pymmcore>) · [device adapters](<https://pymmcore-plus.github.io/pymmcore-plus/install/index.md>)

The C++ core and drivers for hundreds of cameras, stages, shutters, lasers, etc...

Your microscope

Micro-Manager's demo devices, or your own hardware

## Getting help

If you have usage questions (*"How do I...?"*), please ask on the [image.sc forum](<https://forum.image.sc/tag/pymmcore-plus>) with the `pymmcore-plus` tag, or come chat with us on [Zulip](<https://imagesc.zulipchat.com/#narrow/channel/442785-pymmcore.5B-plus.5D>). Bug reports and feature requests are always welcome on [GitHub](<https://github.com/pymmcore-plus>) (each package has its own repository; see [Contributing](<https://pymmcore-plus.github.io/contributing/index.md>) if you're not sure which one).
