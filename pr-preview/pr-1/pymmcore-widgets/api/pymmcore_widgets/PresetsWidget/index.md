# PresetsWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

A Widget to create a QCombobox containing the presets of the specified group.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `group` | `str` | Group name. | *required* |
| `parent` | `QWidget \| None` | Optional parent widget. By default, None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

Methods:

| Name | Description |
| --- | --- |
| `value` | Get current value. |
| `setValue` | Set the combobox to the given value. |
| `allowedValues` | Return the allowed values for this widget. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `dev_prop` |  |  |

## dev\_prop

```python
dev_prop = self._get_preset_dev_prop(self._group, self._presets[0])
```

## value

```python
value() -> str
```

Get current value.

## setValue

```python
setValue(value: str) -> None
```

Set the combobox to the given value.

## allowedValues

```python
allowedValues() -> tuple[str, ...]
```

Return the allowed values for this widget.

## Example

examples/presets\_widget.py

```python
"""Example Usage of the PresetsWidget class.

In this example all the available groups created in micromanager
are displayed with a 'PresetsWidget'.
"""

from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication, QFormLayout, QWidget

from pymmcore_widgets import PresetsWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

wdg = QWidget()
wdg.setLayout(QFormLayout())

for group in mmc.getAvailableConfigGroups():
    gp_wdg = PresetsWidget(group)
    wdg.layout().addRow(f"{group}:", gp_wdg)

wdg.show()

app.exec()
```
