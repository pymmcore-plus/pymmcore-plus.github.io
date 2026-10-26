---
title: Home
description: Control microscopes with Python, using Micro-Manager's device adapters.
hide:
  - navigation
  - toc
  - path
---

<div class="pymm-hero" markdown>

<div class="pymm-hero__text" markdown>

# Control microscopes with Python

**pymmcore-plus** and friends give you pure-Python access to the hundreds of
devices supported by [Micro-Manager](https://micro-manager.org): script your
hardware, describe and run multi-dimensional experiments, and build (or simply
use) graphical interfaces &mdash; no Java required.

[Get started](getting-started/index.md){ .md-button .md-button--primary }
[User guide](guide/index.md){ .md-button }

</div>

<div class="pymm-hero__code" markdown>

```python
import useq
from pymmcore_plus import CMMCorePlus

core = CMMCorePlus()
core.loadSystemConfiguration()  # demo devices

experiment = useq.MDASequence(
    channels=["DAPI", "FITC"],
    z_plan={"range": 4, "step": 0.5},
    time_plan={"interval": 2, "loops": 10},
)
core.mda.run(experiment, output="data.ome.zarr")
```

</div>

</div>

## What would you like to do?

<div class="grid cards" markdown>

-   :lucide-terminal:{ .lg .middle } **Script a microscope**

    ---

    Load a configuration, move stages, snap images, and react to every change
    from Python or Jupyter.

    [:octicons-arrow-right-24: First steps](getting-started/first-steps.md)

-   :lucide-layers:{ .lg .middle } **Run acquisitions**

    ---

    Describe time-lapses, z-stacks, channels and positions with `useq`, run them
    with a hackable acquisition engine, and save to OME-Zarr or OME-TIFF.

    [:octicons-arrow-right-24: Your first acquisition](getting-started/first-acquisition.md)

-   :lucide-app-window:{ .lg .middle } **Build a GUI**

    ---

    Compose ready-made Qt widgets &mdash; property browsers, stage controls,
    MDA editors, image previews &mdash; into your own application.

    [:octicons-arrow-right-24: Your first GUI](getting-started/first-gui.md)

-   :lucide-microscope:{ .lg .middle } **Just use an app**

    ---

    Point-and-click microscope control with `pymmcore-gui`, or inside napari
    with `napari-micromanager`.

    [:octicons-arrow-right-24: Applications](pymmcore-gui/index.md)

</div>

## How the pieces fit together

Each layer builds on the ones below it, and every layer is usable on its own.
Click a package to learn more.

<div class="pymm-stack" markdown>

<div class="pymm-layer pymm-layer--apps" markdown>
<div class="pymm-layer__label">Applications</div>
<div class="pymm-layer__pkgs" markdown>[**pymmcore-gui**](pymmcore-gui/index.md) &middot; [**napari-micromanager**](napari-micromanager/index.md)</div>
<div class="pymm-layer__desc">Complete microscope control applications.</div>
</div>

<div class="pymm-layer pymm-layer--widgets" markdown>
<div class="pymm-layer__label">Widgets</div>
<div class="pymm-layer__pkgs" markdown>[**pymmcore-widgets**](pymmcore-widgets/widgets/index.md)</div>
<div class="pymm-layer__desc">Qt widgets for devices, properties, configurations and acquisitions.</div>
</div>

<div class="pymm-layer pymm-layer--core" markdown>
<div class="pymm-layer__label">Control &amp; acquisition</div>
<div class="pymm-layer__pkgs" markdown>[**pymmcore-plus**](pymmcore-plus/index.md) &middot; [**useq-schema**](useq-schema/index.md)</div>
<div class="pymm-layer__desc">A Pythonic core with events, an acquisition engine, and a hardware-agnostic schema for experiments.</div>
</div>

<div class="pymm-layer pymm-layer--mm" markdown>
<div class="pymm-layer__label">Micro-Manager</div>
<div class="pymm-layer__pkgs" markdown>[**pymmcore**](https://github.com/micro-manager/pymmcore) &middot; [device adapters](pymmcore-plus/install.md)</div>
<div class="pymm-layer__desc">The C++ core and drivers for hundreds of cameras, stages, shutters, lasers&hellip;</div>
</div>

<div class="pymm-layer pymm-layer--hw" markdown>
<div class="pymm-layer__label">Your microscope</div>
<div class="pymm-layer__pkgs" markdown>:lucide-microscope: &nbsp; (or the built-in demo devices &mdash; no hardware needed)</div>
</div>

</div>

## Community

<div class="grid cards" markdown>

-   :fontawesome-brands-discourse: **Ask a question** on the
    [image.sc forum](https://forum.image.sc/tag/pymmcore-plus)

-   :simple-zulip: **Chat with developers** on
    [Zulip](https://imagesc.zulipchat.com/#narrow/channel/442785-pymmcore.5B-plus.5D)

-   :fontawesome-brands-github: **Report a bug or request a feature** on
    [GitHub](https://github.com/pymmcore-plus)

</div>
