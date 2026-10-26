# useq.v2

New MDASequence API.

Classes:

| Name | Description |
| --- | --- |
| `AutoFocusTransform` | Insert hardware-autofocus events created by an `AutoFocusPlan`. |
| `AxisIterable` |  |
| `ChannelsPlan` |  |
| `EventBuilder` | Callable that builds an event from an AxesIndex. |
| `EventTransform` | Callable that can modify, drop, or insert events. |
| `GridFromEdges` | Yield absolute stage positions to cover a bounded area. |
| `GridFromPolygon` | Grid plan based on a polygon boundary. |
| `GridRowsColumns` | Grid plan based on number of rows and columns. |
| `GridWidthHeight` | Grid plan based on total width and height. |
| `KeepShutterOpenTransform` | Replicates the v1 `keep_shutter_open_across` behaviour. |
| `MDASequence` |  |
| `MultiAxisSequence` | Represents a multidimensional sequence. |
| `MultiPhaseTimePlan` | Time sequence composed of multiple phases. |
| `MultiPositionPlan` | Base class for all multi-position plans. |
| `Position` | Define a position in 3D space. |
| `RandomPoints` | Yield random points in a specified geometric shape. |
| `RelativeTo` | Where the coordinates of the grid are relative to. |
| `ResetEventTimerTransform` | Marks the first frame of each timepoint with `reset_event_timer=True`. |
| `SimpleValueAxis` | A basic axis implementation that yields values directly. |
| `StagePositions` |  |
| `TDurationLoops` | Define temporal sequence using duration and number of loops. |
| `TIntervalDuration` | Define temporal sequence using interval and duration. |
| `TIntervalLoops` | Define temporal sequence using interval and number of loops. |
| `TimePlan` |  |
| `ZAboveBelow` | Define Z as asymmetric range above and below some reference position. |
| `ZAbsolutePositions` | Define Z as a list of absolute positions. |
| `ZPlan` | Base class for Z-axis plans in v2 MDA sequences. |
| `ZRangeAround` | Define Z as a symmetric range around some reference position. |
| `ZRelativePositions` | Define Z as a list of positions relative to some reference. |
| `ZTopBottom` | Define Z using absolute top &amp; bottom positions. |

Functions:

| Name | Description |
| --- | --- |
| `RelativePosition` | Create a relative position. |
| `iterate_multi_dim_sequence` | Iterate over a MultiDimSequence. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `AbsolutePosition` |  |  |
| `AnyTimePlan` |  |  |
| `AnyZPlan` |  |  |
| `MultiPointPlan` |  |  |
| `RelativeMultiPointPlan` |  |  |
| `SinglePhaseTimePlan` |  |  |

## AbsolutePosition

```python
AbsolutePosition = Position
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

## MultiPointPlan

```python
MultiPointPlan = AbsoluteMultiPointPlan | RelativeMultiPointPlan
```

## RelativeMultiPointPlan

```python
RelativeMultiPointPlan = GridRowsColumns | GridWidthHeight | RandomPoints
```

## SinglePhaseTimePlan

```python
SinglePhaseTimePlan = TIntervalDuration | TIntervalLoops | TDurationLoops
```

## AutoFocusTransform

```python
AutoFocusTransform(af_plan: AxesBasedAF)
```

Bases: `EventTransform[MDAEvent]`

Insert hardware-autofocus events created by an `AutoFocusPlan`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `af_plan` | `AxesBasedAF` | The autofocus plan. An autofocus event is inserted whenever one of `af_plan.axes` changes between consecutive events. | *required* |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `priority` |  |  |

### priority

```python
priority = -1
```

## AxisIterable

Bases: `BaseModel`, `Generic[V]`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `str` | A string id representing the axis. | *required* |

Methods:

| Name | Description |
| --- | --- |
| `should_skip` | Return True if this axis wants to skip the combination. |
| `contribute_to_mda_event` | Contribute data to the event being built. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `axis_key` | `str` | A string id representing the axis. |

### axis\_key

```python
axis_key: str
```

A string id representing the axis.

### should\_skip

```python
should_skip(prefix: AxesIndex) -> bool
```

Return True if this axis wants to skip the combination.

Default implementation returns False.

### contribute\_to\_mda\_event

```python
contribute_to_mda_event(value: V, index: Mapping[str, int]) -> Kwargs
```

Contribute data to the event being built.

This method allows each axis to contribute its data to the final MDAEvent. The default implementation does nothing - subclasses should override to add their specific contributions.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `V` | The value provided by this axis, for this iteration. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `event_data` | `dict[str, Any]` | Data to be added to the MDAEvent, it is ultimately up to the EventBuilder to decide how to merge possibly conflicting contributions from different axes. |

## ChannelsPlan

Bases: `SimpleValueAxis[Channel]`, `FrozenModel`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `Literal[<Axis.CHANNEL: 'c'>]` | A string id representing the axis. | `<Axis.CHANNEL: 'c'>` |
| `values` | `list[Channel]` | Built-in mutable sequence.<br><br>If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified. | `<dynamic>` |

Methods:

| Name | Description |
| --- | --- |
| `contribute_to_mda_event` | Contribute channel information to the MDA event. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `axis_key` | `Literal[CHANNEL]` |  |

### axis\_key

```python
axis_key: Literal[CHANNEL] = Field(
    default=Axis.CHANNEL, frozen=True, init=False
)
```

### contribute\_to\_mda\_event

```python
contribute_to_mda_event(value: Channel, index: Mapping[str, int]) -> Kwargs
```

Contribute channel information to the MDA event.

## EventBuilder

Bases: `Protocol[EventTco]`

Callable that builds an event from an AxesIndex.

## EventTransform

Bases: `Protocol[EventT]`

Callable that can modify, drop, or insert events.

The transformer receives:

- **event** - the current (already built) event.
- **prev\_event** - the *previously transformed* event that was just yielded, or `None` if this is the first call.
- **make\_next\_event** - a zero-argument callable that lazily builds the *next* raw event (i.e. before any transformers). Only call it if you really need look-ahead so the pipeline stays lazy.

The transformer must return a list.

Return **one** event in the list for a 1-to-1 mapping, an empty list to drop the original event, or a list with multiple items to insert extras.

## GridFromEdges

Bases: `_GridPlan`

Yield absolute stage positions to cover a bounded area.

The bounded area is defined by top, left, bottom and right edges in stage coordinates. The bounds define the *outer* edges of the images, including the field of view and overlap.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `Literal[<Axis.GRID: 'g'>]` | A string id representing the axis. | `<Axis.GRID: 'g'>` |
| `fov_width` | `float \| None` |  | `None` |
| `fov_height` | `float \| None` |  | `None` |
| `overlap` | `tuple[float, float]` |  | `(0.0, 0.0)` |
| `mode` | `OrderMode` |  | `<OrderMode.row_wise_snake: 'row_wise_snake'>` |
| `top` | `float` |  | *required* |
| `left` | `float` |  | *required* |
| `bottom` | `float` |  | *required* |
| `right` | `float` |  | *required* |

Methods:

| Name | Description |
| --- | --- |
| `plot` | Plot the positions in the plan. |

### top

```python
top: float = Field(..., frozen=True)
```

### left

```python
left: float = Field(..., frozen=True)
```

### bottom

```python
bottom: float = Field(..., frozen=True)
```

### right

```python
right: float = Field(..., frozen=True)
```

### is\_relative

```python
is_relative: bool
```

### plot

```python
plot(*, show: bool = True) -> Axes
```

Plot the positions in the plan.

## GridFromPolygon

Bases: `_GridPlan`

Grid plan based on a polygon boundary.

This grid plan generates absolute stage positions that cover a polygon region. Additionally the convex hull, and/or a buffered polygon can be created to generate tiles over a larger area surrounding the initial polygon.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `Literal[<Axis.GRID: 'g'>]` | A string id representing the axis. | `<Axis.GRID: 'g'>` |
| `fov_width` | `float \| None` |  | `None` |
| `fov_height` | `float \| None` |  | `None` |
| `overlap` | `tuple[float, float]` |  | `(0.0, 0.0)` |
| `mode` | `OrderMode` |  | `<OrderMode.row_wise_snake: 'row_wise_snake'>` |
| `vertices` | `list[tuple[float, float]]` | List of vertices that define the polygon, must have at least 3 vertices. | *required* |
| `convex_hull` | `bool \| None` | If True, the convex hull of the polygon will be used. | `False` |
| `offset` | `float \| None` | Offsets the polygon in all directions to improve tile coverage. | `None` |

Methods:

| Name | Description |
| --- | --- |
| `validate_vertices` |  |
| `iter_grid_positions` | Iterate over all grid positions, given a field of view size. |
| `plot` | Plot the positions in the plan. |

### vertices

```python
vertices: Annotated[
    list[tuple[float, float]],
    Field(
        ...,
        min_length=3,
        description="List of vertices that define the polygon, must have at least 3 vertices.",
        frozen=True,
    ),
]
```

### convex\_hull

```python
convex_hull: Annotated[
    bool | None,
    Field(
        False,
        description="If True, the convex hull of the polygon will be used.",
    ),
] = False
```

### offset

```python
offset: Annotated[
    float | None,
    Field(
        None,
        frozen=True,
        description="Offsets the polygon in all directions to improve tile coverage.",
    ),
] = None
```

### is\_relative

```python
is_relative: bool
```

### poly

```python
poly: Polygon
```

Return the processed polygon vertices as a shapely Polygon.

### prepared\_poly

```python
prepared_poly: PreparedGeometry
```

Return the prepared polygon for faster intersection tests.

### validate\_vertices

```python
validate_vertices(
    value: list[tuple[float, float]],
) -> list[tuple[float, float]]
```

### iter\_grid\_positions

```python
iter_grid_positions(
    fov_width: float | None = None,
    fov_height: float | None = None,
    *,
    order: OrderMode | None = None,
) -> Iterator[Position]
```

Iterate over all grid positions, given a field of view size.

### plot

```python
plot(*, show: bool = True) -> Axes
```

Plot the positions in the plan.

## GridRowsColumns

Bases: `_GridPlan`

Grid plan based on number of rows and columns.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `Literal[<Axis.GRID: 'g'>]` | A string id representing the axis. | `<Axis.GRID: 'g'>` |
| `fov_width` | `float \| None` |  | `None` |
| `fov_height` | `float \| None` |  | `None` |
| `overlap` | `tuple[float, float]` |  | `(0.0, 0.0)` |
| `mode` | `OrderMode` |  | `<OrderMode.row_wise_snake: 'row_wise_snake'>` |
| `rows` | `int` |  | *required* |
| `columns` | `int` |  | *required* |
| `relative_to` | `RelativeTo` |  | `<RelativeTo.center: 'center'>` |

### rows

```python
rows: int = Field(..., frozen=True, ge=1)
```

### columns

```python
columns: int = Field(..., frozen=True, ge=1)
```

### relative\_to

```python
relative_to: RelativeTo = Field(default=RelativeTo.center, frozen=True)
```

## GridWidthHeight

Bases: `_GridPlan`

Grid plan based on total width and height.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `Literal[<Axis.GRID: 'g'>]` | A string id representing the axis. | `<Axis.GRID: 'g'>` |
| `fov_width` | `float \| None` |  | `None` |
| `fov_height` | `float \| None` |  | `None` |
| `overlap` | `tuple[float, float]` |  | `(0.0, 0.0)` |
| `mode` | `OrderMode` |  | `<OrderMode.row_wise_snake: 'row_wise_snake'>` |
| `width` | `float` |  | *required* |
| `height` | `float` |  | *required* |
| `relative_to` | `RelativeTo` |  | `<RelativeTo.center: 'center'>` |

### width

```python
width: float = Field(..., frozen=True, gt=0)
```

### height

```python
height: float = Field(..., frozen=True, gt=0)
```

### relative\_to

```python
relative_to: RelativeTo = Field(default=RelativeTo.center, frozen=True)
```

## KeepShutterOpenTransform

```python
KeepShutterOpenTransform(axes: tuple[str, ...])
```

Bases: `EventTransform[MDAEvent]`

Replicates the v1 `keep_shutter_open_across` behaviour.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axes` | `tuple[str, ...]` | Tuple of axis names (`"p"`, `"t"`, `"c"`, `"z"`, …) on which the shutter may stay open when only **they** change between consecutive events. | *required* |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `axes` |  |  |

### axes

```python
axes = axes
```

## MDASequence

```python
MDASequence(
    *,
    axis_order: tuple[str, ...] | str | None = ...,
    value: Any = ...,
    time_plan: AxisIterable[float] | list | dict | None = ...,
    z_plan: AxisIterable[Position] | None = ...,
    channels: AxisIterable[Channel] | list | None = ...,
    stage_positions: AxisIterable[Position] | list | None = ...,
    grid_plan: AxisIterable[Position] | None = ...,
    autofocus_plan: AnyAutofocusPlan | None = ...,
    keep_shutter_open_across: str | tuple[str, ...] = ...,
    metadata: dict[str, Any] = ...,
    event_builder: EventBuilder[MDAEvent] = ...,
    transforms: tuple[EventTransform[MDAEvent], ...] = ...,
)
```

```python
MDASequence(
    *,
    axes: tuple[AxisIterable, ...] = ...,
    axis_order: tuple[str, ...] | None = ...,
    value: Any = ...,
    autofocus_plan: AnyAutofocusPlan | None = ...,
    keep_shutter_open_across: tuple[str, ...] = ...,
    metadata: dict[str, Any] = ...,
    event_builder: EventBuilder[MDAEvent] = ...,
    transforms: tuple[EventTransform[MDAEvent], ...] = ...,
)
```

```python
MDASequence(**kwargs: Any)
```

Bases: `MultiAxisSequence[MDAEvent]`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axes` | `tuple[AxisIterable, ...]` |  | `()` |
| `axis_order` | `tuple[str, ...] \| None` |  | `None` |
| `value` | `Any` |  | `None` |
| `event_builder` | `EventBuilder[MDAEvent] \| None` | Builds MDAEvent objects from AxesIndex. | `<dynamic>` |
| `transforms` | `tuple[EventTransform[MDAEvent], ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |
| `autofocus_plan` | `AxesBasedAF \| None` |  | `None` |
| `keep_shutter_open_across` | `tuple[str, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |
| `metadata` | `dict[str, Any]` | dict() -\> new empty dictionary dict(mapping) -\> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -\> new dictionary initialized as if via: d = {} for k, v in iterable: d\[k\] = v dict(\*\*kwargs) -\> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) | `<class 'dict'>` |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `autofocus_plan` | `AnyAutofocusPlan \| None` |  |
| `keep_shutter_open_across` | `tuple[str, ...]` |  |
| `metadata` | `dict[str, Any]` |  |
| `event_builder` | `Annotated[EventBuilder[MDAEvent], ImportableObject()] \| None` |  |
| `transforms` | `tuple[Annotated[EventTransform[MDAEvent], ImportableObject()], ...]` |  |
| `shape` | `tuple[int, ...]` | Return the shape of this sequence. |
| `sizes` | `Mapping[str, int]` | Mapping of axis name to size of that axis. |
| `used_axes` | `tuple[str, ...]` | Return keys of the axes whose length is not 0. |
| `time_plan` | `AxisIterable[float] \| None` | Return the time plan. |
| `z_plan` | `AxisIterable[Position] \| None` | Return the z plan. |
| `channels` | `Sequence[Channel]` | Return the channels. |
| `stage_positions` | `Sequence[Position]` | Return the stage positions. |
| `grid_plan` | `AxisIterable[Position] \| None` | Return the grid plan. |

### autofocus\_plan

```python
autofocus_plan: AnyAutofocusPlan | None = None
```

### keep\_shutter\_open\_across

```python
keep_shutter_open_across: tuple[str, ...] = Field(default_factory=tuple)
```

### metadata

```python
metadata: dict[str, Any] = Field(default_factory=dict)
```

### event\_builder

```python
event_builder: Annotated[EventBuilder[MDAEvent], ImportableObject()] | None = (
    Field(default_factory=MDAEventBuilder, repr=False)
)
```

### transforms

```python
transforms: tuple[
    Annotated[EventTransform[MDAEvent], ImportableObject()], ...
] = Field(default_factory=_default_transforms, repr=False)
```

### shape

```python
shape: tuple[int, ...]
```

Return the shape of this sequence.

> [!NOTE]
>
> This doesn't account for jagged arrays, like channels that exclude z stacks or skip timepoints.

### sizes

```python
sizes: Mapping[str, int]
```

Mapping of axis name to size of that axis.

### used\_axes

```python
used_axes: tuple[str, ...]
```

Return keys of the axes whose length is not 0.

### time\_plan

```python
time_plan: AxisIterable[float] | None
```

Return the time plan.

### z\_plan

```python
z_plan: AxisIterable[Position] | None
```

Return the z plan.

### channels

```python
channels: Sequence[Channel]
```

Return the channels.

### stage\_positions

```python
stage_positions: Sequence[Position]
```

Return the stage positions.

### grid\_plan

```python
grid_plan: AxisIterable[Position] | None
```

Return the grid plan.

## MultiAxisSequence

Bases: `MutableModel`, `Generic[EventTco]`

Represents a multidimensional sequence.

At the top level the `value` field is ignored. When used as a nested override, `value` is the value for that branch and its axes are iterated using its own axis\_order if provided; otherwise, it inherits the parent's axis\_order.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axes` | `tuple[AxisIterable, ...]` |  | `()` |
| `axis_order` | `tuple[str, ...] \| None` |  | `None` |
| `value` | `Any` |  | `None` |
| `event_builder` | `EventBuilder[EventTco] \| None` |  | `None` |
| `transforms` | `tuple[EventTransform, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |

Methods:

| Name | Description |
| --- | --- |
| `is_finite` | Return `True` if the sequence is finite (all axes are Sized). |
| `iter_axes` | Iterate over the axes and yield combinations with context. |
| `iter_events` | Iterate over axes, build raw events, then apply transformers. |
| `compose_transforms` | Compose transforms from the context of nested sequences. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `axes` | `tuple[AxisIterable, ...]` |  |
| `axis_order` | `tuple[str, ...] \| None` |  |
| `value` | `Any` |  |
| `event_builder` | `Annotated[EventBuilder[EventTco], ImportableObject()] \| None` |  |
| `transforms` | `tuple[Annotated[EventTransform, ImportableObject()], ...]` |  |

### axes

```python
axes: tuple[AxisIterable, ...] = ()
```

### axis\_order

```python
axis_order: tuple[str, ...] | None = None
```

### value

```python
value: Any = None
```

### event\_builder

```python
event_builder: Annotated[EventBuilder[EventTco], ImportableObject()] | None = (
    Field(default=None, repr=False)
)
```

### transforms

```python
transforms: tuple[Annotated[EventTransform, ImportableObject()], ...] = Field(
    default_factory=tuple, repr=False
)
```

### is\_finite

```python
is_finite() -> bool
```

Return `True` if the sequence is finite (all axes are Sized).

### iter\_axes

```python
iter_axes(
    axis_order: tuple[str, ...] | None = None,
) -> Iterator[AxesIndexWithContext]
```

Iterate over the axes and yield combinations with context.

Yields:

| Type | Description |
| --- | --- |
| `AxesIndexWithContext` | A tuple of (AxesIndex, MultiAxisSequence) where AxesIndex is a dictionary mapping axis keys to tuples of (index, value, AxisIterable), and MultiAxisSequence is the context that generated this axes combination. For example, when iterating over an `AxisIterable` with a single axis "t", with values of \[0.1, .2\], the yielded tuples would be: - ({'t': (0, 0.1, )}, ) - ({'t': (1, 0.2, )}, ) |

### iter\_events

```python
iter_events(axis_order: tuple[str, ...] | None = None) -> Iterator[EventTco]
```

Iterate over axes, build raw events, then apply transformers.

### compose\_transforms

```python
compose_transforms(
    context: tuple[MultiAxisSequence, ...] = (),
) -> tuple[EventTransform, ...]
```

Compose transforms from the context of nested sequences.

The base implementation aggregates transforms from outer to inner sequences. Only a single instance of each transform type is kept, so if multiple sequences in the context have the same transform type, only one will be used, and innermost MultiAxisSequence's transform will take precedence.

## MultiPhaseTimePlan

Bases: `TimePlan`

Time sequence composed of multiple phases.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `str` | A string id representing the axis. | `<Axis.TIME: 't'>` |
| `prioritize_duration` | `bool` |  | `False` |
| `phases` | `list[TIntervalDuration \| TIntervalLoops \| TDurationLoops]` |  | *required* |

### phases

```python
phases: list[SinglePhaseTimePlan]
```

## MultiPositionPlan

Bases: `AxisIterable[Position]`

Base class for all multi-position plans.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `str` | A string id representing the axis. | *required* |
| `fov_width` | `float \| None` |  | `None` |
| `fov_height` | `float \| None` |  | `None` |

Methods:

| Name | Description |
| --- | --- |
| `contribute_to_mda_event` |  |
| `plot` | Plot the positions in the plan. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `fov_width` | `Annotated[float, Ge(0)] \| None` |  |
| `fov_height` | `Annotated[float, Ge(0)] \| None` |  |
| `is_relative` | `bool` |  |

### fov\_width

```python
fov_width: Annotated[float, Ge(0)] | None = None
```

### fov\_height

```python
fov_height: Annotated[float, Ge(0)] | None = None
```

### is\_relative

```python
is_relative: bool
```

### contribute\_to\_mda\_event

```python
contribute_to_mda_event(
    value: Position, index: Mapping[str, int]
) -> KwargsContribution
```

### plot

```python
plot(*, show: bool = True) -> Axes
```

Plot the positions in the plan.

## Position

Bases: `MutableModel`

Define a position in 3D space.

Any of the attributes can be `None` to indicate that the position is not defined. For engines implementing support for useq, a position of `None` implies "do not move" or "stay at current position" on that axis.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `x` | `float \| None` |  | `None` |
| `y` | `float \| None` |  | `None` |
| `z` | `float \| None` |  | `None` |
| `name` | `str \| None` |  | `None` |
| `is_relative` | `bool` |  | `False` |

### x

```python
x: float | None = None
```

### y

```python
y: float | None = None
```

### z

```python
z: float | None = None
```

### name

```python
name: str | None = None
```

### is\_relative

```python
is_relative: bool = False
```

## RandomPoints

Bases: `MultiPositionPlan`

Yield random points in a specified geometric shape.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `Literal[<Axis.GRID: 'g'>]` | A string id representing the axis. | `<Axis.GRID: 'g'>` |
| `fov_width` | `float \| None` |  | `None` |
| `fov_height` | `float \| None` |  | `None` |
| `num_points` | `int` |  | *required* |
| `max_width` | `float` |  | `1` |
| `max_height` | `float` |  | `1` |
| `shape` | `Shape` |  | `<Shape.ELLIPSE: 'ellipse'>` |
| `random_seed` | `int \| None` |  | `None` |
| `allow_overlap` | `bool` |  | `True` |
| `order` | `TraversalOrder \| None` |  | `<TraversalOrder.TWO_OPT: 'two_opt'>` |
| `start_at` | `Position \| int` |  | `0` |

Methods:

| Name | Description |
| --- | --- |
| `num_positions` |  |

### axis\_key

```python
axis_key: Literal[GRID] = Field(default=Axis.GRID, frozen=True, init=False)
```

### num\_points

```python
num_points: Annotated[int, Gt(0)]
```

### max\_width

```python
max_width: Annotated[float, Gt(0)] = 1
```

### max\_height

```python
max_height: Annotated[float, Gt(0)] = 1
```

### shape

```python
shape: Shape = Shape.ELLIPSE
```

### random\_seed

```python
random_seed: int | None = None
```

### allow\_overlap

```python
allow_overlap: bool = True
```

### order

```python
order: TraversalOrder | None = TraversalOrder.TWO_OPT
```

### start\_at

```python
start_at: Position | Annotated[int, Ge(0)] = 0
```

### num\_positions

```python
num_positions() -> int
```

## RelativeTo

Bases: `Enum`

Where the coordinates of the grid are relative to.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `center` | `Literal['center']` | Grid is centered around the origin. |
| `top_left` | `Literal['top_left']` | Grid is positioned such that the top left corner is at the origin. |

### center

```python
center = 'center'
```

### top\_left

```python
top_left = 'top_left'
```

## ResetEventTimerTransform

```python
ResetEventTimerTransform()
```

Bases: `EventTransform[MDAEvent]`

Marks the first frame of each timepoint with `reset_event_timer=True`.

## SimpleValueAxis

Bases: `AxisIterable[V]`

A basic axis implementation that yields values directly.

If a value needs to declare sub-axes, yield a nested MultiAxisSequence. The default should\_skip always returns False.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `str` | A string id representing the axis. | *required* |
| `values` | `list[V]` | Built-in mutable sequence.<br><br>If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified. | `<dynamic>` |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `values` | `list[V]` |  |

### values

```python
values: list[V] = Field(default_factory=list)
```

## StagePositions

Bases: `AxisIterable[Position]`, `FrozenModel`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `Literal[<Axis.POSITION: 'p'>]` | A string id representing the axis. | `<Axis.POSITION: 'p'>` |
| `values` | `list[Position \| MDASequence]` | Built-in mutable sequence.<br><br>If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified. | `<dynamic>` |

Methods:

| Name | Description |
| --- | --- |
| `contribute_to_mda_event` | Contribute channel information to the MDA event. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `axis_key` | `Literal[POSITION]` |  |
| `values` | `list[Position \| MDASequence]` |  |

### axis\_key

```python
axis_key: Literal[POSITION] = Field(
    default=Axis.POSITION, frozen=True, init=False
)
```

### values

```python
values: list[Position | MDASequence] = Field(default_factory=list)
```

### contribute\_to\_mda\_event

```python
contribute_to_mda_event(value: Position, index: Mapping[str, int]) -> Kwargs
```

Contribute channel information to the MDA event.

## TDurationLoops

Bases: `_SizedTimePlan`

Define temporal sequence using duration and number of loops.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `str` | A string id representing the axis. | `<Axis.TIME: 't'>` |
| `prioritize_duration` | `bool` |  | `False` |
| `loops` | `int` |  | *required* |
| `duration` | `timedelta` |  | *required* |

### duration

```python
duration: NonNegativeTimeDelta
```

### loops

```python
loops: int = Field(..., gt=0)
```

### interval

```python
interval: timedelta
```

## TIntervalDuration

Bases: `TimePlan`

Define temporal sequence using interval and duration.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `str` | A string id representing the axis. | `<Axis.TIME: 't'>` |
| `prioritize_duration` | `bool` |  | `True` |
| `interval` | `timedelta` |  | *required* |
| `duration` | `timedelta \| None` |  | `None` |

### interval

```python
interval: TimeDelta
```

### duration

```python
duration: NonNegativeTimeDelta | None = None
```

### prioritize\_duration

```python
prioritize_duration: bool = True
```

## TIntervalLoops

Bases: `_SizedTimePlan`

Define temporal sequence using interval and number of loops.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `str` | A string id representing the axis. | `<Axis.TIME: 't'>` |
| `prioritize_duration` | `bool` |  | `False` |
| `loops` | `int` |  | *required* |
| `interval` | `timedelta` |  | *required* |

### interval

```python
interval: TimeDelta
```

### loops

```python
loops: int = Field(..., gt=0)
```

### duration

```python
duration: timedelta
```

## TimePlan

Bases: `AxisIterable[float]`, `FrozenModel`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `str` | A string id representing the axis. | `<Axis.TIME: 't'>` |
| `prioritize_duration` | `bool` |  | `False` |

Methods:

| Name | Description |
| --- | --- |
| `contribute_to_mda_event` | Contribute time data to the event being built. |
| `num_timepoints` | Return the number of time points in this plan. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `axis_key` | `str` |  |
| `prioritize_duration` | `bool` |  |

### axis\_key

```python
axis_key: str = Field(default=Axis.TIME, frozen=True, init=False)
```

### prioritize\_duration

```python
prioritize_duration: bool = False
```

### contribute\_to\_mda\_event

```python
contribute_to_mda_event(value: float, index: Mapping[str, int]) -> Kwargs
```

Contribute time data to the event being built.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `float` | The time value for this iteration. | *required* |
| `index` | `Mapping[str, int]` | Current axis indices. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `dict` | Event data to be merged into the MDAEvent. |

### num\_timepoints

```python
num_timepoints() -> int
```

Return the number of time points in this plan.

This is deprecated and will be removed in a future version. Use `len()` instead.

## ZAboveBelow

Bases: `ZPlan`

Define Z as asymmetric range above and below some reference position.

Note that `below` will always be visited, regardless of `go_up`, while `above` will always be *encompassed* by the range, but may not be precisely visited if the step size does not divide evenly into the range.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `Literal[<Axis.Z: 'z'>]` | A string id representing the axis. | `<Axis.Z: 'z'>` |
| `above` | `float` |  | *required* |
| `below` | `float` |  | *required* |
| `step` | `float` |  | *required* |
| `go_up` | `bool` |  | `True` |

### above

```python
above: float
```

### below

```python
below: float
```

### step

```python
step: Annotated[float, Ge(0)]
```

### go\_up

```python
go_up: bool = True
```

## ZAbsolutePositions

Bases: `ZPlan`

Define Z as a list of absolute positions.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `Literal[<Axis.Z: 'z'>]` | A string id representing the axis. | `<Axis.Z: 'z'>` |
| `absolute` | `list[float]` |  | *required* |

### absolute

```python
absolute: list[float]
```

### is\_relative

```python
is_relative: bool
```

## ZPlan

Bases: `AxisIterable[Position]`, `FrozenModel`

Base class for Z-axis plans in v2 MDA sequences.

All Z plans inherit from MDAAxisIterable and can be used in the new v2 MDA sequence framework.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `Literal[<Axis.Z: 'z'>]` | A string id representing the axis. | `<Axis.Z: 'z'>` |

Methods:

| Name | Description |
| --- | --- |
| `contribute_to_mda_event` | Contribute Z position to the MDA event. |
| `num_positions` | Get the number of Z positions. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `axis_key` | `Literal[Z]` |  |
| `is_relative` | `bool` | Return True if Z positions are relative to current position. |

### axis\_key

```python
axis_key: Literal[Z] = Field(default=Axis.Z, frozen=True, init=False)
```

### is\_relative

```python
is_relative: bool
```

Return True if Z positions are relative to current position.

### contribute\_to\_mda\_event

```python
contribute_to_mda_event(
    value: Position, index: Mapping[str, int]
) -> KwargsContribution
```

Contribute Z position to the MDA event.

### num\_positions

```python
num_positions() -> int
```

Get the number of Z positions.

## ZRangeAround

Bases: `ZPlan`

Define Z as a symmetric range around some reference position.

Note that `-range / 2` will always be visited, regardless of `go_up`, while `+range / 2` will always be *encompassed* by the range, but may not be precisely visited if the step size does not divide evenly into the range.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `Literal[<Axis.Z: 'z'>]` | A string id representing the axis. | `<Axis.Z: 'z'>` |
| `range` | `float` |  | *required* |
| `step` | `float` |  | *required* |
| `go_up` | `bool` |  | `True` |

### range

```python
range: float
```

### step

```python
step: Annotated[float, Ge(0)]
```

### go\_up

```python
go_up: bool = True
```

## ZRelativePositions

Bases: `ZPlan`

Define Z as a list of positions relative to some reference.

Typically, the "reference" will be whatever the current Z position is at the start of the sequence.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `Literal[<Axis.Z: 'z'>]` | A string id representing the axis. | `<Axis.Z: 'z'>` |
| `relative` | `list[float]` |  | *required* |

### relative

```python
relative: list[float]
```

## ZTopBottom

Bases: `ZPlan`

Define Z using absolute top &amp; bottom positions.

Note that `bottom` will always be visited, regardless of `go_up`, while `top` will always be *encompassed* by the range, but may not be precisely visited if the step size does not divide evenly into the range.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axis_key` | `Literal[<Axis.Z: 'z'>]` | A string id representing the axis. | `<Axis.Z: 'z'>` |
| `top` | `float` |  | *required* |
| `bottom` | `float` |  | *required* |
| `step` | `float` |  | *required* |
| `go_up` | `bool` |  | `True` |

### top

```python
top: float
```

### bottom

```python
bottom: float
```

### step

```python
step: Annotated[float, Ge(0)]
```

### go\_up

```python
go_up: bool = True
```

### is\_relative

```python
is_relative: bool
```

## RelativePosition

```python
RelativePosition(**kwargs: Any) -> Position
```

Create a relative position.

## iterate\_multi\_dim\_sequence

```python
iterate_multi_dim_sequence(
    seq: MultiAxisSequence, axis_order: tuple[str, ...] | None = None
) -> Iterator[AxesIndexWithContext]
```

Iterate over a MultiDimSequence.

Orders the base axes (if an axis\_order is provided) and then iterates over all index combinations using iterate\_axes\_recursive. The parent's axis\_order is passed down to nested sequences.

Yields:

| Type | Description |
| --- | --- |
| `AxesIndexWithContext` | A tuple of (AxesIndex, MultiAxisSequence) where AxesIndex is a dictionary mapping axis keys to tuples of (index, value, axis), and MultiAxisSequence is the context that generated this axes combination. |

## Re-exports

These names can be imported from this module, but are documented at their top-level location.

| Name | Description |
| --- | --- |
| `AcquireImage` | `useq.Action` to acquire an image. |
| `Action` | Base class for a `useq.MDAEvent` action. |
| `AnyAutofocusPlan` |  |
| `AutoFocusPlan` | Base class for hardware autofocus plans. |
| `AxesBasedAF` | Autofocus plan that performs autofocus when any of the specified axes change. |
| `Axis` | Recognized useq-schema axis keys. |
| `Channel` | Define an acquisition channel. |
| `CustomAction` | `useq.Action` to perform a custom action. |
| `EventChannel` | Channel in a MDA event. |
| `HardwareAutofocus` | `useq.Action` to perform a hardware autofocus. |
| `MDAEvent` | Define a single event in a `MDASequence`. |
| `OrderMode` | Order in which grid positions will be iterated. |
| `PropertyTuple` | Three-tuple capturing a device, property, and value. |
| `SLMImage` | SLM Image in a MDA event. |
| `Shape` | Shape of the bounding box for random points. |
| `TraversalOrder` |  |
| `WellPlate` | A multi-well plate definition. |
| `WellPlatePlan` | A plan for acquiring images from a multi-well plate. |
| `register_well_plates` | Register well-plate definitions to allow lookup by key. |
| `registered_well_plate_keys` | Return a set of all registered well-plate keys. |
