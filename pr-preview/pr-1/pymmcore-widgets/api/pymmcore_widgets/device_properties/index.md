# pymmcore\_widgets.device\_properties

Widgets related to device properties.

Classes:

| Name | Description |
| --- | --- |
| `DevicePropertyTable` | Table of all currently loaded device properties. |

## DevicePropertyTable

```python
DevicePropertyTable(
    parent: QWidget | None = None,
    *,
    enable_property_widgets: bool = True,
    mmcore: CMMCorePlus | None = None,
    connect_core: bool = True,
)
```

Bases: `QTableWidget`

Table of all currently loaded device properties.

This table is used by `PropertyBrowser` to display all properties in the system, and by the `GroupPresetTableWidget`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget` | Parent widget, by default None | `None` |
| `enable_property_widgets` | `bool` | Whether to enable each property widget, by default True | `True` |
| `mmcore` | `CMMCorePlus` | CMMCore instance, by default None | `None` |
| `connect_core` | `bool` | Whether to connect the widget to the core. If False, changes in the table will not update the core. By default, True. | `True` |

Methods:

| Name | Description |
| --- | --- |
| `checkGroup` |  |
| `setRowNumbersVisible` | Set whether line numbers are visible. |
| `setRowsCheckable` | Set whether individual row checkboxes are visible. |
| `setReadOnlyDevicesVisible` | Set whether read-only devices are visible. |
| `filterDevices` | Update the table to only show devices that match the given query/filter. |
| `getCheckedProperties` | Return a list of checked properties. |
| `value` |  |
| `setValue` |  |
| `setCheckedProperties` |  |
| `getRowData` |  |
| `setPropertyWidgetsEnabled` | Set whether each widget is enabled. |
| `uncheckAll` | Uncheck all rows. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `valueChanged` |  |  |
| `PROP_ROLE` |  |  |

### valueChanged

```python
valueChanged = Signal()
```

### PROP\_ROLE

```python
PROP_ROLE = QTableWidgetItem.ItemType.UserType + 1
```

### checkGroup

```python
checkGroup(group: str) -> None
```

### setRowNumbersVisible

```python
setRowNumbersVisible(visible: bool = True) -> None
```

Set whether line numbers are visible.

### setRowsCheckable

```python
setRowsCheckable(checkable: bool = True) -> None
```

Set whether individual row checkboxes are visible.

### setReadOnlyDevicesVisible

```python
setReadOnlyDevicesVisible(visible: bool = True) -> None
```

Set whether read-only devices are visible.

### filterDevices

```python
filterDevices(
    query: str | Pattern = "",
    *,
    exclude_devices: Iterable[DeviceType] = (),
    include_devices: Iterable[DeviceType] = (),
    include_read_only: bool = True,
    include_pre_init: bool = True,
    always_show_checked: bool = False,
    predicate: Callable[[DeviceProperty], bool | None] | None = None,
) -> None
```

Update the table to only show devices that match the given query/filter.

Filters are applied in the following order: 1. If `include_devices` is provided, only devices of the specified types will be considered. 2. If `exclude_devices` is provided, devices of the specified types will be hidden (even if they are in `include_devices`). 3. If `always_show_checked` is True, remaining rows that are checked will always be shown, regardless of other filters. 4. If `predicate` is provided and it returns False, the row is hidden. 5. If `include_read_only` is False, read-only properties are hidden. 6. If `include_pre_init` is False, pre-initialized properties are hidden. 7. Query filtering is applied last, hiding rows that do not match the query.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str \| Pattern` | A string or regex pattern to match against the device-property names. If empty, no filtering is applied, by default "" | `''` |
| `exclude_devices` | `Iterable[DeviceType]` | A list of device types to exclude from the table, by default () | `()` |
| `include_devices` | `Iterable[DeviceType]` | A list of device types to include in the table, by default () | `()` |
| `include_read_only` | `bool` | Whether to include read-only properties in the table, by default True | `True` |
| `include_pre_init` | `bool` | Whether to include pre-initialized properties in the table, by default True | `True` |
| `always_show_checked` | `bool` | Whether to always include rows that are checked, by default False. | `False` |
| `predicate` | `Callable[[DeviceProperty, QTableWidgetItem], bool \| None] \| None` | A function that takes a `DeviceProperty` and `QTableWidgetItem` and returns True to include the row, False to exclude it, or None to skip filtering. If None, no additional filtering is applied, by default None | `None` |

### getCheckedProperties

```python
getCheckedProperties(*, visible_only: bool = False) -> list[Setting]
```

Return a list of checked properties.

Each item in the list is a tuple of (device, property, value).

### value

```python
value() -> list[Setting]
```

### setValue

```python
setValue(value: Iterable[tuple[str, str, str]]) -> None
```

### setCheckedProperties

```python
setCheckedProperties(
    value: Iterable[tuple[str, str, str]], with_value: bool = True
) -> None
```

### getRowData

```python
getRowData(row: int) -> tuple[str, str, str]
```

### setPropertyWidgetsEnabled

```python
setPropertyWidgetsEnabled(enabled: bool) -> None
```

Set whether each widget is enabled.

### uncheckAll

```python
uncheckAll() -> None
```

Uncheck all rows.

## Re-exports

These names can be imported from this module, but are documented at their top-level location.

| Name | Description |
| --- | --- |
| `PropertiesWidget` | Convenience container to control a specific set of PropertyWidgets. |
| `PropertyBrowser` | A Widget to browse and change properties of all devices. |
| `PropertyWidget` | Widget to display and control a single device property. |
