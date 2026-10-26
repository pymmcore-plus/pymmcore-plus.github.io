# TimePlanWidget

Screenshot generated from the [example below](<#example>).

Bases: `DataTableWidget`

Table to edit a [useq.TimePlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#time-plans>).

Methods:

| Name | Description |
| --- | --- |
| `value` | Return the current value of the table as a [useq.TimePlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#time-plans>). |
| `setValue` | Set the current value of the table from a [useq.TimePlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#time-plans>). |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `PHASE` |  |  |
| `INTERVAL` |  |  |
| `DURATION` |  |  |
| `LOOPS` |  |  |

## PHASE

```python
PHASE = TextColumn(key='phase', default=None, is_row_selector=True)
```

## INTERVAL

```python
INTERVAL = TimeDeltaColumn(
    key="interval", default="1 s", minimum_unit="milliseconds"
)
```

## DURATION

```python
DURATION = TimeDeltaColumn(
    key="duration", default="0 s", minimum_unit="seconds"
)
```

## LOOPS

```python
LOOPS = IntColumn(key='loops', default=1, minimum=1)
```

## value

```python
value(
    exclude_unchecked: bool = True,
) -> MultiPhaseTimePlan | TIntervalLoops | TIntervalDuration
```

Return the current value of the table as a [useq.TimePlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#time-plans>).

Returns:

| Type | Description |
| --- | --- |
| `MultiPhaseTimePlan \| TIntervalLoops \| TIntervalDuration` | The current [useq.TimePlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#time-plans>) value of the table. |

## setValue

```python
setValue(value: Any) -> None
```

Set the current value of the table from a [useq.TimePlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#time-plans>).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `MultiPhaseTimePlan \| TIntervalLoops \| TDurationLoops \| TIntervalDuration \| None` | The [useq.TimePlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#time-plans>) to set. | *required* |

## Example

examples/time\_plan\_widget.py

```python
"""Example usage of the TimePlanWidget class.

Check also the 'mda_widget.py' example to see the TimePlanWidget
used in combination of other widgets.
"""

import useq
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import TimePlanWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

t_wdg = TimePlanWidget()
t_wdg.setValue(useq.TIntervalLoops(interval=3, loops=5))
t_wdg.show()

app.exec()
```
