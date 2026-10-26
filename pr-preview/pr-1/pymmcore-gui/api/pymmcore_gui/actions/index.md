# pymmcore\_gui.actions

Classes:

| Name | Description |
| --- | --- |
| `ActionKey` | A Key representing an action in the GUI. |
| `QCoreAction` | QAction that can act on a CMMCorePlus instance. |
| `WidgetActionInfo` | Subclass to set default values for WidgetAction. |

## ActionKey

Bases: `str`, `Enum`

A Key representing an action in the GUI.

This is subclassed in core\_actions, widget\_actions, etc. to provide a unique key for each action.

## QCoreAction

```python
QCoreAction(
    mmc: CMMCorePlus,
    info: ActionInfo | None = None,
    parent: QObject | None = None,
)
```

Bases: `QAction`

QAction that can act on a CMMCorePlus instance.

Methods:

| Name | Description |
| --- | --- |
| `apply_info` | Apply settings from a `CoreActionInfo` object to the QAction. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `key` | `str` |  |
| `mmc` |  |  |

### key

```python
key: str
```

### mmc

```python
mmc = mmc
```

### apply\_info

```python
apply_info(info: ActionInfo) -> None
```

Apply settings from a `CoreActionInfo` object to the QAction.

## WidgetActionInfo

Bases: `ActionInfo`

Subclass to set default values for WidgetAction.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `checkable` | `bool` |  |
| `create_widget` | `Callable[[QWidgetType], QWidget]` |  |
| `dock_area` | `DockWidgetArea \| SideBarLocation \| None` |  |
| `scroll_mode` | `eInsertMode` |  |
| `floatable` | `bool` |  |

### checkable

```python
checkable: bool = True
```

### create\_widget

```python
create_widget: Callable[[QWidgetType], QWidget]
```

### dock\_area

```python
dock_area: DockWidgetArea | SideBarLocation | None = (
    DockWidgetArea.RightDockWidgetArea
)
```

### scroll\_mode

```python
scroll_mode: eInsertMode = CDockWidget.eInsertMode.AutoScrollArea
```

### floatable

```python
floatable: bool = True
```

## Re-exports

These names can be imported from this module, but are documented at their top-level location.

| Name | Description |
| --- | --- |
| `ActionInfo` | Information for creating a QCoreAction. |
| `CoreAction` | Actions that act on the global CMMCore instance. |
| `WidgetAction` | Widget Actions toggle/create singleton widgets. |
