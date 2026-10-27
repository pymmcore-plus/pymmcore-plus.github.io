# SnapButton

Screenshot generated from the [example below](<#example>).

## Example

examples/snap\_button.py

```python
"""Example usage of the SnapButton class.

Check also the 'image_preview.py' example to see the SnapButton
used in combination of other widgets.
"""

from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import SnapButton

app = QApplication([])

mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

snap_btn = SnapButton()
snap_btn.show()

app.exec()
```

## API

Bases: `QPushButton`

Button that snaps an image with the current camera.

Clicking it calls `CMMCorePlus.snap` in a separate thread (so the GUI stays responsive), which emits the `imageSnapped` event. If live mode is running, it is stopped first.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |
| `See` |  |  | *required* |
| `widget` |  |  | *required* |
