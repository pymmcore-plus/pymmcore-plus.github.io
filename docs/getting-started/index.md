---
title: Which package do I need?
---

# Which package do I need?

The pymmcore-plus ecosystem is a set of packages that build on each other.
Most people need just one or two of them:

| If you want to&hellip; | Use | Start here |
| --- | --- | --- |
| Control a microscope with a point-and-click app | **pymmcore-gui** | [Applications](../pymmcore-gui/index.md) |
| Control a microscope from inside [napari](https://napari.org) | **napari-micromanager** | [napari-micromanager](../napari-micromanager/index.md) |
| Script your microscope from Python or Jupyter | **pymmcore-plus** | [First steps](first-steps.md) |
| Run multi-dimensional acquisitions from code | **pymmcore-plus** + **useq-schema** | [Your first acquisition](first-acquisition.md) |
| Describe experiments in a hardware-agnostic way | **useq-schema** | [Describing experiments](../useq-schema/schema/sequence.md) |
| Build your own Qt GUI for a microscope | **pymmcore-widgets** | [Your first GUI](first-gui.md) |

``` mermaid
graph BT
  hw[Your hardware] --> mm["Micro-Manager device adapters<br/>(C++, via pymmcore)"]
  mm --> plus[pymmcore-plus]
  useq[useq-schema] --> plus
  plus --> widgets[pymmcore-widgets]
  widgets --> gui[pymmcore-gui]
  widgets --> napari[napari-micromanager]
  click plus "../pymmcore-plus/"
  click useq "../useq-schema/"
  click widgets "../pymmcore-widgets/widgets/"
  click gui "../pymmcore-gui/"
  click napari "../napari-micromanager/"
```

Installing a package also installs everything it builds on: `pymmcore-widgets`
brings in `pymmcore-plus`, which brings in `useq-schema` and `pymmcore`.  The one
thing you always need to install separately is the set of **Micro-Manager device
adapters** (the drivers for your hardware) &mdash; see
[Installation](install.md).

## What each package does

[pymmcore-plus](../pymmcore-plus/index.md)
:   The foundation.  [`CMMCorePlus`][pymmcore_plus.CMMCorePlus] is a drop-in
    replacement for Micro-Manager's `CMMCore` with a Pythonic API, an event
    system, and a flexible acquisition engine.  Also includes the `mmcore`
    command line tool.

[useq-schema](../useq-schema/index.md)
:   A hardware-agnostic schema for multi-dimensional experiments
    ([`MDASequence`][useq.MDASequence], [`MDAEvent`][useq.MDAEvent]).  Not
    specific to Micro-Manager: any acquisition engine can consume it.

[pymmcore-widgets](../pymmcore-widgets/widgets/index.md)
:   Qt widgets that control a `CMMCorePlus` instance: device and property
    controls, configuration editors, MDA editors, image previews, and more.

[pymmcore-gui](../pymmcore-gui/index.md)
:   A complete desktop application combining all of the above (plus the
    [ndv](https://github.com/pyapp-kit/ndv) viewer).

[napari-micromanager](../napari-micromanager/index.md)
:   A napari plugin providing microscope control inside the napari viewer.
