# pymmcore\_plus.experimental.unicore

Classes:

| Name | Description |
| --- | --- |
| `CameraDevice` |  |
| `Device` | ABC for all Devices. |
| `GenericDevice` | Generic device API, e.g. for devices that don't fit into other categories. |
| `HubDevice` | ABC for Hub devices that can have peripheral devices attached. |
| `PropertyInfo` | State of a property of a device. |
| `SLMDevice` | ABC for Spatial Light Modulator (SLM) devices. |
| `ShutterDevice` | Shutter device API, e.g. for physical shutters or electronic shutter control. |
| `SimpleCameraDevice` | A convenience subclass of `CameraDevice` for simple/simulated cameras. |
| `StageDevice` | ABC for Stage devices. |
| `StateDevice` | State device API, e.g. filter wheel, objective turret, etc. |
| `UniMMCore` | Unified Core object that first checks for python, then C++ devices. |
| `XYStageDevice` | ABC for XYStage devices. |
| `XYStepperStageDevice` | ABC for XYStage devices that support stepper motors. |

Functions:

| Name | Description |
| --- | --- |
| `pymm_property` | Decorates a (getter) method to create a device property. |

## CameraDevice

```python
CameraDevice()
```

Bases: `Device`

Methods:

| Name | Description |
| --- | --- |
| `get_exposure` | Get the current exposure time in milliseconds. |
| `set_exposure` | Set the exposure time in milliseconds. |
| `shape` | Return the shape of the current image buffer. |
| `dtype` | Return the data type of the image buffer. |
| `start_sequence` | Start a sequence acquisition. |
| `register_standard_properties` | Inspect the class for standard properties and register them. |
| `get_roi` | Return the current ROI as `(x, y, width, height)`. |
| `set_roi` | Set the ROI. |
| `clear_roi` | Reset the ROI to the full sensor frame. |
| `get_binning` | Get the binning factor for the camera. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `STANDARD_PROPERTIES` | `ClassVar` |  |

### STANDARD\_PROPERTIES

```python
STANDARD_PROPERTIES: ClassVar = MappingProxyType(
    {
        Keyword.ActualInterval_ms: ("actual_interval_ms", float),
        Keyword.Binning: ("binning", int),
        Keyword.CameraID: ("camera_id", str),
        Keyword.CameraName: ("camera_name", str),
        Keyword.CCDTemperature: ("ccd_temperature", float),
        Keyword.CCDTemperatureSetPoint: ("ccd_temperature_set_point", float),
        Keyword.EMGain: ("em_gain", float),
        Keyword.Exposure: ("exposure", float),
        Keyword.Gain: ("gain", float),
        Keyword.Interval_ms: ("interval_ms", float),
        Keyword.Offset: ("offset", float),
        "PixelFormat": ("pixel_format", PixelFormat),
        Keyword.ReadoutMode: ("readout_mode", str),
        Keyword.ReadoutTime: ("readout_time", float),
        Keyword.Metadata_ROI_X: ("roi_x", int),
        Keyword.Metadata_ROI_Y: ("roi_y", int),
    }
)
```

### get\_exposure

```python
get_exposure() -> float
```

Get the current exposure time in milliseconds.

### set\_exposure

```python
set_exposure(exposure: float) -> None
```

Set the exposure time in milliseconds.

### shape

```python
shape() -> tuple[int, int] | tuple[int, int, int]
```

Return the shape of the current image buffer.

This is used when querying Height, Width *and* number of components. If the camera is grayscale, it should return (height, width). If the camera is color, it should return (height, width, n\_channels).

If the camera supports ROI, this should return the ROI dimensions.

### dtype

```python
dtype() -> DTypeLike
```

Return the data type of the image buffer.

### start\_sequence

```python
start_sequence(
    n: int | None, get_buffer: Callable[[Sequence[int], DTypeLike], ndarray]
) -> Iterator[Mapping]
```

Start a sequence acquisition.

This method should be implemented by the camera device adapter and should yield metadata for each acquired image. The implementation should call get\_buffer() to get a buffer, fill it with image data, then yield the metadata for that image.

The core will handle threading and synchronization. This function may block.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `n` | `int \| None` | If an integer, this is the number of images to acquire. If None, the camera should acquire images indefinitely until stopped. | *required* |
| `get_buffer` | `Callable[[Sequence[int], DTypeLike], ndarray]` | A callable that returns a buffer for the camera to fill with image data. You should call this with the shape of the image and the dtype of the image data. The core will produce a buffer of the requested shape and dtype, and you should fill it (in place) with the image data. | *required* |

Yields:

| Type | Description |
| --- | --- |
| `Mapping` | Metadata for each acquired image. This should be yielded after the corresponding buffer has been filled with image data. |

### register\_standard\_properties

```python
register_standard_properties() -> None
```

Inspect the class for standard properties and register them.

### get\_roi

```python
get_roi() -> tuple[int, int, int, int]
```

Return the current ROI as `(x, y, width, height)`.

The default implementation returns the full frame from `shape()`. Override in subclasses to support hardware ROI.

### set\_roi

```python
set_roi(x: int, y: int, width: int, height: int) -> None
```

Set the ROI.

The default implementation raises `NotImplementedError`. Override in subclasses to support hardware ROI.

### clear\_roi

```python
clear_roi() -> None
```

Reset the ROI to the full sensor frame.

No-op by default (nothing was set, nothing to clear).

### get\_binning

```python
get_binning() -> int
```

Get the binning factor for the camera.

## Device

```python
Device()
```

Bases: `_Lockable`, `ABC`

ABC for all Devices.

Methods:

| Name | Description |
| --- | --- |
| `register_property` | Manually register a property. |
| `initialize` | Initialize the device. |
| `shutdown` | Shutdown the device. |
| `get_label` |  |
| `type` | Return the type of the device. |
| `name` | Return the name of the device. |
| `description` | Return a description of the device. |
| `busy` | Return `True` if the device is busy. |
| `has_property` | Return `True` if the device has a property with the given name. |
| `get_property_names` | Return the names of the properties. |
| `get_property_info` | Return the property controller for a property. |
| `get_property_value` | Return the value of a property. |
| `set_property_value` | Set the value of a property. |
| `set_property_allowed_values` | Set the allowed values of a property. |
| `set_property_limits` | Set the limits of a property. |
| `set_property_sequence_max_length` | Set the sequence max length of a property. |
| `load_property_sequence` | Load a sequence into a property. |
| `start_property_sequence` | Start a sequence of a property. |
| `stop_property_sequence` | Stop a sequence of a property. |
| `is_property_sequenceable` | Return `True` if the property is sequenceable. |
| `is_property_read_only` | Return `True` if the property is read-only. |
| `get_parent_label` | Return the label of the parent hub device, or empty string if none. |
| `set_parent_label` | Set the label of the parent hub device. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `core` | `CMMCoreProxy` | The device may use this to access a restricted subset of the Core API. |

### core

```python
core: CMMCoreProxy
```

The device may use this to access a restricted subset of the Core API.

### register\_property

```python
register_property(
    name: str,
    *,
    default_value: TProp | None = None,
    getter: Callable[[TDev], TProp] | None = None,
    setter: Callable[[TDev, TProp], None] | None = None,
    limits: tuple[int | float, int | float] | None = None,
    sequence_max_length: int = 0,
    allowed_values: Sequence[TProp] | None = None,
    is_read_only: bool = False,
    is_pre_init: bool = False,
    property_type: PropArg = None,
    sequence_loader: Callable[[TDev, Sequence[TProp]], None] | None = None,
    sequence_starter: Callable[[TDev], None] | None = None,
    sequence_stopper: Callable[[TDev], None] | None = None,
) -> None
```

Manually register a property.

This is an alternative to using the `@pymm_property` decorator. It can be used to register properties that are not defined in the class body. This is useful for pure "user-side" properties that are not used by the adapter, but which the adapter may want to access (such as a preference or a configuration setting that doesn't affect the device's behavior, but which the adapter may want to read).

Properties defined this way are not accessible as class attributes.

### initialize

```python
initialize() -> None
```

Initialize the device.

### shutdown

```python
shutdown() -> None
```

Shutdown the device.

### get\_label

```python
get_label() -> str
```

### type

```python
type() -> DeviceType
```

Return the type of the device.

### name

```python
name() -> str
```

Return the name of the device.

### description

```python
description() -> str
```

Return a description of the device.

### busy

```python
busy() -> bool
```

Return `True` if the device is busy.

### has\_property

```python
has_property(prop_name: str) -> bool
```

Return `True` if the device has a property with the given name.

### get\_property\_names

```python
get_property_names() -> KeysView[str]
```

Return the names of the properties.

### get\_property\_info

```python
get_property_info(prop_name: str) -> PropertyInfo
```

Return the property controller for a property.

### get\_property\_value

```python
get_property_value(prop_name: str) -> Any
```

Return the value of a property.

### set\_property\_value

```python
set_property_value(prop_name: str, value: Any) -> None
```

Set the value of a property.

### set\_property\_allowed\_values

```python
set_property_allowed_values(
    prop_name: str, allowed_values: Sequence[Any]
) -> None
```

Set the allowed values of a property.

### set\_property\_limits

```python
set_property_limits(prop_name: str, limits: tuple[float, float] | None) -> None
```

Set the limits of a property.

### set\_property\_sequence\_max\_length

```python
set_property_sequence_max_length(prop_name: str, max_length: int) -> None
```

Set the sequence max length of a property.

### load\_property\_sequence

```python
load_property_sequence(prop_name: str, sequence: Sequence[Any]) -> None
```

Load a sequence into a property.

### start\_property\_sequence

```python
start_property_sequence(prop_name: str) -> None
```

Start a sequence of a property.

### stop\_property\_sequence

```python
stop_property_sequence(prop_name: str) -> None
```

Stop a sequence of a property.

### is\_property\_sequenceable

```python
is_property_sequenceable(prop_name: str) -> bool
```

Return `True` if the property is sequenceable.

### is\_property\_read\_only

```python
is_property_read_only(prop_name: str) -> bool
```

Return `True` if the property is read-only.

### get\_parent\_label

```python
get_parent_label() -> str
```

Return the label of the parent hub device, or empty string if none.

### set\_parent\_label

```python
set_parent_label(parent_label: str) -> None
```

Set the label of the parent hub device.

## GenericDevice

```python
GenericDevice()
```

Bases: `Device`

Generic device API, e.g. for devices that don't fit into other categories.

Generic Devices generally only use the device property interface.

## HubDevice

```python
HubDevice()
```

Bases: `Device`

ABC for Hub devices that can have peripheral devices attached.

Hub devices represent a central device (e.g., a controller) that can have multiple peripheral devices attached to it. Examples include multi-channel controllers, or devices that manage multiple sub-devices.

To implement a Hub device, simply override `get_installed_peripherals()`:

```python
class MyHub(HubDevice):
    def get_installed_peripherals(self) -> Sequence[tuple[str, str]]:
        return [
            ("Motor1", "First motor controller"),
            ("Motor2", "Second motor controller"),
        ]
```

If your hub needs to perform expensive detection (e.g., scanning a bus), implement caching inside your `get_installed_peripherals()` method.

Methods:

| Name | Description |
| --- | --- |
| `get_installed_peripherals` | Return information about installed peripheral devices. |

### get\_installed\_peripherals

```python
get_installed_peripherals() -> Sequence[tuple[str, str]]
```

Return information about installed peripheral devices.

Override this method to return a sequence of `tuple[str, str]` objects describing all devices that can be loaded as peripherals of this hub.

Returns:

| Type | Description |
| --- | --- |
| `Sequence[tuple[str, str]]` | A sequence of (name, description) tuples for each available peripheral. The name MUST be the name of a class, importable from the same module as this hub. |

## PropertyInfo

```python
PropertyInfo(
    *,
    name: str,
    default_value: TProp | None = None,
    last_value: TProp | None = None,
    limits: tuple[int | float, int | float] | None = None,
    sequence_max_length: int = 0,
    description: str | None = None,
    type: PropertyType = Undef,
    allowed_values: Sequence[TProp] | None = None,
    is_read_only: bool | None = None,
    is_pre_init: bool = False,
)
```

Bases: `Generic[TProp]`

State of a property of a device.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` |  | *required* |
| `default_value` | `TProp \| None` |  | `None` |
| `last_value` | `TProp \| None` |  | `None` |
| `limits` | `tuple[int \| float, int \| float] \| None` |  | `None` |
| `sequence_max_length` | `int` |  | `0` |
| `description` | `str \| None` |  | `None` |
| `type` | `PropertyType` |  | `undefined` |
| `allowed_values` | `Sequence[TProp] \| None` |  | `None` |
| `is_read_only` | `bool \| None` |  | `None` |
| `is_pre_init` | `bool` |  | `False` |

### name

```python
name: str
```

### default\_value

```python
default_value: TProp | None = None
```

### last\_value

```python
last_value: TProp | None = None
```

### limits

```python
limits: tuple[int | float, int | float] | None = None
```

### sequence\_max\_length

```python
sequence_max_length: int = 0
```

### description

```python
description: str | None = None
```

### type

```python
type: PropertyType = PropertyType.Undef
```

### allowed\_values

```python
allowed_values: Sequence[TProp] | None = None
```

### is\_read\_only

```python
is_read_only: bool | None = None
```

### is\_pre\_init

```python
is_pre_init: bool = False
```

### number\_of\_allowed\_values

```python
number_of_allowed_values: int
```

Return the number of allowed values.

### is\_sequenceable

```python
is_sequenceable: bool
```

Return True if the property is sequenceable.

## SLMDevice

```python
SLMDevice(*args: Any, **kwargs: Any)
```

Bases: `SequenceableDevice[ndarray]`

ABC for Spatial Light Modulator (SLM) devices.

SLM devices are capable of displaying images. They are expected to represent a rectangular grid of pixels that can be either 8-bit or 32-bit. Illumination (light source on or off) is logically independent of displaying the image.

Methods:

| Name | Description |
| --- | --- |
| `shape` | Return the shape of the SLM image buffer. |
| `dtype` | Return the data type of the image buffer. |
| `set_image` | Load the image into the SLM device adapter. |
| `get_image` | Get the current image from the SLM device adapter. |
| `display_image` | Command the SLM to display the loaded image. |
| `set_exposure` | Command the SLM to turn off after a specified interval. |
| `get_exposure` | Find out the exposure interval of an SLM. |
| `get_sequence_max_length` | Return the maximum length of an image sequence that can be uploaded. |
| `send_sequence` | Load a sequence of images to the SLM. |
| `start_sequence` | Start a sequence of images on the SLM. |
| `stop_sequence` | Stop a sequence of images on the SLM. |

### shape

```python
shape() -> tuple[int, ...]
```

Return the shape of the SLM image buffer.

This is used when querying Width, Height, *and* number of components. If the SLM is grayscale, it should return (width, height). If the SLM is color, it should return (width, height, n\_channels).

### dtype

```python
dtype() -> DTypeLike
```

Return the data type of the image buffer.

### set\_image

```python
set_image(pixels: ndarray) -> None
```

Load the image into the SLM device adapter.

### get\_image

```python
get_image() -> ndarray
```

Get the current image from the SLM device adapter.

This is useful for verifying that the image was set correctly.

### display\_image

```python
display_image() -> None
```

Command the SLM to display the loaded image.

### set\_exposure

```python
set_exposure(interval_ms: float) -> None
```

Command the SLM to turn off after a specified interval.

### get\_exposure

```python
get_exposure() -> float
```

Find out the exposure interval of an SLM.

### get\_sequence\_max\_length

```python
get_sequence_max_length() -> int
```

Return the maximum length of an image sequence that can be uploaded.

### send\_sequence

```python
send_sequence(sequence: Sequence[ndarray]) -> None
```

Load a sequence of images to the SLM.

### start\_sequence

```python
start_sequence() -> None
```

Start a sequence of images on the SLM.

### stop\_sequence

```python
stop_sequence() -> None
```

Stop a sequence of images on the SLM.

## ShutterDevice

```python
ShutterDevice()
```

Bases: `Device`

Shutter device API, e.g. for physical shutters or electronic shutter control.

Or any 2-state device that can be either open or closed.

Methods:

| Name | Description |
| --- | --- |
| `get_open` | Return True if the shutter is open, False if it is closed. |
| `set_open` | Set the shutter to open or closed. |

### get\_open

```python
get_open() -> bool
```

Return True if the shutter is open, False if it is closed.

### set\_open

```python
set_open(open: bool) -> None
```

Set the shutter to open or closed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `open` | `bool` | True to open the shutter, False to close it. | *required* |

## SimpleCameraDevice

```python
SimpleCameraDevice()
```

Bases: `CameraDevice`

A convenience subclass of `CameraDevice` for simple/simulated cameras.

Instead of implementing `start_sequence()` and `shape()` directly, subclasses only need to implement:

- `sensor_shape()`: the full (height, width) of the sensor
- `snap(buffer)`: fill the provided **full-frame** buffer with image data and return metadata. The buffer is always sized to `sensor_shape()`. If a ROI is active, cropping is handled automatically by this base class.

Software ROI (`set_roi` / `clear_roi`) works out of the box.

.. warning:: This class is **not** recommended for real hardware cameras that need efficient ring-buffer or hardware-triggered acquisition. For those, use subclass `CameraDevice` directly and implement `start_sequence()`.

Methods:

| Name | Description |
| --- | --- |
| `sensor_shape` | Return the full sensor shape `(height, width[, n_channels])`. |
| `snap` | Snap a single image into the provided full-frame buffer. |
| `shape` | Return the current image shape, accounting for any active ROI. |
| `get_roi` | Return the current ROI as `(x, y, width, height)`. |
| `set_roi` | Set the software ROI, validating bounds against the sensor shape. |
| `clear_roi` | Reset the ROI to the full sensor frame. |
| `start_sequence` | Loop over `snap()`, cropping to the active ROI if set. |

### sensor\_shape

```python
sensor_shape() -> tuple[int, int] | tuple[int, int, int]
```

Return the full sensor shape `(height, width[, n_channels])`.

### snap

```python
snap(buffer: ndarray) -> Mapping
```

Snap a single image into the provided full-frame buffer.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `buffer` | `ndarray` | Pre-allocated buffer shaped to `sensor_shape()`. **Must** be filled with full-frame image data every time. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Mapping` | Metadata for the acquired image. |

### shape

```python
shape() -> tuple[int, int] | tuple[int, int, int]
```

Return the current image shape, accounting for any active ROI.

### get\_roi

```python
get_roi() -> tuple[int, int, int, int]
```

Return the current ROI as `(x, y, width, height)`.

### set\_roi

```python
set_roi(x: int, y: int, width: int, height: int) -> None
```

Set the software ROI, validating bounds against the sensor shape.

### clear\_roi

```python
clear_roi() -> None
```

Reset the ROI to the full sensor frame.

### start\_sequence

```python
start_sequence(
    n: int | None, get_buffer: Callable[[Sequence[int], DTypeLike], ndarray]
) -> Iterator[Mapping]
```

Loop over `snap()`, cropping to the active ROI if set.

## StageDevice

```python
StageDevice(*args: Any, **kwargs: Any)
```

Bases: `_BaseStage[float]`

ABC for Stage devices.

Methods:

| Name | Description |
| --- | --- |
| `set_position_um` | Set the position of the stage in microns. |
| `get_position_um` | Returns the current position of the stage in microns. |
| `get_focus_direction` | Returns the focus direction of the stage. |
| `set_focus_direction` | Sets the focus direction of the stage. |
| `set_relative_position_um` | Move the stage by a relative amount. |
| `set_adapter_origin_um` | Enable software translation of coordinates. |
| `is_linear_sequenceable` | Return True if the stage supports linear sequences. |
| `set_linear_sequence` | Load a linear sequence defined by step size and number of slices. |
| `is_continuous_focus_drive` | Return True if positions can be set while continuous focus runs. |

### set\_position\_um

```python
set_position_um(val: float) -> None
```

Set the position of the stage in microns.

### get\_position\_um

```python
get_position_um() -> float
```

Returns the current position of the stage in microns.

### get\_focus\_direction

```python
get_focus_direction() -> FocusDirection
```

Returns the focus direction of the stage.

### set\_focus\_direction

```python
set_focus_direction(sign: int) -> None
```

Sets the focus direction of the stage.

### set\_relative\_position\_um

```python
set_relative_position_um(d: float) -> None
```

Move the stage by a relative amount.

Can be overridden for more efficient implementations.

### set\_adapter\_origin\_um

```python
set_adapter_origin_um(newZUm: float) -> None
```

Enable software translation of coordinates.

The current position of the stage becomes Z = newZUm. Only some stages support this functionality; it is recommended that set\_origin() be used instead where available.

### is\_linear\_sequenceable

```python
is_linear_sequenceable() -> bool
```

Return True if the stage supports linear sequences.

A linear sequence is defined by a step size and number of slices.

### set\_linear\_sequence

```python
set_linear_sequence(dZ_um: float, nSlices: int) -> None
```

Load a linear sequence defined by step size and number of slices.

### is\_continuous\_focus\_drive

```python
is_continuous_focus_drive() -> bool
```

Return True if positions can be set while continuous focus runs.

## StateDevice

```python
StateDevice(state_labels: Mapping[int, str] | Iterable[tuple[int, str]])
```

Bases: `Device`

State device API, e.g. filter wheel, objective turret, etc.

A state device is a device that at any point in time is in a single state out of a list of possible states, like a filter wheel, an objective turret, etc. The interface contains functions to get and set the state, to give states human readable labels, and functions to make it possible to treat the state device as a shutter.

In terms of implementation, this base class provides the basic functionality by presenting state and label as properties, which it keeps in sync with the underlying device.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `state_labels` | `Mapping[int, str] \| Iterable[tuple[int, str]]` | A mapping (or iterable of 2-tuples) of integer state indices to string labels. | *required* |

Methods:

| Name | Description |
| --- | --- |
| `get_state` | Get the current state of the device (integer index). |
| `set_state` | Set the state of the device (integer index). |
| `from_count` | Simplified constructor with just a number of states. |
| `register_standard_properties` | Inspect the class for standard properties and register them. |
| `set_position_or_label` | Set the position of the device by index or label. |
| `assign_label_to_position` | Assign a User-defined label to a position. |
| `get_position_for_label` | Return the position corresponding to the provided label. |

### get\_state

```python
get_state() -> int
```

Get the current state of the device (integer index).

### set\_state

```python
set_state(position: int) -> None
```

Set the state of the device (integer index).

### from\_count

```python
from_count(count: int) -> Self
```

Simplified constructor with just a number of states.

### register\_standard\_properties

```python
register_standard_properties() -> None
```

Inspect the class for standard properties and register them.

### set\_position\_or\_label

```python
set_position_or_label(pos_or_label: int | str) -> None
```

Set the position of the device by index or label.

### assign\_label\_to\_position

```python
assign_label_to_position(pos: int, label: str) -> None
```

Assign a User-defined label to a position.

### get\_position\_for\_label

```python
get_position_for_label(label: str) -> int
```

Return the position corresponding to the provided label.

## UniMMCore

```python
UniMMCore(*args: Any, **kwargs: Any)
```

Bases: `CMMCorePlus`

Unified Core object that first checks for python, then C++ devices.

Methods:

| Name | Description |
| --- | --- |
| `loadSystemConfiguration` | Load a system config file conforming to the MM `.cfg` format. |
| `saveSystemConfiguration` | Save the current system configuration to a text file. |
| `loadDevice` | Loads a device from the plugin library, or python module. |
| `loadPyDevice` | Load a `unicore.Device` as a python device. |
| `isPyDevice` | Returns True if the specified device label corresponds to a Python device. |
| `unloadDevice` |  |
| `unloadAllDevices` |  |
| `reset` |  |
| `initializeDevice` |  |
| `initializeAllDevices` |  |
| `getDeviceInitializationState` |  |
| `getLoadedDevices` |  |
| `getLoadedDevicesOfType` |  |
| `getDeviceType` |  |
| `getDeviceLibrary` |  |
| `getDeviceName` |  |
| `getDeviceDescription` |  |
| `getParentLabel` |  |
| `setParentLabel` |  |
| `getInstalledDevices` |  |
| `getLoadedPeripheralDevices` |  |
| `getInstalledDeviceDescription` |  |
| `getDevicePropertyNames` |  |
| `hasProperty` |  |
| `getProperty` |  |
| `getPropertyFromCache` |  |
| `setProperty` |  |
| `getPropertyType` |  |
| `hasPropertyLimits` |  |
| `getPropertyLowerLimit` |  |
| `getPropertyUpperLimit` |  |
| `getAllowedPropertyValues` |  |
| `isPropertyPreInit` |  |
| `isPropertyReadOnly` |  |
| `isPropertySequenceable` |  |
| `getPropertySequenceMaxLength` |  |
| `loadPropertySequence` |  |
| `startPropertySequence` |  |
| `stopPropertySequence` |  |
| `deviceBusy` |  |
| `waitForDevice` |  |
| `waitForConfig` |  |
| `systemBusy` |  |
| `waitForSystem` |  |
| `waitForDeviceType` |  |
| `deviceTypeBusy` |  |
| `getDeviceDelayMs` |  |
| `setDeviceDelayMs` |  |
| `usesDeviceDelay` |  |
| `setXYStageDevice` |  |
| `getXYStageDevice` | Returns the label of the currently selected XYStage device. |
| `setXYPosition` | Sets the position of the XY stage in microns. |
| `getXYPosition` | Obtains the current position of the XY stage in microns. |
| `getXPosition` | Obtains the current position of the X axis of the XY stage in microns. |
| `getYPosition` | Obtains the current position of the Y axis of the XY stage in microns. |
| `getXYStageSequenceMaxLength` | Gets the maximum length of an XY stage's position sequence. |
| `isXYStageSequenceable` | Queries XY stage if it can be used in a sequence. |
| `loadXYStageSequence` | Transfer a sequence of stage positions to the xy stage. |
| `setOriginX` | Zero the given XY stage's X coordinate at the current position. |
| `setOriginY` | Zero the given XY stage's Y coordinate at the current position. |
| `setOriginXY` | Zero the given XY stage's coordinates at the current position. |
| `setAdapterOriginXY` | Enable software translation of coordinates for the current XY stage. |
| `setRelativeXYPosition` | Sets the relative position of the XY stage in microns. |
| `startXYStageSequence` | Starts an ongoing sequence of triggered events in an XY stage. |
| `stopXYStageSequence` | Stops an ongoing sequence of triggered events in an XY stage. |
| `getFocusDevice` | Return the current Focus Device. |
| `setFocusDevice` | Set new current Focus Device. |
| `getPosition` |  |
| `setPosition` |  |
| `setFocusDirection` |  |
| `getFocusDirection` | Get the current focus direction of the Z stage. |
| `setOrigin` | Zero the current focus/Z stage's coordinates at the current position. |
| `setRelativePosition` | Sets the relative position of the stage in microns. |
| `setAdapterOrigin` | Enable software translation of coordinates for the current focus/Z stage. |
| `isStageSequenceable` | Queries stage if it can be used in a sequence. |
| `isStageLinearSequenceable` | Queries if the stage can be used in a linear sequence. |
| `getStageSequenceMaxLength` | Gets the maximum length of a stage's position sequence. |
| `loadStageSequence` | Transfer a sequence of stage positions to the stage. |
| `startStageSequence` | Starts an ongoing sequence of triggered events in a stage. |
| `stopStageSequence` | Stops an ongoing sequence of triggered events in a stage. |
| `setStageLinearSequence` | Loads a linear sequence (defined by step size and nr. of steps). |
| `isContinuousFocusDrive` | Check if a stage has continuous focusing capability. |
| `home` | Perform a hardware homing operation for an XY or focus/Z stage. |
| `stop` | Stop the XY or focus/Z stage. |
| `setCameraDevice` | Set the camera device. |
| `getCameraDevice` | Returns the label of the currently selected camera device. |
| `getImage` |  |
| `isSequenceRunning` |  |
| `getRemainingImageCount` |  |
| `getLastImage` |  |
| `getLastImageMD` |  |
| `getNBeforeLastImageMD` |  |
| `popNextImage` |  |
| `popNextImageMD` |  |
| `setCircularBufferMemoryFootprint` | Set the circular buffer memory footprint in MB. |
| `initializeCircularBuffer` | Initialize the circular buffer. |
| `getBufferFreeCapacity` | Get the number of free slots in the circular buffer. |
| `getBufferTotalCapacity` | Get the total capacity of the circular buffer. |
| `getCircularBufferMemoryFootprint` | Get the circular buffer memory footprint in MB. |
| `clearCircularBuffer` | Clear all images from the circular buffer. |
| `isBufferOverflowed` | Check if the circular buffer has overflowed. |
| `getImageBitDepth` |  |
| `getBytesPerPixel` |  |
| `getImageBufferSize` |  |
| `getImageHeight` |  |
| `getImageWidth` |  |
| `getNumberOfComponents` |  |
| `getNumberOfCameraChannels` |  |
| `getCameraChannelName` | Get the name of the camera channel. |
| `getExposure` | Get the exposure time in milliseconds. |
| `setExposure` | Set the exposure time in milliseconds. |
| `getROI` | Get the current region of interest (ROI) for the camera. |
| `clearROI` | Clear the current region of interest (ROI) for the camera. |
| `isExposureSequenceable` | Check if the camera supports exposure sequences. |
| `loadExposureSequence` | Transfer a sequence of exposure times to the camera. |
| `getExposureSequenceMaxLength` | Get the maximum length of the exposure sequence. |
| `startExposureSequence` | Start a sequence of exposures. |
| `stopExposureSequence` | Stop a sequence of exposures. |
| `prepareSequenceAcquisition` | Prepare the camera for sequence acquisition. |
| `getPixelSizeAffine` | Get the pixel size affine transformation matrix. |
| `getPixelSizeUm` | Get the pixel size in micrometers. |
| `setSLMDevice` | Set the SLM device. |
| `getSLMDevice` | Returns the label of the currently selected SLM device. |
| `setSLMImage` | Load the image into the SLM device adapter. |
| `getSLMImage` | Get the current image from the SLM device. |
| `setSLMPixelsTo` | Set all pixels of the SLM to a uniform intensity or RGB values. |
| `displaySLMImage` | Command the SLM to display the loaded image. |
| `setSLMExposure` | Command the SLM to turn off after a specified interval. |
| `getSLMExposure` | Find out the exposure interval of an SLM. |
| `getSLMWidth` | Returns the width of the SLM in pixels. |
| `getSLMHeight` | Returns the height of the SLM in pixels. |
| `getSLMNumberOfComponents` | Returns the number of color components (channels) in the SLM. |
| `getSLMBytesPerPixel` | Returns the number of bytes per pixel for the SLM. |
| `getSLMSequenceMaxLength` | Get the maximum length of an image sequence that can be uploaded. |
| `loadSLMSequence` | Load a sequence of images to the SLM. |
| `startSLMSequence` | Start a sequence of images on the SLM. |
| `stopSLMSequence` | Stop a sequence of images on the SLM. |
| `setState` | Set state (position) on the specific device. |
| `getState` | Return the current state (position) on the specific device. |
| `getNumberOfStates` | Return the total number of available positions (states). |
| `setStateLabel` | Set device state using the previously assigned label (string). |
| `getStateLabel` | Return the current state as the label (string). |
| `defineStateLabel` | Define a label for the specific state. |
| `getStateLabels` | Return labels for all states. |
| `getStateFromLabel` | Obtain the state for a given label. |
| `setShutterDevice` |  |
| `getShutterDevice` | Returns the label of the currently selected Shutter device. |
| `getShutterOpen` |  |
| `defineConfigGroup` |  |
| `deleteConfigGroup` |  |
| `renameConfigGroup` |  |
| `defineConfig` |  |
| `deleteConfig` |  |
| `renameConfig` |  |
| `getConfigData` |  |
| `setConfig` |  |
| `getCurrentConfig` |  |
| `getCurrentConfigFromCache` |  |
| `getConfigState` |  |
| `getConfigGroupState` |  |
| `getConfigGroupStateFromCache` |  |
| `getSystemState` | Return the entire system state including Python device properties. |
| `getSystemStateCache` |  |
| `updateSystemStateCache` | Update the system state cache for all devices including Python devices. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `load_py_device` |  |  |

### load\_py\_device

```python
load_py_device = loadPyDevice
```

### loadSystemConfiguration

```python
loadSystemConfiguration(fileName: str | Path = 'MMConfig_demo.cfg') -> None
```

Load a system config file conforming to the MM `.cfg` format.

This is a Python implementation that supports both C++ and Python devices. Lines prefixed with `#py` are processed as Python device commands but are ignored by upstream C++/pymmcore implementations.

Format example::

```text
# C++ devices
Device, Camera, DemoCamera, DCam
Property, Core, Initialize, 1

# Python devices (hidden from upstream via comment prefix)
# py pyDevice,PyCamera,mypackage.cameras,MyCameraClass
# py Property,PyCamera,Exposure,50.0
```

[https://micro-manager.org/Micro-Manager\_Configuration\_Guide\#configuration-file-syntax](<https://micro-manager.org/Micro-Manager_Configuration_Guide#configuration-file-syntax>)

For relative paths, the current working directory is first checked, then the device adapter path is checked.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `fileName` | `str \| Path` | Path to the configuration file. Defaults to "MMConfig\_demo.cfg". | `'MMConfig_demo.cfg'` |

### saveSystemConfiguration

```python
saveSystemConfiguration(
    filename: str | Path, *, prefix_py_devices: bool = True
) -> None
```

Save the current system configuration to a text file.

This saves both C++ and Python devices. Python device lines are prefixed with `#py` by default so they are ignored by upstream C++/pymmcore.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `filename` | `str \| Path` | Path to save the configuration file. | *required* |
| `prefix_py_devices` | `bool` | If True (default), Python device lines are prefixed with `#py` so they are ignored by upstream C++/pymmcore implementations, allowing config files to work with regular pymmcore. If False, Python device lines are saved without the prefix (config will only be loadable by UniMMCore). | `True` |

### loadDevice

```python
loadDevice(
    label: str, moduleName: AdapterName | str, deviceName: DeviceName | str
) -> None
```

Loads a device from the plugin library, or python module.

In the standard MM case, this will load a device from the plugin library:

```python
core.loadDevice("cam", "DemoCamera", "DCam")
```

For python devices, this will load a device from a python module:

```python
core.loadDevice("pydev", "package.module", "DeviceClass")
```

### loadPyDevice

```python
loadPyDevice(label: str, device: Device) -> None
```

Load a `unicore.Device` as a python device.

This API allows you to create python-side Device objects that can be used in tandem with the C++ devices. Whenever a method is called that would normally interact with a C++ device, this class will first check if a python device with the same label exists, and if so, use that instead.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `label` | `str` | The label to assign to the device. | *required* |
| `device` | `Device` | The device object to load. Use the appropriate subclass of `Device` for the type of device you are creating. | *required* |

### isPyDevice

```python
isPyDevice(label: DeviceLabel | str) -> bool
```

Returns True if the specified device label corresponds to a Python device.

### unloadDevice

```python
unloadDevice(label: DeviceLabel | str) -> None
```

### unloadAllDevices

```python
unloadAllDevices() -> None
```

### reset

```python
reset() -> None
```

### initializeDevice

```python
initializeDevice(label: DeviceLabel | str) -> None
```

### initializeAllDevices

```python
initializeAllDevices() -> None
```

### getDeviceInitializationState

```python
getDeviceInitializationState(label: str) -> DeviceInitializationState
```

### getLoadedDevices

```python
getLoadedDevices() -> tuple[DeviceLabel, ...]
```

### getLoadedDevicesOfType

```python
getLoadedDevicesOfType(devType: int) -> tuple[DeviceLabel, ...]
```

### getDeviceType

```python
getDeviceType(label: str) -> DeviceType
```

### getDeviceLibrary

```python
getDeviceLibrary(label: DeviceLabel | str) -> AdapterName
```

### getDeviceName

```python
getDeviceName(label: DeviceLabel | str) -> DeviceName
```

### getDeviceDescription

```python
getDeviceDescription(label: DeviceLabel | str) -> str
```

### getParentLabel

```python
getParentLabel(peripheralLabel: DeviceLabel | str) -> DeviceLabel | Literal['']
```

### setParentLabel

```python
setParentLabel(
    deviceLabel: DeviceLabel | str, parentHubLabel: DeviceLabel | str
) -> None
```

### getInstalledDevices

```python
getInstalledDevices(hubLabel: DeviceLabel | str) -> tuple[DeviceName, ...]
```

### getLoadedPeripheralDevices

```python
getLoadedPeripheralDevices(
    hubLabel: DeviceLabel | str,
) -> tuple[DeviceLabel, ...]
```

### getInstalledDeviceDescription

```python
getInstalledDeviceDescription(
    hubLabel: DeviceLabel | str, peripheralLabel: DeviceName | str
) -> str
```

### getDevicePropertyNames

```python
getDevicePropertyNames(label: DeviceLabel | str) -> tuple[PropertyName, ...]
```

### hasProperty

```python
hasProperty(label: DeviceLabel | str, propName: PropertyName | str) -> bool
```

### getProperty

```python
getProperty(label: DeviceLabel | str, propName: PropertyName | str) -> Any
```

### getPropertyFromCache

```python
getPropertyFromCache(
    deviceLabel: DeviceLabel | str, propName: PropertyName | str
) -> Any
```

### setProperty

```python
setProperty(
    label: str, propName: str, propValue: bool | float | int | str
) -> None
```

### getPropertyType

```python
getPropertyType(label: str, propName: str) -> PropertyType
```

### hasPropertyLimits

```python
hasPropertyLimits(
    label: DeviceLabel | str, propName: PropertyName | str
) -> bool
```

### getPropertyLowerLimit

```python
getPropertyLowerLimit(
    label: DeviceLabel | str, propName: PropertyName | str
) -> float
```

### getPropertyUpperLimit

```python
getPropertyUpperLimit(
    label: DeviceLabel | str, propName: PropertyName | str
) -> float
```

### getAllowedPropertyValues

```python
getAllowedPropertyValues(
    label: DeviceLabel | str, propName: PropertyName | str
) -> tuple[str, ...]
```

### isPropertyPreInit

```python
isPropertyPreInit(
    label: DeviceLabel | str, propName: PropertyName | str
) -> bool
```

### isPropertyReadOnly

```python
isPropertyReadOnly(
    label: DeviceLabel | str, propName: PropertyName | str
) -> bool
```

### isPropertySequenceable

```python
isPropertySequenceable(
    label: DeviceLabel | str, propName: PropertyName | str
) -> bool
```

### getPropertySequenceMaxLength

```python
getPropertySequenceMaxLength(
    label: DeviceLabel | str, propName: PropertyName | str
) -> int
```

### loadPropertySequence

```python
loadPropertySequence(
    label: DeviceLabel | str,
    propName: PropertyName | str,
    eventSequence: Sequence[Any],
) -> None
```

### startPropertySequence

```python
startPropertySequence(
    label: DeviceLabel | str, propName: PropertyName | str
) -> None
```

### stopPropertySequence

```python
stopPropertySequence(
    label: DeviceLabel | str, propName: PropertyName | str
) -> None
```

### deviceBusy

```python
deviceBusy(label: DeviceLabel | str) -> bool
```

### waitForDevice

```python
waitForDevice(label: DeviceLabel | str) -> None
```

### waitForConfig

```python
waitForConfig(group: str, configName: str) -> None
```

### systemBusy

```python
systemBusy() -> bool
```

### waitForSystem

```python
waitForSystem() -> None
```

### waitForDeviceType

```python
waitForDeviceType(devType: int) -> None
```

### deviceTypeBusy

```python
deviceTypeBusy(devType: int) -> bool
```

### getDeviceDelayMs

```python
getDeviceDelayMs(label: DeviceLabel | str) -> float
```

### setDeviceDelayMs

```python
setDeviceDelayMs(label: DeviceLabel | str, delayMs: float) -> None
```

### usesDeviceDelay

```python
usesDeviceDelay(label: DeviceLabel | str) -> bool
```

### setXYStageDevice

```python
setXYStageDevice(xyStageLabel: DeviceLabel | str) -> None
```

### getXYStageDevice

```python
getXYStageDevice() -> DeviceLabel | Literal['']
```

Returns the label of the currently selected XYStage device.

Returns empty string if no XYStage device is selected.

### setXYPosition

```python
setXYPosition(x: float, y: float) -> None
```

```python
setXYPosition(xyStageLabel: DeviceLabel | str, x: float, y: float) -> None
```

```python
setXYPosition(*args: Any) -> None
```

Sets the position of the XY stage in microns.

### getXYPosition

```python
getXYPosition() -> tuple[float, float]
```

```python
getXYPosition(xyStageLabel: DeviceLabel | str) -> tuple[float, float]
```

```python
getXYPosition(xyStageLabel: DeviceLabel | str = '') -> tuple[float, float]
```

Obtains the current position of the XY stage in microns.

### getXPosition

```python
getXPosition() -> float
```

```python
getXPosition(xyStageLabel: DeviceLabel | str) -> float
```

```python
getXPosition(xyStageLabel: DeviceLabel | str = '') -> float
```

Obtains the current position of the X axis of the XY stage in microns.

### getYPosition

```python
getYPosition() -> float
```

```python
getYPosition(xyStageLabel: DeviceLabel | str) -> float
```

```python
getYPosition(xyStageLabel: DeviceLabel | str = '') -> float
```

Obtains the current position of the Y axis of the XY stage in microns.

### getXYStageSequenceMaxLength

```python
getXYStageSequenceMaxLength(xyStageLabel: DeviceLabel | str) -> int
```

Gets the maximum length of an XY stage's position sequence.

### isXYStageSequenceable

```python
isXYStageSequenceable(xyStageLabel: DeviceLabel | str) -> bool
```

Queries XY stage if it can be used in a sequence.

### loadXYStageSequence

```python
loadXYStageSequence(
    xyStageLabel: DeviceLabel | str,
    xSequence: Sequence[float],
    ySequence: Sequence[float],
) -> None
```

Transfer a sequence of stage positions to the xy stage.

xSequence and ySequence must have the same length. This should only be called for XY stages that are sequenceable

### setOriginX

```python
setOriginX() -> None
```

```python
setOriginX(xyStageLabel: DeviceLabel | str) -> None
```

```python
setOriginX(xyStageLabel: DeviceLabel | str = '') -> None
```

Zero the given XY stage's X coordinate at the current position.

### setOriginY

```python
setOriginY() -> None
```

```python
setOriginY(xyStageLabel: DeviceLabel | str) -> None
```

```python
setOriginY(xyStageLabel: DeviceLabel | str = '') -> None
```

Zero the given XY stage's Y coordinate at the current position.

### setOriginXY

```python
setOriginXY() -> None
```

```python
setOriginXY(xyStageLabel: DeviceLabel | str) -> None
```

```python
setOriginXY(xyStageLabel: DeviceLabel | str = '') -> None
```

Zero the given XY stage's coordinates at the current position.

### setAdapterOriginXY

```python
setAdapterOriginXY(newXUm: float, newYUm: float) -> None
```

```python
setAdapterOriginXY(
    xyStageLabel: DeviceLabel | str, newXUm: float, newYUm: float
) -> None
```

```python
setAdapterOriginXY(*args: Any) -> None
```

Enable software translation of coordinates for the current XY stage.

The current position of the stage becomes (newXUm, newYUm). It is recommended that setOriginXY() be used instead where available.

### setRelativeXYPosition

```python
setRelativeXYPosition(dx: float, dy: float) -> None
```

```python
setRelativeXYPosition(
    xyStageLabel: DeviceLabel | str, dx: float, dy: float
) -> None
```

```python
setRelativeXYPosition(*args: Any) -> None
```

Sets the relative position of the XY stage in microns.

### startXYStageSequence

```python
startXYStageSequence(xyStageLabel: DeviceLabel | str) -> None
```

Starts an ongoing sequence of triggered events in an XY stage.

This should only be called for stages that are sequenceable

### stopXYStageSequence

```python
stopXYStageSequence(xyStageLabel: DeviceLabel | str) -> None
```

Stops an ongoing sequence of triggered events in an XY stage.

This should only be called for stages that are sequenceable

### getFocusDevice

```python
getFocusDevice() -> DeviceLabel | Literal['']
```

Return the current Focus Device.

### setFocusDevice

```python
setFocusDevice(focusLabel: str) -> None
```

Set new current Focus Device.

### getPosition

```python
getPosition() -> float
```

```python
getPosition(stageLabel: str) -> float
```

```python
getPosition(stageLabel: str | None = None) -> float
```

### setPosition

```python
setPosition(position: float) -> None
```

```python
setPosition(stageLabel: DeviceLabel | str, position: float) -> None
```

```python
setPosition(*args: Any) -> None
```

### setFocusDirection

```python
setFocusDirection(stageLabel: DeviceLabel | str, sign: int) -> None
```

### getFocusDirection

```python
getFocusDirection(stageLabel: DeviceLabel | str) -> FocusDirection
```

Get the current focus direction of the Z stage.

### setOrigin

```python
setOrigin() -> None
```

```python
setOrigin(stageLabel: DeviceLabel | str) -> None
```

```python
setOrigin(stageLabel: DeviceLabel | str | None = None) -> None
```

Zero the current focus/Z stage's coordinates at the current position.

### setRelativePosition

```python
setRelativePosition(d: float) -> None
```

```python
setRelativePosition(stageLabel: DeviceLabel | str, d: float) -> None
```

```python
setRelativePosition(*args: Any) -> None
```

Sets the relative position of the stage in microns.

### setAdapterOrigin

```python
setAdapterOrigin(newZUm: float) -> None
```

```python
setAdapterOrigin(stageLabel: DeviceLabel | str, newZUm: float) -> None
```

```python
setAdapterOrigin(*args: Any) -> None
```

Enable software translation of coordinates for the current focus/Z stage.

The current position of the stage becomes Z = newZUm. Only some stages support this functionality; it is recommended that setOrigin() be used instead where available.

### isStageSequenceable

```python
isStageSequenceable(stageLabel: DeviceLabel | str) -> bool
```

Queries stage if it can be used in a sequence.

### isStageLinearSequenceable

```python
isStageLinearSequenceable(stageLabel: DeviceLabel | str) -> bool
```

Queries if the stage can be used in a linear sequence.

A linear sequence is defined by a step size and number of slices.

### getStageSequenceMaxLength

```python
getStageSequenceMaxLength(stageLabel: DeviceLabel | str) -> int
```

Gets the maximum length of a stage's position sequence.

### loadStageSequence

```python
loadStageSequence(
    stageLabel: DeviceLabel | str, positionSequence: Sequence[float]
) -> None
```

Transfer a sequence of stage positions to the stage.

This should only be called for stages that are sequenceable.

### startStageSequence

```python
startStageSequence(stageLabel: DeviceLabel | str) -> None
```

Starts an ongoing sequence of triggered events in a stage.

This should only be called for stages that are sequenceable.

### stopStageSequence

```python
stopStageSequence(stageLabel: DeviceLabel | str) -> None
```

Stops an ongoing sequence of triggered events in a stage.

This should only be called for stages that are sequenceable.

### setStageLinearSequence

```python
setStageLinearSequence(
    stageLabel: DeviceLabel | str, dZ_um: float, nSlices: int
) -> None
```

Loads a linear sequence (defined by step size and nr. of steps).

### isContinuousFocusDrive

```python
isContinuousFocusDrive(stageLabel: DeviceLabel | str) -> bool
```

Check if a stage has continuous focusing capability.

Returns True if positions can be set while continuous focus runs.

### home

```python
home(xyOrZStageLabel: DeviceLabel | str) -> None
```

Perform a hardware homing operation for an XY or focus/Z stage.

### stop

```python
stop(xyOrZStageLabel: DeviceLabel | str) -> None
```

Stop the XY or focus/Z stage.

### setCameraDevice

```python
setCameraDevice(cameraLabel: DeviceLabel | str) -> None
```

Set the camera device.

### getCameraDevice

```python
getCameraDevice() -> DeviceLabel | Literal['']
```

Returns the label of the currently selected camera device.

Returns empty string if no camera device is selected.

### getImage

```python
getImage(*, fix: bool = True) -> ndarray
```

```python
getImage(numChannel: int, *, fix: bool = True) -> ndarray
```

```python
getImage(numChannel: int | None = None, *, fix: bool = True) -> ndarray
```

### isSequenceRunning

```python
isSequenceRunning() -> bool
```

```python
isSequenceRunning(cameraLabel: DeviceLabel | str) -> bool
```

```python
isSequenceRunning(cameraLabel: DeviceLabel | str | None = None) -> bool
```

### getRemainingImageCount

```python
getRemainingImageCount() -> int
```

### getLastImage

```python
getLastImage(*, out: ndarray | None = None) -> ndarray
```

### getLastImageMD

```python
getLastImageMD(
    channel: int, slice: int, md: Metadata, /, *, out: ndarray | None = None
) -> ndarray
```

```python
getLastImageMD(md: Metadata, /, *, out: ndarray | None = None) -> ndarray
```

```python
getLastImageMD(*args: Any, out: ndarray | None = None) -> ndarray
```

### getNBeforeLastImageMD

```python
getNBeforeLastImageMD(
    n: int, md: Metadata, /, *, out: ndarray | None = None
) -> ndarray
```

### popNextImage

```python
popNextImage(*, fix: bool = True) -> ndarray
```

### popNextImageMD

```python
popNextImageMD(channel: int, slice: int, md: Metadata) -> ndarray
```

```python
popNextImageMD(md: Metadata) -> ndarray
```

```python
popNextImageMD(*args: Any) -> ndarray
```

### setCircularBufferMemoryFootprint

```python
setCircularBufferMemoryFootprint(sizeMB: int) -> None
```

Set the circular buffer memory footprint in MB.

### initializeCircularBuffer

```python
initializeCircularBuffer() -> None
```

Initialize the circular buffer.

### getBufferFreeCapacity

```python
getBufferFreeCapacity() -> int
```

Get the number of free slots in the circular buffer.

### getBufferTotalCapacity

```python
getBufferTotalCapacity() -> int
```

Get the total capacity of the circular buffer.

### getCircularBufferMemoryFootprint

```python
getCircularBufferMemoryFootprint() -> int
```

Get the circular buffer memory footprint in MB.

### clearCircularBuffer

```python
clearCircularBuffer() -> None
```

Clear all images from the circular buffer.

### isBufferOverflowed

```python
isBufferOverflowed() -> bool
```

Check if the circular buffer has overflowed.

### getImageBitDepth

```python
getImageBitDepth() -> int
```

### getBytesPerPixel

```python
getBytesPerPixel() -> int
```

### getImageBufferSize

```python
getImageBufferSize() -> int
```

### getImageHeight

```python
getImageHeight() -> int
```

### getImageWidth

```python
getImageWidth() -> int
```

### getNumberOfComponents

```python
getNumberOfComponents() -> int
```

### getNumberOfCameraChannels

```python
getNumberOfCameraChannels() -> int
```

### getCameraChannelName

```python
getCameraChannelName(channelNr: int) -> str
```

Get the name of the camera channel.

### getExposure

```python
getExposure() -> float
```

```python
getExposure(cameraLabel: DeviceLabel | str) -> float
```

```python
getExposure(cameraLabel: DeviceLabel | str | None = None) -> float
```

Get the exposure time in milliseconds.

### setExposure

```python
setExposure(exp: float) -> None
```

```python
setExposure(cameraLabel: DeviceLabel | str, dExp: float) -> None
```

```python
setExposure(*args: Any) -> None
```

Set the exposure time in milliseconds.

### getROI

```python
getROI() -> list[int]
```

```python
getROI(label: DeviceLabel | str) -> list[int]
```

```python
getROI(label: DeviceLabel | str = '') -> list[int]
```

Get the current region of interest (ROI) for the camera.

### clearROI

```python
clearROI() -> None
```

Clear the current region of interest (ROI) for the camera.

### isExposureSequenceable

```python
isExposureSequenceable(cameraLabel: DeviceLabel | str) -> bool
```

Check if the camera supports exposure sequences.

### loadExposureSequence

```python
loadExposureSequence(
    cameraLabel: DeviceLabel | str, exposureSequence_ms: Sequence[float]
) -> None
```

Transfer a sequence of exposure times to the camera.

### getExposureSequenceMaxLength

```python
getExposureSequenceMaxLength(cameraLabel: DeviceLabel | str) -> int
```

Get the maximum length of the exposure sequence.

### startExposureSequence

```python
startExposureSequence(cameraLabel: DeviceLabel | str) -> None
```

Start a sequence of exposures.

### stopExposureSequence

```python
stopExposureSequence(cameraLabel: DeviceLabel | str) -> None
```

Stop a sequence of exposures.

### prepareSequenceAcquisition

```python
prepareSequenceAcquisition(cameraLabel: DeviceLabel | str) -> None
```

Prepare the camera for sequence acquisition.

### getPixelSizeAffine

```python
getPixelSizeAffine() -> AffineTuple
```

```python
getPixelSizeAffine(cached: bool) -> AffineTuple
```

```python
getPixelSizeAffine(cached: bool = False) -> AffineTuple
```

Get the pixel size affine transformation matrix.

### getPixelSizeUm

```python
getPixelSizeUm() -> float
```

```python
getPixelSizeUm(cached: bool) -> float
```

```python
getPixelSizeUm(cached: bool = False) -> float
```

Get the pixel size in micrometers.

### setSLMDevice

```python
setSLMDevice(slmLabel: DeviceLabel | str) -> None
```

Set the SLM device.

### getSLMDevice

```python
getSLMDevice() -> DeviceLabel | Literal['']
```

Returns the label of the currently selected SLM device.

Returns empty string if no SLM device is selected.

### setSLMImage

```python
setSLMImage(pixels: ndarray) -> None
```

```python
setSLMImage(slmLabel: DeviceLabel | str, pixels: ndarray) -> None
```

```python
setSLMImage(*args: Any) -> None
```

Load the image into the SLM device adapter.

### getSLMImage

```python
getSLMImage(slmLabel: DeviceLabel | str | None = None) -> ndarray
```

Get the current image from the SLM device.

### setSLMPixelsTo

```python
setSLMPixelsTo(intensity: int) -> None
```

```python
setSLMPixelsTo(red: int, green: int, blue: int) -> None
```

```python
setSLMPixelsTo(slmLabel: DeviceLabel | str, intensity: int) -> None
```

```python
setSLMPixelsTo(
    slmLabel: DeviceLabel | str, red: int, green: int, blue: int
) -> None
```

```python
setSLMPixelsTo(*args: Any) -> None
```

Set all pixels of the SLM to a uniform intensity or RGB values.

### displaySLMImage

```python
displaySLMImage() -> None
```

```python
displaySLMImage(slmLabel: DeviceLabel | str) -> None
```

```python
displaySLMImage(slmLabel: DeviceLabel | str | None = None) -> None
```

Command the SLM to display the loaded image.

### setSLMExposure

```python
setSLMExposure(interval_ms: float) -> None
```

```python
setSLMExposure(slmLabel: DeviceLabel | str, interval_ms: float) -> None
```

```python
setSLMExposure(*args: Any) -> None
```

Command the SLM to turn off after a specified interval.

### getSLMExposure

```python
getSLMExposure() -> float
```

```python
getSLMExposure(slmLabel: DeviceLabel | str) -> float
```

```python
getSLMExposure(slmLabel: DeviceLabel | str | None = None) -> float
```

Find out the exposure interval of an SLM.

### getSLMWidth

```python
getSLMWidth() -> int
```

```python
getSLMWidth(slmLabel: DeviceLabel | str) -> int
```

```python
getSLMWidth(slmLabel: DeviceLabel | str | None = None) -> int
```

Returns the width of the SLM in pixels.

### getSLMHeight

```python
getSLMHeight() -> int
```

```python
getSLMHeight(slmLabel: DeviceLabel | str) -> int
```

```python
getSLMHeight(slmLabel: DeviceLabel | str | None = None) -> int
```

Returns the height of the SLM in pixels.

### getSLMNumberOfComponents

```python
getSLMNumberOfComponents() -> int
```

```python
getSLMNumberOfComponents(slmLabel: DeviceLabel | str) -> int
```

```python
getSLMNumberOfComponents(slmLabel: DeviceLabel | str | None = None) -> int
```

Returns the number of color components (channels) in the SLM.

### getSLMBytesPerPixel

```python
getSLMBytesPerPixel() -> int
```

```python
getSLMBytesPerPixel(slmLabel: DeviceLabel | str) -> int
```

```python
getSLMBytesPerPixel(slmLabel: DeviceLabel | str | None = None) -> int
```

Returns the number of bytes per pixel for the SLM.

### getSLMSequenceMaxLength

```python
getSLMSequenceMaxLength(slmLabel: DeviceLabel | str) -> int
```

Get the maximum length of an image sequence that can be uploaded.

### loadSLMSequence

```python
loadSLMSequence(
    slmLabel: DeviceLabel | str, imageSequence: Sequence[bytes | ndarray]
) -> None
```

Load a sequence of images to the SLM.

### startSLMSequence

```python
startSLMSequence(slmLabel: DeviceLabel | str) -> None
```

Start a sequence of images on the SLM.

### stopSLMSequence

```python
stopSLMSequence(slmLabel: DeviceLabel | str) -> None
```

Stop a sequence of images on the SLM.

### setState

```python
setState(stateDeviceLabel: DeviceLabel | str, state: int) -> None
```

Set state (position) on the specific device.

### getState

```python
getState(stateDeviceLabel: DeviceLabel | str) -> int
```

Return the current state (position) on the specific device.

### getNumberOfStates

```python
getNumberOfStates(stateDeviceLabel: DeviceLabel | str) -> int
```

Return the total number of available positions (states).

### setStateLabel

```python
setStateLabel(stateDeviceLabel: DeviceLabel | str, stateLabel: str) -> None
```

Set device state using the previously assigned label (string).

### getStateLabel

```python
getStateLabel(stateDeviceLabel: DeviceLabel | str) -> StateLabel
```

Return the current state as the label (string).

### defineStateLabel

```python
defineStateLabel(
    stateDeviceLabel: DeviceLabel | str, state: int, label: str
) -> None
```

Define a label for the specific state.

### getStateLabels

```python
getStateLabels(stateDeviceLabel: DeviceLabel | str) -> tuple[StateLabel, ...]
```

Return labels for all states.

### getStateFromLabel

```python
getStateFromLabel(stateDeviceLabel: DeviceLabel | str, stateLabel: str) -> int
```

Obtain the state for a given label.

### setShutterDevice

```python
setShutterDevice(shutterLabel: DeviceLabel | str) -> None
```

### getShutterDevice

```python
getShutterDevice() -> DeviceLabel | Literal['']
```

Returns the label of the currently selected Shutter device.

Returns empty string if no Shutter device is selected.

### getShutterOpen

```python
getShutterOpen() -> bool
```

```python
getShutterOpen(shutterLabel: DeviceLabel | str) -> bool
```

```python
getShutterOpen(shutterLabel: DeviceLabel | str | None = None) -> bool
```

### defineConfigGroup

```python
defineConfigGroup(groupName: str) -> None
```

### deleteConfigGroup

```python
deleteConfigGroup(groupName: str) -> None
```

### renameConfigGroup

```python
renameConfigGroup(oldGroupName: str, newGroupName: str) -> None
```

### defineConfig

```python
defineConfig(groupName: str, configName: str) -> None
```

```python
defineConfig(
    groupName: str, configName: str, deviceLabel: str, propName: str, value: Any
) -> None
```

```python
defineConfig(
    groupName: str,
    configName: str,
    deviceLabel: str | None = None,
    propName: str | None = None,
    value: Any | None = None,
) -> None
```

### deleteConfig

```python
deleteConfig(groupName: str, configName: str) -> None
```

```python
deleteConfig(
    groupName: str, configName: str, deviceLabel: str, propName: str
) -> None
```

```python
deleteConfig(
    groupName: str,
    configName: str,
    deviceLabel: str | None = None,
    propName: str | None = None,
) -> None
```

### renameConfig

```python
renameConfig(groupName: str, oldConfigName: str, newConfigName: str) -> None
```

### getConfigData

```python
getConfigData(
    configGroup: str, configName: str, *, native: Literal[True]
) -> Configuration
```

```python
getConfigData(
    configGroup: str, configName: str, *, native: Literal[False] = False
) -> Configuration
```

```python
getConfigData(
    configGroup: str, configName: str, *, native: bool = False
) -> Configuration | Configuration
```

### setConfig

```python
setConfig(groupName: str, configName: str) -> None
```

### getCurrentConfig

```python
getCurrentConfig(groupName: str) -> ConfigPresetName | Literal['']
```

### getCurrentConfigFromCache

```python
getCurrentConfigFromCache(groupName: str) -> ConfigPresetName | Literal['']
```

### getConfigState

```python
getConfigState(
    group: str, config: str, *, native: bool = False
) -> Configuration | Configuration
```

### getConfigGroupState

```python
getConfigGroupState(group: str, *, native: Literal[True]) -> Configuration
```

```python
getConfigGroupState(
    group: str, *, native: Literal[False] = False
) -> Configuration
```

```python
getConfigGroupState(
    group: str, *, native: bool = False
) -> Configuration | Configuration
```

### getConfigGroupStateFromCache

```python
getConfigGroupStateFromCache(
    group: str, *, native: Literal[True]
) -> Configuration
```

```python
getConfigGroupStateFromCache(
    group: str, *, native: Literal[False] = False
) -> Configuration
```

```python
getConfigGroupStateFromCache(
    group: str, *, native: bool = False
) -> Configuration | Configuration
```

### getSystemState

```python
getSystemState(*, native: bool = False) -> Configuration | Configuration
```

Return the entire system state including Python device properties.

This method iterates through all devices (C++ and Python) and returns all property values. Following the C++ implementation pattern.

### getSystemStateCache

```python
getSystemStateCache(*, native: Literal[True]) -> Configuration
```

```python
getSystemStateCache(*, native: Literal[False] = False) -> Configuration
```

```python
getSystemStateCache(*, native: bool = False) -> Configuration | Configuration
```

### updateSystemStateCache

```python
updateSystemStateCache() -> None
```

Update the system state cache for all devices including Python devices.

This populates our Python-side cache with current values from all Python devices, then calls the C++ updateSystemStateCache.

## XYStageDevice

```python
XYStageDevice(*args: Any, **kwargs: Any)
```

Bases: `_BaseStage[tuple[float, float]]`

ABC for XYStage devices.

Methods:

| Name | Description |
| --- | --- |
| `set_position_um` | Set the position of the XY stage in microns. |
| `get_position_um` | Returns the current position of the XY stage in microns. |
| `set_origin_x` | Zero the stage's X coordinates at the current position. |
| `set_origin_y` | Zero the stage's Y coordinates at the current position. |
| `set_relative_position_um` | Move the stage by a relative amount. |
| `set_adapter_origin_um` | Alter the software coordinate translation between micrometers and steps. |
| `set_origin` | Zero the stage's coordinates at the current position. |

### set\_position\_um

```python
set_position_um(x: float, y: float) -> None
```

Set the position of the XY stage in microns.

### get\_position\_um

```python
get_position_um() -> tuple[float, float]
```

Returns the current position of the XY stage in microns.

### set\_origin\_x

```python
set_origin_x() -> None
```

Zero the stage's X coordinates at the current position.

### set\_origin\_y

```python
set_origin_y() -> None
```

Zero the stage's Y coordinates at the current position.

### set\_relative\_position\_um

```python
set_relative_position_um(dx: float, dy: float) -> None
```

Move the stage by a relative amount.

Can be overridden for more efficient implementations.

### set\_adapter\_origin\_um

```python
set_adapter_origin_um(x: float, y: float) -> None
```

Alter the software coordinate translation between micrometers and steps.

... such that the current position becomes the given coordinates.

### set\_origin

```python
set_origin() -> None
```

Zero the stage's coordinates at the current position.

This is a convenience method that calls `set_origin_x` and `set_origin_y`. Can be overridden for more efficient implementations.

## XYStepperStageDevice

```python
XYStepperStageDevice()
```

Bases: `XYStageDevice`

ABC for XYStage devices that support stepper motors.

In this variant, rather than providing `set_position_um` and `get_position_um`, you provide `set_position_steps`, `get_position_steps`, `get_step_size_x_um`, and `get_step_size_y_um`. A default implementation of `set_position_um` and `get_position_um` is then provided that uses these methods, taking into account the XY-mirroring properties of the device.

Methods:

| Name | Description |
| --- | --- |
| `set_position_steps` | Set the position of the XY stage in steps. |
| `get_position_steps` | Returns the current position of the XY stage in steps. |
| `get_step_size_x_um` | Returns the step size of the X axis in microns. |
| `get_step_size_y_um` | Returns the step size of the Y axis in microns. |
| `set_position_um` | Set the position of the XY stage in microns. |
| `get_position_um` | Get the position of the XY stage in microns. |
| `set_relative_position_steps` | Move the stage by a relative amount. |
| `set_relative_position_um` | Default implementation for relative motion. |
| `set_adapter_origin_um` | Alter the software coordinate translation between micrometers and steps. |
| `set_origin` | Zero the stage's coordinates at the current position. |
| `set_origin_x` | Zero the stage's X coordinates at the current position. |
| `set_origin_y` | Zero the stage's Y coordinates at the current position. |

### set\_position\_steps

```python
set_position_steps(x: int, y: int) -> None
```

Set the position of the XY stage in steps.

### get\_position\_steps

```python
get_position_steps() -> tuple[int, int]
```

Returns the current position of the XY stage in steps.

### get\_step\_size\_x\_um

```python
get_step_size_x_um() -> float
```

Returns the step size of the X axis in microns.

### get\_step\_size\_y\_um

```python
get_step_size_y_um() -> float
```

Returns the step size of the Y axis in microns.

### set\_position\_um

```python
set_position_um(x: float, y: float) -> None
```

Set the position of the XY stage in microns.

### get\_position\_um

```python
get_position_um() -> tuple[float, float]
```

Get the position of the XY stage in microns.

### set\_relative\_position\_steps

```python
set_relative_position_steps(dx: int, dy: int) -> None
```

Move the stage by a relative amount.

Can be overridden for more efficient implementations.

### set\_relative\_position\_um

```python
set_relative_position_um(dx: float, dy: float) -> None
```

Default implementation for relative motion.

Can be overridden for more efficient implementations.

### set\_adapter\_origin\_um

```python
set_adapter_origin_um(x: float = 0.0, y: float = 0.0) -> None
```

Alter the software coordinate translation between micrometers and steps.

... such that the current position becomes the given coordinates.

### set\_origin

```python
set_origin() -> None
```

Zero the stage's coordinates at the current position.

### set\_origin\_x

```python
set_origin_x() -> None
```

Zero the stage's X coordinates at the current position.

### set\_origin\_y

```python
set_origin_y() -> None
```

Zero the stage's Y coordinates at the current position.

## pymm\_property

```python
pymm_property(fget: Callable[[TDev], TProp]) -> PropertyController[TDev, TProp]
```

```python
pymm_property(
    *,
    allowed_values: Sequence[TProp] | None,
    sequence_max_length: int = ...,
    is_read_only: bool | None = ...,
    is_pre_init: bool = ...,
    name: str | None = ...,
    property_type: PropArg = ...,
) -> Callable[[Callable[[TDev], TProp]], PropertyController[TDev, TProp]]
```

```python
pymm_property(
    *,
    limits: tuple[TLim, TLim] | None,
    sequence_max_length: int = ...,
    is_read_only: bool | None = ...,
    is_pre_init: bool = ...,
    name: str | None = ...,
    property_type: PropArg = ...,
) -> Callable[[Callable[[TDev], TLim]], PropertyController[TDev, TLim]]
```

```python
pymm_property(
    *,
    sequence_max_length: int = ...,
    is_read_only: bool | None = ...,
    is_pre_init: bool = ...,
    name: str | None = ...,
    property_type: PropArg = ...,
) -> Callable[[Callable[[TDev], TProp]], PropertyController[TDev, TProp]]
```

```python
pymm_property(
    fget: Callable[[TDev], TProp] | None = None,
    *,
    limits: tuple[TLim, TLim] | None = None,
    sequence_max_length: int = 0,
    allowed_values: Sequence[TProp] | None = None,
    is_read_only: bool | None = None,
    is_pre_init: bool = False,
    name: str | None = None,
    property_type: PropArg = None,
) -> (
    PropertyController[TDev, TProp]
    | Callable[[Callable[[TDev], TProp]], PropertyController[TDev, TProp]]
)
```

Decorates a (getter) method to create a device property.

The returned PropertyController instance can be additionally used (similar to `@property`) to decorate `setter`, `sequence_loader`, `sequence_starter`, and/or `sequence_stopper` methods.

Properties can have limits, allowed values, but may not have both.

Properties will only be considered "sequenceable" (i.e. they support hardware triggering) if they have a non-zero sequence\_max\_length AND have decorated `sequence_loader` and `sequence_starter` methods.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `fget` | `Callable[[TDev], TProp]` | The getter method for the property, by default None. | `None` |
| `limits` | `tuple[float, float]` | The minimum and maximum values of the property, by default None. Cannot be combined with `allowed_values`. | `None` |
| `sequence_max_length` | `int` | The maximum length of a sequence of property values, by default 0. | `0` |
| `allowed_values` | `Sequence[TProp]` | The allowed values of the property, by default None. Cannot be combined with `limits`. | `None` |
| `is_read_only` | `bool` | Whether the property is read-only, by default False. | `None` |
| `is_pre_init` | `bool` | Whether the property must be set before initialization, by default False. | `False` |
| `name` | `str` | The name of the property, by default, the name of the getter method is used. | `None` |
| `property_type` | `PropArg` | The type of the property, by default the return annotation of the getter method is used (but must be one of `float`, `int`, or `str`). | `None` |

Examples:

```python
class MyDevice(Device):
    @pymm_property(limits=(0, 100), sequence_max_length=10)
    def position(self) -> float:
        # get position from device
        return 42.0

    @position.setter
    def position(self, value: float) -> None:
        print(f"Setting position to {value}")

    @position.sequence_loader
    def load_position_sequence(self, sequence: Sequence[float]) -> None:
        print(f"Loading position sequence: {sequence}")

    @position.sequence_starter
    def start_position_sequence(self) -> None:
        print("Starting position sequence")

    @pymm_property(is_read_only=True)
    def pressure(self) -> float:
        return 1.0

    @pymm_property(allowed_values=["low", "medium", "high"])
    def speed(self) -> str:
        # get speed from device
        return "medium"

    @speed.setter
    def speed(self, value: str) -> None:
        print(f"Setting speed to {value}")
```
