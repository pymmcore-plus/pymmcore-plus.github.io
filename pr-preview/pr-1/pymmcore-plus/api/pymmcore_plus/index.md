# pymmcore\_plus

pymmcore superset providing improved APIs, event handling, and a pure python acquisition engine.

**Submodules**

| Name | Description |
| --- | --- |
| `core` | `CMMCorePlus` and its supporting classes. |
| `experimental` | Experimental features. The APIs here may change in future releases. |
| `install` | Download and install Micro-Manager device adapters (see `mmcore install`). |
| `mda` | Running multi-dimensional acquisitions: the runner, the default engine, and signals. |
| `metadata` | Schema and helpers for the metadata emitted during an MDA. |
| `mocks` | Mock objects for testing. |
| `model` | An in-memory model of a Micro-Manager configuration. |
| `seq_tester` | Classes for working with SequenceTester devices. |

**Classes**

| Name | Description |
| --- | --- |
| `AbstractChangeAccumulator` | Abstract base class for accumulating a series of `setX` calls to a device. |
| `ActionType` | Action that triggered a device property handler. |
| `CFGCommand` | Commands used in Micro-Manager configuration (`.cfg`) files. |
| `CFGGroup` | Names of built-in config groups and presets (`System`, `Startup`, etc...). |
| `CMMCorePlus` | Wrapper for CMMCore with extended functionality. |
| `CMMCoreSignaler` | Signals that will be emitted from CMMCorePlus objects (psygnal backend). |
| `ConfigGroup` | Convenience object for dealing with a set of related Configuration objects. |
| `Configuration` | Encapsulation of configuration information. |
| `Device` | Convenience object-oriented device API. |
| `DeviceAdapter` | Convenience view onto a device-adapter library. |
| `DeviceDetectionStatus` | DeviceDetectionStatus from device discovery. |
| `DeviceInitializationState` | DeviceInitializationState returned by getDeviceInitializationState. |
| `DeviceProperty` | Convenience view onto a device property. |
| `DeviceType` | Type of a Micro-Manager device. |
| `FocusDirection` | Direction a focus stage moves (towards or away from the sample). |
| `GeneratorMDASequence` | Placeholder sequence used when the runner is given events, not an `MDASequence`. |
| `Keyword` | Standard property and device names (the `g_Keyword_*` constants). |
| `Metadata` | Subclass of `pymmcore.Metadata` with a pythonic interface. |
| `PCoreSignaler` | Declares the protocol for all signals that will be emitted from CMMCorePlus. |
| `PixelFormat` | Subset of GeniCam Pixel Format names used by pymmcore-plus. |
| `PortType` | Type of a port device (serial, USB, HID). |
| `PropertyType` | Type of a device property value. |

**Functions**

| Name | Description |
| --- | --- |
| `configure_logging` | Configure logging for pymmcore-plus. |
| `find_micromanager` | Locate a Micro-Manager folder (for device adapters). |
| `install_pymmcore_ipy_completion` | Install the CMMCorePlus completion matcher in the current IPython session. |
| `use_micromanager` | Set the preferred Micro-Manager path. |

## Classes

### AbstractChangeAccumulator

```python
AbstractChangeAccumulator(zero: T)
```

Bases: `ABC`, `Generic[T]`

Abstract base class for accumulating a series of `setX` calls to a device.

A `ChangeAccumulator` is a class that accumulates a series of `setX` calls to a device, retaining an internal target value, and emitting a signal when the device has reached its target and is idle. It can be shared by multiple players (e.g. widgets, or other classes) that want to control the same device, and allows them all to issue relative/absolute moves, and be notified when the device is idle.

A common use case is to accumulate setPosition calls made to a stage device, where you might want to accumulate a series of relative moves, and snap an image only when the stage is idle after reaching its target position.

#### finished

```python
finished = psygnal.Signal()
```

Signal emitted when the device has reached its target and is idle.

#### is\_moving

```python
is_moving: bool
```

Returns True if the device is moving.

#### target

```python
target: T | None
```

The target position of the stage. Or None if not moving.

#### add\_relative

```python
add_relative(delta: T) -> None
```

Add a relative value to the target.

#### set\_absolute

```python
set_absolute(target: T) -> None
```

Assign an absolute value to the target.

This will reset the accumulated state and issue a move to the target position. After the move finishes, new `move_relative()` calls are interpreted relative to *target*.

#### poll\_done

```python
poll_done() -> bool
```

Check if the device is done moving.

This should be called repeatedly by some event loop driver.

Returns True exactly once when: 1. The device is idle (not busy) AND 2. The last issued move command has been completed

After returning True it resets its state and will return False until the next move\_relative() call.

### ConfigGroup

```python
ConfigGroup(group_name: str, mmcore: CMMCorePlus)
```

Bases: `MutableMapping[str, Configuration]`

Convenience object for dealing with a set of related Configuration objects.

This object behaves as a `collections.abc.MutableMapping` of `str` (preset name) to `Configuration` objects.

It is the object type returned by `pymmcore_plus.CMMCorePlus.getConfigGroupObject`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `group_name` | `str` | The name of the configuration group to manage. (It needn't exist yet) | *required* |
| `mmcore` | `CMMCorePlus` | The core object managing this config group. | *required* |

#### name

```python
name: str
```

Return the name of this ConfigGroup.

#### core

```python
core: CMMCorePlus
```

Return the `CMMCorePlus` instance to which this ConfigGroup is bound.

#### is\_consistent

```python
is_consistent: bool
```

Return `True` if all presets in this group have the same properties.

Note that a group with 0 or 1 presets is always considered consistent. If two or more presets are present, they must all have the same device properties. (values of course may vary.)

#### exists

```python
exists() -> bool
```

Return `True` if this ConfigGroup exists in the current configuration.

#### create

```python
create() -> None
```

Create this configuration group in core (as an empty group).

If the group already exists, this is a no-op.

#### delete

```python
delete() -> None
```

Delete this entire configuration group and all presets in it.

#### iterDeviceProperties

```python
iterDeviceProperties() -> Iterator[DeviceProperty]
```

Iterate `DeviceProperty` for all properties in this ConfigGroup.

Note, this only iterates over properties that are defined in the first preset of this ConfigGroup. This *should* be the same for all presets in this ConfigGroup, but it is not guaranteed. Use `is_consistent` to check if all presets in this ConfigGroup have the same properties.

#### renameConfig

```python
renameConfig(oldConfigName: str, newConfigName: str) -> None
```

Rename a configuration in this group.

If the configuration does not exist, a KeyError is thrown.

#### setConfig

```python
setConfig(configName: str) -> None
```

Set the current configuration to `configName`.

This actually updates the hardware state to match what is stored in the preset `configName`.

#### getCurrentConfig

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

#### getCurrentConfigFromCache

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

#### wait

```python
wait(configName: str | None = None) -> None
```

Blocks until all devices included in the configuration group ready.

If `configName` not provided, then the first configuration in the group is used.

#### rename

```python
rename(newGroupName: str) -> None
```

Rename this configuration group.

### Configuration

```python
Configuration()
```

Bases: `Configuration`

Encapsulation of configuration information.

This is the type of object returned by default (provided `native=False`) by `getConfigData`, `getPixelSizeConfigData`, `getSystemState`, `getSystemStateCache`, `getConfigState`, `getConfigGroupState` and `getConfigGroupStateFromCache`.

This class is a subclass of `pymmcore.Configuration`. It can be indexed like a mapping, with `(deviceLabel, propertyLabel)` keys (`cfg["Camera", "Exposure"]`, `cfg["Camera", "Exposure"] = "10"`, `del cfg["Camera", "Exposure"]`), and it has a few list-like methods (`append`, `extend`, `remove`). Iterating over it yields `(deviceLabel, propertyLabel, value)` 3-tuples. (It is *not* a full `MutableMapping`: there are no `keys()`, `values()` or `items()` methods. Use `dict` or `html` for other views.)

Note that the "order" of this collection is not well-defined, so while you *can* index with an integer (which returns a `pymmcore.PropertySetting`), you should not rely on the order of the items in the collection.

> [!TIP]
>
> All of the methods in `pymmcore_plus.CMMCorePlus` that would have returned a `pymmcore.Configuration` in `pymmcore` (e.g. `getConfigData`, `getConfigState`, etc...) have been reimplemented to return a `pymmcore_plus.Configuration` object. This object has the same API as `pymmcore.Configuration`, but you can request a "native" (unenhanced) `pymmcore` object by passing `native=True` to the method.

#### remove

```python
remove(key: DevPropTuple) -> None
```

Remove setting for `(devLabel, propLabel)` from the configuration.

#### append

```python
append(setting: PropertySetting | DevPropValueTuple) -> None
```

Add a setting to the configuration.

#### extend

```python
extend(
    other: Configuration | Iterable[PropertySetting | DevPropValueTuple],
) -> None
```

Add all settings from another Configuration.

#### html

```python
html() -> str
```

Return config representation as HTML.

#### dict

```python
dict() -> dict[str, dict[str, str]]
```

Return config as a nested dict {Device: {Property: Value}}.

#### from\_configuration

```python
from_configuration(config: Configuration) -> Configuration
```

Create Configuration (Plus) from pymmcore.Configuration.

#### create

```python
create(*args: Any, **kwargs: Any) -> Configuration
```

More flexible init to create a `Configuration`.

Can create from: 1. A dict of dicts (outer key is device, inner key is prop) 2. A sequence of 3-tuple 3. kwargs: where the key is the device, and the value is a {prop: value} map

### Device

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

#### UNASSIGNED

```python
UNASSIGNED = '__UNASSIGNED__'
```

#### propertyChanged

```python
propertyChanged: PSignalInstance = _DevicePropValueSignal(
    device_label, None, mmcore
)
```

#### label

```python
label: str
```

Return the assigned label of this device.

#### core

```python
core: CMMCorePlus
```

Return the `CMMCorePlus` instance to which this Device is bound.

#### properties

```python
properties: tuple[DeviceProperty, ...]
```

Get all properties supported by device as DeviceProperty objects.

#### create

```python
create(
    device_label: str,
    mmcore: CMMCorePlus,
    device_type: type[Device] | DeviceType = Any,
) -> Self
```

#### get\_subclass

```python
get_subclass(device_label: str, mmcore: CMMCorePlus) -> type[Device]
```

#### isBusy

```python
isBusy() -> bool
```

Return busy status for this device.

#### delayMs

```python
delayMs() -> float
```

Return action delay in ms for this device.

#### setDelayMs

```python
setDelayMs(delayMs: float) -> None
```

Override the built-in value for the action delay.

#### usesDelay

```python
usesDelay() -> bool
```

Return `True` if the device will use the delay setting or not.

#### description

```python
description() -> str
```

Return device description.

#### library

```python
library() -> str
```

Return device library (aka module, device adapter) name.

#### name

```python
name() -> str
```

Return the device name (this is not the same as the assigned label).

#### propertyNames

```python
propertyNames() -> tuple[str, ...]
```

Return all property names supported by this device.

#### getPropertyObject

```python
getPropertyObject(property_name: str) -> DeviceProperty
```

Return a `DeviceProperty` object bound to this device on this core.

#### setProperty

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

#### getProperty

```python
getProperty(property_name: str) -> str
```

Get a device property value.

#### initialize

```python
initialize() -> None
```

Initialize device.

#### unload

```python
unload() -> None
```

Unload device from the core and adjust all configuration data.

#### isLoaded

```python
isLoaded() -> bool
```

Return `True` if device is loaded.

#### load

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

#### detect

```python
detect() -> DeviceDetectionStatus
```

Tries to communicate to device through a given serial port.

Used to automate discovery of correct serial port. Also configures the serial port correctly.

#### supportsDetection

```python
supportsDetection() -> bool
```

Return whether or not the device supports automatic device detection.

(i.e. whether or not detectDevice() may be safely called).

#### type

```python
type() -> DeviceType
```

Return device type.

#### schema

```python
schema() -> DeviceSchema
```

Return dict in JSON-schema format for properties of `device_label`.

#### wait

```python
wait() -> None
```

Block the calling thread until device becomes non-busy.

#### getParentLabel

```python
getParentLabel() -> str
```

Return the parent device label of this device.

#### setParentLabel

```python
setParentLabel(parent_label: str) -> None
```

Set the parent device label of this device.

### DeviceAdapter

```python
DeviceAdapter(library_name: str, mmcore: CMMCorePlus)
```

Convenience view onto a device-adapter library.

This is the type of object that is returned by `pymmcore_plus.CMMCorePlus.getAdapterObject`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `library_name` | `str` | Name of the device adapter library (e.g. `"DemoCamera"`). | *required* |
| `mmcore` | `CMMCorePlus` | CMMCorePlus instance | *required* |

#### name

```python
name: str
```

Return the short name of this device adapter library.

#### core

```python
core: CMMCorePlus
```

Return the `CMMCorePlus` instance to which this DeviceAdapter is bound.

#### available\_devices

```python
available_devices: tuple[Device, ...]
```

Get available devices offered by this device adapter.

Returns:

| Type | Description |
| --- | --- |
| `tuple[Device, ...]` | Tuple of `Device` objects, with the name, type, and description of each device. These objects also have a `load` method that can be used to load the device under a given label. |

#### loaded\_devices

```python
loaded_devices: tuple[Device, ...]
```

Get currently loaded devices controlled this adapter.

Returns:

| Type | Description |
| --- | --- |
| `tuple[Device, ...]` | Tuple of loaded `Device` objects. |

#### unload

```python
unload() -> None
```

Forcefully unload this library.

### DeviceProperty

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

#### device

```python
device = device_label
```

#### name

```python
name = property_name
```

#### core

```python
core: CMMCorePlus
```

Return the `CMMCorePlus` instance to which this Property is bound.

#### valueChanged

```python
valueChanged: _DevicePropValueSignal
```

#### value

```python
value: Any
```

Return current property value, cast to appropriate type if applicable.

#### InfoDict

```python
InfoDict = InfoDict
```

#### isValid

```python
isValid() -> bool
```

Return `True` if device is loaded and has a property by this name.

#### isLoaded

```python
isLoaded() -> bool
```

Return true if the device name is loaded.

#### fromCache

```python
fromCache() -> Any
```

Return cached property value.

#### setValue

```python
setValue(val: Any) -> None
```

Functional alternate to property setter.

#### isReadOnly

```python
isReadOnly() -> bool
```

Return `True` if property is read only.

#### isPreInit

```python
isPreInit() -> bool
```

Return `True` if property must be defined prior to initialization.

#### hasLimits

```python
hasLimits() -> bool
```

Return `True` if property has limits.

#### lowerLimit

```python
lowerLimit() -> float
```

Return lower limit if property has limits, or 0 otherwise.

#### upperLimit

```python
upperLimit() -> float
```

Return upper limit if property has limits, or 0 otherwise.

#### range

```python
range() -> tuple[float, float]
```

Return (lowerLimit, upperLimit) range tuple.

#### type

```python
type() -> PropertyType
```

Return `PropertyType` of this property.

#### deviceType

```python
deviceType() -> DeviceType
```

Return `DeviceType` of the device owning this property.

#### allowedValues

```python
allowedValues() -> tuple[str, ...]
```

Return allowed values for this property, if constrained.

#### isSequenceable

```python
isSequenceable() -> bool
```

Return `True` if property can be used in a sequence.

#### sequenceMaxLength

```python
sequenceMaxLength() -> int
```

Return maximum number of property events that can be put in a sequence.

#### loadSequence

```python
loadSequence(eventSequence: Sequence[str]) -> None
```

Transfer a sequence of events/states/whatever to the device.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `eventSequence` | `Sequence[str]` | The sequence of events/states that the device will execute in response to external triggers | *required* |

#### startSequence

```python
startSequence() -> None
```

Start an ongoing sequence of triggered events in a property.

#### stopSequence

```python
stopSequence() -> None
```

Stop an ongoing sequence of triggered events in a property.

#### dict

```python
dict() -> InfoDict
```

Return dict of info about this Property.

Returns a `dict` with the following keys: `"valid"`, `"value"`, `"type"`, `"device_type"`, `"read_only"`, `"sequenceable"`, `"sequence_max_length"`, `"pre_init"`, `"range"`, `"allowed_values"`.

If the device is invalid or not loaded, the `"valid"` key will be `False` and the rest of the keys will be `None`.

### Metadata

```python
Metadata(*args: Any, **kwargs: Any)
```

Bases: `Metadata`

Subclass of `pymmcore.Metadata` with a pythonic interface.

This subclass fully implements a `collections.abc.Mapping` interface (i.e. it behaves like a Python `dict`). It also adds a `json()` convenience method to convert to a JSON string.

#### get

```python
get(name: str, default: Any = _NULL) -> Any
```

#### copy

```python
copy() -> Metadata
```

#### clear

```python
clear() -> None
```

#### json

```python
json() -> str
```

#### keys

```python
keys() -> KeysView[str]
```

#### items

```python
items() -> ItemsView[str, str]
```

#### values

```python
values() -> ValuesView[str]
```

### CMMCoreSignaler

Bases: `SignalGroup`

Signals that will be emitted from CMMCorePlus objects (psygnal backend).

See `PCoreSignaler` for what each signal emits.

#### propertiesChanged

```python
propertiesChanged = Signal()
```

#### propertyChanged

```python
propertyChanged = Signal(str, str, str)
```

#### channelGroupChanged

```python
channelGroupChanged = Signal(str)
```

#### configGroupChanged

```python
configGroupChanged = Signal(str, str)
```

#### configSet

```python
configSet = Signal(str, str)
```

#### systemConfigurationLoaded

```python
systemConfigurationLoaded = Signal()
```

#### pixelSizeChanged

```python
pixelSizeChanged = Signal(float)
```

#### pixelSizeAffineChanged

```python
pixelSizeAffineChanged = Signal(float, float, float, float, float, float)
```

#### stagePositionChanged

```python
stagePositionChanged = Signal(str, float)
```

#### XYStagePositionChanged

```python
XYStagePositionChanged = Signal(str, float, float)
```

#### exposureChanged

```python
exposureChanged = Signal(str, float)
```

#### SLMExposureChanged

```python
SLMExposureChanged = Signal(str, float)
```

#### shutterOpenChanged

```python
shutterOpenChanged = Signal(str, bool)
```

#### imageSnapped

```python
imageSnapped = Signal(str)
```

#### sequenceAcquisitionStopped

```python
sequenceAcquisitionStopped = Signal(str)
```

#### sequenceAcquisitionStarted

```python
sequenceAcquisitionStarted: SignalInstance
```

#### mdaEngineRegistered

```python
mdaEngineRegistered = Signal(MDAEngine, MDAEngine)
```

#### continuousSequenceAcquisitionStarting

```python
continuousSequenceAcquisitionStarting = Signal()
```

#### continuousSequenceAcquisitionStarted

```python
continuousSequenceAcquisitionStarted = Signal()
```

#### sequenceAcquisitionStarting

```python
sequenceAcquisitionStarting: SignalInstance
```

#### autoShutterSet

```python
autoShutterSet = Signal(bool)
```

#### configGroupDeleted

```python
configGroupDeleted = Signal(str)
```

#### configDeleted

```python
configDeleted = Signal(str, str)
```

#### configDefined

```python
configDefined = Signal(str, str, str, str, str)
```

#### roiSet

```python
roiSet = Signal(str, int, int, int, int)
```

#### xYStagePositionChanged

```python
xYStagePositionChanged: SignalInstance
```

#### sLMExposureChanged

```python
sLMExposureChanged: SignalInstance
```

### GeneratorMDASequence

Bases: `MDASequence`

Placeholder sequence used when the runner is given events, not an `MDASequence`.

When `MDARunner.run` receives any iterable of events other than a `useq.MDASequence` (a list, a generator, a queue-backed iterator, a `useq.v2.MDASequence`, etc...), the shape of the experiment isn't known in advance. An empty `GeneratorMDASequence` is then passed to the engine's `setup_sequence` and emitted in `sequenceStarted` in its place.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `metadata` | `dict[str, Any]` |  |
| `axis_order` | `tuple[str, ...]` |  |
| `stage_positions` | `WellPlatePlan \| tuple[AbsolutePosition, ...]` |  |
| `grid_plan` | `GridFromEdges \| GridFromPolygon \| GridRowsColumns \| GridWidthHeight \| RandomPoints \| RelativePosition \| None` |  |
| `channels` | `tuple[Channel, ...]` |  |
| `time_plan` | `MultiPhaseTimePlan \| TIntervalDuration \| TIntervalLoops \| TDurationLoops \| None` |  |
| `z_plan` | `ZTopBottom \| ZAboveBelow \| ZRangeAround \| ZAbsolutePositions \| ZRelativePositions \| None` |  |
| `autofocus_plan` | `AxesBasedAF \| None` |  |
| `setup` | `MDAEvent \| None` |  |
| `keep_shutter_open_across` | `tuple[str, ...]` |  |

#### axis\_order

```python
axis_order: tuple[str, ...] = ()
```

#### sizes

```python
sizes: dict[str, int]
```

#### iter\_axis

```python
iter_axis(axis: str) -> Iterator
```

## Functions

### install\_pymmcore\_ipy\_completion

```python
install_pymmcore_ipy_completion(shell: InteractiveShell | None = None) -> None
```

Install the CMMCorePlus completion matcher in the current IPython session.

### find\_micromanager

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

1. An environment variable named `MICROMANAGER_PATH`.
2. A path previously selected with `mmcore use` (or `use_micromanager`).
3. A `Micro-Manager*` folder in the `mm` folder of the `pymmcore-plus` user data directory. This is where `mmcore install` puts things by default:

   - **Windows**: `C:\Users\<user>\AppData\Local\pymmcore-plus\pymmcore-plus\mm`
   - **macOS**: `~/Library/Application Support/pymmcore-plus/mm`
   - **Linux**: `~/.local/share/pymmcore-plus/mm`
4. The device adapters bundled with the [`mm-test-adapters`](<https://pypi.org/project/mm-test-adapters/>) Python package, if it is installed (`pip install mm-test-adapters`). These are just the test devices (`DemoCamera`, `Utilities`, `SequenceTester`, etc...).
5. A `Micro-Manager*` folder in the default Micro-Manager install location:

   - **Windows**: `C:/Program Files/`
   - **macOS**: `/Applications`
   - **Linux**: `/usr/local/lib`

With `return_first=True`, installations whose device interface version doesn't match the one required by the installed `pymmcore` are skipped (except for `MICROMANAGER_PATH`, which is always used as-is). Run `mmcore list` to see everything that was found, and which one is active.

> [!NOTE]
>
> This function is used by `pymmcore_plus.CMMCorePlus` to locate the Micro-Manager device adapters. By default, the output of this function is passed to `setDeviceAdapterSearchPaths` when creating a new `CMMCorePlus` instance.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `return_first` | `bool` | If True (default), return the first found path. If False, return a list of all found paths. | `True` |

### use\_micromanager

```python
use_micromanager(
    path: str | Path | None = None, pattern: str | Pattern[str] | None = None
) -> Path | None
```

Set the preferred Micro-Manager path.

This sets the preferred Micro-Manager path, and persists across sessions. This path takes precedence over everything *except* the `MICROMANAGER_PATH` environment variable. (This is what `mmcore use` calls.)

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `path` | `str \| Path \| None` | Path to an existing directory. This directory should contain Micro-Manager device adapters. If `None`, the path will be determined using `pattern`. | `None` |
| `pattern` | `str \| Pattern \| None` | A regex pattern to match against the Micro-Manager paths found by `find_micromanager`. If no match is found, a `FileNotFoundError` will be raised. | `None` |

### configure\_logging

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

- `PYMM_LOG_LEVEL` - The log level for `stderr` logging. By default `WARNING`.
- `PYMM_LOG_FILE` - The path to the log file. If set to `0`, `false`, `no`, or `none`, logging to file will be disabled.
- `PYMM_LOG_RICH` - If set to `1`, `true`, or `yes`, use `rich` for stderr logging. Note: rich formatting adds some overhead; see [https://github.com/pymmcore-plus/pymmcore-plus/issues/449](<https://github.com/pymmcore-plus/pymmcore-plus/issues/449>).

> [!NOTE]
>
> This function will clear all existing logging handlers and replace them with new ones. So be sure to pass all the settings you want to use each time you call this function.

Parameters:

<table>       <thead>         <tr>           <th>Name</th>           <th>Type</th>           <th>Description</th>           <th>Default</th>         </tr>       </thead>       <tbody>           <tr class="doc-section-item">             <td>                 <code>file</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.configure_logging" backlink-type="used-by" identifier="str" optional="">str</autoref> | <autoref backlink-anchor="pymmcore_plus.configure_logging" backlink-type="used-by" hover="" identifier="pathlib.Path" optional="">Path</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                 <p>Path to logfile. May also be set with the <code>PYMM_LOG_FILE</code> environment variable. If <code>None</code>, will not log to file.  By default, logs to <code>pymmcore-plus.log</code> in:</p> <ul> <li>macOS: <code>~/Library/Application Support/pymmcore-plus/logs</code></li> <li>Linux: <code>~/.local/share/pymmcore-plus/logs</code></li> <li>Windows: <code>C:\Users\&lt;username&gt;\AppData\Local\pymmcore-plus\pymmcore-plus\logs</code></li> </ul>                </div>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.configure_logging" backlink-type="used-by" hover="" identifier="pymmcore_plus._logger.LOG_FILE" optional="">LOG_FILE</autoref></code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>stderr_level</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.configure_logging" backlink-type="used-by" identifier="int" optional="">int</autoref> | <autoref backlink-anchor="pymmcore_plus.configure_logging" backlink-type="used-by" identifier="str" optional="">str</autoref></code>             </td>             <td>               <div class="doc-md-description">                 <p>Level for stderr logging. One of &quot;DEBUG&quot;, &quot;INFO&quot;, &quot;WARNING&quot;, &quot;ERROR&quot;, &quot;CRITICAL&quot;, or 10, 20, 30, 40, or 50, respectively. By default <code>&quot;WARNING&quot;</code> (or the value of <code>PYMM_LOG_LEVEL</code>).</p>                </div>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.configure_logging" backlink-type="used-by" hover="" identifier="pymmcore_plus._logger.DEFAULT_LOG_LEVEL" optional="">DEFAULT_LOG_LEVEL</autoref></code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>file_level</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.configure_logging" backlink-type="used-by" identifier="int" optional="">int</autoref> | <autoref backlink-anchor="pymmcore_plus.configure_logging" backlink-type="used-by" identifier="str" optional="">str</autoref></code>             </td>             <td>               <div class="doc-md-description">                 <p>Level for logging to file, by default <code>&quot;DEBUG&quot;</code>.</p>                </div>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.configure_logging" backlink-type="used-by" hover="" identifier="logging.DEBUG" optional="">DEBUG</autoref></code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>log_to_stderr</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.configure_logging" backlink-type="used-by" identifier="bool" optional="">bool</autoref></code>             </td>             <td>               <div class="doc-md-description">                 <p>Whether to log to stderr, by default True</p>                </div>             </td>             <td>                   <code>True</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>file_rotation</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.configure_logging" backlink-type="used-by" identifier="int" optional="">int</autoref></code>             </td>             <td>               <div class="doc-md-description">                 <p>When to rollover to the next log file, in MegaBytes, by default <code>40</code>.</p>                </div>             </td>             <td>                   <code>40</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>file_retention</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.configure_logging" backlink-type="used-by" identifier="int" optional="">int</autoref></code>             </td>             <td>               <div class="doc-md-description">                 <p>Maximum number of log files to retain, by default <code>20</code></p>                </div>             </td>             <td>                   <code>20</code>             </td>           </tr>       </tbody>     </table>
