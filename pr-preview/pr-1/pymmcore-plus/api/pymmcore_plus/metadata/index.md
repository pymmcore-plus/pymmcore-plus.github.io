# Metadata Schema

This page defines the schema for the metadata `dicts` emitted during the course of a [multi-dimensional acquisition](<https://pymmcore-plus.github.io/pymmcore-plus/guides/mda_engine/index.md>) (MDA).

These are not classes (and should not be imported outside of a `typing.TYPE_CHECKING` clause), but rather are `typing.TypedDict` definitions that outline the structure of objects that are passed to the `sequenceStarted` and `frameReady` callbacks in an MDA. One use case for these definitions is to provide type hints for the arguments to these callbacks, which is both handy for looking up the structure of the metadata and for static type checking:

```python
from __future__ import annotations

from typing import TYPE_CHECKING

from pymmcore_plus import CMMCorePlus

if TYPE_CHECKING:
    import numpy as np
    import useq

    from pymmcore_plus.metadata import FrameMetaV1

core = CMMCorePlus()


@core.mda.events.frameReady.connect
def on_frame(img: np.ndarray, event: useq.MDAEvent, meta: FrameMetaV1) -> None:
    # your editor now knows which keys `meta` has
    print(meta["camera_device"], meta["exposure_ms"], meta["runner_time_ms"])
```

## Primary metadata types

### pymmcore\_plus.metadata.SummaryMetaV1

Bases: `TypedDict`

Complete summary metadata for the system.

This is the structure of the summary metadata object that is emitted during the `sequenceStarted` event of an MDA run. It contains general information about the system and all of the devices.

It may be generated outside of a running mda sequence as well using `pymmcore_plus.metadata.summary_metadata`

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `format` | `Literal['summary-dict']` | The format of this summary metadata object. |
| `version` | `Literal['1.0']` | The version of this summary metadata object. |
| `datetime` | `NotRequired[str]` | The date and time when the summary metadata was generated. This is an ISO 8601 formatted string, including date, time and offset from UTC: `YYYY-MM-DD HH:MM:SS.mmmmmm+HH:MM` |
| `devices` | `tuple[DeviceInfo, ...]` | Information about all loaded devices. |
| `system_info` | `SystemInfo` | General system information. |
| `image_infos` | `tuple[ImageInfo, ...]` | Information about the current image structure. |
| `config_groups` | `tuple[ConfigGroup, ...]` | Groups of device property settings. |
| `pixel_size_configs` | `tuple[PixelSizeConfigPreset, ...]` | Pixel size presets. |
| `position` | `Position` | Current position in 3D space. |
| `mda_sequence` | `NotRequired[MDASequence]` | *NotRequired*. The current MDA sequence. |
| `extra` | `NotRequired[dict[str, Any]]` | *NotRequired*. Additional information, may be used to store arbitrary user info. |

### pymmcore\_plus.metadata.FrameMetaV1

Bases: `TypedDict`

Metadata for a single frame.

This is the structure of the summary metadata object that is emitted during the `frameReady` event of an MDA run. It contains information about the frame that was just acquired. By design, it is relatively lightweight and does not contain the full system state. Values that are not expected to change during an MDA sequence should be looked up in the summary metadata.

It may be generated outside of a running mda sequence as well using `pymmcore_plus.metadata.frame_metadata`

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `format` | `Literal['frame-dict']` | The format of this frame metadata object. |
| `version` | `Literal['1.0']` | The version of this frame metadata object. |
| `pixel_size_um` | `float` | The pixel size in microns. |
| `camera_device` | `str \| None` | The label of the camera device used to acquire the image. |
| `exposure_ms` | `float` | The exposure time in milliseconds. |
| `property_values` | `tuple[PropertyValue, ...]` | Device property settings. This is not a comprehensive list of all device properties, but only those that may have changed for this frame (such as properties in the channel config or light path config). |
| `runner_time_ms` | `float` | Elapsed time in milliseconds since the beginning of the MDA sequence. |
| `position` | `NotRequired[Position]` | *NotRequired*. The current stage position(s) in 3D space. This is often slow to retrieve, so its inclusion is optional and left to the implementer. |
| `mda_event` | `NotRequired[MDAEvent]` | *NotRequired*. The MDA event object that commanded the acquisition of this frame. |
| `hardware_triggered` | `NotRequired[bool]` | *NotRequired*. Whether the frame was part of a hardware-triggered sequence. If missing, assume `False`. |
| `images_remaining_in_buffer` | `NotRequired[int]` | *NotRequired*. The number of images remaining to be popped from the image buffer (only applicable for hardware-triggered sequences). |
| `camera_metadata` | `NotRequired[dict[str, Any]]` | *NotRequired*. Additional metadata from the camera device. This is unstructured and may contain any information that the camera device provides. Do not rely on the presence of any particular keys. |
| `extra` | `NotRequired[dict[str, Any]]` | *NotRequired*. Additional information, may be used to store arbitrary user info or additional metadata. |

---

## Supporting types

### pymmcore\_plus.metadata.DeviceInfo

Bases: `TypedDict`

Information about a specific device.

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `label` | `str` | The user-provided label of the device. |
| `library` | `str` | The name of the device adapter library (e.g. "DemoCamera" or "ASITiger"). |
| `name` | `str` | The name of the device, as known to the adapter. (e.g. "DCam" or "XYStage") |
| `type` | `str` | The type of the device (e.g. "Camera", "XYStage", "State", etc...) |
| `description` | `str` | A description of the device, provided by the adapter. |
| `properties` | `tuple[PropertyInfo, ...]` | Information about the device's properties. |
| `parent_label` | `NotRequired[str]` | *Not Required*. The label of the parent device, if any. This will be missing for hub devices and other devices that are not peripherals. |
| `labels` | `NotRequired[tuple[str, ...]]` | *Not Required*. The labels of the device, if it is a state device. |
| `child_names` | `NotRequired[tuple[str, ...]]` | *Not Required*. The names of the child (peripheral) devices, if it is a hub device. |
| `is_continuous_focus_drive` | `NotRequired[bool]` | *Not Required*. Whether the device is a continuous focus drive. If missing, assume `False`. |
| `focus_direction` | `NotRequired[Literal['Unknown', 'TowardSample', 'AwayFromSample']]` | *Not Required*. The direction of focus movement. Will be missing if device is not a Stage device. |
| `is_sequenceable` | `NotRequired[bool]` | *Not Required*. Whether the device is sequenceable. If missing, assume `False`. This may be present for Cameras, SLMs, Stages, and XYStages. See also the `is_sequenceable` property of each `PropertyInfo` object. |

### pymmcore\_plus.metadata.SystemInfo

Bases: `TypedDict`

General system information.

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `pymmcore_version` | `str` | The version of the PyMMCore library. |
| `pymmcore_backend` | `NotRequired[str]` | *Not Required*. The name of the PyMMCore backend in use (e.g. "pymmcore" or "pymmcore-nano"). |
| `pymmcore_plus_version` | `str` | The version of the PyMMCore Plus library. |
| `mmcore_version` | `str` | The version of the MMCore library. (e.g. `MMCore version 11.1.1`) |
| `device_api_version` | `str` | The version of the device API. (e.g. `Device API version 71, Module API version 10`) |
| `device_adapter_search_paths` | `tuple[str, ...]` | The active search paths for device adapters. This may be useful to indicate the nightly build of device adapters, or other information that isn't in the version numbers. |
| `system_configuration_file` | `str \| None` | The path of the last loaded system configuration file, if any. |
| `primary_log_file` | `str` | The path of the primary log file. |
| `sequence_buffer_size_mb` | `int` | The size of the circular buffer available for storing images during hardware-triggered sequence acquisition. |
| `continuous_focus_enabled` | `NotRequired[bool]` | *Not Required*. Whether continuous focus is enabled. |
| `continuous_focus_locked` | `NotRequired[bool]` | *Not Required*. Whether continuous focus is currently locked. |
| `auto_shutter` | `NotRequired[bool]` | *Not Required*. Whether auto-shutter is currently active. |
| `timeout_ms` | `NotRequired[int]` | *Not Required*. The current timeout in milliseconds for the system. The default timeout is 5000 ms. |

### pymmcore\_plus.metadata.ImageInfo

Bases: `TypedDict`

Information about the image format for a camera device.

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `camera_label` | `str` | The label of the corresponding camera device. |
| `plane_shape` | `tuple[int, ...]` | The shape (height, width\[, num\_components\]) of the numpy array that will be returned for each snap of the camera. This will be length 2 for monochromatic images, and length 3 for images with multiple components (e.g. RGB). |
| `dtype` | `str` | The numpy dtype of the image array (e.g. "uint8", "uint16", etc...) |
| `height` | `int` | The height of the image in pixels. |
| `width` | `int` | The width of the image in pixels. |
| `pixel_format` | `Literal['Mono8', 'Mono10', 'Mono12', 'Mono14', 'Mono16', 'Mono32', 'RGB8', 'RGB10', 'RGB12', 'RGB14', 'RGB16']` | The GenICam pixel format of the camera. See PixelFormat and [https://docs.baslerweb.com/pixel-format\#unpacked-and-packed-pixel-formats](<https://docs.baslerweb.com/pixel-format#unpacked-and-packed-pixel-formats>) for more information. |
| `pixel_size_config_name` | `str` | The name of the currently active pixel size configuration. |
| `pixel_size_um` | `float` | The pixel size in microns. |
| `magnification_factor` | `NotRequired[float]` | *Not Required*. The product of magnification of all loaded devices of type MagnifierDevice. If no devices are found, or all have magnification=1, this will not be present. |
| `pixel_size_affine` | `NotRequired[tuple[float, float, float, float, float, float]]` | *Not Required*. Affine Transform to relate camera pixels with stage movement, corrected for binning and known magnification devices. The affine transform consists of the first two rows of a 3x3 matrix, the third row is always assumed to be `(0, 0, 1)`. If missing, assume identity transform. |
| `roi` | `NotRequired[tuple[int, int, int, int]]` | *Not Required*. The active subarray (ROI: region of interest) on the camera, in the form `(x_offset, y_offset, width, height)`. If missing, the full chip is being used. |
| `multi_roi` | `NotRequired[tuple[list[int], list[int], list[int], list[int]]]` | *Not Required*. The active subarrays (ROIs: regions of interest) on the camera, in the form `(x_offsets, y_offsets, widths, heights)`. If missing, the camera does not support multiple ROIs or is not currently using them. |
| `num_camera_adapter_channels` | `NotRequired[int]` |  |

### pymmcore\_plus.metadata.ConfigGroup

Bases: `TypedDict`

A group of configuration presets.

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `str` | The name of the config group. |
| `presets` | `tuple[ConfigPreset, ...]` | A collection of presets, each of which define a set of device property settings that can be applied to the system. |

### pymmcore\_plus.metadata.ConfigPreset

Bases: `TypedDict`

A group of device property settings.

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `str` | The name of the preset. |
| `settings` | `tuple[PropertyValue, ...]` | A collection of device property settings that make up the preset. |

### pymmcore\_plus.metadata.PixelSizeConfigPreset

Bases: `ConfigPreset`

A specialized group of device property settings for a pixel size preset.

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `str` | The name of the pixel size preset. |
| `settings` | `tuple[PropertyValue, ...]` | A collection of device property settings that make up the pixel size preset. |
| `pixel_size_um` | `float` | The pixel size in microns. |
| `pixel_size_affine` | `NotRequired[tuple[float, float, float, float, float, float]]` | *Not Required*. Affine Transform to relate camera pixels with stage movement, corrected for binning and known magnification devices. The affine transform consists of the first two rows of a 3x3 matrix, the third row is always assumed to be 0.0 0.0 1.0. |
| `pixel_size_dxdz` | `NotRequired[float]` | *Not Required*. The angle between the camera's x axis and the axis (direction) of the z drive for the given pixel size configuration. This angle is dimensionless (i.e. the ratio of the translation in x caused by a translation in z, i.e. dx / dz). If missing, assume 0.0. |
| `pixel_size_dydz` | `NotRequired[float]` | *Not Required*. The angle between the camera's y axis and the axis (direction) of the z drive for the given pixel size configuration. This angle is dimensionless (i.e. the ratio of the translation in y caused by a translation in z, i.e. dy / dz). If missing, assume 0.0. |
| `pixel_size_optimal_z_um` | `NotRequired[float]` | *Not Required*. User-defined optimal Z step size is for this pixel size config. If missing, assume 0.0. |

### pymmcore\_plus.metadata.PropertyInfo

Bases: `TypedDict`

Information about a single device property.

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `str` | The name of the property. |
| `value` | `str \| None` | The current value of the property, if any. |
| `data_type` | `NotRequired[Literal['undefined', 'float', 'int', 'str']]` | *Not Required*. The data type of the `value` field. |
| `is_read_only` | `NotRequired[bool]` | *Not Required*. Whether the property is read-only. |
| `allowed_values` | `NotRequired[tuple[str, ...]]` | *Not Required*. The allowed values for the property, if any. Consumers should not depend on this field being present. |
| `is_pre_init` | `NotRequired[bool]` | *Not Required*. Whether the property is pre-init. If missing, assume `False`. |
| `limits` | `NotRequired[tuple[float, float]]` | *Not Required*. The limits of the property, if any. If missing, the property has no limits. |
| `sequenceable` | `NotRequired[bool]` | *Not Required*. Whether the property is sequenceable. If missing, assume `False`. |
| `sequence_max_length` | `NotRequired[int]` | *Not Required*. The maximum length of a sequence for the property, if applicable. Will be missing if the property is not sequenceable. |

### pymmcore\_plus.metadata.PropertyValue

Bases: `TypedDict`

A single device property setting.

This represents a single device property setting, whether it be an "active" value, or an intended value as a part of a configuration preset.

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `dev` | `str` | The label of the device. |
| `prop` | `str` | The name of the property. |
| `val` | `Any` | The value of the property. |

### pymmcore\_plus.metadata.Position

Bases: `TypedDict`

Represents a position in 3D space and focus.

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `x` | `NotRequired[float]` | *Not Required*. The X coordinate of the "active" XY stage device. May be missing if there is no current XY stage device. |
| `y` | `NotRequired[float]` | *Not Required*. The Y coordinate of the "active" XY stage device. May be missing if there is no current XY stage device. |
| `z` | `NotRequired[float]` | *Not Required*. The coordinate of the "active" focus device. May be missing if there is no current focus stage device. |
| `all_stages` | `NotRequired[list[StagePosition]]` | *Not Required*. The positions of *all* stage devices (both inactive and active devices that are represented by `x`, `y`, and `z`). Inclusion of this field is up to the implementer. |

### pymmcore\_plus.metadata.StagePosition

Bases: `TypedDict`

Represents the position of a single stage device.

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `device_label` | `str` |  |
| `position` | `float \| tuple[float, float]` |  |

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

Convert `obj` (e.g. a metadata dict) to builtin Python types.

### pymmcore\_plus.metadata.json\_dumps

```python
json_dumps = std_json_dumps
```

Serialize `obj` (e.g. a metadata dict) to JSON bytes.
