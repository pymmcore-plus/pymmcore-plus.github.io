# useq.pycromanager

Convert useq objects to the event dicts used by [Pycro-Manager](<https://pycro-manager.readthedocs.io>).

**Classes**

| Name | Description |
| --- | --- |
| `PycroManagerAxes` | Axes dict used by pycro-manager. |
| `PycroManagerEvent` | Dict in the format expected by pycro-manager. |

**Functions**

| Name | Description |
| --- | --- |
| `to_pycromanager` | Convert a `useq.MDAEvent` or `useq.MDASequence` to pycro-manager form. |

**Attributes**

| Name | Description |
| --- | --- |
| `PycroAxis` |  |
| `PycroKey` |  |

## Classes

### PycroManagerAxes

Bases: `TypedDict`

Axes dict used by pycro-manager.

#### time

```python
time: int
```

#### position

```python
position: int
```

#### z

```python
z: int
```

#### channel

```python
channel: str
```

#### row

```python
row: int
```

#### column

```python
column: int
```

### PycroManagerEvent

Bases: `TypedDict`

Dict in the format expected by pycro-manager.

#### axes

```python
axes: Required[PycroManagerAxes]
```

#### x

```python
x: float
```

#### y

```python
y: float
```

#### z

```python
z: float
```

#### min\_start\_time

```python
min_start_time: float
```

#### config\_group

```python
config_group: list[str]
```

#### exposure

```python
exposure: float
```

#### properties

```python
properties: list[list[str]]
```

#### keep\_shutter\_open

```python
keep_shutter_open: bool
```

## Functions

### to\_pycromanager

```python
to_pycromanager(obj: MDAEvent) -> PycroManagerEvent
```

```python
to_pycromanager(obj: MDASequence) -> list[PycroManagerEvent]
```

```python
to_pycromanager(
    obj: MDAEvent | MDASequence,
) -> PycroManagerEvent | list[PycroManagerEvent]
```

Convert a `useq.MDAEvent` or `useq.MDASequence` to pycro-manager form.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `obj` | `MDAEvent \| MDASequence` | The event or sequence to convert. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `PycroManagerEvent \| list[PycroManagerEvent]` | If `obj` is an `useq.MDAEvent`, returns a single pycro-manager event dict. Otherwise, returns a list of pycro-manager event dicts. |

## Attributes

### PycroAxis

```python
PycroAxis = Literal['time', 'position', 'z', 'channel', 'row', 'column']
```

### PycroKey

```python
PycroKey = Literal[
    "x", "y", "z", "exposure", "min_start_time", "keep_shutter_open"
]
```
