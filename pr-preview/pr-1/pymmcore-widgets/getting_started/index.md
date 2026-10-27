# Building a Custom GUI

The widgets in `pymmcore-widgets` are ordinary `QWidget`s that control a `CMMCorePlus`, so you can arrange them with Qt layouts like any other widget. [Your first GUI](<https://pymmcore-plus.github.io/getting-started/first-gui/index.md>) puts a few of them in a window. This page covers the things you'll want to know once you start building something bigger: which Qt to install, how widgets find their core, and a larger example.

## Installing a Qt backend

`pymmcore-widgets` does *not* install Qt for you, so you choose the Qt backend with an extra:

```sh
pip install "pymmcore-widgets[PyQt6]"
# or
pip install "pymmcore-widgets[PySide6]"
```

(Keep the quotes. In zsh, the default shell on macOS, the square brackets otherwise cause a "no matches found" error.) You'll also need Python 3.11 or newer, and the Micro-Manager device adapters (see [Installation](<https://pymmcore-plus.github.io/getting-started/install/index.md>)).

> [!NOTE]
>
> **PyQt6 or PySide6?**
>
> Qt is the C++ toolkit the widgets are drawn with, and PyQt6 and PySide6 are two sets of Python bindings for it. The widgets work with (and are tested on) both, on macOS and Windows. The main difference is the license. PyQt6 is GPL (or commercial), and PySide6 is LGPL. That matters if you distribute your GUI, for example as a bundled application. If you don't have a reason to choose, PyQt6 is a fine default (it's what [pymmcore-gui](<https://pymmcore-plus.github.io/pymmcore-gui/index.md>) uses).
>
> We no longer test PyQt5 or PySide2 (and PySide2 can't be installed on Python 3.11 or newer).

The widgets import Qt through [qtpy](<https://github.com/spyder-ide/qtpy>), which is installed with `pymmcore-widgets`. qtpy provides one API (`from qtpy.QtWidgets import QApplication`) on top of whichever binding is installed, and the examples on this site use it too. If you write your own code against qtpy as well, it will run with either backend. (If both are installed in the same environment, qtpy picks PyQt6; set the environment variable `QT_API=pyside6` to use PySide6.)

## Basic usage

For a basic use of any of the widgets, we need to:

1. create a Qt application (`QApplication`);
2. create a Micro-Manager core instance so that all the widgets will control the same core;
3. load a configuration file;
4. create and show the widget(s) we want.

The order of the first two steps matters. Create the `QApplication` before the core (see [Qt integration](<https://pymmcore-plus.github.io/pymmcore-plus/examples/integration-with-qt/index.md>) for why).

In this example, we replace step 3 with the ConfigurationWidget, which lets us load any Micro-Manager configuration file. We also add the GroupPresetTableWidget, which shows the configuration groups and presets stored in the configuration file:

basic\_usage.py

```python
# import the necessary packages
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ConfigurationWidget, GroupPresetTableWidget

# create a QApplication
app = QApplication([])

# create a CMMCorePlus instance.
mmc = CMMCorePlus.instance()

# create a ConfigurationWidget
cfg_widget = ConfigurationWidget()

# create a GroupPresetTableWidget
gp_widget = GroupPresetTableWidget()

# show the created widgets
cfg_widget.show()
gp_widget.show()

app.exec()
```

The code above will create a Qt application with the `ConfigurationWidget` and the `GroupPresetTableWidget`:

## Choosing a core

By default, most widgets use the global singleton core, `CMMCorePlus.instance()`, and create it if it doesn't exist yet. This means that all the widgets in your GUI control the same core without you connecting anything, and so does any other code that calls `CMMCorePlus.instance()`. (So in the example above, the `mmc = CMMCorePlus.instance()` line isn't strictly necessary. Without it, the `ConfigurationWidget` would create the core.)

If you need a specific core instead, create it first and pass it to each widget as the `mmcore` argument, for example `GroupPresetTableWidget(mmcore=my_core)`. A few widgets are different:

- The sequence editors (`MDASequenceWidget`, `ChannelTable`, `PositionTable`, `TimePlanWidget`, `ZPlanWidget` and `GridPlanWidget`) don't use a core at all. They edit `useq` objects. Read the result with `value()`, set it with `setValue()`, and connect to `valueChanged`. `MDAWidget` is the sequence editor that *is* connected to a core (and can run the acquisition).
- `ConfigWizard` calls the argument `core`, not `mmcore`.
- `ConfigGroupsEditor` and `ConfigGroupsTree` are built from a core with `create_from_core(core)`, and don't follow it afterwards.
- `InstallWidget` installs device adapters and doesn't need a core.

## Custom GUI

The widgets are ordinary `QWidget`s, so building a custom GUI with them is mostly a matter of Qt layouts. If you're new to Qt, the [Qt for Python tutorials](<https://doc.qt.io/qtforpython-6/tutorials/index.html>) are a good place to start. Here, we only give a simple example of a custom GUI built from some of the `pymmcore-widgets`.

We create a [Qt application](<https://doc.qt.io/qt-6/qapplication.html>) with a general-purpose [QWidget](<https://doc.qt.io/qt-6/qwidget.html>) that incorporates a variety of `pymmcore-widgets`: ConfigurationWidget, ChannelGroupWidget, ChannelWidget, DefaultCameraExposureWidget, ImagePreview, SnapButton, and LiveButton.

This simple GUI can be used to load a Micro-Manager configuration file, snap an image or stream images from the camera, with the flexibility to select a channel and adjust the exposure time:

custom\_gui.py

```python
# Import the necessary packages
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QGridLayout, QWidget

from pymmcore_widgets import (
    ChannelGroupWidget,
    ChannelWidget,
    ConfigurationWidget,
    DefaultCameraExposureWidget,
    ImagePreview,
    LiveButton,
    SnapButton,
)


# Create a QWidget class named MyWidget
class MyWidget(QWidget):
    """An example QWidget that uses some of the widgets in pymmcore_widgets."""

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent=parent)

        # This is not strictly necessary but we can create a Micro-Manager core
        # instance so that all the widgets can control the same core. If you don't
        # create a core instance, the first widget to be instantiated will create
        # a new core instance.
        CMMCorePlus.instance()

        # Create the wanted pymmcore_widgets
        cfg = ConfigurationWidget()
        ch_group_combo = ChannelGroupWidget()
        ch_combo = ChannelWidget()
        exp = DefaultCameraExposureWidget()
        preview = ImagePreview()
        snap = SnapButton()
        live = LiveButton()

        # Create the layout for MyWidget
        # In Qt, a `layout` (https://doc.qt.io/qt-6/layout.html) is used to add
        # widgets to a `QWidget`. For this example, we'll employ a
        # `QGridLayout` (https://doc.qt.io/qt-6/qgridlayout.html) to organize the
        # widgets in a grid-like arrangement.
        layout = QGridLayout(self)

        # Add the wanted pymmcore_widgets to the layout.
        # The first two arguments of 'addWidget' specify the grid position
        # in terms of rows and columns. The third and fourth arguments
        # define the span of the widget across multiple rows and columns.
        layout.addWidget(cfg, 0, 0, 1, 3)
        layout.addWidget(ch_group_combo, 1, 0)
        layout.addWidget(ch_combo, 1, 1)
        layout.addWidget(exp, 1, 2)
        layout.addWidget(preview, 2, 0, 1, 3)
        layout.addWidget(snap, 3, 1)
        layout.addWidget(live, 3, 2)


# Create a QApplication and show MyWidget
if __name__ == "__main__":
    from qtpy.QtWidgets import QApplication

    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()
```

Running it (and loading a configuration) looks like this:

## Next steps

The [widget gallery](<https://pymmcore-plus.github.io/pymmcore-widgets/widgets/index.md>) lists the other widgets you can add, each with an example. If you'd rather start from a ready-made application, see [pymmcore-gui](<https://pymmcore-plus.github.io/pymmcore-gui/index.md>) (which you can also extend with your own widgets) or [napari-micromanager](<https://pymmcore-plus.github.io/napari-micromanager/index.md>).
