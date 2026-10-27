---
title: API Reference
---

# API Reference

These pages are generated from the docstrings of each package.  Each object is
documented once, under the shortest path you can import it from (e.g.
`pymmcore_plus.CMMCorePlus`, not `pymmcore_plus.core.CMMCorePlus`).  Other modules
that re-export it just link there.

<div class="grid cards" markdown>

-   **[pymmcore-plus](../pymmcore-plus/index.md)**

    ---

    [`CMMCorePlus`][pymmcore_plus.CMMCorePlus] (all of the core's methods,
    marking what pymmcore-plus adds or changes), the
    [acquisition engine][pymmcore_plus.mda], device objects, constants, metadata,
    and the [`mmcore` command line tool](../pymmcore-plus/cli.md).

-   **[useq-schema](../useq-schema/schema/sequence.md)**

    ---

    [`MDASequence`][useq.MDASequence], [`MDAEvent`][useq.MDAEvent], and the
    plans for each axis (time, z, positions, grids, autofocus).

-   **[pymmcore-widgets](../pymmcore-widgets/api/pymmcore_widgets/index.md)**

    ---

    One page for each widget, with a screenshot and an example.  (The
    [widget gallery](../pymmcore-widgets/widgets/index.md) is a quicker way to
    browse them.)

-   **[pymmcore-gui](../pymmcore-gui/api/pymmcore_gui/index.md)**

    ---

    The application's entry points ([`create_mmgui`][pymmcore_gui.create_mmgui])
    and the actions and widgets you can use to extend it.

</div>

napari-micromanager has no public Python API of its own, but you can drive it from
a script (see [Scripting napari-micromanager](../napari-micromanager/scripting.md)).

Release notes for each package are on GitHub:
[pymmcore-plus](https://github.com/pymmcore-plus/pymmcore-plus/releases),
[useq-schema](https://github.com/pymmcore-plus/useq-schema/releases),
[pymmcore-widgets](https://github.com/pymmcore-plus/pymmcore-widgets/releases),
[napari-micromanager](https://github.com/pymmcore-plus/napari-micromanager/releases).

!!! tip "Linking to these docs from your own project"

    Each package publishes an object inventory for
    [mkdocstrings](https://mkdocstrings.github.io/) and
    [intersphinx](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html),
    e.g. `https://pymmcore-plus.github.io/pymmcore-plus/objects.inv` (or
    `https://pymmcore-plus.github.io/objects.inv` for everything).
