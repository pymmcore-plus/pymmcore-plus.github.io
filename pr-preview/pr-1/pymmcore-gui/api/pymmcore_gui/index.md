# pymmcore\_gui

A Micro-Manager GUI based on pymmcore-widgets and pymmcore-plus.

Classes:

| Name | Description |
| --- | --- |
| `ActionInfo` | Information for creating a QCoreAction. |
| `CoreAction` | Actions that act on the global CMMCore instance. |
| `MicroManagerGUI` | Micro-Manager minimal GUI. |
| `WidgetAction` | Widget Actions toggle/create singleton widgets. |

Functions:

| Name | Description |
| --- | --- |
| `create_mmgui` | Initialize the pymmcore-gui application and Main Window. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `__version__` | `str` |  |

## \_\_version\_\_

```python
__version__: str = version('pymmcore-gui')
```

## ActionInfo

Bases: `BaseModel`

Information for creating a QCoreAction.

Methods:

| Name | Description |
| --- | --- |
| `model_post_init` |  |
| `to_qaction` | Create a QCoreAction from this info. |
| `for_key` | Get the ActionInfo for a given key. |
| `widget_actions` | Return all widget actions. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `key` | `str` | A unique key to identify the action. |
| `text` | `str` | How the action should be displayed in the GUI. |
| `auto_repeat` | `bool` |  |
| `checkable` | `bool` |  |
| `checked` | `bool` |  |
| `enabled` | `bool` |  |
| `icon` | `str \| None \| QIconType` |  |
| `icon_text` | `str \| None` |  |
| `icon_visible_in_menu` | `bool \| None` |  |
| `menu_role` | `MenuRole \| None` |  |
| `priority` | `Priority \| None` |  |
| `shortcut` | `str \| None \| QKeySequenceType` |  |
| `shortcut_context` | `ShortcutContext \| None` |  |
| `shortcut_visible_in_context_menu` | `bool \| None` |  |
| `status_top` | `str \| None` |  |
| `tooltip` | `str \| None` |  |
| `visible` | `bool` |  |
| `whats_this` | `str \| None` |  |
| `on_triggered` | `ActionTriggeredFunc \| None` |  |
| `on_created` | `CoreActionFunc \| None` |  |

### key

```python
key: str
```

A unique key to identify the action.

### text

```python
text: str
```

How the action should be displayed in the GUI.

### auto\_repeat

```python
auto_repeat: bool = False
```

### checkable

```python
checkable: bool = False
```

### checked

```python
checked: bool = False
```

### enabled

```python
enabled: bool = True
```

### icon

```python
icon: str | None | QIconType = None
```

### icon\_text

```python
icon_text: str | None = None
```

### icon\_visible\_in\_menu

```python
icon_visible_in_menu: bool | None = None
```

### menu\_role

```python
menu_role: MenuRole | None = None
```

### priority

```python
priority: Priority | None = None
```

### shortcut

```python
shortcut: str | None | QKeySequenceType = None
```

### shortcut\_context

```python
shortcut_context: ShortcutContext | None = None
```

### shortcut\_visible\_in\_context\_menu

```python
shortcut_visible_in_context_menu: bool | None = None
```

### status\_top

```python
status_top: str | None = None
```

### tooltip

```python
tooltip: str | None = None
```

### visible

```python
visible: bool = True
```

### whats\_this

```python
whats_this: str | None = None
```

### on\_triggered

```python
on_triggered: ActionTriggeredFunc | None = None
```

### on\_created

```python
on_created: CoreActionFunc | None = None
```

### model\_post\_init

```python
model_post_init(__context: Any) -> None
```

### to\_qaction

```python
to_qaction(mmc: CMMCorePlus, parent: QObject | None = None) -> QCoreAction
```

Create a QCoreAction from this info.

### for\_key

```python
for_key(key: str) -> Self
```

Get the ActionInfo for a given key.

### widget\_actions

```python
widget_actions() -> dict[str, WidgetActionInfo]
```

Return all widget actions.

## CoreAction

Bases: `ActionKey`

Actions that act on the global CMMCore instance.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `SNAP` |  |  |
| `TOGGLE_LIVE` |  |  |
| `LOAD_DEMO` |  |  |
| `LOAD_CONFIG` |  |  |
| `SAVE_CONFIG` |  |  |

### SNAP

```python
SNAP = 'pymmcore_gui.snap_image'
```

### TOGGLE\_LIVE

```python
TOGGLE_LIVE = 'pymmcore_gui.toggle_live'
```

### LOAD\_DEMO

```python
LOAD_DEMO = 'pymmcore_gui.load_demo_config'
```

### LOAD\_CONFIG

```python
LOAD_CONFIG = 'pymmcore_gui.load_config'
```

### SAVE\_CONFIG

```python
SAVE_CONFIG = 'pymmcore_gui.save_config'
```

## MicroManagerGUI

```python
MicroManagerGUI(*, mmcore: CMMCorePlus | None = None)
```

Bases: `QMainWindow`

Micro-Manager minimal GUI.

Methods:

| Name | Description |
| --- | --- |
| `get_action` | Create a QAction from this key. |
| `get_widget` | Get (or create) widget for `key` ensuring that it is linked to its QAction. |
| `get_dock_widget` | Get the QDockWidget for `key`. |
| `closeEvent` |  |
| `restore_state` | Restore the state of the window from settings (or load default state). |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `TOOLBARS` | `Mapping[str, ToolDictValue]` |  |
| `MENUS` | `Mapping[str, MenuDictValue]` |  |
| `bell_button` |  |  |
| `dock_manager` |  |  |
| `nm` | `NotificationManager` | A callable that can be used to show a message in the status bar. |
| `mmcore` | `CMMCorePlus` |  |

### TOOLBARS

```python
TOOLBARS: Mapping[str, ToolDictValue] = {
    Toolbar.CAMERA_ACTIONS: [CoreAction.SNAP, CoreAction.TOGGLE_LIVE],
    Toolbar.OPTICAL_CONFIGS: OCToolBar,
    Toolbar.WIDGETS: [
        WidgetAction.CONSOLE,
        WidgetAction.PROP_BROWSER,
        WidgetAction.MDA_WIDGET,
        WidgetAction.STAGE_CONTROL,
        WidgetAction.CAMERA_ROI,
    ],
}
```

### MENUS

```python
MENUS: Mapping[str, MenuDictValue] = {
    Menu.PYMM_GUI: [WidgetAction.ABOUT],
    Menu.WINDOW: _create_window_menu,
    Menu.DEVICE: [
        WidgetAction.PROP_BROWSER,
        WidgetAction.CONFIG_WIZARD,
        None,
        CoreAction.LOAD_CONFIG,
        CoreAction.LOAD_DEMO,
        CoreAction.SAVE_CONFIG,
        None,
        WidgetAction.INSTALL_DEVICES,
    ],
    Menu.HELP: [],
}
```

### bell\_button

```python
bell_button = QPushButton(QIconifyIcon('codicon:bell'), None)
```

### dock\_manager

```python
dock_manager = CDockManager(self)
```

### nm

```python
nm: NotificationManager
```

A callable that can be used to show a message in the status bar.

### mmcore

```python
mmcore: CMMCorePlus
```

### get\_action

```python
get_action(key: str, create: bool = True) -> QAction
```

Create a QAction from this key.

### get\_widget

```python
get_widget(key: Literal[ABOUT], create: bool = ...) -> AboutWidget
```

```python
get_widget(key: Literal[CAMERA_ROI], create: bool = ...) -> CameraRoiWidget
```

```python
get_widget(
    key: Literal[CONFIG_GROUPS], create: bool = ...
) -> GroupPresetTableWidget
```

```python
get_widget(key: Literal[CONFIG_WIZARD], create: bool = ...) -> ConfigWizard
```

```python
get_widget(key: Literal[CONSOLE], create: bool = ...) -> MMConsole
```

```python
get_widget(key: Literal[EXCEPTION_LOG], create: bool = ...) -> ExceptionLog
```

```python
get_widget(key: Literal[INSTALL_DEVICES], create: bool = ...) -> InstallWidget
```

```python
get_widget(key: Literal[MDA_WIDGET], create: bool = ...) -> MDAWidget
```

```python
get_widget(
    key: Literal[PIXEL_CONFIG], create: bool = ...
) -> PixelConfigurationWidget
```

```python
get_widget(key: Literal[PROP_BROWSER], create: bool = ...) -> PropertyBrowser
```

```python
get_widget(
    key: Literal[STAGE_CONTROL], create: bool = ...
) -> StagesControlWidget
```

```python
get_widget(key: str, create: bool = ...) -> QWidget
```

```python
get_widget(key: str, create: bool = True) -> QWidget
```

Get (or create) widget for `key` ensuring that it is linked to its QAction.

If the widget has been "closed" (hidden), it will be re-shown.

Note that all widgets created this way are singletons, so calling this method multiple times will return the same widget instance.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `WidgetAction` | The widget to get. | *required* |
| `create` | `bool` | Whether to create the widget if it doesn't exist yet, by default True. | `True` |

Raises:

| Type | Description |
| --- | --- |
| `KeyError` | If the widget doesn't exist and `create` is False. |

### get\_dock\_widget

```python
get_dock_widget(key: str) -> CDockWidget
```

Get the QDockWidget for `key`.

Note, you can also get the QDockWidget by calling `get_widget(key)`, and then calling `widget.parent()`. The parent will *either* be an instance of `QDockWidget` (if it's actually a docked widget), or `MicroManagerGUI`, if it's not docked. You *should* use `isisinstance` in this case to check.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `WidgetAction` | The key for the *inner* widget owned by the requested QDockWidget. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `KeyError` | If the widget doesn't exist. |

### closeEvent

```python
closeEvent(a0: QCloseEvent) -> None
```

### restore\_state

```python
restore_state(*, show: bool = False) -> None
```

Restore the state of the window from settings (or load default state).

show is added as a convenience here because it may be a common use case to restore the state in a single shot timer and (only) then show the window. This avoids the window flashing on the screen before it is properly positioned.

## WidgetAction

Bases: `ActionKey`

Widget Actions toggle/create singleton widgets.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `ABOUT` |  |  |
| `PROP_BROWSER` |  |  |
| `PIXEL_CONFIG` |  |  |
| `INSTALL_DEVICES` |  |  |
| `MDA_WIDGET` |  |  |
| `CONFIG_GROUPS` |  |  |
| `CAMERA_ROI` |  |  |
| `CONSOLE` |  |  |
| `EXCEPTION_LOG` |  |  |
| `STAGE_CONTROL` |  |  |
| `STAGE_EXPLORER` |  |  |
| `CONFIG_WIZARD` |  |  |

### ABOUT

```python
ABOUT = 'pymmcore_gui.about_widget'
```

### PROP\_BROWSER

```python
PROP_BROWSER = 'pymmcore_gui.property_browser'
```

### PIXEL\_CONFIG

```python
PIXEL_CONFIG = 'pymmcore_gui.pixel_config_widget'
```

### INSTALL\_DEVICES

```python
INSTALL_DEVICES = 'pymmcore_gui.install_devices_widget'
```

### MDA\_WIDGET

```python
MDA_WIDGET = 'pymmcore_gui.mda_widget'
```

### CONFIG\_GROUPS

```python
CONFIG_GROUPS = 'pymmcore_gui.config_groups_widget'
```

### CAMERA\_ROI

```python
CAMERA_ROI = 'pymmcore_gui.camera_roi_widget'
```

### CONSOLE

```python
CONSOLE = 'pymmcore_gui.console'
```

### EXCEPTION\_LOG

```python
EXCEPTION_LOG = 'pymmcore_gui.exception_log'
```

### STAGE\_CONTROL

```python
STAGE_CONTROL = 'pymmcore_gui.stage_control_widget'
```

### STAGE\_EXPLORER

```python
STAGE_EXPLORER = 'pymmcore_gui.stage_explorer_widget'
```

### CONFIG\_WIZARD

```python
CONFIG_WIZARD = 'pymmcore_gui.hardware_config_wizard'
```

## create\_mmgui

```python
create_mmgui(
    *,
    mm_config: Path | str | None | Literal[False] = None,
    mmcore: CMMCorePlus | None = None,
    install_sys_excepthook: bool = True,
    install_sentry: bool = True,
    exec_app: bool = True,
) -> MicroManagerGUI
```

Initialize the pymmcore-gui application and Main Window.

This is the primary way to start pymmcore-gui. (It is also called by `__main__.main()` when running from the command line.)

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `mm_config` | `str \| None \| False` | The path to the Micro-Manager configuration file to load. - If `False`, no configuration will be loaded. - If a non-empty string, that configuration will be loaded. - If None (or the empty string), auto-deciding logic will be used based on the stored user settings (based on the settings values for `Settings.last_config` and `Settings.auto_load_last_config`). | `None` |
| `mmcore` | `CMMCorePlus \| None` | The CMMCorePlus instance to use. If `None` (default), the global `CMMCorePlus.instance()` will be used if it exists, or a new (global) instance will be created (which you may access later with `CMMCorePlus.instance()`). Note: you may wish to also pass `mm_config = False` to prevent loading a system configuration, if you have already loaded one in your instance. | `None` |
| `install_sys_excepthook` | `bool` | If True (the default), installs a custom excepthook that does not raise sys.exit(). This is necessary to prevent the application from closing when an unhandled exception is raised in the main thread. | `True` |
| `install_sentry` | `bool` | If True (the default), the user will be given an option to send error reports to the developers, unless they have previously opted in/out. If False, no prompt will be shown, and no error reports will be sent. | `True` |
| `exec_app` | `bool` | If True (the default), the QApplication event loop will be started. If False, the event loop will not be started, and the caller is responsible for starting it with `QApplication.instance().exec()`. | `True` |
