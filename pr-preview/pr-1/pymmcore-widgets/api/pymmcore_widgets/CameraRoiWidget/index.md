# CameraRoiWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

A Widget to control the camera device ROI.

When the ROI changes, the `roiChanged` Signal is emitted with the current ROI (x, y, width, height, comboBoxText)

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget, by default None | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

Methods:

| Name | Description |
| --- | --- |
| `value` | Return the camera information dict. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `roiChanged` |  |  |
| `camera_combo` |  |  |
| `camera_roi_combo` |  |  |
| `start_x` |  |  |
| `start_y` |  |  |
| `roi_width` |  |  |
| `roi_height` |  |  |
| `center_checkbox` |  |  |
| `lbl_info` |  |  |
| `snap_checkbox` |  |  |
| `crop_btn` |  |  |
| `camera` | `str` |  |

## roiChanged

```python
roiChanged = Signal(int, int, int, int, str)
```

## camera\_combo

```python
camera_combo = QComboBox()
```

## camera\_roi\_combo

```python
camera_roi_combo = QComboBox()
```

## start\_x

```python
start_x = QSpinBox()
```

## start\_y

```python
start_y = QSpinBox()
```

## roi\_width

```python
roi_width = QSpinBox()
```

## roi\_height

```python
roi_height = QSpinBox()
```

## center\_checkbox

```python
center_checkbox = QCheckBox(text='center ROI')
```

## lbl\_info

```python
lbl_info = QLabel('....')
```

## snap\_checkbox

```python
snap_checkbox = QCheckBox(text='Auto Snap')
```

## crop\_btn

```python
crop_btn = QPushButton('Crop')
```

## camera

```python
camera: str
```

## value

```python
value() -> dict[str, CameraInfo]
```

Return the camera information dict.

## Example

examples/camera\_roi\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import CameraRoiWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

# this widget supports multiple camera devices
mmc.loadDevice("Camera2", "DemoCamera", "DCam")
mmc.initializeDevice("Camera2")

cam_roi_wdg = CameraRoiWidget()
cam_roi_wdg.show()

app.exec()
```
