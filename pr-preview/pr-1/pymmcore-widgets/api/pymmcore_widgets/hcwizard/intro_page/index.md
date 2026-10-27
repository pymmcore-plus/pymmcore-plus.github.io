# pymmcore\_widgets.hcwizard.intro\_page

Config wizard, step 1: start a new configuration or edit an existing file.

**Classes**

| Name | Description |
| --- | --- |
| `IntroPage` | First page, for selecting new or existing configuration. |

**Attributes**

| Name | Description |
| --- | --- |
| `EXISTING_CONFIG` |  |
| `SRC_CONFIG` |  |

## Classes

### IntroPage

```python
IntroPage(model: Microscope, core: CMMCorePlus)
```

Bases: `ConfigWizardPage`

First page, for selecting new or existing configuration.

#### initializePage

```python
initializePage() -> None
```

Called to prepare the page just before it is shown.

#### cleanupPage

```python
cleanupPage() -> None
```

Called to reset the page's contents when the user clicks BACK.

#### validatePage

```python
validatePage() -> bool
```

Validate the page when the user clicks Next or Finish.

#### isComplete

```python
isComplete() -> bool
```

Called to determine whether the Next/Finish button should be enabled.

## Attributes

### SRC\_CONFIG

```python
SRC_CONFIG = 'src_config'
```

### EXISTING\_CONFIG

```python
EXISTING_CONFIG = 'EXISTING_CONFIG'
```
