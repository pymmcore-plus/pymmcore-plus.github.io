# ChannelTable

Screenshot generated from the [example below](<#example>).

## Example

examples/channel\_table.py

```python
"""Example usage of the ChannelTable class.

ChannelTable edits a list of `useq.Channel`s.  It doesn't use a CMMCorePlus, so
you tell it which channel groups and channels to offer.

Check also the 'mda_widget.py' example to see the ChannelTable
used in combination of other widgets.
"""

from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ChannelTable

app = QApplication([])

ch_table_wdg = ChannelTable(rows=1)
ch_table_wdg.setChannelGroups({"Channel": ["DAPI", "FITC"]})
ch_table_wdg.valueChanged.connect(lambda: print(ch_table_wdg.value()))
ch_table_wdg.resize(500, 200)
ch_table_wdg.show()

app.exec()
```

## API

Bases: `DataTableWidget`

Table to edit a list of channels (`useq.Channel`).

It doesn't use a core: call `setChannelGroups` to say which channel groups and presets to offer.

### valueChanged

```python
valueChanged = Signal()
```

Emitted (with no arguments) when the table changes; read it with `value()`.

### COLUMNS

```python
COLUMNS: tuple[ColumnInfo, ...]
```

### GROUP

```python
GROUP = TextColumn(key='group', default=DEFAULT_GROUP, hidden=True)
```

### CONFIG

```python
CONFIG = TextColumn(key='config', default=None, is_row_selector=True)
```

### EXPOSURE

```python
EXPOSURE = FloatColumn(
    key="exposure", header="Exposure [ms]", default=100.0, minimum=0.01
)
```

### ACQUIRE\_EVERY

```python
ACQUIRE_EVERY = IntColumn(key='acquire_every', default=1, minimum=1)
```

### DO\_STACK

```python
DO_STACK = BoolColumn(key='do_stack', default=True)
```

### Z\_OFFSET

```python
Z_OFFSET = FloatColumn(
    key="z_offset", default=0.0, minimum=-10000, maximum=10000
)
```

### table

```python
table() -> DataTable
```

### toolBar

```python
toolBar() -> QToolBar
```

### setChannelGroups

```python
setChannelGroups(groups: Mapping[str, Sequence[str]] | None) -> None
```

Set the channel groups that can be selected in the table.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `groups` | `Mapping[str, Sequence[str]]` | A mapping of group names to a sequence of config names. | *required* |

### channelGroups

```python
channelGroups() -> Mapping[str, Sequence[str]]
```

Return the current channel groups that can be selected in the table.

### value

```python
value(exclude_unchecked: bool = True) -> tuple[Channel, ...]
```

Return the current value of the table as a tuple of `useq.Channel`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `exclude_unchecked` | `bool` | Exclude unchecked rows, by default True | `True` |

Returns:

| Type | Description |
| --- | --- |
| `tuple[Channel, ...]` | A tuple of `useq.Channel`. |

### setValue

```python
setValue(value: Iterable[Channel]) -> None
```

Set the current value of the table from an Iterable of `useq.Channel`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `Iterable[Channel]` | An Iterable of `useq.Channel`. | *required* |
