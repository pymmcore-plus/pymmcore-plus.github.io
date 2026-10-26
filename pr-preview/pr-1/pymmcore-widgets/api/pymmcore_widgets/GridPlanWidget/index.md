# GridPlanWidget

Screenshot generated from the [example below](<#example>).

Bases: `QScrollArea`

Widget to edit a [`useq-schema` GridPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#grid-plans>).

Methods:

| Name | Description |
| --- | --- |
| `mode` | Return the current mode, one of "number", "area", or "bounds". |
| `setMode` | Set the current mode, one of "number", "area", "bounds", or "polygon". |
| `value` | Return the current value of the widget as a [`useq-schema` GridPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#grid-plans>). |
| `setValue` | Set the current value of the widget from a [`useq-schema` GridPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#grid-plans>). |
| `setFovWidth` | Set the current field of view width. |
| `setFovHeight` | Set the current field of view height. |
| `fovWidth` | Return the current field of view width. |
| `fovHeight` | Return the current field of view height. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `valueChanged` |  |  |
| `row_col_wdg` |  |  |
| `width_height_wdg` |  |  |
| `bounds_wdg` |  |  |
| `polygon_wdg` |  |  |
| `overlap` |  |  |
| `order` |  |  |
| `relative_to` |  |  |

## valueChanged

```python
valueChanged = Signal(object)
```

## row\_col\_wdg

```python
row_col_wdg = _RowsColsWidget()
```

## width\_height\_wdg

```python
width_height_wdg = _WidthHeightWidget()
```

## bounds\_wdg

```python
bounds_wdg = _BoundsWidget()
```

## polygon\_wdg

```python
polygon_wdg = _PolygonWidget()
```

## overlap

```python
overlap = self._bottom_stuff.overlap
```

## order

```python
order = self._bottom_stuff.order
```

## relative\_to

```python
relative_to = self._bottom_stuff.relative_to
```

## mode

```python
mode() -> Mode
```

Return the current mode, one of "number", "area", or "bounds".

## setMode

```python
setMode(mode: Mode | Literal['number', 'area', 'bounds', 'polygon']) -> None
```

Set the current mode, one of "number", "area", "bounds", or "polygon".

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `mode` | `Mode \| Literal['number', 'area', 'bounds', 'polygon']` | The mode to set. | *required* |

## value

```python
value() -> GridPlan
```

Return the current value of the widget as a [`useq-schema` GridPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#grid-plans>).

Returns:

| Type | Description |
| --- | --- |
| `GridFromEdges \| GridRowsColumns \| GridWidthHeight` | The current [GridPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#grid-plans>) value of the widget. |

## setValue

```python
setValue(value: GridPlan) -> None
```

Set the current value of the widget from a [`useq-schema` GridPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#grid-plans>).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `GridFromEdges \| GridRowsColumns \| GridWidthHeight \| GridFromPolygon` | The [`useq-schema` GridPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#grid-plans>) to set. | *required* |

## setFovWidth

```python
setFovWidth(value: float) -> None
```

Set the current field of view width.

## setFovHeight

```python
setFovHeight(value: float) -> None
```

Set the current field of view height.

## fovWidth

```python
fovWidth() -> float | None
```

Return the current field of view width.

## fovHeight

```python
fovHeight() -> float | None
```

Return the current field of view height.

## Example

examples/grid\_plan\_widget.py

```python
"""Example usage of the GridPlanWidget class.

Check also the 'position_table.py' and 'mda_widget.py' examples to see the
GridPlanWidget used in combination of other widgets.
"""

from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import GridPlanWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

grid_wdg = GridPlanWidget()
grid_wdg.valueChanged.connect(print)
grid_wdg.show()

app.exec()
```
