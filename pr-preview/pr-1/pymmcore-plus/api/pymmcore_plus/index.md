# pymmcore\_plus

pymmcore superset providing improved APIs, event handling, and a pure python acquisition engine.

Classes:

| Name | Description |
| --- | --- |
| `AbstractChangeAccumulator` | Abstract base class for accumulating a series of `setX` calls to a device. |
| `ActionType` |  |
| `CFGCommand` |  |
| `CFGGroup` |  |
| `CMMCoreSignaler` | Signals that will be emitted from CMMCorePlus objects. |
| `ConfigGroup` | Convenience object for dealing with a set of related Configuration objects. |
| `Configuration` | Encapsulation of configuration information. |
| `Device` | Convenience object-oriented device API. |
| `DeviceAdapter` | Convenience view onto a device-adapter library. |
| `DeviceDetectionStatus` | DeviceDetectionStatus from device discovery. |
| `DeviceInitializationState` | DeviceInitializationState returned by getDeviceInitializationState. |
| `DeviceProperty` | Convenience view onto a device property. |
| `DeviceType` |  |
| `FocusDirection` |  |
| `GeneratorMDASequence` |  |
| `Keyword` |  |
| `Metadata` | Subclass of `pymmcore.Metadata` with a pythonic interface. |
| `PCoreSignaler` | Declares the protocol for all signals that will be emitted from CMMCorePlus. |
| `PixelFormat` | Subset of GeniCam Pixel Format names used by pymmcore-plus. |
| `PortType` |  |
| `PropertyType` |  |

Functions:

| Name | Description |
| --- | --- |
| `configure_logging` | Configure logging for pymmcore-plus. |
| `find_micromanager` | Locate a Micro-Manager folder (for device adapters). |
| `install_pymmcore_ipy_completion` | Install the CMMCorePlus completion matcher in the current IPython session. |
| `use_micromanager` | Set the preferred Micro-Manager path. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `__version__` |  |  |

## \_\_version\_\_

```python
__version__ = version('pymmcore-plus')
```

## AbstractChangeAccumulator

```python
AbstractChangeAccumulator(zero: T)
```

Bases: `ABC`, `Generic[T]`

Abstract base class for accumulating a series of `setX` calls to a device.

A `ChangeAccumulator` is a class that accumulates a series of `setX` calls to a device, retaining an internal target value, and emitting a signal when the device has reached its target and is idle. It can be shared by multiple players (e.g. widgets, or other classes) that want to control the same device, and allows them all to issue relative/absolute moves, and be notified when the device is idle.

A common use case is to accumulate setPosition calls made to a stage device, where you might want to accumulate a series of relative moves, and snap an image only when the stage is idle after reaching its target position.

Methods:

| Name | Description |
| --- | --- |
| `add_relative` | Add a relative value to the target. |
| `set_absolute` | Assign an absolute value to the target. |
| `poll_done` | Check if the device is done moving. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `finished` |  | Signal emitted when the device has reached its target and is idle. |
| `is_moving` | `bool` | Returns True if the device is moving. |
| `target` | `T \| None` | The target position of the stage. Or None if not moving. |

### finished

```python
finished = psygnal.Signal()
```

Signal emitted when the device has reached its target and is idle.

### is\_moving

```python
is_moving: bool
```

Returns True if the device is moving.

### target

```python
target: T | None
```

The target position of the stage. Or None if not moving.

### add\_relative

```python
add_relative(delta: T) -> None
```

Add a relative value to the target.

### set\_absolute

```python
set_absolute(target: T) -> None
```

Assign an absolute value to the target.

This will reset the accumulated state and issue a move to the target position. After the move finishes, new `move_relative()` calls are interpreted relative to *target*.

### poll\_done

```python
poll_done() -> bool
```

Check if the device is done moving.

This should be called repeatedly by some event loop driver.

Returns True exactly once when: 1. The device is idle (not busy) AND 2. The last issued move command has been completed

After returning True it resets its state and will return False until the next move\_relative() call.

## ActionType

Bases: `IntEnum`

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `NoAction` |  |  |
| `BeforeGet` |  |  |
| `AfterSet` |  |  |
| `IsSequenceable` |  |  |
| `AfterLoadSequence` |  |  |
| `StartSequence` |  |  |
| `StopSequence` |  |  |

### NoAction

```python
NoAction = pymmcore.NoAction
```

### BeforeGet

```python
BeforeGet = pymmcore.BeforeGet
```

### AfterSet

```python
AfterSet = pymmcore.AfterSet
```

### IsSequenceable

```python
IsSequenceable = pymmcore.IsSequenceable
```

### AfterLoadSequence

```python
AfterLoadSequence = pymmcore.AfterLoadSequence
```

### StartSequence

```python
StartSequence = pymmcore.StartSequence
```

### StopSequence

```python
StopSequence = pymmcore.StopSequence
```

## CFGCommand

Bases: `StrEnum`

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `Device` |  |  |
| `Label` |  |  |
| `Property` |  |  |
| `Configuration` |  |  |
| `ConfigGroup` |  |  |
| `Equipment` |  |  |
| `Delay` |  |  |
| `ImageSynchro` |  |  |
| `ConfigPixelSize` |  |  |
| `PixelSize_um` |  |  |
| `PixelSizeAffine` |  |  |
| `ParentID` |  |  |
| `FocusDirection` |  |  |
| `PixelSize_dxdz` |  |  |
| `PixelSize_dydz` |  |  |
| `PixelSize_OptimalZUm` |  |  |
| `FieldDelimiters` |  |  |

### Device

```python
Device = pymmcore.g_CFGCommand_Device
```

### Label

```python
Label = pymmcore.g_CFGCommand_Label
```

### Property

```python
Property = pymmcore.g_CFGCommand_Property
```

### Configuration

```python
Configuration = pymmcore.g_CFGCommand_Configuration
```

### ConfigGroup

```python
ConfigGroup = pymmcore.g_CFGCommand_ConfigGroup
```

### Equipment

```python
Equipment = pymmcore.g_CFGCommand_Equipment
```

### Delay

```python
Delay = pymmcore.g_CFGCommand_Delay
```

### ImageSynchro

```python
ImageSynchro = pymmcore.g_CFGCommand_ImageSynchro
```

### ConfigPixelSize

```python
ConfigPixelSize = pymmcore.g_CFGCommand_ConfigPixelSize
```

### PixelSize\_um

```python
PixelSize_um = pymmcore.g_CFGCommand_PixelSize_um
```

### PixelSizeAffine

```python
PixelSizeAffine = pymmcore.g_CFGCommand_PixelSizeAffine
```

### ParentID

```python
ParentID = pymmcore.g_CFGCommand_ParentID
```

### FocusDirection

```python
FocusDirection = pymmcore.g_CFGCommand_FocusDirection
```

### PixelSize\_dxdz

```python
PixelSize_dxdz = pymmcore.g_CFGCommand_PixelSizedxdz
```

### PixelSize\_dydz

```python
PixelSize_dydz = pymmcore.g_CFGCommand_PixelSizedydz
```

### PixelSize\_OptimalZUm

```python
PixelSize_OptimalZUm = pymmcore.g_CFGCommand_PixelSizeOptimalZUm
```

### FieldDelimiters

```python
FieldDelimiters = pymmcore.g_FieldDelimiters
```

## CFGGroup

Bases: `StrEnum`

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `System` |  |  |
| `System_Startup` |  |  |
| `System_Shutdown` |  |  |
| `PixelSizeUm` |  |  |

### System

```python
System = pymmcore.g_CFGGroup_System
```

### System\_Startup

```python
System_Startup = pymmcore.g_CFGGroup_System_Startup
```

### System\_Shutdown

```python
System_Shutdown = pymmcore.g_CFGGroup_System_Shutdown
```

### PixelSizeUm

```python
PixelSizeUm = pymmcore.g_CFGGroup_PixelSizeUm
```

## CMMCoreSignaler

Bases: `SignalGroup`, `_DevicePropertyEventMixin`

Signals that will be emitted from CMMCorePlus objects.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `propertiesChanged` |  |  |
| `propertyChanged` |  |  |
| `channelGroupChanged` |  |  |
| `configGroupChanged` |  |  |
| `configSet` |  |  |
| `systemConfigurationLoaded` |  |  |
| `pixelSizeChanged` |  |  |
| `pixelSizeAffineChanged` |  |  |
| `stagePositionChanged` |  |  |
| `XYStagePositionChanged` |  |  |
| `exposureChanged` |  |  |
| `SLMExposureChanged` |  |  |
| `shutterOpenChanged` |  |  |
| `imageSnapped` |  |  |
| `sequenceAcquisitionStopped` |  |  |
| `sequenceAcquisitionStarted` | `SignalInstance` |  |
| `mdaEngineRegistered` |  |  |
| `continuousSequenceAcquisitionStarting` |  |  |
| `continuousSequenceAcquisitionStarted` |  |  |
| `sequenceAcquisitionStarting` | `SignalInstance` |  |
| `autoShutterSet` |  |  |
| `configGroupDeleted` |  |  |
| `configDeleted` |  |  |
| `configDefined` |  |  |
| `roiSet` |  |  |
| `xYStagePositionChanged` | `SignalInstance` |  |
| `sLMExposureChanged` | `SignalInstance` |  |

### propertiesChanged

```python
propertiesChanged = Signal()
```

### propertyChanged

```python
propertyChanged = Signal(str, str, str)
```

### channelGroupChanged

```python
channelGroupChanged = Signal(str)
```

### configGroupChanged

```python
configGroupChanged = Signal(str, str)
```

### configSet

```python
configSet = Signal(str, str)
```

### systemConfigurationLoaded

```python
systemConfigurationLoaded = Signal()
```

### pixelSizeChanged

```python
pixelSizeChanged = Signal(float)
```

### pixelSizeAffineChanged

```python
pixelSizeAffineChanged = Signal(float, float, float, float, float, float)
```

### stagePositionChanged

```python
stagePositionChanged = Signal(str, float)
```

### XYStagePositionChanged

```python
XYStagePositionChanged = Signal(str, float, float)
```

### exposureChanged

```python
exposureChanged = Signal(str, float)
```

### SLMExposureChanged

```python
SLMExposureChanged = Signal(str, float)
```

### shutterOpenChanged

```python
shutterOpenChanged = Signal(str, bool)
```

### imageSnapped

```python
imageSnapped = Signal(str)
```

### sequenceAcquisitionStopped

```python
sequenceAcquisitionStopped = Signal(str)
```

### sequenceAcquisitionStarted

```python
sequenceAcquisitionStarted: SignalInstance
```

### mdaEngineRegistered

```python
mdaEngineRegistered = Signal(MDAEngine, MDAEngine)
```

### continuousSequenceAcquisitionStarting

```python
continuousSequenceAcquisitionStarting = Signal()
```

### continuousSequenceAcquisitionStarted

```python
continuousSequenceAcquisitionStarted = Signal()
```

### sequenceAcquisitionStarting

```python
sequenceAcquisitionStarting: SignalInstance
```

### autoShutterSet

```python
autoShutterSet = Signal(bool)
```

### configGroupDeleted

```python
configGroupDeleted = Signal(str)
```

### configDeleted

```python
configDeleted = Signal(str, str)
```

### configDefined

```python
configDefined = Signal(str, str, str, str, str)
```

### roiSet

```python
roiSet = Signal(str, int, int, int, int)
```

### xYStagePositionChanged

```python
xYStagePositionChanged: SignalInstance
```

### sLMExposureChanged

```python
sLMExposureChanged: SignalInstance
```

## ConfigGroup

```python
ConfigGroup(group_name: str, mmcore: CMMCorePlus)
```

Bases: `MutableMapping[str, Configuration]`

Convenience object for dealing with a set of related Configuration objects.

This object behaves as a `collections.abc.MutableMapping` of `str` (configuration group name) to `Configuration` objects.

It is object type returned by `pymmcore_plus.CMMCorePlus.getConfigGroupObject`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `group_name` | `str` | The name of the configuration group to manage. (It needn't exist yet) | *required* |
| `mmcore` | `CMMCorePlus` | The core object managing this config group. | *required* |

Methods:

| Name | Description |
| --- | --- |
| `exists` | Return `True` if this ConfigGroup exists in the current configuration. |
| `create` | Create this configuration group in core (as an empty group). |
| `delete` | Delete this entire configuration group and all presets in it. |
| `iterDeviceProperties` | Iterate `DeviceProperty` for all properties in this ConfigGroup. |
| `renameConfig` | Rename a configuration in this group. |
| `setConfig` | Set the current configuration to `configName`. |
| `getCurrentConfig` | Returns the current configuration for a given group. |
| `getCurrentConfigFromCache` | Returns the current configuration for a given group from the cache. |
| `wait` | Blocks until all devices included in the configuration group ready. |
| `rename` | Rename this configuration group. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `str` | Return the name of this ConfigGroup. |
| `core` | `CMMCorePlus` | Return the `CMMCorePlus` instance to which this Device is bound. |
| `is_consistent` | `bool` | Return `True` if all presets in this group have the same properties. |

### name

```python
name: str
```

Return the name of this ConfigGroup.

### core

```python
core: CMMCorePlus
```

Return the `CMMCorePlus` instance to which this Device is bound.

### is\_consistent

```python
is_consistent: bool
```

Return `True` if all presets in this group have the same properties.

Note that a group with 0 or 1 presets is always considered consistent. If two or more presets are present, they must all have the same device properties. (values of course may vary.)

### exists

```python
exists() -> bool
```

Return `True` if this ConfigGroup exists in the current configuration.

### create

```python
create() -> None
```

Create this configuration group in core (as an empty group).

If the group already exists, this is a no-op.

### delete

```python
delete() -> None
```

Delete this entire configuration group and all presets in it.

### iterDeviceProperties

```python
iterDeviceProperties() -> Iterator[DeviceProperty]
```

Iterate `DeviceProperty` for all properties in this ConfigGroup.

Note, this only iterates over properties that are defined in the first preset of this ConfigGroup. This *should* be the same for all presets in this ConfigGroup, but it is not guaranteed. Use `is_consistent` to check if all presets in this ConfigGroup have the same properties.

### renameConfig

```python
renameConfig(oldConfigName: str, newConfigName: str) -> None
```

Rename a configuration in this group.

If the configuration does not exist, a KeyError is thrown.

### setConfig

```python
setConfig(configName: str) -> None
```

Set the current configuration to `configName`.

This actually updates the hardware state to match what is stored in the preset `configName`.

### getCurrentConfig

```python
getCurrentConfig(as_object: Literal[True]) -> Configuration
```

```python
getCurrentConfig(as_object: Literal[False] = False) -> str
```

```python
getCurrentConfig(as_object: bool = False) -> str | Configuration
```

Returns the current configuration for a given group.

### getCurrentConfigFromCache

```python
getCurrentConfigFromCache(as_object: Literal[True]) -> Configuration
```

```python
getCurrentConfigFromCache(as_object: Literal[False] = False) -> str
```

```python
getCurrentConfigFromCache(as_object: bool = False) -> str | Configuration
```

Returns the current configuration for a given group from the cache.

### wait

```python
wait(configName: str | None = None) -> None
```

Blocks until all devices included in the configuration group ready.

If `configName` not provided, then the first configuration in the group is used.

### rename

```python
rename(newGroupName: str) -> None
```

Rename this configuration group.

## Configuration

```python
Configuration()
```

Bases: `Configuration`

Encapsulation of configuration information.

This is the type of object returned by default (provided `native==False`) by: `getConfigData][pymmcore_plus.CMMCorePlus.getConfigData], [`getPixelSizeConfigData `getSystemState][pymmcore_plus.CMMCorePlus.getSystemState] [`getSystemStateCache `getConfigState][pymmcore_plus.CMMCorePlus.getConfigState] [`getConfigGroupState \`getConfigGroupStateFromCache

This class is a subclass of `pymmcore.Configuration` that implements an `collections.abc.MutableSequence` (i.e. it behaves like a Python list). It also behaves much like a `collections.abc.MutableMapping`, where the keys are 2-tuples of (deviceLabel, propertyLabel) and the values are the property values.

Note that the "order" of this collection is not well-defined, so while you *can* index with an integer, you should not rely on the order of the items in the collection. `__getitem__/__setitem__/__delitem__` all accept a 2-tuple of `(deviceLabel, propertyLabel)`.

It adds a few convenience methods:

> [!TIP]
>
> All of the methods in `pymmcore_plus.CMMCorePlus` that would have returned a `pymmcore.Configuration` in `pymmcore` (e.g. `getConfigData`, `getConfigState`, etc...). have been reimplemented to return a `pymmcore_plus.Configuration` object. This object has the same API as `pymmcore.Configuration`, but you can request a "native" (unenhanced) `pymmcore` object by passing `native=True` to the method.

Methods:

| Name | Description |
| --- | --- |
| `remove` | Remove setting for `(devLabel, propLabel)` from the configuration. |
| `append` | Add a setting to the configuration. |
| `extend` | Add all settings from another Configuration. |
| `html` | Return config representation as HTML. |
| `dict` | Return config as a nested dict {Device: {Property: Value}}. |
| `from_configuration` | Create Configuration (Plus) from pymmcore.Configuration. |
| `create` | More flexible init to create a `Configuration`. |

### remove

```python
remove(key: DevPropTuple) -> None
```

Remove setting for `(devLabel, propLabel)` from the configuration.

### append

```python
append(setting: PropertySetting | DevPropValueTuple) -> None
```

Add a setting to the configuration.

### extend

```python
extend(
    other: Configuration | Iterable[PropertySetting | DevPropValueTuple],
) -> None
```

Add all settings from another Configuration.

### html

```python
html() -> str
```

Return config representation as HTML.

### dict

```python
dict() -> dict[str, dict[str, str]]
```

Return config as a nested dict {Device: {Property: Value}}.

### from\_configuration

```python
from_configuration(config: Configuration) -> Configuration
```

Create Configuration (Plus) from pymmcore.Configuration.

### create

```python
create(*args: Any, **kwargs: Any) -> Configuration
```

More flexible init to create a `Configuration`.

Can create from: 1. A dict of dicts (outer key is device, inner key is prop) 2. A sequence of 3-tuple 3. kwargs: where the key is the device, and the value is a {prop: value} map

## Device

```python
Device(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Convenience object-oriented device API.

This is the type of object that is returned by `pymmcore_plus.CMMCorePlus.getDeviceObject`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_label` | `str` | Device label assigned to this device. | `UNASSIGNED` |
| `mmcore` | `CMMCorePlus` | CMMCorePlus instance that owns this device. | `None` |
| `type` | `DeviceType` | The type of device to create. If not specified, the type will be inferred from the core if the device is already loaded. If the device is not loaded, an error will be raised. This parameter is mainly intended for usage when calling from `CMMCorePlus.getDeviceObject()`. Otherwise, prefer using `[SpecificDeviceSubclass].create()`. | `UnknownType` |

Examples:

```pycon
>>> core = CMMCorePlus()
>>> device = Device("Camera", core)
>>> device.isLoaded()
>>> device.load("NotALib", "DCam")  # useful error
>>> device.load("DemoCamera", "DCam")
>>> device.initialize()
>>> device.load("DemoCamera", "DCam")  # no-op w/ useful warning
>>> device.properties  # tuple of DeviceProperty objects
>>> device.description()
>>> device.isBusy()
>>> device.wait()
>>> device.type()
>>> device.schema()  # JSON schema of device properties
```

Methods:

| Name | Description |
| --- | --- |
| `create` |  |
| `get_subclass` |  |
| `isBusy` | Return busy status for this device. |
| `delayMs` | Return action delay in ms for this device. |
| `setDelayMs` | Override the built-in value for the action delay. |
| `usesDelay` | Return `True` if the device will use the delay setting or not. |
| `description` | Return device description. |
| `library` | Return device library (aka module, device adapter) name. |
| `name` | Return the device name (this is not the same as the assigned label). |
| `propertyNames` | Return all property names supported by this device. |
| `getPropertyObject` | Return a `DeviceProperty` object bound to this device on this core. |
| `setProperty` | Set a device property value. |
| `getProperty` | Get a device property value. |
| `initialize` | Initialize device. |
| `unload` | Unload device from the core and adjust all configuration data. |
| `isLoaded` | Return `True` if device is loaded. |
| `load` | Load device from the plugin library. |
| `detect` | Tries to communicate to device through a given serial port. |
| `supportsDetection` | Return whether or not the device supports automatic device detection. |
| `type` | Return device type. |
| `schema` | Return dict in JSON-schema format for properties of `device_label`. |
| `wait` | Block the calling thread until device becomes non-busy. |
| `getParentLabel` | Return the parent device label of this device. |
| `setParentLabel` | Set the parent device label of this device. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `UNASSIGNED` |  |  |
| `propertyChanged` | `PSignalInstance` |  |
| `label` | `str` | Return the assigned label of this device. |
| `core` | `CMMCorePlus` | Return the `CMMCorePlus` instance to which this Device is bound. |
| `properties` | `tuple[DeviceProperty, ...]` | Get all properties supported by device as DeviceProperty objects. |

### UNASSIGNED

```python
UNASSIGNED = '__UNASSIGNED__'
```

### propertyChanged

```python
propertyChanged: PSignalInstance = _DevicePropValueSignal(
    device_label, None, mmcore
)
```

### label

```python
label: str
```

Return the assigned label of this device.

### core

```python
core: CMMCorePlus
```

Return the `CMMCorePlus` instance to which this Device is bound.

### properties

```python
properties: tuple[DeviceProperty, ...]
```

Get all properties supported by device as DeviceProperty objects.

### create

```python
create(
    device_label: str,
    mmcore: CMMCorePlus,
    device_type: type[Device] | DeviceType = Any,
) -> Self
```

### get\_subclass

```python
get_subclass(device_label: str, mmcore: CMMCorePlus) -> type[Device]
```

### isBusy

```python
isBusy() -> bool
```

Return busy status for this device.

### delayMs

```python
delayMs() -> float
```

Return action delay in ms for this device.

### setDelayMs

```python
setDelayMs(delayMs: float) -> None
```

Override the built-in value for the action delay.

### usesDelay

```python
usesDelay() -> bool
```

Return `True` if the device will use the delay setting or not.

### description

```python
description() -> str
```

Return device description.

### library

```python
library() -> str
```

Return device library (aka module, device adapter) name.

### name

```python
name() -> str
```

Return the device name (this is not the same as the assigned label).

### propertyNames

```python
propertyNames() -> tuple[str, ...]
```

Return all property names supported by this device.

### getPropertyObject

```python
getPropertyObject(property_name: str) -> DeviceProperty
```

Return a `DeviceProperty` object bound to this device on this core.

### setProperty

```python
setProperty(property_name: str, value: bool | float | int | str) -> None
```

Set a device property value.

See also, `Device.getPropertyObject`.

Examples:

```pycon
>>> camera = Device("Camera")
>>> camera.setProperty("Exposure", 100)
>>> print(camera.getProperty("Exposure"))
# or
>>> exposure = camera.getPropertyObject("Exposure")
>>> exposure.value = 100
>>> print(exposure.value)
```

### getProperty

```python
getProperty(property_name: str) -> str
```

Get a device property value.

### initialize

```python
initialize() -> None
```

Initialize device.

### unload

```python
unload() -> None
```

Unload device from the core and adjust all configuration data.

### isLoaded

```python
isLoaded() -> bool
```

Return `True` if device is loaded.

### load

```python
load(
    adapter_name: str = "", device_name: str = "", device_label: str = ""
) -> Device
```

Load device from the plugin library.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `adapter_name` | `str` | The name of the device adapter module (short name, not full file name). (This is what is returned by `Device.library()`). Must be specified if `adapter_name` was not provided to the `Device` constructor. | `''` |
| `device_name` | `str` | The name of the device. The name must correspond to one of the names recognized by the specific plugin library. (This is what is returned by `Device.name()`). Must be specified if `device_name` was not provided to the `Device` constructor. | `''` |
| `device_label` | `str` | The name to assign to the device. If not specified, the device will be assigned a default name: `adapter_name-device_name`, unless this Device instance was initialized with a label. | `''` |

### detect

```python
detect() -> DeviceDetectionStatus
```

Tries to communicate to device through a given serial port.

Used to automate discovery of correct serial port. Also configures the serial port correctly.

### supportsDetection

```python
supportsDetection() -> bool
```

Return whether or not the device supports automatic device detection.

(i.e. whether or not detectDevice() may be safely called).

### type

```python
type() -> DeviceType
```

Return device type.

### schema

```python
schema() -> DeviceSchema
```

Return dict in JSON-schema format for properties of `device_label`.

### wait

```python
wait() -> None
```

Block the calling thread until device becomes non-busy.

### getParentLabel

```python
getParentLabel() -> str
```

Return the parent device label of this device.

### setParentLabel

```python
setParentLabel(parent_label: str) -> None
```

Set the parent device label of this device.

## DeviceAdapter

```python
DeviceAdapter(library_name: str, mmcore: CMMCorePlus)
```

Convenience view onto a device-adapter library.

This is the type of object that is returned by `pymmcore_plus.CMMCorePlus.getAdapterObject`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `library_name` | `str` | Device this property belongs to | *required* |
| `mmcore` | `CMMCorePlus` | CMMCorePlus instance | *required* |

Methods:

| Name | Description |
| --- | --- |
| `unload` | Forcefully unload this library. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `str` | Return the short name of this device adapter library. |
| `core` | `CMMCorePlus` | Return the `CMMCorePlus` instance to which this Device is bound. |
| `available_devices` | `tuple[Device, ...]` | Get available devices offered by this device adapter. |
| `loaded_devices` | `tuple[Device, ...]` | Get currently loaded devices controlled this adapter. |

### name

```python
name: str
```

Return the short name of this device adapter library.

### core

```python
core: CMMCorePlus
```

Return the `CMMCorePlus` instance to which this Device is bound.

### available\_devices

```python
available_devices: tuple[Device, ...]
```

Get available devices offered by this device adapter.

Returns:

| Type | Description |
| --- | --- |
| `tuple[Device, ...]` | Tuple of `Device` objects, with the name, type, and description of each device. These objects also have a `load` method that can be used to load the device under a given label. |

### loaded\_devices

```python
loaded_devices: tuple[Device, ...]
```

Get currently loaded devices controlled this adapter.

Returns:

| Type | Description |
| --- | --- |
| `tuple[Device, ...]` | Tuple of loaded `Device` objects. |

### unload

```python
unload() -> None
```

Forcefully unload this library.

## DeviceDetectionStatus

Bases: `IntEnum`

DeviceDetectionStatus from device discovery.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `Unimplemented` |  | There is as yet no mechanism to programmatically detect the device. |
| `Misconfigured` |  | Some information needed to communicate with the device is invalid. |
| `CanNotCommunicate` |  | Communication attributes are valid, but the device does not respond. |
| `CanCommunicate` |  | Communication verified, parameters have been set to valid values. |

### Unimplemented

```python
Unimplemented = pymmcore.Unimplemented
```

There is as yet no mechanism to programmatically detect the device.

### Misconfigured

```python
Misconfigured = pymmcore.Misconfigured
```

Some information needed to communicate with the device is invalid.

### CanNotCommunicate

```python
CanNotCommunicate = pymmcore.CanNotCommunicate
```

Communication attributes are valid, but the device does not respond.

### CanCommunicate

```python
CanCommunicate = pymmcore.CanCommunicate
```

Communication verified, parameters have been set to valid values.

## DeviceInitializationState

Bases: `IntEnum`

DeviceInitializationState returned by getDeviceInitializationState.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `Uninitialized` |  |  |
| `InitializedSuccessfully` |  |  |
| `InitializationFailed` |  |  |

### Uninitialized

```python
Uninitialized = pymmcore.Uninitialized
```

### InitializedSuccessfully

```python
InitializedSuccessfully = pymmcore.InitializedSuccessfully
```

### InitializationFailed

```python
InitializationFailed = pymmcore.InitializationFailed
```

## DeviceProperty

```python
DeviceProperty(device_label: str, property_name: str, mmcore: CMMCorePlus)
```

Convenience view onto a device property.

This is the type of object that is returned by `pymmcore_plus.CMMCorePlus.getPropertyObject`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_label` | `str` | Device this property belongs to | *required* |
| `property_name` | `str` | Name of this property | *required* |
| `mmcore` | `CMMCorePlus` | CMMCorePlus instance | *required* |

Examples:

```pycon
>>> core = CMMCorePlus()
>>> prop = DeviceProperty("Objective", "Label", core)
>>> prop.isValid()  # points to a loaded device property in core
>>> prop.value
>>> prop.value = "Objective-2"  # setter
>>> prop.isReadOnly()
>>> prop.hasLimits()
>>> prop.range()
>>> prop.dict()  # all the info in one dict.
```

Methods:

| Name | Description |
| --- | --- |
| `isValid` | Return `True` if device is loaded and has a property by this name. |
| `isLoaded` | Return true if the device name is loaded. |
| `fromCache` | Return cached property value. |
| `setValue` | Functional alternate to property setter. |
| `isReadOnly` | Return `True` if property is read only. |
| `isPreInit` | Return `True` if property must be defined prior to initialization. |
| `hasLimits` | Return `True` if property has limits. |
| `lowerLimit` | Return lower limit if property has limits, or 0 otherwise. |
| `upperLimit` | Return upper limit if property has limits, or 0 otherwise. |
| `range` | Return (lowerLimit, upperLimit) range tuple. |
| `type` | Return `PropertyType` of this property. |
| `deviceType` | Return `DeviceType` of the device owning this property. |
| `allowedValues` | Return allowed values for this property, if constrained. |
| `isSequenceable` | Return `True` if property can be used in a sequence. |
| `sequenceMaxLength` | Return maximum number of property events that can be put in a sequence. |
| `loadSequence` | Transfer a sequence of events/states/whatever to the device. |
| `startSequence` | Start an ongoing sequence of triggered events in a property. |
| `stopSequence` | Stop an ongoing sequence of triggered events in a property. |
| `dict` | Return dict of info about this Property. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `device` |  |  |
| `name` |  |  |
| `core` | `CMMCorePlus` | Return the `CMMCorePlus` instance to which this Property is bound. |
| `valueChanged` | `_DevicePropValueSignal` |  |
| `value` | `Any` | Return current property value, cast to appropriate type if applicable. |
| `InfoDict` |  |  |

### device

```python
device = device_label
```

### name

```python
name = property_name
```

### core

```python
core: CMMCorePlus
```

Return the `CMMCorePlus` instance to which this Property is bound.

### valueChanged

```python
valueChanged: _DevicePropValueSignal
```

### value

```python
value: Any
```

Return current property value, cast to appropriate type if applicable.

### InfoDict

```python
InfoDict = InfoDict
```

### isValid

```python
isValid() -> bool
```

Return `True` if device is loaded and has a property by this name.

### isLoaded

```python
isLoaded() -> bool
```

Return true if the device name is loaded.

### fromCache

```python
fromCache() -> Any
```

Return cached property value.

### setValue

```python
setValue(val: Any) -> None
```

Functional alternate to property setter.

### isReadOnly

```python
isReadOnly() -> bool
```

Return `True` if property is read only.

### isPreInit

```python
isPreInit() -> bool
```

Return `True` if property must be defined prior to initialization.

### hasLimits

```python
hasLimits() -> bool
```

Return `True` if property has limits.

### lowerLimit

```python
lowerLimit() -> float
```

Return lower limit if property has limits, or 0 otherwise.

### upperLimit

```python
upperLimit() -> float
```

Return upper limit if property has limits, or 0 otherwise.

### range

```python
range() -> tuple[float, float]
```

Return (lowerLimit, upperLimit) range tuple.

### type

```python
type() -> PropertyType
```

Return `PropertyType` of this property.

### deviceType

```python
deviceType() -> DeviceType
```

Return `DeviceType` of the device owning this property.

### allowedValues

```python
allowedValues() -> tuple[str, ...]
```

Return allowed values for this property, if constrained.

### isSequenceable

```python
isSequenceable() -> bool
```

Return `True` if property can be used in a sequence.

### sequenceMaxLength

```python
sequenceMaxLength() -> int
```

Return maximum number of property events that can be put in a sequence.

### loadSequence

```python
loadSequence(eventSequence: Sequence[str]) -> None
```

Transfer a sequence of events/states/whatever to the device.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `eventSequence` | `Sequence[str]` | The sequence of events/states that the device will execute in response to external triggers | *required* |

### startSequence

```python
startSequence() -> None
```

Start an ongoing sequence of triggered events in a property.

### stopSequence

```python
stopSequence() -> None
```

Stop an ongoing sequence of triggered events in a property.

### dict

```python
dict() -> InfoDict
```

Return dict of info about this Property.

Returns an `InfoDict` with the following keys: `"valid", "value", "type", "device_type", "read_only", "pre_init", "range", "allowed"`.

If the device is invalid or not loaded, the `"valid"` key will be `False` and the rest of the keys will be `None`.

## DeviceType

Bases: `IntEnum`

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `UnknownType` |  |  |
| `AnyType` |  |  |
| `CameraDevice` |  |  |
| `ShutterDevice` |  |  |
| `StateDevice` |  |  |
| `StageDevice` |  |  |
| `XYStageDevice` |  |  |
| `SerialDevice` |  |  |
| `GenericDevice` |  |  |
| `AutoFocusDevice` |  |  |
| `CoreDevice` |  |  |
| `ImageProcessorDevice` |  |  |
| `SignalIODevice` |  |  |
| `MagnifierDevice` |  |  |
| `SLMDevice` |  |  |
| `HubDevice` |  |  |
| `GalvoDevice` |  |  |
| `PressurePumpDevice` |  |  |
| `VolumetricPumpDevice` |  |  |
| `Unknown` |  |  |
| `Any` |  |  |
| `Camera` |  |  |
| `Shutter` |  |  |
| `State` |  |  |
| `Stage` |  |  |
| `XYStage` |  |  |
| `Serial` |  |  |
| `Generic` |  |  |
| `AutoFocus` |  |  |
| `Core` |  |  |
| `ImageProcessor` |  |  |
| `SignalIO` |  |  |
| `Magnifier` |  |  |
| `SLM` |  |  |
| `Hub` |  |  |
| `Galvo` |  |  |
| `PressurePump` |  |  |
| `VolumetricPump` |  |  |

### UnknownType

```python
UnknownType = pymmcore.UnknownType
```

### AnyType

```python
AnyType = pymmcore.AnyType
```

### CameraDevice

```python
CameraDevice = pymmcore.CameraDevice
```

### ShutterDevice

```python
ShutterDevice = pymmcore.ShutterDevice
```

### StateDevice

```python
StateDevice = pymmcore.StateDevice
```

### StageDevice

```python
StageDevice = pymmcore.StageDevice
```

### XYStageDevice

```python
XYStageDevice = pymmcore.XYStageDevice
```

### SerialDevice

```python
SerialDevice = pymmcore.SerialDevice
```

### GenericDevice

```python
GenericDevice = pymmcore.GenericDevice
```

### AutoFocusDevice

```python
AutoFocusDevice = pymmcore.AutoFocusDevice
```

### CoreDevice

```python
CoreDevice = pymmcore.CoreDevice
```

### ImageProcessorDevice

```python
ImageProcessorDevice = pymmcore.ImageProcessorDevice
```

### SignalIODevice

```python
SignalIODevice = pymmcore.SignalIODevice
```

### MagnifierDevice

```python
MagnifierDevice = pymmcore.MagnifierDevice
```

### SLMDevice

```python
SLMDevice = pymmcore.SLMDevice
```

### HubDevice

```python
HubDevice = pymmcore.HubDevice
```

### GalvoDevice

```python
GalvoDevice = pymmcore.GalvoDevice
```

### PressurePumpDevice

```python
PressurePumpDevice = pymmcore.PressurePumpDevice
```

### VolumetricPumpDevice

```python
VolumetricPumpDevice = pymmcore.VolumetricPumpDevice
```

### Unknown

```python
Unknown = UnknownType
```

### Any

```python
Any = AnyType
```

### Camera

```python
Camera = CameraDevice
```

### Shutter

```python
Shutter = ShutterDevice
```

### State

```python
State = StateDevice
```

### Stage

```python
Stage = StageDevice
```

### XYStage

```python
XYStage = XYStageDevice
```

### Serial

```python
Serial = SerialDevice
```

### Generic

```python
Generic = GenericDevice
```

### AutoFocus

```python
AutoFocus = AutoFocusDevice
```

### Core

```python
Core = CoreDevice
```

### ImageProcessor

```python
ImageProcessor = ImageProcessorDevice
```

### SignalIO

```python
SignalIO = SignalIODevice
```

### Magnifier

```python
Magnifier = MagnifierDevice
```

### SLM

```python
SLM = SLMDevice
```

### Hub

```python
Hub = HubDevice
```

### Galvo

```python
Galvo = GalvoDevice
```

### PressurePump

```python
PressurePump = PressurePumpDevice
```

### VolumetricPump

```python
VolumetricPump = VolumetricPumpDevice
```

## FocusDirection

Bases: `IntEnum`

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `Unknown` |  |  |
| `TowardSample` |  |  |
| `AwayFromSample` |  |  |
| `FocusDirectionUnknown` |  |  |
| `FocusDirectionTowardSample` |  |  |
| `FocusDirectionAwayFromSample` |  |  |

### Unknown

```python
Unknown = 0
```

### TowardSample

```python
TowardSample = 1
```

### AwayFromSample

```python
AwayFromSample = -1
```

### FocusDirectionUnknown

```python
FocusDirectionUnknown = Unknown
```

### FocusDirectionTowardSample

```python
FocusDirectionTowardSample = TowardSample
```

### FocusDirectionAwayFromSample

```python
FocusDirectionAwayFromSample = AwayFromSample
```

## GeneratorMDASequence

Bases: `MDASequence`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `metadata` | `dict[str, Any]` | dict() -\> new empty dictionary dict(mapping) -\> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -\> new dictionary initialized as if via: d = {} for k, v in iterable: d\[k\] = v dict(\*\*kwargs) -\> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) | `<class 'dict'>` |
| `axis_order` | `tuple[str, ...]` |  | `()` |
| `stage_positions` | `WellPlatePlan \| tuple[AbsolutePosition, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |
| `grid_plan` | `GridFromEdges \| GridFromPolygon \| GridRowsColumns \| GridWidthHeight \| RandomPoints \| RelativePosition \| None` |  | `None` |
| `channels` | `tuple[Channel, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |
| `time_plan` | `MultiPhaseTimePlan \| TIntervalDuration \| TIntervalLoops \| TDurationLoops \| None` |  | `None` |
| `z_plan` | `ZTopBottom \| ZAboveBelow \| ZRangeAround \| ZAbsolutePositions \| ZRelativePositions \| None` |  | `None` |
| `autofocus_plan` | `AxesBasedAF \| None` |  | `None` |
| `setup` | `MDAEvent \| None` |  | `None` |
| `keep_shutter_open_across` | `tuple[str, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |

Methods:

| Name | Description |
| --- | --- |
| `iter_axis` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `axis_order` | `tuple[str, ...]` |  |
| `sizes` | `dict[str, int]` |  |

### axis\_order

```python
axis_order: tuple[str, ...] = ()
```

### sizes

```python
sizes: dict[str, int]
```

### iter\_axis

```python
iter_axis(axis: str) -> Iterator
```

## Keyword

Bases: `StrEnum`

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `Name` |  |  |
| `Description` |  |  |
| `CameraName` |  |  |
| `CameraID` |  |  |
| `CameraChannelName` |  |  |
| `CameraChannelIndex` |  |  |
| `Binning` |  |  |
| `Exposure` |  |  |
| `ActualExposure` |  |  |
| `ActualInterval_ms` |  |  |
| `Interval_ms` |  |  |
| `Elapsed_Time_ms` |  |  |
| `PixelType` |  |  |
| `ReadoutTime` |  |  |
| `ReadoutMode` |  |  |
| `Gain` |  |  |
| `EMGain` |  |  |
| `Offset` |  |  |
| `CCDTemperature` |  |  |
| `CCDTemperatureSetPoint` |  |  |
| `State` |  |  |
| `Label` |  |  |
| `Position` |  |  |
| `Type` |  |  |
| `Delay` |  |  |
| `BaudRate` |  |  |
| `DataBits` |  |  |
| `StopBits` |  |  |
| `Parity` |  |  |
| `Handshaking` |  |  |
| `DelayBetweenCharsMs` |  |  |
| `Port` |  |  |
| `AnswerTimeout` |  |  |
| `Speed` |  |  |
| `CoreDevice` |  |  |
| `CoreInitialize` |  |  |
| `CoreCamera` |  |  |
| `CoreShutter` |  |  |
| `CoreXYStage` |  |  |
| `CoreFocus` |  |  |
| `CoreAutoFocus` |  |  |
| `CoreAutoShutter` |  |  |
| `CoreChannelGroup` |  |  |
| `CoreImageProcessor` |  |  |
| `CoreSLM` |  |  |
| `CoreGalvo` |  |  |
| `CoreTimeoutMs` |  |  |
| `Channel` |  |  |
| `Version` |  |  |
| `ColorMode` |  |  |
| `Transpose_SwapXY` |  |  |
| `Transpose_MirrorX` |  |  |
| `Transpose_MirrorY` |  |  |
| `Transpose_Correction` |  |  |
| `Closed_Position` |  |  |
| `HubID` |  |  |
| `Metadata_CameraLabel` |  |  |
| `Metadata_Exposure` |  |  |
| `Metadata_Height` |  |  |
| `Metadata_ImageNumber` |  |  |
| `Metadata_ROI_X` |  |  |
| `Metadata_ROI_Y` |  |  |
| `Metadata_Score` |  |  |
| `Metadata_TimeInCore` |  |  |
| `Metadata_Width` |  |  |

### Name

```python
Name = pymmcore.g_Keyword_Name
```

### Description

```python
Description = pymmcore.g_Keyword_Description
```

### CameraName

```python
CameraName = pymmcore.g_Keyword_CameraName
```

### CameraID

```python
CameraID = pymmcore.g_Keyword_CameraID
```

### CameraChannelName

```python
CameraChannelName = pymmcore.g_Keyword_CameraChannelName
```

### CameraChannelIndex

```python
CameraChannelIndex = pymmcore.g_Keyword_CameraChannelIndex
```

### Binning

```python
Binning = pymmcore.g_Keyword_Binning
```

### Exposure

```python
Exposure = pymmcore.g_Keyword_Exposure
```

### ActualExposure

```python
ActualExposure = pymmcore.g_Keyword_ActualExposure
```

### ActualInterval\_ms

```python
ActualInterval_ms = pymmcore.g_Keyword_ActualInterval_ms
```

### Interval\_ms

```python
Interval_ms = pymmcore.g_Keyword_Interval_ms
```

### Elapsed\_Time\_ms

```python
Elapsed_Time_ms = pymmcore.g_Keyword_Elapsed_Time_ms
```

### PixelType

```python
PixelType = pymmcore.g_Keyword_PixelType
```

### ReadoutTime

```python
ReadoutTime = pymmcore.g_Keyword_ReadoutTime
```

### ReadoutMode

```python
ReadoutMode = pymmcore.g_Keyword_ReadoutMode
```

### Gain

```python
Gain = pymmcore.g_Keyword_Gain
```

### EMGain

```python
EMGain = pymmcore.g_Keyword_EMGain
```

### Offset

```python
Offset = pymmcore.g_Keyword_Offset
```

### CCDTemperature

```python
CCDTemperature = pymmcore.g_Keyword_CCDTemperature
```

### CCDTemperatureSetPoint

```python
CCDTemperatureSetPoint = pymmcore.g_Keyword_CCDTemperatureSetPoint
```

### State

```python
State = pymmcore.g_Keyword_State
```

### Label

```python
Label = pymmcore.g_Keyword_Label
```

### Position

```python
Position = pymmcore.g_Keyword_Position
```

### Type

```python
Type = pymmcore.g_Keyword_Type
```

### Delay

```python
Delay = pymmcore.g_Keyword_Delay
```

### BaudRate

```python
BaudRate = pymmcore.g_Keyword_BaudRate
```

### DataBits

```python
DataBits = pymmcore.g_Keyword_DataBits
```

### StopBits

```python
StopBits = pymmcore.g_Keyword_StopBits
```

### Parity

```python
Parity = pymmcore.g_Keyword_Parity
```

### Handshaking

```python
Handshaking = pymmcore.g_Keyword_Handshaking
```

### DelayBetweenCharsMs

```python
DelayBetweenCharsMs = pymmcore.g_Keyword_DelayBetweenCharsMs
```

### Port

```python
Port = pymmcore.g_Keyword_Port
```

### AnswerTimeout

```python
AnswerTimeout = pymmcore.g_Keyword_AnswerTimeout
```

### Speed

```python
Speed = pymmcore.g_Keyword_Speed
```

### CoreDevice

```python
CoreDevice = pymmcore.g_Keyword_CoreDevice
```

### CoreInitialize

```python
CoreInitialize = pymmcore.g_Keyword_CoreInitialize
```

### CoreCamera

```python
CoreCamera = pymmcore.g_Keyword_CoreCamera
```

### CoreShutter

```python
CoreShutter = pymmcore.g_Keyword_CoreShutter
```

### CoreXYStage

```python
CoreXYStage = pymmcore.g_Keyword_CoreXYStage
```

### CoreFocus

```python
CoreFocus = pymmcore.g_Keyword_CoreFocus
```

### CoreAutoFocus

```python
CoreAutoFocus = pymmcore.g_Keyword_CoreAutoFocus
```

### CoreAutoShutter

```python
CoreAutoShutter = pymmcore.g_Keyword_CoreAutoShutter
```

### CoreChannelGroup

```python
CoreChannelGroup = pymmcore.g_Keyword_CoreChannelGroup
```

### CoreImageProcessor

```python
CoreImageProcessor = pymmcore.g_Keyword_CoreImageProcessor
```

### CoreSLM

```python
CoreSLM = pymmcore.g_Keyword_CoreSLM
```

### CoreGalvo

```python
CoreGalvo = pymmcore.g_Keyword_CoreGalvo
```

### CoreTimeoutMs

```python
CoreTimeoutMs = pymmcore.g_Keyword_CoreTimeoutMs
```

### Channel

```python
Channel = pymmcore.g_Keyword_Channel
```

### Version

```python
Version = pymmcore.g_Keyword_Version
```

### ColorMode

```python
ColorMode = pymmcore.g_Keyword_ColorMode
```

### Transpose\_SwapXY

```python
Transpose_SwapXY = pymmcore.g_Keyword_Transpose_SwapXY
```

### Transpose\_MirrorX

```python
Transpose_MirrorX = pymmcore.g_Keyword_Transpose_MirrorX
```

### Transpose\_MirrorY

```python
Transpose_MirrorY = pymmcore.g_Keyword_Transpose_MirrorY
```

### Transpose\_Correction

```python
Transpose_Correction = pymmcore.g_Keyword_Transpose_Correction
```

### Closed\_Position

```python
Closed_Position = pymmcore.g_Keyword_Closed_Position
```

### HubID

```python
HubID = pymmcore.g_Keyword_HubID
```

### Metadata\_CameraLabel

```python
Metadata_CameraLabel = pymmcore.g_Keyword_Metadata_CameraLabel
```

### Metadata\_Exposure

```python
Metadata_Exposure = pymmcore.g_Keyword_Metadata_Exposure
```

### Metadata\_Height

```python
Metadata_Height = pymmcore.g_Keyword_Metadata_Height
```

### Metadata\_ImageNumber

```python
Metadata_ImageNumber = pymmcore.g_Keyword_Metadata_ImageNumber
```

### Metadata\_ROI\_X

```python
Metadata_ROI_X = pymmcore.g_Keyword_Metadata_ROI_X
```

### Metadata\_ROI\_Y

```python
Metadata_ROI_Y = pymmcore.g_Keyword_Metadata_ROI_Y
```

### Metadata\_Score

```python
Metadata_Score = pymmcore.g_Keyword_Metadata_Score
```

### Metadata\_TimeInCore

```python
Metadata_TimeInCore = pymmcore.g_Keyword_Metadata_TimeInCore
```

### Metadata\_Width

```python
Metadata_Width = pymmcore.g_Keyword_Metadata_Width
```

## Metadata

```python
Metadata(*args: Any, **kwargs: Any)
```

Bases: `Metadata`

Subclass of `pymmcore.Metadata` with a pythonic interface.

This subclass fully implements a `collections.abc.Mapping` interface (i.e. it behaves like a Python `dict`). It also adds a `json()` convenience method to convert to a JSON string.

Methods:

| Name | Description |
| --- | --- |
| `get` |  |
| `copy` |  |
| `clear` |  |
| `json` |  |
| `keys` |  |
| `items` |  |
| `values` |  |

### get

```python
get(name: str, default: Any = _NULL) -> Any
```

### copy

```python
copy() -> Metadata
```

### clear

```python
clear() -> None
```

### json

```python
json() -> str
```

### keys

```python
keys() -> KeysView[str]
```

### items

```python
items() -> ItemsView[str, str]
```

### values

```python
values() -> ValuesView[str]
```

## PCoreSignaler

Bases: `Protocol`

Declares the protocol for all signals that will be emitted from CMMCorePlus.

The main instance of this interface is available on the `CMMCorePlus` object at the `events` attribute. Each signal on `events` is an object has a `connect` and a `disconnect` method that you can use to connect/disconnect your own callback functions. `connect` and `disconnect` accept a single argument, which is a callable that will be called when the signal is emitted. The callable should accept no more positional arguments than the signal emits (noted for each signal below), but may accept fewer.

> [!NOTE]
>
> These events are a superset of those emitted by [MMEventCallback](<https://valelab4.ucsf.edu/~MM/doc/mmcorej/mmcorej/MMEventCallback.html>) in the MMCore C++ library. The "on" prefix has been removed from the names here and the first letter lower cased.
>
> **Important**
>
> In the core C++ library (and in `pymmcore`), the emission of many of these events is left to the discretion of the device adapter. In `pymmcore_plus`, we attempt to emit these events in a more consistent manner (e.g. by checking a particular value before and after calling into the C++ library). So, the emission of these events is not guaranteed to be 1:1 with the C++ library; however, it should be easier to follow the state of the core when using `pymmcore_plus.CMMCorePlus`.

Examples:

To connect to the `onExposureChanged` event emitted by MMCore, you would connect to the `exposureChanged` signal on this class:

```python
from pymmcore_plus import CMMCorePlus

core = CMMCorePlus()


def on_exposure_changed(device: str, new_exposure: float):
    print(f"Exposure changed for {device} to {new_exposure}")


core.events.exposureChanged.connect(my_callback)
```

Events may also be connected as a decorator:

```python
@core.events.exposureChanged.connect
def on_exposure_changed(device: str, new_exposure: float): ...
```

---

Methods:

| Name | Description |
| --- | --- |
| `devicePropertyChanged` | Return object to connect/disconnect to device/property-specific changes. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `propertiesChanged` | `PSignal` | Emits with no arguments when properties have changed. |
| `propertyChanged` | `PSignal` | Emits `(name: str, propName: str, propValue: str)` when a specific property has changed. |
| `channelGroupChanged` | `PSignal` | Emits `(newChannelGroupName: str)` when a channel group has changed. |
| `configGroupChanged` | `PSignal` | Emits `(groupName: str, newConfigName: str)` when a config group has changed. |
| `systemConfigurationLoaded` | `PSignal` | Emits with no arguments when the system configuration has been loaded. |
| `pixelSizeChanged` | `PSignal` | Emits `(newPixelSizeUm: float)` when the pixel size has changed. |
| `pixelSizeAffineChanged` | `PSignal` | Emits `(float, float, float, float, float, float)` when the pixel size affine has changed. |
| `stagePositionChanged` | `PSignal` | Emits `(name: str, pos: float)` when a stage position has changed. |
| `XYStagePositionChanged` | `PSignal` | Emits `(name: str, xpos: float, ypos: float)` when an XY stage position has changed. |
| `xYStagePositionChanged` | `PSignal` |  |
| `exposureChanged` | `PSignal` | Emits `(name: str, newExposure: float)` when an exposure has changed. |
| `SLMExposureChanged` | `PSignal` | Emits `(name: str, newExposure: float)` when the exposure of the SLM device changes. |
| `sLMExposureChanged` | `PSignal` |  |
| `shutterOpenChanged` | `PSignal` | Emits `(name: str, isOpen: bool)` when the shutter open state has changed. |
| `configSet` | `PSignal` | Emits `(str, str)` when a config has been set. |
| `imageSnapped` | `PSignal` | Emits with no arguments whenever snap is called. |
| `mdaEngineRegistered` | `PSignal` | Emits `(MDAEngine, MDAEngine)` when an MDAEngine is registered. |
| `continuousSequenceAcquisitionStarting` | `PSignal` | Emits with no arguments *before* continuous sequence acquisition is started. |
| `continuousSequenceAcquisitionStarted` | `PSignal` | Emits with no arguments *after* continuous sequence acquisition has started. |
| `sequenceAcquisitionStarting` | `PSignal` | Emits `(str,)` *before* sequence acquisition is started. |
| `sequenceAcquisitionStarted` | `PSignal` | Emits `(str)` *after* sequence acquisition has started. |
| `sequenceAcquisitionStopped` | `PSignal` | Emits `(str)` when sequence acquisition is stopped. |
| `autoShutterSet` | `PSignal` | Emits `(bool)` when the auto shutter setting is changed. |
| `configGroupDeleted` | `PSignal` | Emits `(str)` when a config group is deleted. |
| `configDeleted` | `PSignal` | Emits `(str, str)` when a config is deleted. |
| `configDefined` | `PSignal` | Emits `(str, str, str, str, str)` when a config is defined. |
| `roiSet` | `PSignal` | Emits `(str, int, int, int, int)` when an ROI is set. |

### propertiesChanged

```python
propertiesChanged: PSignal
```

Emits with no arguments when properties have changed.

### propertyChanged

```python
propertyChanged: PSignal
```

Emits `(name: str, propName: str, propValue: str)` when a specific property has changed.

### channelGroupChanged

```python
channelGroupChanged: PSignal
```

Emits `(newChannelGroupName: str)` when a channel group has changed.

### configGroupChanged

```python
configGroupChanged: PSignal
```

Emits `(groupName: str, newConfigName: str)` when a config group has changed.

### systemConfigurationLoaded

```python
systemConfigurationLoaded: PSignal
```

Emits with no arguments when the system configuration has been loaded.

### pixelSizeChanged

```python
pixelSizeChanged: PSignal
```

Emits `(newPixelSizeUm: float)` when the pixel size has changed.

### pixelSizeAffineChanged

```python
pixelSizeAffineChanged: PSignal
```

Emits `(float, float, float, float, float, float)` when the pixel size affine has changed.

### stagePositionChanged

```python
stagePositionChanged: PSignal
```

Emits `(name: str, pos: float)` when a stage position has changed.

### XYStagePositionChanged

```python
XYStagePositionChanged: PSignal
```

Emits `(name: str, xpos: float, ypos: float)` when an XY stage position has changed.

### xYStagePositionChanged

```python
xYStagePositionChanged: PSignal
```

### exposureChanged

```python
exposureChanged: PSignal
```

Emits `(name: str, newExposure: float)` when an exposure has changed.

### SLMExposureChanged

```python
SLMExposureChanged: PSignal
```

Emits `(name: str, newExposure: float)` when the exposure of the SLM device changes.

### sLMExposureChanged

```python
sLMExposureChanged: PSignal
```

### shutterOpenChanged

```python
shutterOpenChanged: PSignal
```

Emits `(name: str, isOpen: bool)` when the shutter open state has changed.

### configSet

```python
configSet: PSignal
```

Emits `(str, str)` when a config has been set.

> ✨ This signal is unique to `pymmcore-plus`.

### imageSnapped

```python
imageSnapped: PSignal
```

Emits with no arguments whenever snap is called.

> ✨ This signal is unique to `pymmcore-plus`.

### mdaEngineRegistered

```python
mdaEngineRegistered: PSignal
```

Emits `(MDAEngine, MDAEngine)` when an MDAEngine is registered.

> ✨ This signal is unique to `pymmcore-plus`.

### continuousSequenceAcquisitionStarting

```python
continuousSequenceAcquisitionStarting: PSignal
```

Emits with no arguments *before* continuous sequence acquisition is started.

> ✨ This signal is unique to `pymmcore-plus`.

### continuousSequenceAcquisitionStarted

```python
continuousSequenceAcquisitionStarted: PSignal
```

Emits with no arguments *after* continuous sequence acquisition has started.

> ✨ This signal is unique to `pymmcore-plus`.

### sequenceAcquisitionStarting

```python
sequenceAcquisitionStarting: PSignal
```

Emits `(str,)` *before* sequence acquisition is started.

> [!NOTE]
>
> **Breaking Change**
>
> In `pymmcore-plus` version 0.16.0, the `sequenceAcquisitionStarting` signal was *reduced* from `(str, int, float, bool)` to `(str,)` to match the signature emitted by the C++ MMCore library.

`(cameraLabel,)`

> ✨ This signal is unique to `pymmcore-plus`.

### sequenceAcquisitionStarted

```python
sequenceAcquisitionStarted: PSignal
```

Emits `(str)` *after* sequence acquisition has started.

> [!NOTE]
>
> **Breaking Change**
>
> In `pymmcore-plus` version 0.16.0, the `sequenceAcquisitionStarted` signal was *reduced* from `(str, int, float, bool)` to `(str,)` to match the signature emitted by the C++ MMCore library.

(cameraLabel,)

> ✨ This signal is unique to `pymmcore-plus`.

### sequenceAcquisitionStopped

```python
sequenceAcquisitionStopped: PSignal
```

Emits `(str)` when sequence acquisition is stopped.

> ✨ This signal is unique to `pymmcore-plus`.

### autoShutterSet

```python
autoShutterSet: PSignal
```

Emits `(bool)` when the auto shutter setting is changed.

### configGroupDeleted

```python
configGroupDeleted: PSignal
```

Emits `(str)` when a config group is deleted.

> ✨ This signal is unique to `pymmcore-plus`.

### configDeleted

```python
configDeleted: PSignal
```

Emits `(str, str)` when a config is deleted.

> ✨ This signal is unique to `pymmcore-plus`.

### configDefined

```python
configDefined: PSignal
```

Emits `(str, str, str, str, str)` when a config is defined.

> ✨ This signal is unique to `pymmcore-plus`.

### roiSet

```python
roiSet: PSignal
```

Emits `(str, int, int, int, int)` when an ROI is set.

> ✨ This signal is unique to `pymmcore-plus`.

### devicePropertyChanged

```python
devicePropertyChanged(
    device: str, property: str | None = None
) -> PSignalInstance
```

Return object to connect/disconnect to device/property-specific changes.

Note that the callback provided to `.connect()` must take *two* parameters (property\_name, new\_value) if only `device` is provided, and *one* parameter (new\_value) of both `device` and `property` are provided.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device` | `str` | A device label | *required* |
| `property` | `Optional[str]` | Optional property label. If not provided, all property changes on `device` will trigger an event emission. by default None | `None` |

Returns:

| Type | Description |
| --- | --- |
| `_PropertySignal` | Object with `connect` and `disconnect` methods that attach a callback to the change event of a specific property or device. |

Examples:

```pycon
>>> core.events.devicePropertyChanged("Camera", "Gain").connect(callback)
>>> core.events.devicePropertyChanged("Camera").connect(callback)
```

## PixelFormat

Bases: `StrEnum`

Subset of GeniCam Pixel Format names used by pymmcore-plus.

(This is similar to PixelType, but follows GeniCam standards.)

See [https://docs.baslerweb.com/pixel-format\#unpacked-and-packed-pixel-formats](<https://docs.baslerweb.com/pixel-format#unpacked-and-packed-pixel-formats>) for helpful clarifications. Note that **unpacked** pixel formats (like Mono8, Mono12, Mono16) are always 8-bit aligned. Meaning Mono12 is actually a 16-bit buffer.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `MONO8` | `str` | 8-bit (unpacked) monochrome pixel format. |
| `MONO10` | `str` | 10-bit (unpacked) monochrome pixel format. (16-bit buffer) |
| `MONO12` | `str` | 12-bit (unpacked) monochrome pixel format. (16-bit buffer) |
| `MONO14` | `str` | 14-bit (unpacked) monochrome pixel format. (16-bit buffer) |
| `MONO16` | `str` | 16-bit (unpacked) monochrome pixel format |
| `MONO32` | `str` | 32-bit (unpacked) monochrome pixel format |
| `RGB8` | `str` | 8-bit RGB pixel format. (24-bit buffer) |
| `RGB10` | `str` | 10-bit RGB pixel format. (48-bit buffer) |
| `RGB12` | `str` | 12-bit RGB pixel format. (48-bit buffer) |
| `RGB14` | `str` | 14-bit RGB pixel format. (48-bit buffer) |
| `RGB16` | `str` | 16-bit RGB pixel format. (48-bit buffer) |

Methods:

| Name | Description |
| --- | --- |
| `pick` |  |
| `for_current_camera` |  |

### MONO8

```python
MONO8 = 'Mono8'
```

### MONO10

```python
MONO10 = 'Mono10'
```

### MONO12

```python
MONO12 = 'Mono12'
```

### MONO14

```python
MONO14 = 'Mono14'
```

### MONO16

```python
MONO16 = 'Mono16'
```

### MONO32

```python
MONO32 = 'Mono32'
```

### RGB8

```python
RGB8 = 'RGB8'
```

### RGB10

```python
RGB10 = 'RGB10'
```

### RGB12

```python
RGB12 = 'RGB12'
```

### RGB14

```python
RGB14 = 'RGB14'
```

### RGB16

```python
RGB16 = 'RGB16'
```

### pick

```python
pick(bit_depth: int, n_comp: int = 1) -> PixelFormat
```

### for\_current\_camera

```python
for_current_camera(core: CMMCore) -> PixelFormat
```

## PortType

Bases: `IntEnum`

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `InvalidPort` |  |  |
| `SerialPort` |  |  |
| `USBPort` |  |  |
| `HIDPort` |  |  |

### InvalidPort

```python
InvalidPort = pymmcore.InvalidPort
```

### SerialPort

```python
SerialPort = pymmcore.SerialPort
```

### USBPort

```python
USBPort = pymmcore.USBPort
```

### HIDPort

```python
HIDPort = pymmcore.HIDPort
```

## PropertyType

Bases: `IntEnum`

Methods:

| Name | Description |
| --- | --- |
| `to_python` |  |
| `to_json` |  |
| `create` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `Undef` |  |  |
| `String` |  |  |
| `Float` |  |  |
| `Integer` |  |  |
| `Boolean` |  |  |
| `Enum` |  |  |

### Undef

```python
Undef = pymmcore.Undef
```

### String

```python
String = pymmcore.String
```

### Float

```python
Float = pymmcore.Float
```

### Integer

```python
Integer = pymmcore.Integer
```

### Boolean

```python
Boolean = auto()
```

### Enum

```python
Enum = auto()
```

### to\_python

```python
to_python() -> type | None
```

### to\_json

```python
to_json() -> str
```

### create

```python
create(value: Any) -> PropertyType
```

## configure\_logging

```python
configure_logging(
    file: str | Path | None = LOG_FILE,
    stderr_level: int | str = DEFAULT_LOG_LEVEL,
    file_level: int | str = DEBUG,
    log_to_stderr: bool = True,
    file_rotation: int = 40,
    file_retention: int = 20,
) -> None
```

Configure logging for pymmcore-plus.

This function is called automatically once when pymmcore-plus is imported, to set up logging to stderr and a log file. You can call it again to change the logging settings.

You may also configure logging using the following environment variables:

- `PYMM_LOG_LEVEL` - The log level for `stderr` logging. By default `INFO`.
- `PYMM_LOG_FILE` - The path to the log file. If set to `0`, `false`, `no`, or `none`, logging to file will be disabled.
- `PYMM_LOG_RICH` - If set to `1`, `true`, or `yes`, use `rich` for stderr logging (requires `rich` to be installed). Note: rich formatting adds some overhead; see [https://github.com/pymmcore-plus/pymmcore-plus/issues/449](<https://github.com/pymmcore-plus/pymmcore-plus/issues/449>).

> [!NOTE]
>
> This function will clear all existing logging handlers and replace them with new ones. So be sure to pass all the settings you want to use each time you call this function.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `file` | `str \| Path \| None` | Path to logfile. May also be set with MM\_LOG\_FILE environment variable. If `None`, will not log to file. By default, logs to: Mac OS X: \~/Library/Application Support/pymmcore-plus/logs Unix: \~/.local/share/pymmcore-plus/logs Win: C:\\Users\\\\AppData\\Local\\pymmcore-plus\\pymmcore-plus\\logs | `LOG_FILE` |
| `stderr_level` | `int \| str` | Level for stderr logging. One of "TRACE", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL", or 5, 10, 20, 30, 40, or 50, respectively. by default `"INFO"`. | `DEFAULT_LOG_LEVEL` |
| `file_level` | `int \| str` | Level for logging to file, by default `"TRACE"` | `DEBUG` |
| `log_to_stderr` | `bool` | Whether to log to stderr, by default True | `True` |
| `file_rotation` | `int` | When to rollover to the next log file, in MegaBytes, by default `40`. | `40` |
| `file_retention` | `int` | Maximum number of log files to retain, by default `20` | `20` |

## find\_micromanager

```python
find_micromanager(return_first: Literal[True] = ...) -> str | None
```

```python
find_micromanager(return_first: Literal[False]) -> list[str]
```

```python
find_micromanager(return_first: bool = True) -> str | list[str] | None
```

Locate a Micro-Manager folder (for device adapters).

In order, this will look for:

1. An environment variable named `MICROMANAGER_PATH`
2. A path stored in the `CURRENT_MM_PATH` file (set by `use_micromanager`).
3. A `Micro-Manager*` folder in the `pymmcore-plus` user data directory (this is the default install location when running `mmcore install`)

   - **Windows**: C:\\Users\\\[user\]\\AppData\\Local\\pymmcore-plus\\pymmcore-plus
   - **macOS**: \~/Library/Application Support/pymmcore-plus
   - **Linux**: \~/.local/share/pymmcore-plus
4. A `Micro-Manager*` folder in the `pymmcore_plus` package directory (this is the default install location when running `python -m pymmcore_plus.install`)
5. The default micro-manager install location:

   - **Windows**: `C:/Program Files/`
   - **macOS**: `/Applications`
   - **Linux**: `/usr/local/lib`

> [!NOTE]
>
> This function is used by `pymmcore_plus.CMMCorePlus` to locate the micro-manager device adapters. By default, the output of this function is passed to `setDeviceAdapterSearchPaths` when creating a new `CMMCorePlus` instance.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `return_first` | `bool` | If True (default), return the first found path. If False, return a list of all found paths. | `True` |

## install\_pymmcore\_ipy\_completion

```python
install_pymmcore_ipy_completion(shell: InteractiveShell | None = None) -> None
```

Install the CMMCorePlus completion matcher in the current IPython session.

## use\_micromanager

```python
use_micromanager(
    path: str | Path | None = None, pattern: str | Pattern[str] | None = None
) -> Path | None
```

Set the preferred Micro-Manager path.

This sets the preferred micromanager path, and persists across sessions. This path takes precedence over everything *except* the `MICROMANAGER_PATH` environment variable.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `path` | `str \| Path \| None` | Path to an existing directory. This directory should contain micro-manager device adapters. If `None`, the path will be determined using `pattern`. | `None` |
| `pattern` | `str Pattern \| \| None` | A regex pattern to match against the micromanager paths found by `find_micromanager`. If no match is found, a `FileNotFoundError` will be raised. | `None` |

## Documented on other pages

| Object | Page | Description |
| --- | --- | --- |
| `CMMCorePlus` | CMMCorePlus | Wrapper for CMMCore with extended functionality. |
