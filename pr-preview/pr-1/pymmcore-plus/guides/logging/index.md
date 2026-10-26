# Logging

By default, pymmcore-plus logs to the console at the `INFO` level and to a logfile in the pymmcore-plus application data directory at the `DEBUG` level. The logfile is named `pymmcore_plus.log` and is rotated at 40MB, with a maximum retention of 20 logfiles.

## Customizing logging

The `pymmcore_plus.configure_logging` function allows you to customize the log level, logfile name, and logfile rotation settings.

You may also configure logging using the following environment variables:

| Variable | Default | Description |
| --- | --- | --- |
| PYMM\_LOG\_LEVEL | INFO | The log level. |
| PYMM\_LOG\_FILE | `pymmcore_plus.log` in the pymmcore-plus log directory | The logfile location. |
| PYMM\_LOG\_RICH | `0` (disabled) | Use [rich](<https://rich.readthedocs.io/>) for stderr logging (requires `rich`). Set to `1`, `true`, or `yes` to enable. Note: adds some formatting overhead ([\#449](<https://github.com/pymmcore-plus/pymmcore-plus/issues/449>)). |

> [!TIP]
>
> **pymmcore-plus log directory**
>
> The application data directory is platform-dependent. Here are the log folders for each supported platform:
>
> | OS | Path |
> | --- | --- |
> | macOS | \~/Library/Application Support/pymmcore-plus/logs |
> | Unix | \~/.local/share/pymmcore-plus/logs |
> | Win | C:\\Users\\username\\AppData\\Local\\pymmcore-plus\\pymmcore-plus\\logs |
>
> You can also use `mmcore logs --reveal` to open the log directory in your file manager.

Note that both pymmcore-plus and the underlying CMMCore object will write to the log file. By default, CMMCorePlus will call `setPrimaryLogFile()` with the location of the pymmcore-plus logfile upon instantiation.

## Managing logs with the CLI

The `mmcore` CLI provides a `logs` subcommand for managing logs.

```console
$ mmcore logs --help

 Usage: mmcore logs [OPTIONS]                                                   

 Display recent output from pymmcore-plus log.                                  

╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --num     -n      <int>  Number of lines to display.                         │
│ --tail    -t             Continually stream logs.                            │
│ --clear   -c             Delete all log files.                               │
│ --reveal                 Reveal log file in Explorer/Finder.                 │
│ --help                   Show this message and exit.                         │
╰──────────────────────────────────────────────────────────────────────────────╯
```

A particularly useful command is `mmcore logs --tail`, which will continually stream the current logfile to the console. This can be started in another process and left running to monitor an experiment in progress.

To delete all logfiles, use `mmcore logs --clear`.
