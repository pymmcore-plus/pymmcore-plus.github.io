# ConfigGroupsTree

Screenshot generated from the [example below](<#example>).

Bases: `QTreeView`

A tree widget that displays configuration groups.

Methods:

| Name | Description |
| --- | --- |
| `create_from_core` | Create a ConfigGroupsTree from a CMMCorePlus instance. |
| `setUndoStack` | Set the undo stack and configure undo-aware delegates. |
| `setModel` | Set the model for the tree view. |

## create\_from\_core

```python
create_from_core(
    core: CMMCorePlus, parent: QWidget | None = None
) -> ConfigGroupsTree
```

Create a ConfigGroupsTree from a CMMCorePlus instance.

## setUndoStack

```python
setUndoStack(undo_stack: QUndoStack) -> None
```

Set the undo stack and configure undo-aware delegates.

## setModel

```python
setModel(model: QAbstractItemModel | None) -> None
```

Set the model for the tree view.

## Example

examples/config\_groups\_tree.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtCore import QModelIndex
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ConfigGroupsTree

app = QApplication([])

core = CMMCorePlus()
core.loadSystemConfiguration()

tree = ConfigGroupsTree.create_from_core(core)
tree.show()
tree.expandRecursively(QModelIndex())
tree.resize(600, 600)

app.exec()
```
