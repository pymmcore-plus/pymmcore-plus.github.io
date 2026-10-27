# Events

There are two objects that emit events in `pymmcore-plus`. The `CMMCorePlus` object emits the `PCoreSignaler` signals at `core.events` when the state of the microscope changes, and the `MDARunner` emits the `PMDASignaler` signals at `core.mda.events` as an acquisition sequence progresses.

See [Events and Callbacks](<https://pymmcore-plus.github.io/pymmcore-plus/guides/events/index.md>) for how to connect callbacks, choosing the Qt or psygnal backend, and which thread your callbacks run on.

## PCoreSignaler

Bases: `Protocol`

Declares the protocol for all signals that will be emitted from CMMCorePlus.

The main instance of this interface is available on the `CMMCorePlus` object at the `events` attribute. Each signal on `events` is an object that has a `connect` and a `disconnect` method that you can use to connect/disconnect your own callback functions. `connect` and `disconnect` accept a single argument, which is a callable that will be called when the signal is emitted. The callable should accept no more positional arguments than the signal emits (noted for each signal below), but may accept fewer.

> [!NOTE]
>
> These events are a superset of those emitted by [MMEventCallback](<https://micro-manager.org/apidoc/mmcorej/latest/mmcorej/MMEventCallback.html>) in the MMCore C++ library. The "on" prefix has been removed from the names here and the first letter lower cased.
>
> **Important**
>
> In the core C++ library (and in `pymmcore`), the emission of many of these events is left to the discretion of the device adapter. In `pymmcore_plus`, we attempt to emit these events in a more consistent manner (e.g. by checking a particular value before and after calling into the C++ library). So, the emission of these events is not guaranteed to be 1:1 with the C++ library; however, it should be easier to follow the state of the core when using `pymmcore_plus.CMMCorePlus`.

Examples:

To connect to the `onExposureChanged` event emitted by MMCore, you would connect to the `exposureChanged` signal on this class:

```python
from pymmcore_plus import CMMCorePlus

core = CMMCorePlus()


def on_exposure_changed(device: str, new_exposure: float):
    print(f"Exposure changed for {device} to {new_exposure}")


core.events.exposureChanged.connect(on_exposure_changed)
```

Events may also be connected as a decorator:

```python
@core.events.exposureChanged.connect
def on_exposure_changed(device: str, new_exposure: float): ...
```

---

### propertiesChanged

```python
propertiesChanged: PSignal
```

Emits with no arguments when properties have changed.

### propertyChanged

```python
propertyChanged: PSignal
```

Emits `(name: str, propName: str, propValue: str)` when a specific property has changed.

### channelGroupChanged

```python
channelGroupChanged: PSignal
```

Emits `(newChannelGroupName: str)` when a channel group has changed.

### configGroupChanged

```python
configGroupChanged: PSignal
```

Emits `(groupName: str, newConfigName: str)` when a config group has changed.

### systemConfigurationLoaded

```python
systemConfigurationLoaded: PSignal
```

Emits with no arguments when the system configuration has been loaded.

### pixelSizeChanged

```python
pixelSizeChanged: PSignal
```

Emits `(newPixelSizeUm: float)` when the pixel size has changed.

### pixelSizeAffineChanged

```python
pixelSizeAffineChanged: PSignal
```

Emits `(float, float, float, float, float, float)` when the pixel size affine has changed.

### stagePositionChanged

```python
stagePositionChanged: PSignal
```

Emits `(name: str, pos: float)` when a stage position has changed.

### XYStagePositionChanged

```python
XYStagePositionChanged: PSignal
```

Emits `(name: str, xpos: float, ypos: float)` when an XY stage position has changed.

### exposureChanged

```python
exposureChanged: PSignal
```

Emits `(name: str, newExposure: float)` when an exposure has changed.

### SLMExposureChanged

```python
SLMExposureChanged: PSignal
```

Emits `(name: str, newExposure: float)` when the exposure of the SLM device changes.

### shutterOpenChanged

```python
shutterOpenChanged: PSignal
```

Emits `(name: str, isOpen: bool)` when the shutter open state has changed.

### configSet

```python
configSet: PSignal
```

Emits `(groupName: str, configName: str)` when a config has been set.

> ✨ This signal is unique to `pymmcore-plus`.

### imageSnapped

```python
imageSnapped: PSignal
```

Emits `(cameraLabel: str)` whenever `snapImage` is called.

### mdaEngineRegistered

```python
mdaEngineRegistered: PSignal
```

Emits `(newEngine, oldEngine)` when an MDAEngine is registered.

> ✨ This signal is unique to `pymmcore-plus`.

### continuousSequenceAcquisitionStarting

```python
continuousSequenceAcquisitionStarting: PSignal
```

Emits with no arguments *before* continuous sequence acquisition is started.

> ✨ This signal is unique to `pymmcore-plus`.

### continuousSequenceAcquisitionStarted

```python
continuousSequenceAcquisitionStarted: PSignal
```

Emits with no arguments *after* continuous sequence acquisition has started.

> ✨ This signal is unique to `pymmcore-plus`.

### sequenceAcquisitionStarting

```python
sequenceAcquisitionStarting: PSignal
```

Emits `(cameraLabel: str)` *before* sequence acquisition is started.

> [!NOTE]
>
> **Breaking Change**
>
> In `pymmcore-plus` version 0.16.0, the `sequenceAcquisitionStarting` signal was *reduced* from `(str, int, float, bool)` to `(str,)` to match the signature emitted by the C++ MMCore library.

> ✨ This signal is unique to `pymmcore-plus`.

### sequenceAcquisitionStarted

```python
sequenceAcquisitionStarted: PSignal
```

Emits `(cameraLabel: str)` *after* sequence acquisition has started.

> [!NOTE]
>
> **Breaking Change**
>
> In `pymmcore-plus` version 0.16.0, the `sequenceAcquisitionStarted` signal was *reduced* from `(str, int, float, bool)` to `(str,)` to match the signature emitted by the C++ MMCore library.

### sequenceAcquisitionStopped

```python
sequenceAcquisitionStopped: PSignal
```

Emits `(cameraLabel: str)` when sequence acquisition is stopped.

### autoShutterSet

```python
autoShutterSet: PSignal
```

Emits `(state: bool)` when the auto shutter setting is changed.

> ✨ This signal is unique to `pymmcore-plus`.

### configGroupDeleted

```python
configGroupDeleted: PSignal
```

Emits `(groupName: str)` when a config group is deleted.

> ✨ This signal is unique to `pymmcore-plus`.

### configDeleted

```python
configDeleted: PSignal
```

Emits `(groupName: str, configName: str)` when a config is deleted.

> ✨ This signal is unique to `pymmcore-plus`.

### configDefined

```python
configDefined: PSignal
```

Emits `(str, str, str, str, str)` when a config is defined.

The arguments are `(groupName, configName, deviceLabel, propName, value)`. The last three are empty strings when an empty preset is defined.

> ✨ This signal is unique to `pymmcore-plus`.

### roiSet

```python
roiSet: PSignal
```

Emits `(cameraLabel: str, x, y, width, height)` when an ROI is set.

> ✨ This signal is unique to `pymmcore-plus`.

### devicePropertyChanged

```python
devicePropertyChanged(
    device: str, property: str | None = None
) -> PSignalInstance
```

Return object to connect/disconnect to device/property-specific changes.

Note that the callback provided to `.connect()` must take *two* parameters (property\_name, new\_value) if only `device` is provided, and *one* parameter (new\_value) of both `device` and `property` are provided.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device` | `str` | A device label | *required* |
| `property` | `Optional[str]` | Optional property label. If not provided, all property changes on `device` will trigger an event emission. by default None | `None` |

Returns:

| Type | Description |
| --- | --- |
| `_PropertySignal` | Object with `connect` and `disconnect` methods that attach a callback to the change event of a specific property or device. |

Examples:

```pycon
>>> core.events.devicePropertyChanged("Camera", "Gain").connect(callback)
>>> core.events.devicePropertyChanged("Camera").connect(callback)
```

## PMDASignaler

Bases: `Protocol`

Declares the protocol for all signals that will be emitted from `pymmcore_plus.mda.MDARunner`.

### sequenceStarted

```python
sequenceStarted: PSignal
```

Emits `(sequence: MDASequence, metadata: dict)` when an acquisition sequence is started.

For the default `MDAEngine`, the metadata `dict` will be of type `SummaryMetaV1`.

### sequencePauseToggled

```python
sequencePauseToggled: PSignal
```

Emits `(paused: bool)` when an acquisition sequence is paused or unpaused.

### sequenceCanceled

```python
sequenceCanceled: PSignal
```

Emits `(sequence: MDASequence)` when an acquisition sequence is canceled.

### sequenceFinished

```python
sequenceFinished: PSignal
```

Emits `(sequence: MDASequence)` when an acquisition sequence is finished.

### frameReady

```python
frameReady: PSignal
```

Emits `(img: np.ndarray, event: MDAEvent, metadata: dict)` after an image is acquired during an acquisition sequence.

For the default `MDAEngine`, the metadata `dict` will be of type `FrameMetaV1`.

### awaitingEvent

```python
awaitingEvent: PSignal
```

Emits `(event: MDAEvent, remaining_sec: float)` when the runner is waiting to start an event.

Note: Not all events in a sequence will emit this signal. This will only be emitted if the wait time is non-zero.

### eventStarted

```python
eventStarted: PSignal
```

Emits `(event: MDAEvent)` immediately before event setup and execution.
