# pymmcore\_widgets.hcwizard.delay\_page

Classes:

| Name | Description |
| --- | --- |
| `DelayPage` | Page for setting device delays. |
| `DelayTable` | Simple Property Table. |

## DelayPage

```python
DelayPage(model: Microscope, core: CMMCorePlus)
```

Bases: `ConfigWizardPage`

Page for setting device delays.

Methods:

| Name | Description |
| --- | --- |
| `initializePage` | Called to prepare the page just before it is shown. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `delays_table` |  |  |

### delays\_table

```python
delays_table = DelayTable(self._model)
```

### initializePage

```python
initializePage() -> None
```

Called to prepare the page just before it is shown.

## DelayTable

```python
DelayTable(model: Microscope, parent: QWidget | None = None)
```

Bases: `QTableWidget`

Simple Property Table.

Methods:

| Name | Description |
| --- | --- |
| `rebuild` | Rebuild the table for the given device and prop\_names. |

### rebuild

```python
rebuild() -> None
```

Rebuild the table for the given device and prop\_names.
