# ImagePreview

Screenshot generated from the [example below](<#example>).

## Example

examples/image\_preview.py

```python
"""ImagePreview shows the latest image from the core (snapped or live).

Here it's combined with a few other widgets into a minimal "snap and live" window.
"""

from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication, QGroupBox, QHBoxLayout, QVBoxLayout, QWidget

from pymmcore_widgets import (
    ChannelWidget,
    ExposureWidget,
    ImagePreview,
    LiveButton,
    SnapButton,
)


class ImageFrame(QWidget):
    """An example widget with a snap/live button and an image preview."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.preview = ImagePreview()
        self.snap_button = SnapButton()
        self.live_button = LiveButton()
        self.exposure = ExposureWidget()
        self.channel = ChannelWidget()

        self.setLayout(QVBoxLayout())

        buttons = QGroupBox()
        buttons.setLayout(QHBoxLayout())
        buttons.layout().addWidget(self.snap_button)
        buttons.layout().addWidget(self.live_button)

        ch_exp = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        ch_exp.setLayout(layout)

        ch = QGroupBox()
        ch.setTitle("Channel")
        ch.setLayout(QHBoxLayout())
        ch.layout().setContentsMargins(0, 0, 0, 0)
        ch.layout().addWidget(self.channel)
        layout.addWidget(ch)

        exp = QGroupBox()
        exp.setTitle("Exposure")
        exp.setLayout(QHBoxLayout())
        exp.layout().setContentsMargins(0, 0, 0, 0)
        exp.layout().addWidget(self.exposure)
        layout.addWidget(exp)

        self.layout().addWidget(self.preview)
        self.layout().addWidget(ch_exp)
        self.layout().addWidget(buttons)


if __name__ == "__main__":
    app = QApplication([])
    mmc = CMMCorePlus.instance()
    mmc.loadSystemConfiguration()
    frame = ImageFrame()
    frame.show()
    mmc.snap()
    app.exec()
```

## API

Bases: `QWidget`

A Widget that displays the latest image from the core.

This widget will automatically update when the active core snaps an image, when the active core starts streaming or when a Multi-Dimensional Acquisition is running.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget. By default, None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |
| `use_with_mda` | `bool` | If False, the widget will not update when a Multi-Dimensional Acquisition is running. By default, True. | `True` |

### use\_with\_mda

```python
use_with_mda: bool
```

Get whether the widget should update when a MDA is running.

### clims

```python
clims: tuple[float, float] | Literal['auto']
```

Get the contrast limits of the image.

### cmap

```python
cmap: str
```

Get the colormap (lookup table) of the image.
