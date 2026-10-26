---
title: Your first acquisition
---

# Your first acquisition

A *multi-dimensional acquisition* (MDA) is a series of images collected across
time points, stage positions, channels, z-planes, and so on.  It takes two
pieces:

- [**useq-schema**](../useq-schema/index.md) to **describe** the experiment, and
- the [**pymmcore-plus** acquisition engine](../pymmcore-plus/guides/mda_engine.md)
  to **run** it.

## Describe the experiment

An [`MDASequence`][useq.MDASequence] declares what to acquire.  It is plain data:
you can save it as JSON or YAML, and it knows nothing about hardware.

```python
import useq

sequence = useq.MDASequence(
    channels=["DAPI", {"config": "FITC", "exposure": 50}],  # (1)!
    time_plan={"interval": 0.5, "loops": 3},                 # (2)!
    z_plan={"range": 4, "step": 1},                          # (3)!
    stage_positions=[(0, 0, 0), (100, 100, 0)],              # (4)!
    axis_order="tpcz",                                       # (5)!
)

sequence.sizes        # {'t': 3, 'p': 2, 'c': 2, 'z': 5}
len(list(sequence))   # 60 events
```

1.  Channels are configuration presets in the `Channel` group (the default
    group), with an optional exposure.
2.  3 time points, 0.5 s apart.
3.  A 4 µm z-stack around the current position, in 1 µm steps.
4.  Two `(x, y, z)` stage positions.
5.  The nesting order: for each **t**ime point, visit each **p**osition, image each
    **c**hannel, then each **z** plane.

Iterating the sequence yields [`MDAEvent`][useq.MDAEvent] objects &mdash; one per
image &mdash; each saying exactly what the hardware should do.  See
the [`MDASequence` reference](../useq-schema/schema/sequence.md) for everything a
sequence can express (grids, well plates, autofocus, per-position
sub-sequences, ...).

## Run it

```python
from pymmcore_plus import CMMCorePlus

core = CMMCorePlus()
core.loadSystemConfiguration()

@core.mda.events.frameReady.connect  # (1)!
def on_frame(image, event, metadata):
    print(event.index, image.shape)

core.mda.run(sequence, output="experiment.ome.zarr")  # (2)!
```

1.  Connect to [events][pymmcore_plus.mda.events.PMDASignaler] to process data
    as it arrives.
2.  `mda.run` blocks until the acquisition is done.  Use
    [`core.run_mda(sequence)`][pymmcore_plus.CMMCorePlus.run_mda] to run on a
    background thread instead.

The `output` argument saves to OME-Zarr (or `.ome.tiff`) using
[ome-writers](https://pymmcore-plus.github.io/ome-writers/); install it with
`pip install "pymmcore-plus[io]"`.

## Beyond sequences

The engine accepts **any iterable of `MDAEvent`s**, not just an
`MDASequence`.  That makes it easy to run adaptive, "smart" microscopy where
each event is decided based on previous images:

```python
from queue import Queue

events = Queue()
STOP = object()
core.run_mda(iter(events.get, STOP))  # runs until STOP is put in the queue

events.put(useq.MDAEvent(channel="DAPI", exposure=10))
events.put(useq.MDAEvent(x_pos=100, y_pos=200, channel="FITC"))
events.put(STOP)
```

## Where next?

- [The acquisition engine](../pymmcore-plus/guides/mda_engine.md): everything about
  running MDAs: pausing, cancelling, hardware triggering, serialization.
- [Event-driven acquisition](../pymmcore-plus/guides/event_driven_acquisition.md)
  and [custom acquisition engines](../pymmcore-plus/guides/custom_engine.md).
- [Your first GUI](first-gui.md): run the same experiments from a graphical
  interface.
