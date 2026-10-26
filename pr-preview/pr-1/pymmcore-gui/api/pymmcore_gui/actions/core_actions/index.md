# pymmcore\_gui.actions.core\_actions

Defines actions that act on the global CMMCore instance.

Functions:

| Name | Description |
| --- | --- |
| `load_demo_config` | Load the demo configuration. |
| `load_sys_config_dialog` | Open a dialog to load a system configuration. |
| `save_sys_config_dialog` | Open a dialog to save a system configuration. |
| `snap_image` | Snap an image, stopping sequence if running. |
| `toggle_live` | Start or stop live mode. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `load_config_action` |  |  |
| `load_demo_action` |  |  |
| `snap_action` |  |  |
| `toggle_live_action` |  |  |

## load\_config\_action

```python
load_config_action = ActionInfo(
    key="pymmcore_gui.save_config",
    text="Save System Configuration...",
    on_triggered=save_sys_config_dialog,
)
```

## load\_demo\_action

```python
load_demo_action = ActionInfo(
    key=CoreAction.LOAD_DEMO,
    text="Load Demo Configuration",
    on_triggered=load_demo_config,
)
```

## snap\_action

```python
snap_action = ActionInfo(
    key=CoreAction.SNAP,
    text="Snap Image",
    shortcut="Ctrl+K",
    auto_repeat=True,
    icon="mdi-light:camera",
    on_triggered=snap_image,
    on_created=_init_snap_image,
)
```

## toggle\_live\_action

```python
toggle_live_action = ActionInfo(
    key=CoreAction.TOGGLE_LIVE,
    text="Toggle Live",
    shortcut="Ctrl+L",
    auto_repeat=True,
    icon="mdi:video-outline",
    checkable=True,
    on_triggered=toggle_live,
    on_created=_init_toggle_live,
)
```

## load\_demo\_config

```python
load_demo_config(action: QCoreAction, checked: bool) -> None
```

Load the demo configuration.

## load\_sys\_config\_dialog

```python
load_sys_config_dialog(action: QCoreAction, checked: bool) -> None
```

Open a dialog to load a system configuration.

## save\_sys\_config\_dialog

```python
save_sys_config_dialog(action: QCoreAction, checked: bool) -> None
```

Open a dialog to save a system configuration.

## snap\_image

```python
snap_image(action: QCoreAction, checked: bool) -> None
```

Snap an image, stopping sequence if running.

## toggle\_live

```python
toggle_live(action: QCoreAction, checked: bool) -> None
```

Start or stop live mode.

## Re-exports

These names can be imported from this module, but are documented at their top-level location.

| Name | Description |
| --- | --- |
| `CoreAction` | Actions that act on the global CMMCore instance. |
