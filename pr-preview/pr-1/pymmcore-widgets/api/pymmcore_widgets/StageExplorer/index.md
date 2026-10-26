# StageExplorer

Screenshot generated from the [example below](<#example>).

Bases: `QWidget`

A stage positions explorer widget.

This widget provides a visual representation of the stage positions. The user can interact with the stage positions by panning and zooming the view. The user can also move the stage to a specific position (and, optionally, snap an image) by double-clicking on the view.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `parent` | `QWidget \| None` | Optional parent widget, by default None. | `None` |
| `mmcore` | `CMMCorePlus \| None` | Optional `CMMCorePlus` micromanager core. By default, None. If not specified, the widget will use the active (or create a new) `CMMCorePlus.instance`. | `None` |

**Properties**

auto\_zoom\_to\_fit : bool A boolean property that controls whether to automatically "zoom to fit" the view when a new image is added to the scene or when the position of the stage marker (if enabled) is out of view. By default, False. By default, False. snap\_on\_double\_click : bool A boolean property that controls whether to snap an image when the user double-clicks on the view. By default, False. poll\_stage\_position : bool A boolean property that controls whether to poll the stage position. If True, the widget will poll the stage position and display a rectangle around the current stage position. By default, False.

Methods:

| Name | Description |
| --- | --- |
| `closeEvent` |  |
| `toolBar` | Return the toolbar of the widget. |
| `add_image` | Add an image to the scene at a give (x, y) stage position in microns. |
| `zoom_to_fit` | Zoom to fit the current view to the images in the scene. |
| `keyPressEvent` |  |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `roi_manager` |  |  |
| `auto_zoom_to_fit` | `bool` | Whether to automatically zoom to fit the full scene in the view. |
| `snap_on_double_click` | `bool` | Whether to snap an image on double click. |
| `poll_stage_position` | `bool` | Whether to continually show the current stage position. |

## roi\_manager

```python
roi_manager = SceneROIManager(self._stage_viewer.canvas)
```

## auto\_zoom\_to\_fit

```python
auto_zoom_to_fit: bool
```

Whether to automatically zoom to fit the full scene in the view.

When True, the view will automatically zoom to fit the full scene when a new image is added or when the stage position marker moves out of view.

## snap\_on\_double\_click

```python
snap_on_double_click: bool
```

Whether to snap an image on double click.

When True, the widget will snap an image when the user double-clicks on the view, after the stage has moved to the clicked position.

## poll\_stage\_position

```python
poll_stage_position: bool
```

Whether to continually show the current stage position.

## closeEvent

```python
closeEvent(a0: QCloseEvent | None) -> None
```

## toolBar

```python
toolBar() -> StageExplorerToolbar
```

Return the toolbar of the widget.

## add\_image

```python
add_image(image: ndarray, stage_x_um: float, stage_y_um: float) -> None
```

Add an image to the scene at a give (x, y) stage position in microns.

## zoom\_to\_fit

```python
zoom_to_fit(*, margin: float = 0.05) -> None
```

Zoom to fit the current view to the images in the scene.

...also considering the stage position marker.

## keyPressEvent

```python
keyPressEvent(a0: QKeyEvent | None) -> None
```

## Example

examples/stage\_explorer\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtCore import QModelIndex
from qtpy.QtWidgets import QApplication, QHBoxLayout, QSplitter, QVBoxLayout, QWidget

from pymmcore_widgets import (
    CameraRoiWidget,
    GroupPresetTableWidget,
    MDAWidget,
    StageExplorer,
    StageWidget,
)

app = QApplication([])

mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()
mmc.setProperty("Camera", "BitDepth", "12")

# set camera roi (rectangular helps confirm orientation)
mmc.setROI(0, 0, 600, 400)

xy = mmc.getXYStageDevice()
if mmc.hasProperty(xy, "Velocity"):
    mmc.setProperty(xy, "Velocity", 2)

explorer = StageExplorer()
stage_ctrl = StageWidget(mmc.getXYStageDevice())
stage_ctrl.setStep(512)
stage_ctrl.snap_checkbox.setChecked(True)

z_ctrl = StageWidget(mmc.getFocusDevice())
z_ctrl.snap_checkbox.setChecked(True)

mda_widget = MDAWidget()
group_wdg = GroupPresetTableWidget()
cam_roi = CameraRoiWidget()


# As an example...
# When ROIs are edited or destroyed, update the MDA widget's stage positions.
def _on_data_changed(top_left: QModelIndex, bottom_right: QModelIndex) -> None:
    mgr = explorer.roi_manager
    positions = [
        roi.create_useq_position(overlap=mgr.scan_overlap, mode=mgr.scan_mode)
        for roi in mgr.all_rois()
    ]
    # optional: skip positions that don't actually have a valid sequence (grid plan)
    positions = [pos for pos in positions if pos.sequence is not None]
    mda_widget.stage_positions.setValue(positions)


model = explorer.roi_manager.roi_model
model.dataChanged.connect(_on_data_changed)
model.rowsRemoved.connect(_on_data_changed)


# layout

splitter = QSplitter()
left = QWidget()
llayout = QVBoxLayout(left)
llayout.addWidget(group_wdg)
llayout.addWidget(cam_roi)
splitter.addWidget(left)
splitter.addWidget(explorer)
right = QWidget()
rlayout = QVBoxLayout(right)
rtop = QHBoxLayout()
rtop.addWidget(stage_ctrl)
rtop.addWidget(z_ctrl)
rlayout.addLayout(rtop)
rlayout.addWidget(mda_widget)
splitter.addWidget(right)
splitter.show()

app.exec()
```
