# MDASequenceWidget

Screenshot generated from the [example below](<#example>).

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
# without a core, the widget doesn't know your channels: tell it what to offer
wdg.channels.setChannelGroups({"Channel": ["DAPI", "FITC"]})
wdg.setValue(
    useq.MDASequence(
        channels=["DAPI", "FITC"],
        time_plan=useq.TIntervalLoops(interval=0.5, loops=11),
    )
)
wdg.valueChanged.connect(lambda: print(wdg.value()))
wdg.show()
app.exec()
```

## API

Bases: `QWidget`

A widget that provides a GUI to construct and edit a `useq.MDASequence`.

This widget requires no connection to a microscope or core instance. It strictly deals with loading and creating `useq-schema` `useq.MDASequence` objects.

### valueChanged

```python
valueChanged = Signal()
```

Emitted (with no arguments) when the sequence changes; read it with `value()`.

### channels

```python
channels: ChannelTable
```

### time\_plan

```python
time_plan: TimePlanWidget
```

### z\_plan

```python
z_plan: ZPlanWidget
```

### stage\_positions

```python
stage_positions: PositionTable
```

### grid\_plan

```python
grid_plan: GridPlanWidget
```

### value

```python
value() -> MDASequence
```

Return the current value of the widget as a `useq.MDASequence`.

Returns:

| Type | Description |
| --- | --- |
| `MDASequence` | The current `useq.MDASequence` value of the widget. |

### setValue

```python
setValue(value: MDASequence) -> None
```

Set the current value of the widget from a `useq.MDASequence`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `MDASequence` | The `useq.MDASequence` to set. | *required* |

### save

```python
save(file: str | Path | None = None) -> None
```

Save the current `useq.MDASequence` to a file.

### load

```python
load(file: str | Path | None = None) -> None
```

Load a `useq.MDASequence` from a file.
