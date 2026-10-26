# pymmcore\_gui.actions.widget\_actions

Defines actions that toggle/create singleton widgets.

Functions:

| Name | Description |
| --- | --- |
| `create_about_widget` | Create an "about this program" widget. |
| `create_camera_roi` | Create the Camera ROI widget. |
| `create_config_groups` | Create the Config Groups widget. |
| `create_config_wizard` | Create the Hardware Configuration Wizard. |
| `create_exception_log` | Create the Exception Log widget. |
| `create_install_widgets` | Create the Install Devices widget. |
| `create_mda_widget` | Create the MDA widget. |
| `create_mm_console` | Create a console widget. |
| `create_pixel_config` | Create the Pixel Configuration widget. |
| `create_property_browser` | Create a Property Browser widget. |
| `create_stage_explorer_widget` | Create the Stage Explorer widget. |
| `create_stage_widget` | Create the Stage Control widget. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `CT` |  |  |
| `QWidgetType` |  |  |
| `show_about` |  |  |
| `show_camera_roi` |  |  |
| `show_config_groups` |  |  |
| `show_config_wizard` |  |  |
| `show_console` |  |  |
| `show_exception_log` |  |  |
| `show_install_devices` |  |  |
| `show_mda_widget` |  |  |
| `show_pixel_config` |  |  |
| `show_property_browser` |  |  |
| `show_stage_control` |  |  |
| `stage_explorer_widget` |  |  |

## CT

```python
CT = TypeVar('CT', bound=Callable[[QWidget], QWidget])
```

## QWidgetType

```python
QWidgetType = Annotated[QWidget, _ensure_isinstance(QWidget)]
```

## show\_about

```python
show_about = WidgetActionInfo(
    key=WidgetAction.ABOUT,
    text="About Pymmcore Gui...",
    create_widget=create_about_widget,
    dock_area=None,
    checkable=False,
    menu_role=QAction.MenuRole.AboutRole,
    scroll_mode=CDockWidget.eInsertMode.ForceNoScrollArea,
)
```

## show\_camera\_roi

```python
show_camera_roi = WidgetActionInfo(
    key=WidgetAction.CAMERA_ROI,
    text="Camera ROI",
    shortcut="Ctrl+Shift+R",
    icon="material-symbols-light:screenshot-region-rounded",
    create_widget=create_camera_roi,
    dock_area=DockWidgetArea.LeftDockWidgetArea,
)
```

## show\_config\_groups

```python
show_config_groups = WidgetActionInfo(
    key=WidgetAction.CONFIG_GROUPS,
    text="Config Groups",
    shortcut="Ctrl+Shift+G",
    icon="mdi-light:format-list-bulleted",
    create_widget=create_config_groups,
    dock_area=DockWidgetArea.LeftDockWidgetArea,
    scroll_mode=CDockWidget.eInsertMode.ForceNoScrollArea,
)
```

## show\_config\_wizard

```python
show_config_wizard = WidgetActionInfo(
    key=WidgetAction.CONFIG_WIZARD,
    text="Hardware Config Wizard...",
    icon="mdi:cog",
    create_widget=create_config_wizard,
    dock_area=None,
    checkable=False,
)
```

## show\_console

```python
show_console = WidgetActionInfo(
    key=WidgetAction.CONSOLE,
    text="Console",
    shortcut="Ctrl+Shift+C",
    icon="iconoir:terminal",
    create_widget=create_mm_console,
    dock_area=DockWidgetArea.BottomDockWidgetArea,
)
```

## show\_exception\_log

```python
show_exception_log = WidgetActionInfo(
    key=WidgetAction.EXCEPTION_LOG,
    text="Exception Log",
    shortcut="Ctrl+Shift+E",
    icon="mdi-light:alert",
    create_widget=create_exception_log,
    dock_area=None,
)
```

## show\_install\_devices

```python
show_install_devices = WidgetActionInfo(
    key=WidgetAction.INSTALL_DEVICES,
    text="Install Devices...",
    shortcut="Ctrl+Shift+I",
    icon="mdi-light:download",
    create_widget=create_install_widgets,
    dock_area=None,
    checkable=False,
    scroll_mode=CDockWidget.eInsertMode.ForceNoScrollArea,
)
```

## show\_mda\_widget

```python
show_mda_widget = WidgetActionInfo(
    key=WidgetAction.MDA_WIDGET,
    text="MDA",
    shortcut="Ctrl+Shift+M",
    icon="qlementine-icons:cube-16",
    create_widget=create_mda_widget,
)
```

## show\_pixel\_config

```python
show_pixel_config = WidgetActionInfo(
    key=WidgetAction.PIXEL_CONFIG,
    text="Pixel Size Configuration",
    shortcut="Ctrl+Shift+X",
    icon="mdi-light:grid",
    create_widget=create_pixel_config,
)
```

## show\_property\_browser

```python
show_property_browser = WidgetActionInfo(
    key=WidgetAction.PROP_BROWSER,
    text="Device Property Browser...",
    shortcut="Ctrl+Shift+P",
    icon="mdi-light:format-list-bulleted",
    create_widget=create_property_browser,
    dock_area=SideBarLocation.SideBarLeft,
)
```

## show\_stage\_control

```python
show_stage_control = WidgetActionInfo(
    key=WidgetAction.STAGE_CONTROL,
    text="Stage Control",
    shortcut="Ctrl+Shift+S",
    icon="fa:arrows",
    create_widget=create_stage_widget,
    dock_area=DockWidgetArea.LeftDockWidgetArea,
)
```

## stage\_explorer\_widget

```python
stage_explorer_widget = WidgetActionInfo(
    key=WidgetAction.STAGE_EXPLORER,
    text="Stage Explorer",
    icon="mdi:map-search",
    create_widget=create_stage_explorer_widget,
    dock_area=DockWidgetArea.LeftDockWidgetArea,
    floatable=False,
)
```

## create\_about\_widget

```python
create_about_widget(parent: QWidget) -> QWidget
```

Create an "about this program" widget.

## create\_camera\_roi

```python
create_camera_roi(parent: QWidget) -> CameraRoiWidget
```

Create the Camera ROI widget.

## create\_config\_groups

```python
create_config_groups(parent: QWidget) -> GroupPresetTableWidget
```

Create the Config Groups widget.

## create\_config\_wizard

```python
create_config_wizard(parent: QWidget) -> ConfigWizard
```

Create the Hardware Configuration Wizard.

## create\_exception\_log

```python
create_exception_log(parent: QWidget) -> ExceptionLog
```

Create the Exception Log widget.

## create\_install\_widgets

```python
create_install_widgets(parent: QWidget) -> QDialog
```

Create the Install Devices widget.

## create\_mda\_widget

```python
create_mda_widget(parent: QWidget) -> MDAWidget
```

Create the MDA widget.

## create\_mm\_console

```python
create_mm_console(parent: QWidget) -> MMConsole
```

Create a console widget.

## create\_pixel\_config

```python
create_pixel_config(parent: QWidget) -> PixelConfigurationWidget
```

Create the Pixel Configuration widget.

## create\_property\_browser

```python
create_property_browser(parent: QWidget) -> PropertyBrowser
```

Create a Property Browser widget.

## create\_stage\_explorer\_widget

```python
create_stage_explorer_widget(parent: QWidget) -> StageExplorer
```

Create the Stage Explorer widget.

## create\_stage\_widget

```python
create_stage_widget(parent: QWidget) -> StagesControlWidget
```

Create the Stage Control widget.

## Re-exports

These names can be imported from this module, but are documented at their top-level location.

| Name | Description |
| --- | --- |
| `WidgetAction` | Widget Actions toggle/create singleton widgets. |
