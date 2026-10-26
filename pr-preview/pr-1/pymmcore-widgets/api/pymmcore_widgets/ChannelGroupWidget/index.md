# ChannelGroupWidget

Screenshot generated from the [example below](<#example>).

Bases: `QComboBox`

A QComboBox to follow and control Micro-Manager ChannelGroup.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget. By default, None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

## Example

examples/channel\_group\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ChannelGroupWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

ch_group_wdg = ChannelGroupWidget()
ch_group_wdg.show()

app.exec()
```
