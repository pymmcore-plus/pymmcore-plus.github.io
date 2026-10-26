# ConfigWizard

Screenshot generated from the [example below](<#example>).

Bases: `QWizard`

Hardware Configuration Wizard for Micro-Manager.

It can be used to create a new configuration file or edit an existing one.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `config_file` | `str` | Path to a configuration file to load, by default "". | `''` |
| `core` | `CMMCorePlus` | A CMMCorePlus instance, by default, uses the global singleton. | `None` |
| `parent` | `QWidget` | The parent widget, by default None. | `None` |

Methods:

| Name | Description |
| --- | --- |
| `sizeHint` | Return the size hint for the wizard. |
| `microscopeModel` | Return the microscope model. |
| `save` | Save the configuration to a file. |
| `closeEvent` | Called when the window is closed. |
| `accept` | Accept the wizard and save the configuration to a file. |
| `reject` | Reject the wizard and reload the prior configuration. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `step_labels` |  |  |

## step\_labels

```python
step_labels = [QLabel(f'{i + 1}. {t}') for i, t in enumerate(titles)]
```

## sizeHint

```python
sizeHint() -> QSize
```

Return the size hint for the wizard.

## microscopeModel

```python
microscopeModel() -> Microscope
```

Return the microscope model.

## save

```python
save(path: str | Path) -> None
```

Save the configuration to a file.

## closeEvent

```python
closeEvent(event: QCloseEvent | None) -> None
```

Called when the window is closed.

## accept

```python
accept() -> None
```

Accept the wizard and save the configuration to a file.

## reject

```python
reject() -> None
```

Reject the wizard and reload the prior configuration.

## Example

examples/config\_wizard.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets.hcwizard.config_wizard import ConfigWizard

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

wiz = ConfigWizard()
wiz.show()

app.exec()
```
