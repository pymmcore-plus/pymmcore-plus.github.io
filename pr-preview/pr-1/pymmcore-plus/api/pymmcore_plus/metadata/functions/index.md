# pymmcore\_plus.metadata.functions

Functions:

| Name | Description |
| --- | --- |
| `config_group` | Return a dictionary of configuration presets for a specific group. |
| `config_groups` | Return all configuration groups. |
| `device_info` | Return information about a specific device label. |
| `devices_info` | Return a dictionary of device information for all loaded devices. |
| `image_info` | Return information about the current camera image properties. |
| `image_infos` | Return information about the current image properties for all cameras. |
| `pixel_size_config` | Return info for a specific pixel size preset for a specific. |
| `pixel_size_configs` | Return a dictionary of pixel size configurations. |
| `position` | Return current position of active (and, optionally, all) stages. |
| `properties` | Return a dictionary of device properties values for all loaded devices. |
| `property_info` | Return information on a specific device property. |
| `system_info` | Return general system information. |

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `DEFAULT_AFFINE` |  |  |

## DEFAULT\_AFFINE

```python
DEFAULT_AFFINE = (1.0, 0.0, 0.0, 0.0, 1.0, 0.0)
```

## config\_group

```python
config_group(core: CMMCorePlus, *, group_name: str) -> ConfigGroup
```

Return a dictionary of configuration presets for a specific group.

## config\_groups

```python
config_groups(core: CMMCorePlus) -> tuple[ConfigGroup, ...]
```

Return all configuration groups.

## device\_info

```python
device_info(
    core: CMMCorePlus,
    *,
    label: str,
    cached: bool = True,
    include_property_details: bool = True,
) -> DeviceInfo
```

Return information about a specific device label.

## devices\_info

```python
devices_info(
    core: CMMCorePlus,
    cached: bool = True,
    include_property_details: bool = True,
) -> tuple[DeviceInfo, ...]
```

Return a dictionary of device information for all loaded devices.

## image\_info

```python
image_info(core: CMMCorePlus) -> ImageInfo
```

Return information about the current camera image properties.

## image\_infos

```python
image_infos(core: CMMCorePlus) -> tuple[ImageInfo, ...]
```

Return information about the current image properties for all cameras.

## pixel\_size\_config

```python
pixel_size_config(
    core: CMMCorePlus, *, config_name: str
) -> PixelSizeConfigPreset
```

Return info for a specific pixel size preset for a specific.

## pixel\_size\_configs

```python
pixel_size_configs(core: CMMCorePlus) -> tuple[PixelSizeConfigPreset, ...]
```

Return a dictionary of pixel size configurations.

## position

```python
position(core: CMMCorePlus, all_stages: bool = False) -> Position
```

Return current position of active (and, optionally, all) stages.

## properties

```python
properties(
    core: CMMCorePlus,
    device: str,
    *,
    cached: bool = True,
    include_details: bool = True,
) -> tuple[PropertyInfo, ...]
```

Return a dictionary of device properties values for all loaded devices.

## property\_info

```python
property_info(
    core: CMMCorePlus,
    device: str,
    prop: str,
    *,
    cached: bool = True,
    include_property_details: bool = True,
) -> PropertyInfo
```

Return information on a specific device property.

## system\_info

```python
system_info(core: CMMCorePlus) -> SystemInfo
```

Return general system information.

## Re-exports

These names can be imported from this module, but are documented at their top-level location.

| Name | Description |
| --- | --- |
| `frame_metadata` | Return metadata for the current frame. |
| `summary_metadata` | Return a summary metadata for the current state of the system. |
