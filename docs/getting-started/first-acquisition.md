---
title: Your First Acquisition
---

# Your First Acquisition

A multi-dimensional acquisition (MDA) is a series of images collected across time
points, stage positions, channels, z-planes, etc...  In pymmcore-plus, the
experiment is *described* with [useq-schema](../useq-schema/index.md) and *run* by
the [acquisition engine](../pymmcore-plus/guides/mda_engine.md).

We'll need a core with a configuration loaded:

```python
from pymmcore_plus import CMMCorePlus

core = CMMCorePlus()
core.loadSystemConfiguration()
```

## Describing the experiment

An [`MDASequence`][useq.MDASequence] declares what to acquire.  It doesn't know
anything about your hardware (beyond the names of things like channel presets),
and can be saved to (and loaded from) JSON or YAML.

```python
import useq

x, y = core.getXYPosition()
z = core.getZPosition()

sequence = useq.MDASequence(
    channels=["DAPI", {"config": "FITC", "exposure": 50}],  # (1)!
    time_plan={"interval": 0.5, "loops": 3},  # (2)!
    z_plan={"range": 4, "step": 1},  # (3)!
    stage_positions=[(x, y, z), (x + 100, y, z)],  # (4)!
    axis_order="tpcz",  # (5)!
)

sequence.sizes       # {'t': 3, 'p': 2, 'c': 2, 'z': 5}
len(list(sequence))  # 60 events
```

1.  Channels are presets in the `Channel` configuration group (the default
    group), with an optional exposure in milliseconds.
2.  3 time points, 0.5 seconds apart.
3.  A 4 µm z-stack in 1 µm steps, centered on the `z` of each stage position.
4.  Two `(x, y, z)` stage positions, in µm: the current position, and one
    100 µm away in x.  These are absolute stage coordinates, so on a real
    microscope, make sure they're somewhere safe!
5.  The nesting order, outermost first: for each **t**ime point, visit each
    **p**osition, and there, for each **c**hannel, take a **z**-stack.

!!! warning "Where is the z-stack?"

    A z-stack described with `range` (or `above` and `below`) is *relative* to the
    `z` of each stage position.  If a position has no `z`, or the sequence has no
    stage positions at all, it is currently relative to z = 0, *not* to wherever
    your focus is.  On a real microscope that could drive the objective a long
    way, which is why we pass the current `z` explicitly above.

Iterating over the sequence yields one [`MDAEvent`][useq.MDAEvent] per image, each
describing what the hardware should do for that image (any field that is left
unset means "leave it as it is").  See the
[`MDASequence` reference](../useq-schema/schema/sequence.md) for more of what a
sequence can express (grids, well plates, autofocus, per-position sub-sequences,
etc...).

## Running it

```python
@core.mda.events.frameReady.connect  # (1)!
def on_frame(image, event, metadata):
    print(event.index, image.shape)

core.mda.run(sequence, output="experiment.ome.zarr", overwrite=True)  # (2)!
```

1.  Connect to [events][pymmcore_plus.mda.events.PMDASignaler] to process data
    as it arrives.  `frameReady` is called with the image (a numpy array), the
    `MDAEvent` and a dict of metadata.
2.  `mda.run` blocks until the acquisition is done.  (Use
    [`core.run_mda(sequence)`][pymmcore_plus.CMMCorePlus.run_mda] to run it on a
    background thread instead.)  `overwrite=True` replaces `experiment.ome.zarr`
    if it already exists; without it, running the script a second time raises a
    `FileExistsError`.

... prints a line for each of the 60 images:

```
{'t': 0, 'p': 0, 'c': 0, 'z': 0} (512, 512)
{'t': 0, 'p': 0, 'c': 0, 'z': 1} (512, 512)
{'t': 0, 'p': 0, 'c': 0, 'z': 2} (512, 512)
...
{'t': 2, 'p': 1, 'c': 1, 'z': 4} (512, 512)
```

## Where did the data go?

The `output` argument writes the images to disk as they arrive, and the extension
picks the format.  An `.ome.zarr` "file" is actually a folder.  Each stage position
is stored as a separate image inside it (`experiment.ome.zarr/0`,
`experiment.ome.zarr/1`), as an array with dimensions `(t, c, z, y, x)`.  You can
read it back with [zarr](https://zarr.readthedocs.io) (`pip install zarr`):

```python
import zarr

data = zarr.open_array("experiment.ome.zarr/0/0", mode="r")
data.shape  # (3, 2, 5, 512, 512)
```

If you'd rather have files that you can drag into Fiji, use
`output="experiment.ome.tiff"` (this needs the `io` extra:
`pip install "pymmcore-plus[io]"`).  With more than one stage position, you get one
file per position, in a folder named after your output
(`experiment/experiment_p000.ome.tiff`, `experiment/experiment_p001.ome.tiff`).

See [Saving data](../pymmcore-plus/guides/saving_data.md) for more on formats and
options.

## Beyond sequences

`MDASequence` is just one way to make events.  The engine will run *any* iterable
of `MDAEvent` objects, so a plain list works too:

```python
events = [
    useq.MDAEvent(channel="DAPI", exposure=10),
    useq.MDAEvent(channel="FITC", x_pos=x + 50, y_pos=y),
]
core.mda.run(events)
```

The iterable needn't even be of known length.  A generator or a
[`Queue`][queue.Queue] can decide on the next event based on previous images (see
[Event-driven acquisition](../pymmcore-plus/guides/event_driven_acquisition.md)).

## Next steps

[The acquisition engine](../pymmcore-plus/guides/mda_engine.md) covers running
acquisitions in more depth (pausing and cancelling, hardware triggering, etc...),
and [Building sequences](../useq-schema/guides/sequences.md) shows more of what
you can describe with an `MDASequence`.  When you're ready for a graphical
interface, have a look at [your first GUI](first-gui.md).
