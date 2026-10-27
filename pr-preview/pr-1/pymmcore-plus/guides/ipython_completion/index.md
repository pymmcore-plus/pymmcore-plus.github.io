# IPython Tab Completion

`pymmcore-plus` provides an IPython completer that allows you to use tab-completion for methods on the `CMMCorePlus` object. If you hit `<Tab>` after the parenthesis of a core method that expects the name of an existing device, you will be presented with suggestions for the names of loaded devices (of the appropriate type). The same works for property names (e.g. the second argument of `getProperty`), config group and preset names, and device adapter names.

The completer is installed automatically when you import `pymmcore_plus` in an IPython session (including Jupyter notebooks). You may disable this feature by setting the [environment variable](<https://pymmcore-plus.github.io/pymmcore-plus/env_var/index.md>) `PYMM_DISABLE_IPYTHON_COMPLETIONS` to `1` before importing `pymmcore_plus`.
