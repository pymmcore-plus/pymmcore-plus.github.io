# pymmcore\_widgets.config\_presets

Widgets related to configuration groups and presets.

**Classes**

| Name | Description |
| --- | --- |
| `ConfigPresetsTable` | 2D Table for viewing configuration presets. |
| `GroupsPresetFinder` | Widget that switches between column and tree view for config groups. |

## Classes

### ConfigPresetsTable

```python
ConfigPresetsTable(parent: QWidget | None = None)
```

Bases: `QWidget`

2D Table for viewing configuration presets.

Adds buttons to transpose, duplicate, and remove presets.

With all the presets as columns and the device/property pairs as rows. (unless transposed).

To use, call `setModel` with a `QConfigGroupsModel`, and then `setGroup` with the name or index of the group you want to view.

#### create\_from\_core

```python
create_from_core(
    core: CMMCorePlus, parent: QWidget | None = None
) -> ConfigPresetsTable
```

Create a PresetsTable from a CMMCorePlus instance.

#### setAvailableDevices

```python
setAvailableDevices(devices: Sequence[Device]) -> None
```

Set the available devices for property selection dialogs.

#### setModel

```python
setModel(model: QAbstractItemModel | None) -> None
```

Set the model for the table view.

#### sourceModel

```python
sourceModel() -> QConfigGroupsModel | None
```

Return the source model of the table view.

#### setGroup

```python
setGroup(group_name_or_index: str | QModelIndex) -> None
```

Set the group to be displayed.

#### setUndoStack

```python
setUndoStack(undo_stack: QUndoStack) -> None
```

Set the undo stack for remove/duplicate operations.

### GroupsPresetFinder

```python
GroupsPresetFinder(parent: QWidget | None = None)
```

Bases: `QStackedWidget`

Widget that switches between column and tree view for config groups.

This mimics the macOS Finder's behavior with two main views: - Column view: Groups/presets/settings side by side (index 0) - Tree view: Hierarchical structure of groups and presets (index 1)

#### currentPresetChanged

```python
currentPresetChanged = Signal(QModelIndex, QModelIndex)
```

#### currentGroupChanged

```python
currentGroupChanged = Signal(QModelIndex, QModelIndex)
```

#### presetSelectionChanged

```python
presetSelectionChanged = Signal(list)
```

#### setUndoStack

```python
setUndoStack(undo_stack: QUndoStack) -> None
```

Set the undo stack and configure delegates for undo/redo.

#### model

```python
model() -> QConfigGroupsModel | None
```

Return the currently attached model.

#### setModel

```python
setModel(model: QAbstractItemModel | None) -> None
```

Attach *model* to all views and give them one shared selection model.

#### removeSelected

```python
removeSelected() -> None
```

#### duplicateSelected

```python
duplicateSelected() -> None
```

#### showColumnView

```python
showColumnView() -> None
```

Switch to column view mode (groups and presets side by side).

#### showTreeView

```python
showTreeView() -> None
```

Switch to tree view mode (hierarchical view).

#### toggleView

```python
toggleView() -> None
```

Toggle between column view and tree view modes.

#### setCurrentGroupAsChannelGroup

```python
setCurrentGroupAsChannelGroup() -> None
```

Set the currently selected group as the channel group in the model.

#### isTreeViewActive

```python
isTreeViewActive() -> bool
```

Return True if tree view is currently active.

#### setCurrentGroup

```python
setCurrentGroup(group: str) -> QModelIndex
```

Set the currently selected group by name.

Returns the index of the selected group, or an invalid index if not found.

#### currentGroup

```python
currentGroup() -> QModelIndex
```

Return the currently selected group index.

#### currentPreset

```python
currentPreset() -> QModelIndex
```

Return the currently selected preset index.

#### selectedPresets

```python
selectedPresets() -> list[QModelIndex]
```

Return all selected preset indices.

#### setCurrentPreset

```python
setCurrentPreset(group: str, preset: str) -> QModelIndex
```

Set the currently selected preset by group and preset name.

Returns the index of the selected preset, or an invalid index if not found.

#### clearSelection

```python
clearSelection() -> None
```

Clear selection in all views.

## Re-exports

These can also be imported from this module, but each is documented under its shortest import path (linked below).

| Name | Description |
| --- | --- |
| `ConfigGroupsEditor` | Editor for configuration groups and their presets. |
| `ConfigGroupsTree` | A tree widget that displays configuration groups. |
| `GroupPresetTableWidget` | Table of all configuration groups, to view and set their presets. |
| `ObjectivesPixelConfigurationWidget` | A Widget to define the pixel size configurations using the objective device. |
| `PixelConfigurationWidget` | A Widget to define the pixel size configurations. |
