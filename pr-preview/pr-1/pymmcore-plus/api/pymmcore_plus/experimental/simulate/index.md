# pymmcore\_plus.experimental.simulate

Simulated microscope sample for testing and development.

This module provides tools for creating virtual microscope samples that integrate with CMMCorePlus. When a sample is installed on a core, image acquisition returns rendered images based on the sample objects and current microscope state (stage position, exposure, pixel size, etc.).

Examples:

Create a sample with some objects and use it with a core:

```pycon
>>> from pymmcore_plus import CMMCorePlus
>>> from pymmcore_plus.experimental.simulate import (
...     Sample,
...     Point,
...     Line,
...     Rectangle,
...     RenderConfig,
... )
>>>
>>> # Create core and load config
>>> core = CMMCorePlus.instance()
>>> core.loadSystemConfiguration()
>>>
>>> # Define sample objects (coordinates in microns)
>>> sample = Sample(
...     [
...         Point(0, 0, intensity=200, radius=5),
...         Point(50, 50, intensity=150, radius=3),
...         Line((0, 0), (100, 100), intensity=100),
...         Rectangle((20, 20), width=30, height=20, intensity=180, fill=True),
...     ]
... )
>>>
>>> # Use as context manager
>>> with sample.patch(core):
...     core.snapImage()
...     img = core.getImage()  # Returns rendered simulation
...     print(img.shape, img.dtype)
```

Custom render configuration:

```pycon
>>> config = RenderConfig(
...     noise_std=5.0,  # More noise
...     defocus_scale=0.2,  # More blur with Z
...     shot_noise=False,  # Disable shot noise
...     bit_depth=16,  # 16-bit output
... )
>>> sample = Sample([Point(0, 0)], config=config)
```

Manual install/uninstall:

```pycon
>>> sample.install(core)
>>> # ... do stuff ...
>>> sample.uninstall()
```

Classes:

| Name | Description |
| --- | --- |
| `Arc` | An arc (partial ellipse outline) in the sample. |
| `Bitmap` | A bitmap image placed in the sample. |
| `Ellipse` | An ellipse in the sample. |
| `Line` | A line segment in the sample. |
| `Point` | A circular point/spot in the sample. |
| `Polygon` | A polygon in the sample. |
| `Rectangle` | A rectangle in the sample. |
| `RegularPolygon` | A regular polygon inscribed in a circle. |
| `RenderConfig` | Configuration for the rendering engine. |
| `Sample` | A simulated microscope sample that integrates with CMMCorePlus. |
| `SampleObject` | Base class for drawable sample objects. |

Functions:

| Name | Description |
| --- | --- |
| `rects_intersect` | Check if two rectangles intersect. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `Bounds` | `TypeAlias` |  |

## Bounds

```python
Bounds: TypeAlias = tuple[float, float, float, float]
```

## Arc

```python
Arc(
    center: tuple[float, float],
    rx: float,
    ry: float,
    start_angle: float,
    end_angle: float,
    intensity: int = 255,
    width: int = 1,
)
```

Bases: `SampleObject`

An arc (partial ellipse outline) in the sample.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `center` | `tuple[float, float]` | Center (x, y) in world units. | *required* |
| `rx` | `float` | X radius in world units. | *required* |
| `ry` | `float` | Y radius in world units. | *required* |
| `start_angle` | `float` | Start angle in degrees. | *required* |
| `end_angle` | `float` | End angle in degrees. | *required* |
| `intensity` | `int` | Brightness value (0-255). Default 255. | `255` |
| `width` | `int` | Arc width in pixels. Default 1. | `1` |

Methods:

| Name | Description |
| --- | --- |
| `draw` |  |
| `draw_cv2` |  |
| `get_bounds` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `center` | `tuple[float, float]` |  |
| `rx` | `float` |  |
| `ry` | `float` |  |
| `start_angle` | `float` |  |
| `end_angle` | `float` |  |
| `intensity` | `int` |  |
| `width` | `int` |  |

### center

```python
center: tuple[float, float]
```

### rx

```python
rx: float
```

### ry

```python
ry: float
```

### start\_angle

```python
start_angle: float
```

### end\_angle

```python
end_angle: float
```

### intensity

```python
intensity: int = 255
```

### width

```python
width: int = 1
```

### draw

```python
draw(draw_context: ImageDraw, transform: TransformFn, scale: float) -> None
```

### draw\_cv2

```python
draw_cv2(img: ndarray, transform: TransformFn, scale: float) -> None
```

### get\_bounds

```python
get_bounds() -> Bounds
```

## Bitmap

```python
Bitmap(
    top_left: tuple[float, float],
    data: ndarray | Image | str,
    bitmap_scale: float = 1.0,
)
```

Bases: `SampleObject`

A bitmap image placed in the sample.

The bitmap is placed at a fixed position and scale in world coordinates. Each pixel of the bitmap corresponds to one world unit.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `top_left` | `tuple[float, float]` | Top-left corner (x, y) in world units. | *required* |
| `data` | `ndarray \| Image \| str` | Image data as numpy array, PIL Image, or path to image file. | *required* |
| `bitmap_scale` | `float` | World units per bitmap pixel. Default 1.0 (1 pixel = 1 world unit). | `1.0` |

Methods:

| Name | Description |
| --- | --- |
| `draw` |  |
| `get_bounds` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `top_left` | `tuple[float, float]` |  |
| `data` | `ndarray \| Image \| str` |  |
| `bitmap_scale` | `float` |  |

### top\_left

```python
top_left: tuple[float, float]
```

### data

```python
data: ndarray | Image | str
```

### bitmap\_scale

```python
bitmap_scale: float = 1.0
```

### draw

```python
draw(draw_context: ImageDraw, transform: TransformFn, scale: float) -> None
```

### get\_bounds

```python
get_bounds() -> Bounds
```

## Ellipse

```python
Ellipse(
    center: tuple[float, float],
    rx: float,
    ry: float,
    intensity: int = 255,
    fill: bool = False,
    width: int = 1,
)
```

Bases: `SampleObject`

An ellipse in the sample.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `center` | `tuple[float, float]` | Center (x, y) in world units. | *required* |
| `rx` | `float` | X radius in world units. | *required* |
| `ry` | `float` | Y radius in world units. | *required* |
| `intensity` | `int` | Brightness value (0-255). Default 255. | `255` |
| `fill` | `bool` | If True, fill the ellipse. If False, draw outline only. Default False. | `False` |
| `width` | `int` | Outline width in pixels (only used if fill=False). Default 1. | `1` |

Methods:

| Name | Description |
| --- | --- |
| `draw` |  |
| `draw_cv2` |  |
| `get_bounds` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `center` | `tuple[float, float]` |  |
| `rx` | `float` |  |
| `ry` | `float` |  |
| `intensity` | `int` |  |
| `fill` | `bool` |  |
| `width` | `int` |  |

### center

```python
center: tuple[float, float]
```

### rx

```python
rx: float
```

### ry

```python
ry: float
```

### intensity

```python
intensity: int = 255
```

### fill

```python
fill: bool = False
```

### width

```python
width: int = 1
```

### draw

```python
draw(draw_context: ImageDraw, transform: TransformFn, scale: float) -> None
```

### draw\_cv2

```python
draw_cv2(img: ndarray, transform: TransformFn, scale: float) -> None
```

### get\_bounds

```python
get_bounds() -> Bounds
```

## Line

```python
Line(
    start: tuple[float, float],
    end: tuple[float, float],
    intensity: int = 255,
    width: int = 1,
)
```

Bases: `SampleObject`

A line segment in the sample.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `start` | `tuple[float, float]` | Start point (x, y) in world units. | *required* |
| `end` | `tuple[float, float]` | End point (x, y) in world units. | *required* |
| `intensity` | `int` | Brightness value (0-255). Default 255. | `255` |
| `width` | `int` | Line width in pixels. Default 1. | `1` |

Methods:

| Name | Description |
| --- | --- |
| `draw` |  |
| `draw_cv2` |  |
| `get_bounds` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `start` | `tuple[float, float]` |  |
| `end` | `tuple[float, float]` |  |
| `intensity` | `int` |  |
| `width` | `int` |  |

### start

```python
start: tuple[float, float]
```

### end

```python
end: tuple[float, float]
```

### intensity

```python
intensity: int = 255
```

### width

```python
width: int = 1
```

### draw

```python
draw(draw_context: ImageDraw, transform: TransformFn, scale: float) -> None
```

### draw\_cv2

```python
draw_cv2(img: ndarray, transform: TransformFn, scale: float) -> None
```

### get\_bounds

```python
get_bounds() -> Bounds
```

## Point

```python
Point(x: float, y: float, intensity: int = 255, radius: float = 2.0)
```

Bases: `SampleObject`

A circular point/spot in the sample.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `x` | `float` | X coordinate in world units. | *required* |
| `y` | `float` | Y coordinate in world units. | *required* |
| `intensity` | `int` | Brightness value (0-255). Default 255. | `255` |
| `radius` | `float` | Radius in world units. Default 2.0. | `2.0` |

Methods:

| Name | Description |
| --- | --- |
| `draw` |  |
| `draw_cv2` |  |
| `get_bounds` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `x` | `float` |  |
| `y` | `float` |  |
| `intensity` | `int` |  |
| `radius` | `float` |  |

### x

```python
x: float
```

### y

```python
y: float
```

### intensity

```python
intensity: int = 255
```

### radius

```python
radius: float = 2.0
```

### draw

```python
draw(draw_context: ImageDraw, transform: TransformFn, scale: float) -> None
```

### draw\_cv2

```python
draw_cv2(img: ndarray, transform: TransformFn, scale: float) -> None
```

### get\_bounds

```python
get_bounds() -> Bounds
```

## Polygon

```python
Polygon(
    vertices: Sequence[tuple[float, float]],
    intensity: int = 255,
    fill: bool = False,
    width: int = 1,
)
```

Bases: `SampleObject`

A polygon in the sample.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `vertices` | `Sequence[tuple[float, float]]` | List of (x, y) vertices in world units. | *required* |
| `intensity` | `int` | Brightness value (0-255). Default 255. | `255` |
| `fill` | `bool` | If True, fill the polygon. Default False. | `False` |
| `width` | `int` | Outline width in pixels (only used if fill=False). Default 1. | `1` |

Methods:

| Name | Description |
| --- | --- |
| `draw` |  |
| `draw_cv2` |  |
| `get_bounds` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `vertices` | `Sequence[tuple[float, float]]` |  |
| `intensity` | `int` |  |
| `fill` | `bool` |  |
| `width` | `int` |  |

### vertices

```python
vertices: Sequence[tuple[float, float]]
```

### intensity

```python
intensity: int = 255
```

### fill

```python
fill: bool = False
```

### width

```python
width: int = 1
```

### draw

```python
draw(draw_context: ImageDraw, transform: TransformFn, scale: float) -> None
```

### draw\_cv2

```python
draw_cv2(img: ndarray, transform: TransformFn, scale: float) -> None
```

### get\_bounds

```python
get_bounds() -> Bounds
```

## Rectangle

```python
Rectangle(
    top_left: tuple[float, float],
    width: float,
    height: float,
    intensity: int = 255,
    fill: bool = False,
    corner_radius: float = 0,
    line_width: int = 1,
)
```

Bases: `SampleObject`

A rectangle in the sample.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `top_left` | `tuple[float, float]` | Top-left corner (x, y) in world units. | *required* |
| `width` | `float` | Width in world units. | *required* |
| `height` | `float` | Height in world units. | *required* |
| `intensity` | `int` | Brightness value (0-255). Default 255. | `255` |
| `fill` | `bool` | If True, fill the rectangle. If False, draw outline only. Default False. | `False` |
| `corner_radius` | `float` | Corner radius for rounded rectangles, in world units. Default 0. | `0` |
| `line_width` | `int` | Outline width in pixels (only used if fill=False). Default 1. | `1` |

Methods:

| Name | Description |
| --- | --- |
| `draw` |  |
| `draw_cv2` |  |
| `get_bounds` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `top_left` | `tuple[float, float]` |  |
| `width` | `float` |  |
| `height` | `float` |  |
| `intensity` | `int` |  |
| `fill` | `bool` |  |
| `corner_radius` | `float` |  |
| `line_width` | `int` |  |
| `bottom_right` | `tuple[float, float]` | Bottom-right corner coordinates. |

### top\_left

```python
top_left: tuple[float, float]
```

### width

```python
width: float
```

### height

```python
height: float
```

### intensity

```python
intensity: int = 255
```

### fill

```python
fill: bool = False
```

### corner\_radius

```python
corner_radius: float = 0
```

### line\_width

```python
line_width: int = 1
```

### bottom\_right

```python
bottom_right: tuple[float, float]
```

Bottom-right corner coordinates.

### draw

```python
draw(draw_context: ImageDraw, transform: TransformFn, scale: float) -> None
```

### draw\_cv2

```python
draw_cv2(img: ndarray, transform: TransformFn, scale: float) -> None
```

### get\_bounds

```python
get_bounds() -> Bounds
```

## RegularPolygon

```python
RegularPolygon(
    center: tuple[float, float],
    radius: float,
    n_sides: int,
    rotation: float = 0,
    intensity: int = 255,
    fill: bool = False,
    width: int = 1,
    _vertices: list[tuple[float, float]] = list(),
)
```

Bases: `SampleObject`

A regular polygon inscribed in a circle.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `center` | `tuple[float, float]` | Center (x, y) in world units. | *required* |
| `radius` | `float` | Radius of bounding circle in world units. | *required* |
| `n_sides` | `int` | Number of sides. | *required* |
| `rotation` | `float` | Rotation angle in degrees. Default 0. | `0` |
| `intensity` | `int` | Brightness value (0-255). Default 255. | `255` |
| `fill` | `bool` | If True, fill the polygon. Default False. | `False` |
| `width` | `int` | Outline width in pixels (only used if fill=False). Default 1. | `1` |

Methods:

| Name | Description |
| --- | --- |
| `draw` |  |
| `draw_cv2` |  |
| `get_bounds` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `center` | `tuple[float, float]` |  |
| `radius` | `float` |  |
| `n_sides` | `int` |  |
| `rotation` | `float` |  |
| `intensity` | `int` |  |
| `fill` | `bool` |  |
| `width` | `int` |  |

### center

```python
center: tuple[float, float]
```

### radius

```python
radius: float
```

### n\_sides

```python
n_sides: int
```

### rotation

```python
rotation: float = 0
```

### intensity

```python
intensity: int = 255
```

### fill

```python
fill: bool = False
```

### width

```python
width: int = 1
```

### draw

```python
draw(draw_context: ImageDraw, transform: TransformFn, scale: float) -> None
```

### draw\_cv2

```python
draw_cv2(img: ndarray, transform: TransformFn, scale: float) -> None
```

### get\_bounds

```python
get_bounds() -> Bounds
```

## RenderConfig

```python
RenderConfig(
    shot_noise: bool = True,
    defocus_scale: float = 0.125,
    base_blur: float = 1.5,
    random_seed: int | None = None,
    backend: Backend = "auto",
)
```

Configuration for the rendering engine.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `shot_noise` | `bool` | Whether to apply Poisson (shot) noise. Default True. | `True` |
| `defocus_scale` | `float` | Blur radius per unit of Z distance from focus. Default 0.125. blur\_radius = base\_blur + abs(z) \* defocus\_scale | `0.125` |
| `base_blur` | `float` | Minimum blur radius (at perfect focus). Default 1.0. | `1.5` |
| `random_seed` | `int \| None` | Random seed for reproducible noise. Default None (random). | `None` |
| `backend` | `Backend` | Rendering backend: "auto" (default), "pil", or "cv2". "auto" uses cv2 if available, otherwise PIL. "cv2" raises ImportError if opencv-python is not installed. | `'auto'` |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `shot_noise` | `bool` |  |
| `defocus_scale` | `float` |  |
| `base_blur` | `float` |  |
| `random_seed` | `int \| None` |  |
| `backend` | `Backend` |  |

### shot\_noise

```python
shot_noise: bool = True
```

### defocus\_scale

```python
defocus_scale: float = 0.125
```

### base\_blur

```python
base_blur: float = 1.5
```

### random\_seed

```python
random_seed: int | None = None
```

### backend

```python
backend: Backend = 'auto'
```

## Sample

```python
Sample(objects: Iterable[SampleObject], config: RenderConfig | None = None)
```

A simulated microscope sample that integrates with CMMCorePlus.

Use `sample.patch(core)` as a context manager to intercept image acquisition calls and return rendered images based on microscope state.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `objects` | `Iterable[SampleObject]` | Sample objects to render (points, lines, shapes, etc.). | *required* |
| `config` | `RenderConfig \| None` | Rendering configuration. If None, uses default config. | `None` |

Methods:

| Name | Description |
| --- | --- |
| `render` | Render the sample for the given microscope state. |
| `patch` | Patch the core to use this sample for image generation. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `objects` | `list[SampleObject]` | List of sample objects. |
| `config` | `RenderConfig` | Rendering configuration. |

### objects

```python
objects: list[SampleObject]
```

List of sample objects.

### config

```python
config: RenderConfig
```

Rendering configuration.

### render

```python
render(state: SummaryMetaV1) -> ndarray
```

Render the sample for the given microscope state.

### patch

```python
patch(core: CMMCorePlus) -> Generator[Sample, None, None]
```

Patch the core to use this sample for image generation.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `core` | `CMMCorePlus` | The core instance to patch. | *required* |

Yields:

| Type | Description |
| --- | --- |
| `Sample` | This sample instance. |

## SampleObject

Bases: `ABC`

Base class for drawable sample objects.

All coordinates are in world-space (typically microns). Objects are rendered by calling `draw()` with a transform function that converts world coordinates to pixel coordinates.

Subclasses must implement: - `draw()`: Render the object onto a PIL ImageDraw context - `get_bounds()`: Return the bounding box in world coordinates - `intensity`: Property returning the object's intensity value

Methods:

| Name | Description |
| --- | --- |
| `draw` | Draw this object onto the given context. |
| `get_bounds` | Return bounding box in world coordinates. |
| `draw_cv2` | Draw this object using OpenCV (optional, for performance). |
| `should_draw` | Check if this object intersects the field of view. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `intensity` | `int` |  |

### intensity

```python
intensity: int
```

### draw

```python
draw(draw_context: ImageDraw, transform: TransformFn, scale: float) -> None
```

Draw this object onto the given context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `draw_context` | `ImageDraw` | PIL ImageDraw context to draw on. | *required* |
| `transform` | `TransformFn` | Function to convert (world\_x, world\_y) to (pixel\_x, pixel\_y). | *required* |
| `scale` | `float` | Pixels per world unit (e.g., pixels per micron). | *required* |

### get\_bounds

```python
get_bounds() -> Bounds
```

Return bounding box in world coordinates.

Returns:

| Type | Description |
| --- | --- |
| `Bounds` | Tuple of (left, top, right, bottom) in world units. |

### draw\_cv2

```python
draw_cv2(img: ndarray, transform: TransformFn, scale: float) -> None
```

Draw this object using OpenCV (optional, for performance).

Default implementation falls back to PIL via a temporary image. Subclasses can override for better performance.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `img` | `ndarray` | Image array to draw on (modified in-place). | *required* |
| `transform` | `TransformFn` | Function to convert (world\_x, world\_y) to (pixel\_x, pixel\_y). | *required* |
| `scale` | `float` | Pixels per world unit. | *required* |

### should\_draw

```python
should_draw(fov_rect: Bounds) -> bool
```

Check if this object intersects the field of view.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `fov_rect` | `Bounds` | Field of view rectangle in world coordinates. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `bool` | True if object should be drawn (intersects FOV). |

## rects\_intersect

```python
rects_intersect(a: Bounds, b: Bounds) -> bool
```

Check if two rectangles intersect.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `a` | `Bounds` | First rectangle as (left, top, right, bottom). | *required* |
| `b` | `Bounds` | Second rectangle as (left, top, right, bottom). | *required* |

Returns:

| Type | Description |
| --- | --- |
| `bool` | True if rectangles intersect. |
