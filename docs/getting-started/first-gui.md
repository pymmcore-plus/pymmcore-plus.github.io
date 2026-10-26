---
title: Your first GUI
---

# Your first GUI

There are two ways to get a graphical interface:

- **Use an application**: [pymmcore-gui](#use-an-application) or
  [napari-micromanager](#use-an-application).
- **Build your own** from [pymmcore-widgets](../pymmcore-widgets/widgets/index.md),
  a library of Qt widgets that control a `CMMCorePlus`.

## Use an application

=== "pymmcore-gui"

    ```sh
    pip install git+https://github.com/pymmcore-plus/pymmcore-gui
    mmgui
    ```

    Or download a [bundled app](../pymmcore-gui/install.md).  See
    [Using pymmcore-gui](../pymmcore-gui/usage.md).

=== "napari-micromanager"

    ```sh
    pip install "napari-micromanager[pyqt6]"
    napari-micromanager
    ```

    See [getting started with napari-micromanager](../napari-micromanager/getting_started.md).

## Build your own

Every widget in `pymmcore-widgets` connects to a `CMMCorePlus` instance (by
default, the global [`CMMCorePlus.instance()`][pymmcore_plus.CMMCorePlus.instance]),
listens to its [events](../pymmcore-plus/guides/events.md), and stays in sync with
the hardware &mdash; whether the change came from the widget, from another
widget, or from your own code.

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

1.  Widgets use the global core by default.  Pass `mmcore=...` to a widget to use
    a specific instance.

A slightly larger version of this example looks like this:

![type:video](../pymmcore-widgets/images/my_widget.mp4){: style='width: 100%'}

## Where next?

- The [widget gallery](../pymmcore-widgets/widgets/index.md) shows every widget,
  each with a screenshot and a runnable example.
- [Getting started with pymmcore-widgets](../pymmcore-widgets/getting_started.md)
  walks through a complete custom GUI.
- [Qt integration](../pymmcore-plus/examples/integration-with-qt.md) explains how
  to keep the GUI responsive while the hardware works.
