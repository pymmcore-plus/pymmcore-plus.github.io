# pymmcore\_widgets.hcwizard.delay\_page

Config wizard, step 4: set delays for devices that can't report when they're done.

**Classes**

| Name | Description |
| --- | --- |
| `DelayPage` | Page for setting device delays. |
| `DelayTable` | Simple Property Table. |

## Classes

### DelayTable

```python
DelayTable(model: Microscope, parent: QWidget | None = None)
```

Bases: `QTableWidget`

Simple Property Table.

#### rebuild

```python
rebuild() -> None
```

Rebuild the table for the given device and prop\_names.

### DelayPage

```python
DelayPage(model: Microscope, core: CMMCorePlus)
```

Bases: `ConfigWizardPage`

Page for setting device delays.

#### initializePage

```python
initializePage() -> None
```

Called to prepare the page just before it is shown.
