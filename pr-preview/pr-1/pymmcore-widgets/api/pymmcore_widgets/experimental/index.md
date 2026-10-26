# pymmcore\_widgets.experimental

Experimental widgets.

Classes:

| Name | Description |
| --- | --- |
| `StackViewer` | A viewer for MDA acquisitions started by MDASequence in pymmcore-plus events. |

## StackViewer

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

Methods:

| Name | Description |
| --- | --- |
| `construct_canvas` |  |
| `add_slider` |  |
| `add_image` |  |
| `sequenceStarted` | Sequence started by the mmcore. Adjust our settings, make layers etc. |
| `frameReady` | Frame received from acquisition, display the image, update sliders etc. |
| `on_mouse_move` | Mouse moved on the canvas, display the pixel value and position. |
| `on_display_timer` | Update display, usually triggered by QTimer started by slider click. |
| `display_image` |  |
| `on_clim_timer` |  |
| `closeEvent` | Write window size and position to config file. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `sequence` |  |  |
| `canvas_size` |  |  |
| `transform` |  |  |
| `cmaps` |  |  |
| `display_index` |  |  |
| `main_layout` |  |  |
| `info_bar` |  |  |
| `datastore` |  |  |
| `images` | `dict[tuple, Image]` |  |
| `frame` |  |  |
| `ready` |  |  |
| `current_channel` |  |  |
| `pixel_size` |  |  |
| `missed_events` | `list[MDAEvent]` |  |
| `collapse_btn` |  |  |
| `bottom_buttons` |  |  |
| `save_btn` |  |  |

### sequence

```python
sequence = sequence
```

### canvas\_size

```python
canvas_size = size
```

### transform

```python
transform = transform
```

### cmaps

```python
cmaps = [
    cm
    for x in self.cmap_names
    if (cm := try_cast_colormap(x)) is not None
]
```

### display\_index

```python
display_index = dict.fromkeys(DIMENSIONS, 0)
```

### main\_layout

```python
main_layout = QtWidgets.QVBoxLayout()
```

### info\_bar

```python
info_bar = QtWidgets.QLabel()
```

### datastore

```python
datastore = datastore or QOMEZarrDatastore()
```

### images

```python
images: dict[tuple, Image] = {}
```

### frame

```python
frame = 0
```

### ready

```python
ready = False
```

### current\_channel

```python
current_channel = 0
```

### pixel\_size

```python
pixel_size = 1.0
```

### missed\_events

```python
missed_events: list[MDAEvent] = []
```

### collapse\_btn

```python
collapse_btn = QtWidgets.QPushButton()
```

### bottom\_buttons

```python
bottom_buttons = QtWidgets.QHBoxLayout()
```

### save\_btn

```python
save_btn = SaveButton(self.datastore)
```

### construct\_canvas

```python
construct_canvas() -> None
```

### add\_slider

```python
add_slider(dim: str) -> None
```

### add\_image

```python
add_image(event: MDAEvent) -> None
```

### sequenceStarted

```python
sequenceStarted(sequence: MDASequence) -> None
```

Sequence started by the mmcore. Adjust our settings, make layers etc.

### frameReady

```python
frameReady(event: MDAEvent) -> None
```

Frame received from acquisition, display the image, update sliders etc.

### on\_mouse\_move

```python
on_mouse_move(event: SceneMouseEvent) -> None
```

Mouse moved on the canvas, display the pixel value and position.

### on\_display\_timer

```python
on_display_timer() -> None
```

Update display, usually triggered by QTimer started by slider click.

### display\_image

```python
display_image(img: ndarray, channel: int = 0, grid: int = 0) -> None
```

### on\_clim\_timer

```python
on_clim_timer(channel: int | None = None) -> None
```

### closeEvent

```python
closeEvent(e: QCloseEvent) -> None
```

Write window size and position to config file.
