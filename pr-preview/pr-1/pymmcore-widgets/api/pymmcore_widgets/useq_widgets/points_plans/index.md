# pymmcore\_widgets.useq\_widgets.points\_plans

Widgets that create MultiPoint plans.

**Classes**

| Name | Description |
| --- | --- |
| `GridRowColumnWidget` | Widget to generate a grid of FOVs within a specified area. |
| `RandomPointWidget` | Widget to generate random points within a specified area. |
| `RelativePointPlanSelector` | Widget to select a relative multi-position point plan. |

## Classes

### GridRowColumnWidget

```python
GridRowColumnWidget(parent: QWidget | None = None)
```

Bases: `QWidget`

Widget to generate a grid of FOVs within a specified area.

#### valueChanged

```python
valueChanged = Signal(object)
```

#### overlap

```python
overlap: tuple[float, float]
```

Return the overlap along x and y.

#### fov\_size

```python
fov_size: tuple[float | None, float | None]
```

Return the FOV size in (width, height).

#### value

```python
value() -> GridRowsColumns
```

Return the values of the widgets.

#### setValue

```python
setValue(value: GridRowsColumns | Mapping) -> None
```

Set the values of the widgets.

#### reset

```python
reset() -> None
```

Reset value to 1x1, row-wise-snake, with 0 overlap.

### RelativePointPlanSelector

```python
RelativePointPlanSelector(parent: QWidget | None = None)
```

Bases: `QWidget`

Widget to select a relative multi-position point plan.

See also: PointsPlanWidget which combines this widget with a graphical representation of the points.

In useq, a RelativeMultiPointPlan is one of: - useq.RelativePosition - useq.RandomPoints - useq.GridRowsColumns - useq.GridWidthHeight \# not included in this widget

#### valueChanged

```python
valueChanged = Signal(object)
```

#### active\_plan\_type

```python
active_plan_type: type[RelativePointPlan]
```

#### value

```python
value() -> RelativeMultiPointPlan
```

#### setValue

```python
setValue(plan: RelativeMultiPointPlan) -> None
```

Set the value of the widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `plan` | `RelativePosition \| RandomPoints \| GridRowsColumns` | The point plan to set. | *required* |

### RandomPointWidget

```python
RandomPointWidget(parent: QWidget | None = None)
```

Bases: `QWidget`

Widget to generate random points within a specified area.

#### valueChanged

```python
valueChanged = Signal(object)
```

#### fov\_size

```python
fov_size: tuple[float | None, float | None]
```

Return the FOV size.

#### start\_at

```python
start_at: RelativePosition | int
```

Return the start\_at value.

#### value

```python
value() -> RandomPoints
```

Return the values of the widgets.

#### setValue

```python
setValue(value: RandomPoints | Mapping) -> None
```

Set the values of the widgets.

#### reset

```python
reset() -> None
```

Reset value to 1 point and 0 area.

## Re-exports

These can also be imported from this module, but each is documented under its shortest import path (linked below).

| Name | Description |
| --- | --- |
| `PointsPlanWidget` | Widget to select the FOVs per well of the plate. |
