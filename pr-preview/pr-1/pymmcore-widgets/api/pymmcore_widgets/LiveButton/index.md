# LiveButton

Screenshot generated from the [example below](<#example>).

## Example

examples/live\_button.py

```python
"""Example usage of the LiveButton class.

Check also the 'image_preview.py' example to see the LiveButton
used in combination of other widgets.
"""

from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import LiveButton

app = QApplication([])

mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

live_btn = LiveButton()
live_btn.show()

app.exec()
```

## API

Bases: `QPushButton`

Button that starts and stops live mode.

When pressed, a continuous sequence acquisition is started or stopped and a pymmcore-plus signal `continuousSequenceAcquisitionStarted` or `sequenceAcquisitionStopped` is emitted.

See the `ImagePreview` example for this widget combined with an image preview and other controls.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

### button\_text\_on

```python
button_text_on: str
```

Set the live button text for when live mode is on.

Default = "Live."

### button\_text\_off

```python
button_text_off: str
```

Set the live button text for when live mode is off.

Default = "Stop."

### icon\_color\_on

```python
icon_color_on: COLOR_TYPE
```

Set the live button color for when live mode is on.

Default = (0. 255, 0).

### icon\_color\_off

```python
icon_color_off: COLOR_TYPE
```

Set the live button color for when live mode is off.

Default = "magenta".
