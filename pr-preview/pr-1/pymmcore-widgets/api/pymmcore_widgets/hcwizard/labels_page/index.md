# pymmcore\_widgets.hcwizard.labels\_page

Classes:

| Name | Description |
| --- | --- |
| `LabelsPage` | Provide a table for defining position labels for state devices. |

## LabelsPage

```python
LabelsPage(model: Microscope, core: CMMCorePlus)
```

Bases: `ConfigWizardPage`

Provide a table for defining position labels for state devices.

Methods:

| Name | Description |
| --- | --- |
| `initializePage` | Called to prepare the page just before it is shown. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `labels_table` |  |  |
| `dev_combo` |  |  |

### labels\_table

```python
labels_table = _LabelTable(self._model)
```

### dev\_combo

```python
dev_combo = QComboBox()
```

### initializePage

```python
initializePage() -> None
```

Called to prepare the page just before it is shown.
