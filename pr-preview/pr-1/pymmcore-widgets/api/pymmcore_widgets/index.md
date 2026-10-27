# pymmcore\_widgets

A set of widgets for the pymmcore-plus module.

**Submodules**

| Name | Description |
| --- | --- |
| `config_presets` | Widgets related to configuration groups and presets. |
| `device_properties` | Widgets related to device properties. |
| `experimental` | Experimental widgets. |
| `hcwizard` | Configuration wizard creating/editing a MicroManager configuration file. |
| `useq_widgets` | Widgets for the useq-schema data model. |

**Classes**

| Name | Description |
| --- | --- |
| `CameraRoiWidget` | A Widget to control the camera device ROI. |
| `ChannelGroupWidget` | Combo box that chooses which configuration group is the channel group. |
| `ChannelTable` | Table to edit a list of channels (`useq.Channel`). |
| `ChannelWidget` | Combo box that shows and sets the current channel. |
| `ConfigGroupsEditor` | Editor for configuration groups and their presets. |
| `ConfigGroupsTree` | A tree widget that displays configuration groups. |
| `ConfigWizard` | Hardware Configuration Wizard for Micro-Manager. |
| `ConfigurationWidget` | A Widget to select and load a Micro-Manager system configuration. |
| `CoreLogWidget` | Live view of the core's log file. |
| `DefaultCameraExposureWidget` | A Widget to get/set exposure on the default camera. |
| `ExposureWidget` | Spin box that shows and sets the exposure time (in ms) of a camera. |
| `GridPlanWidget` | Widget to edit a grid plan. |
| `GroupPresetTableWidget` | Table of all configuration groups, to view and set their presets. |
| `HCSWizard` | A wizard to set up a high-content screening (HCS) experiment. |
| `ImagePreview` | A Widget that displays the latest image from the core. |
| `InstallWidget` | Widget to install Micro-Manager's device adapters (like `mmcore install`). |
| `LiveButton` | Button that starts and stops live mode. |
| `MDASequenceWidget` | A widget that provides a GUI to construct and edit a `useq.MDASequence`. |
| `MDAWidget` | Main MDA Widget connected to a `pymmcore_plus.CMMCorePlus` instance. |
| `ObjectivesPixelConfigurationWidget` | A Widget to define the pixel size configurations using the objective device. |
| `ObjectivesWidget` | Combo box that shows and sets the current objective. |
| `PixelConfigurationWidget` | A Widget to define the pixel size configurations. |
| `PositionTable` | Table to edit a list of stage positions (`useq.Position`). |
| `PresetsWidget` | Combo box that shows and sets the current preset of one configuration group. |
| `PropertiesWidget` | Controls for a filtered set of device properties (a PropertyWidget each). |
| `PropertyBrowser` | A Widget to browse and change properties of all devices. |
| `PropertyWidget` | Widget to display and control a single device property. |
| `ShuttersWidget` | Button that opens and closes a shutter, with an optional autoshutter checkbox. |
| `SnapButton` | Button that snaps an image with the current camera. |
| `StageExplorer` | Zoomable view of the stage, where snapped images appear at their positions. |
| `StageWidget` | Arrow buttons to move an XY stage or a Z (focus) stage. |
| `TimePlanWidget` | Table to edit a time plan (`useq.AnyTimePlan`), one row per phase. |
| `ZPlanWidget` | Widget to edit a z plan (`useq.AnyZPlan`). |
