# Scripting napari-micromanager

`napari-micromanager` creates and owns its own `CMMCorePlus`. (It deliberately does *not* use the global `CMMCorePlus.instance()`, so a core you configured with `CMMCorePlus.instance()` is not the one the plugin drives.) Once you have a reference to the plugin's core, anything you can do with [pymmcore-plus](<https://pymmcore-plus.github.io/pymmcore-plus/index.md>) can be combined with the GUI. There are a few ways to get it:

- `main_window.core`, where `main_window` is the plugin's `MainWindow` (see the script below);
- `napari_micromanager.get_core()`, which finds the plugin in the current napari viewer;
- in napari's console, the variable `mmcore` (see below).

## Launching napari from a script

For complex scripting you will likely want to launch napari from a script or a Jupyter notebook:

examples/launch\_from\_script.py

```python
import napari

v = napari.Viewer()
dw, main_window = v.window.add_plugin_dock_widget("napari-micromanager")

# the CMMCorePlus instance that napari-micromanager is driving
mmc = main_window.core

# do any complicated scripting you want here
...

# start napari
napari.run()
```

## Using a core you created

To have the plugin drive a core that you created and configured yourself, pass it as `mmcore` when you create the `MainWindow`, and add that to the viewer:

```python
import napari
from napari_micromanager import MainWindow
from pymmcore_plus import CMMCorePlus

core = CMMCorePlus()
core.loadSystemConfiguration()  # or your own configuration file

viewer = napari.Viewer()
main_window = MainWindow(viewer, mmcore=core)
viewer.window.add_dock_widget(main_window, name="MicroManager", area="top")

napari.run()
```

The plugin then leaves the core's lifecycle to you. When the window closes, it doesn't cancel a running acquisition or unload the devices, as it does for a core it created itself.

## Using the integrated napari console

After launching napari and starting the `napari-micromanager` plugin, open the napari console (the `>_` button at the bottom left of the window). It already defines `mmcore`, the core the plugin is driving, along with `MDASequence` and `MDAEvent` from [useq](<https://pymmcore-plus.github.io/useq-schema/index.md>), so you can run an acquisition from there:

```python
mmcore.run_mda(MDASequence(time_plan={"interval": 1, "loops": 5}))
```
