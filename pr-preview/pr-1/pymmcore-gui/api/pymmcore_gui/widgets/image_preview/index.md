# pymmcore\_gui.widgets.image\_preview

Classes:

| Name | Description |
| --- | --- |
| `ImagePreviewBase` |  |

## ImagePreviewBase

```python
ImagePreviewBase(
    parent: QWidget | None, mmcore: CMMCorePlus, *, use_with_mda: bool = False
)
```

Bases: `QWidget`

Methods:

| Name | Description |
| --- | --- |
| `attach` | Attach this widget to events in `core`. |
| `detach` | Detach this widget from events in `core`. |
| `append` | Set texture data. |
| `timerEvent` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `use_with_mda` |  |  |

### use\_with\_mda

```python
use_with_mda = use_with_mda
```

### attach

```python
attach(core: CMMCorePlus) -> None
```

Attach this widget to events in `core`.

### detach

```python
detach() -> None
```

Detach this widget from events in `core`.

### append

```python
append(data: ndarray) -> None
```

Set texture data.

The dtype must be compatible with wgpu texture formats. Will also apply contrast limits if \_clims is "auto".

### timerEvent

```python
timerEvent(a0: QTimerEvent) -> None
```
