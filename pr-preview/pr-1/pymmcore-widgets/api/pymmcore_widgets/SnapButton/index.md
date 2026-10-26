# SnapButton

Screenshot generated from the [example below](<#example>).

Bases: `QPushButton`

Create a snap QPushButton.

This button is linked to the `CMMCorePlus.snap` method. Once the button is clicked, an image is acquired and the `pymmcore-plus` signal `imageSnapped` is emitted.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

Examples:

> [!NOTE]
>
> **Combining `SnapButton` with other widgets**
>
> see [ImagePreview](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ImagePreview/#example>)

## Example

examples/snap\_button.py

```python
"""Example usage of the SnapButton class.

Check also the 'image_widget.py' example to see the SnapButton
used in combination of other widgets.
"""

from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import SnapButton

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

snap_btn = SnapButton()
snap_btn.show()

app.exec()
```
