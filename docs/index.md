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

# pymmcore-plus

These docs cover `pymmcore-plus` and the packages built around it, which let you
control a microscope from Python by talking directly to
[Micro-Manager](https://micro-manager.org)'s C++ core and device adapters (with no
Java process involved).  You can use them to script your hardware and run
multi-dimensional acquisitions, or to build your own GUI (or just use one of
ours).

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

If you're new here, [Getting Started](getting-started/which-package.md) walks you through
installing things, controlling Micro-Manager's demo devices from Python, running a
first acquisition, and putting together a small GUI (no microscope required).  If
you already know Micro-Manager, have a look at
[Coming from Micro-Manager](getting-started/from-micro-manager.md), which maps what
you know onto these packages.

If you'd rather not write any code, [pymmcore-gui](pymmcore-gui/index.md) is our
(work in progress) desktop application, and
[napari-micromanager](napari-micromanager/index.md) controls a microscope from
inside [napari](https://napari.org).

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
<div class="pymm-layer__pkgs" markdown>[**pymmcore-plus**](pymmcore-plus/index.md) &middot; [**useq-schema**](useq-schema/index.md)</div>
<div class="pymm-layer__desc">The core, extended with events and an acquisition engine, and a schema for describing experiments.</div>
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

## Getting help

If you have usage questions (*"How do I...?"*), please ask on the
[image.sc forum](https://forum.image.sc/tag/pymmcore-plus) with the `pymmcore-plus`
tag, or come chat with us on
[Zulip](https://imagesc.zulipchat.com/#narrow/channel/442785-pymmcore.5B-plus.5D).
Bug reports and feature requests are always welcome on
[GitHub](https://github.com/pymmcore-plus) (each package has its own repository;
see [Contributing](contributing/index.md) if you're not sure which one).
