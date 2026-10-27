# ExposureWidget

Screenshot generated from the [example below](<#example>).

## Example

examples/exposure\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ExposureWidget

app = QApplication([])

mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

exp_wdg = ExposureWidget()
exp_wdg.show()

app.exec()
```

## API

Bases: `QWidget`

Spin box that shows and sets the exposure time (in ms) of a camera.

See the `ImagePreview` example for this widget combined with an image preview and other controls.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `camera` | `str \| None` | The camera device label. By default, None. If not specified, the widget will use the current Camera device. | `None` |
| `parent` | `QWidget \| None` | Optional parent widget. By default, None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance()`. | `None` |

### setCamera

```python
setCamera(camera: str | None = None) -> None
```

Set which camera this widget tracks.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `camera` | `str` | The camera device label. By default, None. If not specified, the widget will use the current Camera device. | `None` |
