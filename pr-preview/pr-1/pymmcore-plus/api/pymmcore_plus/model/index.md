# pymmcore\_plus.model

Classes:

| Name | Description |
| --- | --- |
| `AvailableDevice` | Model of an available device, with a possible hub parent. |
| `ConfigGroup` | ConfigGroup model. |
| `ConfigPreset` | ConfigPreset model. |
| `CoreDevice` | CoreDevice(name: 'str' = 'Core', library: 'str' = '', adapter\_name: 'str' = 'Core', description: 'str' = 'Core device', device\_type: 'DeviceType' = , properties: 'list\[Property\]' = , delay\_ms: 'float' = 0.0, uses\_delay: 'bool' = False, parent\_label: 'str' = '', initialized: 'bool' = False, labels: 'tuple\[str, ...\]' = , focus\_direction: 'FocusDirection' = , children: 'tuple\[str, ...\]' = ) |
| `Device` | Model of a device. |
| `Microscope` | Full model of a microscope. |
| `PixelSizeGroup` | Model of the pixel size group. |
| `PixelSizePreset` | PixelSizePreset model. |
| `Property` | Model of a device property. |
| `Setting` | Model of a device setting. |

## AvailableDevice

```python
AvailableDevice(
    name: str = UNDEFINED,
    library: str = "",
    adapter_name: str = "",
    description: str = "",
    device_type: DeviceType = Any,
    properties: list[Property] = list(),
    delay_ms: float = 0.0,
    uses_delay: bool = False,
    parent_label: str = "",
    initialized: bool = False,
    labels: tuple[str, ...] = tuple(),
    focus_direction: FocusDirection = Unknown,
    children: tuple[str, ...] = tuple(),
    library_hub: AvailableDevice | None = None,
)
```

Bases: `Device`

Model of an available device, with a possible hub parent.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` |  | `'UNDEFINED'` |
| `library` | `str` |  | `''` |
| `adapter_name` | `str` |  | `''` |
| `description` | `str` |  | `''` |
| `device_type` | `DeviceType` |  | `<DeviceType.AnyType: 1>` |
| `properties` | `list[Property]` | Built-in mutable sequence.<br><br>If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified. | `<dynamic>` |
| `delay_ms` | `float` |  | `0.0` |
| `uses_delay` | `bool` |  | `False` |
| `parent_label` | `str` |  | `''` |
| `initialized` | `bool` |  | `False` |
| `labels` | `tuple[str, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |
| `focus_direction` | `FocusDirection` |  | `<FocusDirection.Unknown: 0>` |
| `children` | `tuple[str, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |
| `library_hub` | `AvailableDevice \| None` |  | `None` |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `library_hub` | `AvailableDevice \| None` |  |

### library\_hub

```python
library_hub: AvailableDevice | None = None
```

## ConfigGroup

```python
ConfigGroup(name: str, presets: MutableMapping[str, ConfigPreset] = dict())
```

ConfigGroup model.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` |  | *required* |
| `presets` | `MutableMapping[str, ConfigPreset]` | dict() -\> new empty dictionary dict(mapping) -\> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -\> new dictionary initialized as if via: d = {} for k, v in iterable: d\[k\] = v dict(\*\*kwargs) -\> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) | `<class 'dict'>` |

Methods:

| Name | Description |
| --- | --- |
| `from_metadata` |  |
| `create_from_core` |  |
| `update_from_core` | Update this object's values from the core. |
| `all_config_groups` | Get all config presets from the given core. |
| `apply_to_core` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `str` |  |
| `presets` | `MutableMapping[str, ConfigPreset]` |  |

### name

```python
name: str
```

### presets

```python
presets: MutableMapping[str, ConfigPreset] = field(default_factory=dict)
```

### from\_metadata

```python
from_metadata(meta: ConfigGroup) -> Self
```

### create\_from\_core

```python
create_from_core(core: CMMCorePlus, name: str) -> Self
```

### update\_from\_core

```python
update_from_core(core: CMMCorePlus) -> None
```

Update this object's values from the core.

### all\_config\_groups

```python
all_config_groups(core: CMMCorePlus) -> dict[str, ConfigGroup]
```

Get all config presets from the given core.

### apply\_to\_core

```python
apply_to_core(
    core: CMMCorePlus,
    *,
    exclude: Container[str] = (),
    on_err: ErrCallback | None = None,
    apply_properties: bool = False,
    then_update: bool = True,
) -> None
```

## ConfigPreset

```python
ConfigPreset(name: str, settings: list[Setting] = list())
```

ConfigPreset model.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` |  | *required* |
| `settings` | `list[Setting]` | Built-in mutable sequence.<br><br>If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified. | `<dynamic>` |

Methods:

| Name | Description |
| --- | --- |
| `from_metadata` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `str` |  |
| `settings` | `list[Setting]` |  |

### name

```python
name: str
```

### settings

```python
settings: list[Setting] = field(default_factory=list)
```

### from\_metadata

```python
from_metadata(meta: ConfigPreset) -> Self
```

## CoreDevice

```python
CoreDevice(
    name: str = CORE,
    library: str = "",
    adapter_name: str = CORE,
    description: str = "Core device",
    device_type: DeviceType = Core,
    properties: list[Property] = _core_props(),
    delay_ms: float = 0.0,
    uses_delay: bool = False,
    parent_label: str = "",
    initialized: bool = False,
    labels: tuple[str, ...] = tuple(),
    focus_direction: FocusDirection = Unknown,
    children: tuple[str, ...] = tuple(),
)
```

Bases: `Device`

CoreDevice(name: 'str' = 'Core', library: 'str' = '', adapter\_name: 'str' = 'Core', description: 'str' = 'Core device', device\_type: 'DeviceType' = , properties: 'list\[Property\]' = , delay\_ms: 'float' = 0.0, uses\_delay: 'bool' = False, parent\_label: 'str' = '', initialized: 'bool' = False, labels: 'tuple\[str, ...\]' = , focus\_direction: 'FocusDirection' = , children: 'tuple\[str, ...\]' = )

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` |  | `'Core'` |
| `library` | `str` |  | `''` |
| `adapter_name` | `str` |  | `'Core'` |
| `description` | `str` |  | `'Core device'` |
| `device_type` | `DeviceType` |  | `<DeviceType.CoreDevice: 10>` |
| `properties` | `list[Property]` | Built-in mutable sequence.<br><br>If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified. | `[Property(device_name='Core', name='AutoShutter', value='1', is_read_only=False, is_pre_init=False, allowed_values=('0', '1'), has_limits=False, lower_limit=0.0, upper_limit=0.0, property_type=undefined), Property(device_name='Core', name='Camera', value='', is_read_only=False, is_pre_init=False, allowed_values=('',), has_limits=False, lower_limit=0.0, upper_limit=0.0, property_type=undefined), Property(device_name='Core', name='Shutter', value='', is_read_only=False, is_pre_init=False, allowed_values=('',), has_limits=False, lower_limit=0.0, upper_limit=0.0, property_type=undefined), Property(device_name='Core', name='Focus', value='', is_read_only=False, is_pre_init=False, allowed_values=('',), has_limits=False, lower_limit=0.0, upper_limit=0.0, property_type=undefined), Property(device_name='Core', name='XYStage', value='', is_read_only=False, is_pre_init=False, allowed_values=('',), has_limits=False, lower_limit=0.0, upper_limit=0.0, property_type=undefined), Property(device_name='Core', name='AutoFocus', value='', is_read_only=False, is_pre_init=False, allowed_values=('',), has_limits=False, lower_limit=0.0, upper_limit=0.0, property_type=undefined), Property(device_name='Core', name='ImageProcessor', value='', is_read_only=False, is_pre_init=False, allowed_values=('',), has_limits=False, lower_limit=0.0, upper_limit=0.0, property_type=undefined), Property(device_name='Core', name='SLM', value='', is_read_only=False, is_pre_init=False, allowed_values=('',), has_limits=False, lower_limit=0.0, upper_limit=0.0, property_type=undefined), Property(device_name='Core', name='Galvo', value='', is_read_only=False, is_pre_init=False, allowed_values=('',), has_limits=False, lower_limit=0.0, upper_limit=0.0, property_type=undefined), Property(device_name='Core', name='ChannelGroup', value='', is_read_only=False, is_pre_init=False, allowed_values=('',), has_limits=False, lower_limit=0.0, upper_limit=0.0, property_type=undefined), Property(device_name='Core', name='TimeoutMs', value='', is_read_only=False, is_pre_init=False, allowed_values=('',), has_limits=False, lower_limit=0.0, upper_limit=0.0, property_type=undefined)]` |
| `delay_ms` | `float` |  | `0.0` |
| `uses_delay` | `bool` |  | `False` |
| `parent_label` | `str` |  | `''` |
| `initialized` | `bool` |  | `False` |
| `labels` | `tuple[str, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |
| `focus_direction` | `FocusDirection` |  | `<FocusDirection.Unknown: 0>` |
| `children` | `tuple[str, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |

Methods:

| Name | Description |
| --- | --- |
| `apply_to_core` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `str` |  |
| `adapter_name` | `str` |  |
| `device_type` | `DeviceType` |  |
| `description` | `str` |  |
| `properties` | `list[Property]` |  |

### name

```python
name: str = CORE
```

### adapter\_name

```python
adapter_name: str = CORE
```

### device\_type

```python
device_type: DeviceType = DeviceType.Core
```

### description

```python
description: str = 'Core device'
```

### properties

```python
properties: list[Property] = field(default_factory=_core_props)
```

### apply\_to\_core

```python
apply_to_core(
    core: CMMCorePlus,
    *,
    exclude: Container[str] = (value,),
    on_err: ErrCallback | None = None,
    apply_properties: bool = True,
    then_update: bool = True,
) -> None
```

## Device

```python
Device(
    name: str = UNDEFINED,
    library: str = "",
    adapter_name: str = "",
    description: str = "",
    device_type: DeviceType = Any,
    properties: list[Property] = list(),
    delay_ms: float = 0.0,
    uses_delay: bool = False,
    parent_label: str = "",
    initialized: bool = False,
    labels: tuple[str, ...] = tuple(),
    focus_direction: FocusDirection = Unknown,
    children: tuple[str, ...] = tuple(),
)
```

Bases: `CoreObject`

Model of a device.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` |  | `'UNDEFINED'` |
| `library` | `str` |  | `''` |
| `adapter_name` | `str` |  | `''` |
| `description` | `str` |  | `''` |
| `device_type` | `DeviceType` |  | `<DeviceType.AnyType: 1>` |
| `properties` | `list[Property]` | Built-in mutable sequence.<br><br>If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified. | `<dynamic>` |
| `delay_ms` | `float` |  | `0.0` |
| `uses_delay` | `bool` |  | `False` |
| `parent_label` | `str` |  | `''` |
| `initialized` | `bool` |  | `False` |
| `labels` | `tuple[str, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |
| `focus_direction` | `FocusDirection` |  | `<FocusDirection.Unknown: 0>` |
| `children` | `tuple[str, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |

Methods:

| Name | Description |
| --- | --- |
| `from_metadata` |  |
| `get_property` | Get a device by name. |
| `set_property` |  |
| `set_prop_default` | Works similar to `dict.set_default`. Add property if it doesn't exist. |
| `replace` |  |
| `create_from_core` |  |
| `update_from_core` | Update device properties from the core. |
| `load` | Load device properties from the core. |
| `unload` | Unload device from the core. |
| `initialize` | Initialize the device in core. |
| `apply_to_core` |  |
| `child_descriptions` |  |
| `loaded_peripherals` | Return device labels of all loaded devices that belong to this hub. |
| `available_peripherals` | Return all available devices that belong to this hub that aren't in model. |
| `set_label` | Set the label for a state device. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `str` |  |
| `library` | `str` |  |
| `adapter_name` | `str` |  |
| `description` | `str` |  |
| `device_type` | `DeviceType` |  |
| `properties` | `list[Property]` |  |
| `delay_ms` | `float` |  |
| `uses_delay` | `bool` |  |
| `parent_label` | `str` |  |
| `initialized` | `bool` |  |
| `labels` | `tuple[str, ...]` |  |
| `focus_direction` | `FocusDirection` |  |
| `children` | `tuple[str, ...]` |  |
| `port` | `str \| None` | Returns the value of the first property named "Port". |

### name

```python
name: str = UNDEFINED
```

### library

```python
library: str = ''
```

### adapter\_name

```python
adapter_name: str = ''
```

### description

```python
description: str = ''
```

### device\_type

```python
device_type: DeviceType = DeviceType.Any
```

### properties

```python
properties: list[Property] = field(default_factory=list)
```

### delay\_ms

```python
delay_ms: float = 0.0
```

### uses\_delay

```python
uses_delay: bool = False
```

### parent\_label

```python
parent_label: str = ''
```

### initialized

```python
initialized: bool = False
```

### labels

```python
labels: tuple[str, ...] = field(default_factory=tuple)
```

### focus\_direction

```python
focus_direction: FocusDirection = FocusDirection.Unknown
```

### children

```python
children: tuple[str, ...] = field(default_factory=tuple)
```

### port

```python
port: str | None
```

Returns the value of the first property named "Port".

Returns `None` if the device has no port property.

### from\_metadata

```python
from_metadata(metadata: DeviceInfo) -> Self
```

### get\_property

```python
get_property(name: str) -> Property
```

Get a device by name.

### set\_property

```python
set_property(prop_name: str, value: Any) -> None
```

### set\_prop\_default

```python
set_prop_default(prop_name: str, value: str = '', **kwargs: Any) -> Property
```

Works similar to `dict.set_default`. Add property if it doesn't exist.

### replace

```python
replace(**kwargs: Any) -> Device
```

### create\_from\_core

```python
create_from_core(core: CMMCorePlus, *args: Any, **kwargs: Any) -> Device
```

### update\_from\_core

```python
update_from_core(
    core: CMMCorePlus,
    *,
    exclude: Container[str] = (),
    on_err: ErrCallback | None = None,
) -> None
```

Update device properties from the core.

### load

```python
load(core: CMMCorePlus, *, reload: bool = False) -> None
```

Load device properties from the core.

### unload

```python
unload(core: CMMCorePlus) -> None
```

Unload device from the core.

### initialize

```python
initialize(
    core: CMMCorePlus,
    *,
    apply_pre_init: bool = False,
    reload: bool = False,
    then_update: bool = True,
) -> None
```

Initialize the device in core.

### apply\_to\_core

```python
apply_to_core(
    core: CMMCorePlus,
    *,
    exclude: Container[str] = ("delay_ms",),
    on_err: ErrCallback | None = None,
    apply_properties: bool = True,
    then_update: bool = True,
) -> None
```

### child\_descriptions

```python
child_descriptions(core: CMMCorePlus) -> tuple[str, ...]
```

### loaded\_peripherals

```python
loaded_peripherals(core: CMMCorePlus) -> tuple[str, ...]
```

Return device labels of all loaded devices that belong to this hub.

NOTE: unlike "available\_peripherals", this returns device labels currently loaded into core. It does not check whether the devices are in the model.

### available\_peripherals

```python
available_peripherals(model: Microscope) -> Iterable[AvailableDevice]
```

Return all available devices that belong to this hub that aren't in model.

### set\_label

```python
set_label(state: int | str, label: str) -> None
```

Set the label for a state device.

## Microscope

```python
Microscope(
    core_device: CoreDevice = CoreDevice(),
    devices: list[Device] = list(),
    config_groups: dict[str, ConfigGroup] = dict(),
    pixel_size_group: PixelSizeGroup = PixelSizeGroup(),
    config_file: str = "",
    initialized: bool = False,
)
```

Full model of a microscope.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `core_device` | `CoreDevice` | CoreDevice(name: 'str' = 'Core', library: 'str' = '', adapter\_name: 'str' = 'Core', description: 'str' = 'Core device', device\_type: 'DeviceType' = , properties: 'list\[Property\]' = , delay\_ms: 'float' = 0.0, uses\_delay: 'bool' = False, parent\_label: 'str' = '', initialized: 'bool' = False, labels: 'tuple\[str, ...\]' = , focus\_direction: 'FocusDirection' = , children: 'tuple\[str, ...\]' = ) | `<dynamic>` |
| `devices` | `list[Device]` | Built-in mutable sequence.<br><br>If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified. | `<dynamic>` |
| `config_groups` | `dict[str, ConfigGroup]` | dict() -\> new empty dictionary dict(mapping) -\> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -\> new dictionary initialized as if via: d = {} for k, v in iterable: d\[k\] = v dict(\*\*kwargs) -\> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) | `<class 'dict'>` |
| `pixel_size_group` | `PixelSizeGroup` | Model of the pixel size group. | `<dynamic>` |
| `config_file` | `str` |  | `''` |
| `initialized` | `bool` |  | `False` |

Methods:

| Name | Description |
| --- | --- |
| `reset` | Reset the Microscope to an empty state. |
| `is_dirty` | Return True if the model has changed since last save. |
| `mark_clean` | Mark the model as clean. |
| `get_device` | Get a device by name. |
| `filter_devices` | Filter devices by name . |
| `create_from_config` |  |
| `load_config` | Load model from a micro-manager config file or string. |
| `save` | Save model as a micro-manager config file. |
| `from_summary_metadata` | Create a Microscope model from summary metadata. |
| `create_from_core` |  |
| `update_from_core` | Update this object's values from the core. |
| `apply_to_core` |  |
| `initialize` | Attempt to initialize all devices in the model. |
| `load_available_devices` | Load the available device list. |
| `update_config_groups_from_core` | Load config groups from the core. |
| `update_pixel_sizes_from_core` | Load pixel size groups from the core. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `core_device` | `CoreDevice` |  |
| `devices` | `list[Device]` |  |
| `config_groups` | `dict[str, ConfigGroup]` |  |
| `pixel_size_group` | `PixelSizeGroup` |  |
| `config_file` | `str` |  |
| `initialized` | `bool` |  |
| `available_devices` | `tuple[AvailableDevice, ...]` |  |
| `assigned_com_ports` | `dict[Device, Device]` | Return map of SerialDevice -\> DeviceUsingIt. |
| `available_serial_devices` | `Iterable[Device]` | Return the available com ports. |

### core\_device

```python
core_device: CoreDevice = field(default_factory=CoreDevice)
```

### devices

```python
devices: list[Device] = field(default_factory=list)
```

### config\_groups

```python
config_groups: dict[str, ConfigGroup] = field(default_factory=dict)
```

### pixel\_size\_group

```python
pixel_size_group: PixelSizeGroup = field(default_factory=PixelSizeGroup)
```

### config\_file

```python
config_file: str = ''
```

### initialized

```python
initialized: bool = False
```

### available\_devices

```python
available_devices: tuple[AvailableDevice, ...]
```

### assigned\_com\_ports

```python
assigned_com_ports: dict[Device, Device]
```

Return map of SerialDevice -\> DeviceUsingIt.

A com port is "claimed" if it is assigned to a device.

### available\_serial\_devices

```python
available_serial_devices: Iterable[Device]
```

Return the available com ports.

### reset

```python
reset() -> None
```

Reset the Microscope to an empty state.

### is\_dirty

```python
is_dirty() -> bool
```

Return True if the model has changed since last save.

### mark\_clean

```python
mark_clean() -> None
```

Mark the model as clean.

### get\_device

```python
get_device(name: str) -> Device
```

Get a device by name.

### filter\_devices

```python
filter_devices(
    name: str | None = None,
    library: str | None = None,
    adapter_name: str | None = None,
    description: str | None = None,
    device_type: DeviceType | str | None = None,
    parent_label: str | None = None,
) -> Iterable[Device]
```

Filter devices by name .

### create\_from\_config

```python
create_from_config(config_file: str | Path) -> Microscope
```

### load\_config

```python
load_config(path_or_text: str | Path) -> None
```

Load model from a micro-manager config file or string.

### save

```python
save(path: str | Path) -> None
```

Save model as a micro-manager config file.

### from\_summary\_metadata

```python
from_summary_metadata(summary_meta: SummaryMetaV1) -> Microscope
```

Create a Microscope model from summary metadata.

This may be used to load a model from summary metadata, such as as written during the course of a Multi-Dimensional Acquisition. This is useful for restoring the state of a microscope from a specific experiment, or writing out a cfg file that can be used to restore the state of the microscope.

### create\_from\_core

```python
create_from_core(core: CMMCorePlus, *args: Any, **kwargs: Any) -> Microscope
```

### update\_from\_core

```python
update_from_core(
    core: CMMCorePlus,
    *,
    exclude: Container[str] = (),
    on_err: ErrCallback | None = None,
) -> None
```

Update this object's values from the core.

### apply\_to\_core

```python
apply_to_core(
    core: CMMCorePlus,
    *,
    exclude: Container[str] = (),
    on_err: ErrCallback | None = None,
    apply_properties: bool = True,
    then_update: bool = True,
) -> None
```

### initialize

```python
initialize(
    core: CMMCorePlus,
    on_fail: Callable[[Device | Property, BaseException], bool | None] = _noop,
) -> None
```

Attempt to initialize all devices in the model.

Simulates what MMCore does upon loading config file.

### load\_available\_devices

```python
load_available_devices(core: CMMCorePlus) -> None
```

Load the available device list.

### update\_config\_groups\_from\_core

```python
update_config_groups_from_core(core: CMMCorePlus) -> None
```

Load config groups from the core.

### update\_pixel\_sizes\_from\_core

```python
update_pixel_sizes_from_core(core: CMMCorePlus) -> None
```

Load pixel size groups from the core.

## PixelSizeGroup

```python
PixelSizeGroup(
    name: str = PIXEL_SIZE_GROUP,
    presets: MutableMapping[str, PixelSizePreset] = dict(),
)
```

Bases: `ConfigGroup`

Model of the pixel size group.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` |  | `'PixelSizeGroup'` |
| `presets` | `MutableMapping[str, PixelSizePreset]` | dict() -\> new empty dictionary dict(mapping) -\> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -\> new dictionary initialized as if via: d = {} for k, v in iterable: d\[k\] = v dict(\*\*kwargs) -\> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) | `<class 'dict'>` |

Methods:

| Name | Description |
| --- | --- |
| `from_metadata` | Create a PixelSizeGroup from metadata. |
| `create_from_core` | Create pixel size presets from the given core. |
| `apply_to_core` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `str` |  |
| `presets` | `MutableMapping[str, PixelSizePreset]` |  |

### name

```python
name: str = PIXEL_SIZE_GROUP
```

### presets

```python
presets: MutableMapping[str, PixelSizePreset] = field(default_factory=dict)
```

### from\_metadata

```python
from_metadata(meta: tuple[PixelSizeConfigPreset, ...]) -> Self
```

Create a PixelSizeGroup from metadata.

### create\_from\_core

```python
create_from_core(
    core: CMMCorePlus, name: str = PIXEL_SIZE_GROUP
) -> PixelSizeGroup
```

Create pixel size presets from the given core.

### apply\_to\_core

```python
apply_to_core(
    core: CMMCorePlus,
    *,
    exclude: Container[str] = (),
    on_err: ErrCallback | None = None,
    apply_properties: bool = False,
    then_update: bool = True,
) -> None
```

## PixelSizePreset

```python
PixelSizePreset(
    name: str,
    settings: list[Setting] = list(),
    pixel_size_um: float = 0.0,
    affine: AffineTuple = DEFAULT_AFFINE,
    angle_dxdz: float = 0.0,
    angle_dydz: float = 0.0,
    optimalz_um: float = 0.0,
)
```

Bases: `ConfigPreset`

PixelSizePreset model.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` |  | *required* |
| `settings` | `list[Setting]` | Built-in mutable sequence.<br><br>If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified. | `<dynamic>` |
| `pixel_size_um` | `float` |  | `0.0` |
| `affine` | `AffineTuple` |  | `(1.0, 0.0, 0.0, 0.0, 1.0, 0.0)` |
| `angle_dxdz` | `float` |  | `0.0` |
| `angle_dydz` | `float` |  | `0.0` |
| `optimalz_um` | `float` |  | `0.0` |

Methods:

| Name | Description |
| --- | --- |
| `from_metadata` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `pixel_size_um` | `float` |  |
| `affine` | `AffineTuple` |  |
| `angle_dxdz` | `float` |  |
| `angle_dydz` | `float` |  |
| `optimalz_um` | `float` |  |

### pixel\_size\_um

```python
pixel_size_um: float = 0.0
```

### affine

```python
affine: AffineTuple = DEFAULT_AFFINE
```

### angle\_dxdz

```python
angle_dxdz: float = 0.0
```

### angle\_dydz

```python
angle_dydz: float = 0.0
```

### optimalz\_um

```python
optimalz_um: float = 0.0
```

### from\_metadata

```python
from_metadata(meta: PixelSizeConfigPreset) -> Self
```

## Property

```python
Property(
    device_name: str,
    name: str,
    value: str = "",
    is_read_only: bool = False,
    is_pre_init: bool = False,
    allowed_values: tuple[str, ...] = tuple(),
    has_limits: bool = False,
    lower_limit: float = 0.0,
    upper_limit: float = 0.0,
    property_type: PropertyType = Undef,
)
```

Bases: `CoreObject`

Model of a device property.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_name` | `str` |  | *required* |
| `name` | `str` |  | *required* |
| `value` | `str` |  | `''` |
| `is_read_only` | `bool` |  | `False` |
| `is_pre_init` | `bool` |  | `False` |
| `allowed_values` | `tuple[str, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |
| `has_limits` | `bool` |  | `False` |
| `lower_limit` | `float` |  | `0.0` |
| `upper_limit` | `float` |  | `0.0` |
| `property_type` | `PropertyType` |  | `undefined` |

Methods:

| Name | Description |
| --- | --- |
| `apply_to_core` | Apply the property to the given Core instance. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `device_name` | `str` |  |
| `name` | `str` |  |
| `value` | `str` |  |
| `is_read_only` | `bool` |  |
| `is_pre_init` | `bool` |  |
| `allowed_values` | `tuple[str, ...]` |  |
| `has_limits` | `bool` |  |
| `lower_limit` | `float` |  |
| `upper_limit` | `float` |  |
| `property_type` | `PropertyType` |  |

### device\_name

```python
device_name: str
```

### name

```python
name: str
```

### value

```python
value: str = ''
```

### is\_read\_only

```python
is_read_only: bool = False
```

### is\_pre\_init

```python
is_pre_init: bool = False
```

### allowed\_values

```python
allowed_values: tuple[str, ...] = field(default_factory=tuple)
```

### has\_limits

```python
has_limits: bool = False
```

### lower\_limit

```python
lower_limit: float = 0.0
```

### upper\_limit

```python
upper_limit: float = 0.0
```

### property\_type

```python
property_type: PropertyType = PropertyType.Undef
```

### apply\_to\_core

```python
apply_to_core(
    core: CMMCorePlus,
    *,
    exclude: Container[str] = (),
    on_err: ErrCallback | None = None,
    then_update: bool = True,
) -> None
```

Apply the property to the given Core instance.

## Setting

Bases: `NamedTuple`

Model of a device setting.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_name` | `ForwardRef('str')` |  | `'UNDEFINED'` |
| `property_name` | `ForwardRef('str')` |  | `'UNDEFINED'` |
| `property_value` | `ForwardRef('str')` |  | `'UNDEFINED'` |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `device_name` | `str` |  |
| `property_name` | `str` |  |
| `property_value` | `str` |  |

### device\_name

```python
device_name: str = UNDEFINED
```

### property\_name

```python
property_name: str = UNDEFINED
```

### property\_value

```python
property_value: str = UNDEFINED
```
