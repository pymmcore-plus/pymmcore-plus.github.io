# pymmcore\_plus.install

Functions:

| Name | Description |
| --- | --- |
| `available_versions` | Return a map of version -\> url available for download. |
| `install` | Install Micro-Manager to `dest`. |

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `BASE_URL` |  |  |
| `DOWNLOADS_URL` |  |  |
| `INTERFACES` | `dict[int, str]` |  |
| `MACH` |  |  |
| `PLATFORM` |  |  |
| `PYMMCORE_DIV` |  |  |
| `TEST_ADAPTERS_REPO` |  |  |
| `plat` |  |  |

## BASE\_URL

```python
BASE_URL = 'https://download.micro-manager.org'
```

## DOWNLOADS\_URL

```python
DOWNLOADS_URL = f'{BASE_URL}/nightly/2.0/{plat}/'
```

## INTERFACES

```python
INTERFACES: dict[int, str] = {
    74: "20250815",
    73: "20250318",
    72: "20250318",
    71: "20221031",
    70: "20210219",
    69: "20180712",
    68: "20171107",
    67: "20160609",
    66: "20160608",
    65: "20150528",
    64: "20150515",
    63: "20150505",
    62: "20150501",
    61: "20140801",
    60: "20140618",
    59: "20140515",
    58: "20140514",
    57: "20140125",
    56: "20140120",
}
```

## MACH

```python
MACH = machine()
```

## PLATFORM

```python
PLATFORM = system()
```

## PYMMCORE\_DIV

```python
PYMMCORE_DIV = _pymmcore.version_info.device_interface
```

## TEST\_ADAPTERS\_REPO

```python
TEST_ADAPTERS_REPO = 'micro-manager/mm-test-adapters'
```

## plat

```python
plat = {'Darwin': 'Mac', 'Windows': 'Windows', 'Linux': 'Linux'}.get(PLATFORM)
```

## available\_versions

```python
available_versions() -> dict[str, str]
```

Return a map of version -\> url available for download.

Returns a dict like: { '20220906': '[https://download.micro-manager.org/nightly/2.0/Mac/Micro-Manager-2.0.1-20220906.dmg](<https://download.micro-manager.org/nightly/2.0/Mac/Micro-Manager-2.0.1-20220906.dmg>)', '20220901': '[https://download.micro-manager.org/nightly/2.0/Mac/Micro-Manager-2.0.1-20220901.dmg](<https://download.micro-manager.org/nightly/2.0/Mac/Micro-Manager-2.0.1-20220901.dmg>)', '20220823': '[https://download.micro-manager.org/nightly/2.0/Mac/Micro-Manager-2.0.1-20220823.dmg](<https://download.micro-manager.org/nightly/2.0/Mac/Micro-Manager-2.0.1-20220823.dmg>)', }

## install

```python
install(
    dest: Path | str = USER_DATA_MM_PATH,
    release: str = "latest-compatible",
    log_msg: _MsgLogger = _pretty_print,
    test_adapters: bool = False,
) -> None
```

Install Micro-Manager to `dest`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `dest` | `Path \| str` | Where to install Micro-Manager, by default will install to a pymmcore-plus folder in the user's data directory: `appdirs.user_data_dir()`. | `USER_DATA_MM_PATH` |
| `release` | `str` | Which release to install, by default "latest". Should be a date in the form YYYYMMDD, "latest" to install the latest nightly release, or "latest-compatible" to install the latest nightly release that is compatible with the device interface version of the current pymmcore version. | `'latest-compatible'` |
| `log_msg` | `_MsgLogger` | Callback to log messages, must have signature: `def logger(text: str, color: str = "", emoji: str = ""): ...` May ignore color and emoji. | `_pretty_print` |
| `test_adapters` | `bool` | Whether to install test adapters, by default False. | `False` |
