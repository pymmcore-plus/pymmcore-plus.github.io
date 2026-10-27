# Widget Gallery

The top-level widgets in `pymmcore-widgets`, grouped by what they do, roughly in the order you'd reach for them when building a GUI. Click a widget for a runnable example and its API (the screenshots are generated from those examples).

Most of these widgets control a `CMMCorePlus` (by default the global `CMMCorePlus.instance()`, or the one you pass as `mmcore=`). They follow the core's [events](<https://pymmcore-plus.github.io/pymmcore-plus/guides/events/index.md>), so they stay in sync with each other and with your own code. The [sequence editors](<#sequence-editors>) are the exception: they don't use a core at all. (See [Building a custom GUI](<https://pymmcore-plus.github.io/pymmcore-widgets/getting_started/#choosing-a-core>) for the details.)

## Camera and images

Snap and live buttons, an image preview, and the camera's exposure and ROI.

- [**`SnapButton`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/SnapButton/index.md>)

  Button that snaps an image with the current camera.
- [**`LiveButton`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/LiveButton/index.md>)

  Button that starts and stops live mode.
- [**`ImagePreview`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ImagePreview/index.md>)

  A Widget that displays the latest image from the core.
- [**`ExposureWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ExposureWidget/index.md>)

  Spin box that shows and sets the exposure time (in ms) of a camera.
- [**`DefaultCameraExposureWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/DefaultCameraExposureWidget/index.md>)

  A Widget to get/set exposure on the default camera.
- [**`CameraRoiWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/CameraRoiWidget/index.md>)

  A Widget to control the camera device ROI.

## Channels, objectives and presets

These widgets show (and change) the current state of the microscope: the channel, the objective, the preset of any configuration group, and the shutters.

- [**`ChannelWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ChannelWidget/index.md>)

  Combo box that shows and sets the current channel.
- [**`ChannelGroupWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ChannelGroupWidget/index.md>)

  Combo box that chooses which configuration group is the channel group.
- [**`ObjectivesWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ObjectivesWidget/index.md>)

  Combo box that shows and sets the current objective.
- [**`PresetsWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/PresetsWidget/index.md>)

  Combo box that shows and sets the current preset of one configuration group.
- [**`GroupPresetTableWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/GroupPresetTableWidget/index.md>)

  Table of all configuration groups, to view and set their presets.
- [**`ShuttersWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ShuttersWidget/index.md>)

  Button that opens and closes a shutter, with an optional autoshutter checkbox.

## Stages

Move an XY or Z stage, or explore the sample in a zoomable view of the stage, where snapped images appear at the position they were taken.

- [**`StageWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/StageWidget/index.md>)

  Arrow buttons to move an XY stage or a Z (focus) stage.
- [**`StageExplorer`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/StageExplorer/index.md>)

  Zoomable view of the stage, where snapped images appear at their positions.

## Devices and properties

View and change the properties of any of the loaded devices.

- [**`PropertyBrowser`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/PropertyBrowser/index.md>)

  A Widget to browse and change properties of all devices.
- [**`PropertiesWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/PropertiesWidget/index.md>)

  Controls for a filtered set of device properties (a PropertyWidget each).
- [**`PropertyWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/PropertyWidget/index.md>)

  Widget to display and control a single device property.

## Acquisition

Define a multi-dimensional acquisition (a `useq.MDASequence`) and run it on the core. `MDAWidget` is the `MDASequenceWidget` below, connected to a core. It offers the core's channels, can add the current stage position, and has buttons to run, pause and cancel the acquisition.

- [**`MDAWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/MDAWidget/index.md>)

  Main MDA Widget connected to a `pymmcore_plus.CMMCorePlus` instance.
- [**`HCSWizard`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/HCSWizard/index.md>)

  A wizard to set up a high-content screening (HCS) experiment.

## Sequence editors

> [!NOTE]
>
> **No core needed**
>
> These widgets edit `useq` objects and don't touch the microscope. Read the result with `value()`, set it with `setValue()`, and connect to `valueChanged` to hear about changes. Use them to describe an experiment in your own GUI; to run one, pass the sequence to `CMMCorePlus.run_mda` (or use the `MDAWidget` above).

- [**`MDASequenceWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/MDASequenceWidget/index.md>)

  A widget that provides a GUI to construct and edit a `useq.MDASequence`.
- [**`ChannelTable`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ChannelTable/index.md>)

  Table to edit a list of channels (`useq.Channel`).
- [**`TimePlanWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/TimePlanWidget/index.md>)

  Table to edit a time plan (`useq.AnyTimePlan`), one row per phase.
- [**`ZPlanWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ZPlanWidget/index.md>)

  Widget to edit a z plan (`useq.AnyZPlan`).
- [**`PositionTable`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/PositionTable/index.md>)

  Table to edit a list of stage positions (`useq.Position`).
- [**`GridPlanWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/GridPlanWidget/index.md>)

  Widget to edit a grid plan.

## Configuration and setup

Load, create and edit a configuration file (the `ConfigWizard` is Micro-Manager's Hardware Configuration Wizard), set pixel sizes, install device adapters, and watch the core's log.

- [**`ConfigurationWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ConfigurationWidget/index.md>)

  A Widget to select and load a Micro-Manager system configuration.
- [**`ConfigWizard`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ConfigWizard/index.md>)

  Hardware Configuration Wizard for Micro-Manager.
- [**`ConfigGroupsEditor`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ConfigGroupsEditor/index.md>)

  Editor for configuration groups and their presets.
- [**`ConfigGroupsTree`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ConfigGroupsTree/index.md>)

  A tree widget that displays configuration groups.
- [**`PixelConfigurationWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/PixelConfigurationWidget/index.md>)

  A Widget to define the pixel size configurations.
- [**`ObjectivesPixelConfigurationWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/ObjectivesPixelConfigurationWidget/index.md>)

  A Widget to define the pixel size configurations using the objective device.
- [**`InstallWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/InstallWidget/index.md>)

  Widget to install Micro-Manager's device adapters (like `mmcore install`).
- [**`CoreLogWidget`**](<https://pymmcore-plus.github.io/pymmcore-widgets/api/pymmcore_widgets/CoreLogWidget/index.md>)

  Live view of the core's log file.
