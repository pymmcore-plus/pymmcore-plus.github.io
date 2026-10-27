# pymmcore\_gui.widgets.image\_preview

The image preview: what a snap, live mode or an MDA shows.

**Classes**

| Name | Description |
| --- | --- |
| `ImagePreviewBase` |  |

## Classes

### ImagePreviewBase

```python
ImagePreviewBase(
    parent: QWidget | None, mmcore: CMMCorePlus, *, use_with_mda: bool = False
)
```

Bases: `QWidget`

#### attach

```python
attach(core: CMMCorePlus) -> None
```

Attach this widget to events in `core`.

#### detach

```python
detach() -> None
```

Detach this widget from events in `core`.

#### append

```python
append(data: ndarray) -> None
```

Set texture data.

The dtype must be compatible with wgpu texture formats. Will also apply contrast limits if \_clims is "auto".

#### timerEvent

```python
timerEvent(a0: QTimerEvent) -> None
```
