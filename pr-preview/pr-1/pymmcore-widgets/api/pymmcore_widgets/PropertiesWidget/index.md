# PropertiesWidget

Screenshot generated from the [example below](<#example>).

## Example

examples/properties\_widget.py

```python
"""The PropertiesWidget is a container for a set of PropertyWidgets.

It creates widgets for a set of different properties, filtered based on
the arguments to the constructor.
"""

from pymmcore_plus import CMMCorePlus, PropertyType
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import PropertiesWidget

app = QApplication([])

mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

wdg = PropertiesWidget(
    # regex pattern to match property names
    property_name_pattern="test",
    property_type={PropertyType.Float},
    has_limits=True,
)

wdg.show()
app.exec()
```

## API

Bases: `QWidget`

Controls for a filtered set of device properties (a PropertyWidget each).

Properties can be filtered by a number of criteria, which are passed to `CMMCorePlus.iterProperties`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `property_type` | `int \| Sequence[int] \| None` | PropertyType (or types) to filter by, by default all property types will be yielded. | `None` |
| `property_name_pattern` | `str \| Pattern \| None` | Property name to filter by, by default all property names will be yielded. May be a compiled regular expression or a string, in which case it will be compiled with `re.IGNORECASE`. | `None` |
| `device_type` | `DeviceType \| None` | DeviceType to filter by, by default all device types will be yielded. | `None` |
| `device_label` | `str \| None` | Device label to filter by, by default all device labels will be yielded. | `None` |
| `has_limits` | `bool \| None` | If provided, only properties with `hasPropertyLimits` matching this value will be yielded. | `None` |
| `is_read_only` | `bool \| None` | If provided, only properties with `isPropertyReadOnly` matching this value will be yielded. | `None` |
| `is_sequenceable` | `bool \| None` | If provided only properties with `isPropertySequenceable` matching this value will be yielded. | `None` |

### rebuild

```python
rebuild() -> None
```

Rebuild the layout, populating based on current filters.
