# User Guide

The User Guide is organized by topic, roughly following the stack from the hardware up. Each page belongs to one package's docs (the badge at the top says which), and names of classes and functions link to the [API reference](<https://pymmcore-plus.github.io/api/index.md>). If you're new here, [Getting Started](<https://pymmcore-plus.github.io/getting-started/which-package/index.md>) is probably a better place to begin.

- **Controlling hardware**

  ---

  [Installing device adapters](<https://pymmcore-plus.github.io/pymmcore-plus/install/index.md>), [using your own microscope](<https://pymmcore-plus.github.io/guide/own-microscope/index.md>), [devices and properties](<https://pymmcore-plus.github.io/pymmcore-plus/guides/devices/index.md>), [configuration groups](<https://pymmcore-plus.github.io/pymmcore-plus/guides/configuration/index.md>), and [events and callbacks](<https://pymmcore-plus.github.io/pymmcore-plus/guides/events/index.md>) (which are how GUIs, and your own code, stay in sync with the core).
- **Describing experiments**

  ---

  How [useq-schema](<https://pymmcore-plus.github.io/useq-schema/index.md>) describes an acquisition as a sequence of events, and [building sequences](<https://pymmcore-plus.github.io/useq-schema/guides/sequences/index.md>) with time points, z-stacks, channels, positions, grids, etc...
- **Running acquisitions**

  ---

  [The acquisition engine](<https://pymmcore-plus.github.io/pymmcore-plus/guides/mda_engine/index.md>), [saving data](<https://pymmcore-plus.github.io/pymmcore-plus/guides/saving_data/index.md>), [event-driven acquisition](<https://pymmcore-plus.github.io/pymmcore-plus/guides/event_driven_acquisition/index.md>), and [writing your own engine](<https://pymmcore-plus.github.io/pymmcore-plus/guides/custom_engine/index.md>).
- **Building GUIs**

  ---

  The [widget gallery](<https://pymmcore-plus.github.io/pymmcore-widgets/widgets/index.md>), [building a custom GUI](<https://pymmcore-plus.github.io/pymmcore-widgets/getting_started/index.md>) from those widgets, and [keeping it responsive](<https://pymmcore-plus.github.io/pymmcore-plus/examples/integration-with-qt/index.md>).
- **Applications**

  ---

  [pymmcore-gui](<https://pymmcore-plus.github.io/pymmcore-gui/index.md>), our desktop application, and [napari-micromanager](<https://pymmcore-plus.github.io/napari-micromanager/index.md>), which controls a microscope from inside napari.
- **Advanced topics**

  ---

  [Device adapters written in Python](<https://pymmcore-plus.github.io/pymmcore-plus/guides/unicore/index.md>) (`UniMMCore`), a preview of [useq-schema v2](<https://pymmcore-plus.github.io/useq-schema/v2-migration/index.md>), and a [Pycro-Manager-style API](<https://pymmcore-plus.github.io/pymmcore-plus/examples/pycro-manager-api/index.md>).

> [!NOTE]
>
> **Something not working?**
>
> The troubleshooting pages cover [the core and device adapters](<https://pymmcore-plus.github.io/pymmcore-plus/troubleshooting/index.md>) and [Qt and widgets](<https://pymmcore-plus.github.io/pymmcore-widgets/troubleshooting/index.md>). Turning up the [logging](<https://pymmcore-plus.github.io/pymmcore-plus/guides/logging/index.md>) (or [profiling](<https://pymmcore-plus.github.io/pymmcore-plus/profiling/index.md>), if things are slow) can also help you work out what's going on. If you're still stuck, please ask on the [image.sc forum](<https://forum.image.sc/tag/pymmcore-plus>).
