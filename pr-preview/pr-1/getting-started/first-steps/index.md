# First Steps

At the heart of Micro-Manager is its *core* (`CMMCore`): a C++ library that loads your hardware configuration, talks to each device through its device adapter, and hands you images. Micro-Manager's Java application (MMStudio) is built on top of it, and [`pymmcore`](<https://github.com/micro-manager/pymmcore>) makes it available in Python.

The main object in `pymmcore-plus` is `CMMCorePlus`, an enhanced subclass of `pymmcore.CMMCore`. It aims to be a drop-in replacement, so if you've used `pymmcore` (or the `mmc` object in Micro-Manager's script panel), the methods you know are all still there. `CMMCorePlus` adds a number of things on top, and we'll look at a few of them here.

These examples use Micro-Manager's demo devices, so you don't need any hardware. You can paste them into a Python session (`python`, `ipython` or a Jupyter notebook) started in the environment where you [installed](<https://pymmcore-plus.github.io/getting-started/install/index.md>) `pymmcore-plus`, or put them in a script.

> [!WARNING]
>
> **Is Micro-Manager open?**
>
> `CMMCorePlus` doesn't connect to a running copy of Micro-Manager; it opens the devices itself. Most hardware can only be opened by one program at a time, so close Micro-Manager (MMStudio) before you load the same configuration here. (The demo devices don't mind.) See [Coming from Micro-Manager](<https://pymmcore-plus.github.io/getting-started/from-micro-manager/index.md>) for more.

## Loading a configuration

```python
from pymmcore_plus import CMMCorePlus

core = CMMCorePlus()
core.loadSystemConfiguration()  # (1)!

print(core.getLoadedDevices())
# ('DHub', 'Camera', 'Dichroic', 'Emission', 'Excitation', 'Objective', 'Z', ...)
```

1. With no argument, this loads the demo configuration (`MMConfig_demo.cfg`). Pass the path to your own `.cfg` file to use your hardware (see [Using your own microscope](<https://pymmcore-plus.github.io/guide/own-microscope/index.md>)).

## Snapping an image

```python
core.setExposure(25)  # milliseconds
image = core.snap()  # (1)!
print(image.shape, image.dtype)  # (512, 512) uint16
```

1. `snap` is a `CMMCorePlus` convenience that calls `snapImage()` and returns `getImage()` as a numpy array.

`image` is just a numpy array, so you can look at it or save it with whatever tools you like. For example, to save it as a TIFF (that you can open in Fiji), use [tifffile](<https://github.com/cgohlke/tifffile>), which comes with the `io` extra (or `pip install tifffile`):

```python
import tifffile

tifffile.imwrite("snap.tif", image)
```

(In a Jupyter notebook, `matplotlib.pyplot.imshow(image)` is a quick way to have a look at it.)

## Reading and setting properties

Each device has a number of *properties*. You can use the classic string-based API:

```python
core.getProperty("Camera", "Binning")      # '1'
core.setProperty("Camera", "Binning", "2")
core.getImageWidth()                       # 256
```

...or the object-oriented `Device` and `DeviceProperty` views:

```python
camera = core.getDeviceObject("Camera")
gain = camera.getPropertyObject("Gain")
gain.value = 1
gain.range()  # (-5.0, 8.0)
```

See [Devices &amp; properties](<https://pymmcore-plus.github.io/pymmcore-plus/guides/devices/index.md>) for more.

## Configuration groups and presets

A *configuration group* (such as "Channel") holds a number of *presets* (such as "DAPI" or "FITC"), each of which sets several properties at once. These are the same groups and presets you'd see in Micro-Manager's main window:

```python
core.getAvailableConfigs("Channel")   # ('Cy5', 'DAPI', 'FITC', 'Rhodamine')
core.setConfig("Channel", "FITC")
core.getCurrentConfig("Channel")      # 'FITC'
```

See [Configuration groups](<https://pymmcore-plus.github.io/pymmcore-plus/guides/configuration/index.md>) for more.

## Moving stages

Positions are in microns:

```python
core.setXYPosition(100, 200)
core.setZPosition(10)
core.waitForSystem()  # (1)!
core.getXYPosition()  # [100.005, 199.995]
```

1. Stage movements may return before the hardware has finished moving. `waitForSystem` blocks until all devices are done.

## Connecting to events

`CMMCorePlus` emits [events](<https://pymmcore-plus.github.io/pymmcore-plus/guides/events/index.md>) as the state of the microscope changes, and you can connect your own callbacks to them. (This is how the widgets in `pymmcore-widgets` stay in sync with the core.)

```python
@core.events.propertyChanged.connect  # (1)!
def on_change(device: str, prop: str, value: str) -> None:
    print(f"{device}.{prop} changed to {value}")

core.setProperty("Camera", "Gain", "2")  # prints "Camera.Gain changed to 2"
```

1. Using `connect` as a decorator registers the function below it as a callback. `core.events.propertyChanged.connect(on_change)` does the same thing.

> [!TIP]
>
> **`CMMCorePlus.instance`**
>
> Creating/accessing a `CMMCorePlus` object using `CMMCorePlus.instance()` is a convenient way to access the same core instance from multiple places in your code. The widgets in [`pymmcore-widgets`](<https://pymmcore-plus.github.io/pymmcore-widgets/widgets/index.md>) also use `CMMCorePlus.instance()` by default, so any widgets you use will automatically connect to the same core instance without any additional configuration.
>
> Attempts *are* made to make it thread-safe. But please open an issue if you find any problems.

## Next steps

From here, you'll probably want to run [your first acquisition](<https://pymmcore-plus.github.io/getting-started/first-acquisition/index.md>). When you're ready to use a real microscope, see [Using your own microscope](<https://pymmcore-plus.github.io/guide/own-microscope/index.md>). The [User Guide](<https://pymmcore-plus.github.io/guide/index.md>) covers each topic in more depth, and the `CMMCorePlus` reference lists all of the core's methods, marking what `pymmcore-plus` adds or changes.
