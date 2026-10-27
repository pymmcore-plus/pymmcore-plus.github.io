# CLI Reference

This page provides documentation for the `mmcore` command line tool, which is installed along with `pymmcore-plus`.

The CLI can be used to interact with the `pymmcore_plus` package from the command line, including the installation, removal, and selection of Micro-Manager device adapters, showing log files, and running a test acquisition (`mmcore run`, which doesn't save anything). (The default `--dest` folder for `install` and `build-dev` depends on your platform; see [Micro-Manager device adapters](<https://pymmcore-plus.github.io/pymmcore-plus/install/#installing-micro-manager-device-adapters>).)

## `mmcore`

mmcore: pymmcore-plus command line.

For additional help on a specific command: type `mmcore COMMAND --help`

**Usage**:

```console
$ mmcore [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--version`: Show version and exit.
- `--install-completion`: Install completion for the current shell.
- `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
- `--help`: Show this message and exit.

### `mmcore clean`

Remove all Micro-Manager installs downloaded by pymmcore-plus.

**Usage**:

```console
$ mmcore clean [OPTIONS] [glob]
```

**Arguments**:

- `glob`: glob pattern to clean \[default: \*\]

**Options**:

- `--help`: Show this message and exit.

### `mmcore list`

Show all discovered Micro-Manager installations.

**Usage**:

```console
$ mmcore list [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.

### `mmcore mmstudio`

Run the Java Micro-Manager GUI.

This command will attempt to locate and execute an ImageJ application found in the active Micro-Manager directory.

**Usage**:

```console
$ mmcore mmstudio [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.

### `mmcore install`

Install Micro-Manager device adapters from [https://download.micro-manager.org](<https://download.micro-manager.org>).

On Windows and Intel macOS, this downloads a nightly build of Micro-Manager. Micro-Manager doesn't publish nightly builds for Linux or Apple Silicon, so on those platforms only the test adapters (DemoCamera, Utilities, etc...) are installed, from [https://github.com/micro-manager/mm-test-adapters](<https://github.com/micro-manager/mm-test-adapters>).

**Usage**:

```console
$ mmcore install [OPTIONS]
```

**Options**:

- `-d, --dest <directory>`: Installation directory. \[default: \<user data dir\>/pymmcore-plus/mm\]
- `-r, --release <str>`: Release date. e.g. 20210201 \[default: latest-compatible\]
- `--plain-output`: Do not use rich output. Useful for scripting.
- `--test-adapters`: Install only test adapters (e.g. DemoCamera and others for testing).
- `--help`: Show this message and exit.

### `mmcore run`

Run a Micro-Manager acquisition from a useq-schema MDASequence file.

Nothing is saved to disk (this is mostly useful for testing and profiling).

**Usage**:

```console
$ mmcore run [OPTIONS] [useq]
```

**Arguments**:

- `useq`: Path to useq-schema file.

**Options**:

- `-c, --config <file>`: Path to Micro-Manager system configuration file.
- `--z-go-up / --no-z-go-up`: Acquire from bottom to top.
- `--z-top <float>`: Top of z-stack.
- `--z-bottom <float>`: Bottom of z-stack.
- `--z-range <float>`: Symmetric range of z-stack around position.
- `--z-above <float>`: Asymmetric range of z-stack above position.
- `--z-below <float>`: Asymmetric range of z-stack below position.
- `--z-step <float>`: Step size of z-stack.
- `-zr <float>`: Relative z-positions to acquire (may use multiple times).
- `-za <float>`: Absolute z-positions to acquire (may use multiple times).
- `--t-interval <float>`: Interval between timepoints.
- `--t-duration <float>`: Duration of time lapse.
- `--t-loops <float>`: Number of time points to acquire.
- `--dry-run / --no-dry-run`: Do not run the acquisition. \[default: no-dry-run\]
- `--axis-order <str>`: Order of axes to acquire (e.g. 'TPCZ').
- `--channel <str>`: Channel to acquire. Argument is a string of the following form:

  - name: "DAPI"
  - name;exposure: "DAPI;0.5"
  - useq-schema JSON: '{"config": "DAPI", "exposure": 0.5, "z\_offset": 0.5}'
- `--channel-group <str>`: Name of Micro-Manager configuration group for channels. \[default: Channel\]
- `--help`: Show this message and exit.

### `mmcore build-dev`

Build Micro-Manager device adapters from the git repo.

Currently only supports macos and linux.

**Usage**:

```console
$ mmcore build-dev [OPTIONS] [devices]...
```

**Arguments**:

- `devices...`: Device adapters to build. Defaults to \['DemoCamera', 'Utilities', 'SequenceTester'\]

**Options**:

- `-d, --dest <directory>`: Installation directory. \[default: \<user data dir\>/pymmcore-plus/mm\]
- `-y`: Overwrite existing if git sha is already built. If not specified, will prompt.
- `--help`: Show this message and exit.

### `mmcore logs`

Display recent output from pymmcore-plus log.

**Usage**:

```console
$ mmcore logs [OPTIONS]
```

**Options**:

- `-n, --num <int>`: Number of lines to display.
- `-t, --tail`: Continually stream logs.
- `-c, --clear`: Delete all log files.
- `--reveal`: Reveal log file in Explorer/Finder.
- `--help`: Show this message and exit.

### `mmcore info`

Display information about the Micro-Manager and pymmcore install.

**Usage**:

```console
$ mmcore info [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.

### `mmcore use`

Change the currently used Micro-Manager version/path.

**Usage**:

```console
$ mmcore use [OPTIONS] {pattern}
```

**Arguments**:

- `pattern`: Path to an existing directory, or pattern to match against installations found by `mmcore list` \[required\]

**Options**:

- `--help`: Show this message and exit.

### `mmcore bench`

Run a benchmark of Core and Devices loaded with `config` (or Demo).

**Usage**:

```console
$ mmcore bench [OPTIONS]
```

**Options**:

- `-c, --config <file>`: Path to Micro-Manager system configuration file.
- `-n, --number <int>`: Number of iterations for each test. \[default: 10\]
- `--help`: Show this message and exit.
