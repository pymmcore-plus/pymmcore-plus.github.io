# Device &amp; Property objects

`pymmcore-plus` offers two classes that provide a more **object-oriented** interface to common operations and queries performed on devices and their properties.

In the original `CMMCore` API, there are a lot of methods that accept a `deviceLabel` string as the first argument (and perhaps additional arguments) and query something about that device (e.g. `getDeviceLibrary`, `getDeviceType`, `waitForDevice`, etc...). In `pymmcore-plus`, the `Device` class acts as a "view" onto a specific device, and these methods are implemented as methods (that no longer require the `deviceLabel` argument), and the `deviceLabel` is passed to the constructor.

Similarly, there are many methods in the `CMMCore` API that require both a device label and a device property name, and modify that specific property (e.g. `isPropertySequenceable`, `getProperty`, `isPropertyReadOnly`, etc...). Here, the `DeviceProperty` class acts as a "view" onto a specific device property, with an object-oriented interface to these methods.

```python
from pymmcore_plus import CMMCorePlus

core = CMMCorePlus()
core.loadSystemConfiguration()  # demo config

camera = core.getDeviceObject("Camera")
print(camera.type(), camera.library())  # Camera DemoCamera

exposure = camera.getPropertyObject("Exposure")
exposure.value = 42
print(exposure.value, exposure.isReadOnly(), exposure.range())  # 42.0 False (0.0, 10000.0)
```

> [!TIP]
>
> **API reference**
>
> See `Device`, `DeviceProperty`, and `DeviceAdapter` for the full API.

## Property info

`DeviceProperty.dict()` returns all information about a property as a typed dictionary:

### InfoDict

Bases: `TypedDict`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `valid` | `ForwardRef('bool', module='pymmcore_plus.core._property')` |  | *required* |
| `value` | `ForwardRef('Any \| None', module='pymmcore_plus.core._property')` |  | *required* |
| `type` | `ForwardRef('str \| None', module='pymmcore_plus.core._property')` |  | *required* |
| `device_type` | `ForwardRef('str \| None', module='pymmcore_plus.core._property')` |  | *required* |
| `read_only` | `ForwardRef('bool \| None', module='pymmcore_plus.core._property')` |  | *required* |
| `sequenceable` | `ForwardRef('bool \| None', module='pymmcore_plus.core._property')` |  | *required* |
| `sequence_max_length` | `ForwardRef('int \| None', module='pymmcore_plus.core._property')` |  | *required* |
| `pre_init` | `ForwardRef('bool \| None', module='pymmcore_plus.core._property')` |  | *required* |
| `range` | `ForwardRef('tuple[float, float] \| None', module='pymmcore_plus.core._property')` |  | *required* |
| `allowed_values` | `ForwardRef('tuple[str, ...] \| None', module='pymmcore_plus.core._property')` |  | *required* |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `valid` | `bool` |  |
| `value` | `Any \| None` |  |
| `type` | `str \| None` |  |
| `device_type` | `str \| None` |  |
| `read_only` | `bool \| None` |  |
| `sequenceable` | `bool \| None` |  |
| `sequence_max_length` | `int \| None` |  |
| `pre_init` | `bool \| None` |  |
| `range` | `tuple[float, float] \| None` |  |
| `allowed_values` | `tuple[str, ...] \| None` |  |

#### valid

```python
valid: bool
```

#### value

```python
value: Any | None
```

#### type

```python
type: str | None
```

#### device\_type

```python
device_type: str | None
```

#### read\_only

```python
read_only: bool | None
```

#### sequenceable

```python
sequenceable: bool | None
```

#### sequence\_max\_length

```python
sequence_max_length: int | None
```

#### pre\_init

```python
pre_init: bool | None
```

#### range

```python
range: tuple[float, float] | None
```

#### allowed\_values

```python
allowed_values: tuple[str, ...] | None
```
