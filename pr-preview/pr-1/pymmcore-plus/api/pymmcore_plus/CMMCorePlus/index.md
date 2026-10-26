# CMMCorePlus

```python
CMMCorePlus(mm_path: str | None = None, adapter_paths: Sequence[str] = ())
```

Bases: `CMMCore`

Wrapper for CMMCore with extended functionality.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `mm_path` | `str \| None` | Path to the Micro-Manager installation. If `None` (default), will use the return value of `pymmcore_plus.find_micromanager`. | `None` |
| `adapter_paths` | `Sequence[str]` | Paths to search for device adapters, by default () | `()` |

## Method summary

`CMMCorePlus` is a subclass of [`pymmcore.CMMCore`](<https://github.com/micro-manager/pymmcore>), so **every** method of the C++ core is available here. The table below lists all of them: use the filters to see what `pymmcore-plus` adds (✨) or changes (), and hover over an override to see why.

✨ only in `CMMCorePlus`  · overridden by `CMMCorePlus` (hover for why)  · *no icon*: inherited unchanged from `pymmcore.CMMCore`

| Method | Origin | Category | Description |
| --- | --- | --- | --- |
| [`addGalvoPolygonVertex`](<#pymmcore_plus.CMMCorePlus.addGalvoPolygonVertex>)(galvoLabel, polygonIndex, x, y) |  | [Galvos](<#cmmcoreplus-galvos>) | Add a vertex to a galvo polygon. |
| [`canSequenceEvents`](<#pymmcore_plus.CMMCorePlus.canSequenceEvents>)(e1, e2, cur\_length) | ✨ | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Check whether two `useq.MDAEvent` are sequenceable by this core instance. |
| [`channelGroup_pattern`](<#pymmcore_plus.CMMCorePlus.channelGroup_pattern>) | ✨ | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | The regex pattern used to identify channel groups. |
| [`clearCircularBuffer`](<#pymmcore_plus.CMMCorePlus.clearCircularBuffer>)() |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Removes all images from the circular buffer. |
| [`clearROI`](<#pymmcore_plus.CMMCorePlus.clearROI>)() |  | [Cameras](<#cmmcoreplus-cameras>) | Set the region of interest of the current camera to the full frame. |
| [`debugLogEnabled`](<#pymmcore_plus.CMMCorePlus.debugLogEnabled>)() |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Indicates if logging of debug messages is enabled |
| [`defineConfig`](<#pymmcore_plus.CMMCorePlus.defineConfig>)(groupName, configName, deviceLabel, propName, value) (2 overloads) | ➕ | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Defines a configuration. |
| [`defineConfigGroup`](<#pymmcore_plus.CMMCorePlus.defineConfigGroup>)(groupName) |  | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Creates an empty configuration group. |
| [`definePixelSizeConfig`](<#pymmcore_plus.CMMCorePlus.definePixelSizeConfig>)(args, kwargs) (2 overloads) | ➕ | [Pixel size](<#cmmcoreplus-pixel-size>) | Defines an empty pixel size entry. |
| [`defineStateLabel`](<#pymmcore_plus.CMMCorePlus.defineStateLabel>)(stateDeviceLabel, state, stateLabel) |  | [State devices](<#cmmcoreplus-state-devices>) | Defines a label for the specific state. |
| [`deleteConfig`](<#pymmcore_plus.CMMCorePlus.deleteConfig>)(groupName, configName, deviceLabel, propName) (2 overloads) | ➕ | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Delete `configName` from `groupName`. |
| [`deleteConfigGroup`](<#pymmcore_plus.CMMCorePlus.deleteConfigGroup>)(groupName) | ➕ | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Deletes an entire configuration `group`. |
| [`deleteGalvoPolygons`](<#pymmcore_plus.CMMCorePlus.deleteGalvoPolygons>)(galvoLabel) |  | [Galvos](<#cmmcoreplus-galvos>) | Remove all added polygons |
| [`deletePixelSizeConfig`](<#pymmcore_plus.CMMCorePlus.deletePixelSizeConfig>)(resolutionID) | ➕ | [Pixel size](<#cmmcoreplus-pixel-size>) | Delete the pixel size configuration for the given `resolutionID`. |
| [`describe`](<#pymmcore_plus.CMMCorePlus.describe>)(sort, show\_config\_groups, show\_available) | ✨ | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) | Print information table with the current configuration. |
| [`detectDevice`](<#pymmcore_plus.CMMCorePlus.detectDevice>)(deviceLabel) | ➕ | [Devices](<#cmmcoreplus-devices>) | Tries to communicate to a device through a given serial port. |
| [`deviceBusy`](<#pymmcore_plus.CMMCorePlus.deviceBusy>)(label) |  | [Devices](<#cmmcoreplus-devices>) | Checks the busy status of the specific device. |
| [`deviceTypeBusy`](<#pymmcore_plus.CMMCorePlus.deviceTypeBusy>)(devType) |  | [Devices](<#cmmcoreplus-devices>) | Checks the busy status for all devices of the specific type. |
| [`displaySLMImage`](<#pymmcore_plus.CMMCorePlus.displaySLMImage>)(slmLabel) |  | [SLMs](<#cmmcoreplus-slms>) | Display the waiting image on the SLM. |
| [`enableContinuousFocus`](<#pymmcore_plus.CMMCorePlus.enableContinuousFocus>)(enable) |  | [Autofocus](<#cmmcoreplus-autofocus>) | Enables or disables the operation of the continuous focusing hardware device. |
| [`enableDebugLog`](<#pymmcore_plus.CMMCorePlus.enableDebugLog>)(enable) |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Enable or disable logging of debug messages. |
| [`enableFeature`](<#pymmcore_plus.CMMCorePlus.enableFeature>)(name, enable) |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Enable or disable the given Core feature. |
| [`enableStderrLog`](<#pymmcore_plus.CMMCorePlus.enableStderrLog>)(enable) |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Enables or disables log message display on the standard console. |
| [`events`](<#pymmcore_plus.CMMCorePlus.events>) | ✨ | [Acquisition engine &amp; events](<#cmmcoreplus-acquisition-engine-events>) | Signaler for core events. |
| [`fixImage`](<#pymmcore_plus.CMMCorePlus.fixImage>)(img, ncomponents) | ✨ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Fix img shape/dtype based on `self.getNumberOfComponents()`. |
| [`fullFocus`](<#pymmcore_plus.CMMCorePlus.fullFocus>)() |  | [Autofocus](<#cmmcoreplus-autofocus>) | Performs focus acquisition and lock for the one-shot focusing device. |
| [`getAdapterObject`](<#pymmcore_plus.CMMCorePlus.getAdapterObject>)(library\_name) | ✨ | [Devices](<#cmmcoreplus-devices>) | Return an `Adapter` object bound to library\_name on this core. |
| [`getAllowedBinningValues`](<#pymmcore_plus.CMMCorePlus.getAllowedBinningValues>)() (2 overloads) |  | [Cameras](<#cmmcoreplus-cameras>) | Returns allowed binning values for the current camera. |
| [`getAllowedPropertyValues`](<#pymmcore_plus.CMMCorePlus.getAllowedPropertyValues>)(label, propName) |  | [Properties](<#cmmcoreplus-properties>) | Returns all valid values for the specified property. |
| [`getAPIVersionInfo`](<#pymmcore_plus.CMMCorePlus.getAPIVersionInfo>)() |  | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) | Returns the module and device interface versions. |
| [`getAutoFocusDevice`](<#pymmcore_plus.CMMCorePlus.getAutoFocusDevice>)() |  | [Autofocus](<#cmmcoreplus-autofocus>) | Returns the label of the currently selected auto-focus device. |
| [`getAutoFocusOffset`](<#pymmcore_plus.CMMCorePlus.getAutoFocusOffset>)() | ➕ | [Autofocus](<#cmmcoreplus-autofocus>) |  |
| [`getAutoShutter`](<#pymmcore_plus.CMMCorePlus.getAutoShutter>)() |  | [Shutters](<#cmmcoreplus-shutters>) | Returns the current setting of the auto-shutter option. |
| [`getAvailableConfigGroups`](<#pymmcore_plus.CMMCorePlus.getAvailableConfigGroups>)() |  | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Returns the names of all defined configuration groups |
| [`getAvailableConfigs`](<#pymmcore_plus.CMMCorePlus.getAvailableConfigs>)(configGroup) |  | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Returns all defined configuration (preset) names in a given group |
| [`getAvailableDeviceDescriptions`](<#pymmcore_plus.CMMCorePlus.getAvailableDeviceDescriptions>)(library) |  | [Devices](<#cmmcoreplus-devices>) | Get descriptions for available devices from the specified library. |
| [`getAvailableDevices`](<#pymmcore_plus.CMMCorePlus.getAvailableDevices>)(library) |  | [Devices](<#cmmcoreplus-devices>) | Get available devices from the specified device library. |
| [`getAvailableDeviceTypes`](<#pymmcore_plus.CMMCorePlus.getAvailableDeviceTypes>)(library) |  | [Devices](<#cmmcoreplus-devices>) | Get type information for available devices from the specified library. |
| [`getAvailablePixelSizeConfigs`](<#pymmcore_plus.CMMCorePlus.getAvailablePixelSizeConfigs>)() |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Returns all defined resolution preset names |
| [`getBinning`](<#pymmcore_plus.CMMCorePlus.getBinning>)() (2 overloads) |  | [Cameras](<#cmmcoreplus-cameras>) | Returns the current binning factor of the camera. |
| [`getBufferFreeCapacity`](<#pymmcore_plus.CMMCorePlus.getBufferFreeCapacity>)() |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Returns the number of images that can be added to the buffer without overflowing. |
| [`getBufferTotalCapacity`](<#pymmcore_plus.CMMCorePlus.getBufferTotalCapacity>)() |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Returns the total number of images that can be stored in the buffer |
| [`getBytesPerPixel`](<#pymmcore_plus.CMMCorePlus.getBytesPerPixel>)() |  | [Cameras](<#cmmcoreplus-cameras>) | How many bytes for each pixel. |
| [`getCameraChannelName`](<#pymmcore_plus.CMMCorePlus.getCameraChannelName>)(channelNr) |  | [Cameras](<#cmmcoreplus-cameras>) | Returns the name of the requested channel as known by the default camera |
| [`getCameraChannelNames`](<#pymmcore_plus.CMMCorePlus.getCameraChannelNames>)() | ✨ | [Cameras](<#cmmcoreplus-cameras>) | Convenience method to call `getCameraChannelName` for all camera channels. |
| [`getCameraDevice`](<#pymmcore_plus.CMMCorePlus.getCameraDevice>)() |  | [Cameras](<#cmmcoreplus-cameras>) | Returns the label of the currently selected camera device. |
| [`getChannelGroup`](<#pymmcore_plus.CMMCorePlus.getChannelGroup>)() |  | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Returns the group determining the channel selection. |
| [`getCircularBufferMemoryFootprint`](<#pymmcore_plus.CMMCorePlus.getCircularBufferMemoryFootprint>)() |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Returns the size of the Circular Buffer in MB |
| [`getConfigData`](<#pymmcore_plus.CMMCorePlus.getConfigData>)(configGroup, configName, native) (2 overloads) | ➕ | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Return the configuration object for a given `configGroup` and `configName`. |
| [`getConfigGroupObject`](<#pymmcore_plus.CMMCorePlus.getConfigGroupObject>)(group\_name, allow\_missing) | ✨ | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Return a `ConfigGroup` object bound to group\_name on this core. |
| [`getConfigGroupState`](<#pymmcore_plus.CMMCorePlus.getConfigGroupState>)(group, native) (2 overloads) | ➕ | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Return the state of the devices included in the specified `group`. |
| [`getConfigGroupStateFromCache`](<#pymmcore_plus.CMMCorePlus.getConfigGroupStateFromCache>)(group, native) (2 overloads) | ➕ | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Return the state of the system cache, for the devices in the specified group. |
| [`getConfigState`](<#pymmcore_plus.CMMCorePlus.getConfigState>)(group, config, native) | ➕ | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Return state of devices included in the specified configuration. |
| [`getCoreErrorText`](<#pymmcore_plus.CMMCorePlus.getCoreErrorText>)(code) |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Returns a pre-defined error test with the given error code |
| [`getCurrentConfig`](<#pymmcore_plus.CMMCorePlus.getCurrentConfig>)(groupName) |  | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Returns the current configuration (preset) for a given group. |
| [`getCurrentConfigFromCache`](<#pymmcore_plus.CMMCorePlus.getCurrentConfigFromCache>)(groupName) |  | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Returns the configuration for a given group based on the data in the cache. |
| [`getCurrentDeviceOfType`](<#pymmcore_plus.CMMCorePlus.getCurrentDeviceOfType>)(device\_type) | ✨ | [Devices](<#cmmcoreplus-devices>) | Return the current device of type `device_type`. |
| [`getCurrentFocusScore`](<#pymmcore_plus.CMMCorePlus.getCurrentFocusScore>)() |  | [Autofocus](<#cmmcoreplus-autofocus>) | Returns the focus score from the default focusing device measured at the current Z position. |
| [`getCurrentPixelSizeConfig`](<#pymmcore_plus.CMMCorePlus.getCurrentPixelSizeConfig>)() (2 overloads) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Get the current pixel configuration name |
| [`getDeviceAdapterNames`](<#pymmcore_plus.CMMCorePlus.getDeviceAdapterNames>)() |  | [Devices](<#cmmcoreplus-devices>) | Return the names of discoverable device adapters. |
| [`getDeviceAdapterSearchPaths`](<#pymmcore_plus.CMMCorePlus.getDeviceAdapterSearchPaths>)() |  | [Devices](<#cmmcoreplus-devices>) | Return the current device adapter search paths. |
| [`getDeviceDelayMs`](<#pymmcore_plus.CMMCorePlus.getDeviceDelayMs>)(label) |  | [Devices](<#cmmcoreplus-devices>) | Reports action delay in milliseconds for the specific device. |
| [`getDeviceDescription`](<#pymmcore_plus.CMMCorePlus.getDeviceDescription>)(label) |  | [Devices](<#cmmcoreplus-devices>) | Returns description text for a given device label. "Description" is determined by the library and is immutable. |
| [`getDeviceInitializationState`](<#pymmcore_plus.CMMCorePlus.getDeviceInitializationState>)(label) | ➕ | [State devices](<#cmmcoreplus-state-devices>) | Queries the initialization state of the given device. |
| [`getDeviceLibrary`](<#pymmcore_plus.CMMCorePlus.getDeviceLibrary>)(label) |  | [Devices](<#cmmcoreplus-devices>) | Returns device library (aka module, device adapter) name. |
| [`getDeviceName`](<#pymmcore_plus.CMMCorePlus.getDeviceName>)(label) |  | [Devices](<#cmmcoreplus-devices>) | Returns device name for a given device label. |
| [`getDeviceObject`](<#pymmcore_plus.CMMCorePlus.getDeviceObject>)(device\_label, device\_type) (17 overloads) | ✨ | [Devices](<#cmmcoreplus-devices>) | Return a `Device` object bound to device\_label on this core. |
| [`getDevicePropertyNames`](<#pymmcore_plus.CMMCorePlus.getDevicePropertyNames>)(label) |  | [Properties](<#cmmcoreplus-properties>) | Returns all property names supported by the device. |
| [`getDeviceSchema`](<#pymmcore_plus.CMMCorePlus.getDeviceSchema>)(device\_label) | ✨ | [Devices](<#cmmcoreplus-devices>) | Return JSON-schema describing device `device_label` and its properties. |
| [`getDeviceTimeoutMs`](<#pymmcore_plus.CMMCorePlus.getDeviceTimeoutMs>)(label) |  | [Devices](<#cmmcoreplus-devices>) | Returns the per-device timeout in milliseconds, or the default if not set. |
| [`getDeviceType`](<#pymmcore_plus.CMMCorePlus.getDeviceType>)(label) | ➕ | [Devices](<#cmmcoreplus-devices>) | Return device type for a given device. |
| [`getExposure`](<#pymmcore_plus.CMMCorePlus.getExposure>)() (2 overloads) |  | [Cameras](<#cmmcoreplus-cameras>) | Returns the current exposure setting of the camera in milliseconds. |
| [`getExposureSequenceMaxLength`](<#pymmcore_plus.CMMCorePlus.getExposureSequenceMaxLength>)(cameraLabel) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Gets the maximum length of a camera's exposure sequence. |
| [`getFocusDevice`](<#pymmcore_plus.CMMCorePlus.getFocusDevice>)() |  | [Stages](<#cmmcoreplus-stages>) | Returns the label of the currently selected focus device. |
| [`getFocusDirection`](<#pymmcore_plus.CMMCorePlus.getFocusDirection>)(stageLabel) | ➕ | [Stages](<#cmmcoreplus-stages>) | Return device type for a given device. |
| [`getGalvoChannel`](<#pymmcore_plus.CMMCorePlus.getGalvoChannel>)(galvoLabel) |  | [Galvos](<#cmmcoreplus-galvos>) | Get the name of the active galvo channel (for a multi-laser galvo device). |
| [`getGalvoDevice`](<#pymmcore_plus.CMMCorePlus.getGalvoDevice>)() |  | [Galvos](<#cmmcoreplus-galvos>) | Returns the label of the currently selected Galvo device. |
| [`getGalvoPosition`](<#pymmcore_plus.CMMCorePlus.getGalvoPosition>)(galvoDevice) (2 overloads) |  | [Galvos](<#cmmcoreplus-galvos>) | Get x,y position of the galvo device. |
| [`getGalvoXMinimum`](<#pymmcore_plus.CMMCorePlus.getGalvoXMinimum>)(galvoLabel) |  | [Galvos](<#cmmcoreplus-galvos>) | Get the Galvo x minimum |
| [`getGalvoXRange`](<#pymmcore_plus.CMMCorePlus.getGalvoXRange>)(galvoLabel) |  | [Galvos](<#cmmcoreplus-galvos>) | Get the Galvo x range |
| [`getGalvoYMinimum`](<#pymmcore_plus.CMMCorePlus.getGalvoYMinimum>)(galvoLabel) |  | [Galvos](<#cmmcoreplus-galvos>) | Get the Galvo y minimum |
| [`getGalvoYRange`](<#pymmcore_plus.CMMCorePlus.getGalvoYRange>)(galvoLabel) |  | [Galvos](<#cmmcoreplus-galvos>) | Get the Galvo y range |
| [`getImage`](<#pymmcore_plus.CMMCorePlus.getImage>)(numChannel, fix) (2 overloads) | ➕ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Return the internal image buffer. |
| [`getImageBitDepth`](<#pymmcore_plus.CMMCorePlus.getImageBitDepth>)() |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | How many bits of dynamic range are to be expected from the camera. |
| [`getImageBufferSize`](<#pymmcore_plus.CMMCorePlus.getImageBufferSize>)() |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Returns the size of the internal image buffer. |
| [`getImageHeight`](<#pymmcore_plus.CMMCorePlus.getImageHeight>)() |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Vertical dimension of the image buffer in pixels. |
| [`getImageProcessorDevice`](<#pymmcore_plus.CMMCorePlus.getImageProcessorDevice>)() |  | [Cameras](<#cmmcoreplus-cameras>) | Returns the label of the currently selected image processor device. |
| [`getImageWidth`](<#pymmcore_plus.CMMCorePlus.getImageWidth>)() |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Horizontal dimension of the image buffer in pixels. |
| [`getInstalledDeviceDescription`](<#pymmcore_plus.CMMCorePlus.getInstalledDeviceDescription>)(hubLabel, peripheralLabel) |  | [Devices](<#cmmcoreplus-devices>) | Returns description from the specified peripheral on `hubLabel` device. |
| [`getInstalledDevices`](<#pymmcore_plus.CMMCorePlus.getInstalledDevices>)(hubLabel) |  | [Devices](<#cmmcoreplus-devices>) | Performs auto-detection and loading of child devices that are attached to a Hub device. |
| [`getLastFocusScore`](<#pymmcore_plus.CMMCorePlus.getLastFocusScore>)() |  | [Autofocus](<#cmmcoreplus-autofocus>) | Returns the latest focus score from the focusing device. |
| [`getLastImage`](<#pymmcore_plus.CMMCorePlus.getLastImage>)() |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Gets the last image from the circular buffer. |
| [`getLastImageAndMD`](<#pymmcore_plus.CMMCorePlus.getLastImageAndMD>)(channel, slice, fix) (2 overloads) | ✨ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Return last image from the circular buffer along with metadata. |
| [`getLastImageMD`](<#pymmcore_plus.CMMCorePlus.getLastImageMD>)(channel, slice, md) (2 overloads) |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Returns a pointer to the pixels of the image that was last inserted into the circular buffer. Also provides all metadata associated with that image |
| [`getLoadedDevices`](<#pymmcore_plus.CMMCorePlus.getLoadedDevices>)() |  | [Devices](<#cmmcoreplus-devices>) | Returns an array of labels for currently loaded devices. |
| [`getLoadedDevicesOfType`](<#pymmcore_plus.CMMCorePlus.getLoadedDevicesOfType>)(devType) |  | [Devices](<#cmmcoreplus-devices>) | Returns an array of labels for currently loaded devices of specific type. |
| [`getLoadedPeripheralDevices`](<#pymmcore_plus.CMMCorePlus.getLoadedPeripheralDevices>)(hubLabel) |  | [Devices](<#cmmcoreplus-devices>) | Return labels of all loaded peripherals of `hubLabel` device. |
| [`getMagnificationFactor`](<#pymmcore_plus.CMMCorePlus.getMagnificationFactor>)() |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Returns the product of all Magnifiers in the system or 1.0 when none is found. This is used internally by GetPixelSizeUm |
| [`getMMCoreVersionMajor`](<#pymmcore_plus.CMMCorePlus.getMMCoreVersionMajor>)() |  | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) |  |
| [`getMMCoreVersionMinor`](<#pymmcore_plus.CMMCorePlus.getMMCoreVersionMinor>)() |  | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) |  |
| [`getMMCoreVersionPatch`](<#pymmcore_plus.CMMCorePlus.getMMCoreVersionPatch>)() |  | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) |  |
| [`getMMDeviceDeviceInterfaceVersion`](<#pymmcore_plus.CMMCorePlus.getMMDeviceDeviceInterfaceVersion>)() |  | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) |  |
| [`getMMDeviceModuleInterfaceVersion`](<#pymmcore_plus.CMMCorePlus.getMMDeviceModuleInterfaceVersion>)() |  | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) |  |
| [`getMultiROI`](<#pymmcore_plus.CMMCorePlus.getMultiROI>)(\_) | ➕ | [Cameras](<#cmmcoreplus-cameras>) | Get multiple ROIs from the current camera device. |
| [`getNBeforeLastImageAndMD`](<#pymmcore_plus.CMMCorePlus.getNBeforeLastImageAndMD>)(n, fix) | ✨ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Return image taken `n` images ago along with associated metadata. |
| [`getNBeforeLastImageMD`](<#pymmcore_plus.CMMCorePlus.getNBeforeLastImageMD>)(n, md) |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Returns a pointer to the pixels of the image that was inserted n images ago. Also provides all metadata associated with that image |
| [`getNumberOfCameraChannels`](<#pymmcore_plus.CMMCorePlus.getNumberOfCameraChannels>)() |  | [Cameras](<#cmmcoreplus-cameras>) | Returns the number of simultaneous channels the default camera is returning. |
| [`getNumberOfComponents`](<#pymmcore_plus.CMMCorePlus.getNumberOfComponents>)() |  | [Cameras](<#cmmcoreplus-cameras>) | Returns the number of components the default camera is returning. |
| [`getNumberOfStates`](<#pymmcore_plus.CMMCorePlus.getNumberOfStates>)(stateDeviceLabel) |  | [State devices](<#cmmcoreplus-state-devices>) | Returns the total number of available positions (states). |
| [`getOrGuessChannelGroup`](<#pymmcore_plus.CMMCorePlus.getOrGuessChannelGroup>)() | ✨ | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Get the channelGroup or find a likely set of candidates. |
| [`getParentLabel`](<#pymmcore_plus.CMMCorePlus.getParentLabel>)(peripheralLabel) |  | [State devices](<#cmmcoreplus-state-devices>) | Returns parent device. Returns empty string if no parent is found. |
| [`getPhysicalCameraDevice`](<#pymmcore_plus.CMMCorePlus.getPhysicalCameraDevice>)(channel\_index) | ✨ | [Cameras](<#cmmcoreplus-cameras>) | Return the name of the actual camera device for a given channel index. |
| [`getPixelSizeAffine`](<#pymmcore_plus.CMMCorePlus.getPixelSizeAffine>)() (2 overloads) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Returns the current Affine Transform to related camera pixels with stage movement. |
| [`getPixelSizeAffineByID`](<#pymmcore_plus.CMMCorePlus.getPixelSizeAffineByID>)(resolutionID) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Returns the Affine Transform to related camera pixels with stage movement for the requested pixel size group. The raw affine transform without correction for binning and magnification will be returned. |
| [`getPixelSizeConfigData`](<#pymmcore_plus.CMMCorePlus.getPixelSizeConfigData>)(configName, native) (2 overloads) | ➕ | [Pixel size](<#cmmcoreplus-pixel-size>) | Return the configuration object for a given pixel size preset `configName`. |
| [`getPixelSizedxdz`](<#pymmcore_plus.CMMCorePlus.getPixelSizedxdz>)() (3 overloads) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Returns the angle between the camera's x axis and the axis (direction) of the z drive. |
| [`getPixelSizedydz`](<#pymmcore_plus.CMMCorePlus.getPixelSizedydz>)() (3 overloads) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Returns the angle between the camera's y axis and the axis (direction) of the z drive. |
| [`getPixelSizeOptimalZUm`](<#pymmcore_plus.CMMCorePlus.getPixelSizeOptimalZUm>)() (3 overloads) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Returns the optimal z step size in um, optionally using cached pixel configuration. |
| [`getPixelSizeUm`](<#pymmcore_plus.CMMCorePlus.getPixelSizeUm>)() (2 overloads) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Returns the current pixel size in microns. |
| [`getPixelSizeUmByID`](<#pymmcore_plus.CMMCorePlus.getPixelSizeUmByID>)(resolutionID) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Returns the pixel size in um for the requested pixel size group |
| [`getPosition`](<#pymmcore_plus.CMMCorePlus.getPosition>)() (2 overloads) |  | [Stages](<#cmmcoreplus-stages>) | Returns the current position of the current FocusDevice in microns. |
| [`getPrimaryLogFile`](<#pymmcore_plus.CMMCorePlus.getPrimaryLogFile>)() |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Return the name of the primary Core log file. |
| [`getPrimaryLogLevel`](<#pymmcore_plus.CMMCorePlus.getPrimaryLogLevel>)() |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Return the current primary log file level. |
| [`getProperty`](<#pymmcore_plus.CMMCorePlus.getProperty>)(label, propName) |  | [Properties](<#cmmcoreplus-properties>) | Returns the property value for the specified device. |
| [`getPropertyFromCache`](<#pymmcore_plus.CMMCorePlus.getPropertyFromCache>)(deviceLabel, propName) |  | [Properties](<#cmmcoreplus-properties>) | Returns the cached property value for the specified device. |
| [`getPropertyLowerLimit`](<#pymmcore_plus.CMMCorePlus.getPropertyLowerLimit>)(label, propName) |  | [Properties](<#cmmcoreplus-properties>) | Returns the property lower limit value, if the property has limits - 0 otherwise. |
| [`getPropertyObject`](<#pymmcore_plus.CMMCorePlus.getPropertyObject>)(device\_label, property\_name) | ✨ | [Properties](<#cmmcoreplus-properties>) | Return a DeviceProperty object bound to a device/property on this core. |
| [`getPropertySequenceMaxLength`](<#pymmcore_plus.CMMCorePlus.getPropertySequenceMaxLength>)(label, propName) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Queries device property for the maximum number of events that can be put in a sequence |
| [`getPropertyType`](<#pymmcore_plus.CMMCorePlus.getPropertyType>)(label, propName) | ➕ | [Properties](<#cmmcoreplus-properties>) | Return the intrinsic property type for a given device and property. |
| [`getPropertyUpperLimit`](<#pymmcore_plus.CMMCorePlus.getPropertyUpperLimit>)(label, propName) |  | [Properties](<#cmmcoreplus-properties>) | Returns the property upper limit value, if the property has limits - 0 otherwise. |
| [`getPumpFlowrate`](<#pymmcore_plus.CMMCorePlus.getPumpFlowrate>)(pumpLabel) |  | [Pumps](<#cmmcoreplus-pumps>) | Return the flowrate of the pump in uL per second |
| [`getPumpMaxVolume`](<#pymmcore_plus.CMMCorePlus.getPumpMaxVolume>)(pumpLabel) |  | [Pumps](<#cmmcoreplus-pumps>) | Return max volume of the pump in uL |
| [`getPumpPressureKPa`](<#pymmcore_plus.CMMCorePlus.getPumpPressureKPa>)(pumpLabel) |  | [Pumps](<#cmmcoreplus-pumps>) | Return the pressure of the pump in kPa. |
| [`getPumpVolume`](<#pymmcore_plus.CMMCorePlus.getPumpVolume>)(pumpLabel) |  | [Pumps](<#cmmcoreplus-pumps>) | Return the fluid volume in the pump in uL |
| [`getRemainingImageCount`](<#pymmcore_plus.CMMCorePlus.getRemainingImageCount>)() |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Returns number ofimages available in the Circular Buffer |
| [`getROI`](<#pymmcore_plus.CMMCorePlus.getROI>)() (2 overloads) |  | [Cameras](<#cmmcoreplus-cameras>) | Return the current hardware region of interest for a camera. |
| [`getSerialPortAnswer`](<#pymmcore_plus.CMMCorePlus.getSerialPortAnswer>)(portLabel, term) |  | [Serial ports](<#cmmcoreplus-serial-ports>) | Continuously read from the serial port until the terminating sequence is encountered. |
| [`getShutterDevice`](<#pymmcore_plus.CMMCorePlus.getShutterDevice>)() |  | [Shutters](<#cmmcoreplus-shutters>) | Returns the label of the currently selected shutter device. |
| [`getShutterOpen`](<#pymmcore_plus.CMMCorePlus.getShutterOpen>)() (2 overloads) |  | [Shutters](<#cmmcoreplus-shutters>) | Returns the state of the currently selected (default) shutter. |
| [`getSLMBytesPerPixel`](<#pymmcore_plus.CMMCorePlus.getSLMBytesPerPixel>)(slmLabel) |  | [SLMs](<#cmmcoreplus-slms>) | Returns the number of bytes per SLM pixel |
| [`getSLMDevice`](<#pymmcore_plus.CMMCorePlus.getSLMDevice>)() |  | [SLMs](<#cmmcoreplus-slms>) | Returns the label of the currently selected SLM device. |
| [`getSLMExposure`](<#pymmcore_plus.CMMCorePlus.getSLMExposure>)(slmLabel) |  | [SLMs](<#cmmcoreplus-slms>) | Returns the exposure time that will be used by the SLM for illumination |
| [`getSLMHeight`](<#pymmcore_plus.CMMCorePlus.getSLMHeight>)(slmLabel) |  | [SLMs](<#cmmcoreplus-slms>) | Returns the height (in "pixels") of the SLM |
| [`getSLMNumberOfComponents`](<#pymmcore_plus.CMMCorePlus.getSLMNumberOfComponents>)(slmLabel) |  | [SLMs](<#cmmcoreplus-slms>) | Returns the number of components (usually these depict colors) of the SLM. |
| [`getSLMSequenceMaxLength`](<#pymmcore_plus.CMMCorePlus.getSLMSequenceMaxLength>)(slmLabel) |  | [SLMs](<#cmmcoreplus-slms>) | For SLMs that support sequences, returns the maximum length of the sequence that can be uploaded to the device |
| [`getSLMWidth`](<#pymmcore_plus.CMMCorePlus.getSLMWidth>)(slmLabel) |  | [SLMs](<#cmmcoreplus-slms>) | Returns the width (in "pixels") of the SLM |
| [`getStageSequenceMaxLength`](<#pymmcore_plus.CMMCorePlus.getStageSequenceMaxLength>)(stageLabel) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Gets the maximum length of a stage's position sequence. |
| [`getState`](<#pymmcore_plus.CMMCorePlus.getState>)(stateDeviceLabel) |  | [State devices](<#cmmcoreplus-state-devices>) | Returns the current state (position) on the specific device. |
| [`getStateFromLabel`](<#pymmcore_plus.CMMCorePlus.getStateFromLabel>)(stateDeviceLabel, stateLabel) |  | [State devices](<#cmmcoreplus-state-devices>) | Obtain the state for a given label. |
| [`getStateLabel`](<#pymmcore_plus.CMMCorePlus.getStateLabel>)(stateDeviceLabel) |  | [State devices](<#cmmcoreplus-state-devices>) | Returns the current state as the label (string). |
| [`getStateLabels`](<#pymmcore_plus.CMMCorePlus.getStateLabels>)(stateDeviceLabel) |  | [State devices](<#cmmcoreplus-state-devices>) | Return labels for all states |
| [`getStderrLogLevel`](<#pymmcore_plus.CMMCorePlus.getStderrLogLevel>)() |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Return the current stderr log level. |
| [`getSystemState`](<#pymmcore_plus.CMMCorePlus.getSystemState>)(native) | ➕ | [State devices](<#cmmcoreplus-state-devices>) | Return the entire system state. |
| [`getSystemStateCache`](<#pymmcore_plus.CMMCorePlus.getSystemStateCache>)(native) (2 overloads) | ➕ | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) | Return the entire system state from cache. |
| [`getTaggedImage`](<#pymmcore_plus.CMMCorePlus.getTaggedImage>)(channel\_index) | ✨ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Return getImage as named tuple with metadata. |
| [`getTags`](<#pymmcore_plus.CMMCorePlus.getTags>)(meta, channel\_index) | ✨ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Return a dict of metadata tags for the state of the core. |
| [`getTimeoutMs`](<#pymmcore_plus.CMMCorePlus.getTimeoutMs>)() |  | [Devices](<#cmmcoreplus-devices>) | Get the timeout for all wait commands. |
| [`getVersionInfo`](<#pymmcore_plus.CMMCorePlus.getVersionInfo>)() |  | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) | Displays core version. |
| [`getXPosition`](<#pymmcore_plus.CMMCorePlus.getXPosition>)() (2 overloads) |  | [Stages](<#cmmcoreplus-stages>) | Obtains the current position of the X axis of the XY stage in microns. |
| [`getXYPosition`](<#pymmcore_plus.CMMCorePlus.getXYPosition>)() (2 overloads) |  | [Stages](<#cmmcoreplus-stages>) | Obtains the current position of the XY stage in microns. |
| [`getXYStageDevice`](<#pymmcore_plus.CMMCorePlus.getXYStageDevice>)() |  | [Stages](<#cmmcoreplus-stages>) | Returns the label of the currently selected XYStage device. |
| [`getXYStageSequenceMaxLength`](<#pymmcore_plus.CMMCorePlus.getXYStageSequenceMaxLength>)(xyStageLabel) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Gets the maximum length of an XY stage's position sequence. |
| [`getYPosition`](<#pymmcore_plus.CMMCorePlus.getYPosition>)() (2 overloads) |  | [Stages](<#cmmcoreplus-stages>) | Obtains the current position of the Y axis of the XY stage in microns. |
| [`getZPosition`](<#pymmcore_plus.CMMCorePlus.getZPosition>)() | ✨ | [Stages](<#cmmcoreplus-stages>) | Obtains the current position of the Z axis of the Z stage in microns. |
| [`guessObjectiveDevices`](<#pymmcore_plus.CMMCorePlus.guessObjectiveDevices>)() | ✨ | [State devices](<#cmmcoreplus-state-devices>) | Find any loaded devices that are likely to be an Objective/Nosepiece. |
| [`hasDeviceTimeout`](<#pymmcore_plus.CMMCorePlus.hasDeviceTimeout>)(label) |  | [Devices](<#cmmcoreplus-devices>) | Returns True if a per-device timeout has been set for the given device. |
| [`hasProperty`](<#pymmcore_plus.CMMCorePlus.hasProperty>)(label, propName) |  | [Properties](<#cmmcoreplus-properties>) | Checks if device has a property with a specified name. |
| [`hasPropertyLimits`](<#pymmcore_plus.CMMCorePlus.hasPropertyLimits>)(label, propName) |  | [Properties](<#cmmcoreplus-properties>) | Queries device if the specific property has limits. |
| [`home`](<#pymmcore_plus.CMMCorePlus.home>)(xyOrZStageLabel) |  | [Stages](<#cmmcoreplus-stages>) | Perform a hardware homing operation for an XY or focus/Z stage. |
| [`incrementalFocus`](<#pymmcore_plus.CMMCorePlus.incrementalFocus>)() |  | [Autofocus](<#cmmcoreplus-autofocus>) | Performs incremental focus for the one-shot focusing device. |
| [`initializeAllDevices`](<#pymmcore_plus.CMMCorePlus.initializeAllDevices>)() |  | [Devices](<#cmmcoreplus-devices>) | Calls Initialize() method for each loaded device. |
| [`initializeCircularBuffer`](<#pymmcore_plus.CMMCorePlus.initializeCircularBuffer>)() |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Initialize circular buffer based on the current camera settings. |
| [`initializeDevice`](<#pymmcore_plus.CMMCorePlus.initializeDevice>)(label) |  | [Devices](<#cmmcoreplus-devices>) | Initializes specific device. |
| [`instance`](<#pymmcore_plus.CMMCorePlus.instance>)(cls) | ✨ | [Other](<#cmmcoreplus-other>) | Return the global singleton instance of `CMMCorePlus`. |
| [`invertPumpDirection`](<#pymmcore_plus.CMMCorePlus.invertPumpDirection>)(pumpLabel, invert) |  | [Pumps](<#cmmcoreplus-pumps>) | Sets whether the pump direction needs to be inverted |
| [`isBufferOverflowed`](<#pymmcore_plus.CMMCorePlus.isBufferOverflowed>)() |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Indicates whether the circular buffer is overflowed |
| [`isConfigDefined`](<#pymmcore_plus.CMMCorePlus.isConfigDefined>)(groupName, configName) |  | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Checks if the configuration already exists within a group. |
| [`isContinuousFocusDrive`](<#pymmcore_plus.CMMCorePlus.isContinuousFocusDrive>)(stageLabel) |  | [Autofocus](<#cmmcoreplus-autofocus>) | Check if a stage has continuous focusing capability. |
| [`isContinuousFocusEnabled`](<#pymmcore_plus.CMMCorePlus.isContinuousFocusEnabled>)() |  | [Autofocus](<#cmmcoreplus-autofocus>) | Checks if the continuous focusing hardware device is ON or OFF. |
| [`isContinuousFocusLocked`](<#pymmcore_plus.CMMCorePlus.isContinuousFocusLocked>)() |  | [Autofocus](<#cmmcoreplus-autofocus>) | Returns the lock-in status of the continuous focusing device. |
| [`isExposureSequenceable`](<#pymmcore_plus.CMMCorePlus.isExposureSequenceable>)(cameraLabel) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Queries camera if exposure can be used in a sequence |
| [`isFeatureEnabled`](<#pymmcore_plus.CMMCorePlus.isFeatureEnabled>)(name) |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Return whether the given Core feature is currently enabled. |
| [`isGroupDefined`](<#pymmcore_plus.CMMCorePlus.isGroupDefined>)(groupName) |  | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Checks if the group already exists. |
| [`isMultiROIEnabled`](<#pymmcore_plus.CMMCorePlus.isMultiROIEnabled>)() |  | [Cameras](<#cmmcoreplus-cameras>) | Queries the camera to determine if multiple ROIs are currently set. |
| [`isMultiROISupported`](<#pymmcore_plus.CMMCorePlus.isMultiROISupported>)() |  | [Cameras](<#cmmcoreplus-cameras>) | Queries the camera to determine if it supports multiple ROIs. |
| [`isPixelSizeConfigDefined`](<#pymmcore_plus.CMMCorePlus.isPixelSizeConfigDefined>)(resolutionID) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Checks if the Pixel Size Resolution already exists |
| [`isPropertyPreInit`](<#pymmcore_plus.CMMCorePlus.isPropertyPreInit>)(label, propName) |  | [Properties](<#cmmcoreplus-properties>) | Tells us whether the property must be defined prior to initialization. |
| [`isPropertyReadOnly`](<#pymmcore_plus.CMMCorePlus.isPropertyReadOnly>)(label, propName) |  | [Properties](<#cmmcoreplus-properties>) | Tells us whether the property can be modified. |
| [`isPropertySequenceable`](<#pymmcore_plus.CMMCorePlus.isPropertySequenceable>)(label, propName) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Queries device if the specified property can be used in a sequence |
| [`isPumpDirectionInverted`](<#pymmcore_plus.CMMCorePlus.isPumpDirectionInverted>)(pumpLabel) |  | [Pumps](<#cmmcoreplus-pumps>) | Return True if pump direction needs to be inverted |
| [`isSequenceRunning`](<#pymmcore_plus.CMMCorePlus.isSequenceRunning>)() (2 overloads) |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Check if the current camera is acquiring the sequence. |
| [`isStageLinearSequenceable`](<#pymmcore_plus.CMMCorePlus.isStageLinearSequenceable>)(stageLabel) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Queries if the stage can be used in a linear sequence. |
| [`isStageSequenceable`](<#pymmcore_plus.CMMCorePlus.isStageSequenceable>)(stageLabel) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Queries stage if it can be used in a sequence |
| [`isStageUsingCallbacks`](<#pymmcore_plus.CMMCorePlus.isStageUsingCallbacks>)(stageLabel) |  | [Stages](<#cmmcoreplus-stages>) | Queries whether the stage uses callbacks to signal position changes. |
| [`isXYStageSequenceable`](<#pymmcore_plus.CMMCorePlus.isXYStageSequenceable>)(xyStageLabel) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Queries XY stage if it can be used in a sequence |
| [`isXYStageUsingCallbacks`](<#pymmcore_plus.CMMCorePlus.isXYStageUsingCallbacks>)(xyStageLabel) |  | [Stages](<#cmmcoreplus-stages>) | Queries whether the XY stage uses callbacks to signal position changes. |
| [`iterConfigGroups`](<#pymmcore_plus.CMMCorePlus.iterConfigGroups>)() | ✨ | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Iterate `ConfigGroup` objects for all configs. |
| [`iterDeviceAdapters`](<#pymmcore_plus.CMMCorePlus.iterDeviceAdapters>)(adapter\_pattern, as\_object) (2 overloads) | ✨ | [Devices](<#cmmcoreplus-devices>) | Iterate over all available device adapters. |
| [`iterDevices`](<#pymmcore_plus.CMMCorePlus.iterDevices>)(device\_type, device\_label, device\_adapter, as\_object) (2 overloads) | ✨ | [Devices](<#cmmcoreplus-devices>) | Iterate over currently loaded devices. |
| [`iterProperties`](<#pymmcore_plus.CMMCorePlus.iterProperties>)(property\_type, property\_name\_pattern, device\_type, device\_label, has\_limits, is\_read\_only, is\_sequenceable, as\_object) (2 overloads) | ✨ | [Properties](<#cmmcoreplus-properties>) | Iterate over currently loaded (device\_label, property\_name) pairs. |
| [`loadDevice`](<#pymmcore_plus.CMMCorePlus.loadDevice>)(label, moduleName, deviceName) | ➕ | [Devices](<#cmmcoreplus-devices>) | Load a device from the plugin library. |
| [`loadExposureSequence`](<#pymmcore_plus.CMMCorePlus.loadExposureSequence>)(cameraLabel, exposureSequence\_ms) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Transfer a sequence of exposure times to the camera. |
| [`loadGalvoPolygons`](<#pymmcore_plus.CMMCorePlus.loadGalvoPolygons>)(galvoLabel) |  | [Galvos](<#cmmcoreplus-galvos>) | Load a set of galvo polygons to the device |
| [`loadPropertySequence`](<#pymmcore_plus.CMMCorePlus.loadPropertySequence>)(label, propName, eventSequence) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Transfer a sequence of events/states/whatever to the device. |
| [`loadSLMSequence`](<#pymmcore_plus.CMMCorePlus.loadSLMSequence>)(slmLabel, imageSequence) |  | [SLMs](<#cmmcoreplus-slms>) | Load a sequence of images into the SLM |
| [`loadStageSequence`](<#pymmcore_plus.CMMCorePlus.loadStageSequence>)(stageLabel, positionSequence) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Transfer a sequence of events/states/whatever to the device. |
| [`loadSystemConfiguration`](<#pymmcore_plus.CMMCorePlus.loadSystemConfiguration>)(fileName) | ➕ | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) | Load a system config file conforming to the MM `.cfg` format. |
| [`loadSystemState`](<#pymmcore_plus.CMMCorePlus.loadSystemState>)(fileName) |  | [State devices](<#cmmcoreplus-state-devices>) | Loads the system configuration from the text file conforming to the MM specific format. |
| [`loadXYStageSequence`](<#pymmcore_plus.CMMCorePlus.loadXYStageSequence>)(xyStageLabel, xSequence, ySequence) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Transfer a sequence of stage positions to the xy stage. |
| [`log`](<#pymmcore_plus.CMMCorePlus.log>)(msg, level) (2 overloads) |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Log a message at the given level. |
| [`logMessage`](<#pymmcore_plus.CMMCorePlus.logMessage>)(msg) (2 overloads) |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Record text message in the log file. |
| [`mda`](<#pymmcore_plus.CMMCorePlus.mda>) | ✨ | [Acquisition engine &amp; events](<#cmmcoreplus-acquisition-engine-events>) | Return the `MDARunner` for this `CMMCorePlus` instance. |
| [`noop`](<#pymmcore_plus.CMMCorePlus.noop>)() |  | [Other](<#cmmcoreplus-other>) | A static method that does nothing. |
| [`objective_device_pattern`](<#pymmcore_plus.CMMCorePlus.objective_device_pattern>) | ✨ | [State devices](<#cmmcoreplus-state-devices>) | Pattern used to guess objective device labels. |
| [`pointGalvoAndFire`](<#pymmcore_plus.CMMCorePlus.pointGalvoAndFire>)(galvoLabel, x, y, pulseTime\_us) |  | [Galvos](<#cmmcoreplus-galvos>) | Set the Galvo to an x,y position and fire the laser for a predetermined duration. |
| [`popNextImage`](<#pymmcore_plus.CMMCorePlus.popNextImage>)(fix) | ➕ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Gets and removes the next image from the circular buffer. |
| [`popNextImageAndMD`](<#pymmcore_plus.CMMCorePlus.popNextImageAndMD>)(channel, slice, fix) (2 overloads) | ✨ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Gets and removes the next image (and metadata) from the circular buffer. |
| [`popNextImageMD`](<#pymmcore_plus.CMMCorePlus.popNextImageMD>)(channel, slice, md) (2 overloads) |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Gets and removes the next image (and metadata) from the circular buffer |
| [`popNextTaggedImage`](<#pymmcore_plus.CMMCorePlus.popNextTaggedImage>)(channel\_index) | ✨ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Return popNextImageAndMD as named tuple with metadata. |
| [`prepareSequenceAcquisition`](<#pymmcore_plus.CMMCorePlus.prepareSequenceAcquisition>)(cameraLabel) |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Prepare the camera for the sequence acquisition to save the time in the |
| [`pressurePumpCalibrate`](<#pymmcore_plus.CMMCorePlus.pressurePumpCalibrate>)(pumpLabel) |  | [Pumps](<#cmmcoreplus-pumps>) | Calibrates the pressure pump. |
| [`pressurePumpRequiresCalibration`](<#pymmcore_plus.CMMCorePlus.pressurePumpRequiresCalibration>)(pumpLabel) |  | [Pumps](<#cmmcoreplus-pumps>) | Return True if pump requires calibration before operation. |
| [`pressurePumpStop`](<#pymmcore_plus.CMMCorePlus.pressurePumpStop>)(pumpLabel) |  | [Pumps](<#cmmcoreplus-pumps>) | Stops the pressure pump. |
| [`pumpDispenseDurationSeconds`](<#pymmcore_plus.CMMCorePlus.pumpDispenseDurationSeconds>)(pumpLabel, seconds) |  | [Pumps](<#cmmcoreplus-pumps>) | Dispenses for the provided duration (in seconds) at the set flowrate. |
| [`pumpDispenseVolumeUl`](<#pymmcore_plus.CMMCorePlus.pumpDispenseVolumeUl>)(pumpLabel, microLiter) |  | [Pumps](<#cmmcoreplus-pumps>) | Dispenses the provided volume (in uL) at the set flowrate. |
| [`pumpStart`](<#pymmcore_plus.CMMCorePlus.pumpStart>)(pumpLabel) |  | [Pumps](<#cmmcoreplus-pumps>) | Start dispensing until syringe is empty, or manually stopped. |
| [`readFromSerialPort`](<#pymmcore_plus.CMMCorePlus.readFromSerialPort>)(portLabel) |  | [Serial ports](<#cmmcoreplus-serial-ports>) | Reads the contents of the Rx buffer. |
| [`register_mda_engine`](<#pymmcore_plus.CMMCorePlus.register_mda_engine>)(engine) | ✨ | [Acquisition engine &amp; events](<#cmmcoreplus-acquisition-engine-events>) | Set the MDA Engine to be used on `run_mda`. |
| [`registerCallback`](<#pymmcore_plus.CMMCorePlus.registerCallback>)(\_) | ➕ | [Acquisition engine &amp; events](<#cmmcoreplus-acquisition-engine-events>) | \*registerCallback is disallowed in pymmcore-plus!\* |
| [`renameConfig`](<#pymmcore_plus.CMMCorePlus.renameConfig>)(groupName, oldConfigName, newConfigName) |  | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Renames a configuration within a specified group. |
| [`renameConfigGroup`](<#pymmcore_plus.CMMCorePlus.renameConfigGroup>)(oldGroupName, newGroupName) |  | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Renames a configuration group. |
| [`renamePixelSizeConfig`](<#pymmcore_plus.CMMCorePlus.renamePixelSizeConfig>)(oldConfigName, newConfigName) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Renames a pixel size configuration. |
| [`reset`](<#pymmcore_plus.CMMCorePlus.reset>)() |  | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) | Unloads all devices from the core, clears all configuration data and property blocks. |
| [`run_mda`](<#pymmcore_plus.CMMCorePlus.run_mda>)(events, output, block, dimension\_overrides) | ✨ | [Acquisition engine &amp; events](<#cmmcoreplus-acquisition-engine-events>) | Run a sequence of useq.MDAEvent on a new thread. |
| [`runGalvoPolygons`](<#pymmcore_plus.CMMCorePlus.runGalvoPolygons>)(galvoLabel) |  | [Galvos](<#cmmcoreplus-galvos>) | Run a loop of galvo polygons |
| [`runGalvoSequence`](<#pymmcore_plus.CMMCorePlus.runGalvoSequence>)(galvoLabel) |  | [Galvos](<#cmmcoreplus-galvos>) | Run a sequence of galvo positions |
| [`saveSystemConfiguration`](<#pymmcore_plus.CMMCorePlus.saveSystemConfiguration>)(filename) | ➕ | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) | Saves the current system configuration to a text file. |
| [`saveSystemState`](<#pymmcore_plus.CMMCorePlus.saveSystemState>)(fileName) |  | [State devices](<#cmmcoreplus-state-devices>) | Saves the current system state to a text file of the MM specific format. |
| [`setAdapterOrigin`](<#pymmcore_plus.CMMCorePlus.setAdapterOrigin>)(newZUm) (2 overloads) |  | [Stages](<#cmmcoreplus-stages>) | Enable software translation of coordinates for the current focus/Z stage. |
| [`setAdapterOriginXY`](<#pymmcore_plus.CMMCorePlus.setAdapterOriginXY>)(newXUm, newYUm) (2 overloads) |  | [Stages](<#cmmcoreplus-stages>) | Enable software translation of coordinates for the current XY stage. |
| [`setAutoFocusDevice`](<#pymmcore_plus.CMMCorePlus.setAutoFocusDevice>)(focusLabel) |  | [Autofocus](<#cmmcoreplus-autofocus>) | Sets the current auto-focus device. |
| [`setAutoFocusOffset`](<#pymmcore_plus.CMMCorePlus.setAutoFocusOffset>)(offset) | ➕ | [Autofocus](<#cmmcoreplus-autofocus>) | Applies offset the one-shot focusing device. |
| [`setAutoShutter`](<#pymmcore_plus.CMMCorePlus.setAutoShutter>)(state) | ➕ | [Shutters](<#cmmcoreplus-shutters>) | Set shutter to automatically open and close when an image is acquired. |
| [`setBinning`](<#pymmcore_plus.CMMCorePlus.setBinning>)(binning) (2 overloads) |  | [Cameras](<#cmmcoreplus-cameras>) | Sets the binning factor of the current camera. |
| [`setCameraDevice`](<#pymmcore_plus.CMMCorePlus.setCameraDevice>)(cameraLabel) |  | [Cameras](<#cmmcoreplus-cameras>) | Sets the current camera device. |
| [`setChannelGroup`](<#pymmcore_plus.CMMCorePlus.setChannelGroup>)(channelGroup) | ➕ | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Specifies the group determining the channel selection. |
| [`setCircularBufferMemoryFootprint`](<#pymmcore_plus.CMMCorePlus.setCircularBufferMemoryFootprint>)(sizeMB) |  | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Reserve memory for the circular buffer. |
| [`setConfig`](<#pymmcore_plus.CMMCorePlus.setConfig>)(groupName, configName) | ➕ | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Applies a configuration to a group. |
| [`setContext`](<#pymmcore_plus.CMMCorePlus.setContext>)(kwargs) | ✨ | [Acquisition engine &amp; events](<#cmmcoreplus-acquisition-engine-events>) | Set core properties in a context restoring the initial values on exit. |
| [`setDeviceAdapterSearchPaths`](<#pymmcore_plus.CMMCorePlus.setDeviceAdapterSearchPaths>)(paths) | ➕ | [Devices](<#cmmcoreplus-devices>) | Set the device adapter search paths. |
| [`setDeviceDelayMs`](<#pymmcore_plus.CMMCorePlus.setDeviceDelayMs>)(label, delayMs) |  | [Devices](<#cmmcoreplus-devices>) | Overrides the built-in value for the action delay. |
| [`setDeviceTimeoutMs`](<#pymmcore_plus.CMMCorePlus.setDeviceTimeoutMs>)(label, timeoutMs) |  | [Devices](<#cmmcoreplus-devices>) | Sets a per-device timeout in milliseconds. |
| [`setExposure`](<#pymmcore_plus.CMMCorePlus.setExposure>)(exp) (2 overloads) |  | [Cameras](<#cmmcoreplus-cameras>) | Sets the exposure setting of the current camera in milliseconds. |
| [`setFocusDevice`](<#pymmcore_plus.CMMCorePlus.setFocusDevice>)(focusLabel) | ➕ | [Stages](<#cmmcoreplus-stages>) | Set the current Focus Device and emit a `propertyChanged` signal. |
| [`setFocusDirection`](<#pymmcore_plus.CMMCorePlus.setFocusDirection>)(stageLabel, sign) |  | [Stages](<#cmmcoreplus-stages>) | Set the focus direction of a stage. |
| [`setGalvoDevice`](<#pymmcore_plus.CMMCorePlus.setGalvoDevice>)(galvoLabel) |  | [Galvos](<#cmmcoreplus-galvos>) | Sets the current galvo device. |
| [`setGalvoIlluminationState`](<#pymmcore_plus.CMMCorePlus.setGalvoIlluminationState>)(galvoLabel, on) |  | [Galvos](<#cmmcoreplus-galvos>) | Set the galvo's illumination state to on or off |
| [`setGalvoPolygonRepetitions`](<#pymmcore_plus.CMMCorePlus.setGalvoPolygonRepetitions>)(galvoLabel, repetitions) |  | [Galvos](<#cmmcoreplus-galvos>) | Set the number of times to loop galvo polygons |
| [`setGalvoPosition`](<#pymmcore_plus.CMMCorePlus.setGalvoPosition>)(galvoLabel, x, y) |  | [Galvos](<#cmmcoreplus-galvos>) | Set the Galvo to an x,y position. |
| [`setGalvoSpotInterval`](<#pymmcore_plus.CMMCorePlus.setGalvoSpotInterval>)(galvoLabel, pulseTime\_us) |  | [Galvos](<#cmmcoreplus-galvos>) | Set the SpotInterval for the specified galvo device. |
| [`setImageProcessorDevice`](<#pymmcore_plus.CMMCorePlus.setImageProcessorDevice>)(procLabel) |  | [Cameras](<#cmmcoreplus-cameras>) | Sets the current image processor device. |
| [`setMultiROI`](<#pymmcore_plus.CMMCorePlus.setMultiROI>)(xs, ys, widths, heights) |  | [Cameras](<#cmmcoreplus-cameras>) | Set multiple ROIs for the current camera device. |
| [`setOrigin`](<#pymmcore_plus.CMMCorePlus.setOrigin>)() (2 overloads) |  | [Stages](<#cmmcoreplus-stages>) | Zero the current focus/Z stage's coordinates at the current position. |
| [`setOriginX`](<#pymmcore_plus.CMMCorePlus.setOriginX>)() (2 overloads) |  | [Stages](<#cmmcoreplus-stages>) | Zero the given XY stage's X coordinate at the current position. |
| [`setOriginXY`](<#pymmcore_plus.CMMCorePlus.setOriginXY>)() (2 overloads) |  | [Stages](<#cmmcoreplus-stages>) | Zero the current XY stage's coordinates at the current position. |
| [`setOriginY`](<#pymmcore_plus.CMMCorePlus.setOriginY>)() (2 overloads) |  | [Stages](<#cmmcoreplus-stages>) | Zero the given XY stage's Y coordinate at the current position. |
| [`setParentLabel`](<#pymmcore_plus.CMMCorePlus.setParentLabel>)(deviceLabel, parentHubLabel) |  | [State devices](<#cmmcoreplus-state-devices>) | Sets parent device label |
| [`setPixelSizeAffine`](<#pymmcore_plus.CMMCorePlus.setPixelSizeAffine>)(resolutionID, affine) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Sets the raw affine transform for the specific pixel size configuration. |
| [`setPixelSizeConfig`](<#pymmcore_plus.CMMCorePlus.setPixelSizeConfig>)(resolutionID) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Applies a Pixel Size Configuration. |
| [`setPixelSizedxdz`](<#pymmcore_plus.CMMCorePlus.setPixelSizedxdz>)(resolutionID, dXdZ) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Sets the pixel size in the X direction in microns. |
| [`setPixelSizedydz`](<#pymmcore_plus.CMMCorePlus.setPixelSizedydz>)(resolutionID, dYdZ) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Sets the pixel size in the Y direction in microns. |
| [`setPixelSizeOptimalZUm`](<#pymmcore_plus.CMMCorePlus.setPixelSizeOptimalZUm>)(resolutionID, optimalZ) |  | [Pixel size](<#cmmcoreplus-pixel-size>) | Sets the pixel size in the Z direction in microns. |
| [`setPixelSizeUm`](<#pymmcore_plus.CMMCorePlus.setPixelSizeUm>)(resolutionID, pixSize) | ➕ | [Pixel size](<#cmmcoreplus-pixel-size>) | Set pixel size in microns for the specified `resolutionID`. |
| [`setPosition`](<#pymmcore_plus.CMMCorePlus.setPosition>)(position) (2 overloads) |  | [Stages](<#cmmcoreplus-stages>) | Sets the position of the current FocusDevice in microns. |
| [`setPrimaryLogFile`](<#pymmcore_plus.CMMCorePlus.setPrimaryLogFile>)(filename) (2 overloads) |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Set the primary Core log file. |
| [`setPrimaryLogFileRotation`](<#pymmcore_plus.CMMCorePlus.setPrimaryLogFileRotation>)(maxFileSize, maxBackupCount) |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Set the primary log file rotation parameters. |
| [`setPrimaryLogLevel`](<#pymmcore_plus.CMMCorePlus.setPrimaryLogLevel>)(level) |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Set the log level for the primary log file. |
| [`setProperty`](<#pymmcore_plus.CMMCorePlus.setProperty>)(label, propName, propValue) | ➕ | [Properties](<#cmmcoreplus-properties>) | Set property named `propName` on device `label` to `propValue`. |
| [`setPumpFlowrate`](<#pymmcore_plus.CMMCorePlus.setPumpFlowrate>)(pumpLabel, volume) |  | [Pumps](<#cmmcoreplus-pumps>) | Set the flowrate of the pump in uL per second |
| [`setPumpMaxVolume`](<#pymmcore_plus.CMMCorePlus.setPumpMaxVolume>)(pumpLabel, volume) |  | [Pumps](<#cmmcoreplus-pumps>) | Set the max volume of the pump in uL |
| [`setPumpPressureKPa`](<#pymmcore_plus.CMMCorePlus.setPumpPressureKPa>)(pumpLabel, pressure) |  | [Pumps](<#cmmcoreplus-pumps>) | Sets the pressure of the pump in kPa. |
| [`setPumpVolume`](<#pymmcore_plus.CMMCorePlus.setPumpVolume>)(pumpLabel, volume) |  | [Pumps](<#cmmcoreplus-pumps>) | Sets the volume of fluid in the pump in uL. |
| [`setRelativePosition`](<#pymmcore_plus.CMMCorePlus.setRelativePosition>)(d) (2 overloads) |  | [Stages](<#cmmcoreplus-stages>) | Sets the relative position of the stage in microns. |
| [`setRelativeXYPosition`](<#pymmcore_plus.CMMCorePlus.setRelativeXYPosition>)(dx, dy) (2 overloads) |  | [Stages](<#cmmcoreplus-stages>) | Sets the relative position of the XY stage in microns. |
| [`setRelativeXYZPosition`](<#pymmcore_plus.CMMCorePlus.setRelativeXYZPosition>)(dx, dy, dz) | ✨ | [Stages](<#cmmcoreplus-stages>) | Sets the relative XYZ position in microns. |
| [`setROI`](<#pymmcore_plus.CMMCorePlus.setROI>)(args) (2 overloads) | ➕ | [Cameras](<#cmmcoreplus-cameras>) | Set the camera Region of Interest (ROI). |
| [`setSerialPortCommand`](<#pymmcore_plus.CMMCorePlus.setSerialPortCommand>)(portLabel, command, term) |  | [Serial ports](<#cmmcoreplus-serial-ports>) | Send string to the serial device and return an answer. |
| [`setSerialProperties`](<#pymmcore_plus.CMMCorePlus.setSerialProperties>)(portName, answerTimeout, baudRate, delayBetweenCharsMs, handshaking, parity, stopBits) |  | [Serial ports](<#cmmcoreplus-serial-ports>) | Sets all com port properties in a single call. |
| [`setShutterDevice`](<#pymmcore_plus.CMMCorePlus.setShutterDevice>)(shutterLabel) |  | [Shutters](<#cmmcoreplus-shutters>) | the current shutter device. |
| [`setShutterOpen`](<#pymmcore_plus.CMMCorePlus.setShutterOpen>)(args) (2 overloads) | ➕ | [Shutters](<#cmmcoreplus-shutters>) | Open or close the currently selected or `shutterLabel` shutter. |
| [`setSLMDevice`](<#pymmcore_plus.CMMCorePlus.setSLMDevice>)(slmLabel) |  | [SLMs](<#cmmcoreplus-slms>) | Sets the current slm device. |
| [`setSLMExposure`](<#pymmcore_plus.CMMCorePlus.setSLMExposure>)(slmLabel, exposure\_ms) |  | [SLMs](<#cmmcoreplus-slms>) | For SLM devices with build-in light source (such as projectors), this will set the exposure time, but not (yet) start the illumination |
| [`setSLMImage`](<#pymmcore_plus.CMMCorePlus.setSLMImage>)(slmLabel, pixels) (2 overloads) |  | [SLMs](<#cmmcoreplus-slms>) | Write an image to the SLM . |
| [`setSLMPixelsTo`](<#pymmcore_plus.CMMCorePlus.setSLMPixelsTo>)(slmLabel, intensity) (2 overloads) |  | [SLMs](<#cmmcoreplus-slms>) | Set all SLM pixels to a single 8-bit intensity. |
| [`setStageLinearSequence`](<#pymmcore_plus.CMMCorePlus.setStageLinearSequence>)(stageLabel, dZ\_um, nSlices) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Loads a linear sequence (defined by stepsize and nr. of steps) into the device. |
| [`setState`](<#pymmcore_plus.CMMCorePlus.setState>)(stateDeviceLabel, state) | ➕ | [State devices](<#cmmcoreplus-state-devices>) | Set state (by position) on `stateDeviceLabel`, with reliable event emission. |
| [`setStateLabel`](<#pymmcore_plus.CMMCorePlus.setStateLabel>)(stateDeviceLabel, stateLabel) | ➕ | [State devices](<#cmmcoreplus-state-devices>) | Set state (by label) on `stateDeviceLabel`, with reliable event emission. |
| [`setStderrLogLevel`](<#pymmcore_plus.CMMCorePlus.setStderrLogLevel>)(level) |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Set the stderr log level. |
| [`setSystemState`](<#pymmcore_plus.CMMCorePlus.setSystemState>)(conf) |  | [State devices](<#cmmcoreplus-state-devices>) | Sets all properties contained in the Configuration object. |
| [`setTimeoutMs`](<#pymmcore_plus.CMMCorePlus.setTimeoutMs>)(timeoutMs) |  | [Devices](<#cmmcoreplus-devices>) | Sets the timeout for all wait commands. |
| [`setXYPosition`](<#pymmcore_plus.CMMCorePlus.setXYPosition>)(args) (2 overloads) | ➕ | [Stages](<#cmmcoreplus-stages>) | Sets the position of the XY stage in microns. |
| [`setXYStageDevice`](<#pymmcore_plus.CMMCorePlus.setXYStageDevice>)(xyStageLabel) |  | [Stages](<#cmmcoreplus-stages>) | Sets the current XY device. |
| [`setZPosition`](<#pymmcore_plus.CMMCorePlus.setZPosition>)(val) | ✨ | [Stages](<#cmmcoreplus-stages>) | Set the position of the current focus device in microns. |
| [`sleep`](<#pymmcore_plus.CMMCorePlus.sleep>)(intervalMs) |  | [Other](<#cmmcoreplus-other>) | Waits (blocks the calling thread) for specified time in milliseconds. |
| [`snap`](<#pymmcore_plus.CMMCorePlus.snap>)(numChannel, fix) | ✨ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Snap and return an image. |
| [`snapImage`](<#pymmcore_plus.CMMCorePlus.snapImage>)() | ➕ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Acquires a single image with current settings. |
| [`startContinuousSequenceAcquisition`](<#pymmcore_plus.CMMCorePlus.startContinuousSequenceAcquisition>)(intervalMs) | ➕ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Start a ContinuousSequenceAcquisition. |
| [`startExposureSequence`](<#pymmcore_plus.CMMCorePlus.startExposureSequence>)(cameraLabel) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Starts an ongoing sequence of triggered exposures in a camera. |
| [`startPropertySequence`](<#pymmcore_plus.CMMCorePlus.startPropertySequence>)(label, propName) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Starts an ongoing sequence of triggered events in a property of a device. |
| [`startSecondaryLogFile`](<#pymmcore_plus.CMMCorePlus.startSecondaryLogFile>)(filename, enableDebug) (3 overloads) |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Start capturing logging output into an additional file. |
| [`startSequenceAcquisition`](<#pymmcore_plus.CMMCorePlus.startSequenceAcquisition>)(args) (2 overloads) | ➕ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Starts streaming camera sequence acquisition. |
| [`startSLMSequence`](<#pymmcore_plus.CMMCorePlus.startSLMSequence>)(slmLabel) |  | [SLMs](<#cmmcoreplus-slms>) | Starts the sequence previously uploaded to the SLM |
| [`startStageSequence`](<#pymmcore_plus.CMMCorePlus.startStageSequence>)(stageLabel) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Starts an ongoing sequence of triggered events in a stage. |
| [`startXYStageSequence`](<#pymmcore_plus.CMMCorePlus.startXYStageSequence>)(xyStageLabel) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Starts an ongoing sequence of triggered events in an XY stage. |
| [`state`](<#pymmcore_plus.CMMCorePlus.state>)(cached, include\_time, \_kwargs) | ✨ | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) | Return info on the current state of the core. |
| [`stderrLogEnabled`](<#pymmcore_plus.CMMCorePlus.stderrLogEnabled>)() |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Indicates whether logging output goes to stdErr |
| [`stop`](<#pymmcore_plus.CMMCorePlus.stop>)(xyOrZStageLabel) |  | [Stages](<#cmmcoreplus-stages>) | Stop the XY or focus/Z stage motors |
| [`stopExposureSequence`](<#pymmcore_plus.CMMCorePlus.stopExposureSequence>)(cameraLabel) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Stops an ongoing sequence of triggered exposures in a camera. |
| [`stopPropertySequence`](<#pymmcore_plus.CMMCorePlus.stopPropertySequence>)(label, propName) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Stops an ongoing sequence of triggered events in a property of a device. |
| [`stopSecondaryLogFile`](<#pymmcore_plus.CMMCorePlus.stopSecondaryLogFile>)(handle) |  | [Logging &amp; errors](<#cmmcoreplus-logging-errors>) | Stop capturing logging output into an additional file. |
| [`stopSequenceAcquisition`](<#pymmcore_plus.CMMCorePlus.stopSequenceAcquisition>)(cameraLabel) | ➕ | [Images &amp; buffer](<#cmmcoreplus-images-buffer>) | Stops streaming camera sequence acquisition. |
| [`stopSLMSequence`](<#pymmcore_plus.CMMCorePlus.stopSLMSequence>)(slmLabel) |  | [SLMs](<#cmmcoreplus-slms>) | Stops the SLM sequence if previously started |
| [`stopStageSequence`](<#pymmcore_plus.CMMCorePlus.stopStageSequence>)(stageLabel) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Stops an ongoing sequence of triggered events in a stage. |
| [`stopXYStageSequence`](<#pymmcore_plus.CMMCorePlus.stopXYStageSequence>)(xyStageLabel) |  | [Hardware sequencing](<#cmmcoreplus-hardware-sequencing>) | Stops an ongoing sequence of triggered events in an XY stage. |
| [`supportsDeviceDetection`](<#pymmcore_plus.CMMCorePlus.supportsDeviceDetection>)(deviceLabel) |  | [Devices](<#cmmcoreplus-devices>) | Return whether or not the device supports automatic device detection (i.e. |
| [`systemBusy`](<#pymmcore_plus.CMMCorePlus.systemBusy>)() |  | [Devices](<#cmmcoreplus-devices>) | Checks the busy status of the entire system. |
| [`systemConfigurationFile`](<#pymmcore_plus.CMMCorePlus.systemConfigurationFile>)() | ✨ | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) | Return the path to the last loaded system configuration file, or `None`. |
| [`unloadAllDevices`](<#pymmcore_plus.CMMCorePlus.unloadAllDevices>)() | ➕ | [Devices](<#cmmcoreplus-devices>) | Unload all devices from the core and reset all configuration data. |
| [`unloadDevice`](<#pymmcore_plus.CMMCorePlus.unloadDevice>)(label) |  | [Devices](<#cmmcoreplus-devices>) | Unloads the device from the core and adjusts all configuration data. |
| [`unloadLibrary`](<#pymmcore_plus.CMMCorePlus.unloadLibrary>)(moduleName) |  | [Devices](<#cmmcoreplus-devices>) | Forcefully unload a library. |
| [`unsetDeviceTimeout`](<#pymmcore_plus.CMMCorePlus.unsetDeviceTimeout>)(label) |  | [Devices](<#cmmcoreplus-devices>) | Removes any per-device timeout, restoring the default. |
| [`updateCoreProperties`](<#pymmcore_plus.CMMCorePlus.updateCoreProperties>)() |  | [Properties](<#cmmcoreplus-properties>) | Updates CoreProperties (currently all Core properties are devices types) with the loaded hardware. |
| [`updateSystemStateCache`](<#pymmcore_plus.CMMCorePlus.updateSystemStateCache>)() |  | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) | Updates the state of the entire hardware. |
| [`usesDeviceDelay`](<#pymmcore_plus.CMMCorePlus.usesDeviceDelay>)(label) |  | [Devices](<#cmmcoreplus-devices>) | Signals if the device will use the delay setting or not. |
| [`volumetricPumpHome`](<#pymmcore_plus.CMMCorePlus.volumetricPumpHome>)(pumpLabel) |  | [Pumps](<#cmmcoreplus-pumps>) | Homes the volumetric pump. |
| [`volumetricPumpRequiresHoming`](<#pymmcore_plus.CMMCorePlus.volumetricPumpRequiresHoming>)(pumpLabel) |  | [Pumps](<#cmmcoreplus-pumps>) | Return True if the volumetric pump requires homing. |
| [`volumetricPumpStop`](<#pymmcore_plus.CMMCorePlus.volumetricPumpStop>)(pumpLabel) |  | [Pumps](<#cmmcoreplus-pumps>) | Stops the volumetric pump. |
| [`waitForConfig`](<#pymmcore_plus.CMMCorePlus.waitForConfig>)(group, configName) |  | [Config groups &amp; presets](<#cmmcoreplus-config-groups-presets>) | Blocks until all devices included in the configuration become ready. |
| [`waitForDevice`](<#pymmcore_plus.CMMCorePlus.waitForDevice>)(label) |  | [Devices](<#cmmcoreplus-devices>) | Waits (blocks the calling thread) until the specified device becomes non-busy. |
| [`waitForDeviceType`](<#pymmcore_plus.CMMCorePlus.waitForDeviceType>)(devType) |  | [Devices](<#cmmcoreplus-devices>) | Blocks until all devices of the specific type become ready (not-busy). |
| [`waitForSystem`](<#pymmcore_plus.CMMCorePlus.waitForSystem>)() |  | [System state &amp; configuration files](<#cmmcoreplus-system-state-configuration-files>) | Blocks until all devices in the system become ready (not-busy). |
| [`writeToSerialPort`](<#pymmcore_plus.CMMCorePlus.writeToSerialPort>)(portLabel, data) |  | [Serial ports](<#cmmcoreplus-serial-ports>) | Sends an array of characters to the serial port and returns immediately. |

## Acquisition engine &amp; events

### events

```python
events: PCoreSignaler
```

Signaler for core events.

✨ *This method is new in `CMMCorePlus`.*

This attribute allows connecting callbacks to various events that occur within the core. See `pymmcore_plus.core.events.PCoreSignaler` documentation for details of the available signals, and how to connect to them.

### mda

```python
mda: MDARunner
```

Return the `MDARunner` for this `CMMCorePlus` instance.

✨ *This method is new in `CMMCorePlus`.*

### register\_mda\_engine

```python
register_mda_engine(engine: PMDAEngine) -> None
```

Set the MDA Engine to be used on `run_mda`.

✨ *This method is new in `CMMCorePlus`.*

This will unregister the previous engine and emit an `mdaEngineRegistered` signal. The current Engine must not be running an MDA in order to register a new engine.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `engine` | `PMDAEngine` | Any object conforming to the PMDAEngine protocol. | *required* |

### registerCallback

```python
registerCallback(*_: Never) -> Never
```

*registerCallback is disallowed in pymmcore-plus!*

If you want to connect callbacks to events, use the `CMMCorePlus.events` property instead.

### run\_mda

```python
run_mda(
    events: Iterable[MDAEvent],
    *,
    output: SingleOutput | Sequence[SingleOutput] | None = None,
    block: bool = False,
    dimension_overrides: dict[str, DimensionOverride] | None = None,
) -> Thread
```

Run a sequence of useq.MDAEvent on a new thread.

✨ *This method is new in `CMMCorePlus`.*

The currently registered MDAEngine (`core.mda.engine`) will be responsible for executing the acquisition.

After starting the sequence you can pause or cancel the mda with the mda object's `set_paused` and `cancel` methods.

Parameters:

<table>       <thead>         <tr>           <th>Name</th>           <th>Type</th>           <th>Description</th>           <th>Default</th>         </tr>       </thead>       <tbody>           <tr class="doc-section-item">             <td>                 <code>events</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.CMMCorePlus.run_mda" backlink-type="used-by" hover="" identifier="collections.abc.Iterable" optional="">Iterable</autoref>[<autoref backlink-anchor="pymmcore_plus.CMMCorePlus.run_mda" backlink-type="used-by" hover="" identifier="useq.MDAEvent" optional="">MDAEvent</autoref>]</code>             </td>             <td>               <div class="doc-md-description">                 <p>An iterable of <autoref data-zensical-autoref="" domain="py" filepath="/Users/runner/work/pymmcore-plus.github.io/pymmcore-plus.github.io/.repos/pymmcore-plus/src/pymmcore_plus/core/_mmcore_plus.py" identifier="useq.MDAEvent" lineno="1630" origin="pymmcore_plus.CMMCorePlus.run_mda" role="meth" slug="useqmdaevent">useq.MDAEvent</autoref> to execute.  This may be an instance of <autoref data-zensical-autoref="" domain="py" filepath="/Users/runner/work/pymmcore-plus.github.io/pymmcore-plus.github.io/.repos/pymmcore-plus/src/pymmcore_plus/core/_mmcore_plus.py" identifier="useq.MDASequence" lineno="1630" origin="pymmcore_plus.CMMCorePlus.run_mda" role="meth" slug="useqmdasequence">useq.MDASequence</autoref>, or any other iterable of <autoref data-zensical-autoref="" domain="py" filepath="/Users/runner/work/pymmcore-plus.github.io/pymmcore-plus.github.io/.repos/pymmcore-plus/src/pymmcore_plus/core/_mmcore_plus.py" identifier="useq.MDAEvent" lineno="1630" origin="pymmcore_plus.CMMCorePlus.run_mda" role="meth" slug="useqmdaevent">useq.MDAEvent</autoref>.</p>                </div>             </td>             <td>                 <em>required</em>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>output</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.CMMCorePlus.run_mda" backlink-type="used-by" hover="" identifier="pymmcore_plus.mda._runner.SingleOutput" optional="">SingleOutput</autoref> | <autoref backlink-anchor="pymmcore_plus.CMMCorePlus.run_mda" backlink-type="used-by" hover="" identifier="collections.abc.Sequence" optional="">Sequence</autoref>[<autoref backlink-anchor="pymmcore_plus.CMMCorePlus.run_mda" backlink-type="used-by" hover="" identifier="pymmcore_plus.mda._runner.SingleOutput" optional="">SingleOutput</autoref>] | None</code>             </td>             <td>               <div class="doc-md-description">                 <p>The output handler(s) to use.  If None, no output will be saved. &quot;SingleOutput&quot; can be any of the following:</p> <ul> <li>A string or Path to a directory to save images to. A handler will be     created automatically based on the extension of the path.</li> <li>A handler object that implements the <code>DataHandler</code> protocol, currently     meaning it has a <code>frameReady</code> method.  See <code>mda_listeners_connected</code>     for more details.</li> <li>A sequence of either of the above. (all will be connected)</li> </ul>                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>block</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.CMMCorePlus.run_mda" backlink-type="used-by" identifier="bool" optional="">bool</autoref></code>             </td>             <td>               <div class="doc-md-description">                 <p>If True, block until the sequence is complete, by default False.</p>                </div>             </td>             <td>                   <code>False</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>dimension_overrides</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.CMMCorePlus.run_mda" backlink-type="used-by" identifier="dict" optional="">dict</autoref>[<autoref backlink-anchor="pymmcore_plus.CMMCorePlus.run_mda" backlink-type="used-by" identifier="str" optional="">str</autoref>, <autoref backlink-anchor="pymmcore_plus.CMMCorePlus.run_mda" backlink-type="used-by" hover="" identifier="pymmcore_plus.mda._runner.DimensionOverride" optional="">DimensionOverride</autoref>] | None</code>             </td>             <td>               <div class="doc-md-description">                 <p>Per-dimension storage overrides, keyed by dimension name. See <code>MDARunner.run</code> for details.</p>                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>       </tbody>     </table>

Returns:

| Type | Description |
| --- | --- |
| `Thread` | The thread the sequence is running on. Use `thread.join()` to block until done, or `thread.is_alive()` to check if the sequence is complete. |

### setContext

```python
setContext(**kwargs: Unpack[SetContextKwargs]) -> Iterator[None]
```

Set core properties in a context restoring the initial values on exit.

✨ *This method is new in `CMMCorePlus`.*

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `**kwargs` | `Any` | Keyword arguments may be any `Name` for which `get<Name>` and `set<Name>` methods exist (where the first letter in `<Name>` may be either lower or upper case). For example, `setContext(exposure=10)` will call `setExposure(10)` when entering the context and `setExposure(<initial>)` when exiting the context. If the property is not found, a warning is logged and the property is skipped. If the value is a tuple, it is unpacked and passed to the `set<Name>` method (but lists are not unpacked). | `{}` |

Examples:

```python
core = CMMCorePlus.instance()

with core.setContext(autoShutter=False):
    assert not core.getAutoShutter()
    # do other stuff
    ...

# autoShutter is restored to its original value when the context exits
assert core.getAutoShutter()
```

## Pumps

### getPumpFlowrate

```python
getPumpFlowrate(pumpLabel: str) -> float
```

Return the flowrate of the pump in uL per second

### getPumpMaxVolume

```python
getPumpMaxVolume(pumpLabel: str) -> float
```

Return max volume of the pump in uL

### getPumpPressureKPa

```python
getPumpPressureKPa(pumpLabel: str) -> float
```

Return the pressure of the pump in kPa.

### getPumpVolume

```python
getPumpVolume(pumpLabel: str) -> float
```

Return the fluid volume in the pump in uL

### invertPumpDirection

```python
invertPumpDirection(pumpLabel: str, invert: bool) -> None
```

Sets whether the pump direction needs to be inverted

### isPumpDirectionInverted

```python
isPumpDirectionInverted(pumpLabel: str) -> bool
```

Return True if pump direction needs to be inverted

### pressurePumpCalibrate

```python
pressurePumpCalibrate(pumpLabel: str) -> None
```

Calibrates the pressure pump.

### pressurePumpRequiresCalibration

```python
pressurePumpRequiresCalibration(pumpLabel: str) -> bool
```

Return True if pump requires calibration before operation.

### pressurePumpStop

```python
pressurePumpStop(pumpLabel: str) -> None
```

Stops the pressure pump.

### pumpDispenseDurationSeconds

```python
pumpDispenseDurationSeconds(pumpLabel: str, seconds: float) -> None
```

Dispenses for the provided duration (in seconds) at the set flowrate.

### pumpDispenseVolumeUl

```python
pumpDispenseVolumeUl(pumpLabel: str, microLiter: float) -> None
```

Dispenses the provided volume (in uL) at the set flowrate.

### pumpStart

```python
pumpStart(pumpLabel: str) -> None
```

Start dispensing until syringe is empty, or manually stopped.

(whichever occurs first).

### setPumpFlowrate

```python
setPumpFlowrate(pumpLabel: str, volume: float) -> None
```

Set the flowrate of the pump in uL per second

### setPumpMaxVolume

```python
setPumpMaxVolume(pumpLabel: str, volume: float) -> None
```

Set the max volume of the pump in uL

### setPumpPressureKPa

```python
setPumpPressureKPa(pumpLabel: str, pressure: float) -> None
```

Sets the pressure of the pump in kPa.

### setPumpVolume

```python
setPumpVolume(pumpLabel: str, volume: float) -> None
```

Sets the volume of fluid in the pump in uL.

Note it does not withdraw upto this amount. It is merely to inform MM of the volume in a prefilled pump.

### volumetricPumpHome

```python
volumetricPumpHome(pumpLabel: str) -> None
```

Homes the volumetric pump.

### volumetricPumpRequiresHoming

```python
volumetricPumpRequiresHoming(pumpLabel: str) -> bool
```

Return True if the volumetric pump requires homing.

### volumetricPumpStop

```python
volumetricPumpStop(pumpLabel: str) -> None
```

Stops the volumetric pump.

## Galvos

### addGalvoPolygonVertex

```python
addGalvoPolygonVertex(
    galvoLabel: str, polygonIndex: int, x: float, y: float
) -> None
```

Add a vertex to a galvo polygon.

### deleteGalvoPolygons

```python
deleteGalvoPolygons(galvoLabel: DeviceLabel | str) -> None
```

Remove all added polygons

### getGalvoChannel

```python
getGalvoChannel(galvoLabel: DeviceLabel | str) -> str
```

Get the name of the active galvo channel (for a multi-laser galvo device).

### getGalvoDevice

```python
getGalvoDevice() -> DeviceLabel | Literal['']
```

Returns the label of the currently selected Galvo device.

Returns empty string if no Galvo device is selected.

### getGalvoPosition

```python
getGalvoPosition(galvoDevice: DeviceLabel | str) -> list[float]
```

```python
getGalvoPosition(
    galvoLabel: DeviceLabel | str,
    x_stage: Sequence[float],
    y_stage: Sequence[float],
) -> None
```

```python
getGalvoPosition(galvoDevice: DeviceLabel | str) -> list[float]
```

Get x,y position of the galvo device.

### getGalvoXMinimum

```python
getGalvoXMinimum(galvoLabel: DeviceLabel | str) -> float
```

Get the Galvo x minimum

### getGalvoXRange

```python
getGalvoXRange(galvoLabel: DeviceLabel | str) -> float
```

Get the Galvo x range

### getGalvoYMinimum

```python
getGalvoYMinimum(galvoLabel: DeviceLabel | str) -> float
```

Get the Galvo y minimum

### getGalvoYRange

```python
getGalvoYRange(galvoLabel: DeviceLabel | str) -> float
```

Get the Galvo y range

### loadGalvoPolygons

```python
loadGalvoPolygons(galvoLabel: DeviceLabel | str) -> None
```

Load a set of galvo polygons to the device

### pointGalvoAndFire

```python
pointGalvoAndFire(
    galvoLabel: DeviceLabel | str, x: float, y: float, pulseTime_us: float
) -> None
```

Set the Galvo to an x,y position and fire the laser for a predetermined duration.

### runGalvoPolygons

```python
runGalvoPolygons(galvoLabel: DeviceLabel | str) -> None
```

Run a loop of galvo polygons

### runGalvoSequence

```python
runGalvoSequence(galvoLabel: DeviceLabel | str) -> None
```

Run a sequence of galvo positions

### setGalvoDevice

```python
setGalvoDevice(galvoLabel: DeviceLabel | str) -> None
```

Sets the current galvo device.

### setGalvoIlluminationState

```python
setGalvoIlluminationState(galvoLabel: DeviceLabel | str, on: bool) -> None
```

Set the galvo's illumination state to on or off

### setGalvoPolygonRepetitions

```python
setGalvoPolygonRepetitions(
    galvoLabel: DeviceLabel | str, repetitions: int
) -> None
```

Set the number of times to loop galvo polygons

### setGalvoPosition

```python
setGalvoPosition(galvoLabel: DeviceLabel | str, x: float, y: float) -> None
```

Set the Galvo to an x,y position.

### setGalvoSpotInterval

```python
setGalvoSpotInterval(
    galvoLabel: DeviceLabel | str, pulseTime_us: float
) -> None
```

Set the SpotInterval for the specified galvo device.

## SLMs

### displaySLMImage

```python
displaySLMImage(slmLabel: DeviceLabel | str) -> None
```

Display the waiting image on the SLM.

### getSLMBytesPerPixel

```python
getSLMBytesPerPixel(slmLabel: DeviceLabel | str) -> int
```

Returns the number of bytes per SLM pixel

### getSLMDevice

```python
getSLMDevice() -> DeviceLabel | Literal['']
```

Returns the label of the currently selected SLM device.

Returns empty string if no SLM device is selected.

### getSLMExposure

```python
getSLMExposure(slmLabel: DeviceLabel | str) -> float
```

Returns the exposure time that will be used by the SLM for illumination

### getSLMHeight

```python
getSLMHeight(slmLabel: DeviceLabel | str) -> int
```

Returns the height (in "pixels") of the SLM

### getSLMNumberOfComponents

```python
getSLMNumberOfComponents(slmLabel: DeviceLabel | str) -> int
```

Returns the number of components (usually these depict colors) of the SLM.

For instance, an RGB projector will return 3, but a grey scale SLM returns 1

### getSLMSequenceMaxLength

```python
getSLMSequenceMaxLength(slmLabel: DeviceLabel | str) -> int
```

For SLMs that support sequences, returns the maximum length of the sequence that can be uploaded to the device

### getSLMWidth

```python
getSLMWidth(slmLabel: DeviceLabel | str) -> int
```

Returns the width (in "pixels") of the SLM

### loadSLMSequence

```python
loadSLMSequence(
    slmLabel: DeviceLabel | str, imageSequence: list[bytes]
) -> None
```

Load a sequence of images into the SLM

### setSLMDevice

```python
setSLMDevice(slmLabel: DeviceLabel | str) -> None
```

Sets the current slm device.

### setSLMExposure

```python
setSLMExposure(slmLabel: DeviceLabel | str, exposure_ms: float) -> None
```

For SLM devices with build-in light source (such as projectors), this will set the exposure time, but not (yet) start the illumination

### setSLMImage

```python
setSLMImage(slmLabel: DeviceLabel | str, pixels: NDArray[uint8]) -> None
```

```python
setSLMImage(slmLabel: DeviceLabel | str, pixels: Any) -> None
```

```python
setSLMImage(slmLabel: DeviceLabel | str, pixels: NDArray[uint8]) -> None
```

Write an image to the SLM .

When passing a numpy array, `pixels` must be one of the following:

- a 2D numpy array \[h,w\] of uint8s, representing a grayscale image to write to the SLM.
- a 3D numpy array \[h,w,3\] of uint8s with 3 color channels \[R,G,B\], representing an imgRGB32 image to write to the SLM.

In both cases, the dimensions of the array should match the width and height of the SLM.

> [!WARNING]
>
> SLM might convert grayscale to binary internally.

### setSLMPixelsTo

```python
setSLMPixelsTo(slmLabel: DeviceLabel | str, intensity: int) -> None
```

```python
setSLMPixelsTo(
    slmLabel: DeviceLabel | str, red: int, green: int, blue: int
) -> None
```

```python
setSLMPixelsTo(slmLabel: DeviceLabel | str, intensity: int) -> None
```

Set all SLM pixels to a single 8-bit intensity.

### startSLMSequence

```python
startSLMSequence(slmLabel: DeviceLabel | str) -> None
```

Starts the sequence previously uploaded to the SLM

### stopSLMSequence

```python
stopSLMSequence(slmLabel: DeviceLabel | str) -> None
```

Stops the SLM sequence if previously started

## Serial ports

### getSerialPortAnswer

```python
getSerialPortAnswer(portLabel: str, term: str) -> str
```

Continuously read from the serial port until the terminating sequence is encountered.

### readFromSerialPort

```python
readFromSerialPort(portLabel: str) -> list[str]
```

Reads the contents of the Rx buffer.

### setSerialPortCommand

```python
setSerialPortCommand(portLabel: str, command: str, term: str) -> None
```

Send string to the serial device and return an answer.

### setSerialProperties

```python
setSerialProperties(
    portName: str,
    answerTimeout: str,
    baudRate: str,
    delayBetweenCharsMs: str,
    handshaking: str,
    parity: str,
    stopBits: str,
) -> None
```

Sets all com port properties in a single call.

### writeToSerialPort

```python
writeToSerialPort(portLabel: str, data: bytes) -> None
```

Sends an array of characters to the serial port and returns immediately.

## Pixel size

### definePixelSizeConfig

```python
definePixelSizeConfig(resolutionID: str) -> None
```

```python
definePixelSizeConfig(
    resolutionID: str, deviceLabel: str, propName: str, value: str
) -> None
```

```python
definePixelSizeConfig(*args: str, **kwargs: str) -> None
```

Defines an empty pixel size entry.

**Why Override?** To emit a `pixelSizeChanged` event.

### deletePixelSizeConfig

```python
deletePixelSizeConfig(resolutionID: str) -> None
```

Delete the pixel size configuration for the given `resolutionID`.

**Why Override?** To emit a `pixelSizeChanged` event.

### getAvailablePixelSizeConfigs

```python
getAvailablePixelSizeConfigs() -> tuple[PixelSizeConfigName, ...]
```

Returns all defined resolution preset names

### getCurrentPixelSizeConfig

```python
getCurrentPixelSizeConfig() -> PixelSizeConfigName
```

```python
getCurrentPixelSizeConfig(cached: bool) -> PixelSizeConfigName
```

```python
getCurrentPixelSizeConfig() -> PixelSizeConfigName
```

Get the current pixel configuration name

### getMagnificationFactor

```python
getMagnificationFactor() -> float
```

Returns the product of all Magnifiers in the system or 1.0 when none is found. This is used internally by GetPixelSizeUm

### getPixelSizeAffine

```python
getPixelSizeAffine() -> AffineTuple
```

```python
getPixelSizeAffine(cached: bool) -> AffineTuple
```

```python
getPixelSizeAffine() -> AffineTuple
```

Returns the current Affine Transform to related camera pixels with stage movement.

### getPixelSizeAffineByID

```python
getPixelSizeAffineByID(resolutionID: PixelSizeConfigName | str) -> AffineTuple
```

Returns the Affine Transform to related camera pixels with stage movement for the requested pixel size group. The raw affine transform without correction for binning and magnification will be returned.

### getPixelSizeConfigData

```python
getPixelSizeConfigData(
    configName: str, *, native: Literal[True]
) -> Configuration
```

```python
getPixelSizeConfigData(
    configName: str, *, native: Literal[False] = False
) -> Configuration
```

```python
getPixelSizeConfigData(
    configName: str, *, native: bool = False
) -> Configuration | Configuration
```

Return the configuration object for a given pixel size preset `configName`.

**Why Override?** The `pymmcore_plus.Configuration` object returned when `native=False` (the default) provides a nicer `Mapping` interface. Pass `native=True` to get the original `pymmcore.Configuration` object.

### getPixelSizedxdz

```python
getPixelSizedxdz() -> float
```

```python
getPixelSizedxdz(cached: bool) -> float
```

```python
getPixelSizedxdz(resolutionID: PixelSizeConfigName | str) -> float
```

```python
getPixelSizedxdz() -> float
```

Returns the angle between the camera's x axis and the axis (direction) of the z drive.

This angle is dimensionless (i.e. the ratio of the translation in x caused by a translation in z, i.e. dx / dz). This angle can be different for different z drives (if there are multiple Z drives in the system, please add the Core-Focus device to the pixel size configuration). See: [https://github.com/micro-manager/micro-manager/issues/1984](<https://github.com/micro-manager/micro-manager/issues/1984>)

### getPixelSizedydz

```python
getPixelSizedydz() -> float
```

```python
getPixelSizedydz(cached: bool) -> float
```

```python
getPixelSizedydz(resolutionID: PixelSizeConfigName | str) -> float
```

```python
getPixelSizedydz() -> float
```

Returns the angle between the camera's y axis and the axis (direction) of the z drive.

This angle is dimensionless (i.e. the ratio of the translation in x caused by a translation in z, i.e. dy / dz). This angle can be different for different z drives (if there are multiple Z drives in the system, please add the Core-Focus device to the pixel size configuration). See: [https://github.com/micro-manager/micro-manager/issues/1984](<https://github.com/micro-manager/micro-manager/issues/1984>)

### getPixelSizeOptimalZUm

```python
getPixelSizeOptimalZUm() -> float
```

```python
getPixelSizeOptimalZUm(cached: bool) -> float
```

```python
getPixelSizeOptimalZUm(resolutionID: PixelSizeConfigName | str) -> float
```

```python
getPixelSizeOptimalZUm() -> float
```

Returns the optimal z step size in um, optionally using cached pixel configuration.

There is no magic to this number, but lets the system configuration communicate to the end user what the optimal Z step size is for this pixel size configuration

### getPixelSizeUm

```python
getPixelSizeUm() -> float
```

```python
getPixelSizeUm(cached: bool) -> float
```

```python
getPixelSizeUm() -> float
```

Returns the current pixel size in microns.

### getPixelSizeUmByID

```python
getPixelSizeUmByID(resolutionID: PixelSizeConfigName | str) -> float
```

Returns the pixel size in um for the requested pixel size group

### isPixelSizeConfigDefined

```python
isPixelSizeConfigDefined(resolutionID: str) -> bool
```

Checks if the Pixel Size Resolution already exists

### renamePixelSizeConfig

```python
renamePixelSizeConfig(
    oldConfigName: PixelSizeConfigName | str, newConfigName: str
) -> None
```

Renames a pixel size configuration.

### setPixelSizeAffine

```python
setPixelSizeAffine(
    resolutionID: PixelSizeConfigName | str, affine: Sequence[float]
) -> None
```

Sets the raw affine transform for the specific pixel size configuration.

The affine transform consists of the first two rows of a 3x3 matrix, the third row is always assumed to be 0.0 0.0 1.0.

### setPixelSizeConfig

```python
setPixelSizeConfig(resolutionID: PixelSizeConfigName | str) -> None
```

Applies a Pixel Size Configuration.

### setPixelSizedxdz

```python
setPixelSizedxdz(resolutionID: PixelSizeConfigName | str, dXdZ: float) -> None
```

Sets the pixel size in the X direction in microns.

### setPixelSizedydz

```python
setPixelSizedydz(resolutionID: PixelSizeConfigName | str, dYdZ: float) -> None
```

Sets the pixel size in the Y direction in microns.

### setPixelSizeOptimalZUm

```python
setPixelSizeOptimalZUm(
    resolutionID: PixelSizeConfigName | str, optimalZ: float
) -> None
```

Sets the pixel size in the Z direction in microns.

### setPixelSizeUm

```python
setPixelSizeUm(resolutionID: str, pixSize: float) -> None
```

Set pixel size in microns for the specified `resolutionID`.

**Why Override?** To emit a `pixelSizeChanged` event.

## Hardware sequencing

### canSequenceEvents

```python
canSequenceEvents(e1: MDAEvent, e2: MDAEvent, cur_length: int = -1) -> bool
```

Check whether two `useq.MDAEvent` are sequenceable by this core instance.

Micro-manager calls hardware triggering "sequencing". Two events can be sequenced if *all* device properties that are changing between the first and second event support sequencing.

If `cur_length` is provided, it is used to determine if the sequence is "full" (i.e. the sequence is already at the maximum length) as determined by the `...SequenceMaxLength()` method corresponding to the device property.

See: [https://micro-manager.org/Hardware-based\_Synchronization\_in\_Micro-Manager](<https://micro-manager.org/Hardware-based_Synchronization_in_Micro-Manager>)

✨ *This method is new in `CMMCorePlus`.*

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `e1` | `MDAEvent` | The first event. | *required* |
| `e2` | `MDAEvent` | The second event. | *required* |
| `cur_length` | `int` | The current length of the sequence. Used when checking `.get<...>SequenceMaxLength` for a given property. If the current length is greater than the max length, the events cannot be sequenced. By default -1, which means the current length is not checked. | `-1` |

Returns:

| Type | Description |
| --- | --- |
| `bool` | True if the events can be sequenced, False otherwise. |

Examples:

> [!NOTE]
>
> The results here will depend on the current state of the core and devices.

```python
>>> from useq import MDAEvent
>>> core = CMMCorePlus.instance()
>>> core.loadSystemConfiguration()
>>> core.canSequenceEvents(MDAEvent(), MDAEvent())
True
>>> core.canSequenceEvents(MDAEvent(x_pos=1), MDAEvent(x_pos=2))
False
>>> core.canSequenceEvents(
...     MDAEvent(channel={'config': 'DAPI'}),
...     MDAEvent(channel={'config': 'FITC'})
... )
False
```

### getExposureSequenceMaxLength

```python
getExposureSequenceMaxLength(cameraLabel: DeviceLabel | str) -> int
```

Gets the maximum length of a camera's exposure sequence.

### getPropertySequenceMaxLength

```python
getPropertySequenceMaxLength(
    label: DeviceLabel | str, propName: PropertyName | str
) -> int
```

Queries device property for the maximum number of events that can be put in a sequence

### getStageSequenceMaxLength

```python
getStageSequenceMaxLength(stageLabel: DeviceLabel | str) -> int
```

Gets the maximum length of a stage's position sequence.

### getXYStageSequenceMaxLength

```python
getXYStageSequenceMaxLength(xyStageLabel: DeviceLabel | str) -> int
```

Gets the maximum length of an XY stage's position sequence.

### isExposureSequenceable

```python
isExposureSequenceable(cameraLabel: DeviceLabel | str) -> bool
```

Queries camera if exposure can be used in a sequence

### isPropertySequenceable

```python
isPropertySequenceable(
    label: DeviceLabel | str, propName: PropertyName | str
) -> bool
```

Queries device if the specified property can be used in a sequence

### isStageLinearSequenceable

```python
isStageLinearSequenceable(stageLabel: DeviceLabel | str) -> bool
```

Queries if the stage can be used in a linear sequence.

A linear sequence is defined by a stepsize and number of slices

### isStageSequenceable

```python
isStageSequenceable(stageLabel: DeviceLabel | str) -> bool
```

Queries stage if it can be used in a sequence

### isXYStageSequenceable

```python
isXYStageSequenceable(xyStageLabel: DeviceLabel | str) -> bool
```

Queries XY stage if it can be used in a sequence

### loadExposureSequence

```python
loadExposureSequence(
    cameraLabel: DeviceLabel | str, exposureSequence_ms: Sequence[float]
) -> None
```

Transfer a sequence of exposure times to the camera.

### loadPropertySequence

```python
loadPropertySequence(
    label: DeviceLabel | str,
    propName: PropertyName | str,
    eventSequence: Sequence[str],
) -> None
```

Transfer a sequence of events/states/whatever to the device.

This should only be called for device-properties that are sequenceable

### loadStageSequence

```python
loadStageSequence(
    stageLabel: DeviceLabel | str, positionSequence: Sequence[float]
) -> None
```

Transfer a sequence of events/states/whatever to the device.

This should only be called for device-properties that are sequenceable

### loadXYStageSequence

```python
loadXYStageSequence(
    xyStageLabel: DeviceLabel | str,
    xSequence: Sequence[float],
    ySequence: Sequence[float],
) -> None
```

Transfer a sequence of stage positions to the xy stage.

xSequence and ySequence must have the same length. This should only be called for XY stages that are sequenceable

### setStageLinearSequence

```python
setStageLinearSequence(
    stageLabel: DeviceLabel | str, dZ_um: float, nSlices: int
) -> None
```

Loads a linear sequence (defined by stepsize and nr. of steps) into the device.

### startExposureSequence

```python
startExposureSequence(cameraLabel: DeviceLabel | str) -> None
```

Starts an ongoing sequence of triggered exposures in a camera.

This should only be called for cameras where exposure time is sequenceable

### startPropertySequence

```python
startPropertySequence(
    label: DeviceLabel | str, propName: PropertyName | str
) -> None
```

Starts an ongoing sequence of triggered events in a property of a device.

This should only be called for device-properties that are sequenceable

### startStageSequence

```python
startStageSequence(stageLabel: DeviceLabel | str) -> None
```

Starts an ongoing sequence of triggered events in a stage.

This should only be called for stages

### startXYStageSequence

```python
startXYStageSequence(xyStageLabel: DeviceLabel | str) -> None
```

Starts an ongoing sequence of triggered events in an XY stage.

This should only be called for stages

### stopExposureSequence

```python
stopExposureSequence(cameraLabel: DeviceLabel | str) -> None
```

Stops an ongoing sequence of triggered exposures in a camera.

This should only be called for cameras where exposure time is sequenceable

### stopPropertySequence

```python
stopPropertySequence(
    label: DeviceLabel | str, propName: PropertyName | str
) -> None
```

Stops an ongoing sequence of triggered events in a property of a device.

This should only be called for device-properties that are sequenceable

### stopStageSequence

```python
stopStageSequence(stageLabel: DeviceLabel | str) -> None
```

Stops an ongoing sequence of triggered events in a stage.

This should only be called for stages that are sequenceable

### stopXYStageSequence

```python
stopXYStageSequence(xyStageLabel: DeviceLabel | str) -> None
```

Stops an ongoing sequence of triggered events in an XY stage.

This should only be called for stages that are sequenceable

## Images &amp; buffer

### clearCircularBuffer

```python
clearCircularBuffer() -> None
```

Removes all images from the circular buffer.

### fixImage

```python
fixImage(img: ndarray, ncomponents: int | None = None) -> ndarray
```

Fix img shape/dtype based on `self.getNumberOfComponents()`.

✨ *This method is new in `CMMCorePlus`.*

convert images with n\_components \> 1 to a shape (w, h, num\_components) and dtype `img.dtype.itemsize//ncomp`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `img` | `ndarray` | input image | *required* |
| `ncomponents` | `int` | number of components in the image, by default `self.getNumberOfComponents()` | `None` |

Returns:

| Type | Description |
| --- | --- |
| `ndarray` | output image (possibly new shape and dtype) |

### getBufferFreeCapacity

```python
getBufferFreeCapacity() -> int
```

Returns the number of images that can be added to the buffer without overflowing.

### getBufferTotalCapacity

```python
getBufferTotalCapacity() -> int
```

Returns the total number of images that can be stored in the buffer

### getCircularBufferMemoryFootprint

```python
getCircularBufferMemoryFootprint() -> int
```

Returns the size of the Circular Buffer in MB

### getImage

```python
getImage(*, fix: bool = True) -> ndarray
```

```python
getImage(numChannel: int, *, fix: bool = True) -> ndarray
```

```python
getImage(numChannel: int | None = None, *, fix: bool = True) -> ndarray
```

Return the internal image buffer.

**Why Override?** To fix the shape of images with n\_components \> 1 (like RGB images)

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `numChannel` | `int` | The camera channel to get the image from. If None, (the default), then Multi-Channel cameras will return the content of the first channel. | `None` |
| `fix` | `bool` | If `True` (the default), then images with n\_components \> 1 (like RGB images) will be reshaped to (w, h, n\_components) using `fixImage`. | `True` |

### getImageBitDepth

```python
getImageBitDepth() -> int
```

How many bits of dynamic range are to be expected from the camera.

### getImageBufferSize

```python
getImageBufferSize() -> int
```

Returns the size of the internal image buffer.

### getImageHeight

```python
getImageHeight() -> int
```

Vertical dimension of the image buffer in pixels.

### getImageWidth

```python
getImageWidth() -> int
```

Horizontal dimension of the image buffer in pixels.

### getLastImage

```python
getLastImage() -> ndarray
```

Gets the last image from the circular buffer.

### getLastImageAndMD

```python
getLastImageAndMD(
    channel: int, slice: int, *, fix: bool = True
) -> tuple[ndarray, Metadata]
```

```python
getLastImageAndMD(*, fix: bool = True) -> tuple[ndarray, Metadata]
```

```python
getLastImageAndMD(
    channel: int | None = None, slice: int | None = None, *, fix: bool = True
) -> tuple[ndarray, Metadata]
```

Return last image from the circular buffer along with metadata.

✨ *This method is new in `CMMCorePlus`.*

This is a convenience method that is very similar to `getLastImageMD`, except that it doesn't require instantiating a `MetaData` object first. It returns a tuple containing the image and a `pymmcore_plus.Metadata` object.

It also adds a `fix` parameter, which reshapes multi-component images (like RGB images) to (w, h, n\_components) using `fixImage` by default.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `channel` | `int` | Channel index, by default None | `None` |
| `slice` | `int` | Slice index, by default None | `None` |
| `fix` | `bool` | If `True` (the default), then images with n\_components \> 1 (like RGB images) will be reshaped to (w, h, n\_components) using `fixImage`. | `True` |

Returns:

| Type | Description |
| --- | --- |
| `tuple[ndarray, Metadata]` | Image and metadata |

### getLastImageMD

```python
getLastImageMD(channel: int, slice: int, md: Metadata) -> ndarray
```

```python
getLastImageMD(md: Metadata) -> ndarray
```

```python
getLastImageMD(channel: int, slice: int, md: Metadata) -> ndarray
```

Returns a pointer to the pixels of the image that was last inserted into the circular buffer. Also provides all metadata associated with that image

### getNBeforeLastImageAndMD

```python
getNBeforeLastImageAndMD(
    n: int, *, fix: bool = True
) -> tuple[ndarray, Metadata]
```

Return image taken `n` images ago along with associated metadata.

✨ *This method is new in `CMMCorePlus`.*

This is a convenience method that is very similar to `getNBeforeLastImageMD`, except that it doesn't require instantiating a `MetaData` object first. It returns a tuple containing the image and a `pymmcore_plus.Metadata` object.

It also adds a `fix` parameter, which reshapes multi-component images (like RGB images) to (w, h, n\_components) using `fixImage` by default.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `n` | `int` | The number of images ago to retrieve. 0 is the last image, 1 is the image before that, etc. | *required* |
| `fix` | `bool` | If `True` (the default), then images with n\_components \> 1 (like RGB images) will be reshaped to (w, h, n\_components) using `fixImage`. | `True` |

### getNBeforeLastImageMD

```python
getNBeforeLastImageMD(n: int, md: Metadata) -> ndarray
```

Returns a pointer to the pixels of the image that was inserted n images ago. Also provides all metadata associated with that image

### getRemainingImageCount

```python
getRemainingImageCount() -> int
```

Returns number ofimages available in the Circular Buffer

### getTaggedImage

```python
getTaggedImage(channel_index: int = 0) -> TaggedImage
```

Return getImage as named tuple with metadata.

✨ *This method is new in `CMMCorePlus`.* It returns an object similar to MMCoreJ.getTaggedImage().

### getTags

```python
getTags(
    meta: Metadata | None = None, channel_index: int | None = None
) -> dict[str, Any]
```

Return a dict of metadata tags for the state of the core.

NOTE: this function is pretty slow, and is potentially called on every frame of an acquisition. It would be nice to determine what is absolutely necessary, and possible allow the user to specify what they want to include.

✨ *This method is new in `CMMCorePlus`.* It returns only the `.tags` attribute of what you would get with `getTaggedImage()` or `popNextTaggedImage()`.

### initializeCircularBuffer

```python
initializeCircularBuffer() -> None
```

Initialize circular buffer based on the current camera settings.

### isBufferOverflowed

```python
isBufferOverflowed() -> bool
```

Indicates whether the circular buffer is overflowed

### isSequenceRunning

```python
isSequenceRunning() -> bool
```

```python
isSequenceRunning(cameraLabel: DeviceLabel | str) -> bool
```

```python
isSequenceRunning() -> bool
```

Check if the current camera is acquiring the sequence.

Returns false when the sequence is done

### popNextImage

```python
popNextImage(*, fix: bool = True) -> ndarray
```

Gets and removes the next image from the circular buffer.

**Why Override?** to add the `fix` parameter, which reshapes multi-component images (like RGB images) to (w, h, n\_components) using `fixImage` by default.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `fix` | `bool` | If `True` (the default), then images with n\_components \> 1 (like RGB images) will be reshaped to (w, h, n\_components) using `fixImage`. | `True` |

### popNextImageAndMD

```python
popNextImageAndMD(
    channel: int, slice: int, *, fix: bool = True
) -> tuple[ndarray, Metadata]
```

```python
popNextImageAndMD(*, fix: bool = True) -> tuple[ndarray, Metadata]
```

```python
popNextImageAndMD(
    channel: int = 0, slice: int = 0, *, fix: bool = True
) -> tuple[ndarray, Metadata]
```

Gets and removes the next image (and metadata) from the circular buffer.

✨ *This method is new in `CMMCorePlus`.*

This is a convenience method that is very similar to `popNextImageMD`, except that it doesn't require instantiating a `MetaData` object first. It returns a tuple containing the image and a `pymmcore_plus.Metadata` object.

It also adds a `fix` parameter, which reshapes multi-component images (like RGB images) to (w, h, n\_components) using `fixImage` by default.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `channel` | `int` | Channel index, by default None | `0` |
| `slice` | `int` | Slice index, by default None | `0` |
| `fix` | `bool` | If `True` (the default), then images with n\_components \> 1 (like RGB images) will be reshaped to (w, h, n\_components) using `fixImage`. | `True` |

Returns:

| Type | Description |
| --- | --- |
| `tuple[ndarray, Metadata]` | Image and metadata |

### popNextImageMD

```python
popNextImageMD(channel: int, slice: int, md: Metadata) -> ndarray
```

```python
popNextImageMD(md: Metadata) -> ndarray
```

```python
popNextImageMD(channel: int, slice: int, md: Metadata) -> ndarray
```

Gets and removes the next image (and metadata) from the circular buffer

### popNextTaggedImage

```python
popNextTaggedImage(channel_index: int = 0) -> TaggedImage
```

Return popNextImageAndMD as named tuple with metadata.

✨ *This method is new in `CMMCorePlus`.* It returns an object similar to MMCoreJ.popNextTaggedImage().

### prepareSequenceAcquisition

```python
prepareSequenceAcquisition(cameraLabel: DeviceLabel | str) -> None
```

Prepare the camera for the sequence acquisition to save the time in the

StartSequenceAcqusition() call which is supposed to come next.

### setCircularBufferMemoryFootprint

```python
setCircularBufferMemoryFootprint(sizeMB: int) -> None
```

Reserve memory for the circular buffer.

### snap

```python
snap(numChannel: int | None = None, *, fix: bool = True) -> ndarray
```

Snap and return an image.

✨ *This method is new in `CMMCorePlus`.*

Convenience for calling `self.snapImage()` followed by returning the value of `self.getImage()`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `numChannel` | `int` | The camera channel to get the image from. If None, (the default), then Multi-Channel cameras will return the content of the first channel. | `None` |
| `fix` | `bool` | If `True` (the default), then images with n\_components \> 1 (like RGB images) will be reshaped to (w, h, n\_components) using `fixImage`. | `True` |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `img` | `ndarray` |  |

### snapImage

```python
snapImage() -> None
```

Acquires a single image with current settings.

**Why Override?** to emit the `imageSnapped` event after snapping an image. and to emit shutter property changes if `getAutoShutter` is `True`.

### startContinuousSequenceAcquisition

```python
startContinuousSequenceAcquisition(intervalMs: float = 0) -> None
```

Start a ContinuousSequenceAcquisition.

**Why Override?** To emit a `startContinuousSequenceAcquisition` event.

### startSequenceAcquisition

```python
startSequenceAcquisition(
    numImages: int, intervalMs: float, stopOnOverflow: bool
) -> None
```

```python
startSequenceAcquisition(
    cameraLabel: str, numImages: int, intervalMs: float, stopOnOverflow: bool
) -> None
```

```python
startSequenceAcquisition(*args: Any) -> None
```

Starts streaming camera sequence acquisition.

This command does not block the calling thread for the duration of the acquisition.

**Why Override?** To emit a `startSequenceAcquisition` event.

### stopSequenceAcquisition

```python
stopSequenceAcquisition(cameraLabel: str | None = None) -> None
```

Stops streaming camera sequence acquisition.

(for a specified camera if `cameraLabel` is provided.)

**Why Override?** To emit a `stopSequenceAcquisition` event.

## Cameras

### clearROI

```python
clearROI() -> None
```

Set the region of interest of the current camera to the full frame.

### getAllowedBinningValues

```python
getAllowedBinningValues() -> tuple[int, ...]
```

```python
getAllowedBinningValues(label: DeviceLabel | str) -> tuple[int, ...]
```

```python
getAllowedBinningValues() -> tuple[int, ...]
```

Returns allowed binning values for the current camera.

### getBinning

```python
getBinning() -> int
```

```python
getBinning(label: DeviceLabel | str) -> int
```

```python
getBinning() -> int
```

Returns the current binning factor of the camera.

### getBytesPerPixel

```python
getBytesPerPixel() -> int
```

How many bytes for each pixel.

### getCameraChannelName

```python
getCameraChannelName(channelNr: int) -> str
```

Returns the name of the requested channel as known by the default camera

### getCameraChannelNames

```python
getCameraChannelNames() -> tuple[str, ...]
```

Convenience method to call `getCameraChannelName` for all camera channels.

✨ *This method is new in `CMMCorePlus`.*

### getCameraDevice

```python
getCameraDevice() -> DeviceLabel | Literal['']
```

Returns the label of the currently selected camera device.

Returns empty string if no camera device is selected.

### getExposure

```python
getExposure() -> float
```

```python
getExposure(label: DeviceLabel | str) -> float
```

```python
getExposure() -> float
```

Returns the current exposure setting of the camera in milliseconds.

### getImageProcessorDevice

```python
getImageProcessorDevice() -> DeviceLabel | Literal['']
```

Returns the label of the currently selected image processor device.

Returns empty string if no image processor device is selected.

### getMultiROI

```python
getMultiROI(*_: Any) -> tuple[list[int], list[int], list[int], list[int]]
```

Get multiple ROIs from the current camera device.

Will fail if the camera does not support multiple ROIs. Will return empty vectors if multiple ROIs are not currently being used.

**Why Override?** So that the user doesn't need to pass in four empty pymmcore.UnsignedVector() objects.

### getNumberOfCameraChannels

```python
getNumberOfCameraChannels() -> int
```

Returns the number of simultaneous channels the default camera is returning.

### getNumberOfComponents

```python
getNumberOfComponents() -> int
```

Returns the number of components the default camera is returning.

### getPhysicalCameraDevice

```python
getPhysicalCameraDevice(channel_index: int = 0) -> str
```

Return the name of the actual camera device for a given channel index.

✨ *This method is new in `CMMCorePlus`.* It provides a convenience for accessing the name of the actual camera device when using the multi-camera utility.

### getROI

```python
getROI() -> Rectangle
```

```python
getROI(label: DeviceLabel | str) -> Rectangle
```

```python
getROI() -> Rectangle
```

Return the current hardware region of interest for a camera.

If multiple ROIs are set, this method instead returns a rectangle that describes the image that the camera will generate. The coordinates are in units of binned pixels. That is, conceptually, binning is applied before the ROI.

Returns \[0,0,0,0\] if no camera is selected.

### isMultiROIEnabled

```python
isMultiROIEnabled() -> bool
```

Queries the camera to determine if multiple ROIs are currently set.

### isMultiROISupported

```python
isMultiROISupported() -> bool
```

Queries the camera to determine if it supports multiple ROIs.

### setBinning

```python
setBinning(binning: int) -> None
```

```python
setBinning(label: DeviceLabel | str, binning: int) -> None
```

```python
setBinning(binning: int) -> None
```

Sets the binning factor of the current camera.

### setCameraDevice

```python
setCameraDevice(cameraLabel: DeviceLabel | str) -> None
```

Sets the current camera device.

### setExposure

```python
setExposure(exp: float) -> None
```

```python
setExposure(cameraLabel: DeviceLabel | str, dExp: float) -> None
```

```python
setExposure(exp: float) -> None
```

Sets the exposure setting of the current camera in milliseconds.

### setImageProcessorDevice

```python
setImageProcessorDevice(procLabel: DeviceLabel | str) -> None
```

Sets the current image processor device.

### setMultiROI

```python
setMultiROI(
    xs: Sequence[int],
    ys: Sequence[int],
    widths: Sequence[int],
    heights: Sequence[int],
) -> None
```

Set multiple ROIs for the current camera device.

Will fail if the camera does not support multiple ROIs, any widths or heights are non-positive, or if the vectors do not all have the same length.

### setROI

```python
setROI(x: int, y: int, width: int, height: int) -> None
```

```python
setROI(label: str, x: int, y: int, width: int, height: int) -> None
```

```python
setROI(*args: Any) -> None
```

Set the camera Region of Interest (ROI).

**Why Override?** To emit a `roiSet` event.

## Autofocus

### enableContinuousFocus

```python
enableContinuousFocus(enable: bool) -> None
```

Enables or disables the operation of the continuous focusing hardware device.

### fullFocus

```python
fullFocus() -> None
```

Performs focus acquisition and lock for the one-shot focusing device.

### getAutoFocusDevice

```python
getAutoFocusDevice() -> DeviceLabel | Literal['']
```

Returns the label of the currently selected auto-focus device.

Returns empty string if no auto-focus device is selected.

### getAutoFocusOffset

```python
getAutoFocusOffset() -> float
```

### getCurrentFocusScore

```python
getCurrentFocusScore() -> float
```

Returns the focus score from the default focusing device measured at the current Z position.

### getLastFocusScore

```python
getLastFocusScore() -> float
```

Returns the latest focus score from the focusing device.

### incrementalFocus

```python
incrementalFocus() -> None
```

Performs incremental focus for the one-shot focusing device.

### isContinuousFocusDrive

```python
isContinuousFocusDrive(stageLabel: DeviceLabel | str) -> bool
```

Check if a stage has continuous focusing capability.

(positions can be set while continuous focus runs).

### isContinuousFocusEnabled

```python
isContinuousFocusEnabled() -> bool
```

Checks if the continuous focusing hardware device is ON or OFF.

### isContinuousFocusLocked

```python
isContinuousFocusLocked() -> bool
```

Returns the lock-in status of the continuous focusing device.

### setAutoFocusDevice

```python
setAutoFocusDevice(focusLabel: DeviceLabel | str) -> None
```

Sets the current auto-focus device.

### setAutoFocusOffset

```python
setAutoFocusOffset(offset: float) -> None
```

Applies offset the one-shot focusing device.

In micro-manager, there is some variability in the way that autofocus devices are implemented. Some have a separate offset device, while others can directly set the offset of an associated device. As a result, calling `setAutoFocusOffset`, may or may not do anything depending on the current autofocus device.

This method attempts to detect known autofocus devices and

## Stages

### getFocusDevice

```python
getFocusDevice() -> DeviceLabel | Literal['']
```

Returns the label of the currently selected focus device.

Returns empty string if no focus device is selected.

### getFocusDirection

```python
getFocusDirection(stageLabel: str) -> FocusDirection
```

Return device type for a given device.

**Why Override?** The returned `pymmcore_plus.FocusDirection` enum is more interpretable than the raw `int` returned by `pymmcore`

### getPosition

```python
getPosition() -> float
```

```python
getPosition(stageLabel: DeviceLabel | str) -> float
```

```python
getPosition() -> float
```

Returns the current position of the current FocusDevice in microns.

### getXPosition

```python
getXPosition() -> float
```

```python
getXPosition(xyStageLabel: DeviceLabel | str) -> float
```

```python
getXPosition() -> float
```

Obtains the current position of the X axis of the XY stage in microns.

### getXYPosition

```python
getXYPosition() -> Sequence[float]
```

```python
getXYPosition(xyStageLabel: DeviceLabel | str) -> Sequence[float]
```

```python
getXYPosition() -> Sequence[float]
```

Obtains the current position of the XY stage in microns.

### getXYStageDevice

```python
getXYStageDevice() -> DeviceLabel | Literal['']
```

Returns the label of the currently selected XYStage device.

Returns empty string if no XYStage device is selected.

### getYPosition

```python
getYPosition() -> float
```

```python
getYPosition(xyStageLabel: DeviceLabel | str) -> float
```

```python
getYPosition() -> float
```

Obtains the current position of the Y axis of the XY stage in microns.

### getZPosition

```python
getZPosition() -> float
```

Obtains the current position of the Z axis of the Z stage in microns.

✨ *This method is new in `CMMCorePlus`: added to complement `getXPosition` and `getYPosition`*

> [!NOTE]
>
> This is simply an alias for `getPosition`\], which returns the position of the current focus device when called without arguments.

### home

```python
home(xyOrZStageLabel: DeviceLabel | str) -> None
```

Perform a hardware homing operation for an XY or focus/Z stage.

### isStageUsingCallbacks

```python
isStageUsingCallbacks(stageLabel: DeviceLabel | str) -> bool
```

Queries whether the stage uses callbacks to signal position changes.

### isXYStageUsingCallbacks

```python
isXYStageUsingCallbacks(xyStageLabel: DeviceLabel | str) -> bool
```

Queries whether the XY stage uses callbacks to signal position changes.

### setAdapterOrigin

```python
setAdapterOrigin(newZUm: float) -> None
```

```python
setAdapterOrigin(stageLabel: DeviceLabel | str, newZUm: float) -> None
```

```python
setAdapterOrigin(newZUm: float) -> None
```

Enable software translation of coordinates for the current focus/Z stage.

### setAdapterOriginXY

```python
setAdapterOriginXY(newXUm: float, newYUm: float) -> None
```

```python
setAdapterOriginXY(
    xyStageLabel: DeviceLabel | str, newXUm: float, newYUm: float
) -> None
```

```python
setAdapterOriginXY(newXUm: float, newYUm: float) -> None
```

Enable software translation of coordinates for the current XY stage.

The current position of the stage becomes (newXUm, newYUm). It is recommended that setOriginXY() be used instead where available.

### setFocusDevice

```python
setFocusDevice(focusLabel: str) -> None
```

Set the current Focus Device and emit a `propertyChanged` signal.

### setFocusDirection

```python
setFocusDirection(stageLabel: DeviceLabel | str, sign: int) -> None
```

Set the focus direction of a stage.

### setOrigin

```python
setOrigin() -> None
```

```python
setOrigin(stageLabel: DeviceLabel | str) -> None
```

```python
setOrigin() -> None
```

Zero the current focus/Z stage's coordinates at the current position.

### setOriginX

```python
setOriginX() -> None
```

```python
setOriginX(xyStageLabel: DeviceLabel | str) -> None
```

```python
setOriginX() -> None
```

Zero the given XY stage's X coordinate at the current position.

### setOriginXY

```python
setOriginXY() -> None
```

```python
setOriginXY(xyStageLabel: DeviceLabel | str) -> None
```

```python
setOriginXY() -> None
```

Zero the current XY stage's coordinates at the current position.

### setOriginY

```python
setOriginY() -> None
```

```python
setOriginY(xyStageLabel: DeviceLabel | str) -> None
```

```python
setOriginY() -> None
```

Zero the given XY stage's Y coordinate at the current position.

### setPosition

```python
setPosition(position: float) -> None
```

```python
setPosition(stageLabel: DeviceLabel | str, position: float) -> None
```

```python
setPosition(position: float) -> None
```

Sets the position of the current FocusDevice in microns.

### setRelativePosition

```python
setRelativePosition(d: float) -> None
```

```python
setRelativePosition(stageLabel: DeviceLabel | str, d: float) -> None
```

```python
setRelativePosition(d: float) -> None
```

Sets the relative position of the stage in microns.

### setRelativeXYPosition

```python
setRelativeXYPosition(dx: float, dy: float) -> None
```

```python
setRelativeXYPosition(
    xyStageLabel: DeviceLabel | str, dx: float, dy: float
) -> None
```

```python
setRelativeXYPosition(dx: float, dy: float) -> None
```

Sets the relative position of the XY stage in microns.

### setRelativeXYZPosition

```python
setRelativeXYZPosition(dx: float = 0, dy: float = 0, dz: float = 0) -> None
```

Sets the relative XYZ position in microns.

✨ *This method is new in `CMMCorePlus`.*

This is a convenience method that calls `setXYPosition` and `setZPosition` with the current position as the starting point.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `dx` | `float` | The relative change in X position, by default 0 | `0` |
| `dy` | `float` | The relative change in Y position, by default 0 | `0` |
| `dz` | `float` | The relative change in Z position, by default 0 | `0` |

### setXYPosition

```python
setXYPosition(x: float, y: float) -> None
```

```python
setXYPosition(xyStageLabel: str, x: float, y: float) -> None
```

```python
setXYPosition(*args: Any) -> None
```

Sets the position of the XY stage in microns.

**Why Override?** to store the last commanded stage position internally.

### setXYStageDevice

```python
setXYStageDevice(xyStageLabel: DeviceLabel | str) -> None
```

Sets the current XY device.

### setZPosition

```python
setZPosition(val: float) -> None
```

Set the position of the current focus device in microns.

✨ *This method is new in `CMMCorePlus`: added to complement `setXYPosition`*

> [!NOTE]
>
> This is simply an alias for `setPosition`, which returns the position of the current focus device when called with a single argument.

### stop

```python
stop(xyOrZStageLabel: DeviceLabel | str) -> None
```

Stop the XY or focus/Z stage motors

## Shutters

### getAutoShutter

```python
getAutoShutter() -> bool
```

Returns the current setting of the auto-shutter option.

### getShutterDevice

```python
getShutterDevice() -> DeviceLabel | Literal['']
```

Returns the label of the currently selected shutter device.

Returns empty string if no shutter device is selected.

### getShutterOpen

```python
getShutterOpen() -> bool
```

```python
getShutterOpen(shutterLabel: DeviceLabel | str) -> bool
```

```python
getShutterOpen() -> bool
```

Returns the state of the currently selected (default) shutter.

### setAutoShutter

```python
setAutoShutter(state: bool) -> None
```

Set shutter to automatically open and close when an image is acquired.

**Why Override?** To emit an `autoShutterSet` event.

### setShutterDevice

```python
setShutterDevice(shutterLabel: DeviceLabel | str) -> None
```

the current shutter device.

### setShutterOpen

```python
setShutterOpen(state: bool) -> None
```

```python
setShutterOpen(shutterLabel: str, state: bool) -> None
```

```python
setShutterOpen(*args: Any) -> None
```

Open or close the currently selected or `shutterLabel` shutter.

**Why Override?** To emit a `propertyChanged` event.

## Config groups &amp; presets

### channelGroup\_pattern

```python
channelGroup_pattern: Pattern
```

The regex pattern used to identify channel groups.

✨ \*This property is new in `CMMCorePlus`.

It is the regex used by `getOrGuessChannelGroup` to find a config group likely to be a channel group in `getAvailableConfigGroups` if `getChannelGroup` returns `None`.

By default:

```text
re.compile("(chan{1,2}(el)?|filt(er)?)s?", re.IGNORECASE)
```

### defineConfig

```python
defineConfig(groupName: str, configName: str) -> None
```

```python
defineConfig(
    groupName: str, configName: str, deviceLabel: str, propName: str, value: str
) -> None
```

```python
defineConfig(
    groupName: str,
    configName: str,
    deviceLabel: str | None = None,
    propName: str | None = None,
    value: str | None = None,
) -> None
```

Defines a configuration.

**Why Override?** To emit a `configDefined` event. Also, if `groupName` is not a defined group, then `defineConfigGroup(groupName)` is called.

### defineConfigGroup

```python
defineConfigGroup(groupName: str) -> None
```

Creates an empty configuration group.

### deleteConfig

```python
deleteConfig(groupName: str, configName: str) -> None
```

```python
deleteConfig(
    groupName: str, configName: str, deviceLabel: str, propName: str
) -> None
```

```python
deleteConfig(
    groupName: str,
    configName: str,
    deviceLabel: str | None = None,
    propName: str | None = None,
) -> None
```

Delete `configName` from `groupName`.

**Why Override?** To emit a `configDeleted` event.

### deleteConfigGroup

```python
deleteConfigGroup(groupName: str) -> None
```

Deletes an entire configuration `group`.

**Why Override?** To emit a `configGroupDeleted` event.

### getAvailableConfigGroups

```python
getAvailableConfigGroups() -> tuple[ConfigGroupName, ...]
```

Returns the names of all defined configuration groups

### getAvailableConfigs

```python
getAvailableConfigs(
    configGroup: ConfigGroupName | str,
) -> tuple[ConfigPresetName, ...]
```

Returns all defined configuration (preset) names in a given group

### getChannelGroup

```python
getChannelGroup() -> ConfigGroupName | Literal['']
```

Returns the group determining the channel selection.

Returns empty string if no channel group is selected.

### getConfigData

```python
getConfigData(
    configGroup: str, configName: str, *, native: Literal[True]
) -> Configuration
```

```python
getConfigData(
    configGroup: str, configName: str, *, native: Literal[False] = False
) -> Configuration
```

```python
getConfigData(
    configGroup: str, configName: str, *, native: bool = False
) -> Configuration | Configuration
```

Return the configuration object for a given `configGroup` and `configName`.

**Why Override?** The `pymmcore_plus.Configuration` object returned when `native=False` (the default) provides a nicer `Mapping` interface. Pass `native=True` to get the original `pymmcore.Configuration` object.

### getConfigGroupObject

```python
getConfigGroupObject(
    group_name: str, allow_missing: bool = False
) -> ConfigGroup
```

Return a `ConfigGroup` object bound to group\_name on this core.

✨ *This method is new in `CMMCorePlus`.*

`ConfigGroup` objects are a convenient object oriented way to interact with configuration groups (i.e. groups of [Configuration Presets](<https://micro-manager.org/Micro-Manager_Configuration_Guide#configuration-presets>) in Micro-Manager). They allow you to call any method on `CMMCore` that normally requires a `groupName` as the first argument as an argument-free method on the `ConfigGroup` object.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `group_name` | `str` | Configuration group name to get a config group object for. | *required* |
| `allow_missing` | `bool` | If `False` and the `ConfigGroup` does not exist, a `KeyError` will be raised. By default False. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `ConfigGroup` | `ConfigGroup` object bound to `group_name` on this core. |

### getConfigGroupState

```python
getConfigGroupState(group: str, *, native: Literal[True]) -> Configuration
```

```python
getConfigGroupState(
    group: str, *, native: Literal[False] = False
) -> Configuration
```

```python
getConfigGroupState(
    group: str, *, native: bool = False
) -> Configuration | Configuration
```

Return the state of the devices included in the specified `group`.

**Why Override?** The `pymmcore_plus.Configuration` object returned when `native=False` (the default) provides a nicer `Mapping` interface. Pass `native=True` to get the original `pymmcore.Configuration` object.

### getConfigGroupStateFromCache

```python
getConfigGroupStateFromCache(
    group: str, *, native: Literal[True]
) -> Configuration
```

```python
getConfigGroupStateFromCache(
    group: str, *, native: Literal[False] = False
) -> Configuration
```

```python
getConfigGroupStateFromCache(
    group: str, *, native: bool = False
) -> Configuration | Configuration
```

Return the state of the system cache, for the devices in the specified group.

**Why Override?** The `pymmcore_plus.Configuration` object returned when `native=False` (the default) provides a nicer `Mapping` interface. Pass `native=True` to get the original `pymmcore.Configuration` object.

### getConfigState

```python
getConfigState(
    group: str, config: str, *, native: bool = False
) -> Configuration | Configuration
```

Return state of devices included in the specified configuration.

**Why Override?** The `pymmcore_plus.Configuration` object returned when `native=False` (the default) provides a nicer `Mapping` interface. Pass `native=True` to get the original `pymmcore.Configuration` object.

### getCurrentConfig

```python
getCurrentConfig(
    groupName: ConfigGroupName | str,
) -> ConfigPresetName | Literal[""]
```

Returns the current configuration (preset) for a given group.

Returns empty string if no configuration is selected.

### getCurrentConfigFromCache

```python
getCurrentConfigFromCache(
    groupName: ConfigGroupName | str,
) -> ConfigPresetName | Literal[""]
```

Returns the configuration for a given group based on the data in the cache.

### getOrGuessChannelGroup

```python
getOrGuessChannelGroup() -> list[str]
```

Get the channelGroup or find a likely set of candidates.

✨ *This method is new in `CMMCorePlus`.*

If the group is not defined via `.getChannelGroup` then likely candidates will be found by searching for config groups with names that match this object's `channelGroup_pattern` property. This is a settable property with a default value of:

```text
reg = re.compile("(chan{1,2}(el)?|filt(er)?)s?", re.IGNORECASE)
```

### isConfigDefined

```python
isConfigDefined(groupName: str, configName: str) -> bool
```

Checks if the configuration already exists within a group.

If either the groupName or configName are not recognized, returns False.

### isGroupDefined

```python
isGroupDefined(groupName: str) -> bool
```

Checks if the group already exists.

### iterConfigGroups

```python
iterConfigGroups() -> Iterator[ConfigGroup]
```

Iterate `ConfigGroup` objects for all configs.

✨ *This method is new in `CMMCorePlus`.*

Yields:

| Type | Description |
| --- | --- |
| `ConfigGroup` | `ConfigGroup` objects |

### renameConfig

```python
renameConfig(
    groupName: ConfigGroupName | str,
    oldConfigName: ConfigPresetName | str,
    newConfigName: str,
) -> None
```

Renames a configuration within a specified group.

The command will fail if the configuration was not previously defined.

### renameConfigGroup

```python
renameConfigGroup(
    oldGroupName: ConfigGroupName | str, newGroupName: str
) -> None
```

Renames a configuration group.

### setChannelGroup

```python
setChannelGroup(channelGroup: str) -> None
```

Specifies the group determining the channel selection.

...and send a channelGroupChanged signal.

### setConfig

```python
setConfig(groupName: str, configName: str) -> None
```

Applies a configuration to a group.

**Why Override?** The native `onConfigGroupChanged` callback is not always called whenever `CMMCore.setConfig` has been called. We override here to emit a `configSet` event whenever `setConfig` is called. See [https://github.com/micro-manager/mmCoreAndDevices/issues/25](<https://github.com/micro-manager/mmCoreAndDevices/issues/25>) for details.

### waitForConfig

```python
waitForConfig(
    group: ConfigGroupName | str, configName: ConfigPresetName | str
) -> None
```

Blocks until all devices included in the configuration become ready.

## State devices

### defineStateLabel

```python
defineStateLabel(
    stateDeviceLabel: DeviceLabel | str, state: int, stateLabel: str
) -> None
```

Defines a label for the specific state.

### getDeviceInitializationState

```python
getDeviceInitializationState(label: str) -> DeviceInitializationState
```

Queries the initialization state of the given device.

**Why Override?** The returned `pymmcore_plus.DeviceInitializationState` enum is more interpretable than the raw `int` returned by `pymmcore`

### getNumberOfStates

```python
getNumberOfStates(stateDeviceLabel: DeviceLabel | str) -> int
```

Returns the total number of available positions (states).

### getParentLabel

```python
getParentLabel(peripheralLabel: DeviceLabel | str) -> DeviceLabel | Literal['']
```

Returns parent device. Returns empty string if no parent is found.

### getState

```python
getState(stateDeviceLabel: DeviceLabel | str) -> int
```

Returns the current state (position) on the specific device.

### getStateFromLabel

```python
getStateFromLabel(
    stateDeviceLabel: DeviceLabel | str, stateLabel: StateLabel | str
) -> int
```

Obtain the state for a given label.

### getStateLabel

```python
getStateLabel(stateDeviceLabel: DeviceLabel | str) -> StateLabel
```

Returns the current state as the label (string).

### getStateLabels

```python
getStateLabels(stateDeviceLabel: DeviceLabel | str) -> tuple[StateLabel, ...]
```

Return labels for all states

### getSystemState

```python
getSystemState(*, native: bool = False) -> Configuration | Configuration
```

Return the entire system state.

**Why Override?** The `pymmcore_plus.Configuration` object returned when `native=False` (the default) provides a nicer `Mapping` interface. Pass `native=True` to get the original `pymmcore.Configuration` object.

### guessObjectiveDevices

```python
guessObjectiveDevices() -> list[str]
```

Find any loaded devices that are likely to be an Objective/Nosepiece.

✨ *This method is new in `CMMCorePlus`.*

Likely matches are loaded StateDevices with names that match this object's `objective_device_pattern` property. This is a settable property with a default value of::

```text
re.compile("(.+)?(nosepiece|obj(ective)?)(turret)?s?", re.IGNORECASE)
```

### loadSystemState

```python
loadSystemState(fileName: str) -> None
```

Loads the system configuration from the text file conforming to the MM specific format.

### objective\_device\_pattern

```python
objective_device_pattern: Pattern
```

Pattern used to guess objective device labels.

✨ \*This property is new in `CMMCorePlus`.

It is the regex used by `guessObjectiveDevices` to find any devices that are likely to be objective devices.

By default:

```text
re.compile("(.+)?(nosepiece|obj(ective)?)(turret)?s?", re.IGNORECASE)
```

### saveSystemState

```python
saveSystemState(fileName: str) -> None
```

Saves the current system state to a text file of the MM specific format.

### setParentLabel

```python
setParentLabel(
    deviceLabel: DeviceLabel | str, parentHubLabel: DeviceLabel | str
) -> None
```

Sets parent device label

### setState

```python
setState(stateDeviceLabel: str, state: int) -> None
```

Set state (by position) on `stateDeviceLabel`, with reliable event emission.

**Why Override?** In `MMCore`, the calling of the `onPropertyChanged` callback is left to the underlying device adapter, which means it is not always called. This method overrides the default implementation to ensure that `events.propertyChanged` is *always* emitted when `setProperty` has been called and the property Value has actually changed.

### setStateLabel

```python
setStateLabel(stateDeviceLabel: str, stateLabel: str) -> None
```

Set state (by label) on `stateDeviceLabel`, with reliable event emission.

**Why Override?** In `MMCore`, the calling of the `onPropertyChanged` callback is left to the underlying device adapter, which means it is not always called. This method overrides the default implementation to ensure that `events.propertyChanged` is *always* emitted when `setProperty` has been called and the property Value has actually changed.

### setSystemState

```python
setSystemState(conf: Configuration) -> None
```

Sets all properties contained in the Configuration object.

## System state &amp; configuration files

### describe

```python
describe(
    sort: str | None = None,
    show_config_groups: bool = False,
    show_available: bool = False,
) -> None
```

Print information table with the current configuration.

Intended to provide a quick overview of the microscope configuration during interactive terminal usage.

✨ *This method is new in `CMMCorePlus`.*

### getAPIVersionInfo

```python
getAPIVersionInfo() -> str
```

Returns the module and device interface versions.

### getMMCoreVersionMajor

```python
getMMCoreVersionMajor() -> int
```

### getMMCoreVersionMinor

```python
getMMCoreVersionMinor() -> int
```

### getMMCoreVersionPatch

```python
getMMCoreVersionPatch() -> int
```

### getMMDeviceDeviceInterfaceVersion

```python
getMMDeviceDeviceInterfaceVersion() -> int
```

### getMMDeviceModuleInterfaceVersion

```python
getMMDeviceModuleInterfaceVersion() -> int
```

### getSystemStateCache

```python
getSystemStateCache(*, native: Literal[True]) -> Configuration
```

```python
getSystemStateCache(*, native: Literal[False] = False) -> Configuration
```

```python
getSystemStateCache(*, native: bool = False) -> Configuration | Configuration
```

Return the entire system state from cache.

**Why Override?** The `pymmcore_plus.Configuration` object returned when `native=False` (the default) provides a nicer `Mapping` interface. Pass `native=True` to get the original `pymmcore.Configuration` object.

### getVersionInfo

```python
getVersionInfo() -> str
```

Displays core version.

### loadSystemConfiguration

```python
loadSystemConfiguration(fileName: str | Path = 'MMConfig_demo.cfg') -> None
```

Load a system config file conforming to the MM `.cfg` format.

[https://micro-manager.org/Micro-Manager\_Configuration\_Guide\#configuration-file-syntax](<https://micro-manager.org/Micro-Manager_Configuration_Guide#configuration-file-syntax>)

For relative paths, the current working directory is first checked, then the then device adapter path is checked.

**Why Override?** This method overrides the default implementation to A) allow loading the `MMConfig_demo.cfg` file by default, B) to provide more flexible path declarations and C) better error messages when the file cannot be found.

### reset

```python
reset() -> None
```

Unloads all devices from the core, clears all configuration data and property blocks.

### saveSystemConfiguration

```python
saveSystemConfiguration(filename: str) -> None
```

Saves the current system configuration to a text file.

**Why Override?** To also save pixel size configurations.

### state

```python
state(
    *, cached: bool = True, include_time: bool = False, **_kwargs: Any
) -> SummaryMetaV1
```

Return info on the current state of the core.

### systemConfigurationFile

```python
systemConfigurationFile() -> str | None
```

Return the path to the last loaded system configuration file, or `None`.

✨ *This method is new in `CMMCorePlus`.*

### updateSystemStateCache

```python
updateSystemStateCache() -> None
```

Updates the state of the entire hardware.

### waitForSystem

```python
waitForSystem() -> None
```

Blocks until all devices in the system become ready (not-busy).

## Properties

### getAllowedPropertyValues

```python
getAllowedPropertyValues(
    label: DeviceLabel | str, propName: PropertyName | str
) -> tuple[str, ...]
```

Returns all valid values for the specified property.

### getDevicePropertyNames

```python
getDevicePropertyNames(label: DeviceLabel | str) -> tuple[PropertyName, ...]
```

Returns all property names supported by the device.

### getProperty

```python
getProperty(label: DeviceLabel | str, propName: PropertyName | str) -> str
```

Returns the property value for the specified device.

The return value will always be a string. Use getPropertyType to determine the correct type.

### getPropertyFromCache

```python
getPropertyFromCache(
    deviceLabel: DeviceLabel | str, propName: PropertyName | str
) -> str
```

Returns the cached property value for the specified device.

### getPropertyLowerLimit

```python
getPropertyLowerLimit(
    label: DeviceLabel | str, propName: PropertyName | str
) -> float
```

Returns the property lower limit value, if the property has limits - 0 otherwise.

### getPropertyObject

```python
getPropertyObject(device_label: str, property_name: str) -> DeviceProperty
```

Return a DeviceProperty object bound to a device/property on this core.

✨ *This method is new in `CMMCorePlus`.*

`DeviceProperty` objects are a convenient object oriented way to interact with a specific device properties. They allow you to call any method on `CMMCore` that normally requires a `deviceLabel` and `propertyName` as the first two arguments as an argument-free method on the `DeviceProperty` object.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_label` | `str` | Device label to get a property object for. | *required* |
| `property_name` | `str` | Property name to get a property object for. | *required* |

Examples:

```pycon
>>> core = CMMCorePlus()
>>> core.loadDevice("DemoCamera", "DemoCamera", "DCam")
>>> core.initializeDevice("DemoCamera")
>>> core.setCameraDevice("DemoCamera")
>>> exposure = core.getPropertyObject("DemoCamera", "Exposure")
>>> exposure.type()
<PropertyType.Float: 2>
>>> exposure.upperLimit()
10000.0
```

get/set property values easily:

```pycon
>>> exposure.value
10.0
>>> exposure.value = 5.0
>>> exposure.value
5.0
>>> core.getExposure()  # changes reflected in core
5.0
```

### getPropertyType

```python
getPropertyType(label: str, propName: str) -> PropertyType
```

Return the intrinsic property type for a given device and property.

**Why Override?** The returned `pymmcore_plus.PropertyType` enum is more interpretable than the raw `int` returned by `pymmcore`

### getPropertyUpperLimit

```python
getPropertyUpperLimit(
    label: DeviceLabel | str, propName: PropertyName | str
) -> float
```

Returns the property upper limit value, if the property has limits - 0 otherwise.

### hasProperty

```python
hasProperty(label: DeviceLabel | str, propName: PropertyName | str) -> bool
```

Checks if device has a property with a specified name.

### hasPropertyLimits

```python
hasPropertyLimits(
    label: DeviceLabel | str, propName: PropertyName | str
) -> bool
```

Queries device if the specific property has limits.

### isPropertyPreInit

```python
isPropertyPreInit(
    label: DeviceLabel | str, propName: PropertyName | str
) -> bool
```

Tells us whether the property must be defined prior to initialization.

### isPropertyReadOnly

```python
isPropertyReadOnly(
    label: DeviceLabel | str, propName: PropertyName | str
) -> bool
```

Tells us whether the property can be modified.

### iterProperties

```python
iterProperties(
    property_type: int | Iterable[int] | None = ...,
    property_name_pattern: str | Pattern | None = ...,
    *,
    device_type: int | Iterable[int] | None = ...,
    device_label: str | Pattern | None = ...,
    has_limits: bool | None = None,
    is_read_only: bool | None = None,
    is_sequenceable: bool | None = None,
    as_object: Literal[False],
) -> Iterator[tuple[str, str]]
```

```python
iterProperties(
    property_type: int | Iterable[int] | None = ...,
    property_name_pattern: str | Pattern | None = ...,
    *,
    device_type: int | Iterable[int] | None = ...,
    device_label: str | Pattern | None = ...,
    has_limits: bool | None = None,
    is_read_only: bool | None = None,
    is_sequenceable: bool | None = None,
    as_object: Literal[True] = ...,
) -> Iterator[DeviceProperty]
```

```python
iterProperties(
    property_type: int | Iterable[int] | None = None,
    property_name_pattern: str | Pattern | None = None,
    *,
    device_type: int | Iterable[int] | None = None,
    device_label: str | Pattern | None = None,
    has_limits: bool | None = None,
    is_read_only: bool | None = None,
    is_sequenceable: bool | None = None,
    as_object: bool = True,
) -> Iterator[DeviceProperty] | Iterator[tuple[str, str]]
```

Iterate over currently loaded (device\_label, property\_name) pairs.

✨ *This method is new in `CMMCorePlus`.*

It offers a convenient way to iterate over loaded devices, optionally filtering by `DeviceType` and/or device label. It can also yields `DeviceProperty` objects if `as_object` is `True` (the default).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `property_type` | `int \| Sequence[int] \| None` | PropertyType (or types) to filter by, by default all property types will be yielded. | `None` |
| `property_name_pattern` | `str \| Pattern \| None` | Property name to filter by, by default all property names will be yielded. May be a compiled regular expression or a string, in which case it will be compiled with `re.IGNORECASE`. | `None` |
| `device_type` | `DeviceType \| None` | DeviceType to filter by, by default all device types will be yielded. | `None` |
| `device_label` | `str \| None` | Device label to filter by, by default all device labels will be yielded. | `None` |
| `has_limits` | `bool \| None` | If provided, only properties with `hasPropertyLimits` matching this value will be yielded. | `None` |
| `is_read_only` | `bool \| None` | If provided, only properties with `isPropertyReadOnly` matching this value will be yielded. | `None` |
| `is_sequenceable` | `bool \| None` | If provided only properties with `isPropertySequenceable` matching this value will be yielded. | `None` |
| `as_object` | `bool` | If `True`, `DeviceProperty` objects will be yielded instead of `(device_label, property_name)` tuples. By default True | `True` |

Yields:

| Type | Description |
| --- | --- |
| `DeviceProperty \| tuple[str, str]` | `DeviceProperty` objects (if `as_object==True`) or 2-tuples of (device\_name, property\_name) |

### setProperty

```python
setProperty(
    label: str, propName: str, propValue: bool | float | int | str
) -> None
```

Set property named `propName` on device `label` to `propValue`.

**Why Override?** In `MMCore`, the calling of the `onPropertyChanged` callback is left to the underlying device adapter, which means it is not always called. This method overrides the default implementation to ensure that `events.propertyChanged` is *always* emitted when `setProperty` has been called and the property Value has actually changed.

### updateCoreProperties

```python
updateCoreProperties() -> None
```

Updates CoreProperties (currently all Core properties are devices types) with the loaded hardware.

## Devices

### detectDevice

```python
detectDevice(deviceLabel: str) -> DeviceDetectionStatus
```

Tries to communicate to a device through a given serial port.

Used to automate discovery of correct serial port. Also configures the serial port correctly.

**Why Override?** The returned `pymmcore_plus.DeviceDetectionStatus` enum is more interpretable than the raw `int` returned by `pymmcore`

### deviceBusy

```python
deviceBusy(label: DeviceLabel | str) -> bool
```

Checks the busy status of the specific device.

### deviceTypeBusy

```python
deviceTypeBusy(devType: DeviceType) -> bool
```

Checks the busy status for all devices of the specific type.

### getAdapterObject

```python
getAdapterObject(library_name: str) -> DeviceAdapter
```

Return an `Adapter` object bound to library\_name on this core.

✨ *This method is new in `CMMCorePlus`.*

`Adapter` objects are a convenient object oriented way to interact with device adapters. They allow you to call any method on `CMMCore` that normally requires a `library_name` as the first argument as an argument-free method on the `Adapter` object.

### getAvailableDeviceDescriptions

```python
getAvailableDeviceDescriptions(library: AdapterName | str) -> tuple[str, ...]
```

Get descriptions for available devices from the specified library.

### getAvailableDevices

```python
getAvailableDevices(library: AdapterName | str) -> tuple[DeviceName, ...]
```

Get available devices from the specified device library.

### getAvailableDeviceTypes

```python
getAvailableDeviceTypes(library: AdapterName | str) -> tuple[int, ...]
```

Get type information for available devices from the specified library.

### getCurrentDeviceOfType

```python
getCurrentDeviceOfType(
    device_type: DeviceTypesWithCurrent,
) -> DeviceLabel | Literal[""]
```

Return the current device of type `device_type`.

Only the following device types have a "current" device: - CameraDevice - ShutterDevice - StageDevice - XYStageDevice - AutoFocusDevice - SLMDevice - GalvoDevice - ImageProcessorDevice

Calling this method with any other device type will raise a `ValueError`.

✨ *This method is new in `CMMCorePlus`.*

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_type` | `DeviceType` | The type of device to get the current device for. See `DeviceType` for a list of device types. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `str` | The label of the current device of type `device_type`. If no device of that type is currently set, an empty string is returned. |

Raises:

| Type | Description |
| --- | --- |
| `ValueError` | If the core does not have the concept of a "current" device of the provided `device_type`. |

### getDeviceAdapterNames

```python
getDeviceAdapterNames() -> tuple[AdapterName, ...]
```

Return the names of discoverable device adapters.

### getDeviceAdapterSearchPaths

```python
getDeviceAdapterSearchPaths() -> tuple[str, ...]
```

Return the current device adapter search paths.

### getDeviceDelayMs

```python
getDeviceDelayMs(label: DeviceLabel | str) -> float
```

Reports action delay in milliseconds for the specific device.

### getDeviceDescription

```python
getDeviceDescription(label: DeviceLabel | str) -> str
```

Returns description text for a given device label. "Description" is determined by the library and is immutable.

### getDeviceLibrary

```python
getDeviceLibrary(label: DeviceLabel | str) -> AdapterName
```

Returns device library (aka module, device adapter) name.

### getDeviceName

```python
getDeviceName(label: DeviceLabel | str) -> DeviceName
```

Returns device name for a given device label.

### getDeviceObject

```python
getDeviceObject(
    device_label: str, device_type: Literal[Camera]
) -> CameraDevice
```

```python
getDeviceObject(device_label: str, device_type: Literal[Stage]) -> StageDevice
```

```python
getDeviceObject(device_label: str, device_type: Literal[State]) -> StateDevice
```

```python
getDeviceObject(
    device_label: str, device_type: Literal[Shutter]
) -> ShutterDevice
```

```python
getDeviceObject(
    device_label: str, device_type: Literal[XYStage]
) -> XYStageDevice
```

```python
getDeviceObject(
    device_label: str, device_type: Literal[Serial]
) -> SerialDevice
```

```python
getDeviceObject(
    device_label: str, device_type: Literal[Generic]
) -> GenericDevice
```

```python
getDeviceObject(
    device_label: str, device_type: Literal[AutoFocus]
) -> AutoFocusDevice
```

```python
getDeviceObject(
    device_label: str, device_type: Literal[ImageProcessor]
) -> ImageProcessorDevice
```

```python
getDeviceObject(
    device_label: str, device_type: Literal[SignalIO]
) -> SignalIODevice
```

```python
getDeviceObject(
    device_label: str, device_type: Literal[Magnifier]
) -> MagnifierDevice
```

```python
getDeviceObject(device_label: str, device_type: Literal[SLM]) -> SLMDevice
```

```python
getDeviceObject(device_label: str, device_type: Literal[Hub]) -> HubDevice
```

```python
getDeviceObject(device_label: str, device_type: Literal[Galvo]) -> GalvoDevice
```

```python
getDeviceObject(
    device_label: Literal[CoreDevice], device_type: Literal[Core]
) -> CoreDevice
```

```python
getDeviceObject(device_label: str, device_type: DeviceType = ...) -> Device
```

```python
getDeviceObject(device_label: str, device_type: type[_DT]) -> _DT
```

```python
getDeviceObject(
    device_label: str, device_type: type[_DT] | DeviceType = Any
) -> _DT | Device
```

Return a `Device` object bound to device\_label on this core.

✨ *This method is new in `CMMCorePlus`.*

`Device` objects are a convenient object oriented way to interact with devices. They allow you to call any method on `CMMCore` that normally requires a `deviceLabel` as the first argument as an argument-free method on the `Device` object.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_label` | `str` | Device label to get a device object for. | *required* |

Examples:

```pycon
>>> core = CMMCorePlus()
>>> cam = core.getDeviceObject("DemoCamera")
>>> cam.isLoaded()
False
>>> cam.load("DemoCamera", "DCam")
>>> cam.isLoaded()
True
>>> cam.initialize()
```

get the device schema

```pycon
>>> cam.schema()
{
    'title': 'DCam',
    'description': 'Demo camera',
    'type': 'object',
    'properties': {
        'HubID': {'type': 'string', 'readOnly': True, 'default': ''},
        'MaximumExposureMs': {'type': 'number', 'preInit': True},
        'TransposeCorrection': {'type': 'boolean'},
        'TransposeMirrorX': {'type': 'boolean'},
        'TransposeMirrorY': {'type': 'boolean'},
        'TransposeXY': {'type': 'boolean'}
    }
}
```

### getDeviceSchema

```python
getDeviceSchema(device_label: str) -> DeviceSchema
```

Return JSON-schema describing device `device_label` and its properties.

✨ *This method is new in `CMMCorePlus`. It provides a convenient way to get all of the information about a device in a single call.*

Returns:

| Type | Description |
| --- | --- |
| `DeviceSchema` | JSON-schema describing device `device_label` and its properties. |

Examples:

```pycon
>>> core = CMMCorePlus()
>>> core.loadDevice("DemoCamera", "DemoCamera", "DCam")
>>> core.getDeviceSchema("DemoCamera")
{
    'title': 'DCam',
    'description': 'Demo camera',
    'type': 'object',
    'properties': {
        'HubID': {'type': 'string', 'readOnly': True, 'default': ''},
        'MaximumExposureMs': {'type': 'number', 'preInit': True},
        'TransposeCorrection': {'type': 'boolean'},
        'TransposeMirrorX': {'type': 'boolean'},
        'TransposeMirrorY': {'type': 'boolean'},
        'TransposeXY': {'type': 'boolean'}
    }
}
```

### getDeviceTimeoutMs

```python
getDeviceTimeoutMs(label: DeviceLabel | str) -> int
```

Returns the per-device timeout in milliseconds, or the default if not set.

### getDeviceType

```python
getDeviceType(label: str) -> DeviceType
```

Return device type for a given device.

**Why Override?** The returned `pymmcore_plus.Device` enum is more interpretable than the raw `int` returned by `pymmcore`

### getInstalledDeviceDescription

```python
getInstalledDeviceDescription(
    hubLabel: DeviceLabel | str, peripheralLabel: DeviceName | str
) -> str
```

Returns description from the specified peripheral on `hubLabel` device.

### getInstalledDevices

```python
getInstalledDevices(hubLabel: DeviceLabel | str) -> tuple[DeviceName, ...]
```

Performs auto-detection and loading of child devices that are attached to a Hub device.

Raises RuntimeError if hubLabel is not a hub device.

### getLoadedDevices

```python
getLoadedDevices() -> tuple[DeviceLabel, ...]
```

Returns an array of labels for currently loaded devices.

### getLoadedDevicesOfType

```python
getLoadedDevicesOfType(devType: DeviceType) -> tuple[DeviceLabel, ...]
```

Returns an array of labels for currently loaded devices of specific type.

### getLoadedPeripheralDevices

```python
getLoadedPeripheralDevices(
    hubLabel: DeviceLabel | str,
) -> tuple[DeviceLabel, ...]
```

Return labels of all loaded peripherals of `hubLabel` device.

Returns empty tuple if hubLabel is not a hub device, or even if hubLabel is not the name of any device.

### getTimeoutMs

```python
getTimeoutMs() -> int
```

Get the timeout for all wait commands.

(Default is 5000 ms)

### hasDeviceTimeout

```python
hasDeviceTimeout(label: DeviceLabel | str) -> bool
```

Returns True if a per-device timeout has been set for the given device.

### initializeAllDevices

```python
initializeAllDevices() -> None
```

Calls Initialize() method for each loaded device.

See `ParallelDeviceInitialization` feature flag for controlling the order of initialization.

### initializeDevice

```python
initializeDevice(label: DeviceLabel | str) -> None
```

Initializes specific device.

### iterDeviceAdapters

```python
iterDeviceAdapters(
    adapter_pattern: str | Pattern | None = ...,
    *,
    as_object: Literal[True] = ...,
) -> Iterator[DeviceAdapter]
```

```python
iterDeviceAdapters(
    adapter_pattern: str | Pattern | None = ..., *, as_object: Literal[False]
) -> Iterator[str]
```

```python
iterDeviceAdapters(
    adapter_pattern: str | Pattern | None = None, *, as_object: bool = True
) -> Iterator[DeviceAdapter] | Iterator[str]
```

Iterate over all available device adapters.

✨ *This method is new in `CMMCorePlus`.*

It offers a convenient way to iterate over available device adaptor libraries, optionally filtering adapter library name. It can also yield `Adapter` objects if `as_object` is `True` (the default)

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `adapter_pattern` | `str \| None` | Device adapter name or pattern to filter by, by default all device adapters will be yielded. | `None` |
| `as_object` | `bool` | If `True`, `Adapter` objects will be yielded instead of library name strings. By default True | `True` |

Yields:

| Type | Description |
| --- | --- |
| `Device \| str` | `Device` objects (if `as_object==True`) or device label strings. |

### iterDevices

```python
iterDevices(
    device_type: int | Iterable[int] | None = ...,
    device_label: str | Pattern | None = ...,
    device_adapter: str | Pattern | None = ...,
    *,
    as_object: Literal[False],
) -> Iterator[str]
```

```python
iterDevices(
    device_type: int | Iterable[int] | None = ...,
    device_label: str | Pattern | None = ...,
    device_adapter: str | Pattern | None = ...,
    *,
    as_object: Literal[True] = ...,
) -> Iterator[Device]
```

```python
iterDevices(
    device_type: int | Iterable[int] | None = None,
    device_label: str | Pattern | None = None,
    device_adapter: str | Pattern | None = None,
    *,
    as_object: bool = True,
) -> Iterator[Device] | Iterator[str]
```

Iterate over currently loaded devices.

✨ *This method is new in `CMMCorePlus`.*

It offers a convenient way to iterate over loaded devices, optionally filtering by `DeviceType` and/or device label. It can also yield `Device` objects if `as_object` is `True` (the default).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `device_type` | `DeviceType \| None` | DeviceType to filter by, by default all device types will be yielded. | `None` |
| `device_label` | `str \| None` | Device label to filter by, by default all device labels will be yielded. | `None` |
| `device_adapter` | `str \| None` | Device adapter library to filter by, by default devices from all libraries will be yielded. | `None` |
| `as_object` | `bool` | If `True`, `Device` objects will be yielded instead of device label strings. By default True | `True` |

Yields:

| Type | Description |
| --- | --- |
| `Device \| str` | `Device` objects (if `as_object==True`) or device label strings. |

### loadDevice

```python
loadDevice(label: str, moduleName: str, deviceName: str) -> None
```

Load a device from the plugin library.

**Why Override?** To add much better error messages in the case of failure.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `label` | `str` | Name to be assigned to the device during this core session. | *required* |
| `moduleName` | `str` | The name of the device adapter module (short name, not full file name). See `pymmcore.CMMCore.getDeviceAdapterNames` for a list of valid module names. | *required* |
| `deviceName` | `str` | the name of the device. The name must correspond to one of the names recognized by the specific plugin library. See `pymmcore.CMMCore.getAvailableDevices` for a list of valid device names. | *required* |

### setDeviceAdapterSearchPaths

```python
setDeviceAdapterSearchPaths(paths: Sequence[str]) -> None
```

Set the device adapter search paths.

**Why Override?** In cases where MM device adapters use dynamically loaded libraries, the device adapter search paths must also be added to the `PATH` environment variable (e.g. [https://github.com/micro-manager/pymmcore/issues/28](<https://github.com/micro-manager/pymmcore/issues/28>)). This method overrides the default implementation to ensure that the `PATH` environment variable is updated when the device adapter search paths are changed.

### setDeviceDelayMs

```python
setDeviceDelayMs(label: DeviceLabel | str, delayMs: float) -> None
```

Overrides the built-in value for the action delay.

### setDeviceTimeoutMs

```python
setDeviceTimeoutMs(label: DeviceLabel | str, timeoutMs: int) -> None
```

Sets a per-device timeout in milliseconds.

### setTimeoutMs

```python
setTimeoutMs(timeoutMs: int) -> None
```

Sets the timeout for all wait commands.

(Default is 5000 ms)

### supportsDeviceDetection

```python
supportsDeviceDetection(deviceLabel: DeviceLabel | str) -> bool
```

Return whether or not the device supports automatic device detection (i.e.

### systemBusy

```python
systemBusy() -> bool
```

Checks the busy status of the entire system.

### unloadAllDevices

```python
unloadAllDevices() -> None
```

Unload all devices from the core and reset all configuration data.

**Why Override?** To add logging.

### unloadDevice

```python
unloadDevice(label: DeviceLabel | str) -> None
```

Unloads the device from the core and adjusts all configuration data.

### unloadLibrary

```python
unloadLibrary(moduleName: AdapterName | str) -> None
```

Forcefully unload a library.

### unsetDeviceTimeout

```python
unsetDeviceTimeout(label: DeviceLabel | str) -> None
```

Removes any per-device timeout, restoring the default.

### usesDeviceDelay

```python
usesDeviceDelay(label: DeviceLabel | str) -> bool
```

Signals if the device will use the delay setting or not.

### waitForDevice

```python
waitForDevice(label: DeviceLabel | str) -> None
```

Waits (blocks the calling thread) until the specified device becomes non-busy.

### waitForDeviceType

```python
waitForDeviceType(devType: DeviceType) -> None
```

Blocks until all devices of the specific type become ready (not-busy).

## Logging &amp; errors

### debugLogEnabled

```python
debugLogEnabled() -> bool
```

Indicates if logging of debug messages is enabled

### enableDebugLog

```python
enableDebugLog(enable: bool) -> None
```

Enable or disable logging of debug messages.

### enableFeature

```python
enableFeature(name: FeatureFlag | str, enable: bool) -> None
```

Enable or disable the given Core feature.

Core features control whether experimental functionality (which is subject to breaking changes) is exposed, or whether stricter API usage is enforced.

Currently switchable features:

- "StrictInitializationChecks" (default: disabled) When enabled, an exception is thrown when an operation requiring an initialized device is attempted on a device that is not successfully initialized. When disabled, no exception is thrown and a warning is logged (and the operation may potentially cause incorrect behavior or a crash).
- "ParallelDeviceInitialization" (default: enabled) When enabled, serial ports are initialized in serial order, and all other devices are in parallel, using multiple threads, one per device module. Early testing shows this to be reliable, but switch this off when issues are encountered during device initialization.

### enableStderrLog

```python
enableStderrLog(enable: bool) -> None
```

Enables or disables log message display on the standard console.

### getCoreErrorText

```python
getCoreErrorText(code: int) -> str
```

Returns a pre-defined error test with the given error code

### getPrimaryLogFile

```python
getPrimaryLogFile() -> str
```

Return the name of the primary Core log file.

### getPrimaryLogLevel

```python
getPrimaryLogLevel() -> LogLevel
```

Return the current primary log file level.

### getStderrLogLevel

```python
getStderrLogLevel() -> LogLevel
```

Return the current stderr log level.

### isFeatureEnabled

```python
isFeatureEnabled(name: str) -> bool
```

Return whether the given Core feature is currently enabled.

See `enableFeature()` for the available features.

Raises RuntimeError if the feature name is not recognized.

### log

```python
log(msg: str, level: LogLevel) -> None
```

```python
log(msg: str, level: LogLevel, loggerName: str) -> None
```

```python
log(msg: str, level: LogLevel) -> None
```

Log a message at the given level.

### logMessage

```python
logMessage(msg: str) -> None
```

```python
logMessage(msg: str, debugOnly: bool) -> None
```

```python
logMessage(msg: str) -> None
```

Record text message in the log file.

### setPrimaryLogFile

```python
setPrimaryLogFile(filename: str) -> None
```

```python
setPrimaryLogFile(filename: str, truncate: bool) -> None
```

```python
setPrimaryLogFile(filename: str) -> None
```

Set the primary Core log file.

### setPrimaryLogFileRotation

```python
setPrimaryLogFileRotation(maxFileSize: int, maxBackupCount: int) -> None
```

Set the primary log file rotation parameters.

### setPrimaryLogLevel

```python
setPrimaryLogLevel(level: LogLevel) -> None
```

Set the log level for the primary log file.

### setStderrLogLevel

```python
setStderrLogLevel(level: LogLevel) -> None
```

Set the stderr log level.

### startSecondaryLogFile

```python
startSecondaryLogFile(filename: str, enableDebug: bool) -> int
```

```python
startSecondaryLogFile(filename: str, enableDebug: bool, truncate: bool) -> int
```

```python
startSecondaryLogFile(
    filename: str, enableDebug: bool, truncate: bool, synchronous: bool
) -> int
```

```python
startSecondaryLogFile(filename: str, enableDebug: bool) -> int
```

Start capturing logging output into an additional file.

### stderrLogEnabled

```python
stderrLogEnabled() -> bool
```

Indicates whether logging output goes to stdErr

### stopSecondaryLogFile

```python
stopSecondaryLogFile(handle: int) -> None
```

Stop capturing logging output into an additional file.

## Other

### instance

```python
instance() -> CMMCorePlus
```

Return the global singleton instance of `CMMCorePlus`.

✨ *This method is new in `CMMCorePlus`.*

In many cases, a single instance of `CMMCorePlus` is all that will be created in a given session. This class method provides a convenient way to access that instance.

> [!TIP]
>
> Creating/accessing a `CMMCorePlus` object using `CMMCorePlus.instance()` is a convenient way to access the same core instance from multiple places in your code. All widgets in [`pymmcore-widgets`](<https://github.com/pymmcore-plus/pymmcore-widgets>) also use `CMMCorePlus.instance()` by default, so any widgets you use will automatically connect to the same core instance without any additional configuration.
>
> Attempts *are* made to make it thread-safe. But please open an issue if you find any problems.

### noop

```python
noop() -> None
```

A static method that does nothing.

### sleep

```python
sleep(intervalMs: float) -> None
```

Waits (blocks the calling thread) for specified time in milliseconds.

## Typed dictionaries

These are the return types of `getDeviceSchema`.

### DeviceSchema

Bases: `TypedDict`

JSON schema `dict` describing a device.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `title` | `str` |  |
| `description` | `str` |  |
| `type` | `str` |  |
| `properties` | `dict[str, PropertySchema]` |  |

#### title

```python
title: str
```

#### description

```python
description: str
```

#### type

```python
type: str
```

#### properties

```python
properties: dict[str, PropertySchema]
```

### PropertySchema

Bases: `TypedDict`

JSON schema `dict` describing a device property.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `type` | `str` |  |
| `maximum` | `float` |  |
| `minimum` | `float` |  |
| `enum` | `list` |  |
| `readOnly` | `bool` |  |
| `default` | `Any` |  |
| `sequenceable` | `bool` |  |
| `sequenceMaxLength` | `int` |  |
| `preInit` | `bool` |  |

#### type

```python
type: str
```

#### maximum

```python
maximum: float
```

#### minimum

```python
minimum: float
```

#### enum

```python
enum: list
```

#### readOnly

```python
readOnly: bool
```

#### default

```python
default: Any
```

#### sequenceable

```python
sequenceable: bool
```

#### sequenceMaxLength

```python
sequenceMaxLength: int
```

#### preInit

```python
preInit: bool
```
