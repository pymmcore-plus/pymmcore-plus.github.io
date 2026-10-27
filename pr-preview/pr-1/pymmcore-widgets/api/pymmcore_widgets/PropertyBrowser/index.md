# PropertyBrowser

Screenshot generated from the [example below](<#example>).

## Example

examples/property\_browser.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import PropertyBrowser

app = QApplication([])

mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

pb_wdg = PropertyBrowser()
pb_wdg.show()

app.exec()
```

## API

Bases: `QDialog`

A Widget to browse and change properties of all devices.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget. By default, None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |
