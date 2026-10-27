# pymmcore\_widgets.useq\_widgets

Widgets for the useq-schema data model.

**Submodules**

| Name | Description |
| --- | --- |
| `points_plans` | Widgets that create MultiPoint plans. |

**Classes**

| Name | Description |
| --- | --- |
| `BoolColumn` | Column of checkboxes (`bool` values). |
| `ChoiceColumn` | Column of combo boxes, choosing from `allowed_values`. |
| `DataTable` | Table whose columns are defined by `ColumnInfo` class attributes. |
| `DataTableWidget` | A `DataTable` with a toolbar to add, select and remove rows. |
| `FloatColumn` | Column of float spin boxes, between `minimum` and `maximum`. |
| `IntColumn` | Column of integer spin boxes, between `minimum` and `maximum`. |
| `PointsPlanWidget` | Widget to select the FOVs per well of the plate. |
| `TextColumn` | Column that will use a standard QTableWidgetItem. |
| `TimeDeltaColumn` | Column of durations, typed as text with units (e.g. `"1.5 s"`, `"2 min"`). |
| `WellPlateWidget` | Widget for selecting a well plate and a subset of wells. |

**Attributes**

| Name | Description |
| --- | --- |
| `PYMMCW_METADATA_KEY` |  |

## Classes

### BoolColumn

```python
BoolColumn(
    _ROLE: int = UserRole + 1,
    header: str | None = None,
    is_row_selector: bool = False,
    hidden: bool = False,
    default: Any = None,
    default_factory: Callable[[], Any] | None = None,
    data_type: WdgGetSet = TableBoolWidget,
)
```

Bases: `WidgetColumn`

Column of checkboxes (`bool` values).

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `key` | `str` |  |
| `data_type` | `WdgGetSet` |  |
| `header` | `str \| None` |  |
| `is_row_selector` | `bool` |  |
| `hidden` | `bool` |  |
| `default` | `Any` |  |
| `default_factory` | `Callable[[], Any] \| None` |  |

#### data\_type

```python
data_type: WdgGetSet = TableBoolWidget
```

### ChoiceColumn

```python
ChoiceColumn(
    _ROLE: int = UserRole + 1,
    header: str | None = None,
    is_row_selector: bool = False,
    hidden: bool = False,
    default: Any = None,
    default_factory: Callable[[], Any] | None = None,
    data_type: WdgGetSet[CheckableCombo, str] = ChoiceWidget,
    allowed_values: tuple[str, ...] | None = None,
)
```

Bases: `WidgetColumn`

Column of combo boxes, choosing from `allowed_values`.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `key` | `str` |  |
| `data_type` | `WdgGetSet[CheckableCombo, str]` |  |
| `header` | `str \| None` |  |
| `is_row_selector` | `bool` |  |
| `hidden` | `bool` |  |
| `default` | `Any` |  |
| `default_factory` | `Callable[[], Any] \| None` |  |
| `allowed_values` | `tuple[str, ...] \| None` |  |

#### data\_type

```python
data_type: WdgGetSet[CheckableCombo, str] = ChoiceWidget
```

#### allowed\_values

```python
allowed_values: tuple[str, ...] | None = None
```

#### isChecked

```python
isChecked(table: QTableWidget, row: int, col: int) -> bool
```

#### setCheckState

```python
setCheckState(
    table: QTableWidget, row: int, col: int, state: CheckState
) -> None
```

### FloatColumn

```python
FloatColumn(
    _ROLE: int = UserRole + 1,
    header: str | None = None,
    is_row_selector: bool = False,
    hidden: bool = False,
    default: Any = None,
    default_factory: Callable[[], Any] | None = None,
    minimum: float = 0,
    maximum: float = 999999,
    decimals: int = 2,
    data_type: WdgGetSet = TableFloatWidget,
)
```

Column of float spin boxes, between `minimum` and `maximum`.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `key` | `str` |  |
| `data_type` | `WdgGetSet` |  |
| `header` | `str \| None` |  |
| `is_row_selector` | `bool` |  |
| `hidden` | `bool` |  |
| `default` | `Any` |  |
| `default_factory` | `Callable[[], Any] \| None` |  |
| `minimum` | `float` |  |
| `maximum` | `float` |  |
| `decimals` | `int` |  |

#### data\_type

```python
data_type: WdgGetSet = TableFloatWidget
```

### IntColumn

```python
IntColumn(
    _ROLE: int = UserRole + 1,
    header: str | None = None,
    is_row_selector: bool = False,
    hidden: bool = False,
    default: Any = None,
    default_factory: Callable[[], Any] | None = None,
    minimum: int = 0,
    maximum: int = 999999999,
    decimals: int = 2,
    data_type: WdgGetSet = TableIntWidget,
)
```

Column of integer spin boxes, between `minimum` and `maximum`.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `key` | `str` |  |
| `data_type` | `WdgGetSet` |  |
| `header` | `str \| None` |  |
| `is_row_selector` | `bool` |  |
| `hidden` | `bool` |  |
| `default` | `Any` |  |
| `default_factory` | `Callable[[], Any] \| None` |  |
| `minimum` | `int` |  |
| `maximum` | `int` |  |
| `decimals` | `int` |  |

#### data\_type

```python
data_type: WdgGetSet = TableIntWidget
```

#### minimum

```python
minimum: int = 0
```

#### maximum

```python
maximum: int = 999999999
```

### TextColumn

```python
TextColumn(
    _ROLE: int = UserRole + 1,
    header: str | None = None,
    is_row_selector: bool = False,
    hidden: bool = False,
    default: str | None = None,
    default_factory: Callable[[], Any] | None = None,
    data_type: type = str,
    checkable: bool = False,
    checked: bool = True,
)
```

Bases: `ColumnInfo`

Column that will use a standard QTableWidgetItem.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `key` | `str` |  |
| `data_type` | `type` |  |
| `header` | `str \| None` |  |
| `is_row_selector` | `bool` |  |
| `hidden` | `bool` |  |
| `default` | `str \| None` |  |
| `default_factory` | `Callable[[], Any] \| None` |  |
| `checkable` | `bool` |  |
| `checked` | `bool` |  |

#### data\_type

```python
data_type: type = str
```

#### header

```python
header: str | None = None
```

#### is\_row\_selector

```python
is_row_selector: bool = False
```

#### hidden

```python
hidden: bool = False
```

#### default

```python
default: str | None = None
```

#### checkable

```python
checkable: bool = False
```

#### checked

```python
checked: bool = True
```

#### init\_cell

```python
init_cell(
    table: QTableWidget, row: int, col: int, change_signal: SignalInstance
) -> None
```

#### get\_cell\_data

```python
get_cell_data(table: QTableWidget, row: int, col: int) -> dict[str, Any]
```

#### set\_cell\_data

```python
set_cell_data(table: QTableWidget, row: int, col: int, value: Any) -> None
```

#### isChecked

```python
isChecked(table: QTableWidget, row: int, col: int) -> bool
```

#### setCheckState

```python
setCheckState(
    table: QTableWidget, row: int, col: int, state: CheckState
) -> None
```

### TimeDeltaColumn

```python
TimeDeltaColumn(
    _ROLE: int = UserRole + 1,
    header: str | None = None,
    is_row_selector: bool = False,
    hidden: bool = False,
    default: Any = None,
    default_factory: Callable[[], Any] | None = None,
    data_type: WdgGetSet[QTimeLineEdit, float] = TableTimeWidget,
    minimum_unit: Unit = "seconds",
)
```

Bases: `WidgetColumn`

Column of durations, typed as text with units (e.g. `"1.5 s"`, `"2 min"`).

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `key` | `str` |  |
| `data_type` | `WdgGetSet[QTimeLineEdit, float]` |  |
| `header` | `str \| None` |  |
| `is_row_selector` | `bool` |  |
| `hidden` | `bool` |  |
| `default` | `Any` |  |
| `default_factory` | `Callable[[], Any] \| None` |  |
| `minimum_unit` | `Unit` |  |

#### data\_type

```python
data_type: WdgGetSet[QTimeLineEdit, float] = TableTimeWidget
```

#### minimum\_unit

```python
minimum_unit: Unit = 'seconds'
```

### DataTable

```python
DataTable(rows: int = 0, parent: QWidget | None = None)
```

Bases: `QTableWidget`

Table whose columns are defined by `ColumnInfo` class attributes.

#### valueChanged

```python
valueChanged = Signal()
```

#### COLUMNS

```python
COLUMNS: tuple[ColumnInfo, ...] = ()
```

#### columnInfo

```python
columnInfo(col: int) -> ColumnInfo | None
```

#### addColumns

```python
addColumns(column_info: Iterable[ColumnInfo]) -> None
```

#### addColumn

```python
addColumn(column_info: ColumnInfo, position: int | None = None) -> None
```

Add a new column to the table.

The ColumnInfo object is stored in the header item's data and used to populate the new column, and new rows that are added later, based on the data type and other info in the ColumnInfo object.

#### indexOf

```python
indexOf(header: str | ColumnInfo) -> int
```

#### iterRecords

```python
iterRecords(
    exclude_unchecked: bool = False, exclude_hidden_cols: bool = False
) -> Iterator[Record]
```

Return an iterator over the data in the table in records format.

(Records are a list of dicts mapping {'column header' -\> value} for each row.)

#### setValue

```python
setValue(records: Iterable[Record]) -> None
```

Set the value of the table.

#### checkAllRows

```python
checkAllRows() -> None
```

#### clearChecks

```python
clearChecks() -> None
```

#### rowData

```python
rowData(row: int, exclude_hidden_cols: bool = False) -> Record
```

#### setRowData

```python
setRowData(row: int, data: Record) -> None
```

### DataTableWidget

```python
DataTableWidget(rows: int = 0, parent: QWidget | None = None)
```

Bases: `QWidget`

A `DataTable` with a toolbar to add, select and remove rows.

Base class of `ChannelTable`, `PositionTable` and `TimePlanWidget`.

#### valueChanged

```python
valueChanged = Signal()
```

Emitted (with no arguments) when the table changes; read it with `value()`.

#### COLUMNS

```python
COLUMNS: tuple[ColumnInfo, ...]
```

#### table

```python
table() -> DataTable
```

#### toolBar

```python
toolBar() -> QToolBar
```

#### value

```python
value(exclude_unchecked: bool = True) -> Any
```

Return a list of dicts of the data in the table.

#### setValue

```python
setValue(value: Iterable[Any]) -> None
```

Set the value of the table.

### WellPlateWidget

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

#### valueChanged

```python
valueChanged = Signal(object)
```

Emitted with the new `useq.WellPlatePlan` when the plate or selection changes.

#### setShowRotation

```python
setShowRotation(allow: bool) -> None
```

Set whether to allow visible rotation of the well plate.

If `allow` is False, the rotation checkbox is hidden and the rotation is never shown. If True, the checkbox is shown and the user can toggle the rotation on/off.

#### value

```python
value() -> WellPlatePlan
```

Return the current plate and the selected wells as a `useq.WellPlatePlan`.

#### setValue

```python
setValue(value: WellPlatePlan | WellPlate | Mapping) -> None
```

Set the current plate and the selected wells.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `PlateInfo` | The plate information to set containing the plate and the selected wells as a list of (name, row, column). | *required* |

#### currentSelection

```python
currentSelection() -> tuple[tuple[int, int], ...]
```

Return the indices of the selected wells as `((row, col), ...)`.

#### setCurrentSelection

```python
setCurrentSelection(selection: IndexExpression) -> None
```

Select the wells with the given indices.

`selection` can be any 2-d numpy indexing expression, e.g.: - (0, 0) - \[(0, 0), (1, 1), (2, 2)\] - slice(0, 2) - (0, slice(0, 2))

### PointsPlanWidget

```python
PointsPlanWidget(
    plan: RelativeMultiPointPlan | None = None, parent: QWidget | None = None
)
```

Bases: `QWidget`

Widget to select the FOVs per well of the plate.

This widget allows the user to select the number of FOVs per well, (or to generally show a multi-point plan, such as a grid or random points plan, even if not within the context of a well plate.)

The value() method returns the selected plan, one of: - useq.GridRowsColumns - useq.RandomPoints - useq.RelativePosition

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `plan` | `RelativeMultiPointPlan \| None` | The useq MultiPoint plan to display and edit. | `None` |
| `parent` | `QWidget \| None` | The parent widget. | `None` |

#### valueChanged

```python
valueChanged = Signal(object)
```

Emitted with the new points plan when the widget changes.

#### value

```python
value() -> RelativeMultiPointPlan
```

Return the selected plan.

#### setValue

```python
setValue(plan: RelativeMultiPointPlan) -> None
```

Set the current plan.

#### setWellSize

```python
setWellSize(width: float | None = None, height: float | None = None) -> None
```

Set the well size width and/or height in mm.

#### setWellShape

```python
setWellShape(shape: Shape | str) -> None
```

Set the shape of the well.

Can be a `useq.Shape` enum or the strings "circle", "ellipse", "square", or "rectangle".

## Attributes

### PYMMCW\_METADATA\_KEY

```python
PYMMCW_METADATA_KEY = 'pymmcore_widgets'
```

## Re-exports

These can also be imported from this module, but each is documented under its shortest import path (linked below).

| Name | Description |
| --- | --- |
| `ChannelTable` | Table to edit a list of channels (`useq.Channel`). |
| `GridPlanWidget` | Widget to edit a grid plan. |
| `MDASequenceWidget` | A widget that provides a GUI to construct and edit a `useq.MDASequence`. |
| `PositionTable` | Table to edit a list of stage positions (`useq.Position`). |
| `TimePlanWidget` | Table to edit a time plan (`useq.AnyTimePlan`), one row per phase. |
| `ZPlanWidget` | Widget to edit a z plan (`useq.AnyZPlan`). |
