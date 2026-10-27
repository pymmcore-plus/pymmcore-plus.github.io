# ObjectivesPixelConfigurationWidget

Screenshot generated from the [example below](<#example>).

## Example

examples/objectives\_pixel\_configuration\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ObjectivesPixelConfigurationWidget

app = QApplication([])

mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

px_wdg = ObjectivesPixelConfigurationWidget()
px_wdg.show()

app.exec()
```

## API

Bases: `QDialog`

A Widget to define the pixel size configurations using the objective device.

It *requires* to have installed on the microscope a *motorzed objective turret* and allows to set the pixel size using only the *motorzed objective turret device* properties. No other properties can be assigned to the pixel configuration. For this purpose, use the PixelConfigurationWidget which is more similar to the original micromanager pixel configuration widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget, by default None | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |
