# pymmcore\_widgets.experimental

Experimental widgets.

**Classes**

| Name | Description |
| --- | --- |
| `StackViewer` | A viewer for MDA acquisitions started by MDASequence in pymmcore-plus events. |

## Classes

### StackViewer

```python
StackViewer(
    datastore: QOMEZarrDatastore | None = None,
    sequence: MDASequence | None = None,
    mmcore: CMMCorePlus | None = None,
    parent: QWidget | None = None,
    size: tuple[int, int] | None = None,
    transform: tuple[int, bool, bool] = (0, True, False),
    save_button: bool = True,
)
```

Bases: `QWidget`

A viewer for MDA acquisitions started by MDASequence in pymmcore-plus events.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `transform` | `tuple[int, bool, bool]` |  | `(0, True, False)` |

#### construct\_canvas

```python
construct_canvas() -> None
```

#### add\_slider

```python
add_slider(dim: str) -> None
```

#### add\_image

```python
add_image(event: MDAEvent) -> None
```

#### sequenceStarted

```python
sequenceStarted(sequence: MDASequence) -> None
```

Sequence started by the mmcore. Adjust our settings, make layers etc.

#### frameReady

```python
frameReady(event: MDAEvent) -> None
```

Frame received from acquisition, display the image, update sliders etc.

#### on\_mouse\_move

```python
on_mouse_move(event: SceneMouseEvent) -> None
```

Mouse moved on the canvas, display the pixel value and position.

#### on\_display\_timer

```python
on_display_timer() -> None
```

Update display, usually triggered by QTimer started by slider click.

#### display\_image

```python
display_image(img: ndarray, channel: int = 0, grid: int = 0) -> None
```

#### on\_clim\_timer

```python
on_clim_timer(channel: int | None = None) -> None
```

#### closeEvent

```python
closeEvent(e: QCloseEvent) -> None
```

Write window size and position to config file.
