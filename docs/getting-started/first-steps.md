---
title: First steps
---

# First steps: scripting the core

Everything starts with [`CMMCorePlus`][pymmcore_plus.CMMCorePlus], a drop-in
replacement for Micro-Manager's `CMMCore` with a more Pythonic API.  If you have
used Micro-Manager's Java API or `pymmcore`, everything you know still applies.

!!! info "Before you start"

    [Install](install.md) `pymmcore-plus` and the device adapters.  These examples
    use Micro-Manager's **demo configuration**, so no hardware is needed.

## Load a configuration

```python
from pymmcore_plus import CMMCorePlus

core = CMMCorePlus()
core.loadSystemConfiguration()  # (1)!

print(core.getLoadedDevices())
# ('DHub', 'Camera', 'Dichroic', 'Emission', 'Excitation', 'Objective', 'Z', ...)
```

1.  With no argument, this loads the demo configuration (`MMConfig_demo.cfg`).
    Pass the path to your own `.cfg` file to use your hardware.

## Snap an image

```python
core.setExposure(25)
image = core.snap()  # (1)!
print(image.shape, image.dtype)  # (512, 512) uint16
```

1.  [`snap`][pymmcore_plus.CMMCorePlus.snap] is a `CMMCorePlus` convenience that
    calls `snapImage()` and returns `getImage()` as a numpy array.

## Read and set properties

Every device exposes **properties**.  You can use the classic string-based API:

```python
core.getProperty("Camera", "Binning")      # '1'
core.setProperty("Camera", "Binning", "2")
core.getImageWidth()                       # 256
```

...or the object-oriented [`Device`][pymmcore_plus.Device] and
[`DeviceProperty`][pymmcore_plus.DeviceProperty] views:

```python
camera = core.getDeviceObject("Camera")
gain = camera.getPropertyObject("Gain")
gain.value = 1
gain.range()  # (-5.0, 8.0)
```

See [Devices & properties](../pymmcore-plus/guides/devices.md) for more.

## Use configuration groups

Configuration groups (or *presets*) bundle many property settings under one
name, such as an imaging channel:

```python
core.getAvailableConfigs("Channel")   # ('Cy5', 'DAPI', 'FITC', 'Rhodamine')
core.setConfig("Channel", "FITC")
core.getCurrentConfig("Channel")      # 'FITC'
```

## Move stages

```python
core.setXYPosition(100, 200)
core.setZPosition(10)
core.waitForSystem()
core.getXYPosition()  # [100.005, 199.995]
```

## React to changes

`CMMCorePlus` emits [events](../pymmcore-plus/guides/events.md) whenever the
state of the microscope changes, so your code (or a GUI) can stay in sync:

```python
@core.events.propertyChanged.connect
def on_change(device: str, prop: str, value: str) -> None:
    print(f"{device}.{prop} changed to {value}")

core.setProperty("Camera", "Gain", "2")  # prints "Camera.Gain changed to 2"
```

## Where next?

- Every method of the core, with what `pymmcore-plus` adds or changes, is listed
  in the [`CMMCorePlus` reference][pymmcore_plus.CMMCorePlus].
- [Your first acquisition](first-acquisition.md): run multi-dimensional
  experiments.
- The [User Guide](../guide/index.md) covers each topic in depth.
