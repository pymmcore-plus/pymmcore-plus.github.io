# InstallWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

Widget to manage installation of MicroManager.

This widget will let you download and install a specific version of MicroManager from [https://micro-manager.org/downloads](<https://micro-manager.org/downloads>). It will also manage the currently installed versions.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `table` |  |  |
| `toolbar` |  |  |
| `version_combo` |  |  |
| `install_btn` |  |  |
| `feedback_textbox` |  |  |

## table

```python
table = _InstallTable(self)
```

## toolbar

```python
toolbar = QToolBar(self)
```

## version\_combo

```python
version_combo = QComboBox()
```

## install\_btn

```python
install_btn = QPushButton('Install')
```

## feedback\_textbox

```python
feedback_textbox = QTextEdit()
```

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
