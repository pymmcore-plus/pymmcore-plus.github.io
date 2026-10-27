# PositionTable

Screenshot generated from the [example below](<#example>).

## Example

examples/position\_table.py

```python
"""Example usage of the PositionTable class.

PositionTable edits a list of `useq.Position`s.  It doesn't use a CMMCorePlus
(the table inside MDAWidget does, so that it can add the current stage position).

Check also the 'mda_widget.py' example to see the PositionTable
used in combination of other widgets.
"""

from qtpy.QtWidgets import QApplication

from pymmcore_widgets import PositionTable

app = QApplication([])

pos_wdg = PositionTable(rows=3)
pos_wdg.valueChanged.connect(lambda: print(pos_wdg.value()))
pos_wdg.resize(570, 200)
pos_wdg.show()

app.exec()
```

## API

Bases: `DataTableWidget`

Table to edit a list of stage positions (`useq.Position`).

### valueChanged

```python
valueChanged = Signal()
```

Emitted (with no arguments) when the table changes; read it with `value()`.

### COLUMNS

```python
COLUMNS: tuple[ColumnInfo, ...]
```

### NAME

```python
NAME = TextColumn(key='name', default=None, is_row_selector=True)
```

### X

```python
X = FloatColumn(
    key="x", header="X [µm]", default=0.0, maximum=MAX, minimum=-MAX
)
```

### Y

```python
Y = FloatColumn(
    key="y", header="Y [µm]", default=0.0, maximum=MAX, minimum=-MAX
)
```

### Z

```python
Z = FloatColumn(
    key="z", header="Z [µm]", default=0.0, maximum=MAX, minimum=-MAX
)
```

### AF

```python
AF = FloatColumn(key='af', header='AF', default=0.0, maximum=MAX, minimum=-MAX)
```

### SEQ

```python
SEQ = SubSeqColumn(key='sequence', header='Sub-Sequence', default=None)
```

### table

```python
table() -> DataTable
```

### toolBar

```python
toolBar() -> QToolBar
```

### value

```python
value(
    exclude_unchecked: bool = True, exclude_hidden_cols: bool = True
) -> Sequence[Position]
```

Return the current value of the table as a tuple of `useq.Position`.

Note that `exclude_hidden_cols` has the result of: - excluding the Z position in each of the Positions if `include_z.isChecked()` is False - excluding the AF offset in each of the Positions if `af_per_position.isChecked()` is False

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `exclude_unchecked` | `bool` | Exclude unchecked rows, by default True | `True` |
| `exclude_hidden_cols` | `bool` | Exclude hidden columns, by default True | `True` |

Returns:

| Type | Description |
| --- | --- |
| `tuple[Position, ...]` | A tuple of `useq.Position`. |

### setValue

```python
setValue(value: Sequence[Position]) -> None
```

Set the current value of the table from a Sequence of `useq.Position`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `Sequence[Position]` | A Sequence of `useq.Position`. | *required* |

### save

```python
save(file: str | Path | None = None) -> None
```

Save the current positions to a JSON file.

### load

```python
load(file: str | Path | None = None) -> None
```

Load positions from a JSON file and set the table value.

### setXYEnabled

```python
setXYEnabled(enabled: bool) -> None
```

Disable or enable X/Y columns for all rows (e.g. global absolute grid).
