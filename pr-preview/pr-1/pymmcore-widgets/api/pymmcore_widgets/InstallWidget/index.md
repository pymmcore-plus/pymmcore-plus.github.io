# InstallWidget

Screenshot generated from the [example below](<#example>).

## Example

examples/install\_widget.py

```python
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import InstallWidget

app = QApplication([])
wdg = InstallWidget()
wdg.show()
app.exec()
```

## API

Bases: `QWidget`

Widget to install Micro-Manager's device adapters (like `mmcore install`).

This widget will let you download and install a specific version of Micro-Manager from [https://micro-manager.org/downloads](<https://micro-manager.org/downloads>). It will also manage the currently installed versions.
