# ConfigGroupsEditor

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

Widget composed of two QListViews backed by a single tree model.

Methods:

| Name | Description |
| --- | --- |
| `create_from_core` | Create a ConfigGroupsEditor from a CMMCorePlus instance. |
| `update_from_core` | Refresh the editor from the current state of the core. |
| `setCurrentGroup` | Set the currently selected group in the editor. |
| `setCurrentPreset` | Set the currently selected preset in the editor. |
| `setData` | Set the configuration data to be displayed in the editor. |
| `data` | Return the current configuration data as a list of ConfigGroup. |
| `isClean` | Return True if the editor has no unapplied changes. |
| `setClean` | Mark the current state as the clean (saved) baseline. |
| `undoStack` | Return the undo stack for this editor. |
| `dirtyGroups` | Return groups that changed, deleted names, and desired channel group. |
| `sizeHint` | Suggest a size for the widget. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `configChanged` |  |  |
| `applyRequested` |  |  |

## configChanged

```python
configChanged = Signal()
```

## applyRequested

```python
applyRequested = Signal(list, list, object)
```

## create\_from\_core

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

## update\_from\_core

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

## setCurrentGroup

```python
setCurrentGroup(group: str) -> QModelIndex
```

Set the currently selected group in the editor.

Returns the index of the group that was selected, or an invalid index if no such group exists.

## setCurrentPreset

```python
setCurrentPreset(group: str, preset: str) -> QModelIndex
```

Set the currently selected preset in the editor.

Returns the index of the preset that was selected, or an invalid index if no such preset exists.

## setData

```python
setData(data: Iterable[ConfigGroup]) -> None
```

Set the configuration data to be displayed in the editor.

## data

```python
data() -> Sequence[ConfigGroup]
```

Return the current configuration data as a list of ConfigGroup.

## isClean

```python
isClean() -> bool
```

Return True if the editor has no unapplied changes.

## setClean

```python
setClean() -> None
```

Mark the current state as the clean (saved) baseline.

## undoStack

```python
undoStack() -> QUndoStack
```

Return the undo stack for this editor.

## dirtyGroups

```python
dirtyGroups() -> tuple[list[ConfigGroup], list[str], str | None]
```

Return groups that changed, deleted names, and desired channel group.

Compares only preset content (not the `is_channel_group` flag). The channel group designation is returned separately so the consumer can call `setChannelGroup` without needlessly recreating groups.

Returns:

| Type | Description |
| --- | --- |
| `tuple[list[ConfigGroup], list[str], str \| None]` | (changed\_or\_new\_groups, deleted\_group\_names, channel\_group\_name). *channel\_group\_name* is the name of the group that should be the channel group, or None if the designation did not change. |

## sizeHint

```python
sizeHint() -> QSize
```

Suggest a size for the widget.

## Example

examples/config\_groups\_editor.py

```python
import sys

from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ConfigGroupsEditor

app = QApplication([])
core = CMMCorePlus()
core.loadSystemConfiguration("tests/test_config.cfg")

with_cfg = sys.argv[1].lower() in ("1", "true") if len(sys.argv) > 1 else False
cfg = ConfigGroupsEditor.create_from_core(core, load_configs=with_cfg)


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
