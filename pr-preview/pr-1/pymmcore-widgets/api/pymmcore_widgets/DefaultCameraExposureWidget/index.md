# DefaultCameraExposureWidget

Screenshot generated from the [example below](<#example>).

Bases: `ExposureWidget`

A Widget to get/set exposure on the default camera.

Parameters:

<table>       <thead>         <tr>           <th>Name</th>           <th>Type</th>           <th>Description</th>           <th>Default</th>         </tr>       </thead>       <tbody>           <tr class="doc-section-item">             <td>                 <code>parent</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_widgets.DefaultCameraExposureWidget" backlink-type="used-by" hover="" identifier="qtpy.QtWidgets.QWidget" optional="">QWidget</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                 <div class="language-text highlight"><pre><span></span><code>Optional parent widget. By default, None.&#10;</code></pre></div>                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>mmcore</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_widgets.DefaultCameraExposureWidget" backlink-type="used-by" hover="" identifier="pymmcore_plus.CMMCorePlus" optional="">CMMCorePlus</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                 <p>Optional <autoref data-zensical-autoref="" domain="py" filepath="/Users/runner/work/pymmcore-plus.github.io/pymmcore-plus.github.io/.repos/pymmcore-widgets/src/pymmcore_widgets/control/_exposure_widget.py" identifier="pymmcore_plus.CMMCorePlus" lineno="103" origin="pymmcore_widgets.DefaultCameraExposureWidget" role="class"><code>pymmcore_plus.CMMCorePlus</code></autoref> micromanager core. By default, None. If not specified, the widget will use the active (or create a new) <autoref data-zensical-autoref="" domain="py" filepath="/Users/runner/work/pymmcore-plus.github.io/pymmcore-plus.github.io/.repos/pymmcore-widgets/src/pymmcore_widgets/control/_exposure_widget.py" identifier="pymmcore_plus.core._mmcore_plus.CMMCorePlus.instance" lineno="103" origin="pymmcore_widgets.DefaultCameraExposureWidget" role="class"><code>CMMCorePlus.instance</code></autoref>.</p>                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>       </tbody>     </table>

Methods:

| Name | Description |
| --- | --- |
| `setCamera` | Set which camera this widget tracks. |

## setCamera

```python
setCamera(camera: str | None = None, force: bool = False) -> None
```

Set which camera this widget tracks.

Using this on the `DefaultCameraExposureWidget`widget may cause unexpected behavior, instead try to use an `ExposureWidget`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `camera` | `str` | The camera device label. By default, None. If not specified, the widget will use the current Camera device. | `None` |
| `force` | `bool` | Whether to force a change away from tracking the default camera. | `False` |

## Example

examples/default\_camera\_exposure\_widget.py

```python
from pymmcore_plus import CMMCorePlus
from qtpy.QtWidgets import QApplication

from pymmcore_widgets import DefaultCameraExposureWidget

app = QApplication([])

mmc = CMMCorePlus().instance()
mmc.loadSystemConfiguration()

exp_wdg = DefaultCameraExposureWidget()
exp_wdg.show()

app.exec()
```
