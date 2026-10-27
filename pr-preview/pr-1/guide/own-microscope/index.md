# Using Your Own Microscope

[Getting Started](<https://pymmcore-plus.github.io/getting-started/which-package/index.md>) uses Micro-Manager's demo devices throughout. To control real hardware, you need two more things: the device adapters for your hardware, and a configuration file that says which devices you have and how they're set up.

(If Micro-Manager is running and connected to the same hardware, close it first. See [One program at a time](<https://pymmcore-plus.github.io/getting-started/from-micro-manager/#one-program-at-a-time>).)

## What's a configuration file?

A Micro-Manager configuration file (`.cfg`) is a plain text file listing the devices to load (and which device adapter each one comes from), their initial property values, which device plays which role (camera, shutter, focus stage), and the configuration groups, presets and pixel sizes you've defined. Here are a few lines from the demo configuration, `MMConfig_demo.cfg`:

```text
# Devices
Device,Camera,DemoCamera,DCam
Device,Z,DemoCamera,DStage
Device,XY,DemoCamera,DXYStage
...
# Roles
Property,Core,Camera,Camera
Property,Core,Focus,Z
...
# Group: Channel
# Preset: FITC
ConfigGroup,Channel,FITC,Dichroic,Label,Q505LP
ConfigGroup,Channel,FITC,Emission,Label,Chroma-HQ535
...
PixelSize_um,Res10x,1.0
```

You rarely need to edit one by hand. If you already have a configuration file from Micro-Manager, you can use it as it is (both use the same core, so they read the same files). Micro-Manager's [configuration guide](<https://micro-manager.org/Micro-Manager_Configuration_Guide>) describes the format in detail.

## Making a configuration file

The Hardware Configuration Wizard walks you through adding your devices, setting their properties, assigning roles and saving the file. There are three versions of it, and you can use whichever is handiest:

- In [pymmcore-gui](<https://pymmcore-plus.github.io/pymmcore-gui/index.md>): **Devices \> Hardware Config Wizard...**
- As a widget in your own Python code, `ConfigWizard`:

  ```python
  from pymmcore_widgets import ConfigWizard
  from qtpy.QtWidgets import QApplication

  app = QApplication([])
  wizard = ConfigWizard()  # (1)!
  wizard.show()
  app.exec()
  ```

  1. Pass `config_file="MyScope.cfg"` to start from an existing file. Like most widgets, it uses `CMMCorePlus.instance()` unless you pass a core (here, the argument is called `core=`).
- In Micro-Manager itself: **Devices \> Hardware Configuration Wizard...**. If `mmcore install` downloaded a full Micro-Manager for you (on Windows and Intel Macs), `mmcore mmstudio` will start it.

## Getting the device adapters

On Windows and Intel Macs, `mmcore install` downloads a complete Micro-Manager nightly build, which includes the device adapters for most supported hardware. On Apple Silicon Macs and on Linux, it currently downloads only the test adapters (`DemoCamera`, `Utilities` and a few others), so for real hardware on those platforms you'll need to build the adapters you need from [source](<https://github.com/micro-manager/mmCoreAndDevices>).

If you already have Micro-Manager installed (with the adapters you need), `pymmcore-plus` can use it, as long as its *device interface version* matches the one your `pymmcore` expects. `mmcore list` shows the installations it found (and which of them are compatible), and `mmcore use <path>` picks one. See [Micro-Manager device adapters](<https://pymmcore-plus.github.io/pymmcore-plus/install/index.md>) for more on all of this.

Some devices also need the manufacturer's own drivers or SDK installed (many cameras do, for example). Micro-Manager's [device support pages](<https://micro-manager.org/Device_Support>) say what each adapter needs.

## Loading it

In Python, pass the path to `loadSystemConfiguration`:

```python
from pymmcore_plus import CMMCorePlus

core = CMMCorePlus()
core.loadSystemConfiguration("path/to/MyScope.cfg")  # (1)!
```

1. Relative paths are looked for in the current directory first, then in the device adapter folder.

Both applications can load a configuration at startup:

```sh
mmgui -c path/to/MyScope.cfg                # pymmcore-gui
napari-micromanager -c path/to/MyScope.cfg  # napari-micromanager
```

... and `mmcore bench -c path/to/MyScope.cfg` times a few basic operations on each of your devices, which is a quick way to check that they load.

If loading fails, the error message usually names the device that couldn't be initialized. `mmcore logs` shows the end of the log file (which has more detail), and [Troubleshooting](<https://pymmcore-plus.github.io/pymmcore-plus/troubleshooting/index.md>) covers the most common problems.

If you change the configuration from Python (for example, by defining new presets), `core.saveSystemConfiguration("MyScope.cfg")` writes it back out.

## Groups, channels and pixel sizes

Once the devices are loaded, most day-to-day settings live in configuration groups and their presets (see [Configuration groups](<https://pymmcore-plus.github.io/pymmcore-plus/guides/configuration/index.md>)). When you list `channels` in an `MDASequence`, they're looked up in a group named `Channel` by default. If your channel group has a different name, say so:

```python
import useq

useq.MDASequence(channels=[{"config": "DAPI", "group": "Filters"}])
```

Pixel sizes are stored in the configuration file too, as presets tied to your objectives, and the core picks the right one as the objective changes. With the demo configuration:

```python
core.getAvailablePixelSizeConfigs()  # ('Res10x', 'Res20x', 'Res40x')
core.setConfig("Objective", "20X")
core.getPixelSizeUm()                # 0.5
```

You can set these up with the `PixelConfigurationWidget` (in pymmcore-gui, **Window \> Pixel Size Configuration**), and then save the configuration.
