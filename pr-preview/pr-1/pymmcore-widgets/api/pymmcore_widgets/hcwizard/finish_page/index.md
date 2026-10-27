# pymmcore\_widgets.hcwizard.finish\_page

Config wizard, last step: save the configuration file.

**Classes**

| Name | Description |
| --- | --- |
| `FinishPage` | Page for saving the configuration file. |

**Attributes**

| Name | Description |
| --- | --- |
| `DEST_CONFIG` |  |

## Classes

### FinishPage

```python
FinishPage(model: Microscope, core: CMMCorePlus)
```

Bases: `ConfigWizardPage`

Page for saving the configuration file.

#### initializePage

```python
initializePage() -> None
```

Called to prepare the page just before it is shown.

#### validatePage

```python
validatePage() -> bool
```

Validate. the page when the user clicks Next or Finish.

## Attributes

### DEST\_CONFIG

```python
DEST_CONFIG = 'dest_config'
```
