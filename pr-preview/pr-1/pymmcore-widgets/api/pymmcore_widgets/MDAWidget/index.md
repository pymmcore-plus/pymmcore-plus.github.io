# MDAWidget

Screenshot generated from the [example below](<#example>).

Bases: `MDASequenceWidget`

Main MDA Widget connected to a `pymmcore_plus.CMMCorePlus` instance.

It provides a GUI to construct and run a `useq.MDASequence`. Unlike `useq_widgets.MDASequenceWidget`, this widget is connected to a `pymmcore_plus.CMMCorePlus` instance, enabling awareness and control of the current state of the microscope.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget, by default None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

Methods:

| Name | Description |
| --- | --- |
| `value` | Set the current state of the widget from a `useq.MDASequence`. |
| `setValue` | Get the current state of the widget as a `useq.MDASequence`. |
| `get_next_available_path` | Get the next available path. |
| `prepare_mda` | Prepare the MDA sequence experiment. |
| `execute_mda` | Execute the MDA experiment corresponding to the current value. |
| `run_mda` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `save_info` |  |  |
| `control_btns` |  |  |
| `channels` | `CoreConnectedChannelTable` |  |
| `z_plan` | `CoreConnectedZPlanWidget` |  |
| `stage_positions` | `CoreConnectedPositionTable` |  |
| `grid_plan` | `CoreConnectedGridPlanWidget` |  |

## save\_info

```python
save_info = SaveGroupBox(parent=self)
```

## control\_btns

```python
control_btns = _MDAControlButtons(self._mmc, self)
```

## channels

```python
channels: CoreConnectedChannelTable
```

## z\_plan

```python
z_plan: CoreConnectedZPlanWidget
```

## stage\_positions

```python
stage_positions: CoreConnectedPositionTable
```

## grid\_plan

```python
grid_plan: CoreConnectedGridPlanWidget
```

## value

```python
value() -> MDASequence
```

Set the current state of the widget from a `useq.MDASequence`.

## setValue

```python
setValue(value: MDASequence) -> None
```

Get the current state of the widget as a `useq.MDASequence`.

## get\_next\_available\_path

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

## prepare\_mda

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

## execute\_mda

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

## run\_mda

```python
run_mda() -> None
```

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
wdg.channels.setChannelGroups({"Channel": ["DAPI", "FITC"]})
wdg.time_plan.setValue(useq.TIntervalLoops(interval=0.5, loops=11))
wdg.valueChanged.connect(lambda: print(wdg.value()))
wdg.show()
app.exec()
```
