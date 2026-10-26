# pymmcore\_widgets.useq\_widgets.points\_plans

Widgets that create MultiPoint plans.

Classes:

| Name | Description |
| --- | --- |
| `GridRowColumnWidget` | Widget to generate a grid of FOVs within a specified area. |
| `RandomPointWidget` | Widget to generate random points within a specified area. |
| `RelativePointPlanSelector` | Widget to select a relative multi-position point plan. |

## GridRowColumnWidget

```python
GridRowColumnWidget(parent: QWidget | None = None)
```

Bases: `QWidget`

Widget to generate a grid of FOVs within a specified area.

Methods:

| Name | Description |
| --- | --- |
| `value` | Return the values of the widgets. |
| `setValue` | Set the values of the widgets. |
| `reset` | Reset value to 1x1, row-wise-snake, with 0 overlap. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `valueChanged` |  |  |
| `fov_width` | `float \| None` |  |
| `fov_height` | `float \| None` |  |
| `rows` |  |  |
| `columns` |  |  |
| `overlap_x` |  |  |
| `overlap_y` |  |  |
| `mode` |  |  |
| `overlap` | `tuple[float, float]` | Return the overlap along x and y. |
| `fov_size` | `tuple[float \| None, float \| None]` | Return the FOV size in (width, height). |

### valueChanged

```python
valueChanged = Signal(object)
```

### fov\_width

```python
fov_width: float | None = None
```

### fov\_height

```python
fov_height: float | None = None
```

### rows

```python
rows = QSpinBox()
```

### columns

```python
columns = QSpinBox()
```

### overlap\_x

```python
overlap_x = QDoubleSpinBox()
```

### overlap\_y

```python
overlap_y = QDoubleSpinBox()
```

### mode

```python
mode = QComboBox()
```

### overlap

```python
overlap: tuple[float, float]
```

Return the overlap along x and y.

### fov\_size

```python
fov_size: tuple[float | None, float | None]
```

Return the FOV size in (width, height).

### value

```python
value() -> GridRowsColumns
```

Return the values of the widgets.

### setValue

```python
setValue(value: GridRowsColumns | Mapping) -> None
```

Set the values of the widgets.

### reset

```python
reset() -> None
```

Reset value to 1x1, row-wise-snake, with 0 overlap.

## RandomPointWidget

```python
RandomPointWidget(parent: QWidget | None = None)
```

Bases: `QWidget`

Widget to generate random points within a specified area.

Methods:

| Name | Description |
| --- | --- |
| `value` | Return the values of the widgets. |
| `setValue` | Set the values of the widgets. |
| `reset` | Reset value to 1 point and 0 area. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `valueChanged` |  |  |
| `random_seed` | `int` |  |
| `max_width` |  |  |
| `max_height` |  |  |
| `num_points` |  |  |
| `order` |  |  |
| `allow_overlap` |  |  |
| `shape` |  |  |
| `form` |  |  |
| `fov_size` | `tuple[float \| None, float \| None]` | Return the FOV size. |
| `start_at` | `RelativePosition \| int` | Return the start\_at value. |

### valueChanged

```python
valueChanged = Signal(object)
```

### random\_seed

```python
random_seed: int = self._new_seed()
```

### max\_width

```python
max_width = QDoubleSpinBox()
```

### max\_height

```python
max_height = QDoubleSpinBox()
```

### num\_points

```python
num_points = QSpinBox()
```

### order

```python
order = QComboBox()
```

### allow\_overlap

```python
allow_overlap = QCheckBox()
```

### shape

```python
shape = QComboBox()
```

### form

```python
form = QFormLayout()
```

### fov\_size

```python
fov_size: tuple[float | None, float | None]
```

Return the FOV size.

### start\_at

```python
start_at: RelativePosition | int
```

Return the start\_at value.

### value

```python
value() -> RandomPoints
```

Return the values of the widgets.

### setValue

```python
setValue(value: RandomPoints | Mapping) -> None
```

Set the values of the widgets.

### reset

```python
reset() -> None
```

Reset value to 1 point and 0 area.

## RelativePointPlanSelector

```python
RelativePointPlanSelector(parent: QWidget | None = None)
```

Bases: `QWidget`

Widget to select a relative multi-position point plan.

See also: PointsPlanWidget which combines this widget with a graphical representation of the points.

In useq, a RelativeMultiPointPlan is one of: - useq.RelativePosition - useq.RandomPoints - useq.GridRowsColumns - useq.GridWidthHeight \# not included in this widget

Methods:

| Name | Description |
| --- | --- |
| `value` |  |
| `setValue` | Set the value of the widget. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `valueChanged` |  |  |
| `single_pos_wdg` |  |  |
| `random_points_wdg` |  |  |
| `grid_wdg` |  |  |
| `single_radio_btn` |  |  |
| `random_radio_btn` |  |  |
| `grid_radio_btn` |  |  |
| `fov_w` |  |  |
| `fov_h` |  |  |
| `fov_widgets` |  |  |
| `active_plan_type` | `type[RelativePointPlan]` |  |

### valueChanged

```python
valueChanged = Signal(object)
```

### single\_pos\_wdg

```python
single_pos_wdg = RelativePositionWidget()
```

### random\_points\_wdg

```python
random_points_wdg = RandomPointWidget()
```

### grid\_wdg

```python
grid_wdg = GridRowColumnWidget()
```

### single\_radio\_btn

```python
single_radio_btn = QRadioButton()
```

### random\_radio\_btn

```python
random_radio_btn = QRadioButton()
```

### grid\_radio\_btn

```python
grid_radio_btn = QRadioButton()
```

### fov\_w

```python
fov_w = _FovWidget()
```

### fov\_h

```python
fov_h = _FovWidget()
```

### fov\_widgets

```python
fov_widgets = QWidget()
```

### active\_plan\_type

```python
active_plan_type: type[RelativePointPlan]
```

### value

```python
value() -> RelativeMultiPointPlan
```

### setValue

```python
setValue(plan: RelativeMultiPointPlan) -> None
```

Set the value of the widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `plan` | `RelativePosition \| RandomPoints \| GridRowsColumns` | The point plan to set. | *required* |

## Re-exports

These names can be imported from this module, but are documented at their top-level location.

| Name | Description |
| --- | --- |
| `PointsPlanWidget` | Widget to select the FOVVs per well of the plate. |
