---
title: Which Package Do I Need?
---

# Which Package Do I Need?

These packages form a stack.  Each one builds on the ones below it, and installing
one installs all of the Python packages below it, so you only need to pick one:

``` mermaid
%% pymm:align-groups (see pymm.js)
graph TB
  subgraph py [Python]
    gui(pymmcore-gui)
    nmm(napari-micromanager)
    ndv(ndv)
    napari(napari)
    widgets(pymmcore-widgets)
    plus(pymmcore-plus)
    useq(useq-schema)
    omew(ome-writers)
    pyqt(PyQt / PySide)
    pymmcore(pymmcore)
  end
  subgraph cpp ["C++"]
    qt(Qt)
    core(MMCore)
    adapters("device adapters<br/>(cameras, stages, ...)")
  end
  gui --> ndv
  gui --> widgets
  nmm --> widgets
  nmm --> napari
  widgets --> pyqt
  widgets --> plus
  plus --> useq
  plus --> omew
  plus --> pymmcore
  pyqt -.-> qt
  pymmcore -.-> core
  core --> adapters
  classDef app fill:#7c3aed,stroke:#7c3aed,color:#fff
  classDef wid fill:#db2777,stroke:#db2777,color:#fff
  classDef lib fill:#3279b2,stroke:#3279b2,color:#fff
  classDef mm fill:#0d9488,stroke:#0d9488,color:#fff
  classDef ext fill:#6b7280,stroke:#6b7280,color:#fff
  style py rx:10px,ry:10px
  style cpp rx:10px,ry:10px
  class gui,nmm app
  class widgets wid
  class plus,useq,omew lib
  class pymmcore,core,adapters mm
  class ndv,napari,pyqt,qt ext
  click gui "../../pymmcore-gui/"
  click nmm "../../napari-micromanager/"
  click widgets "../../pymmcore-widgets/widgets/"
  click plus "../../pymmcore-plus/"
  click useq "../../useq-schema/"
  click omew "https://pymmcore-plus.github.io/ome-writers/" _blank
  click ndv "https://pyapp-kit.github.io/ndv/" _blank
  click napari "https://napari.org" _blank
  click pymmcore "https://github.com/micro-manager/pymmcore" _blank
  click core "https://github.com/micro-manager/mmCoreAndDevices" _blank
  click adapters "../install/#installing-the-device-adapters"
```

An arrow means "uses": `pymmcore-widgets` uses `pymmcore-plus`, which uses
`pymmcore` to talk to Micro-Manager's C++ core, which in turn talks to your hardware
through the device adapters.

(If you've used Micro-Manager before,
[Coming from Micro-Manager](from-micro-manager.md) maps what you know onto these
packages.)

## Applications

If you mainly want to work with your microscope through a GUI, start with one of
the two apps.  They're alternatives to each other, both built on the libraries
below.  Both can be scripted from Python while they're running, and pymmcore-gui
can be extended with your own widgets, so they're worth a look even if you write
code:

| App | What it is | Start here |
| --- | --- | --- |
| pymmcore-gui | A desktop application (our replacement for Micro-Manager's Java GUI, still early) | [pymmcore-gui](../pymmcore-gui/index.md) |
| napari-micromanager | Microscope control from inside [napari](https://napari.org) | [napari-micromanager](../napari-micromanager/index.md) |

## Libraries

If you want to write your own scripts or applications, pick the highest library you
need (it includes the ones below it):

| If you want to&hellip; | Use | Start here |
| --- | --- | --- |
| Build your own Qt GUI for a microscope | pymmcore-widgets | [Your first GUI](first-gui.md) |
| Script your microscope, or run multi-dimensional acquisitions | pymmcore-plus | [First steps](first-steps.md), then [Your first acquisition](first-acquisition.md) |
| Describe experiments without any hardware | useq-schema | [Describing experiments](../useq-schema/index.md) |

(A *multi-dimensional acquisition*, or MDA, is a series of images across time
points, stage positions, channels, z-planes, etc...  It's what Micro-Manager's
Multi-D Acquisition window does.)

## Installing

The Micro-Manager device adapters (the drivers for your hardware) are *not*
Python packages, so none of these install them for you.
[Installation](install.md) covers the packages and the adapters, so whichever one
you pick, start there.

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

[ome-writers](https://pymmcore-plus.github.io/ome-writers/)
:   Writes OME-Zarr and OME-TIFF files.  pymmcore-plus uses it to
    [save acquisitions](../pymmcore-plus/guides/saving_data.md), but it doesn't
    depend on Micro-Manager and can be used on its own.

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
