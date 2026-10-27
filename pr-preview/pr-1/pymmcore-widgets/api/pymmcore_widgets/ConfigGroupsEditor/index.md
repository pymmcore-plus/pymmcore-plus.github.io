# ConfigGroupsEditor

Screenshot generated from the [example below](<#example>).

## Example

examples/config\_groups\_editor.py

```python
"""ConfigGroupsEditor edits configuration groups and their presets.

It doesn't change the core: when you click "Apply", it emits `applyRequested`
with the changes, and it's up to you what to do with them.
"""

from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ConfigGroupsEditor

app = QApplication([])
core = CMMCorePlus.instance()
core.loadSystemConfiguration()

# load the core's devices, groups and presets into the editor
# (pass `load_configs=False` to start with an empty list of groups)
cfg = ConfigGroupsEditor.create_from_core(core)


# connect to apply signal to print the changes
def _on_apply_clicked(changed, deleted, channel_group):
    print("\n\nApply clicked:")
    print(f"Changed: {[cg.name for cg in changed]}")
    print(f"Deleted: {deleted}")
    print(f"Channel group: {channel_group}")


cfg.applyRequested.connect(_on_apply_clicked)

cfg.resize(900, 550)
cfg.show()

app.exec()
```

## API

Bases: `QWidget`

Editor for configuration groups and their presets.

The editor doesn't change the core. Build it from a core with `create_from_core`, and connect to `applyRequested` to apply the user's changes.

### configChanged

```python
configChanged = Signal()
```

Emitted (with no arguments) whenever the user edits a group or preset.

### applyRequested

```python
applyRequested = Signal(list, list, object)
```

Emitted when the user clicks "Apply".

Arguments are `(changed, deleted, channel_group)`: the new or changed `ConfigGroup`s, the names of deleted groups, and the name of the group that should become the channel group (or `None` if that didn't change).

### create\_from\_core

```python
create_from_core(
    core: CMMCorePlus,
    parent: QWidget | None = None,
    *,
    load_configs: bool = True,
) -> ConfigGroupsEditor
```

Create a ConfigGroupsEditor from a CMMCorePlus instance.

Available devices are loaded from the core, and if `load_configs` is True, config groups/presets are also loaded.

### update\_from\_core

```python
update_from_core(
    core: CMMCorePlus,
    *,
    update_devices: bool = True,
    update_configs: bool = False,
) -> None
```

Refresh the editor from the current state of the core.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `core` | `CMMCorePlus` | The core instance to pull data from. | *required* |
| `update_devices` | `bool` | If True, refresh the list of loaded devices and their properties. This determines which devices and properties appear in the "Edit Properties" and "Add Property" dialogs. | `True` |
| `update_configs` | `bool` | If True, replace the current editor contents with config groups, presets, and their settings from the core. If False, the current groups/presets will be left unchanged (meaning you will have an empty editor until you add groups/presets manually). | `False` |

### setCurrentGroup

```python
setCurrentGroup(group: str) -> QModelIndex
```

Set the currently selected group in the editor.

Returns the index of the group that was selected, or an invalid index if no such group exists.

### setCurrentPreset

```python
setCurrentPreset(group: str, preset: str) -> QModelIndex
```

Set the currently selected preset in the editor.

Returns the index of the preset that was selected, or an invalid index if no such preset exists.

### setData

```python
setData(data: Iterable[ConfigGroup]) -> None
```

Set the configuration data to be displayed in the editor.

### data

```python
data() -> Sequence[ConfigGroup]
```

Return the current configuration data as a list of ConfigGroup.

### isClean

```python
isClean() -> bool
```

Return True if the editor has no unapplied changes.

### setClean

```python
setClean() -> None
```

Mark the current state as the clean (saved) baseline.

### undoStack

```python
undoStack() -> QUndoStack
```

Return the undo stack for this editor.

### dirtyGroups

```python
dirtyGroups() -> tuple[list[ConfigGroup], list[str], str | None]
```

Return groups that changed, deleted names, and desired channel group.

Compares only preset content (not the `is_channel_group` flag). The channel group designation is returned separately so the consumer can call `setChannelGroup` without needlessly recreating groups.

Returns:

| Type | Description |
| --- | --- |
| `tuple[list[ConfigGroup], list[str], str \| None]` | (changed\_or\_new\_groups, deleted\_group\_names, channel\_group\_name). *channel\_group\_name* is the name of the group that should be the channel group, or None if the designation did not change. |
