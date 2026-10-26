# pymmcore\_widgets.hcwizard.finish\_page

Classes:

| Name | Description |
| --- | --- |
| `FinishPage` | Page for saving the configuration file. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `DEST_CONFIG` |  |  |

## DEST\_CONFIG

```python
DEST_CONFIG = 'dest_config'
```

## FinishPage

```python
FinishPage(model: Microscope, core: CMMCorePlus)
```

Bases: `ConfigWizardPage`

Page for saving the configuration file.

Methods:

| Name | Description |
| --- | --- |
| `initializePage` | Called to prepare the page just before it is shown. |
| `validatePage` | Validate. the page when the user clicks Next or Finish. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `file_edit` |  |  |
| `select_file_btn` |  |  |

### file\_edit

```python
file_edit = QLineEdit()
```

### select\_file\_btn

```python
select_file_btn = QPushButton('Browse...')
```

### initializePage

```python
initializePage() -> None
```

Called to prepare the page just before it is shown.

### validatePage

```python
validatePage() -> bool
```

Validate. the page when the user clicks Next or Finish.
