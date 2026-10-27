---
title: User Guide
---

# User Guide

The User Guide is organized by topic, roughly following the stack from the
hardware up.  Each page belongs to one package's docs (the badge at the top says
which), and names of classes and functions link to the
[API reference](../api/index.md).  If you're new here,
[Getting Started](../getting-started/which-package.md) is probably a better place to begin.

<div class="grid cards" markdown>

-   :lucide-sliders-horizontal:{ .lg .middle } **Controlling hardware**

    ---

    [Installing device adapters](../pymmcore-plus/install.md),
    [using your own microscope](own-microscope.md),
    [devices and properties](../pymmcore-plus/guides/devices.md),
    [configuration groups](../pymmcore-plus/guides/configuration.md), and
    [events and callbacks](../pymmcore-plus/guides/events.md) (which are how GUIs,
    and your own code, stay in sync with the core).

-   :lucide-list-tree:{ .lg .middle } **Describing experiments**

    ---

    How [useq-schema](../useq-schema/index.md) describes an acquisition as a
    sequence of events, and
    [building sequences](../useq-schema/guides/sequences.md) with time points,
    z-stacks, channels, positions, grids, etc...

-   :lucide-play:{ .lg .middle } **Running acquisitions**

    ---

    [The acquisition engine](../pymmcore-plus/guides/mda_engine.md),
    [saving data](../pymmcore-plus/guides/saving_data.md),
    [event-driven acquisition](../pymmcore-plus/guides/event_driven_acquisition.md),
    and [writing your own engine](../pymmcore-plus/guides/custom_engine.md).

-   :lucide-app-window:{ .lg .middle } **Building GUIs**

    ---

    The [widget gallery](../pymmcore-widgets/widgets/index.md),
    [building a custom GUI](../pymmcore-widgets/getting_started.md) from those
    widgets, and
    [keeping it responsive](../pymmcore-plus/examples/integration-with-qt.md).

-   :lucide-microscope:{ .lg .middle } **Applications**

    ---

    [pymmcore-gui](../pymmcore-gui/index.md), our desktop application, and
    [napari-micromanager](../napari-micromanager/index.md), which controls a
    microscope from inside napari.

-   :lucide-cpu:{ .lg .middle } **Advanced topics**

    ---

    [Device adapters written in Python](../pymmcore-plus/guides/unicore.md)
    (`UniMMCore`), a preview of [useq-schema v2](../useq-schema/v2-migration.md),
    and a [Pycro-Manager-style API](../pymmcore-plus/examples/pycro-manager-api.md).

</div>

!!! question "Something not working?"

    The troubleshooting pages cover
    [the core and device adapters](../pymmcore-plus/troubleshooting.md) and
    [Qt and widgets](../pymmcore-widgets/troubleshooting.md).  Turning up the
    [logging](../pymmcore-plus/guides/logging.md) (or
    [profiling](../pymmcore-plus/profiling.md), if things are slow) can also help
    you work out what's going on.  If you're still stuck, please ask on the
    [image.sc forum](https://forum.image.sc/tag/pymmcore-plus).
