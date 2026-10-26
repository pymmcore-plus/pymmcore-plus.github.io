# ZPlanWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

Widget to edit a [useq.ZPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#z-plans>).

Methods:

| Name | Description |
| --- | --- |
| `setMode` | Set the current mode. |
| `mode` | Return the current mode. |
| `setSuggestedStep` | Set the suggested z step size and update the button text. |
| `suggestedStep` | Return suggested z step size. |
| `useSuggestedStep` | Apply the suggested z step size to the step field. |
| `value` | Return the current value of the widget as a [useq.ZPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#z-plans>). |
| `setValue` | Set the current value of the widget from a [useq.ZPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#z-plans>). |
| `isGoUp` | Return True if the acquisition direction is up (bottom to top). |
| `setGoUp` | Set the acquisition direction. |
| `currentZRange` | Return the current Z range in microns. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `valueChanged` |  |  |
| `top` | `QDoubleSpinBox` |  |
| `bottom` | `QDoubleSpinBox` |  |
| `step` | `QDoubleSpinBox` |  |
| `steps` | `QSpinBox` |  |
| `range` | `QDoubleSpinBox` |  |
| `above` | `QDoubleSpinBox` |  |
| `below` | `QDoubleSpinBox` |  |
| `Mode` | `Final[type[Mode]]` |  |

## valueChanged

```python
valueChanged = Signal(object)
```

## top

```python
top: QDoubleSpinBox = QDoubleSpinBox()
```

## bottom

```python
bottom: QDoubleSpinBox = QDoubleSpinBox()
```

## step

```python
step: QDoubleSpinBox = QDoubleSpinBox()
```

## steps

```python
steps: QSpinBox = QSpinBox()
```

## range

```python
range: QDoubleSpinBox = QDoubleSpinBox()
```

## above

```python
above: QDoubleSpinBox = QDoubleSpinBox()
```

## below

```python
below: QDoubleSpinBox = QDoubleSpinBox()
```

## Mode

```python
Mode: Final[type[Mode]] = Mode
```

## setMode

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

## mode

```python
mode() -> Mode
```

Return the current mode.

One of "top\_bottom", "range\_around", or "above\_below".

## setSuggestedStep

```python
setSuggestedStep(value: float | None) -> None
```

Set the suggested z step size and update the button text.

## suggestedStep

```python
suggestedStep() -> float | None
```

Return suggested z step size.

## useSuggestedStep

```python
useSuggestedStep() -> None
```

Apply the suggested z step size to the step field.

## value

```python
value() -> ZAboveBelow | ZRangeAround | ZTopBottom | None
```

Return the current value of the widget as a [useq.ZPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#z-plans>).

Returns:

| Type | Description |
| --- | --- |
| `ZAboveBelow \| ZRangeAround \| ZTopBottom \| None` |  |
| `The current [useq.ZPlan](https://pymmcore-plus.github.io/useq-schema/schema/axes/#z-plans)` |  |
| `value of the widget.` |  |

## setValue

```python
setValue(value: ZAboveBelow | ZRangeAround | ZTopBottom) -> None
```

Set the current value of the widget from a [useq.ZPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#z-plans>).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `ZAboveBelow \| ZRangeAround \| ZTopBottom` | The [useq.ZPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#z-plans>) to set. | *required* |

## isGoUp

```python
isGoUp() -> bool
```

Return True if the acquisition direction is up (bottom to top).

## setGoUp

```python
setGoUp(up: bool) -> None
```

Set the acquisition direction.

## currentZRange

```python
currentZRange() -> float
```

Return the current Z range in microns.

## Example

examples/z\_plan\_widget.py

```python
"""Example usage of the ZPlanWidget class.

Check also the 'mda_widget.py' example to see the ZPlanWidget
used in combination of other widgets.
"""

from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ZPlanWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

z_wdg = ZPlanWidget()
z_wdg.show()

app.exec()
```
