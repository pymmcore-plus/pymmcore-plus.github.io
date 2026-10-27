---
title: Coming from Micro-Manager
---

# Coming from Micro-Manager

If you've used Micro-Manager's Java application (MMStudio), much of what you know
carries over.  `pymmcore-plus` uses the same C++ core (`MMCore`) and the same
device adapters as MMStudio, and it reads the same configuration files.  What's
different is everything above the core.  In place of MMStudio's Java GUI and
acquisition engine, you get a Python object
([`CMMCorePlus`][pymmcore_plus.CMMCorePlus]), an acquisition engine written in
Python, and (if you want a GUI) widgets and applications written in Python.

## One program at a time

`pymmcore-plus` doesn't connect to a running copy of Micro-Manager; it *replaces*
it.  Each program loads its own copy of the core, and the core opens your devices
itself (serial ports, camera drivers, etc...).  Most devices can only be opened by
one program at a time, so if MMStudio has your configuration loaded, loading it
again from Python will usually fail (and if it doesn't, the two programs will be
fighting over the same hardware).  So please close MMStudio before you load your
configuration in Python, and vice versa.  (The demo devices don't mind, so it's
fine to have both open while you're trying things out.)

If you want to keep using MMStudio *and* control it from Python at the same time,
that's what Pycro-Manager is for (see [below](#how-is-this-different-from-pycro-manager)).

## Where things went

| In MMStudio | Here |
| --- | --- |
| Hardware Configuration Wizard and `.cfg` files | The same files: `core.loadSystemConfiguration("MyScope.cfg")`.  See [Using your own microscope](../guide/own-microscope.md). |
| Device Property Browser | `core.getProperty()` and `core.setProperty()`, or the [`PropertyBrowser`][pymmcore_widgets.PropertyBrowser] widget |
| Groups and presets (main window) | `core.setConfig("Channel", "FITC")`, or [`GroupPresetTableWidget`][pymmcore_widgets.GroupPresetTableWidget] |
| Snap and Live | `core.snap()` and `core.startContinuousSequenceAcquisition()`, or [`SnapButton`][pymmcore_widgets.SnapButton] and [`LiveButton`][pymmcore_widgets.LiveButton] |
| Multi-D Acquisition window | Describe the experiment with a [`useq.MDASequence`][useq.MDASequence] and run it with `core.mda.run()` (see [Your first acquisition](first-acquisition.md)), or use the [`MDAWidget`][pymmcore_widgets.MDAWidget] |
| Stage Position List | `stage_positions` in an `MDASequence` |
| Saving acquisitions | `core.mda.run(sequence, output="data.ome.zarr")` (or `.ome.tiff`).  See [Saving data](../pymmcore-plus/guides/saving_data.md). |
| Pixel Size Calibration | The same pixel size presets in your `.cfg` file (`core.getPixelSizeUm()`), or the [`PixelConfigurationWidget`][pymmcore_widgets.PixelConfigurationWidget] |
| Script panel (Beanshell) | Python (see [below](#scripts)) |
| Device adapters (the `mmgr_dal_*` files) | The very same files.  `mmcore install` downloads them for you. |

If you'd rather have all of this in one window, [pymmcore-gui](../pymmcore-gui/index.md)
is our (work in progress) pure-Python replacement for MMStudio.

## Scripts

`CMMCorePlus` has the same methods as the core object (`mmc`) in MMStudio's script
panel, so Beanshell scripts translate to Python almost line by line:

=== "Beanshell (MMStudio)"

    ```java
    mmc.setConfig("Channel", "FITC");
    mmc.setExposure(50);
    mmc.snapImage();
    img = mmc.getImage();
    ```

=== "Python"

    ```python
    from pymmcore_plus import CMMCorePlus

    mmc = CMMCorePlus.instance()
    mmc.loadSystemConfiguration()  # (1)!
    mmc.setConfig("Channel", "FITC")
    mmc.setExposure(50)
    mmc.snapImage()
    img = mmc.getImage()  # a numpy array
    ```

    1.  MMStudio had already done this for you.  Pass the path to your own
        `.cfg` file (with no argument, this loads the demo devices).

A few things are different: images come back as numpy arrays (rather than Java
arrays), lists of strings come back as Python tuples (rather than `StrVector`s),
and `CMMCorePlus` adds a number of conveniences on top (like `snap()`, which does
the last two lines in one go).  The `mm` object (MMStudio's own API for displays,
data stores, the acquisition manager, etc...) is part of the Java GUI, so it has no
equivalent here.

If you're working inside one of our applications, the core is already there for
you.  In [pymmcore-gui](../pymmcore-gui/index.md)'s console it's called `mmc`
(just like in MMStudio), and in
[napari-micromanager](../napari-micromanager/index.md)'s console it's `mmcore`.

## How is this different from Pycro-Manager?

A common question about `pymmcore-plus` and related libraries is how they differ
from [Pycro-Manager](https://github.com/micro-manager/pycro-manager), another
Python library written by Henry Pinkard for working with Micro-Manager.

The two projects are not mutually exclusive!  They aim to support different use
cases.

The primary difference is that Pycro-Manager (with its default Java backend)
controls Micro-Manager via a ZMQ-based connection to a remote Java process in
which the Micro-Manager GUI is running (or a headless Java process if the GUI is
not running).  The Java process in turn communicates with the C++ core driving the
hardware.

`pymmcore-plus` aims to remove the need for a Java process by communicating
directly with the C++ core (via the
[`pymmcore`](https://github.com/micro-manager/pymmcore) library), and
re-implementing any necessary event-based or GUI-based functionality in pure
Python or C.

A major advantage of Pycro-Manager is that you get the entire Java-based
Micro-Manager ecosystem, including the GUI and plugins.  A potential disadvantage
(depending on your needs) is that it requires a Java runtime environment and
cross-process communication.

(Pycro-Manager has since added a
[Python backend](https://pycro-manager.readthedocs.io/en/latest/backends.html) for
its headless mode, which also runs the core inside the Python process via
`pymmcore`, along with a Python version of its acquisition engine.  It's a
separate project from `pymmcore-plus`, with its own API.)

If you are looking to control a microscope via Python without any need for Java or
interprocess communication, `pymmcore-plus` may help.  Note, however, that you will
be sacrificing the MMStudio GUI!  See [pymmcore-gui](../pymmcore-gui/index.md),
[napari-micromanager](../napari-micromanager/index.md) and
[pymmcore-widgets](../pymmcore-widgets/widgets/index.md) for our ongoing efforts to
implement a complete Python-based GUI for Micro-Manager.

If you've been using Pycro-Manager and like its API, see
[A Pycro-Manager-style API](../pymmcore-plus/examples/pycro-manager-api.md) for an
example of what that could look like on top of `pymmcore-plus`.
