# pymmcore-plus

`pymmcore-plus` aims to extend [pymmcore](<https://github.com/micro-manager/pymmcore>) (Python bindings for the C++ [Micro-Manager core](<https://github.com/micro-manager/mmCoreAndDevices/>)) with a number of features designed to facilitate working with Micro-Manager in pure Python/C environments. The main object in this library, `CMMCorePlus`, aims to be a drop-in replacement for `pymmcore.CMMCore`, while adding a number of additional features including:

- A multi-dimensional [acquisition engine](<https://pymmcore-plus.github.io/pymmcore-plus/guides/mda_engine/index.md>) implemented in pure Python. (The existing acquisition engines in Micro-Manager are written in Java and Clojure.)
- More flexible [event](<https://pymmcore-plus.github.io/pymmcore-plus/guides/events/index.md>) connections and callback handling.
- Extended convenience APIs for working with the core (which would be hard or impossible to implement in the `pymmcore` SWIG wrapper).
- More pythonic APIs for various pymmcore objects (e.g. `Device`, `Configuration`) and [constants](<https://pymmcore-plus.github.io/pymmcore-plus/guides/constants/index.md>).

## Where to start

If you're new here, start with [Installation](<https://pymmcore-plus.github.io/getting-started/install/index.md>) (which includes getting the [Micro-Manager device adapters](<https://pymmcore-plus.github.io/pymmcore-plus/install/index.md>)), then [First steps](<https://pymmcore-plus.github.io/getting-started/first-steps/index.md>) and [Your first acquisition](<https://pymmcore-plus.github.io/getting-started/first-acquisition/index.md>). The User Guide goes into more depth on [devices and properties](<https://pymmcore-plus.github.io/pymmcore-plus/guides/devices/index.md>), [configuration groups](<https://pymmcore-plus.github.io/pymmcore-plus/guides/configuration/index.md>), [events](<https://pymmcore-plus.github.io/pymmcore-plus/guides/events/index.md>), [running acquisitions](<https://pymmcore-plus.github.io/pymmcore-plus/guides/mda_engine/index.md>) and [saving data](<https://pymmcore-plus.github.io/pymmcore-plus/guides/saving_data/index.md>).

## Reference

- `CMMCorePlus`: every method of the core, with what `pymmcore-plus` adds or overrides marked.
- `pymmcore_plus.mda`: the acquisition runner (`MDARunner`) and engine (`MDAEngine`).
- [Events](<https://pymmcore-plus.github.io/pymmcore-plus/reference/events/index.md>): the signals emitted by `core.events` and `core.mda.events`.
- Metadata schema: the metadata dicts that come with each acquired frame.
- [Constants](<https://pymmcore-plus.github.io/pymmcore-plus/guides/constants/index.md>): the enums that replace pymmcore's integer constants.
- [Command line (`mmcore`)](<https://pymmcore-plus.github.io/pymmcore-plus/cli/index.md>) and [environment variables](<https://pymmcore-plus.github.io/pymmcore-plus/env_var/index.md>).
