# ObjectivesWidget

Screenshot generated from the [example below](<#example>).

## Example

examples/objectives\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ObjectivesWidget

app = QApplication([])

mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

obj_wdg = ObjectivesWidget()
obj_wdg.show()

app.exec()
```

## API

Bases: `QWidget`

Combo box that shows and sets the current objective.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `objective_device` | `str \| None` | Device label for the micromanager objective device. By default, it will be guessed using the `CMMCorePlus.guessObjectiveDevices` method and a choice dialog will be presented if there are multiple options. This method looks for a micromanager device matching the default regex `re.compile("(.+)?(nosepiece\|obj(ective)?)(turret)?s?", re.IGNORECASE)`. To change the search pattern, set `CMMCorePlus.objective_device_pattern`. | `None` |
| `parent` | `QWidget \| None` | Optional parent widget, by default None | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |
