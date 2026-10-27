# MDAWidget

Screenshot generated from the [example below](<#example>).

## Example

examples/mda\_widget.py

```python
"""MDAWidget is a widget for creating and running a useq.MDASequence.

It is fully connected to the CMMCorePlus object, and has a "run" button.
"""

from contextlib import suppress

import useq
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import MDAWidget

with suppress(ImportError):
    from rich import print

app = QApplication([])

CMMCorePlus.instance().loadSystemConfiguration()

wdg = MDAWidget()
# start from a sequence (or build one in the GUI)
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

Bases: `MDASequenceWidget`

Main MDA Widget connected to a `pymmcore_plus.CMMCorePlus` instance.

It provides a GUI to construct and run a `useq.MDASequence`. Unlike `useq_widgets.MDASequenceWidget`, this widget is connected to a `pymmcore_plus.CMMCorePlus` instance, enabling awareness and control of the current state of the microscope.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget, by default None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

### valueChanged

```python
valueChanged = Signal()
```

Emitted (with no arguments) when the sequence changes; read it with `value()`.

### time\_plan

```python
time_plan: TimePlanWidget
```

### channels

```python
channels: CoreConnectedChannelTable
```

### z\_plan

```python
z_plan: CoreConnectedZPlanWidget
```

### stage\_positions

```python
stage_positions: CoreConnectedPositionTable
```

### grid\_plan

```python
grid_plan: CoreConnectedGridPlanWidget
```

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

### value

```python
value() -> MDASequence
```

Return the current state of the widget as a `useq.MDASequence`.

Some fields are filled in from the current state of the core. For example, if there are no stage positions, the current stage position is used.

### setValue

```python
setValue(value: MDASequence) -> None
```

Set the state of the widget from a `useq.MDASequence`.

### get\_next\_available\_path

```python
get_next_available_path(requested_path: Path) -> Path
```

Get the next available path.

This method is called immediately before running an MDA to ensure that the file being saved does not overwrite an existing file. It is also called at the end of the experiment to update the save widget with the next available path.

It may be overridden to provide custom behavior, but it should always return a Path object to a non-existing file or folder.

The default behavior adds/increments a 3-digit counter at the end of the path (before the extension) if the path already exists.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `requested_path` | `Path` | The path we are requesting for use. | *required* |

### prepare\_mda

```python
prepare_mda() -> bool | str | Path | None
```

Prepare the MDA sequence experiment.

Returns:

| Type | Description |
| --- | --- |
| `bool` | False if MDA to be cancelled due to autofocus issue. |
| `str \| Path` | Preparation successful, save path to be used for saving and saving active |
| `None` | Preparation successful, saving deactivated |

### execute\_mda

```python
execute_mda(
    output: Path
    | str
    | SupportsFrameReady
    | Sequence[Path | str | SupportsFrameReady]
    | None,
) -> None
```

Execute the MDA experiment corresponding to the current value.

### run\_mda

```python
run_mda() -> None
```

Run the current sequence (what the "Run" button does).

Calls `prepare_mda`, then `execute_mda` unless preparation was cancelled.
