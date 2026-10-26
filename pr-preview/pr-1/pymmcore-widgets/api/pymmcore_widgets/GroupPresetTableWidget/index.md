# GroupPresetTableWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

A Widget to view and set micromanager group presets.

Shows a table of config groups with their current preset values. Provides an "Edit Groups and Presets" button that opens a `ConfigGroupsEditor` dialog for editing.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget. By default, None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance()`. | `None` |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `table_wdg` |  |  |
| `save_btn` |  |  |
| `load_btn` |  |  |
| `edit_groups_btn` |  |  |

## table\_wdg

```python
table_wdg = _MainTable()
```

## save\_btn

```python
save_btn = QPushButton(text='Save cfg')
```

## load\_btn

```python
load_btn = QPushButton(text='Load cfg')
```

## edit\_groups\_btn

```python
edit_groups_btn = QPushButton(text='Edit Groups and Presets')
```

## Example

examples/group\_preset\_table\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import GroupPresetTableWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

group_preset_wdg = GroupPresetTableWidget()
group_preset_wdg.show()

app.exec()
```
