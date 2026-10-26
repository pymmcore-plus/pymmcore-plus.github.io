# Your first GUI

There are two ways to get a graphical interface:

- **Use an application**: [pymmcore-gui](<#use-an-application>) or [napari-micromanager](<#use-an-application>).
- **Build your own** from [pymmcore-widgets](<https://pymmcore-plus.github.io/pymmcore-widgets/widgets/index.md>), a library of Qt widgets that control a `CMMCorePlus`.

## Use an application

```sh
pip install git+https://github.com/pymmcore-plus/pymmcore-gui
mmgui
```

Or download a [bundled app](<https://pymmcore-plus.github.io/pymmcore-gui/install/index.md>). See [Using pymmcore-gui](<https://pymmcore-plus.github.io/pymmcore-gui/usage/index.md>).

```sh
pip install "napari-micromanager[pyqt6]"
napari-micromanager
```

See [getting started with napari-micromanager](<https://pymmcore-plus.github.io/napari-micromanager/getting_started/index.md>).

## Build your own

Every widget in `pymmcore-widgets` connects to a `CMMCorePlus` instance (by default, the global `CMMCorePlus.instance()`), listens to its [events](<https://pymmcore-plus.github.io/pymmcore-plus/guides/events/index.md>), and stays in sync with the hardware — whether the change came from the widget, from another widget, or from your own code.

Install the widgets with a Qt backend:

```sh
pip install "pymmcore-widgets[PyQt6]"
```

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

1. Widgets use the global core by default. Pass `mmcore=...` to a widget to use a specific instance.

A slightly larger version of this example looks like this:

## Where next?

- The [widget gallery](<https://pymmcore-plus.github.io/pymmcore-widgets/widgets/index.md>) shows every widget, each with a screenshot and a runnable example.
- [Getting started with pymmcore-widgets](<https://pymmcore-plus.github.io/pymmcore-widgets/getting_started/index.md>) walks through a complete custom GUI.
- [Qt integration](<https://pymmcore-plus.github.io/pymmcore-plus/examples/integration-with-qt/index.md>) explains how to keep the GUI responsive while the hardware works.
