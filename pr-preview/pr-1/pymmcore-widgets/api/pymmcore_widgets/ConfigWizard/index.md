# ConfigWizard

Screenshot generated from the [example below](<#example>).

## Example

examples/config\_wizard.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import ConfigWizard

app = QApplication([])

mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

wiz = ConfigWizard()
wiz.show()

app.exec()
```

## API

Bases: `QWizard`

Hardware Configuration Wizard for Micro-Manager.

It can be used to create a new configuration file or edit an existing one.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `config_file` | `str` | Path to a configuration file to load, by default "". | `''` |
| `core` | `CMMCorePlus` | A CMMCorePlus instance, by default, uses the global singleton. (Note that this parameter is called `core`, where other widgets use `mmcore`.) | `None` |
| `parent` | `QWidget` | The parent widget, by default None. | `None` |

### microscopeModel

```python
microscopeModel() -> Microscope
```

Return the microscope model.

### save

```python
save(path: str | Path) -> None
```

Save the configuration to a file.

### accept

```python
accept() -> None
```

Accept the wizard and save the configuration to a file.

### reject

```python
reject() -> None
```

Reject the wizard and reload the prior configuration.
