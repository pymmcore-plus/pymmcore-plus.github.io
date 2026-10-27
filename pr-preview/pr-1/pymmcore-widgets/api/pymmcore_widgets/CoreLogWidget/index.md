# CoreLogWidget

Screenshot generated from the [example below](<#example>).

## Example

examples/core\_log\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import CoreLogWidget

app = QApplication([])
core = CMMCorePlus()

wdg = CoreLogWidget(mmcore=core)
wdg.clear()
wdg.show()

core.loadSystemConfiguration()
app.exec()
```

## API

Bases: `QWidget`

Live view of the core's log file.

It shows the end of the file when it opens, then follows new lines as they are written. There are buttons to pause, clear the view, and turn on debug logging.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `path` | `str \| None` | Log file to show. By default, None, meaning the core's primary log file (`getPrimaryLogFile`). | `None` |
| `max_lines` | `int` | Maximum number of lines kept in the view. By default, 5000. | `5000` |
| `parent` | `QWidget \| None` | Optional parent widget. By default, None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

### clear

```python
clear() -> None
```

Clear the log view.
