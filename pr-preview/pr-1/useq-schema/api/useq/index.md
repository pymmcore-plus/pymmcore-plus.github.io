# useq

Implementation agnostic schema for multi-dimensional microscopy experiments.

**Submodules**

| Name | Description |
| --- | --- |
| `pycromanager` | Convert useq objects to the event dicts used by [Pycro-Manager](<https://pycro-manager.readthedocs.io>). |
| `v2` | New MDASequence API (preview). |

**Classes**

| Name | Description |
| --- | --- |
| `AbsolutePosition` | An absolute position in 3D space. |
| `AcquireImage` | `useq.Action` to acquire an image. |
| `Action` | Base class for a `useq.MDAEvent` action. |
| `AutoFocusPlan` | Base class for hardware autofocus plans. |
| `AxesBasedAF` | Autofocus plan that performs autofocus when any of the specified axes change. |
| `Axis` | Recognized useq-schema axis keys. |
| `CameraROI` | Camera region of interest. |
| `Channel` | Define an acquisition channel. |
| `CustomAction` | `useq.Action` to perform a custom action. |
| `EventChannel` | Channel in a MDA event. |
| `GridFromEdges` | Yield absolute stage positions to cover a bounded area. |
| `GridFromPolygon` | Grid plan based on a polygon boundary. |
| `GridRowsColumns` | Grid plan based on number of rows and columns. |
| `GridWidthHeight` | Grid plan based on total width and height. |
| `HardwareAutofocus` | `useq.Action` to perform a hardware autofocus. |
| `MDAEvent` | Define a single event in a `MDASequence`. |
| `MDASequence` | A sequence of MDA (Multi-Dimensional Acquisition) events. |
| `MultiPhaseTimePlan` | Time sequence composed of multiple phases. |
| `OrderMode` | Order in which grid positions will be iterated. |
| `PropertyTuple` | Three-tuple capturing a device, property, and value. |
| `RandomPoints` | Yield random points in a specified geometric shape. |
| `RelativePosition` | A relative position in 3D space. |
| `SLMImage` | SLM Image in a MDA event. |
| `Shape` | Shape of the bounding box for random points. |
| `TDurationLoops` | Define temporal sequence using duration and number of loops. |
| `TIntervalDuration` | Define temporal sequence using interval and duration. |
| `TIntervalLoops` | Define temporal sequence using interval and number of loops. |
| `TraversalOrder` | Order in which random points are visited. |
| `WellPlate` | A multi-well plate definition. |
| `WellPlatePlan` | A plan for acquiring images from a multi-well plate. |
| `ZAboveBelow` | Define Z as asymmetric range above and below some reference position. |
| `ZAbsolutePositions` | Define Z as a list of absolute positions. |
| `ZRangeAround` | Define Z as a symmetric range around some reference position. |
| `ZRelativePositions` | Define Z as a list of positions relative to some reference. |
| `ZTopBottom` | Define Z using absolute top &amp; bottom positions. |

**Functions**

| Name | Description |
| --- | --- |
| `register_well_plates` | Register well-plate definitions to allow lookup by key. |
| `registered_well_plate_keys` | Return a set of all registered well-plate keys. |

**Attributes**

| Name | Description |
| --- | --- |
| `AnyAutofocusPlan` |  |
| `AnyTimePlan` |  |
| `AnyZPlan` |  |
| `GridRelative` |  |
| `MultiPointPlan` |  |
| `Position` |  |
| `RelativeMultiPointPlan` |  |

## Classes

### Axis

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

#### TIME

```python
TIME = 't'
```

#### POSITION

```python
POSITION = 'p'
```

#### GRID

```python
GRID = 'g'
```

#### CHANNEL

```python
CHANNEL = 'c'
```

#### Z

```python
Z = 'z'
```

### CameraROI

Bases: `UseqModel`

Camera region of interest.

May be initialized with a `(offset_x, offset_y, width, height)` tuple.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `offset_x` | `int` | X offset of the ROI in pixels. Must be \>= 0. |
| `offset_y` | `int` | Y offset of the ROI in pixels. Must be \>= 0. |
| `width` | `int` | Width of the ROI in pixels. Must be \>= 0. |
| `height` | `int` | Height of the ROI in pixels. Must be \>= 0. |

#### offset\_x

```python
offset_x: NonNegativeInt
```

#### offset\_y

```python
offset_y: NonNegativeInt
```

#### width

```python
width: NonNegativeInt
```

#### height

```python
height: NonNegativeInt
```

### SLMImage

Bases: `UseqModel`

SLM Image in a MDA event.

This object can be cast to a numpy.array using `np.asarray` or `np.array`.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `data` | `Any` | Image data. Anything that can be cast to a numpy array. For pydantic simplicity, we mark this as Any, but in practice it should be numpy.typing.ArrayLike (which is anything that can be cast to a numpy array using `np.asarray`). |
| `device` | `str \| None` | Optional name of the SLM device to use. If not provided, the "default" SLM device should be used. (It is left to the backend to determine what device that is). By default, `None`. |
| `exposure` | `float \| None` | Exposure time for the SLM specifically (if different from the detector), in milliseconds. If not provided, the exposure on the owning MDAEvent should be used. By default, `None`. |

#### data

```python
data: Any = Field(..., repr=False)
```

#### device

```python
device: str | None = None
```

#### exposure

```python
exposure: float | None = Field(default=None, gt=0.0)
```

### AbsolutePosition

Bases: `PositionBase`, `FrozenModel`

An absolute position in 3D space.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `x` | `float \| None` | X position in microns. |
| `y` | `float \| None` | Y position in microns. |
| `z` | `float \| None` | Z position in microns. |
| `name` | `str \| None` | Optional name for the position. |
| `sequence` | `MDASequence \| None` | Optional MDASequence relative this position. |
| `properties` | `list[PropertyTuple] \| None` |  |
| `plate_row` | `int \| None` | Optional 0-based row index for well plate positions. |
| `plate_col` | `int \| None` | Optional 0-based column index for well plate positions. |
| `grid_row` | `int \| None` | Optional row index, when used in a grid. |
| `grid_col` | `int \| None` | Optional column index, when used in a grid. |

#### is\_relative

```python
is_relative: bool
```

### RelativePosition

Bases: `PositionBase`

A relative position in 3D space.

Relative positions also support `fov_width` and `fov_height` attributes, and can be used to define a single field of view for a "multi-point" plan.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `fov_width` | `float \| None` |  |
| `fov_height` | `float \| None` |  |
| `x` | `float` | X position in microns. |
| `y` | `float` | Y position in microns. |
| `z` | `float` | Z position in microns. |
| `name` | `str \| None` | Optional name for the position. |
| `sequence` | `MDASequence \| None` | Optional MDASequence relative this position. |
| `properties` | `list[PropertyTuple] \| None` |  |
| `plate_row` | `int \| None` | Optional 0-based row index for well plate positions. |
| `plate_col` | `int \| None` | Optional 0-based column index for well plate positions. |
| `grid_row` | `int \| None` | Optional row index, when used in a grid. |
| `grid_col` | `int \| None` | Optional column index, when used in a grid. |

#### x

```python
x: float = 0
```

#### y

```python
y: float = 0
```

#### z

```python
z: float = 0
```

#### num\_positions

```python
num_positions() -> int
```

## Attributes

### MultiPointPlan

```python
MultiPointPlan = AbsoluteMultiPointPlan | RelativeMultiPointPlan
```

### RelativeMultiPointPlan

```python
RelativeMultiPointPlan = (
    GridRowsColumns | GridWidthHeight | RandomPoints | RelativePosition
)
```

### AnyAutofocusPlan

```python
AnyAutofocusPlan = AxesBasedAF
```

### AnyTimePlan

```python
AnyTimePlan = MultiPhaseTimePlan | SinglePhaseTimePlan
```

### AnyZPlan

```python
AnyZPlan = (
    ZTopBottom
    | ZAboveBelow
    | ZRangeAround
    | ZAbsolutePositions
    | ZRelativePositions
)
```

### GridRelative

```python
GridRelative = GridRowsColumns
```
