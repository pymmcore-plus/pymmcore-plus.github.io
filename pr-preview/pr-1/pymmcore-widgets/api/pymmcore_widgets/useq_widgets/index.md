# pymmcore\_widgets.useq\_widgets

Widgets for the useq-schema data model.

Classes:

| Name | Description |
| --- | --- |
| `BoolColumn` | BoolColumn(key: 'str', data\_type: 'WdgGetSet' = WdgGetSet(widget=\<class 'pymmcore\_widgets.useq\_widgets.\_column\_info.\_CenteredCheckBox'\>, getter=, setter=, connect=\<function  at 0x11429cae0\>), header: 'str \| None' = None, is\_row\_selector: 'bool' = False, hidden: 'bool' = False, default: 'Any' = None, default\_factory: 'Callable\[\[\], Any\] \| None' = None) |
| `ChoiceColumn` | ChoiceColumn(key: 'str', data\_type: 'WdgGetSet\[CheckableCombo, str\]' = WdgGetSet(widget=\<class 'pymmcore\_widgets.useq\_widgets.\_column\_info.CheckableCombo'\>, getter=, setter=, connect=), header: 'str \| None' = None, is\_row\_selector: 'bool' = False, hidden: 'bool' = False, default: 'Any' = None, default\_factory: 'Callable\[\[\], Any\] \| None' = None, allowed\_values: 'tuple\[str, ...\] \| None' = None) |
| `DataTable` |  |
| `DataTableWidget` |  |
| `FloatColumn` | FloatColumn(key: 'str', data\_type: 'WdgGetSet' = WdgGetSet(widget=\<class 'pymmcore\_widgets.useq\_widgets.\_column\_info.TableDoubleSpinBox'\>, getter=, setter=, connect=\<function  at 0x1144667a0\>), header: 'str \| None' = None, is\_row\_selector: 'bool' = False, hidden: 'bool' = False, default: 'Any' = None, default\_factory: 'Callable\[\[\], Any\] \| None' = None, minimum: 'float' = 0, maximum: 'float' = 999999, decimals: 'int' = 2) |
| `IntColumn` | IntColumn(key: 'str', data\_type: 'WdgGetSet' = WdgGetSet(widget=\<class 'pymmcore\_widgets.useq\_widgets.\_column\_info.TableSpinBox'\>, getter=, setter=, connect=\<function  at 0x114466020\>), header: 'str \| None' = None, is\_row\_selector: 'bool' = False, hidden: 'bool' = False, default: 'Any' = None, default\_factory: 'Callable\[\[\], Any\] \| None' = None, minimum: 'int' = 0, maximum: 'int' = 999999999, decimals: 'int' = 2) |
| `PointsPlanWidget` | Widget to select the FOVVs per well of the plate. |
| `TextColumn` | Column that will use a standard QTableWidgetItem. |
| `TimeDeltaColumn` | TimeDeltaColumn(key: 'str', data\_type: 'WdgGetSet\[QTimeLineEdit, float\]' = WdgGetSet(widget=\<class 'pymmcore\_widgets.useq\_widgets.\_column\_info.QTimeLineEdit'\>, getter=, setter=, connect=\<function  at 0x114467920\>), header: 'str \| None' = None, is\_row\_selector: 'bool' = False, hidden: 'bool' = False, default: 'Any' = None, default\_factory: 'Callable\[\[\], Any\] \| None' = None, minimum\_unit: 'Unit' = 'seconds') |
| `WellPlateWidget` | Widget for selecting a well plate and a subset of wells. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `PYMMCW_METADATA_KEY` |  |  |

## PYMMCW\_METADATA\_KEY

```python
PYMMCW_METADATA_KEY = 'pymmcore_widgets'
```

## BoolColumn

```python
BoolColumn(
    key: str,
    data_type: WdgGetSet = TableBoolWidget,
    header: str | None = None,
    is_row_selector: bool = False,
    hidden: bool = False,
    default: Any = None,
    default_factory: Callable[[], Any] | None = None,
)
```

Bases: `WidgetColumn`

BoolColumn(key: 'str', data\_type: 'WdgGetSet' = WdgGetSet(widget=\<class 'pymmcore\_widgets.useq\_widgets.\_column\_info.\_CenteredCheckBox'\>, getter=, setter=, connect=\<function  at 0x11429cae0\>), header: 'str | None' = None, is\_row\_selector: 'bool' = False, hidden: 'bool' = False, default: 'Any' = None, default\_factory: 'Callable\[\[\], Any\] | None' = None)

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` |  | *required* |
| `data_type` | `WdgGetSet` |  | `WdgGetSet(widget=<class 'pymmcore_widgets.useq_widgets._column_info._CenteredCheckBox'>, getter=<function _CenteredCheckBox.isChecked at 0x114465a80>, setter=<function _CenteredCheckBox.setChecked at 0x114465f80>, connect=<function <lambda> at 0x11429cae0>)` |
| `header` | `str \| None` |  | `None` |
| `is_row_selector` | `bool` |  | `False` |
| `hidden` | `bool` |  | `False` |
| `default` | `Any` |  | `None` |
| `default_factory` | `Callable[[], Any] \| None` |  | `None` |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `data_type` | `WdgGetSet` |  |

### data\_type

```python
data_type: WdgGetSet = TableBoolWidget
```

## ChoiceColumn

```python
ChoiceColumn(
    key: str,
    data_type: WdgGetSet[CheckableCombo, str] = ChoiceWidget,
    header: str | None = None,
    is_row_selector: bool = False,
    hidden: bool = False,
    default: Any = None,
    default_factory: Callable[[], Any] | None = None,
    allowed_values: tuple[str, ...] | None = None,
)
```

Bases: `WidgetColumn`

ChoiceColumn(key: 'str', data\_type: 'WdgGetSet\[CheckableCombo, str\]' = WdgGetSet(widget=\<class 'pymmcore\_widgets.useq\_widgets.\_column\_info.CheckableCombo'\>, getter=, setter=, connect=), header: 'str | None' = None, is\_row\_selector: 'bool' = False, hidden: 'bool' = False, default: 'Any' = None, default\_factory: 'Callable\[\[\], Any\] | None' = None, allowed\_values: 'tuple\[str, ...\] | None' = None)

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` |  | *required* |
| `data_type` | `WdgGetSet[CheckableCombo, str]` |  | `WdgGetSet(widget=<class 'pymmcore_widgets.useq_widgets._column_info.CheckableCombo'>, getter=<function CheckableCombo.currentText at 0x1144904a0>, setter=<function CheckableCombo.setCurrentText at 0x114490ae0>, connect=<function CheckableCombo._connect at 0x114490e00>)` |
| `header` | `str \| None` |  | `None` |
| `is_row_selector` | `bool` |  | `False` |
| `hidden` | `bool` |  | `False` |
| `default` | `Any` |  | `None` |
| `default_factory` | `Callable[[], Any] \| None` |  | `None` |
| `allowed_values` | `tuple[str, ...] \| None` |  | `None` |

Methods:

| Name | Description |
| --- | --- |
| `isChecked` |  |
| `setCheckState` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `data_type` | `WdgGetSet[CheckableCombo, str]` |  |
| `allowed_values` | `tuple[str, ...] \| None` |  |

### data\_type

```python
data_type: WdgGetSet[CheckableCombo, str] = ChoiceWidget
```

### allowed\_values

```python
allowed_values: tuple[str, ...] | None = None
```

### isChecked

```python
isChecked(table: QTableWidget, row: int, col: int) -> bool
```

### setCheckState

```python
setCheckState(
    table: QTableWidget, row: int, col: int, state: CheckState
) -> None
```

## DataTable

```python
DataTable(rows: int = 0, parent: QWidget | None = None)
```

Bases: `QTableWidget`

Methods:

| Name | Description |
| --- | --- |
| `columnInfo` |  |
| `addColumns` |  |
| `addColumn` | Add a new column to the table. |
| `indexOf` |  |
| `iterRecords` | Return an iterator over the data in the table in records format. |
| `setValue` | Set the value of the table. |
| `checkAllRows` |  |
| `clearChecks` |  |
| `rowData` |  |
| `setRowData` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `valueChanged` |  |  |
| `COLUMNS` | `tuple[ColumnInfo, ...]` |  |

### valueChanged

```python
valueChanged = Signal()
```

### COLUMNS

```python
COLUMNS: tuple[ColumnInfo, ...] = ()
```

### columnInfo

```python
columnInfo(col: int) -> ColumnInfo | None
```

### addColumns

```python
addColumns(column_info: Iterable[ColumnInfo]) -> None
```

### addColumn

```python
addColumn(column_info: ColumnInfo, position: int | None = None) -> None
```

Add a new column to the table.

The ColumnInfo object is stored in the header item's data and used to populate the new column, and new rows that are added later, based on the data type and other info in the ColumnInfo object.

### indexOf

```python
indexOf(header: str | ColumnInfo) -> int
```

### iterRecords

```python
iterRecords(
    exclude_unchecked: bool = False, exclude_hidden_cols: bool = False
) -> Iterator[Record]
```

Return an iterator over the data in the table in records format.

(Records are a list of dicts mapping {'column header' -\> value} for each row.)

### setValue

```python
setValue(records: Iterable[Record]) -> None
```

Set the value of the table.

### checkAllRows

```python
checkAllRows() -> None
```

### clearChecks

```python
clearChecks() -> None
```

### rowData

```python
rowData(row: int, exclude_hidden_cols: bool = False) -> Record
```

### setRowData

```python
setRowData(row: int, data: Record) -> None
```

## DataTableWidget

```python
DataTableWidget(rows: int = 0, parent: QWidget | None = None)
```

Bases: `QWidget`

Methods:

| Name | Description |
| --- | --- |
| `table` |  |
| `toolBar` |  |
| `value` | Return a list of dicts of the data in the table. |
| `setValue` | Set the value of the table. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `valueChanged` |  |  |
| `COLUMNS` | `tuple[ColumnInfo, ...]` |  |
| `act_add_row` |  |  |
| `act_check_all` |  |  |
| `act_check_none` |  |  |
| `act_remove_row` |  |  |
| `act_clear` |  |  |

### valueChanged

```python
valueChanged = Signal()
```

### COLUMNS

```python
COLUMNS: tuple[ColumnInfo, ...]
```

### act\_add\_row

```python
act_add_row = QAction(
    QIconifyIcon("mdi:plus-thick", color=green), "Add new row", self
)
```

### act\_check\_all

```python
act_check_all = QAction(
    QIconifyIcon("mdi:checkbox-multiple-marked-outline", color=gray),
    "Select all rows",
    self,
)
```

### act\_check\_none

```python
act_check_none = QAction(
    QIconifyIcon("mdi:checkbox-multiple-blank-outline", color=gray),
    "Clear selection",
    self,
)
```

### act\_remove\_row

```python
act_remove_row = QAction(
    QIconifyIcon("mdi:close-box-outline", color=red),
    "Remove selected row",
    self,
)
```

### act\_clear

```python
act_clear = QAction(
    QIconifyIcon("mdi:close-box-multiple-outline", color=red),
    "Remove all rows",
    self,
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

### value

```python
value(exclude_unchecked: bool = True) -> Any
```

Return a list of dicts of the data in the table.

### setValue

```python
setValue(value: Iterable[Any]) -> None
```

Set the value of the table.

## FloatColumn

```python
FloatColumn(
    key: str,
    data_type: WdgGetSet = TableFloatWidget,
    header: str | None = None,
    is_row_selector: bool = False,
    hidden: bool = False,
    default: Any = None,
    default_factory: Callable[[], Any] | None = None,
    minimum: float = 0,
    maximum: float = 999999,
    decimals: int = 2,
)
```

Bases: `_RangeColumn`

FloatColumn(key: 'str', data\_type: 'WdgGetSet' = WdgGetSet(widget=\<class 'pymmcore\_widgets.useq\_widgets.\_column\_info.TableDoubleSpinBox'\>, getter=, setter=, connect=\<function  at 0x1144667a0\>), header: 'str | None' = None, is\_row\_selector: 'bool' = False, hidden: 'bool' = False, default: 'Any' = None, default\_factory: 'Callable\[\[\], Any\] | None' = None, minimum: 'float' = 0, maximum: 'float' = 999999, decimals: 'int' = 2)

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` |  | *required* |
| `data_type` | `WdgGetSet` |  | `WdgGetSet(widget=<class 'pymmcore_widgets.useq_widgets._column_info.TableDoubleSpinBox'>, getter=<built-in method value of PyQt6.sip.wrappertype object at 0x7eda24810>, setter=<built-in method setValue of PyQt6.sip.wrappertype object at 0x7eda24810>, connect=<function <lambda> at 0x1144667a0>)` |
| `header` | `str \| None` |  | `None` |
| `is_row_selector` | `bool` |  | `False` |
| `hidden` | `bool` |  | `False` |
| `default` | `Any` |  | `None` |
| `default_factory` | `Callable[[], Any] \| None` |  | `None` |
| `minimum` | `float` |  | `0` |
| `maximum` | `float` |  | `999999` |
| `decimals` | `int` |  | `2` |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `data_type` | `WdgGetSet` |  |

### data\_type

```python
data_type: WdgGetSet = TableFloatWidget
```

## IntColumn

```python
IntColumn(
    key: str,
    data_type: WdgGetSet = TableIntWidget,
    header: str | None = None,
    is_row_selector: bool = False,
    hidden: bool = False,
    default: Any = None,
    default_factory: Callable[[], Any] | None = None,
    minimum: int = 0,
    maximum: int = 999999999,
    decimals: int = 2,
)
```

Bases: `_RangeColumn`

IntColumn(key: 'str', data\_type: 'WdgGetSet' = WdgGetSet(widget=\<class 'pymmcore\_widgets.useq\_widgets.\_column\_info.TableSpinBox'\>, getter=, setter=, connect=\<function  at 0x114466020\>), header: 'str | None' = None, is\_row\_selector: 'bool' = False, hidden: 'bool' = False, default: 'Any' = None, default\_factory: 'Callable\[\[\], Any\] | None' = None, minimum: 'int' = 0, maximum: 'int' = 999999999, decimals: 'int' = 2)

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` |  | *required* |
| `data_type` | `WdgGetSet` |  | `WdgGetSet(widget=<class 'pymmcore_widgets.useq_widgets._column_info.TableSpinBox'>, getter=<built-in method value of PyQt6.sip.wrappertype object at 0x7eda24410>, setter=<built-in method setValue of PyQt6.sip.wrappertype object at 0x7eda24410>, connect=<function <lambda> at 0x114466020>)` |
| `header` | `str \| None` |  | `None` |
| `is_row_selector` | `bool` |  | `False` |
| `hidden` | `bool` |  | `False` |
| `default` | `Any` |  | `None` |
| `default_factory` | `Callable[[], Any] \| None` |  | `None` |
| `minimum` | `int` |  | `0` |
| `maximum` | `int` |  | `999999999` |
| `decimals` | `int` |  | `2` |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `data_type` | `WdgGetSet` |  |
| `minimum` | `int` |  |
| `maximum` | `int` |  |

### data\_type

```python
data_type: WdgGetSet = TableIntWidget
```

### minimum

```python
minimum: int = 0
```

### maximum

```python
maximum: int = 999999999
```

## PointsPlanWidget

```python
PointsPlanWidget(
    plan: RelativeMultiPointPlan | None = None, parent: QWidget | None = None
)
```

Bases: `QWidget`

Widget to select the FOVVs per well of the plate.

This widget allows the user to select the number of FOVs per well, (or to generally show a multi-point plan, such as a grid or random points plan, even if not within the context of a well plate.)

The value() method returns the selected plan, one of: - useq.GridRowsColumns - useq.RandomPoints - useq.RelativePosition

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `plan` | `RelativeMultiPointPlan \| None` | The useq MultiPoint plan to display and edit. | `None` |
| `parent` | `QWidget \| None` | The parent widget. | `None` |

Methods:

| Name | Description |
| --- | --- |
| `value` | Return the selected plan. |
| `setValue` | Set the current plan. |
| `setWellSize` | Set the well size width and/or height in mm. |
| `setWellShape` | Set the shape of the well. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `valueChanged` |  |  |
| `single_pos_wdg` |  |  |
| `random_points_wdg` |  |  |
| `grid_wdg` |  |  |

### valueChanged

```python
valueChanged = Signal(object)
```

### single\_pos\_wdg

```python
single_pos_wdg = self._selector.single_pos_wdg
```

### random\_points\_wdg

```python
random_points_wdg = self._selector.random_points_wdg
```

### grid\_wdg

```python
grid_wdg = self._selector.grid_wdg
```

### value

```python
value() -> RelativeMultiPointPlan
```

Return the selected plan.

### setValue

```python
setValue(plan: RelativeMultiPointPlan) -> None
```

Set the current plan.

### setWellSize

```python
setWellSize(width: float | None = None, height: float | None = None) -> None
```

Set the well size width and/or height in mm.

### setWellShape

```python
setWellShape(shape: Shape | str) -> None
```

Set the shape of the well.

Can be a `useq.Shape` enum or the strings "circle", "ellipse", "square", or "rectangle".

## TextColumn

```python
TextColumn(
    key: str,
    data_type: type = str,
    header: str | None = None,
    is_row_selector: bool = False,
    hidden: bool = False,
    default: str | None = None,
    default_factory: Callable[[], Any] | None = None,
    checkable: bool = False,
    checked: bool = True,
)
```

Bases: `ColumnInfo`

Column that will use a standard QTableWidgetItem.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` |  | *required* |
| `data_type` | `type` |  | `<class 'str'>` |
| `header` | `str \| None` |  | `None` |
| `is_row_selector` | `bool` |  | `False` |
| `hidden` | `bool` |  | `False` |
| `default` | `str \| None` |  | `None` |
| `default_factory` | `Callable[[], Any] \| None` |  | `None` |
| `checkable` | `bool` |  | `False` |
| `checked` | `bool` |  | `True` |

Methods:

| Name | Description |
| --- | --- |
| `init_cell` |  |
| `get_cell_data` |  |
| `set_cell_data` |  |
| `isChecked` |  |
| `setCheckState` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `key` | `str` |  |
| `data_type` | `type` |  |
| `header` | `str \| None` |  |
| `is_row_selector` | `bool` |  |
| `hidden` | `bool` |  |
| `default` | `str \| None` |  |
| `checkable` | `bool` |  |
| `checked` | `bool` |  |

### key

```python
key: str
```

### data\_type

```python
data_type: type = str
```

### header

```python
header: str | None = None
```

### is\_row\_selector

```python
is_row_selector: bool = False
```

### hidden

```python
hidden: bool = False
```

### default

```python
default: str | None = None
```

### checkable

```python
checkable: bool = False
```

### checked

```python
checked: bool = True
```

### init\_cell

```python
init_cell(
    table: QTableWidget, row: int, col: int, change_signal: SignalInstance
) -> None
```

### get\_cell\_data

```python
get_cell_data(table: QTableWidget, row: int, col: int) -> dict[str, Any]
```

### set\_cell\_data

```python
set_cell_data(table: QTableWidget, row: int, col: int, value: Any) -> None
```

### isChecked

```python
isChecked(table: QTableWidget, row: int, col: int) -> bool
```

### setCheckState

```python
setCheckState(
    table: QTableWidget, row: int, col: int, state: CheckState
) -> None
```

## TimeDeltaColumn

```python
TimeDeltaColumn(
    key: str,
    data_type: WdgGetSet[QTimeLineEdit, float] = TableTimeWidget,
    header: str | None = None,
    is_row_selector: bool = False,
    hidden: bool = False,
    default: Any = None,
    default_factory: Callable[[], Any] | None = None,
    minimum_unit: Unit = "seconds",
)
```

Bases: `WidgetColumn`

TimeDeltaColumn(key: 'str', data\_type: 'WdgGetSet\[QTimeLineEdit, float\]' = WdgGetSet(widget=\<class 'pymmcore\_widgets.useq\_widgets.\_column\_info.QTimeLineEdit'\>, getter=, setter=, connect=\<function  at 0x114467920\>), header: 'str | None' = None, is\_row\_selector: 'bool' = False, hidden: 'bool' = False, default: 'Any' = None, default\_factory: 'Callable\[\[\], Any\] | None' = None, minimum\_unit: 'Unit' = 'seconds')

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` |  | *required* |
| `data_type` | `WdgGetSet[QTimeLineEdit, float]` |  | `WdgGetSet(widget=<class 'pymmcore_widgets.useq_widgets._column_info.QTimeLineEdit'>, getter=<function QTimeLineEdit.value at 0x114490040>, setter=<function QTimeLineEdit.setValue at 0x1144900e0>, connect=<function <lambda> at 0x114467920>)` |
| `header` | `str \| None` |  | `None` |
| `is_row_selector` | `bool` |  | `False` |
| `hidden` | `bool` |  | `False` |
| `default` | `Any` |  | `None` |
| `default_factory` | `Callable[[], Any] \| None` |  | `None` |
| `minimum_unit` | `Unit` |  | `'seconds'` |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `data_type` | `WdgGetSet[QTimeLineEdit, float]` |  |
| `minimum_unit` | `Unit` |  |

### data\_type

```python
data_type: WdgGetSet[QTimeLineEdit, float] = TableTimeWidget
```

### minimum\_unit

```python
minimum_unit: Unit = 'seconds'
```

## WellPlateWidget

```python
WellPlateWidget(
    plan: WellPlatePlan | WellPlate | None = None, parent: QWidget | None = None
)
```

Bases: `QWidget`

Widget for selecting a well plate and a subset of wells.

The value returned/received by this widget is a useq.WellPlatePlan (or simply a useq.WellPlate if no selection is made). This widget draws the well plate and allows the user to select wells by clicking/dragging on them.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `plan` | `WellPlatePlan \| WellPlate \| None` | The initial well plate plan. Accepts both a useq.WellPlate (which lacks a selection definition), or a full WellPlatePlan. By default None. | `None` |
| `parent` | `QWidget` | The parent widget, by default None | `None` |

Methods:

| Name | Description |
| --- | --- |
| `setShowRotation` | Set whether to allow visible rotation of the well plate. |
| `value` | Return the current plate and the selected wells as a `useq.WellPlatePlan`. |
| `setValue` | Set the current plate and the selected wells. |
| `currentSelection` | Return the indices of the selected wells as `((row, col), ...)`. |
| `setCurrentSelection` | Select the wells with the given indices. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `valueChanged` |  |  |
| `plate_name` |  |  |

### valueChanged

```python
valueChanged = Signal(object)
```

### plate\_name

```python
plate_name = QComboBox()
```

### setShowRotation

```python
setShowRotation(allow: bool) -> None
```

Set whether to allow visible rotation of the well plate.

If `allow` is False, the rotation checkbox is hidden and the rotation is never shown. If True, the checkbox is shown and the user can toggle the rotation on/off.

### value

```python
value() -> WellPlatePlan
```

Return the current plate and the selected wells as a `useq.WellPlatePlan`.

### setValue

```python
setValue(value: WellPlatePlan | WellPlate | Mapping) -> None
```

Set the current plate and the selected wells.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `PlateInfo` | The plate information to set containing the plate and the selected wells as a list of (name, row, column). | *required* |

### currentSelection

```python
currentSelection() -> tuple[tuple[int, int], ...]
```

Return the indices of the selected wells as `((row, col), ...)`.

### setCurrentSelection

```python
setCurrentSelection(selection: IndexExpression) -> None
```

Select the wells with the given indices.

`selection` can be any 2-d numpy indexing expression, e.g.: - (0, 0) - \[(0, 0), (1, 1), (2, 2)\] - slice(0, 2) - (0, slice(0, 2))

## Re-exports

These names can be imported from this module, but are documented at their top-level location.

| Name | Description |
| --- | --- |
| `ChannelTable` | Table to edit a list of [useq.Channels](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#useq.Channel>). |
| `GridPlanWidget` | Widget to edit a [`useq-schema` GridPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#grid-plans>). |
| `MDASequenceWidget` | A widget that provides a GUI to construct and edit a `useq.MDASequence`. |
| `PositionTable` | Table to edit a list of [useq.Position](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#useq.Position>). |
| `TimePlanWidget` | Table to edit a [useq.TimePlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#time-plans>). |
| `ZPlanWidget` | Widget to edit a [useq.ZPlan](<https://pymmcore-plus.github.io/useq-schema/schema/axes/#z-plans>). |
