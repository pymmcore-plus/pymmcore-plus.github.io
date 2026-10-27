# ConfigurationWidget

Screenshot generated from the [example below](<#example>).

## Example

examples/configuration\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ConfigurationWidget

app = QApplication([])

mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

cfg_wdg = ConfigurationWidget()
cfg_wdg.show()

app.exec()
```

## API

Bases: `QWidget`

A Widget to select and load a Micro-Manager system configuration.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget. By default, None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

### setTitle

```python
setTitle(title: str) -> None
```

### title

```python
title() -> str
```
