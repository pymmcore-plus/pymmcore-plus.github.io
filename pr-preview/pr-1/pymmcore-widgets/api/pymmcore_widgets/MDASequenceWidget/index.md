# MDASequenceWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

A widget that provides a GUI to construct and edit a `useq.MDASequence`.

This widget requires no connection to a microscope or core instance. It strictly deals with loading and creating `useq-schema` `useq.MDASequence` objects.

Methods:

| Name | Description |
| --- | --- |
| `value` | Return the current value of the widget as a `useq.MDASequence`. |
| `setValue` | Set the current value of the widget from a `useq.MDASequence`. |
| `save` | Save the current `useq.MDASequence` to a file. |
| `load` | Load a `useq.MDASequence` from a file. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `valueChanged` |  |  |
| `tab_wdg` |  |  |
| `axis_order` |  |  |
| `keep_shutter_open` |  |  |
| `af_axis` |  |  |
| `channels` | `ChannelTable` |  |
| `time_plan` | `TimePlanWidget` |  |
| `z_plan` | `ZPlanWidget` |  |
| `stage_positions` | `PositionTable` |  |
| `grid_plan` | `GridPlanWidget` |  |

## valueChanged

```python
valueChanged = Signal()
```

## tab\_wdg

```python
tab_wdg = tab_widget or MDATabs(self)
```

## axis\_order

```python
axis_order = QComboBox()
```

## keep\_shutter\_open

```python
keep_shutter_open = KeepShutterOpen()
```

## af\_axis

```python
af_axis = AutofocusAxis()
```

## channels

```python
channels: ChannelTable
```

## time\_plan

```python
time_plan: TimePlanWidget
```

## z\_plan

```python
z_plan: ZPlanWidget
```

## stage\_positions

```python
stage_positions: PositionTable
```

## grid\_plan

```python
grid_plan: GridPlanWidget
```

## value

```python
value() -> MDASequence
```

Return the current value of the widget as a `useq.MDASequence`.

Returns:

| Type | Description |
| --- | --- |
| `MDASequence` | The current `useq.MDASequence` value of the widget. |

## setValue

```python
setValue(value: MDASequence) -> None
```

Set the current value of the widget from a `useq.MDASequence`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `MDASequence` | The `useq.MDASequence` to set. | *required* |

## save

```python
save(file: str | Path | None = None) -> None
```

Save the current `useq.MDASequence` to a file.

## load

```python
load(file: str | Path | None = None) -> None
```

Load a `useq.MDASequence` from a file.

## Example

examples/mda\_sequence\_widget.py

```python
"""MDASequenceWidget is a widget for creating a useq.MDASequence object.

It has no awareness of the CMMCorePlus object, and does not have a "run" button.
"""

import useq
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import MDASequenceWidget

app = QApplication([])

wdg = MDASequenceWidget()
wdg.channels.setChannelGroups({"Channel": ["DAPI", "FITC"]})
wdg.time_plan.setValue(useq.TIntervalLoops(interval=0.5, loops=11))
wdg.valueChanged.connect(lambda: print(wdg.value()))
wdg.show()
app.exec()
```
