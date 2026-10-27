# pymmcore\_plus.core

`CMMCorePlus` and its supporting classes.

This includes the object-oriented views onto devices, properties and config groups, the enums that replace pymmcore's integer constants, and hardware sequencing helpers.

**Submodules**

| Name | Description |
| --- | --- |
| `events` | Signals emitted by `CMMCorePlus.events`. |

**Classes**

| Name | Description |
| --- | --- |
| `AutoFocusDevice` |  |
| `CameraDevice` |  |
| `CoreDevice` |  |
| `GalvoDevice` |  |
| `GenericDevice` |  |
| `HubDevice` |  |
| `ImageProcessorDevice` |  |
| `MagnifierDevice` |  |
| `SLMDevice` |  |
| `SequencedEvent` | Subclass of MDAEvent that represents a sequence of triggered events. |
| `SerialDevice` |  |
| `ShutterDevice` |  |
| `SignalIODevice` |  |
| `StageDevice` |  |
| `StateDevice` |  |
| `XYStageDevice` |  |

**Functions**

| Name | Description |
| --- | --- |
| `iter_sequenced_events` | Iterate over a sequence of MDAEvents, yielding SequencedEvents when possible. |

## Classes

### AutoFocusDevice

```python
AutoFocusDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Bases: `Device`

#### type

```python
type() -> Literal[AutoFocus]
```

### CameraDevice

```python
CameraDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Bases: `Device`

#### exposure

```python
exposure: float
```

#### isSequenceable

```python
isSequenceable = isExposureSequenceable
```

#### loadSequence

```python
loadSequence = loadExposureSequence
```

#### startSequence

```python
startSequence = startExposureSequence
```

#### stopSequence

```python
stopSequence = stopExposureSequence
```

#### getSequenceMaxLength

```python
getSequenceMaxLength = getExposureSequenceMaxLength
```

#### type

```python
type() -> Literal[Camera]
```

#### setROI

```python
setROI(x: int, y: int, width: int, height: int) -> None
```

Set region of interest for camera.

#### getROI

```python
getROI() -> list[int]
```

Return region of interest for camera.

#### setExposure

```python
setExposure(exposure: float) -> None
```

Set exposure time for camera.

#### getExposure

```python
getExposure() -> float
```

Return exposure time for camera.

#### startSequenceAcquisition

```python
startSequenceAcquisition(
    numImages: int, intervalMs: float, stopOnOverflow: bool
) -> None
```

Start sequence acquisition.

#### prepareSequenceAcquisition

```python
prepareSequenceAcquisition() -> None
```

Prepare sequence acquisition.

#### stopSequenceAcquisition

```python
stopSequenceAcquisition() -> None
```

Stop sequence acquisition.

#### isSequenceRunning

```python
isSequenceRunning() -> bool
```

Return `True` if sequence acquisition is running.

#### isExposureSequenceable

```python
isExposureSequenceable() -> bool
```

Return `True` if camera supports exposure sequence.

#### loadExposureSequence

```python
loadExposureSequence(sequence: Sequence[float]) -> None
```

Load exposure sequence.

#### startExposureSequence

```python
startExposureSequence() -> None
```

Start exposure sequence.

#### stopExposureSequence

```python
stopExposureSequence() -> None
```

Stop exposure sequence.

#### getExposureSequenceMaxLength

```python
getExposureSequenceMaxLength() -> int
```

Return the maximum length of a camera's exposure sequence.

### CoreDevice

```python
CoreDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Bases: `Device`

#### type

```python
type() -> Literal[Core]
```

### GalvoDevice

```python
GalvoDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Bases: `Device`

#### position

```python
position: list[float]
```

#### type

```python
type() -> Literal[Galvo]
```

#### pointAndFire

```python
pointAndFire(x: float, y: float, pulseTime_us: float) -> None
```

Set Galvo to (x, y) and fire the laser for a predetermined duration.

#### setSpotInterval

```python
setSpotInterval(pulseTime_us: float) -> None
```

Set the SpotInterval for the specified galvo device.

#### setPosition

```python
setPosition(x: float, y: float) -> None
```

Set the position of the galvo device.

#### getPosition

```python
getPosition() -> list[float]
```

Return the position of the galvo device.

#### setIlluminationState

```python
setIlluminationState(state: bool) -> None
```

Set the galvo's illumination state to on or off.

#### getXRange

```python
getXRange() -> float
```

Get the Galvo x range.

#### getXMinimum

```python
getXMinimum() -> float
```

Get the Galvo x minimum.

#### getYRange

```python
getYRange() -> float
```

Get the Galvo y range.

#### getYMinimum

```python
getYMinimum() -> float
```

Get the Galvo y minimum.

#### addPolygonVertex

```python
addPolygonVertex(polygonIndex: int, x: float, y: float) -> None
```

Add a vertex to the polygon.

#### deletePolygons

```python
deletePolygons() -> None
```

Delete all polygons.

#### loadPolygons

```python
loadPolygons() -> None
```

Load a set of galvo polygons to the device.

#### runPolygons

```python
runPolygons() -> None
```

Run a loop of galvo polygons.

#### runSequence

```python
runSequence() -> None
```

Run a sequence of galvo positions.

#### setPolygonRepetitions

```python
setPolygonRepetitions(repetitions: int) -> None
```

Set the number of times the galvo polygon should be repeated.

#### getChannel

```python
getChannel() -> str
```

Get the name of the active galvo channel (for a multi-laser galvo device).

### GenericDevice

```python
GenericDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Bases: `Device`

#### type

```python
type() -> Literal[Generic]
```

### HubDevice

```python
HubDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Bases: `Device`

#### type

```python
type() -> Literal[Hub]
```

#### getInstalledDevices

```python
getInstalledDevices() -> tuple[str, ...]
```

Return the list of installed devices.

#### getInstalledDeviceDescription

```python
getInstalledDeviceDescription(device_label: str) -> str
```

Return the description of the installed device.

#### getLoadedPeripheralDevices

```python
getLoadedPeripheralDevices() -> tuple[str, ...]
```

Return the list of loaded peripheral devices.

### ImageProcessorDevice

```python
ImageProcessorDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Bases: `Device`

#### type

```python
type() -> Literal[ImageProcessor]
```

### MagnifierDevice

```python
MagnifierDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Bases: `Device`

#### type

```python
type() -> Literal[Magnifier]
```

### SerialDevice

```python
SerialDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Bases: `Device`

#### answer\_timeout

```python
answer_timeout: str
```

Return the timeout for serial port commands.

#### baud\_rate

```python
baud_rate: str
```

Return the baud rate for serial port commands.

#### data\_bits

```python
data_bits: str
```

Return the data bits for serial port commands.

#### parity

```python
parity: str
```

Return the parity for serial port commands.

#### stop\_bits

```python
stop_bits: str
```

Return the stop bits for serial port commands.

#### handshaking

```python
handshaking: str
```

Return the handshaking for serial port commands.

#### delay\_between\_chars\_ms

```python
delay_between_chars_ms: str
```

Return the delay between characters in milliseconds.

#### type

```python
type() -> Literal[Serial]
```

#### setCommand

```python
setCommand(command: str, term: str) -> None
```

Send string to the serial device and return an answer.

#### getAnswer

```python
getAnswer(term: str) -> str
```

Continuously read from the serial port until the term is encountered.

#### write

```python
write(data: bytes) -> None
```

Send string to the serial device.

#### read

```python
read() -> list[str]
```

Reads the contents of the Rx buffer.

#### setProperties

```python
setProperties(
    answerTimeout: str,
    baudRate: str,
    delayBetweenCharsMs: str,
    handshaking: str,
    parity: str,
    stopBits: str,
) -> None
```

Sets all com port properties in a single call.

### ShutterDevice

```python
ShutterDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Bases: `Device`

#### type

```python
type() -> Literal[Shutter]
```

#### open

```python
open() -> None
```

Open shutter.

#### close

```python
close() -> None
```

Close shutter.

#### isOpen

```python
isOpen() -> bool
```

Return `True` if shutter is open.

### SignalIODevice

```python
SignalIODevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Bases: `Device`

#### type

```python
type() -> Literal[SignalIO]
```

### SLMDevice

```python
SLMDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Bases: `Device`

#### exposure

```python
exposure: float
```

#### type

```python
type() -> Literal[SLM]
```

#### setImage

```python
setImage(pixels: Any) -> None
```

Write an image to the SLM .

#### setPixelsTo

```python
setPixelsTo(intensity: int) -> None
```

```python
setPixelsTo(red: int, green: int, blue: int) -> None
```

```python
setPixelsTo(*args: int) -> None
```

Set all SLM pixels to a single 8-bit intensity or RGB color.

#### displayImage

```python
displayImage() -> None
```

Display the image on the SLM.

#### setExposure

```python
setExposure(exposure_ms: float) -> None
```

Set exposure time for SLM.

#### getExposure

```python
getExposure() -> float
```

Return exposure time for SLM.

#### width

```python
width() -> int
```

Return the width of the SLM image.

#### height

```python
height() -> int
```

Return the height of the SLM image.

#### numberOfComponents

```python
numberOfComponents() -> int
```

Return the number of components in the SLM image.

#### bytesPerPixel

```python
bytesPerPixel() -> int
```

Return the number of bytes per pixel in the SLM image.

#### getSequenceMaxLength

```python
getSequenceMaxLength() -> int
```

Return the maximum length of a sequence for the SLM.

#### isSequenceable

```python
isSequenceable() -> bool
```

Return `True` if the SLM supports sequences.

#### loadSequence

```python
loadSequence(imageSequence: list[bytes]) -> None
```

Load a sequence of images to the SLM.

#### startSequence

```python
startSequence() -> None
```

Start the sequence of images on the SLM.

#### stopSequence

```python
stopSequence() -> None
```

Stop the sequence of images on the SLM.

### StageDevice

```python
StageDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

#### position

```python
position: float
```

#### isSequenceable

```python
isSequenceable = isStageSequenceable
```

#### loadSequence

```python
loadSequence = loadStageSequence
```

#### startSequence

```python
startSequence = startStageSequence
```

#### stopSequence

```python
stopSequence = stopStageSequence
```

#### getSequenceMaxLength

```python
getSequenceMaxLength = getStageSequenceMaxLength
```

#### type

```python
type() -> Literal[Stage]
```

#### setPosition

```python
setPosition(position: float) -> None
```

#### getPosition

```python
getPosition() -> float
```

#### setRelativePosition

```python
setRelativePosition(offset: float) -> None
```

#### getPositionAccumulator

```python
getPositionAccumulator() -> PositionChangeAccumulator
```

#### setOrigin

```python
setOrigin() -> None
```

#### setAdapterOrigin

```python
setAdapterOrigin(newZUm: float) -> None
```

#### setFocusDirection

```python
setFocusDirection(sign: int) -> None
```

#### getFocusDirection

```python
getFocusDirection() -> FocusDirection
```

#### isContinuousFocusDrive

```python
isContinuousFocusDrive() -> bool
```

Return `True` if device supports continuous focus.

#### isStageSequenceable

```python
isStageSequenceable() -> bool
```

Return `True` if device supports stage sequence.

#### isStageLinearSequenceable

```python
isStageLinearSequenceable() -> bool
```

Return `True` if device supports linear stage sequence.

#### startStageSequence

```python
startStageSequence() -> None
```

Start stage sequence.

#### stopStageSequence

```python
stopStageSequence() -> None
```

Stop stage sequence.

#### getStageSequenceMaxLength

```python
getStageSequenceMaxLength() -> int
```

Return maximum length of stage sequence.

#### loadStageSequence

```python
loadStageSequence(positions: Sequence[float]) -> None
```

Load stage sequence.

#### setStageLinearSequence

```python
setStageLinearSequence(dZ_um: float, nSlices: int) -> None
```

Set stage linear sequence.

### StateDevice

```python
StateDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

Bases: `Device`

#### state

```python
state: int
```

#### type

```python
type() -> Literal[State]
```

#### setState

```python
setState(state: int) -> None
```

Set state.

#### getState

```python
getState() -> int
```

Return state.

#### getNumberOfStates

```python
getNumberOfStates() -> int
```

Return number of states.

#### setStateLabel

```python
setStateLabel(label: str) -> None
```

Set state by label.

#### getStateLabel

```python
getStateLabel() -> StateLabel
```

Return state label.

#### defineStateLabel

```python
defineStateLabel(state: int, label: str) -> None
```

Define state labels.

#### getStateLabels

```python
getStateLabels() -> tuple[StateLabel, ...]
```

Return state labels.

#### getStateFromLabel

```python
getStateFromLabel(label: str) -> int
```

Return state for given label.

### XYStageDevice

```python
XYStageDevice(
    device_label: str = UNASSIGNED,
    mmcore: CMMCorePlus | None = None,
    adapter_name: str = "",
    device_name: str = "",
    type: DeviceType = UnknownType,
    description: str = "",
)
```

#### position

```python
position: tuple[float, float]
```

Return the position of the XY stage in microns.

#### setOrigin

```python
setOrigin = setOriginXY
```

#### isSequenceable

```python
isSequenceable = isXYStageSequenceable
```

#### startSequence

```python
startSequence = startXYStageSequence
```

#### stopSequence

```python
stopSequence = stopXYStageSequence
```

#### getSequenceMaxLength

```python
getSequenceMaxLength = getXYStageSequenceMaxLength
```

#### type

```python
type() -> Literal[XYStage]
```

#### setXYPosition

```python
setXYPosition(x: float, y: float) -> None
```

Set the position of the XY stage in microns.

#### getXYPosition

```python
getXYPosition() -> Sequence[float]
```

Return the position of the XY stage in microns.

#### setRelativeXYPosition

```python
setRelativeXYPosition(dx: float, dy: float) -> None
```

Set the relative position of the XY stage in microns.

#### getPositionAccumulator

```python
getPositionAccumulator() -> XYPositionChangeAccumulator
```

#### getXPosition

```python
getXPosition() -> float
```

Return the X position of the XY stage in microns.

#### getYPosition

```python
getYPosition() -> float
```

Return the Y position of the XY stage in microns.

#### setOriginXY

```python
setOriginXY() -> None
```

Zero the current XY stage's coordinates at the current position.

#### setOriginX

```python
setOriginX() -> None
```

Zero the given XY stage's X coordinate at the current position.

#### setOriginY

```python
setOriginY() -> None
```

Zero the given XY stage's Y coordinate at the current position.

#### setAdapterOriginXY

```python
setAdapterOriginXY(newXUm: float, newYUm: float) -> None
```

Enable software translation of coordinates for the current XY stage.

The current position of the stage becomes (newXUm, newYUm). It is recommended that setOriginXY() be used instead where available.

#### isXYStageSequenceable

```python
isXYStageSequenceable() -> bool
```

Return `True` if device supports XY stage sequence.

#### startXYStageSequence

```python
startXYStageSequence() -> None
```

Start XY stage sequence.

#### stopXYStageSequence

```python
stopXYStageSequence() -> None
```

Stop XY stage sequence.

#### getXYStageSequenceMaxLength

```python
getXYStageSequenceMaxLength() -> int
```

Return maximum length of XY stage sequence.

#### loadXYStageSequence

```python
loadXYStageSequence(
    xSequence: Sequence[float], ySequence: Sequence[float]
) -> None
```

Load XY stage sequence.

#### loadSequence

```python
loadSequence(sequence: Sequence[tuple[float, float]]) -> None
```

Load XY stage sequence with a sequence of 2-tuples.

Provided as a wrapper for loadXYStageSequence, for API parity with other sequencaable devices.

### SequencedEvent

Bases: `MDAEvent`

Subclass of MDAEvent that represents a sequence of triggered events.

Attributes:

<table>       <thead>         <tr>           <th>Name</th>           <th>Type</th>           <th>Description</th>         </tr>       </thead>       <tbody>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.index" optional="">index</autoref></code></td>             <td>                   <code><autoref identifier="ReadOnlyDict" optional="">ReadOnlyDict</autoref></code>             </td>             <td>               <div class="doc-md-description">                 <p>A read-only dictionary.</p>                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.channel" optional="">channel</autoref></code></td>             <td>                   <code><autoref identifier="Channel" optional="">Channel</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.exposure" optional="">exposure</autoref></code></td>             <td>                   <code><autoref identifier="float" optional="">float</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.min_start_time" optional="">min_start_time</autoref></code></td>             <td>                   <code><autoref identifier="float" optional="">float</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.pos_name" optional="">pos_name</autoref></code></td>             <td>                   <code><autoref identifier="str" optional="">str</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.x_pos" optional="">x_pos</autoref></code></td>             <td>                   <code><autoref identifier="float" optional="">float</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.y_pos" optional="">y_pos</autoref></code></td>             <td>                   <code><autoref identifier="float" optional="">float</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.z_pos" optional="">z_pos</autoref></code></td>             <td>                   <code><autoref identifier="float" optional="">float</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.slm_image" optional="">slm_image</autoref></code></td>             <td>                   <code><autoref identifier="SLMImage" optional="">SLMImage</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.sequence" optional="">sequence</autoref></code></td>             <td>                   <code><autoref hover="" identifier="useq.MDASequence" optional="">MDASequence</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.properties" optional="">properties</autoref></code></td>             <td>                   <code><autoref identifier="list" optional="">list</autoref>[<autoref identifier="PropertyTuple" optional="">PropertyTuple</autoref>] | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.roi" optional="">roi</autoref></code></td>             <td>                   <code><autoref identifier="CameraROI" optional="">CameraROI</autoref> | None</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.metadata" optional="">metadata</autoref></code></td>             <td>                   <code><autoref identifier="dict" optional="">dict</autoref>[<autoref identifier="str" optional="">str</autoref>, <autoref hover="" identifier="typing.Any" optional="">Any</autoref>]</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.action" optional="">action</autoref></code></td>             <td>                   <code><autoref identifier="HardwareAutofocus" optional="">HardwareAutofocus</autoref> | <autoref hover="" identifier="useq.AcquireImage" optional="">AcquireImage</autoref> | <autoref identifier="CustomAction" optional="">CustomAction</autoref></code>             </td>             <td>               <div class="doc-md-description">                 <p><autoref data-zensical-autoref="" domain="py" filepath="/Users/runner/work/pymmcore-plus.github.io/pymmcore-plus.github.io/.repos/pymmcore-plus/src/pymmcore_plus/core/_sequencing.py" identifier="useq.Action" lineno="58" origin="pymmcore_plus.core.SequencedEvent" role="class"><code>useq.Action</code></autoref> to acquire an image.</p> <h5 id="pymmcore_plus.core.SequencedEvent--attributes">Attributes</h5> <p>type : Literal[&quot;acquire_image&quot;]     This action can be used to acquire an image.</p>                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.keep_shutter_open" optional="">keep_shutter_open</autoref></code></td>             <td>                   <code><autoref identifier="bool" optional="">bool</autoref></code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.reset_event_timer" optional="">reset_event_timer</autoref></code></td>             <td>                   <code><autoref identifier="bool" optional="">bool</autoref></code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.events" optional="">events</autoref></code></td>             <td>                   <code><autoref identifier="tuple" optional="">tuple</autoref>[<autoref hover="" identifier="useq.MDAEvent" optional="">MDAEvent</autoref>, ...]</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.exposure_sequence" optional="">exposure_sequence</autoref></code></td>             <td>                   <code><autoref identifier="tuple" optional="">tuple</autoref>[<autoref identifier="float" optional="">float</autoref>, ...]</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.x_sequence" optional="">x_sequence</autoref></code></td>             <td>                   <code><autoref identifier="tuple" optional="">tuple</autoref>[<autoref identifier="float" optional="">float</autoref>, ...]</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.y_sequence" optional="">y_sequence</autoref></code></td>             <td>                   <code><autoref identifier="tuple" optional="">tuple</autoref>[<autoref identifier="float" optional="">float</autoref>, ...]</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.z_sequence" optional="">z_sequence</autoref></code></td>             <td>                   <code><autoref identifier="tuple" optional="">tuple</autoref>[<autoref identifier="float" optional="">float</autoref>, ...]</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.slm_sequence" optional="">slm_sequence</autoref></code></td>             <td>                   <code><autoref identifier="tuple" optional="">tuple</autoref>[<autoref identifier="bytes" optional="">bytes</autoref>, ...]</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>           <tr class="doc-section-item">             <td><code><autoref hover="" identifier="pymmcore_plus.core.SequencedEvent.property_sequences" optional="">property_sequences</autoref></code></td>             <td>                   <code><autoref identifier="dict" optional="">dict</autoref>[<autoref identifier="tuple" optional="">tuple</autoref>[<autoref identifier="str" optional="">str</autoref>, <autoref identifier="str" optional="">str</autoref>], <autoref identifier="list" optional="">list</autoref>[<autoref identifier="str" optional="">str</autoref>]]</code>             </td>             <td>               <div class="doc-md-description">                                </div>             </td>           </tr>       </tbody>     </table>

#### events

```python
events: tuple[MDAEvent, ...] = Field(repr=False)
```

#### exposure\_sequence

```python
exposure_sequence: tuple[float, ...] = Field(default_factory=tuple)
```

#### x\_sequence

```python
x_sequence: tuple[float, ...] = Field(default_factory=tuple)
```

#### y\_sequence

```python
y_sequence: tuple[float, ...] = Field(default_factory=tuple)
```

#### z\_sequence

```python
z_sequence: tuple[float, ...] = Field(default_factory=tuple)
```

#### slm\_sequence

```python
slm_sequence: tuple[bytes, ...] = Field(default_factory=tuple)
```

#### sequence

```python
sequence: MDASequence | None = Field(default=None, repr=False)
```

#### property\_sequences

```python
property_sequences: dict[tuple[str, str], list[str]] = Field(
    default_factory=dict
)
```

## Functions

### iter\_sequenced\_events

```python
iter_sequenced_events(
    core: CMMCorePlus, events: Iterable[MDAEvent]
) -> Iterator[MDAEvent | SequencedEvent]
```

Iterate over a sequence of MDAEvents, yielding SequencedEvents when possible.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `core` | `CMMCorePlus` | The core object to use for determining sequenceable properties. | *required* |
| `events` | `Iterable[MDAEvent]` | The events to iterate over. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Iterator[MDAEvent \| SequencedEvent]` | A new iterator that will combine multiple MDAEvents into a single SequencedEvent when possible, based on the sequenceable properties of the core object. Note that `SequencedEvent` itself is a subclass of `MDAEvent`, but it's up to the engine to check `isinstance(event, SequencedEvent)` in order to handle SequencedEvents differently. |

## Re-exports

These can also be imported from this module, but each is documented under its shortest import path (linked below).

| Name | Description |
| --- | --- |
| `ActionType` | Action that triggered a device property handler. |
| `CFGCommand` | Commands used in Micro-Manager configuration (`.cfg`) files. |
| `CFGGroup` | Names of built-in config groups and presets (`System`, `Startup`, etc...). |
| `CMMCorePlus` | Wrapper for CMMCore with extended functionality. |
| `ConfigGroup` | Convenience object for dealing with a set of related Configuration objects. |
| `Configuration` | Encapsulation of configuration information. |
| `Device` | Convenience object-oriented device API. |
| `DeviceAdapter` | Convenience view onto a device-adapter library. |
| `DeviceDetectionStatus` | DeviceDetectionStatus from device discovery. |
| `DeviceInitializationState` | DeviceInitializationState returned by getDeviceInitializationState. |
| `DeviceProperty` | Convenience view onto a device property. |
| `DeviceType` | Type of a Micro-Manager device. |
| `FocusDirection` | Direction a focus stage moves (towards or away from the sample). |
| `Keyword` | Standard property and device names (the `g_Keyword_*` constants). |
| `Metadata` | Subclass of `pymmcore.Metadata` with a pythonic interface. |
| `PixelFormat` | Subset of GeniCam Pixel Format names used by pymmcore-plus. |
| `PortType` | Type of a port device (serial, USB, HID). |
| `PropertyType` | Type of a device property value. |
