# GridPlanWidget

Screenshot generated from the [example below](<#example>).

## Example

examples/grid\_plan\_widget.py

```python
"""Example usage of the GridPlanWidget class.

GridPlanWidget edits a useq grid plan.  It doesn't use a CMMCorePlus.

Check also the 'position_table.py' and 'mda_widget.py' examples to see the
GridPlanWidget used in combination of other widgets.
"""

from qtpy.QtWidgets import QApplication

from pymmcore_widgets import GridPlanWidget

app = QApplication([])

grid_wdg = GridPlanWidget()
grid_wdg.valueChanged.connect(print)
grid_wdg.show()

app.exec()
```

## API

Bases: `QScrollArea`

Widget to edit a grid plan.

The value is a `useq.GridRowsColumns`, `useq.GridWidthHeight`, `useq.GridFromEdges` or `useq.GridFromPolygon`, depending on the mode selected in the widget.

### valueChanged

```python
valueChanged = Signal(object)
```

Emitted with the new grid plan when the widget changes.

### mode

```python
mode() -> Mode
```

Return the current mode, one of "number", "area", or "bounds".

### setMode

```python
setMode(mode: Mode | Literal['number', 'area', 'bounds', 'polygon']) -> None
```

Set the current mode, one of "number", "area", "bounds", or "polygon".

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `mode` | `Mode \| Literal['number', 'area', 'bounds', 'polygon']` | The mode to set. | *required* |

### value

```python
value() -> GridPlan
```

Return the current value of the widget as a grid plan.

Returns:

| Type | Description |
| --- | --- |
| `GridFromEdges \| GridRowsColumns \| GridWidthHeight` | The current grid plan value of the widget. |

### setValue

```python
setValue(value: GridPlan) -> None
```

Set the current value of the widget from a grid plan.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `GridFromEdges \| GridRowsColumns \| GridWidthHeight \| GridFromPolygon` | The grid plan to set. | *required* |

### setFovWidth

```python
setFovWidth(value: float) -> None
```

Set the current field of view width.

### setFovHeight

```python
setFovHeight(value: float) -> None
```

Set the current field of view height.

### fovWidth

```python
fovWidth() -> float | None
```

Return the current field of view width.

### fovHeight

```python
fovHeight() -> float | None
```

Return the current field of view height.
