# useq

Implementation agnostic schema for multi-dimensional microscopy experiments.

Classes:

| Name | Description |
| --- | --- |
| `AbsolutePosition` | An absolute position in 3D space. |
| `Axis` | Recognized useq-schema axis keys. |
| `CameraROI` | Camera region of interest. |
| `RelativePosition` | A relative position in 3D space. |
| `SLMImage` | SLM Image in a MDA event. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `AnyAutofocusPlan` |  |  |
| `AnyTimePlan` |  |  |
| `AnyZPlan` |  |  |
| `GridRelative` |  |  |
| `MultiPointPlan` |  |  |
| `RelativeMultiPointPlan` |  |  |

## AnyAutofocusPlan

```python
AnyAutofocusPlan = AxesBasedAF
```

## AnyTimePlan

```python
AnyTimePlan = MultiPhaseTimePlan | SinglePhaseTimePlan
```

## AnyZPlan

```python
AnyZPlan = (
    ZTopBottom
    | ZAboveBelow
    | ZRangeAround
    | ZAbsolutePositions
    | ZRelativePositions
)
```

## GridRelative

```python
GridRelative = GridRowsColumns
```

## MultiPointPlan

```python
MultiPointPlan = AbsoluteMultiPointPlan | RelativeMultiPointPlan
```

## RelativeMultiPointPlan

```python
RelativeMultiPointPlan = (
    GridRowsColumns | GridWidthHeight | RandomPoints | RelativePosition
)
```

## AbsolutePosition

Bases: `PositionBase`, `FrozenModel`

An absolute position in 3D space.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `x` | `float \| None` |  | `None` |
| `y` | `float \| None` |  | `None` |
| `z` | `float \| None` |  | `None` |
| `name` | `str \| None` |  | `None` |
| `sequence` | `MDASequence \| None` |  | `None` |
| `properties` | `list[PropertyTuple] \| None` |  | `None` |
| `plate_row` | `int \| None` |  | `None` |
| `plate_col` | `int \| None` |  | `None` |
| `grid_row` | `int \| None` |  | `None` |
| `grid_col` | `int \| None` |  | `None` |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `is_relative` | `bool` |  |

### is\_relative

```python
is_relative: bool
```

## Axis

Bases: `StrEnum`

Recognized useq-schema axis keys.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `TIME` | `Literal['t']` | Time axis. |
| `POSITION` | `Literal['p']` | XY Stage Position axis. |
| `GRID` | `Literal['g']` | Grid axis (usually an additional row/column iteration around a position). |
| `CHANNEL` | `Literal['c']` | Channel axis. |
| `Z` | `Literal['z']` | Z axis. |

### TIME

```python
TIME = 't'
```

### POSITION

```python
POSITION = 'p'
```

### GRID

```python
GRID = 'g'
```

### CHANNEL

```python
CHANNEL = 'c'
```

### Z

```python
Z = 'z'
```

## CameraROI

Bases: `UseqModel`

Camera region of interest.

May be initialized with a `(offset_x, offset_y, width, height)` tuple.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `offset_x` | `int` |  | *required* |
| `offset_y` | `int` |  | *required* |
| `width` | `int` |  | *required* |
| `height` | `int` |  | *required* |

Classes:

| Name | Description |
| --- | --- |
| `Kwargs` | Type for the kwargs passed to the CameraROI. |

### offset\_x

```python
offset_x: NonNegativeInt
```

### offset\_y

```python
offset_y: NonNegativeInt
```

### width

```python
width: NonNegativeInt
```

### height

```python
height: NonNegativeInt
```

### Kwargs

Bases: `TypedDict`

Type for the kwargs passed to the CameraROI.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `offset_x` | `int` |  |
| `offset_y` | `int` |  |
| `width` | `int` |  |
| `height` | `int` |  |

#### offset\_x

```python
offset_x: int
```

#### offset\_y

```python
offset_y: int
```

#### width

```python
width: int
```

#### height

```python
height: int
```

## RelativePosition

Bases: `PositionBase`, `_MultiPointPlan['RelativePosition']`

A relative position in 3D space.

Relative positions also support `fov_width` and `fov_height` attributes, and can be used to define a single field of view for a "multi-point" plan.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `fov_width` | `float \| None` |  | `None` |
| `fov_height` | `float \| None` |  | `None` |
| `x` | `float` |  | `0` |
| `y` | `float` |  | `0` |
| `z` | `float` |  | `0` |
| `name` | `str \| None` |  | `None` |
| `sequence` | `MDASequence \| None` |  | `None` |
| `properties` | `list[PropertyTuple] \| None` |  | `None` |
| `plate_row` | `int \| None` |  | `None` |
| `plate_col` | `int \| None` |  | `None` |
| `grid_row` | `int \| None` |  | `None` |
| `grid_col` | `int \| None` |  | `None` |

Methods:

| Name | Description |
| --- | --- |
| `num_positions` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `x` | `float` |  |
| `y` | `float` |  |
| `z` | `float` |  |

### x

```python
x: float = 0
```

### y

```python
y: float = 0
```

### z

```python
z: float = 0
```

### num\_positions

```python
num_positions() -> int
```

## SLMImage

Bases: `UseqModel`

SLM Image in a MDA event.

This object can be cast to a numpy.array using `np.asarray` or `np.array`.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `data` | `Any` |  | *required* |
| `device` | `str \| None` |  | `None` |
| `exposure` | `float \| None` |  | `None` |

Classes:

| Name | Description |
| --- | --- |
| `Kwargs` | Type for the kwargs passed to the SLM image. |

### data

```python
data: Any = Field(..., repr=False)
```

### device

```python
device: str | None = None
```

### exposure

```python
exposure: float | None = Field(default=None, gt=0.0)
```

### Kwargs

Bases: `TypedDict`

Type for the kwargs passed to the SLM image.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `data` | `ArrayLike` |  |
| `device` | `str \| None` |  |
| `exposure` | `float \| None` |  |

#### data

```python
data: ArrayLike
```

#### device

```python
device: str | None
```

#### exposure

```python
exposure: float | None
```

## Documented on other pages

| Object | Page | Description |
| --- | --- | --- |
| `AcquireImage` | Event | `useq.Action` to acquire an image. |
| `Action` | Event | Base class for a `useq.MDAEvent` action. |
| `AutoFocusPlan` | Hardware Autofocus Plan | Base class for hardware autofocus plans. |
| `AxesBasedAF` | Hardware Autofocus Plan | Autofocus plan that performs autofocus when any of the specified axes change. |
| `Channel` | Axes | Define an acquisition channel. |
| `CustomAction` | Event | `useq.Action` to perform a custom action. |
| `EventChannel` | Event | Channel in a MDA event. |
| `GridFromEdges` | Axes | Yield absolute stage positions to cover a bounded area. |
| `GridFromPolygon` | Axes | Grid plan based on a polygon boundary. |
| `GridRowsColumns` | Axes | Grid plan based on number of rows and columns. |
| `GridWidthHeight` | Axes | Grid plan based on total width and height. |
| `HardwareAutofocus` | Event | `useq.Action` to perform a hardware autofocus. |
| `MDAEvent` | Event | Define a single event in a `MDASequence`. |
| `MDASequence` | Sequence | A sequence of MDA (Multi-Dimensional Acquisition) events. |
| `MultiPhaseTimePlan` | Axes | Time sequence composed of multiple phases. |
| `OrderMode` | Axes | Order in which grid positions will be iterated. |
| `Position` | Axes |  |
| `PropertyTuple` | Event | Three-tuple capturing a device, property, and value. |
| `RandomPoints` | Axes | Yield random points in a specified geometric shape. |
| `Shape` | Axes | Shape of the bounding box for random points. |
| `TDurationLoops` | Axes | Define temporal sequence using duration and number of loops. |
| `TIntervalDuration` | Axes | Define temporal sequence using interval and duration. |
| `TIntervalLoops` | Axes | Define temporal sequence using interval and number of loops. |
| `TraversalOrder` | Axes |  |
| `WellPlate` | Axes | A multi-well plate definition. |
| `WellPlatePlan` | Axes | A plan for acquiring images from a multi-well plate. |
| `ZAboveBelow` | Axes | Define Z as asymmetric range above and below some reference position. |
| `ZAbsolutePositions` | Axes | Define Z as a list of absolute positions. |
| `ZRangeAround` | Axes | Define Z as a symmetric range around some reference position. |
| `ZRelativePositions` | Axes | Define Z as a list of positions relative to some reference. |
| `ZTopBottom` | Axes | Define Z using absolute top &amp; bottom positions. |
| `register_well_plates` | Axes | Register well-plate definitions to allow lookup by key. |
| `registered_well_plate_keys` | Axes | Return a set of all registered well-plate keys. |
