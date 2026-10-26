# pymmcore\_widgets.hcwizard.intro\_page

Classes:

| Name | Description |
| --- | --- |
| `IntroPage` | First page, for selecting new or existing configuration. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `EXISTING_CONFIG` |  |  |
| `SRC_CONFIG` |  |  |
| `logger` |  |  |

## EXISTING\_CONFIG

```python
EXISTING_CONFIG = 'EXISTING_CONFIG'
```

## SRC\_CONFIG

```python
SRC_CONFIG = 'src_config'
```

## logger

```python
logger = logging.getLogger(__name__)
```

## IntroPage

```python
IntroPage(model: Microscope, core: CMMCorePlus)
```

Bases: `ConfigWizardPage`

First page, for selecting new or existing configuration.

Methods:

| Name | Description |
| --- | --- |
| `initializePage` | Called to prepare the page just before it is shown. |
| `cleanupPage` | Called to reset the page's contents when the user clicks BACK. |
| `validatePage` | Validate the page when the user clicks Next or Finish. |
| `isComplete` | Called to determine whether the Next/Finish button should be enabled. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `file_edit` |  |  |
| `select_file_btn` |  |  |
| `new_btn` |  |  |
| `modify_btn` |  |  |
| `btn_group` |  |  |

### file\_edit

```python
file_edit = QLineEdit()
```

### select\_file\_btn

```python
select_file_btn = QPushButton('Browse...')
```

### new\_btn

```python
new_btn = QRadioButton('Create new configuration')
```

### modify\_btn

```python
modify_btn = QRadioButton('Modify or explore existing configuration')
```

### btn\_group

```python
btn_group = QButtonGroup(self)
```

### initializePage

```python
initializePage() -> None
```

Called to prepare the page just before it is shown.

### cleanupPage

```python
cleanupPage() -> None
```

Called to reset the page's contents when the user clicks BACK.

### validatePage

```python
validatePage() -> bool
```

Validate the page when the user clicks Next or Finish.

### isComplete

```python
isComplete() -> bool
```

Called to determine whether the Next/Finish button should be enabled.
