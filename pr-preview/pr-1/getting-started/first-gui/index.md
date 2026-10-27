# Your First GUI

You can either use one of the existing applications ([pymmcore-gui](<https://pymmcore-plus.github.io/pymmcore-gui/index.md>) or [napari-micromanager](<https://pymmcore-plus.github.io/napari-micromanager/index.md>)), or build your own from [pymmcore-widgets](<https://pymmcore-plus.github.io/pymmcore-widgets/widgets/index.md>), a library of Qt widgets for controlling a `CMMCorePlus`.

## Using an application

Once it's [installed](<https://pymmcore-plus.github.io/pymmcore-gui/install/index.md>) (from GitHub, or as a bundled app for Windows and macOS), start it with the demo devices:

```sh
mmgui run --demo-config
```

Without `--demo-config`, the app starts with no devices loaded. You can load a configuration from the **Devices** menu, or start with `mmgui -c path/to/config.cfg`. See [Using pymmcore-gui](<https://pymmcore-plus.github.io/pymmcore-gui/usage/index.md>) for more.

Once it's [installed](<https://pymmcore-plus.github.io/napari-micromanager/getting_started/index.md>), start it with:

```sh
napari-micromanager
```

Then pick a configuration file at the top left of the window (or start it with `napari-micromanager -c path/to/config.cfg`).

## Building your own

Widgets in `pymmcore-widgets` use the global `CMMCorePlus.instance()` by default (see the tip in [First steps](<https://pymmcore-plus.github.io/getting-started/first-steps/#connecting-to-events>)), and they listen to the core's [events](<https://pymmcore-plus.github.io/pymmcore-plus/guides/events/index.md>), so if you change something from a script (or from another widget), they'll update to match. (A few widgets don't use a core at all. The sequence editors, like `ChannelTable` and `MDASequenceWidget`, just edit `useq` objects.)

You'll need `pymmcore-widgets` and a Qt backend, PyQt6 or PySide6 (see [Installation](<https://pymmcore-plus.github.io/getting-started/install/#installing-the-packages>), and [PyQt6 or PySide6?](<https://pymmcore-plus.github.io/pymmcore-widgets/getting_started/#installing-a-qt-backend>) if you're not sure which). The examples here import Qt from [`qtpy`](<https://github.com/spyder-ide/qtpy>), so they run with either one.

Then combine widgets like any other Qt widgets:

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget

from pymmcore_widgets import (
    ChannelWidget,
    ExposureWidget,
    ImagePreview,
    LiveButton,
    SnapButton,
)

app = QApplication([])

core = CMMCorePlus.instance()  # (1)!
core.loadSystemConfiguration()

window = QWidget()
controls = QHBoxLayout()
controls.addWidget(ChannelWidget())
controls.addWidget(ExposureWidget())
controls.addWidget(SnapButton())
controls.addWidget(LiveButton())

layout = QVBoxLayout(window)
layout.addLayout(controls)
layout.addWidget(ImagePreview())
window.show()

app.exec()
```

1. This is the core the widgets below will use, so loading the configuration here is enough for all of them. Pass `mmcore=...` to a widget to use a different core (the `ConfigWizard` calls it `core=`).

A slightly larger version of this example ([`custom_gui.py`](<https://pymmcore-plus.github.io/pymmcore-widgets/getting_started/index.md>), which adds a configuration loader and a few more controls) looks like this:

## Next steps

The [widget gallery](<https://pymmcore-plus.github.io/pymmcore-widgets/widgets/index.md>) is the best place to find widgets for your own GUI (each one has a screenshot and a runnable example). [Building a custom GUI](<https://pymmcore-plus.github.io/pymmcore-widgets/getting_started/index.md>) walks through the larger example above, and [Qt integration](<https://pymmcore-plus.github.io/pymmcore-plus/examples/integration-with-qt/index.md>) explains how to keep the GUI responsive while the hardware is busy.
