# PropertyWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

Widget to display and control a single device property.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_label` | `str` | Device label. | *required* |
| `prop_name` | `str` | Property name. | *required* |
| `parent` | `QWidget \| None` | Optional parent widget. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional core instance. If not provided, uses the global instance. | `None` |
| `connect_core` | `bool` | If True, widget changes update the core and vice versa. | `True` |

Methods:

| Name | Description |
| --- | --- |
| `value` | Get the current widget value. |
| `setValue` | Set the widget value. |
| `refresh` | Update the value of the widget from mmcore. |
| `propertyType` | Return the property type. |
| `deviceType` | Return the device type. |
| `isReadOnly` | Return True if the property is read-only. |
| `isPreInit` | Return True if the property is pre-initialization. |
| `allowedValues` | Return allowed values if property has constraints. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `valueChanged` |  |  |
| `inner_widget` | `QWidget` | Return the inner value widget (spinbox, slider, combobox, etc). |

## valueChanged

```python
valueChanged = Signal(object)
```

## inner\_widget

```python
inner_widget: QWidget
```

Return the inner value widget (spinbox, slider, combobox, etc).

## value

```python
value() -> Any
```

Get the current widget value.

## setValue

```python
setValue(value: Any) -> None
```

Set the widget value.

## refresh

```python
refresh() -> None
```

Update the value of the widget from mmcore.

(If all goes well this shouldn't be necessary, but if a propertyChanged event is missed, this can be used).

## propertyType

```python
propertyType() -> PropertyType
```

Return the property type.

## deviceType

```python
deviceType() -> DeviceType
```

Return the device type.

## isReadOnly

```python
isReadOnly() -> bool
```

Return True if the property is read-only.

## isPreInit

```python
isPreInit() -> bool
```

Return True if the property is pre-initialization.

## allowedValues

```python
allowedValues() -> tuple[str, ...]
```

Return allowed values if property has constraints.

## Example

examples/property\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication, QFormLayout, QWidget

from pymmcore_widgets import PropertyWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

wdg = QWidget()
wdg.setLayout(QFormLayout())

devs_pros = [
    ("Camera", "AllowMultiROI"),
    ("Camera", "Binning"),
    ("Camera", "CCDTemperature"),
]

for dev, prop in devs_pros:
    prop_wdg = PropertyWidget(dev, prop)
    wdg.layout().addRow(f"{dev}-{prop}:", prop_wdg)

wdg.show()

app.exec()
```
