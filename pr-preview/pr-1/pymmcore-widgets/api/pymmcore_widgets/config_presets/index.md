# pymmcore\_widgets.config\_presets

Widgets related to configuration groups and presets.

Classes:

| Name | Description |
| --- | --- |
| `ConfigPresetsTable` | 2D Table for viewing configuration presets. |
| `GroupsPresetFinder` | Widget that switches between column and tree view for config groups. |

## ConfigPresetsTable

```python
ConfigPresetsTable(parent: QWidget | None = None)
```

Bases: `QWidget`

2D Table for viewing configuration presets.

Adds buttons to transpose, duplicate, and remove presets.

With all the presets as columns and the device/property pairs as rows. (unless transposed).

To use, call `setModel` with a `QConfigGroupsModel`, and then `setGroup` with the name or index of the group you want to view.

Methods:

| Name | Description |
| --- | --- |
| `create_from_core` | Create a PresetsTable from a CMMCorePlus instance. |
| `setAvailableDevices` | Set the available devices for property selection dialogs. |
| `setModel` | Set the model for the table view. |
| `sourceModel` | Return the source model of the table view. |
| `setGroup` | Set the group to be displayed. |
| `setUndoStack` | Set the undo stack for remove/duplicate operations. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `view` |  |  |
| `transpose_action` |  |  |
| `remove_action` |  |  |
| `duplicate_action` |  |  |

### view

```python
view = ConfigPresetsTableView(self)
```

### transpose\_action

```python
transpose_action = tb.addAction(
    StandardIcon.TRANSPOSE.icon(), "Transpose", self.view.transpose
)
```

### remove\_action

```python
remove_action = QAction(StandardIcon.DELETE.icon(), 'Remove')
```

### duplicate\_action

```python
duplicate_action = QAction(StandardIcon.COPY.icon(), 'Duplicate')
```

### create\_from\_core

```python
create_from_core(
    core: CMMCorePlus, parent: QWidget | None = None
) -> ConfigPresetsTable
```

Create a PresetsTable from a CMMCorePlus instance.

### setAvailableDevices

```python
setAvailableDevices(devices: Sequence[Device]) -> None
```

Set the available devices for property selection dialogs.

### setModel

```python
setModel(model: QAbstractItemModel | None) -> None
```

Set the model for the table view.

### sourceModel

```python
sourceModel() -> QConfigGroupsModel | None
```

Return the source model of the table view.

### setGroup

```python
setGroup(group_name_or_index: str | QModelIndex) -> None
```

Set the group to be displayed.

### setUndoStack

```python
setUndoStack(undo_stack: QUndoStack) -> None
```

Set the undo stack for remove/duplicate operations.

## GroupsPresetFinder

```python
GroupsPresetFinder(parent: QWidget | None = None)
```

Bases: `QStackedWidget`

Widget that switches between column and tree view for config groups.

This mimics the macOS Finder's behavior with two main views: - Column view: Groups/presets/settings side by side (index 0) - Tree view: Hierarchical structure of groups and presets (index 1)

Methods:

| Name | Description |
| --- | --- |
| `setUndoStack` | Set the undo stack and configure delegates for undo/redo. |
| `model` | Return the currently attached model. |
| `setModel` | Attach *model* to all views and give them one shared selection model. |
| `removeSelected` |  |
| `duplicateSelected` |  |
| `showColumnView` | Switch to column view mode (groups and presets side by side). |
| `showTreeView` | Switch to tree view mode (hierarchical view). |
| `toggleView` | Toggle between column view and tree view modes. |
| `setCurrentGroupAsChannelGroup` | Set the currently selected group as the channel group in the model. |
| `isTreeViewActive` | Return True if tree view is currently active. |
| `setCurrentGroup` | Set the currently selected group by name. |
| `currentGroup` | Return the currently selected group index. |
| `currentPreset` | Return the currently selected preset index. |
| `selectedPresets` | Return all selected preset indices. |
| `setCurrentPreset` | Set the currently selected preset by group and preset name. |
| `clearSelection` | Clear selection in all views. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `currentPresetChanged` |  |  |
| `currentGroupChanged` |  |  |
| `presetSelectionChanged` |  |  |
| `group_list` |  |  |
| `preset_list` |  |  |
| `config_groups_tree` |  |  |

### currentPresetChanged

```python
currentPresetChanged = Signal(QModelIndex, QModelIndex)
```

### currentGroupChanged

```python
currentGroupChanged = Signal(QModelIndex, QModelIndex)
```

### presetSelectionChanged

```python
presetSelectionChanged = Signal(list)
```

### group\_list

```python
group_list = QListView(self)
```

### preset\_list

```python
preset_list = QListView(self)
```

### config\_groups\_tree

```python
config_groups_tree = ConfigGroupsTree(self)
```

### setUndoStack

```python
setUndoStack(undo_stack: QUndoStack) -> None
```

Set the undo stack and configure delegates for undo/redo.

### model

```python
model() -> QConfigGroupsModel | None
```

Return the currently attached model.

### setModel

```python
setModel(model: QAbstractItemModel | None) -> None
```

Attach *model* to all views and give them one shared selection model.

### removeSelected

```python
removeSelected() -> None
```

### duplicateSelected

```python
duplicateSelected() -> None
```

### showColumnView

```python
showColumnView() -> None
```

Switch to column view mode (groups and presets side by side).

### showTreeView

```python
showTreeView() -> None
```

Switch to tree view mode (hierarchical view).

### toggleView

```python
toggleView() -> None
```

Toggle between column view and tree view modes.

### setCurrentGroupAsChannelGroup

```python
setCurrentGroupAsChannelGroup() -> None
```

Set the currently selected group as the channel group in the model.

### isTreeViewActive

```python
isTreeViewActive() -> bool
```

Return True if tree view is currently active.

### setCurrentGroup

```python
setCurrentGroup(group: str) -> QModelIndex
```

Set the currently selected group by name.

Returns the index of the selected group, or an invalid index if not found.

### currentGroup

```python
currentGroup() -> QModelIndex
```

Return the currently selected group index.

### currentPreset

```python
currentPreset() -> QModelIndex
```

Return the currently selected preset index.

### selectedPresets

```python
selectedPresets() -> list[QModelIndex]
```

Return all selected preset indices.

### setCurrentPreset

```python
setCurrentPreset(group: str, preset: str) -> QModelIndex
```

Set the currently selected preset by group and preset name.

Returns the index of the selected preset, or an invalid index if not found.

### clearSelection

```python
clearSelection() -> None
```

Clear selection in all views.

## Re-exports

These names can be imported from this module, but are documented at their top-level location.

| Name | Description |
| --- | --- |
| `ConfigGroupsEditor` | Widget composed of two QListViews backed by a single tree model. |
| `ConfigGroupsTree` | A tree widget that displays configuration groups. |
| `GroupPresetTableWidget` | A Widget to view and set micromanager group presets. |
| `ObjectivesPixelConfigurationWidget` | A Widget to define the pixel size configurations using the objective device. |
| `PixelConfigurationWidget` | A Widget to define the pixel size configurations. |
