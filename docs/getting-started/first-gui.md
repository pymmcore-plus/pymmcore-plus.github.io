---
title: Your First GUI
---

# Your First GUI

You can either use one of the existing applications
([pymmcore-gui](../pymmcore-gui/index.md) or
[napari-micromanager](../napari-micromanager/index.md)), or build your own from
[pymmcore-widgets](../pymmcore-widgets/widgets/index.md), a library of Qt widgets
for controlling a `CMMCorePlus`.

## Using an application

=== "pymmcore-gui"

    Once it's [installed](../pymmcore-gui/install.md) (from GitHub, or as a
    bundled app for Windows and macOS), start it with the demo devices:

    ```sh
    mmgui run --demo-config
    ```

    Without `--demo-config`, the app starts with no devices loaded.  You can load
    a configuration from the **Devices** menu, or start with
    `mmgui -c path/to/config.cfg`.  See
    [Using pymmcore-gui](../pymmcore-gui/usage.md) for more.

=== "napari-micromanager"

    Once it's [installed](../napari-micromanager/getting_started.md), start it
    with:

    ```sh
    napari-micromanager
    ```

    Then pick a configuration file at the top left of the window (or start it
    with `napari-micromanager -c path/to/config.cfg`).

## Building your own

Widgets in `pymmcore-widgets` use the global
[`CMMCorePlus.instance()`][pymmcore_plus.CMMCorePlus.instance] by default (see the
tip in [First steps](first-steps.md#connecting-to-events)), and they listen to the
core's [events](../pymmcore-plus/guides/events.md), so if you change something from
a script (or from another widget), they'll update to match.  (A few widgets don't
use a core at all.  The sequence editors, like
[`ChannelTable`][pymmcore_widgets.ChannelTable] and
[`MDASequenceWidget`][pymmcore_widgets.MDASequenceWidget], just edit `useq`
objects.)

You'll need `pymmcore-widgets` and a Qt backend, PyQt6 or PySide6 (see
[Installation](install.md#installing-the-packages), and
[PyQt6 or PySide6?](../pymmcore-widgets/getting_started.md#installing-a-qt-backend)
if you're not sure which).  The examples here import Qt from
[`qtpy`](https://github.com/spyder-ide/qtpy), so they run with either one.

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

1.  This is the core the widgets below will use, so loading the configuration here
    is enough for all of them.  Pass `mmcore=...` to a widget to use a different
    core (the [`ConfigWizard`][pymmcore_widgets.ConfigWizard] calls it `core=`).

A slightly larger version of this example
([`custom_gui.py`](../pymmcore-widgets/getting_started.md), which adds a
configuration loader and a few more controls) looks like this:

![type:video](../pymmcore-widgets/images/my_widget.mp4){: style='width: 100%'}

## Next steps

The [widget gallery](../pymmcore-widgets/widgets/index.md) is the best place to
find widgets for your own GUI (each one has a screenshot and a runnable example).
[Building a custom GUI](../pymmcore-widgets/getting_started.md) walks through the
larger example above, and [Qt integration](../pymmcore-plus/examples/integration-with-qt.md)
explains how to keep the GUI responsive while the hardware is busy.
