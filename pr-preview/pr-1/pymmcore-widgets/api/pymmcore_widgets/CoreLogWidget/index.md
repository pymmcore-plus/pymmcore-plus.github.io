# CoreLogWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

High-performance log console with pause, follow-tail, clear, and initial load.

Methods:

| Name | Description |
| --- | --- |
| `clear` | Clear the log view. |
| `sizeHint` |  |
| `closeEvent` | Clean up thread on close. |

## clear

```python
clear() -> None
```

Clear the log view.

## sizeHint

```python
sizeHint() -> QSize
```

## closeEvent

```python
closeEvent(event: QCloseEvent | None) -> None
```

Clean up thread on close.

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
