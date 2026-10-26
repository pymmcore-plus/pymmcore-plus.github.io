# pymmcore\_widgets

A set of widgets for the pymmcore-plus module.

Classes:

| Name | Description |
| --- | --- |
| `DeviceWidget` | A general Device Widget. |
| `StateDeviceWidget` | A Widget with a QComboBox to control the states of a StateDevice. |

## DeviceWidget

```python
DeviceWidget(
    device_label: str,
    *,
    parent: QWidget | None = None,
    mmcore: CMMCorePlus | None = None,
)
```

Bases: `QWidget`

A general Device Widget.

Use `DeviceWidget.for_device('device_label')` method to create a device-type appropriate subclass.

> [!NOTE]
>
> Currently, `DeviceWidget` only supports devices of type `StateDevice`. Calling `DeviceWidget.for_device("device_label")`, will create the `DeviceWidget` subclass pymmcore\_widgets.StateDeviceWidget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_label` | `str` | A device label for which to create a widget. | *required* |
| `parent` | `QWidget \| None` | Optional parent widget. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

Methods:

| Name | Description |
| --- | --- |
| `deviceLabel` | Return device label. |
| `deviceName` | Return device name (this is *not* the device label). |
| `deviceType` | Return type of Device (`pymmcore_plus.DeviceType`). |
| `for_device` | Create a type-appropriate subclass for device with label `device_label`. |

### deviceLabel

```python
deviceLabel() -> str
```

Return device label.

### deviceName

```python
deviceName() -> str
```

Return device name (this is *not* the device label).

### deviceType

```python
deviceType() -> DeviceType
```

Return type of Device (`pymmcore_plus.DeviceType`).

### for\_device

```python
for_device(
    device_label: str, *, mmcore: CMMCorePlus | None = None
) -> DeviceWidget
```

Create a type-appropriate subclass for device with label `device_label`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_label` | `str` | A deviceLabel for which to create a widget. | *required* |
| `mmcore` | `CMMCorePlus \| None` | Optional micromanager core. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `DeviceWidget` | Appropriate DeviceWidget subclass instance. |

## StateDeviceWidget

```python
StateDeviceWidget(
    device_label: str,
    *,
    parent: QWidget | None = None,
    mmcore: CMMCorePlus | None = None,
)
```

Bases: `DeviceWidget`

A Widget with a QComboBox to control the states of a StateDevice.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_label` | `str` | A device label for which to create a widget. | *required* |
| `parent` | `QWidget \| None` | Optional parent widget. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

Methods:

| Name | Description |
| --- | --- |
| `state` | Return current state (index) of the device. |
| `stateLabel` | Return current state (label) of the device. |
| `stateLabels` | Return all state labels of the device. |
| `currentText` |  |
| `setCurrentText` |  |
| `currentIndex` |  |
| `setCurrentIndex` |  |

### state

```python
state() -> int
```

Return current state (index) of the device.

### stateLabel

```python
stateLabel() -> str
```

Return current state (label) of the device.

### stateLabels

```python
stateLabels() -> tuple[str, ...]
```

Return all state labels of the device.

### currentText

```python
currentText() -> str
```

### setCurrentText

```python
setCurrentText(text: str) -> None
```

### currentIndex

```python
currentIndex() -> int
```

### setCurrentIndex

```python
setCurrentIndex(index: int) -> None
```

## Documented on other pages

| Object | Page | Description |
| --- | --- | --- |
| `CameraRoiWidget` | CameraRoiWidget | A Widget to control the camera device ROI. |
| `ChannelGroupWidget` | ChannelGroupWidget | A QComboBox to follow and control Micro-Manager ChannelGroup. |
| `ChannelTable` | ChannelTable | Table to edit a list of [useq.Channels](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#useq.Channel>). |
| `ChannelWidget` | ChannelWidget | A QComboBox to select which micromanager channel configuration to use. |
| `ConfigGroupsEditor` | ConfigGroupsEditor | Widget composed of two QListViews backed by a single tree model. |
| `ConfigGroupsTree` | ConfigGroupsTree | A tree widget that displays configuration groups. |
| `ConfigWizard` | ConfigWizard | Hardware Configuration Wizard for Micro-Manager. |
| `ConfigurationWidget` | ConfigurationWidget | A Widget to select and load a micromanager system configuration. |
| `CoreLogWidget` | CoreLogWidget | High-performance log console with pause, follow-tail, clear, and initial load. |
| `DefaultCameraExposureWidget` | DefaultCameraExposureWidget | A Widget to get/set exposure on the default camera. |
| `ExposureWidget` | ExposureWidget | A Widget to get/set exposure on a camera. |
| `GridPlanWidget` | GridPlanWidget | Widget to edit a [`useq-schema` GridPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#grid-plans>). |
| `GroupPresetTableWidget` | GroupPresetTableWidget | A Widget to view and set micromanager group presets. |
| `HCSWizard` | HCSWizard | A wizard to setup an High Content Screening (HCS) experiment. |
| `ImagePreview` | ImagePreview | A Widget that displays the last image snapped by active core. |
| `InstallWidget` | InstallWidget | Widget to manage installation of MicroManager. |
| `LiveButton` | LiveButton | A Widget to create a two-state (on-off) live mode QPushButton. |
| `MDASequenceWidget` | MDASequenceWidget | A widget that provides a GUI to construct and edit a `useq.MDASequence`. |
| `MDAWidget` | MDAWidget | Main MDA Widget connected to a `pymmcore_plus.CMMCorePlus` instance. |
| `ObjectivesPixelConfigurationWidget` | ObjectivesPixelConfigurationWidget | A Widget to define the pixel size configurations using the objective device. |
| `ObjectivesWidget` | ObjectivesWidget | A QComboBox-based Widget to select the microscope objective. |
| `PixelConfigurationWidget` | PixelConfigurationWidget | A Widget to define the pixel size configurations. |
| `PositionTable` | PositionTable | Table to edit a list of [useq.Position](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#useq.Position>). |
| `PresetsWidget` | PresetsWidget | A Widget to create a QCombobox containing the presets of the specified group. |
| `PropertiesWidget` | PropertiesWidget | Convenience container to control a specific set of PropertyWidgets. |
| `PropertyBrowser` | PropertyBrowser | A Widget to browse and change properties of all devices. |
| `PropertyWidget` | PropertyWidget | Widget to display and control a single device property. |
| `ShuttersWidget` | ShuttersWidget | A Widget to control shutters and Micro-Manager autoshutter. |
| `SnapButton` | SnapButton | Create a snap QPushButton. |
| `StageExplorer` | StageExplorer | A stage positions explorer widget. |
| `StageWidget` | StageWidget | A Widget to control a XY and/or a Z stage. |
| `TimePlanWidget` | TimePlanWidget | Table to edit a [useq.TimePlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#time-plans>). |
| `ZPlanWidget` | ZPlanWidget | Widget to edit a [useq.ZPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#z-plans>). |
