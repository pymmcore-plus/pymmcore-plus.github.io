# pymmcore-widgets

[pymmcore-widgets](<https://github.com/pymmcore-plus/pymmcore-widgets>) is a library of Qt widgets for [pymmcore-plus](<https://pymmcore-plus.github.io/pymmcore-plus/index.md>), meant for building your own microscope GUI in Python. There are widgets for most of the things you do at the microscope (channels, exposure, stages, device properties, configuration groups, snapping and live mode, multi-dimensional acquisitions) and for setting it up (the Hardware Configuration Wizard, pixel sizes, installing device adapters). Most of them control a `CMMCorePlus` and follow its [events](<https://pymmcore-plus.github.io/pymmcore-plus/guides/events/index.md>), so they stay in sync with each other and with your own code. They are also the building blocks of [pymmcore-gui](<https://pymmcore-plus.github.io/pymmcore-gui/index.md>) and [napari-micromanager](<https://pymmcore-plus.github.io/napari-micromanager/index.md>).

A few widgets in one window (the code is the [StageExplorer example](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/StageExplorer/#example>)).

## Where to start

- [Your first GUI](<https://pymmcore-plus.github.io/getting-started/first-gui/index.md>) puts a few of them together in a window.
- The [widget gallery](<https://pymmcore-plus.github.io/pymmcore-widgets/widgets/index.md>) shows each widget with a screenshot, and links to its page with a runnable example and the API.
- [Building a custom GUI](<https://pymmcore-plus.github.io/pymmcore-widgets/getting_started/index.md>) covers choosing a Qt backend, how widgets find their core, and a larger example.
- [Qt integration](<https://pymmcore-plus.github.io/pymmcore-plus/examples/integration-with-qt/index.md>) explains how pymmcore-plus and Qt work together (and how to keep your GUI responsive).

## API reference

Import widgets from the top-level package:

```python
from pymmcore_widgets import MDAWidget, PropertyBrowser, StageWidget
```

Each of these has its own page (listed under `pymmcore_widgets` in the sidebar, and in the [gallery](<https://pymmcore-plus.github.io/pymmcore-widgets/widgets/index.md>)). A few more specialized widgets live in submodules: the sequence editors' building blocks in [`pymmcore_widgets.useq_widgets`](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/useq_widgets/index.md>) (for example `WellPlateWidget` and `PointsPlanWidget`), and `StackViewer` in `pymmcore_widgets.experimental`.
