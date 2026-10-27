# ChannelWidget

Screenshot generated from the [example below](<#example>).

## Example

examples/channel\_widget.py

```python
"""Example usage of the ChannelWidget class.

Check also the 'image_preview.py' example to see the ChannelWidget
used in combination of other widgets.
"""

from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ChannelWidget

app = QApplication([])

mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

ch_wdg = ChannelWidget()
ch_wdg.show()

app.exec()
```

## API

Bases: `QWidget`

Combo box that shows and sets the current channel.

The choices are the presets of the channel group.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `channel_group` | `str \| None` | Name of the micromanager group defining the microscope channels. By default, it will be guessed using the `CMMCorePlus.getOrGuessChannelGroup` method and a choice dialog will be presented if there are multiple options. This method looks for a group configuration name matching the default regex `re.compile("(chan{1,2}(el)?\|filt(er)?)s?", re.IGNORECASE)`. A different string/regex can be set with the `CMMCorePlus.channelGroup_pattern` property. | `None` |
| `parent` | `QWidget \| None` | Optional parent widget. By default, None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |
| `See` |  |  | *required* |
| `widget` |  |  | *required* |
