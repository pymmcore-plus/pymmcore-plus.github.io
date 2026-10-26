# pymmcore\_widgets.hcwizard.roles\_page

Classes:

| Name | Description |
| --- | --- |
| `RolesPage` | Page for selecting default devices and auto-shutter setting. |

## RolesPage

```python
RolesPage(model: Microscope, core: CMMCorePlus)
```

Bases: `ConfigWizardPage`

Page for selecting default devices and auto-shutter setting.

Methods:

| Name | Description |
| --- | --- |
| `initializePage` | Called to prepare the page just before it is shown. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `camera_combo` |  |  |
| `shutter_combo` |  |  |
| `focus_combo` |  |  |
| `auto_shutter_checkbox` |  |  |

### camera\_combo

```python
camera_combo = QComboBox()
```

### shutter\_combo

```python
shutter_combo = QComboBox()
```

### focus\_combo

```python
focus_combo = QComboBox()
```

### auto\_shutter\_checkbox

```python
auto_shutter_checkbox = QCheckBox()
```

### initializePage

```python
initializePage() -> None
```

Called to prepare the page just before it is shown.
