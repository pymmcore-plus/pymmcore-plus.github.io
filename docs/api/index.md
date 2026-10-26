---
title: API Reference
---

# API Reference

The API reference is generated from the source code of each package.  Every
public object is documented once, under its **shortest public import path**
(e.g. `pymmcore_plus.CMMCorePlus`, not `pymmcore_plus.core.CMMCorePlus`);
other modules that re-export it link there.

<div class="grid cards" markdown>

-   **[pymmcore-plus](../pymmcore-plus/index.md)**

    ---

    [`CMMCorePlus`][pymmcore_plus.CMMCorePlus] (every core method, with what
    pymmcore-plus adds), the [acquisition engine][pymmcore_plus.mda],
    device objects, constants, metadata, and the
    [`mmcore` CLI](../pymmcore-plus/cli.md).

-   **[useq-schema](../useq-schema/index.md)**

    ---

    [`MDASequence`][useq.MDASequence], [`MDAEvent`][useq.MDAEvent], and all
    axis plans.

-   **[pymmcore-widgets](../pymmcore-widgets/index.md)**

    ---

    Every widget, with a screenshot and an example.

-   **[pymmcore-gui](../pymmcore-gui/api/pymmcore_gui/index.md)**

    ---

    Application entry points and extension points (actions, widgets).

</div>

!!! tip "Linking to these docs from your own project"

    Each package publishes an object inventory for
    [mkdocstrings](https://mkdocstrings.github.io/) and
    [intersphinx](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html),
    e.g. `https://pymmcore-plus.github.io/pymmcore-plus/objects.inv` (or
    `/objects.inv` for everything).
