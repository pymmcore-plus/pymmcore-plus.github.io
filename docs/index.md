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

A set of Python packages for running a microscope through
[Micro-Manager](https://micro-manager.org)'s C++ core and device adapters, with no
Java process involved.  Script your hardware, run multi-dimensional acquisitions,
build your own GUI, or just use one of ours.

[Get started](getting-started/which-package.md){ .md-button .md-button--primary }
[User guide](guide/index.md){ .md-button }

</div>

<div class="pymm-hero__code" markdown>

```python
import useq
from pymmcore_plus import CMMCorePlus

core = CMMCorePlus()
core.loadSystemConfiguration()  # demo devices

sequence = useq.MDASequence(
    channels=["DAPI", "FITC"],
    time_plan={"interval": 1, "loops": 5},
)
core.mda.run(sequence, output="data.ome.zarr")
```

</div>

</div>

## Where to start

<div class="grid cards pymm-tasks" markdown>

-   :lucide-terminal:{ .lg .middle } **Script a microscope**

    ---

    Load a configuration, move stages, snap images, and connect callbacks to
    changes in the core, from a script or a notebook.

    [:octicons-arrow-right-24: First steps](getting-started/first-steps.md)

-   :lucide-layers:{ .lg .middle } **Run acquisitions**

    ---

    Describe time-lapses, z-stacks, channels and positions with `useq`, run them
    with an acquisition engine you can customize, and save to OME-Zarr or
    OME-TIFF.

    [:octicons-arrow-right-24: Your first acquisition](getting-started/first-acquisition.md)

-   :lucide-app-window:{ .lg .middle } **Build a GUI**

    ---

    Combine Qt widgets (property browsers, stage controls, MDA editors, image
    previews, etc...) into your own application.

    [:octicons-arrow-right-24: Your first GUI](getting-started/first-gui.md)

-   :lucide-microscope:{ .lg .middle } **Just use an app**

    ---

    Point-and-click microscope control with `pymmcore-gui`, or inside napari
    with `napari-micromanager`.

    [:octicons-arrow-right-24: Applications](pymmcore-gui/index.md)

</div>

[Getting Started](getting-started/which-package.md) goes through these in order,
using Micro-Manager's demo devices (no microscope required).  If you already know
Micro-Manager, [Coming from Micro-Manager](getting-started/from-micro-manager.md)
maps what you know onto these packages.

## How the pieces fit together

Each package builds on the ones below it.  You only need to go as far up the stack
as you want (`pymmcore-plus` on its own is enough to script a microscope).

<div class="pymm-stack" markdown>

<div class="pymm-layer pymm-layer--apps" markdown>
<div class="pymm-layer__label">Applications</div>
<div class="pymm-layer__pkgs" markdown>[**pymmcore-gui**](pymmcore-gui/index.md) &middot; [**napari-micromanager**](napari-micromanager/index.md)</div>
<div class="pymm-layer__desc">Desktop applications for running a microscope.</div>
</div>

<div class="pymm-layer pymm-layer--widgets" markdown>
<div class="pymm-layer__label">Widgets</div>
<div class="pymm-layer__pkgs" markdown>[**pymmcore-widgets**](pymmcore-widgets/widgets/index.md)</div>
<div class="pymm-layer__desc">Qt widgets for devices, properties, configurations and acquisitions.</div>
</div>

<div class="pymm-layer pymm-layer--core" markdown>
<div class="pymm-layer__label">Control &amp; acquisition</div>
<div class="pymm-layer__pkgs" markdown>[**pymmcore-plus**](pymmcore-plus/index.md) &middot; [**useq-schema**](useq-schema/index.md) &middot; [**ome-writers**](https://pymmcore-plus.github.io/ome-writers/)</div>
<div class="pymm-layer__desc">The core, extended with events and an acquisition engine, a schema for describing experiments, and writers for OME-Zarr and OME-TIFF.</div>
</div>

<div class="pymm-layer pymm-layer--mm" markdown>
<div class="pymm-layer__label">Micro-Manager</div>
<div class="pymm-layer__pkgs" markdown>[**pymmcore**](https://github.com/micro-manager/pymmcore) &middot; [device adapters](pymmcore-plus/install.md)</div>
<div class="pymm-layer__desc">The C++ core and drivers for hundreds of cameras, stages, shutters, lasers, etc...</div>
</div>

<div class="pymm-layer pymm-layer--hw" markdown>
<div class="pymm-layer__label">Your microscope</div>
<div class="pymm-layer__pkgs" markdown>:lucide-microscope: &nbsp; Micro-Manager's demo devices, or your own hardware</div>
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
