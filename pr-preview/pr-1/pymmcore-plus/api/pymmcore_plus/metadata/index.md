# Metadata Schema

This page defines the schema for the metadata `dicts` emitted during the course of an [Multi-dimensional Acquisition](<https://pymmcore-plus.github.io/pymmcore-plus/guides/mda_engine/index.md>) (MDA).

These are not classes (and should not be imported outside of a `typing.TYPE_CHECKING` clause), but rather are `typing.TypedDict` definitions that outline the structure of objects that are passed to the `sequenceStarted` and `frameReady` callbacks in an MDA. One use case for these definitions is to provide type hints for the arguments to these callbacks, which is both handy for looking up the structure of the metadata and for static type checking.

## Primary Metadata Types

### pymmcore\_plus.metadata.SummaryMetaV1

Bases: `TypedDict`

Complete summary metadata for the system.

This is the structure of the summary metadata object that is emitted during the `sequenceStarted` event of an MDA run. It contains general information about the system and all of the devices.

It may be generated outside of a running mda sequence as well using `pymmcore_plus.metadata.summary_metadata`

Keys:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `format` | `Literal['summary-dict']` |  | *required* |
| `version` | `Literal['1.0']` |  | *required* |
| `datetime` | `NotRequired[str]` |  | *required* |
| `devices` | `tuple[DeviceInfo, ...]` |  | *required* |
| `system_info` | `SystemInfo` |  | *required* |
| `image_infos` | `tuple[ImageInfo, ...]` |  | *required* |
| `config_groups` | `tuple[ConfigGroup, ...]` |  | *required* |
| `pixel_size_configs` | `tuple[PixelSizeConfigPreset, ...]` |  | *required* |
| `position` | `Position` |  | *required* |
| `mda_sequence` | `NotRequired[MDASequence]` |  | *required* |
| `extra` | `NotRequired[dict[str, Any]]` |  | *required* |

### pymmcore\_plus.metadata.FrameMetaV1

Bases: `TypedDict`

Metadata for a single frame.

This is the structure of the summary metadata object that is emitted during the `frameReady` event of an MDA run. It contains information about the frame that was just acquired. By design, it is relatively lightweight and does not contain the full system state. Values that are not expected to change during an MDA sequence should be looked up in the summary metadata.

It may be generated outside of a running mda sequence as well using `pymmcore_plus.metadata.frame_metadata`

Keys:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `format` | `Literal['frame-dict']` |  | *required* |
| `version` | `Literal['1.0']` |  | *required* |
| `pixel_size_um` | `float` |  | *required* |
| `camera_device` | `str \| None` |  | *required* |
| `exposure_ms` | `float` |  | *required* |
| `property_values` | `tuple[PropertyValue, ...]` |  | *required* |
| `runner_time_ms` | `float` |  | *required* |
| `position` | `NotRequired[Position]` |  | *required* |
| `mda_event` | `NotRequired[MDAEvent]` |  | *required* |
| `hardware_triggered` | `NotRequired[bool]` |  | *required* |
| `images_remaining_in_buffer` | `NotRequired[int]` |  | *required* |
| `camera_metadata` | `NotRequired[dict[str, Any]]` |  | *required* |
| `extra` | `NotRequired[dict[str, Any]]` |  | *required* |

---

## Supporting Types

### pymmcore\_plus.metadata.DeviceInfo

Bases: `TypedDict`

Information about a specific device.

Keys:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `label` | `str` |  | *required* |
| `library` | `str` |  | *required* |
| `name` | `str` |  | *required* |
| `type` | `str` |  | *required* |
| `description` | `str` |  | *required* |
| `properties` | `tuple[PropertyInfo, ...]` |  | *required* |
| `parent_label` | `NotRequired[str]` |  | *required* |
| `labels` | `NotRequired[tuple[str, ...]]` |  | *required* |
| `child_names` | `NotRequired[tuple[str, ...]]` |  | *required* |
| `is_continuous_focus_drive` | `NotRequired[bool]` |  | *required* |
| `focus_direction` | `NotRequired[Literal['Unknown', 'TowardSample', 'AwayFromSample']]` |  | *required* |
| `is_sequenceable` | `NotRequired[bool]` |  | *required* |

### pymmcore\_plus.metadata.SystemInfo

Bases: `TypedDict`

General system information.

Keys:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `pymmcore_version` | `str` |  | *required* |
| `pymmcore_backend` | `NotRequired[str]` |  | *required* |
| `pymmcore_plus_version` | `str` |  | *required* |
| `mmcore_version` | `str` |  | *required* |
| `device_api_version` | `str` |  | *required* |
| `device_adapter_search_paths` | `tuple[str, ...]` |  | *required* |
| `system_configuration_file` | `str \| None` |  | *required* |
| `primary_log_file` | `str` |  | *required* |
| `sequence_buffer_size_mb` | `int` |  | *required* |
| `continuous_focus_enabled` | `NotRequired[bool]` |  | *required* |
| `continuous_focus_locked` | `NotRequired[bool]` |  | *required* |
| `auto_shutter` | `NotRequired[bool]` |  | *required* |
| `timeout_ms` | `NotRequired[int]` |  | *required* |

### pymmcore\_plus.metadata.ImageInfo

Bases: `TypedDict`

Information about the image format for a camera device.

Keys:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `camera_label` | `str` |  | *required* |
| `plane_shape` | `tuple[int, ...]` |  | *required* |
| `dtype` | `str` |  | *required* |
| `height` | `int` |  | *required* |
| `width` | `int` |  | *required* |
| `pixel_format` | `Literal['Mono8', 'Mono10', 'Mono12', 'Mono14', 'Mono16', 'Mono32', 'RGB8', 'RGB10', 'RGB12', 'RGB14', 'RGB16']` |  | *required* |
| `pixel_size_config_name` | `str` |  | *required* |
| `pixel_size_um` | `float` |  | *required* |
| `magnification_factor` | `NotRequired[float]` |  | *required* |
| `pixel_size_affine` | `NotRequired[tuple[float, float, float, float, float, float]]` |  | *required* |
| `roi` | `NotRequired[tuple[int, int, int, int]]` |  | *required* |
| `multi_roi` | `NotRequired[tuple[list[int], list[int], list[int], list[int]]]` |  | *required* |
| `num_camera_adapter_channels` | `NotRequired[int]` |  | *required* |

### pymmcore\_plus.metadata.ConfigGroup

Bases: `TypedDict`

A group of configuration presets.

Keys:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` |  | *required* |
| `presets` | `tuple[ConfigPreset, ...]` |  | *required* |

### pymmcore\_plus.metadata.ConfigPreset

Bases: `TypedDict`

A group of device property settings.

Keys:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` |  | *required* |
| `settings` | `tuple[PropertyValue, ...]` |  | *required* |

### pymmcore\_plus.metadata.PixelSizeConfigPreset

Bases: `ConfigPreset`

A specialized group of device property settings for a pixel size preset.

Keys:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` |  | *required* |
| `settings` | `tuple[PropertyValue, ...]` |  | *required* |
| `pixel_size_um` | `float` |  | *required* |
| `pixel_size_affine` | `NotRequired[tuple[float, float, float, float, float, float]]` |  | *required* |
| `pixel_size_dxdz` | `NotRequired[float]` |  | *required* |
| `pixel_size_dydz` | `NotRequired[float]` |  | *required* |
| `pixel_size_optimal_z_um` | `NotRequired[float]` |  | *required* |

### pymmcore\_plus.metadata.PropertyInfo

Bases: `TypedDict`

Information about a single device property.

Keys:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` |  | *required* |
| `value` | `str \| None` |  | *required* |
| `data_type` | `NotRequired[Literal['undefined', 'float', 'int', 'str']]` |  | *required* |
| `is_read_only` | `NotRequired[bool]` |  | *required* |
| `allowed_values` | `NotRequired[tuple[str, ...]]` |  | *required* |
| `is_pre_init` | `NotRequired[bool]` |  | *required* |
| `limits` | `NotRequired[tuple[float, float]]` |  | *required* |
| `sequenceable` | `NotRequired[bool]` |  | *required* |
| `sequence_max_length` | `NotRequired[int]` |  | *required* |

### pymmcore\_plus.metadata.PropertyValue

Bases: `TypedDict`

A single device property setting.

This represents a single device property setting, whether it be an "active" value, or an intended value as a part of a configuration preset.

Keys:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `dev` | `str` |  | *required* |
| `prop` | `str` |  | *required* |
| `val` | `Any` |  | *required* |

### pymmcore\_plus.metadata.Position

Bases: `TypedDict`

Represents a position in 3D space and focus.

Keys:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `x` | `NotRequired[float]` |  | *required* |
| `y` | `NotRequired[float]` |  | *required* |
| `z` | `NotRequired[float]` |  | *required* |
| `all_stages` | `NotRequired[list[StagePosition]]` |  | *required* |

### pymmcore\_plus.metadata.StagePosition

Bases: `TypedDict`

Represents the position of a single stage device.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_label` | `str` |  | *required* |
| `position` | `float \| tuple[float, float]` |  | *required* |

---

## Functions

In most cases, the metadata dicts described above will be received as an argument to either the `sequenceStarted` or `frameReady` callbacks in an MDA. However, they can also be generated with the following functions.

### pymmcore\_plus.metadata.summary\_metadata

```python
summary_metadata(
    core: CMMCorePlus,
    *,
    mda_sequence: MDASequence | None = None,
    cached: bool = True,
    include_time: bool = True,
    include_property_details: bool = True,
) -> SummaryMetaV1
```

Return a summary metadata for the current state of the system.

See pymmcore\_plus.metadata.SummaryMetaV1 for a description of the dictionary format.

### pymmcore\_plus.metadata.frame\_metadata

```python
frame_metadata(
    core: CMMCorePlus,
    *,
    cached: bool = True,
    runner_time_ms: float = -1,
    camera_device: str | None = None,
    property_values: tuple[PropertyValue, ...] = (),
    include_position: bool = False,
    **kwargs: Unpack[_OptionalFrameMetaKwargs],
) -> FrameMetaV1
```

Return metadata for the current frame.

## Serialization

Helpers to convert metadata (which may contain numpy arrays, `useq` objects, etc.) to builtin Python types or JSON.

### pymmcore\_plus.metadata.to\_builtins

```python
to_builtins = std_to_builtins
```

### pymmcore\_plus.metadata.json\_dumps

```python
json_dumps = std_json_dumps
```
