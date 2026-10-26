# ShuttersWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

A Widget to control shutters and Micro-Manager autoshutter.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `shutter_device` | `str` | The shutter device Label. | *required* |
| `autoshutter` | `bool` | If True, a checkbox controlling the Micro-Manager autoshutter is added to the layout. | `True` |
| `button_text_open` | `str` | Text shown on the button when the shutter is open. | `''` |
| `button_text_closed` | `str` | Text shown on the button when the shutter is closed. | `''` |
| `icon_open` | `str` | Iconify icon key for the open state. | `'mdi:hexagon-outline'` |
| `icon_closed` | `str` | Iconify icon key for the closed state. | `'mdi:hexagon-slice-6'` |
| `icon_color_open` | `COLOR_TYPE` | Icon color for the open state. | `'green'` |
| `icon_color_closed` | `COLOR_TYPE` | Icon color for the closed state. | `'gray'` |
| `icon_size` | `int` | Icon size in pixels. | `25` |
| `parent` | `QWidget \| None` | Optional parent widget. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional CMMCorePlus micromanager core. | `None` |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `shutter_device` |  |  |
| `shutter_button` |  |  |
| `autoshutter_checkbox` |  |  |

## shutter\_device

```python
shutter_device = shutter_device
```

## shutter\_button

```python
shutter_button = QPushButton(text=button_text_closed)
```

## autoshutter\_checkbox

```python
autoshutter_checkbox = QCheckBox(text='Auto')
```

## Example

examples/shutters\_widget.py

```python
"""Example usage of the ShuttersWidget class.

In this example all the devices of type 'Shutter' that are loaded
in micromanager are displayed with a 'ShuttersWidget'.

The autoshutter checkbox is displayed only with the last shutter device.
"""

from pymmcore_plus import CMMCorePlus, DeviceType
from qtpy.QtWidgets import QApplication, QHBoxLayout, QWidget

from pymmcore_widgets import ShuttersWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

wdg = QWidget()
wdg.setLayout(QHBoxLayout())

shutter_dev_list = list(mmc.getLoadedDevicesOfType(DeviceType.Shutter))

for idx, shutter_dev in enumerate(shutter_dev_list):
    # bool to display the autoshutter checkbox only with the last shutter
    autoshutter = bool(idx >= len(shutter_dev_list) - 1)
    shutter = ShuttersWidget(shutter_dev, autoshutter=autoshutter)
    wdg.layout().addWidget(shutter)

wdg.show()

app.exec()
```
