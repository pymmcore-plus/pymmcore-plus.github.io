# Axes

The following objects may be used to describe iteration over specific types of dimensions: the stage positions, channels, time plans, z plans, grids and well plates of an [`MDASequence`](<https://pymmcore-plus.github.io/useq-schema/schema/sequence/index.md>). (Most of them may also be given as plain dicts, see [Building Sequences](<https://pymmcore-plus.github.io/useq-schema/guides/sequences/index.md>).)

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
| `config` | `str` | Name of the configuration to use for this channel, (e.g. `"488nm"`, `"DAPI"`, `"FITC"`). |
| `group` | `str` | Optional name of the group to which this channel belongs. By default, `"Channel"`. |
| `exposure` | `float \| None` | Exposure time in milliseconds. Must be positive. If not provided, implies use current exposure time. By default, `None`. |
| `do_stack` | `bool` | If `True`, instructs engine to include this channel in any Z stacks being acquired. By default, `True`. |
| `z_offset` | `float` | Relative Z offset from current position, in microns. By default, `0`. |
| `acquire_every` | `int` | Acquire every Nth frame (if acquiring a time series). By default, `1`. |
| `camera` | `str \| None` | Name of the camera to use for this channel. If not provided, implies use current camera. By default, `None`. |

## Time plans

Ways to describe a temporal acquisition sequence.

## useq.TIntervalDuration

Bases: `TimePlan`

Define temporal sequence using interval and duration.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `interval` | `timedelta` | Time between frames. Scalars are interpreted as seconds. Strings are parsed according to ISO 8601. |
| `duration` | `timedelta` | Total duration of sequence. |
| `prioritize_duration` | `bool` | If `True`, instructs engine to prioritize duration over number of frames in case of conflict. By default, `True`. |

## useq.TIntervalLoops

Bases: `TimePlan`

Define temporal sequence using interval and number of loops.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `interval` | `timedelta` | Time between frames. Scalars are interpreted as seconds. Strings are parsed according to ISO 8601. |
| `loops` | `int` | Number of frames. |
| `prioritize_duration` | `bool` | If `True`, instructs engine to prioritize duration over number of frames in case of conflict. By default, `False`. |

## useq.TDurationLoops

Bases: `TimePlan`

Define temporal sequence using duration and number of loops.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `duration` | `timedelta` | Total duration of sequence. Scalars are interpreted as seconds. Strings are parsed according to ISO 8601. |
| `loops` | `int` | Number of frames. |
| `prioritize_duration` | `bool` | If `True`, instructs engine to prioritize duration over number of frames in case of conflict. By default, `False`. |

## useq.MultiPhaseTimePlan

Bases: `TimePlan`

Time sequence composed of multiple phases.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `phases` | `Sequence[TIntervalDuration \| TIntervalLoops \| TDurationLoops]` | Sequence of time plans. |
| `prioritize_duration` | `bool` |  |

## Z plans

Ways to describe a z-stack acquisition sequence.

## useq.ZTopBottom

Bases: `ZPlan`

Define Z using absolute top &amp; bottom positions.

Note that `bottom` will always be visited, regardless of `go_up`, while `top` will always be *encompassed* by the range, but may not be precisely visited if the step size does not divide evenly into the range.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `top` | `float` | Top position in microns (inclusive). |
| `bottom` | `float` | Bottom position in microns (inclusive). |
| `step` | `float` | Step size in microns. |
| `go_up` | `bool` | If `True`, instructs engine to start at bottom and move towards top. By default, `True`. |

## useq.ZAboveBelow

Bases: `ZPlan`

Define Z as asymmetric range above and below some reference position.

Note that `below` will always be visited, regardless of `go_up`, while `above` will always be *encompassed* by the range, but may not be precisely visited if the step size does not divide evenly into the range.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `above` | `float` | Range above reference position in microns (inclusive). |
| `below` | `float` | Range below reference position in microns (inclusive). |
| `step` | `float` | Step size in microns. |
| `go_up` | `bool` | If `True`, instructs engine to start at bottom and move towards top. By default, `True`. |

## useq.ZAbsolutePositions

Bases: `ZPlan`

Define Z as a list of absolute positions.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `absolute` | `list[float]` | List of absolute z positions. |
| `go_up` | `bool` | If `True` (the default), visits points in the order provided, otherwise in reverse. |

## useq.ZRangeAround

Bases: `ZPlan`

Define Z as a symmetric range around some reference position.

Note that `-range / 2` will always be visited, regardless of `go_up`, while `+range / 2` will always be *encompassed* by the range, but may not be precisely visited if the step size does not divide evenly into the range.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `range` | `float` | Range in microns (inclusive). For example, a range of 4 with a step size of 1 would visit \[-2, -1, 0, 1, 2\]. |
| `step` | `float` | Step size in microns. |
| `go_up` | `bool` | If `True`, instructs engine to start at bottom and move towards top. By default, `True`. |

## useq.ZRelativePositions

Bases: `ZPlan`

Define Z as a list of positions relative to some reference.

Typically, the "reference" will be whatever the current Z position is at the start of the sequence.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `relative` | `list[float]` | List of relative z positions. |
| `go_up` | `bool` | If `True` (the default), visits points in the order provided, otherwise in reverse. |

## Grid plans

Ways to describe a grid acquisition sequence.

## useq.GridRowsColumns

Grid plan based on number of rows and columns.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `rows` | `int` | Number of rows. |
| `columns` | `int` | Number of columns. |
| `relative_to` | `RelativeTo` | Point in the grid to which the coordinates are relative. If "center", the grid is centered around the origin. If "top\_left", the grid is positioned such that the top left corner is at the origin. |
| `overlap` | `tuple[float, float]` | Overlap between grid positions in percent. If a single value is provided, it is used for both x and y. If a tuple is provided, the first value is used for x and the second for y. |
| `mode` | `OrderMode` | Define the ways of ordering the grid positions. Options are row\_wise, column\_wise, row\_wise\_snake, column\_wise\_snake and spiral. By default, row\_wise\_snake. |
| `fov_width` | `float \| None` | Width of the field of view in microns. If not provided, acquisition engines should use current width of the FOV based on the current objective and camera. Engines MAY override this even if provided. |
| `fov_height` | `float \| None` | Height of the field of view in microns. If not provided, acquisition engines should use current height of the FOV based on the current objective and camera. Engines MAY override this even if provided. |

## useq.GridWidthHeight

Grid plan based on total width and height.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `width` | `float` | Minimum total width of the grid, in microns. (may be larger based on fov\_width) |
| `height` | `float` | Minimum total height of the grid, in microns. (may be larger based on fov\_height) |
| `relative_to` | `RelativeTo` | Point in the grid to which the coordinates are relative. If "center", the grid is centered around the origin. If "top\_left", the grid is positioned such that the top left corner is at the origin. |
| `overlap` | `tuple[float, float]` | Overlap between grid positions in percent. If a single value is provided, it is used for both x and y. If a tuple is provided, the first value is used for x and the second for y. |
| `mode` | `OrderMode` | Define the ways of ordering the grid positions. Options are row\_wise, column\_wise, row\_wise\_snake, column\_wise\_snake and spiral. By default, row\_wise\_snake. |
| `fov_width` | `float \| None` | Width of the field of view in microns. If not provided, acquisition engines should use current width of the FOV based on the current objective and camera. Engines MAY override this even if provided. |
| `fov_height` | `float \| None` | Height of the field of view in microns. If not provided, acquisition engines should use current height of the FOV based on the current objective and camera. Engines MAY override this even if provided. |

## useq.GridFromEdges

Yield absolute stage positions to cover a bounded area.

The bounded area is defined by top, left, bottom and right edges in stage coordinates. The bounds define the *outer* edges of the images, including the field of view and overlap.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `top` | `float` | Top stage position of the bounding area |
| `left` | `float` | Left stage position of the bounding area |
| `bottom` | `float` | Bottom stage position of the bounding area |
| `right` | `float` | Right stage position of the bounding area |
| `overlap` | `tuple[float, float]` | Overlap between grid positions in percent. If a single value is provided, it is used for both x and y. If a tuple is provided, the first value is used for x and the second for y. |
| `mode` | `OrderMode` | Define the ways of ordering the grid positions. Options are row\_wise, column\_wise, row\_wise\_snake, column\_wise\_snake and spiral. By default, row\_wise\_snake. |
| `fov_width` | `float \| None` | Width of the field of view in microns. If not provided, acquisition engines should use current width of the FOV based on the current objective and camera. Engines MAY override this even if provided. |
| `fov_height` | `float \| None` | Height of the field of view in microns. If not provided, acquisition engines should use current height of the FOV based on the current objective and camera. Engines MAY override this even if provided. |

## useq.RandomPoints

Yield random points in a specified geometric shape.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `num_points` | `int` | Number of points to generate. |
| `max_width` | `float` | Maximum width of the bounding box in microns. |
| `max_height` | `float` | Maximum height of the bounding box in microns. |
| `shape` | `Shape` | Shape of the bounding box. Current options are "ellipse" and "rectangle". |
| `random_seed` | `int \| None` | Random numpy seed that should be used to generate the points. If None, a random seed will be used. |
| `allow_overlap` | `bool` | By default, True. If False and `fov_width` and `fov_height` are specified, points will not overlap and will be at least `fov_width` and `fov_height` apart. |
| `order` | `TraversalOrder \| None` | Order in which the points will be visited. If None, order is simply the order in which the points are generated (random). Use 'nearest\_neighbor' or 'two\_opt' to order the points in a more structured way. |
| `start_at` | `RelativePosition \| int` | Position or index of the point to start at. This is only used if `order` is 'nearest\_neighbor' or 'two\_opt'. If a position is provided, it will *always* be included in the list of points. If an index is provided, it must be less than the number of points, and corresponds to the index of the (randomly generated) points; this likely only makes sense when `random_seed` is provided. |
| `fov_width` | `float \| None` |  |
| `fov_height` | `float \| None` |  |

## useq.GridFromPolygon

Grid plan based on a polygon boundary.

This grid plan generates absolute stage positions that cover a polygon region. Additionally the convex hull, and/or a buffered polygon can be created to generate tiles over a larger area surrounding the initial polygon.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `vertices` | `list[tuple[float, float]]` | List of (x, y) points that define the polygon boundary. Must have at least 3 points. |
| `convex_hull` | `bool \| None` | If True, the convex hull of the polygon will be used. |
| `offset` | `float \| None` | Expand area bounded by vertices to include all points within a `offset` of the original boundary. A positive offset produces a dilation, a negative offset an erosion. |
| `overlap` | `tuple[float, float]` | Overlap between grid positions in percent. If a single value is provided, it is used for both x and y. If a tuple is provided, the first value is used for x and the second for y. |
| `mode` | `OrderMode` | Define the ways of ordering the grid positions. Options are row\_wise, column\_wise, row\_wise\_snake, column\_wise\_snake and spiral. By default, row\_wise\_snake. |
| `fov_width` | `float \| None` | Width of the field of view in microns. If not provided, acquisition engines should use current width of the FOV based on the current objective and camera. Engines MAY override this even if provided. |
| `fov_height` | `float \| None` | Height of the field of view in microns. If not provided, acquisition engines should use current height of the FOV based on the current objective and camera. Engines MAY override this even if provided. |

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

Order in which random points are visited.

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
| `plate` | `WellPlate` | The well-plate definition. Minimally including rows, columns, and well spacing. If expressed as a string, it is assumed to be a key in `useq.registered_well_plate_keys`. |
| `a1_center_xy` | `tuple[float, float]` | The stage coordinates in µm of the center of well A1 (top-left corner). |
| `rotation` | `float \| None` | The rotation angle in degrees (anti-clockwise) of the plate. If None, no rotation is applied. If expressed as a string, it is assumed to be an angle with units (e.g., "5°", "4 rad", "4.5deg"). If expressed as an arraylike, it is assumed to be a 2x2 rotation matrix `[[cos, -sin], [sin, cos]]`, or a 4-tuple `(cos, -sin, sin, cos)`. |
| `selected_wells` | `tuple[tuple[int, ...], tuple[int, ...]] \| None` | Any \<=2-dimensional index expression for selecting wells. for example: - None -\> No wells are selected. - slice(0) -\> (also) select no wells. - slice(None) -\> Selects all wells. - 0 -\> Selects the first row. - \[0, 1, 2\] -\> Selects the first three rows. - slice(1, 5) -\> selects wells from row 1 to row 4. - (2, slice(1, 4)) -\> select wells in the second row and only columns 1 to 3. - (\[1, 2\], \[3, 4\]) -\> select wells in (row, column): (1, 3) and (2, 4) |
| `well_points_plan` | `GridRowsColumns \| GridWidthHeight \| RandomPoints \| RelativePosition` | A plan for acquiring images within each well. This can be a single position (for a single image per well), a GridRowsColumns (for a grid of images), or RandomPoints (for random points within each well). |

## useq.WellPlate

Bases: `FrozenModel`

A multi-well plate definition.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `rows` | `int` | The number of rows in the plate. Must be \> 0. |
| `columns` | `int` | The number of columns in the plate. Must be \> 0. |
| `well_spacing` | `tuple[float, float]` | The center-to-center distance in mm (pitch) between wells in the x and y directions. If a single value is provided, it is used for both x and y. |
| `well_size` | `tuple[float, float]` | The size in mm of each well in the x and y directions. If the well is squared or rectangular, this is the width and height of the well. If the well is circular, this is the diameter. If a single value is provided, it is used for both x and y. |
| `circular_wells` | `bool` | Whether wells are circular (True) or squared/rectangular (False). |
| `name` | `str` | A name for the plate. |

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
