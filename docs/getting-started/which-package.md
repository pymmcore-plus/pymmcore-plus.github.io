---
title: Which Package Do I Need?
---

# Which Package Do I Need?

There are five packages here, each building on the ones below it (see the
[stack on the home page](../index.md#how-the-pieces-fit-together)).  Most people
only need one of them:

| If you want to&hellip; | Use | Start here |
| --- | --- | --- |
| Control a microscope with a point-and-click app | pymmcore-gui | [pymmcore-gui](../pymmcore-gui/index.md) |
| Control a microscope from inside [napari](https://napari.org) | napari-micromanager | [napari-micromanager](../napari-micromanager/index.md) |
| Script your microscope from Python or Jupyter | pymmcore-plus | [First steps](first-steps.md) |
| Run multi-dimensional acquisitions from code | pymmcore-plus (includes useq-schema) | [Your first acquisition](first-acquisition.md) |
| Describe experiments independently of any hardware | useq-schema | [Describing experiments](../useq-schema/index.md) |
| Build your own Qt GUI for a microscope | pymmcore-widgets | [Your first GUI](first-gui.md) |

(A *multi-dimensional acquisition*, or MDA, is a series of images across time
points, stage positions, channels, z-planes, etc...  It's what Micro-Manager's
Multi-D Acquisition window does.)

Installing a package also installs the ones it builds on (`pip install
pymmcore-widgets` gets you `pymmcore-plus`, `useq-schema` and `pymmcore` too).  The
Micro-Manager device adapters (the drivers for your hardware) are *not* Python
packages, though, and always need to be installed separately.
[Installation](install.md) covers both, so whichever package you pick, start there.

If you've used Micro-Manager before, you may also want to read
[Coming from Micro-Manager](from-micro-manager.md).

## What each package does

[pymmcore-plus](../pymmcore-plus/index.md)
:   Extends [`pymmcore`](https://github.com/micro-manager/pymmcore), the Python
    bindings for Micro-Manager's C++ core.
    [`CMMCorePlus`][pymmcore_plus.CMMCorePlus] aims to be a drop-in replacement
    for `CMMCore`, adding an event system, an acquisition engine written in Python,
    and a number of convenience methods.  It also provides the `mmcore` command
    line tool.

[useq-schema](../useq-schema/index.md)
:   A schema for describing multi-dimensional acquisitions
    ([`MDASequence`][useq.MDASequence], [`MDAEvent`][useq.MDAEvent]).  It *tries*
    to stay agnostic to the acquisition engine (though it was designed around what
    Micro-Manager can do).

[pymmcore-widgets](../pymmcore-widgets/widgets/index.md)
:   Qt widgets for a `CMMCorePlus`: property browsers, device controls,
    configuration editors, MDA editors, image previews, etc...

[pymmcore-gui](../pymmcore-gui/index.md)
:   A desktop application built from all of the above (plus the
    [ndv](https://github.com/pyapp-kit/ndv) viewer).  The goal is a pure-Python
    replacement for Micro-Manager's Java GUI.  It's still early days, so expect
    some rough edges.

[napari-micromanager](../napari-micromanager/index.md)
:   A napari plugin for controlling a microscope from the napari viewer.  It's
    still maintained, but current development is focused on pymmcore-gui.
