# StageWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

A Widget to control a XY and/or a Z stage.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device` | `str` | Stage device. | *required* |
| `levels` | `int` | Number of "arrow" buttons per widget per direction, by default, 2. | `2` |
| `absolute_positioning` | `bool` | If True, the position displays can be edited to set absolute positions. If False, the position displays cannot be edited. | `False` |
| `position_label_below` | `bool` | If True, the position displays will appear below the move buttons. If False, the position displays will appear to the right of the move buttons. | `True` |
| `parent` | `QWidget \| None` | Optional parent widget. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

Methods:

| Name | Description |
| --- | --- |
| `step` | Return the current step size. |
| `setStep` | Set the step size. |
| `enable_absolute_positioning` | Toggles whether the position spinboxes can be edited by the user. |
| `timerEvent` |  |
| `eventFilter` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `BTN_SIZE` |  |  |
| `snap_checkbox` |  |  |

## BTN\_SIZE

```python
BTN_SIZE = 30
```

## snap\_checkbox

```python
snap_checkbox = QCheckBox(text='Snap on Click')
```

## step

```python
step() -> float
```

Return the current step size.

## setStep

```python
setStep(step: float) -> None
```

Set the step size.

## enable\_absolute\_positioning

```python
enable_absolute_positioning(enabled: bool) -> None
```

Toggles whether the position spinboxes can be edited by the user.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `enabled` | `bool` | If True, the position spinboxes will be enabled for user editing. If False, the position spinboxes will be disabled for user editing. | *required* |

## timerEvent

```python
timerEvent(event: QTimerEvent | None) -> None
```

## eventFilter

```python
eventFilter(obj: QObject | None, event: QEvent | None) -> bool
```

## Example

examples/stage\_widget.py

```python
"""Example usage of the StageWidget class.

In this example all the devices of type 'Stage' and 'XYStage' that are loaded
in micromanager are displayed with a 'StageWidget'.
"""

from pymmcore_plus import CMMCorePlus, DeviceType
from qtpy.QtWidgets import QApplication, QGroupBox, QHBoxLayout, QWidget

from pymmcore_widgets import StageWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

wdg = QWidget()
wdg_layout = QHBoxLayout(wdg)

stages = list(mmc.getLoadedDevicesOfType(DeviceType.XYStage))
stages.extend(mmc.getLoadedDevicesOfType(DeviceType.Stage))
for stage in stages:
    lbl = "Z" if mmc.getDeviceType(stage) == DeviceType.Stage else "XY"
    bx = QGroupBox(f"{lbl} Control")
    bx_layout = QHBoxLayout(bx)
    bx_layout.setContentsMargins(0, 0, 0, 0)
    bx_layout.addWidget(StageWidget(device=stage, position_label_below=True))
    wdg_layout.addWidget(bx)


wdg.show()
app.exec()
```
