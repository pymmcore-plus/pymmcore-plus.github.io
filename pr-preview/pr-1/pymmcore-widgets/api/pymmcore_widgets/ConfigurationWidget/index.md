# ConfigurationWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

A Widget to select and load a micromanager system configuration.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget. By default, None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

Methods:

| Name | Description |
| --- | --- |
| `setTitle` |  |
| `title` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `cfg_LineEdit` |  |  |
| `browse_cfg_Button` |  |  |
| `load_cfg_Button` |  |  |

## cfg\_LineEdit

```python
cfg_LineEdit = QLineEdit()
```

## browse\_cfg\_Button

```python
browse_cfg_Button = QPushButton('...')
```

## load\_cfg\_Button

```python
load_cfg_Button = QPushButton('Load')
```

## setTitle

```python
setTitle(title: str) -> None
```

## title

```python
title() -> str
```

## Example

examples/configuration\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ConfigurationWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

cfg_wdg = ConfigurationWidget()
cfg_wdg.show()

app.exec()
```
