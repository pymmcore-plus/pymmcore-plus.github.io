# Control microscopes with Python

A set of Python packages for running a microscope through [Micro-Manager](<https://micro-manager.org>)'s C++ core and device adapters, with no Java process involved. Script your hardware, run multi-dimensional acquisitions, build your own GUI, or just use one of ours.

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

- **Script a microscope**

  ---

  Load a configuration, move stages, snap images, and connect callbacks to changes in the core, from a script or a notebook.
- **Run acquisitions**

  ---

  Describe time-lapses, z-stacks, channels and positions with `useq`, run them with an acquisition engine you can customize, and save to OME-Zarr or OME-TIFF.
- **Build a GUI**

  ---

  Combine Qt widgets (property browsers, stage controls, MDA editors, image previews, etc...) into your own application.
- **Just use an app**

  ---

  Point-and-click microscope control with `pymmcore-gui`, or inside napari with `napari-micromanager`.

[Getting Started](<https://pymmcore-plus.github.io/getting-started/which-package/index.md>) goes through these in order, using Micro-Manager's demo devices (no microscope required). If you already know Micro-Manager, [Coming from Micro-Manager](<https://pymmcore-plus.github.io/getting-started/from-micro-manager/index.md>) maps what you know onto these packages.

## How the pieces fit together

Each package builds on the ones below it. You only need to go as far up the stack as you want (`pymmcore-plus` on its own is enough to script a microscope).

Applications

[**pymmcore-gui**](<https://pymmcore-plus.github.io/pymmcore-gui/index.md>) · [**napari-micromanager**](<https://pymmcore-plus.github.io/napari-micromanager/index.md>)

Desktop applications for running a microscope.

Widgets

[**pymmcore-widgets**](<https://pymmcore-plus.github.io/pymmcore-widgets/widgets/index.md>)

Qt widgets for devices, properties, configurations and acquisitions.

Control &amp; acquisition

[**pymmcore-plus**](<https://pymmcore-plus.github.io/pymmcore-plus/index.md>) · [**useq-schema**](<https://pymmcore-plus.github.io/useq-schema/index.md>) · [**ome-writers**](<https://pymmcore-plus.github.io/ome-writers/>)

The core, extended with events and an acquisition engine, a schema for describing experiments, and writers for OME-Zarr and OME-TIFF.

Micro-Manager

[**pymmcore**](<https://github.com/micro-manager/pymmcore>) · [device adapters](<https://pymmcore-plus.github.io/pymmcore-plus/install/index.md>)

The C++ core and drivers for hundreds of cameras, stages, shutters, lasers, etc...

Your microscope

Micro-Manager's demo devices, or your own hardware

## Community

- **Ask a question** on the [image.sc forum](<https://forum.image.sc/tag/pymmcore-plus>)
- **Chat with developers** on [Zulip](<https://imagesc.zulipchat.com/#narrow/channel/442785-pymmcore.5B-plus.5D>)
- **Report a bug or request a feature** on [GitHub](<https://github.com/pymmcore-plus>)
