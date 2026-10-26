# pymmcore\_plus.core.events

Classes:

| Name | Description |
| --- | --- |
| `QCoreSignaler` |  |

Functions:

| Name | Description |
| --- | --- |
| `_get_auto_core_callback_class` |  |

## QCoreSignaler

```python
QCoreSignaler()
```

Bases: `QObject`

Methods:

| Name | Description |
| --- | --- |
| `devicePropertyChanged` | Return object to connect/disconnect to device/property-specific changes. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `propertiesChanged` |  |  |
| `propertyChanged` |  |  |
| `channelGroupChanged` |  |  |
| `configGroupChanged` |  |  |
| `configSet` |  |  |
| `systemConfigurationLoaded` |  |  |
| `pixelSizeChanged` |  |  |
| `pixelSizeAffineChanged` |  |  |
| `stagePositionChanged` |  |  |
| `XYStagePositionChanged` |  |  |
| `xYStagePositionChanged` |  |  |
| `exposureChanged` |  |  |
| `SLMExposureChanged` |  |  |
| `sLMExposureChanged` |  |  |
| `shutterOpenChanged` |  |  |
| `imageSnapped` |  |  |
| `sequenceAcquisitionStopped` |  |  |
| `sequenceAcquisitionStarted` |  |  |
| `mdaEngineRegistered` |  |  |
| `continuousSequenceAcquisitionStarting` |  |  |
| `continuousSequenceAcquisitionStarted` |  |  |
| `sequenceAcquisitionStarting` |  |  |
| `autoShutterSet` |  |  |
| `configGroupDeleted` |  |  |
| `configDeleted` |  |  |
| `configDefined` |  |  |
| `roiSet` |  |  |
| `property_callbacks` | `PropKeyDict` |  |

### propertiesChanged

```python
propertiesChanged = Signal()
```

### propertyChanged

```python
propertyChanged = Signal(str, str, object)
```

### channelGroupChanged

```python
channelGroupChanged = Signal(str)
```

### configGroupChanged

```python
configGroupChanged = Signal(str, str)
```

### configSet

```python
configSet = Signal(str, str)
```

### systemConfigurationLoaded

```python
systemConfigurationLoaded = Signal()
```

### pixelSizeChanged

```python
pixelSizeChanged = Signal(float)
```

### pixelSizeAffineChanged

```python
pixelSizeAffineChanged = Signal(float, float, float, float, float, float)
```

### stagePositionChanged

```python
stagePositionChanged = Signal(str, float)
```

### XYStagePositionChanged

```python
XYStagePositionChanged = Signal(str, float, float)
```

### xYStagePositionChanged

```python
xYStagePositionChanged = XYStagePositionChanged
```

### exposureChanged

```python
exposureChanged = Signal(str, float)
```

### SLMExposureChanged

```python
SLMExposureChanged = Signal(str, float)
```

### sLMExposureChanged

```python
sLMExposureChanged = SLMExposureChanged
```

### shutterOpenChanged

```python
shutterOpenChanged = Signal(str, bool)
```

### imageSnapped

```python
imageSnapped = Signal(str)
```

### sequenceAcquisitionStopped

```python
sequenceAcquisitionStopped = Signal(str)
```

### sequenceAcquisitionStarted

```python
sequenceAcquisitionStarted
```

### mdaEngineRegistered

```python
mdaEngineRegistered = Signal(object, object)
```

### continuousSequenceAcquisitionStarting

```python
continuousSequenceAcquisitionStarting = Signal()
```

### continuousSequenceAcquisitionStarted

```python
continuousSequenceAcquisitionStarted = Signal()
```

### sequenceAcquisitionStarting

```python
sequenceAcquisitionStarting
```

### autoShutterSet

```python
autoShutterSet = Signal(bool)
```

### configGroupDeleted

```python
configGroupDeleted = Signal(str)
```

### configDeleted

```python
configDeleted = Signal(str, str)
```

### configDefined

```python
configDefined = Signal(str, str, str, str, str)
```

### roiSet

```python
roiSet = Signal(str, int, int, int, int)
```

### property\_callbacks

```python
property_callbacks: PropKeyDict = {}
```

### devicePropertyChanged

```python
devicePropertyChanged(
    device: str, property: str | None = None
) -> _PropertySignal
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

## \_get\_auto\_core\_callback\_class

```python
_get_auto_core_callback_class() -> type[PCoreSignaler]
```

## Re-exports

These names can be imported from this module, but are documented at their top-level location.

| Name | Description |
| --- | --- |
| `CMMCoreSignaler` | Signals that will be emitted from CMMCorePlus objects. |
| `PCoreSignaler` | Declares the protocol for all signals that will be emitted from CMMCorePlus. |
