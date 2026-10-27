# pymmcore\_gui.actions

Actions: the commands behind pymmcore-gui's menus, toolbars and dock widgets.

**Submodules**

| Name | Description |
| --- | --- |
| `core_actions` | Defines actions that act on the global CMMCore instance. |
| `widget_actions` | Defines actions that toggle/create singleton widgets. |

**Classes**

| Name | Description |
| --- | --- |
| `ActionKey` | A Key representing an action in the GUI. |
| `QCoreAction` | QAction that can act on a CMMCorePlus instance. |
| `WidgetActionInfo` | Subclass to set default values for WidgetAction. |

## Classes

### ActionKey

Bases: `str`, `Enum`

A Key representing an action in the GUI.

This is subclassed in core\_actions, widget\_actions, etc. to provide a unique key for each action.

### WidgetActionInfo

Bases: `ActionInfo`

Subclass to set default values for WidgetAction.

#### checkable

```python
checkable: bool = True
```

#### dock\_area

```python
dock_area: DockWidgetArea | SideBarLocation | None = (
    DockWidgetArea.RightDockWidgetArea
)
```

#### scroll\_mode

```python
scroll_mode: eInsertMode = CDockWidget.eInsertMode.AutoScrollArea
```

#### floatable

```python
floatable: bool = True
```

### QCoreAction

```python
QCoreAction(
    mmc: CMMCorePlus,
    info: ActionInfo | None = None,
    parent: QObject | None = None,
)
```

Bases: `QAction`

QAction that can act on a CMMCorePlus instance.

#### apply\_info

```python
apply_info(info: ActionInfo) -> None
```

Apply settings from a `CoreActionInfo` object to the QAction.

## Re-exports

These can also be imported from this module, but each is documented under its shortest import path (linked below).

| Name | Description |
| --- | --- |
| `ActionInfo` | Information for creating a QCoreAction. |
| `CoreAction` | Actions that act on the global CMMCore instance. |
| `WidgetAction` | Widget Actions toggle/create singleton widgets. |
