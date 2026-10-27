# Constants

All of the constants in the `pymmcore` library are in the top level `pymmcore` namespace, making it a bit difficult to know what type or enumeration they refer to.

All of these constants are reimplemented in the `pymmcore_plus` library as enums (`enum.IntEnum` or `enum.StrEnum`) and are available in the `pymmcore_plus` namespace (and are listed below).

For example, the integer corresponding to the `AfterLoadSequence` action type could be accessed as `pymmcore.AfterLoadSequence` or `pymmcore_plus.ActionType.AfterLoadSequence`.

```python
In [1]: import pymmcore

In [2]: pymmcore.AfterLoadSequence
Out[2]: 4

In [3]: from pymmcore_plus import ActionType

In [4]: ActionType.AfterLoadSequence
Out[4]: <ActionType.AfterLoadSequence: 4>

In [5]: int(ActionType.AfterLoadSequence)
Out[5]: 4
```

Additionally, it becomes easier to see what constants are available for each type or enumeration.

```python
In [6]: list(ActionType)
Out[6]:
[
    <ActionType.NoAction: 0>,
    <ActionType.BeforeGet: 1>,
    <ActionType.AfterSet: 2>,
    <ActionType.IsSequenceable: 3>,
    <ActionType.AfterLoadSequence: 4>,
    <ActionType.StartSequence: 5>,
    <ActionType.StopSequence: 6>
]
```

Lastly, many of the methods that return integers in `pymmcore.CMMCore` have been re-implemented in `pymmcore_plus.CMMCorePlus` to return the appropriate enumeration.

```python
import pymmcore

core = pymmcore.CMMCore()
# ...  load config and devices
core.getDeviceType("Camera")  # 2


import pymmcore_plus

core = pymmcore_plus.CMMCorePlus()
# ...  load config and devices
core.getDeviceType("Camera")  # <DeviceType.CameraDevice: 2>
```

## DeviceType

Bases: `IntEnum`

Type of a Micro-Manager device.

### UnknownType

```python
UnknownType = pymmcore.UnknownType
```

### AnyType

```python
AnyType = pymmcore.AnyType
```

### CameraDevice

```python
CameraDevice = pymmcore.CameraDevice
```

### ShutterDevice

```python
ShutterDevice = pymmcore.ShutterDevice
```

### StateDevice

```python
StateDevice = pymmcore.StateDevice
```

### StageDevice

```python
StageDevice = pymmcore.StageDevice
```

### XYStageDevice

```python
XYStageDevice = pymmcore.XYStageDevice
```

### SerialDevice

```python
SerialDevice = pymmcore.SerialDevice
```

### GenericDevice

```python
GenericDevice = pymmcore.GenericDevice
```

### AutoFocusDevice

```python
AutoFocusDevice = pymmcore.AutoFocusDevice
```

### CoreDevice

```python
CoreDevice = pymmcore.CoreDevice
```

### ImageProcessorDevice

```python
ImageProcessorDevice = pymmcore.ImageProcessorDevice
```

### SignalIODevice

```python
SignalIODevice = pymmcore.SignalIODevice
```

### MagnifierDevice

```python
MagnifierDevice = pymmcore.MagnifierDevice
```

### SLMDevice

```python
SLMDevice = pymmcore.SLMDevice
```

### HubDevice

```python
HubDevice = pymmcore.HubDevice
```

### GalvoDevice

```python
GalvoDevice = pymmcore.GalvoDevice
```

### PressurePumpDevice

```python
PressurePumpDevice = pymmcore.PressurePumpDevice
```

### VolumetricPumpDevice

```python
VolumetricPumpDevice = pymmcore.VolumetricPumpDevice
```

### Unknown

```python
Unknown = UnknownType
```

### Any

```python
Any = AnyType
```

### Camera

```python
Camera = CameraDevice
```

### Shutter

```python
Shutter = ShutterDevice
```

### State

```python
State = StateDevice
```

### Stage

```python
Stage = StageDevice
```

### XYStage

```python
XYStage = XYStageDevice
```

### Serial

```python
Serial = SerialDevice
```

### Generic

```python
Generic = GenericDevice
```

### AutoFocus

```python
AutoFocus = AutoFocusDevice
```

### Core

```python
Core = CoreDevice
```

### ImageProcessor

```python
ImageProcessor = ImageProcessorDevice
```

### SignalIO

```python
SignalIO = SignalIODevice
```

### Magnifier

```python
Magnifier = MagnifierDevice
```

### SLM

```python
SLM = SLMDevice
```

### Hub

```python
Hub = HubDevice
```

### Galvo

```python
Galvo = GalvoDevice
```

### PressurePump

```python
PressurePump = PressurePumpDevice
```

### VolumetricPump

```python
VolumetricPump = VolumetricPumpDevice
```

## PropertyType

Bases: `IntEnum`

Type of a device property value.

### Undef

```python
Undef = pymmcore.Undef
```

### String

```python
String = pymmcore.String
```

### Float

```python
Float = pymmcore.Float
```

### Integer

```python
Integer = pymmcore.Integer
```

### Boolean

```python
Boolean = auto()
```

### Enum

```python
Enum = auto()
```

### to\_python

```python
to_python() -> type | None
```

### to\_json

```python
to_json() -> str
```

### create

```python
create(value: Any) -> PropertyType
```

## FocusDirection

Bases: `IntEnum`

Direction a focus stage moves (towards or away from the sample).

### Unknown

```python
Unknown = 0
```

### TowardSample

```python
TowardSample = 1
```

### AwayFromSample

```python
AwayFromSample = -1
```

### FocusDirectionUnknown

```python
FocusDirectionUnknown = Unknown
```

### FocusDirectionTowardSample

```python
FocusDirectionTowardSample = TowardSample
```

### FocusDirectionAwayFromSample

```python
FocusDirectionAwayFromSample = AwayFromSample
```

## ActionType

Bases: `IntEnum`

Action that triggered a device property handler.

### NoAction

```python
NoAction = pymmcore.NoAction
```

### BeforeGet

```python
BeforeGet = pymmcore.BeforeGet
```

### AfterSet

```python
AfterSet = pymmcore.AfterSet
```

### IsSequenceable

```python
IsSequenceable = pymmcore.IsSequenceable
```

### AfterLoadSequence

```python
AfterLoadSequence = pymmcore.AfterLoadSequence
```

### StartSequence

```python
StartSequence = pymmcore.StartSequence
```

### StopSequence

```python
StopSequence = pymmcore.StopSequence
```

## PortType

Bases: `IntEnum`

Type of a port device (serial, USB, HID).

### InvalidPort

```python
InvalidPort = pymmcore.InvalidPort
```

### SerialPort

```python
SerialPort = pymmcore.SerialPort
```

### USBPort

```python
USBPort = pymmcore.USBPort
```

### HIDPort

```python
HIDPort = pymmcore.HIDPort
```

## DeviceDetectionStatus

Bases: `IntEnum`

DeviceDetectionStatus from device discovery.

### Unimplemented

```python
Unimplemented = pymmcore.Unimplemented
```

There is as yet no mechanism to programmatically detect the device.

### Misconfigured

```python
Misconfigured = pymmcore.Misconfigured
```

Some information needed to communicate with the device is invalid.

### CanNotCommunicate

```python
CanNotCommunicate = pymmcore.CanNotCommunicate
```

Communication attributes are valid, but the device does not respond.

### CanCommunicate

```python
CanCommunicate = pymmcore.CanCommunicate
```

Communication verified, parameters have been set to valid values.

## DeviceInitializationState

Bases: `IntEnum`

DeviceInitializationState returned by getDeviceInitializationState.

### Uninitialized

```python
Uninitialized = pymmcore.Uninitialized
```

### InitializedSuccessfully

```python
InitializedSuccessfully = pymmcore.InitializedSuccessfully
```

### InitializationFailed

```python
InitializationFailed = pymmcore.InitializationFailed
```

## PixelFormat

Bases: `StrEnum`

Subset of GeniCam Pixel Format names used by pymmcore-plus.

(This is similar to PixelType, but follows GeniCam standards.)

See [https://docs.baslerweb.com/pixel-format\#unpacked-and-packed-pixel-formats](<https://docs.baslerweb.com/pixel-format#unpacked-and-packed-pixel-formats>) for helpful clarifications. Note that **unpacked** pixel formats (like Mono8, Mono12, Mono16) are always 8-bit aligned. Meaning Mono12 is actually a 16-bit buffer.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `MONO8` | `str` | 8-bit (unpacked) monochrome pixel format. |
| `MONO10` | `str` | 10-bit (unpacked) monochrome pixel format. (16-bit buffer) |
| `MONO12` | `str` | 12-bit (unpacked) monochrome pixel format. (16-bit buffer) |
| `MONO14` | `str` | 14-bit (unpacked) monochrome pixel format. (16-bit buffer) |
| `MONO16` | `str` | 16-bit (unpacked) monochrome pixel format |
| `MONO32` | `str` | 32-bit (unpacked) monochrome pixel format |
| `RGB8` | `str` | 8-bit RGB pixel format. (24-bit buffer) |
| `RGB10` | `str` | 10-bit RGB pixel format. (48-bit buffer) |
| `RGB12` | `str` | 12-bit RGB pixel format. (48-bit buffer) |
| `RGB14` | `str` | 14-bit RGB pixel format. (48-bit buffer) |
| `RGB16` | `str` | 16-bit RGB pixel format. (48-bit buffer) |

### MONO8

```python
MONO8 = 'Mono8'
```

### MONO10

```python
MONO10 = 'Mono10'
```

### MONO12

```python
MONO12 = 'Mono12'
```

### MONO14

```python
MONO14 = 'Mono14'
```

### MONO16

```python
MONO16 = 'Mono16'
```

### MONO32

```python
MONO32 = 'Mono32'
```

### RGB8

```python
RGB8 = 'RGB8'
```

### RGB10

```python
RGB10 = 'RGB10'
```

### RGB12

```python
RGB12 = 'RGB12'
```

### RGB14

```python
RGB14 = 'RGB14'
```

### RGB16

```python
RGB16 = 'RGB16'
```

### pick

```python
pick(bit_depth: int, n_comp: int = 1) -> PixelFormat
```

### for\_current\_camera

```python
for_current_camera(core: CMMCore) -> PixelFormat
```

## Keyword

Bases: `StrEnum`

Standard property and device names (the `g_Keyword_*` constants).

### Name

```python
Name = pymmcore.g_Keyword_Name
```

### Description

```python
Description = pymmcore.g_Keyword_Description
```

### CameraName

```python
CameraName = pymmcore.g_Keyword_CameraName
```

### CameraID

```python
CameraID = pymmcore.g_Keyword_CameraID
```

### CameraChannelName

```python
CameraChannelName = pymmcore.g_Keyword_CameraChannelName
```

### CameraChannelIndex

```python
CameraChannelIndex = pymmcore.g_Keyword_CameraChannelIndex
```

### Binning

```python
Binning = pymmcore.g_Keyword_Binning
```

### Exposure

```python
Exposure = pymmcore.g_Keyword_Exposure
```

### ActualExposure

```python
ActualExposure = pymmcore.g_Keyword_ActualExposure
```

### ActualInterval\_ms

```python
ActualInterval_ms = pymmcore.g_Keyword_ActualInterval_ms
```

### Interval\_ms

```python
Interval_ms = pymmcore.g_Keyword_Interval_ms
```

### Elapsed\_Time\_ms

```python
Elapsed_Time_ms = pymmcore.g_Keyword_Elapsed_Time_ms
```

### PixelType

```python
PixelType = pymmcore.g_Keyword_PixelType
```

### ReadoutTime

```python
ReadoutTime = pymmcore.g_Keyword_ReadoutTime
```

### ReadoutMode

```python
ReadoutMode = pymmcore.g_Keyword_ReadoutMode
```

### Gain

```python
Gain = pymmcore.g_Keyword_Gain
```

### EMGain

```python
EMGain = pymmcore.g_Keyword_EMGain
```

### Offset

```python
Offset = pymmcore.g_Keyword_Offset
```

### CCDTemperature

```python
CCDTemperature = pymmcore.g_Keyword_CCDTemperature
```

### CCDTemperatureSetPoint

```python
CCDTemperatureSetPoint = pymmcore.g_Keyword_CCDTemperatureSetPoint
```

### State

```python
State = pymmcore.g_Keyword_State
```

### Label

```python
Label = pymmcore.g_Keyword_Label
```

### Position

```python
Position = pymmcore.g_Keyword_Position
```

### Type

```python
Type = pymmcore.g_Keyword_Type
```

### Delay

```python
Delay = pymmcore.g_Keyword_Delay
```

### BaudRate

```python
BaudRate = pymmcore.g_Keyword_BaudRate
```

### DataBits

```python
DataBits = pymmcore.g_Keyword_DataBits
```

### StopBits

```python
StopBits = pymmcore.g_Keyword_StopBits
```

### Parity

```python
Parity = pymmcore.g_Keyword_Parity
```

### Handshaking

```python
Handshaking = pymmcore.g_Keyword_Handshaking
```

### DelayBetweenCharsMs

```python
DelayBetweenCharsMs = pymmcore.g_Keyword_DelayBetweenCharsMs
```

### Port

```python
Port = pymmcore.g_Keyword_Port
```

### AnswerTimeout

```python
AnswerTimeout = pymmcore.g_Keyword_AnswerTimeout
```

### Speed

```python
Speed = pymmcore.g_Keyword_Speed
```

### CoreDevice

```python
CoreDevice = pymmcore.g_Keyword_CoreDevice
```

### CoreInitialize

```python
CoreInitialize = pymmcore.g_Keyword_CoreInitialize
```

### CoreCamera

```python
CoreCamera = pymmcore.g_Keyword_CoreCamera
```

### CoreShutter

```python
CoreShutter = pymmcore.g_Keyword_CoreShutter
```

### CoreXYStage

```python
CoreXYStage = pymmcore.g_Keyword_CoreXYStage
```

### CoreFocus

```python
CoreFocus = pymmcore.g_Keyword_CoreFocus
```

### CoreAutoFocus

```python
CoreAutoFocus = pymmcore.g_Keyword_CoreAutoFocus
```

### CoreAutoShutter

```python
CoreAutoShutter = pymmcore.g_Keyword_CoreAutoShutter
```

### CoreChannelGroup

```python
CoreChannelGroup = pymmcore.g_Keyword_CoreChannelGroup
```

### CoreImageProcessor

```python
CoreImageProcessor = pymmcore.g_Keyword_CoreImageProcessor
```

### CoreSLM

```python
CoreSLM = pymmcore.g_Keyword_CoreSLM
```

### CoreGalvo

```python
CoreGalvo = pymmcore.g_Keyword_CoreGalvo
```

### CoreTimeoutMs

```python
CoreTimeoutMs = pymmcore.g_Keyword_CoreTimeoutMs
```

### Channel

```python
Channel = pymmcore.g_Keyword_Channel
```

### Version

```python
Version = pymmcore.g_Keyword_Version
```

### ColorMode

```python
ColorMode = pymmcore.g_Keyword_ColorMode
```

### Transpose\_SwapXY

```python
Transpose_SwapXY = pymmcore.g_Keyword_Transpose_SwapXY
```

### Transpose\_MirrorX

```python
Transpose_MirrorX = pymmcore.g_Keyword_Transpose_MirrorX
```

### Transpose\_MirrorY

```python
Transpose_MirrorY = pymmcore.g_Keyword_Transpose_MirrorY
```

### Transpose\_Correction

```python
Transpose_Correction = pymmcore.g_Keyword_Transpose_Correction
```

### Closed\_Position

```python
Closed_Position = pymmcore.g_Keyword_Closed_Position
```

### HubID

```python
HubID = pymmcore.g_Keyword_HubID
```

### Metadata\_CameraLabel

```python
Metadata_CameraLabel = pymmcore.g_Keyword_Metadata_CameraLabel
```

### Metadata\_Exposure

```python
Metadata_Exposure = pymmcore.g_Keyword_Metadata_Exposure
```

### Metadata\_Height

```python
Metadata_Height = pymmcore.g_Keyword_Metadata_Height
```

### Metadata\_ImageNumber

```python
Metadata_ImageNumber = pymmcore.g_Keyword_Metadata_ImageNumber
```

### Metadata\_ROI\_X

```python
Metadata_ROI_X = pymmcore.g_Keyword_Metadata_ROI_X
```

### Metadata\_ROI\_Y

```python
Metadata_ROI_Y = pymmcore.g_Keyword_Metadata_ROI_Y
```

### Metadata\_Score

```python
Metadata_Score = pymmcore.g_Keyword_Metadata_Score
```

### Metadata\_TimeInCore

```python
Metadata_TimeInCore = pymmcore.g_Keyword_Metadata_TimeInCore
```

### Metadata\_Width

```python
Metadata_Width = pymmcore.g_Keyword_Metadata_Width
```

## CFGCommand

Bases: `StrEnum`

Commands used in Micro-Manager configuration (`.cfg`) files.

### Device

```python
Device = pymmcore.g_CFGCommand_Device
```

### Label

```python
Label = pymmcore.g_CFGCommand_Label
```

### Property

```python
Property = pymmcore.g_CFGCommand_Property
```

### Configuration

```python
Configuration = pymmcore.g_CFGCommand_Configuration
```

### ConfigGroup

```python
ConfigGroup = pymmcore.g_CFGCommand_ConfigGroup
```

### Equipment

```python
Equipment = pymmcore.g_CFGCommand_Equipment
```

### Delay

```python
Delay = pymmcore.g_CFGCommand_Delay
```

### ImageSynchro

```python
ImageSynchro = pymmcore.g_CFGCommand_ImageSynchro
```

### ConfigPixelSize

```python
ConfigPixelSize = pymmcore.g_CFGCommand_ConfigPixelSize
```

### PixelSize\_um

```python
PixelSize_um = pymmcore.g_CFGCommand_PixelSize_um
```

### PixelSizeAffine

```python
PixelSizeAffine = pymmcore.g_CFGCommand_PixelSizeAffine
```

### ParentID

```python
ParentID = pymmcore.g_CFGCommand_ParentID
```

### FocusDirection

```python
FocusDirection = pymmcore.g_CFGCommand_FocusDirection
```

### PixelSize\_dxdz

```python
PixelSize_dxdz = pymmcore.g_CFGCommand_PixelSizedxdz
```

### PixelSize\_dydz

```python
PixelSize_dydz = pymmcore.g_CFGCommand_PixelSizedydz
```

### PixelSize\_OptimalZUm

```python
PixelSize_OptimalZUm = pymmcore.g_CFGCommand_PixelSizeOptimalZUm
```

### FieldDelimiters

```python
FieldDelimiters = pymmcore.g_FieldDelimiters
```

## CFGGroup

Bases: `StrEnum`

Names of built-in config groups and presets (`System`, `Startup`, etc...).

### System

```python
System = pymmcore.g_CFGGroup_System
```

### System\_Startup

```python
System_Startup = pymmcore.g_CFGGroup_System_Startup
```

### System\_Shutdown

```python
System_Shutdown = pymmcore.g_CFGGroup_System_Shutdown
```

### PixelSizeUm

```python
PixelSizeUm = pymmcore.g_CFGGroup_PixelSizeUm
```
