# ExposureWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

A Widget to get/set exposure on a camera.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `camera` | `str` | The camera device label. By default, None. If not specified, the widget will use the current Camera device. | `None` |
| `parent` | `QWidget \| None` | Optional parent widget. By default, None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance()`. | `None` |

Examples:

> [!NOTE]
>
> **Combining `ExposureWidget` with other widgets**
>
> see [ImagePreview](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ImagePreview/#example>)

Methods:

| Name | Description |
| --- | --- |
| `setCamera` | Set which camera this widget tracks. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `label` |  |  |
| `spinBox` |  |  |

## label

```python
label = QLabel()
```

## spinBox

```python
spinBox = QDoubleSpinBox()
```

## setCamera

```python
setCamera(camera: str | None = None) -> None
```

Set which camera this widget tracks.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `camera` | `str` | The camera device label. By default, None. If not specified, the widget will use the current Camera device. | `None` |

## Example

examples/exposure\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ExposureWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

exp_wdg = ExposureWidget()
exp_wdg.show()

app.exec()
```
