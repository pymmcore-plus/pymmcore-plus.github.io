# GroupPresetTableWidget

Screenshot generated from the [example below](<#example>).

## Example

examples/group\_preset\_table\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import GroupPresetTableWidget

app = QApplication([])

mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

group_preset_wdg = GroupPresetTableWidget()
group_preset_wdg.show()

app.exec()
```

## API

Bases: `QWidget`

Table of all configuration groups, to view and set their presets.

Shows a table of config groups with their current preset values. Provides an "Edit Groups and Presets" button that opens a `ConfigGroupsEditor` dialog for editing.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget. By default, None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance()`. | `None` |
