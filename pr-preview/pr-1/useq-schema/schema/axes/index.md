# Axes

The following objects may be used to describe iteration over specific types of dimensions.

## useq.Position

```python
Position = AbsolutePosition
```

## useq.Channel

Bases: `FrozenModel`

Define an acquisition channel.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `config` | `str` |  | *required* |
| `group` | `str` |  | `'Channel'` |
| `exposure` | `float \| None` |  | `None` |
| `do_stack` | `bool` |  | `True` |
| `z_offset` | `float` |  | `0.0` |
| `acquire_every` | `int` |  | `1` |
| `camera` | `str \| None` |  | `None` |

## Time Plans

Ways to describe a temporal acquisition sequence.

## useq.TIntervalDuration

Bases: `TimePlan`

Define temporal sequence using interval and duration.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prioritize_duration` | `bool` |  | `True` |
| `interval` | `timedelta` |  | *required* |
| `duration` | `timedelta` |  | *required* |

## useq.TIntervalLoops

Bases: `TimePlan`

Define temporal sequence using interval and number of loops.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prioritize_duration` | `bool` |  | `False` |
| `interval` | `timedelta` |  | *required* |
| `loops` | `int` |  | *required* |

## useq.TDurationLoops

Bases: `TimePlan`

Define temporal sequence using duration and number of loops.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prioritize_duration` | `bool` |  | `False` |
| `duration` | `timedelta` |  | *required* |
| `loops` | `int` |  | *required* |

## useq.MultiPhaseTimePlan

Bases: `TimePlan`

Time sequence composed of multiple phases.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prioritize_duration` | `bool` |  | `False` |
| `phases` | `Sequence[TIntervalDuration \| TIntervalLoops \| TDurationLoops]` |  | *required* |

## Z Plans

Ways to describe a z-stack acquisition sequence.

## useq.ZTopBottom

Bases: `ZPlan`

Define Z using absolute top &amp; bottom positions.

Note that `bottom` will always be visited, regardless of `go_up`, while `top` will always be *encompassed* by the range, but may not be precisely visited if the step size does not divide evenly into the range.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `go_up` | `bool` |  | `True` |
| `top` | `float` |  | *required* |
| `bottom` | `float` |  | *required* |
| `step` | `float` |  | *required* |

## useq.ZAboveBelow

Bases: `ZPlan`

Define Z as asymmetric range above and below some reference position.

Note that `below` will always be visited, regardless of `go_up`, while `above` will always be *encompassed* by the range, but may not be precisely visited if the step size does not divide evenly into the range.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `go_up` | `bool` |  | `True` |
| `above` | `float` |  | *required* |
| `below` | `float` |  | *required* |
| `step` | `float` |  | *required* |

## useq.ZAbsolutePositions

Bases: `ZPlan`

Define Z as a list of absolute positions.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `go_up` | `bool` |  | `True` |
| `absolute` | `list[float]` |  | *required* |

## useq.ZRangeAround

Bases: `ZPlan`

Define Z as a symmetric range around some reference position.

Note that `-range / 2` will always be visited, regardless of `go_up`, while `+range / 2` will always be *encompassed* by the range, but may not be precisely visited if the step size does not divide evenly into the range.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `go_up` | `bool` |  | `True` |
| `range` | `float` |  | *required* |
| `step` | `float` |  | *required* |

## useq.ZRelativePositions

Bases: `ZPlan`

Define Z as a list of positions relative to some reference.

Typically, the "reference" will be whatever the current Z position is at the start of the sequence.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `go_up` | `bool` |  | `True` |
| `relative` | `list[float]` |  | *required* |

## Grid Plans

Ways to describe a grid acquisition sequence.

## useq.GridRowsColumns

Bases: `_GridPlan[RelativePosition]`

Grid plan based on number of rows and columns.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `fov_width` | `float \| None` |  | `None` |
| `fov_height` | `float \| None` |  | `None` |
| `overlap` | `tuple[float, float]` |  | `(0.0, 0.0)` |
| `mode` | `OrderMode` |  | `<OrderMode.row_wise_snake: 'row_wise_snake'>` |
| `rows` | `int` |  | *required* |
| `columns` | `int` |  | *required* |
| `relative_to` | `RelativeTo` |  | `<RelativeTo.center: 'center'>` |

## useq.GridWidthHeight

Bases: `_GridPlan[RelativePosition]`

Grid plan based on total width and height.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `fov_width` | `float \| None` |  | `None` |
| `fov_height` | `float \| None` |  | `None` |
| `overlap` | `tuple[float, float]` |  | `(0.0, 0.0)` |
| `mode` | `OrderMode` |  | `<OrderMode.row_wise_snake: 'row_wise_snake'>` |
| `width` | `float` |  | *required* |
| `height` | `float` |  | *required* |
| `relative_to` | `RelativeTo` |  | `<RelativeTo.center: 'center'>` |

## useq.GridFromEdges

Bases: `_GridPlan[AbsolutePosition]`

Yield absolute stage positions to cover a bounded area.

The bounded area is defined by top, left, bottom and right edges in stage coordinates. The bounds define the *outer* edges of the images, including the field of view and overlap.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `fov_width` | `float \| None` |  | `None` |
| `fov_height` | `float \| None` |  | `None` |
| `overlap` | `tuple[float, float]` |  | `(0.0, 0.0)` |
| `mode` | `OrderMode` |  | `<OrderMode.row_wise_snake: 'row_wise_snake'>` |
| `top` | `float` |  | *required* |
| `left` | `float` |  | *required* |
| `bottom` | `float` |  | *required* |
| `right` | `float` |  | *required* |

## useq.RandomPoints

Bases: `_MultiPointPlan[RelativePosition]`

Yield random points in a specified geometric shape.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `fov_width` | `float \| None` |  | `None` |
| `fov_height` | `float \| None` |  | `None` |
| `num_points` | `int` |  | *required* |
| `max_width` | `float` |  | `1` |
| `max_height` | `float` |  | `1` |
| `shape` | `Shape` |  | `<Shape.ELLIPSE: 'ellipse'>` |
| `random_seed` | `int \| None` |  | `None` |
| `allow_overlap` | `bool` |  | `True` |
| `order` | `TraversalOrder \| None` |  | `<TraversalOrder.TWO_OPT: 'two_opt'>` |
| `start_at` | `RelativePosition \| int` |  | `0` |

## useq.GridFromPolygon

Bases: `_GridPlan[AbsolutePosition]`

Grid plan based on a polygon boundary.

This grid plan generates absolute stage positions that cover a polygon region. Additionally the convex hull, and/or a buffered polygon can be created to generate tiles over a larger area surrounding the initial polygon.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `fov_width` | `float \| None` |  | `None` |
| `fov_height` | `float \| None` |  | `None` |
| `overlap` | `tuple[float, float]` |  | `(0.0, 0.0)` |
| `mode` | `OrderMode` |  | `<OrderMode.row_wise_snake: 'row_wise_snake'>` |
| `vertices` | `list[tuple[float, float]]` | List of vertices that define the polygon, must have at least 3 vertices. | *required* |
| `convex_hull` | `bool \| None` | If True, the convex hull of the polygon will be used. | `False` |
| `offset` | `float \| None` | Offsets the polygon in all directions to improve tile coverage. | `None` |

### Grid options

## useq.OrderMode

Bases: `Enum`

Order in which grid positions will be iterated.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `row_wise` | `Literal['row_wise']` | Iterate row by row. |
| `column_wise` | `Literal['column_wise']` | Iterate column by column. |
| `row_wise_snake` | `Literal['row_wise_snake']` | Iterate row by row, but alternate the direction of the columns. |
| `column_wise_snake` | `Literal['column_wise_snake']` | Iterate column by column, but alternate the direction of the rows. |
| `spiral` | `Literal['spiral']` | Iterate in a spiral pattern, starting from the center. |

Methods:

| Name | Description |
| --- | --- |
| `generate_indices` | Generate indices for the given grid size. |

### row\_wise

```python
row_wise = 'row_wise'
```

### column\_wise

```python
column_wise = 'column_wise'
```

### row\_wise\_snake

```python
row_wise_snake = 'row_wise_snake'
```

### column\_wise\_snake

```python
column_wise_snake = 'column_wise_snake'
```

### spiral

```python
spiral = 'spiral'
```

### generate\_indices

```python
generate_indices(rows: int, columns: int) -> Iterator[tuple[int, int]]
```

Generate indices for the given grid size.

## useq.Shape

Bases: `Enum`

Shape of the bounding box for random points.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `ELLIPSE` | `Literal['ellipse']` | The bounding box is an ellipse. |
| `RECTANGLE` | `Literal['rectangle']` | The bounding box is a rectangle. |

### ELLIPSE

```python
ELLIPSE = 'ellipse'
```

### RECTANGLE

```python
RECTANGLE = 'rectangle'
```

## useq.TraversalOrder

Bases: `Enum`

Methods:

| Name | Description |
| --- | --- |
| `order_points` | Return the order of points based on the traversal order. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `NEAREST_NEIGHBOR` |  |  |
| `TWO_OPT` |  |  |
| `RANDOM` |  |  |

### NEAREST\_NEIGHBOR

```python
NEAREST_NEIGHBOR = 'nearest_neighbor'
```

### TWO\_OPT

```python
TWO_OPT = 'two_opt'
```

### RANDOM

```python
RANDOM = 'random'
```

### order\_points

```python
order_points(points: ndarray, start_at: int = 0) -> ndarray
```

Return the order of points based on the traversal order.

## Well plates

## useq.WellPlatePlan

Bases: `UseqModel`, `Sequence[Position]`

A plan for acquiring images from a multi-well plate.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `plate` | `WellPlate` |  | *required* |
| `a1_center_xy` | `tuple[float, float]` |  | *required* |
| `rotation` | `float \| None` |  | `None` |
| `selected_wells` | `tuple[tuple[int, ...], tuple[int, ...]] \| None` |  | `None` |
| `well_points_plan` | `GridRowsColumns \| GridWidthHeight \| RandomPoints \| RelativePosition` | A relative position in 3D space.<br><br>Relative positions also support `fov_width` and `fov_height` attributes, and can be used to define a single field of view for a "multi-point" plan. | `<dynamic>` |

## useq.WellPlate

Bases: `FrozenModel`

A multi-well plate definition.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `rows` | `int` |  | *required* |
| `columns` | `int` |  | *required* |
| `well_spacing` | `tuple[float, float]` |  | *required* |
| `well_size` | `tuple[float, float]` |  | *required* |
| `circular_wells` | `bool` |  | `True` |
| `name` | `str` |  | `''` |

## useq.register\_well\_plates

```python
register_well_plates(
    plates: Mapping[str, PlateOrKwargs], /, **kwargs: PlateOrKwargs
) -> None
```

```python
register_well_plates(
    plates: Iterable[tuple[str, PlateOrKwargs]], /, **kwargs: PlateOrKwargs
) -> None
```

```python
register_well_plates(**kwargs: PlateOrKwargs) -> None
```

```python
register_well_plates(
    plates: Mapping[str, PlateOrKwargs]
    | Iterable[tuple[str, PlateOrKwargs]] = (),
    /,
    **kwargs: PlateOrKwargs,
) -> None
```

Register well-plate definitions to allow lookup by key.

Added keys will override existing keys if they already exist.

Values may either be WellPlate instances, or dictionaries with the following keys: - rows: Required\[int\] - columns: Required\[int\] - well\_spacing: Required\[tuple\[float, float\]\] - well\_size: tuple\[float, float\] | None - circular\_wells: bool - name: str

Examples:

```pycon
>>> import useq
>>> useq.register_well_plates(
...     {
...         "custom-square-plate": {
...             "rows": 8, "columns": 8, "well_spacing": 9.3, "well_size": 7.1
...         },
...         "silly-plate": {"rows": 1, "columns": 1, "well_spacing": 100}
...     }
... )
```

## useq.registered\_well\_plate\_keys

```python
registered_well_plate_keys() -> set[str]
```

Return a set of all registered well-plate keys.

These keys may be used as an argument to `WellPlatePlan.plate` to select a plate definition.
