# pymmcore\_plus.seq\_tester

Classes for working with SequenceTester devices.

SequenceTester is a Micro-Manager device that encodes information about the state of the system into the image data. This module provides a class for decoding that information.

Decoding images requires the `msgpack` package to be installed. A typical way to setup the device would be:

```python
core = CMMCorePlus()
core.loadDevice("THub", "SequenceTester", "THub")
core.initializeDevice("THub")
core.loadDevice("TCamera", "SequenceTester", "TCamera")
core.setParentLabel("TCamera", "THub")
core.setProperty("TCamera", "ImageMode", "MachineReadable")
core.setProperty("TCamera", "ImageWidth", 128)
core.setProperty("TCamera", "ImageHeight", 128)
core.initializeDevice("TCamera")
core.setCameraDevice("TCamera")
```

Then, to decode an image:

```python
from pymmcore_plus.seq_tester import decode_image

core.snapImage()
info = decode_image(core.getImage())
```

Classes:

| Name | Description |
| --- | --- |
| `CameraInfo` | Information about a SequenceTester camera. |
| `InfoPacket` | Data produced by a SequenceTester camera. |
| `Setting` | Setting of a SequenceTester property. |
| `SettingEvent` | Historical Setting. |

Functions:

| Name | Description |
| --- | --- |
| `decode_image` | Extract data produced by a SequenceTester camera. |

## CameraInfo

```python
CameraInfo(
    name: str,
    serial_img_num: int,
    is_sequence: bool,
    cumulative_img_num: int,
    frame_num: int,
)
```

Information about a SequenceTester camera.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` |  | *required* |
| `serial_img_num` | `int` |  | *required* |
| `is_sequence` | `bool` |  | *required* |
| `cumulative_img_num` | `int` |  | *required* |
| `frame_num` | `int` |  | *required* |

Methods:

| Name | Description |
| --- | --- |
| `validate` | Coerce val into CameraInfo object. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `str` |  |
| `serial_img_num` | `int` |  |
| `is_sequence` | `bool` |  |
| `cumulative_img_num` | `int` |  |
| `frame_num` | `int` |  |

### name

```python
name: str
```

### serial\_img\_num

```python
serial_img_num: int
```

### is\_sequence

```python
is_sequence: bool
```

### cumulative\_img\_num

```python
cumulative_img_num: int
```

### frame\_num

```python
frame_num: int
```

### validate

```python
validate(val: Any) -> CameraInfo
```

Coerce val into CameraInfo object.

## InfoPacket

```python
InfoPacket(
    hub_global_packet_nr: int,
    camera_info: CameraInfo,
    start_counter: int,
    current_counter: int,
    start_state: list[Setting],
    current_state: list[Setting],
    history: list[SettingEvent],
)
```

Data produced by a SequenceTester camera.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `hub_global_packet_nr` | `int` |  | *required* |
| `camera_info` | `CameraInfo` |  | *required* |
| `start_counter` | `int` |  | *required* |
| `current_counter` | `int` |  | *required* |
| `start_state` | `list[Setting]` |  | *required* |
| `current_state` | `list[Setting]` |  | *required* |
| `history` | `list[SettingEvent]` |  | *required* |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `hub_global_packet_nr` | `int` |  |
| `camera_info` | `CameraInfo` |  |
| `start_counter` | `int` |  |
| `current_counter` | `int` |  |
| `start_state` | `list[Setting]` |  |
| `current_state` | `list[Setting]` |  |
| `history` | `list[SettingEvent]` |  |

### hub\_global\_packet\_nr

```python
hub_global_packet_nr: int
```

### camera\_info

```python
camera_info: CameraInfo
```

### start\_counter

```python
start_counter: int
```

### current\_counter

```python
current_counter: int
```

### start\_state

```python
start_state: list[Setting]
```

### current\_state

```python
current_state: list[Setting]
```

### history

```python
history: list[SettingEvent]
```

## Setting

```python
Setting(device: str, property: str, type: type, value: Any)
```

Setting of a SequenceTester property.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device` | `str` |  | *required* |
| `property` | `str` |  | *required* |
| `type` | `type` |  | *required* |
| `value` | `Any` |  | *required* |

Methods:

| Name | Description |
| --- | --- |
| `validate` | Coerce val into Setting object. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `device` | `str` |  |
| `property` | `str` |  |
| `type` | `type` |  |
| `value` | `Any` |  |

### device

```python
device: str
```

### property

```python
property: str
```

### type

```python
type: type
```

### value

```python
value: Any
```

### validate

```python
validate(val: Any) -> Self
```

Coerce val into Setting object.

## SettingEvent

```python
SettingEvent(device: str, property: str, type: type, value: Any, count: int)
```

Bases: `Setting`

Historical Setting.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device` | `str` |  | *required* |
| `property` | `str` |  | *required* |
| `type` | `type` |  | *required* |
| `value` | `Any` |  | *required* |
| `count` | `int` |  | *required* |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `count` | `int` |  |

### count

```python
count: int
```

## decode\_image

```python
decode_image(img: ndarray) -> InfoPacket
```

Extract data produced by a SequenceTester camera.
