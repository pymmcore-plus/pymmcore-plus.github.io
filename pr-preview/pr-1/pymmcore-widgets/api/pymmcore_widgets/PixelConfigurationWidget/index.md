# PixelConfigurationWidget

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

A Widget to define the pixel size configurations.

Each pixel size configuration can be linked to any device and property. However, it's important to note that all pixel size configurations must include the same devices and properties. The only variation allowed between different configurations is in the values of the device properties.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget, by default None | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `pymmcore_plus.CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

Methods:

| Name | Description |
| --- | --- |
| `value` | Return the current state of the widget describing the pixel configurations. |
| `setValue` | Set the state of the widget describing the pixel configurations. |

## value

```python
value() -> list[PixelSizePreset]
```

Return the current state of the widget describing the pixel configurations.

Returns:

| Type | Description |
| --- | --- |
| `list[PixelSizePreset][PixelSizePreset]` | A list of pixel configurations data. |

**Example:**

```text
output = [
    PixelSizePreset(
        name='Res10x',
        settings=[Setting('Objective', 'Label', 'Nikon 10X S Fluor')],
        pixel_size_um=1.0
    ),
    ...
]
```

## setValue

```python
setValue(value: list[PixelSizePreset]) -> None
```

Set the state of the widget describing the pixel configurations.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `list[PixelSizePreset][PixelSizePreset]` | The list of pixel configurations data to set. | *required* |

**Example:**

```text
input = [
    PixelSizePreset(
        name='Res10x',
        settings=[Setting('Objective', 'Label', 'Nikon 10X S Fluor')],
        pixel_size_um=1.0
    ),
    ...
]
```

## Example

examples/pixel\_configuration\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import PixelConfigurationWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

px_wdg = PixelConfigurationWidget()
px_wdg.show()

app.exec()
```
