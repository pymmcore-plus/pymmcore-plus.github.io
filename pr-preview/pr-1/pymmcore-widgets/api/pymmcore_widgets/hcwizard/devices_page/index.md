# pymmcore\_widgets.hcwizard.devices\_page

Classes:

| Name | Description |
| --- | --- |
| `DevicesPage` | Page for adding and removing devices. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `logger` |  |  |

## logger

```python
logger = logging.getLogger(__name__)
```

## DevicesPage

```python
DevicesPage(model: Microscope, core: CMMCorePlus)
```

Bases: `ConfigWizardPage`

Page for adding and removing devices.

Methods:

| Name | Description |
| --- | --- |
| `initializePage` | Called to prepare the page just before it is shown. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `current` |  |  |
| `available` |  |  |

### current

```python
current = _CurrentDevicesWidget(model, core)
```

### available

```python
available = _AvailableDevicesWidget(model, core)
```

### initializePage

```python
initializePage() -> None
```

Called to prepare the page just before it is shown.
