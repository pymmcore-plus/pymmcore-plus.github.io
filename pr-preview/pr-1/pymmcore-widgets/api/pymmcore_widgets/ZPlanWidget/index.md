# ZPlanWidget

Screenshot generated from the [example below](<#example>).

## Example

examples/z\_plan\_widget.py

```python
"""Example usage of the ZPlanWidget class.

ZPlanWidget edits a useq z plan.  It doesn't use a CMMCorePlus.

Check also the 'mda_widget.py' example to see the ZPlanWidget
used in combination of other widgets.
"""

from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ZPlanWidget

app = QApplication([])

z_wdg = ZPlanWidget()
z_wdg.valueChanged.connect(print)
z_wdg.show()

app.exec()
```

## API

Bases: `QWidget`

Widget to edit a z plan (`useq.AnyZPlan`).

### valueChanged

```python
valueChanged = Signal(object)
```

Emitted with the new z plan (or `None`) when the widget changes.

### Mode

```python
Mode: Final[type[Mode]] = Mode
```

### setMode

```python
setMode(
    mode: Mode | Literal["top_bottom", "range_around", "above_below"],
) -> None
```

Set the current mode.

One of "top\_bottom", "range\_around", or "above\_below".

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `mode` | `Mode \| Literal['top_bottom', 'range_around', 'above_below'] \| None` | The mode to set. By default, None. If None, the mode is determined by the sender().data(), for internal usage. | *required* |

### mode

```python
mode() -> Mode
```

Return the current mode.

One of "top\_bottom", "range\_around", or "above\_below".

### setSuggestedStep

```python
setSuggestedStep(value: float | None) -> None
```

Set the suggested z step size and update the button text.

### suggestedStep

```python
suggestedStep() -> float | None
```

Return suggested z step size.

### useSuggestedStep

```python
useSuggestedStep() -> None
```

Apply the suggested z step size to the step field.

### value

```python
value() -> ZAboveBelow | ZRangeAround | ZTopBottom | None
```

Return the current value of the widget as a z plan (`useq.AnyZPlan`).

Returns:

| Type | Description |
| --- | --- |
| `ZAboveBelow \| ZRangeAround \| ZTopBottom \| None` | The current z plan of the widget (`None` if the step size is 0). |

### setValue

```python
setValue(value: ZAboveBelow | ZRangeAround | ZTopBottom) -> None
```

Set the current value of the widget from a z plan (`useq.AnyZPlan`).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `ZAboveBelow \| ZRangeAround \| ZTopBottom` | The z plan to set. | *required* |

### isGoUp

```python
isGoUp() -> bool
```

Return True if the acquisition direction is up (bottom to top).

### setGoUp

```python
setGoUp(up: bool) -> None
```

Set the acquisition direction.

### currentZRange

```python
currentZRange() -> float
```

Return the current Z range in microns.
