# ChannelWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

A QComboBox to select which micromanager channel configuration to use.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `channel_group` | `str \| None` | Name of the micromanager group defining the microscope channels. By default, it will be guessed using the `CMMCorePlus.getOrGuessChannelGroup` method and a choice dialog will be presented if there are multiple options. This method looks for a group configuration name matching the default regex `re.compile("(chan{1,2}(el)?\|filt(er)?)s?", re.IGNORECASE)`. A different string/regex can be set using the `CMMCorePlus.channelGroup_pattern` method. | `None` |
| `parent` | `QWidget \| None` | Optional parent widget. By default, None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

Examples:

> [!NOTE]
>
> **Combining `ChannelWidget` with other widgets**
>
> see [ImagePreview](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ImagePreview/#example>)

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `channel_wdg` | `PresetsWidget \| QComboBox` |  |

## channel\_wdg

```python
channel_wdg: PresetsWidget | QComboBox
```

## Example

examples/channel\_widget.py

```python
"""Example usage of the ChannelWidget class.

Check also the 'image_widget.py' example to see the ChannelWidget
used in combination of other widgets.
"""

from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ChannelWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

ch_wdg = ChannelWidget()
ch_wdg.show()

app.exec()
```
