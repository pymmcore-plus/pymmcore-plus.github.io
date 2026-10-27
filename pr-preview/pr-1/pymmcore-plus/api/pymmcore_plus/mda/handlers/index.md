# pymmcore\_plus.mda.handlers

Deprecated data handlers (writers) for MDA acquisitions.

> [!WARNING]
>
> **Deprecated**
>
> This module is deprecated, and importing it emits a `FutureWarning`. To save data, pass a path ending in `.ome.zarr` or `.ome.tiff` (or an `ome_writers.AcquisitionSettings`) as the `output` of `MDARunner.run`, which writes with [ome-writers](<https://pymmcore-plus.github.io/ome-writers/>) (see Saving Data). These handlers will be removed in a future version; if you depend on one, please copy it into your own code.

**Classes**

| Name | Description |
| --- | --- |
| `ImageSequenceWriter` | Write each frame of an MDA to a directory as individual image files. |
| `OMETiffWriter` | MDA handler that writes to a 5D OME-TIFF file. |
| `OMEZarrWriter` | MDA handler that writes to a zarr file following the ome-ngff spec. |
| `TensorStoreHandler` | Tensorstore handler for writing MDA sequences. |

**Functions**

| Name | Description |
| --- | --- |
| `handler_for_path` | Convert a string or Path into a handler object. |

## Classes

### ImageSequenceWriter

```python
ImageSequenceWriter(
    directory: Path | str,
    extension: str = ".tif",
    prefix: str = "",
    *,
    imwrite: ImgWriter | None = None,
    overwrite: bool = False,
    include_frame_count: bool = True,
    imwrite_kwargs: dict | None = None,
)
```

Write each frame of an MDA to a directory as individual image files.

This writer assumes very little about the sequence, and simply writes each frame to a file in the specified directory. It is a good option for ragged or sparse sequences, or where the exact number of frames is not known in advance.

The default output format is TIFF, backed by `tifffile.imwrite`, but many other common extensions can be used if `imageio` is installed. Or, you can pass a custom writer function to the `imwrite` argument.

The metadata for each frame is stored in a JSON file in the directory (by default, named "\_frame\_metadata.json"). The metadata is stored as a dict, with the key being the index string for the frame (see index\_template), and the value being the metadata dict for that frame.

The metadata for the entire MDA sequence is stored in a JSON file in the directory (by default, named "\_useq\_MDASequence.json").

> [!NOTE]
>
> This writer outputs a format that is easily consumed by `tifffile.imread` using the `pattern="axes"` option.
>
> ```python
> from tifffile import imread
>
> data = imread("my_folder/*.tif", pattern="axes")
>
> # or with zarr
> import zarr
>
> store = imread("data_folder/*.tif", pattern="axes", aszarr=True)
> data = zarr.open(store)
> ```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `directory` | `Path \| str` | The directory to write the files to. | *required* |
| `extension` | `str` | The file extension to use. By default, ".tif". | `'.tif'` |
| `prefix` | `str` | A prefix to add to the file names. By default, no prefix is added. | `''` |
| `imwrite` | `ImgWriter \| None` | A function to write the image data to disk. The function should take a filename and image data as positional arguments. If None, a writer will be selected based on the extension. For the default extension `.tif`, this will be `tifffile.imwrite` (which must be installed). | `None` |
| `overwrite` | `bool` | Whether to overwrite the directory if it already exists. If False, a FileExistsError will be raised if the directory already exists. | `False` |
| `include_frame_count` | `bool` | Whether to include a frame count item in the template (`{frame:05}`). This will come after the prefix and before the indices. It is a good way to ensure unique keys. by default True | `True` |
| `imwrite_kwargs` | `dict \| None` | Extra keyword arguments to pass to the `imwrite` function. | `None` |

#### FRAME\_META\_PATH

```python
FRAME_META_PATH: str = '_frame_metadata.json'
```

#### SEQ\_META\_PATH

```python
SEQ_META_PATH: str = '_useq_MDASequence.json'
```

#### sequenceStarted

```python
sequenceStarted(seq: MDASequence) -> None
```

Store the sequence metadata and reset the frame counter.

#### sequenceFinished

```python
sequenceFinished(seq: MDASequence) -> None
```

#### frameReady

```python
frameReady(frame: ndarray, event: MDAEvent, meta: FrameMetaV1) -> None
```

Write a frame to disk.

#### fname\_template

```python
fname_template(
    axes: Mapping[str, int] | Sequence[str],
    prefix: str = "",
    extension: str = ".tif",
    delimiter: str = "_",
    include_frame_count: bool = True,
) -> str
```

Generate a string template for file names.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `axes` | `Mapping[str, int] \| Sequence[str]` | The axes to include in the template. If a mapping, the values are the number of digits to use for each axis. If a sequence, the number of digits is determined automatically. | *required* |
| `prefix` | `str` | A prefix to add to the template, by default "" | `''` |
| `extension` | `str` | The file extension to use, by default ".tif" | `'.tif'` |
| `delimiter` | `str` | The delimiter to use between items in the template, by default "\_" | `'_'` |
| `include_frame_count` | `bool` | Whether to include a frame count item in the template (`{frame:05}`). This will come after the prefix and before the indices. It is a good way to ensure unique keys. by default True | `True` |

Examples:

```pycon
>>> SimpleTiffWriter.fname_template("tcz")
'{frame:05}_t{t:04}_c{c:02}_z{z:03}.tif'
>>> fname_template({"c": 2, "z": 3}, "some_prefix")
'some_prefix{frame:05}_c{c:02}_z{z:03}.tif'
```

### OMETiffWriter

```python
OMETiffWriter(filename: Path | str)
```

MDA handler that writes to a 5D OME-TIFF file.

Positions will be split into different files.

Data is memory-mapped to disk using numpy.memmap via tifffile. Tifffile handles the OME-TIFF format.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `filename` | `Path \| str` | The filename to write to. Must end with '.ome.tiff' or '.ome.tif'. | *required* |

#### sequenceStarted

```python
sequenceStarted(seq: MDASequence, meta: SummaryMetaV1 | object = _NULL) -> None
```

#### write\_frame

```python
write_frame(ary: memmap, index: tuple[int, ...], frame: ndarray) -> None
```

Write a frame to the file.

#### new\_array

```python
new_array(position_key: str, dtype: dtype, sizes: dict[str, int]) -> memmap
```

Create a new tifffile file and memmap for this position.

### OMEZarrWriter

```python
OMEZarrWriter(
    store: MutableMapping | str | PathLike | FSMap | None = None,
    *,
    overwrite: bool = False,
    synchronizer: ZarrSynchronizer | None = None,
    zarr_version: Literal[2, 3, None] = None,
    array_kwargs: ArrayCreationKwargs | None = None,
    minify_attrs_metadata: bool = False,
)
```

MDA handler that writes to a zarr file following the ome-ngff spec.

This implements v0.4 [https://ngff.openmicroscopy.org/0.4/index.html](<https://ngff.openmicroscopy.org/0.4/index.html>)

It also aims to be compatible with the xarray Zarr spec: [https://docs.xarray.dev/en/latest/internals/zarr-encoding-spec.html](<https://docs.xarray.dev/en/latest/internals/zarr-encoding-spec.html>)

Note: this does *not* currently calculate any additional pyramid levels. But it would be easy to do so after acquisition. Chunk size is currently 1 XY plane.

Zarr directory structure will be:

```text
root.zarr/
├── .zgroup                 # group metadata
├── .zattrs                 # contains ome-multiscales metadata
│
├── p0                      # each position is a separate <=5D array
│   ├── .zarray
│   ├── .zattrs
│   └── t                   # nested directories for each dimension
│       └── c               # (only collected dimensions will be present)
│           └── z
│               └── y
│                   └── x   # chunks will be each XY plane
├── ...
├── p<n>
│   ├── .zarray
│   ├── .zattrs
│   └── t...
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `store` | `MutableMapping \| str \| PathLike \| FSMap \| None` | Zarr store or path to directory in file system to write to. Semantics are the same as for `zarr.group`: If a string, it is interpreted as a path to a directory. If None, an in-memory store is used. May also be any mutable mapping or instance of `zarr.storage.BaseStore`. | `None` |
| `overwrite` | `bool` | If True, delete any pre-existing data in `store` at `path` before creating the group. If False, raise an error if there is already data in `store` at `path`. by default False. | `False` |
| `synchronizer` | `ZarrSynchronizer \| None` | Array synchronizer passed to `zarr.group`. | `None` |
| `zarr_version` | `(2, 3, None)` | Zarr version passed to `zarr.group`. | `2` |
| `array_kwargs` | `dict` | Keyword arguments passed to `zarr.group.create` when creating the arrays. This may be used to set the zarr `compressor`, `fill_value`, `synchronizer`, etc... Default is `{'dimension_separator': '/'}`. | `None` |
| `minify_attrs_metadata` | `bool` | If True, zattrs metadata will be read from disk, minified, and written back to disk at the end of a successful acquisition (to save space). Default is False. | `False` |

#### group

```python
group: Group
```

Read-only access to the zarr group.

#### in\_tmpdir

```python
in_tmpdir(
    suffix: str | None = ".zarr",
    prefix: str | None = "pymmcore_zarr_",
    dir: str | PathLike[str] | None = None,
    cleanup_atexit: bool = True,
    **kwargs: Any,
) -> OMEZarrWriter
```

Create OMEZarrHandler that writes to a temporary directory.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `suffix` | `str` | If suffix is specified, the file name will end with that suffix, otherwise there will be no suffix. | `'.zarr'` |
| `prefix` | `str` | If prefix is specified, the file name will begin with that prefix, otherwise a default prefix is used. | `'pymmcore_zarr_'` |
| `dir` | `str or PathLike` | If dir is specified, the file will be created in that directory, otherwise a default directory is used (tempfile.gettempdir()) | `None` |
| `cleanup_atexit` | `bool` | Whether to automatically cleanup the temporary directory when the python process exits. Default is True. | `True` |
| `**kwargs` | `Any` | Remaining kwargs are passed to `OMEZarrHandler.__init__` | `{}` |

#### finalize\_metadata

```python
finalize_metadata() -> None
```

Called by superclass in sequenceFinished. Flush metadata to disk.

#### new\_array

```python
new_array(key: str, dtype: dtype, sizes: dict[str, int]) -> Array
```

Create a new array in the group, under `key`.

#### as\_xarray

```python
as_xarray() -> Dataset
```

### TensorStoreHandler

```python
TensorStoreHandler(
    *,
    driver: TsDriver = "zarr",
    kvstore: str | dict | None = "memory://",
    path: str | PathLike | None = None,
    delete_existing: bool = False,
    spec: Mapping | None = None,
)
```

Tensorstore handler for writing MDA sequences.

This is a performant and shape-agnostic handler for writing MDA sequences to chunked storages like zarr, n5, backed by tensorstore: [https://google.github.io/tensorstore/](<https://google.github.io/tensorstore/>)

By default, the handler will store frames in a zarr array, with a shape of (nframes, \*frame\_shape) and a chunk size of (1, \*frame\_shape), i.e. each frame is stored in a separate chunk. To customize shape or chunking, override the `get_full_shape`, `get_chunk_layout`, and `get_index_domain` methods (these may change in the future as we learn to use tensorstore better).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `driver` | `TsDriver` | The driver to use for the tensorstore, by default "zarr". Must be one of "zarr", "zarr3", "n5", or "neuroglancer\_precomputed". | `'zarr'` |
| `kvstore` | `str \| dict \| None` | The key-value store to use for the tensorstore, by default "memory://". A dict might look like {'driver': 'file', 'path': '/path/to/dataset.zarr'} see [https://google.github.io/tensorstore/kvstore/index.html\#json-KvStore](<https://google.github.io/tensorstore/kvstore/index.html#json-KvStore>) for all options. If path is provided, the kvstore will be set to file://path | `'memory://'` |
| `path` | `str \| Path \| None` | Convenience for specifying a local filepath. If provided, overrides the kvstore option, to be `file://file_path`. | `None` |
| `delete_existing` | `bool` | Whether to delete the existing dataset if it exists, by default False. | `False` |
| `spec` | `Mapping` | A spec to use when opening the tensorstore, by default None. Values provided in this object will override the default values provided by the handler. This is a complex object that can completely define the tensorstore, see [https://google.github.io/tensorstore/spec.html](<https://google.github.io/tensorstore/spec.html>) for more information. | `None` |

Examples:

```python
from pymmcore_plus import CMMCorePlus
from pymmcore_plus.mda.handlers import TensorStoreHandler
from useq import MDASequence

core = CMMCorePlus.instance()
core.loadSystemConfiguration()

sequence = MDASequence(
    channels=["DAPI", {"config": "FITC", "exposure": 1}],
    stage_positions=[{"x": 1, "y": 1, "name": "some position"}, {"x": 0, "y": 0}],
    time_plan={"interval": 2, "loops": 3},
    z_plan={"range": 4, "step": 0.5},
    axis_order="tpcz",
)

writer = TensorStoreHandler(path="example_ts.zarr", delete_existing=True)
core.mda.run(sequence, output=writer)
```

#### ts\_driver

```python
ts_driver = driver
```

#### kvstore

```python
kvstore: dict | str = {'driver': 'file', 'path': str(path)}
```

#### delete\_existing

```python
delete_existing = delete_existing
```

#### spec

```python
spec = spec
```

#### frame\_metadatas

```python
frame_metadatas: list[tuple[MDAEvent, FrameMetaV1]] = []
```

#### store

```python
store: TensorStore | None
```

The current tensorstore.

#### current\_sequence

```python
current_sequence: MDASequence | None
```

Return current sequence, or none.

Use `.reset()` to initialize the handler for a new sequence.

#### in\_tmpdir

```python
in_tmpdir(
    suffix: str | None = "",
    prefix: str | None = "pymmcore_zarr_",
    dir: str | PathLike[str] | None = None,
    cleanup_atexit: bool = True,
    **kwargs: Any,
) -> Self
```

Create TensorStoreHandler that writes to a temporary directory.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `suffix` | `str` | If suffix is specified, the file name will end with that suffix, otherwise there will be no suffix. | `''` |
| `prefix` | `str` | If prefix is specified, the file name will begin with that prefix, otherwise a default prefix is used. | `'pymmcore_zarr_'` |
| `dir` | `str or PathLike` | If dir is specified, the file will be created in that directory, otherwise a default directory is used (tempfile.gettempdir()) | `None` |
| `cleanup_atexit` | `bool` | Whether to automatically cleanup the temporary directory when the python process exits. Default is True. | `True` |
| `**kwargs` | `Any` | Remaining kwargs are passed to `TensorStoreHandler.__init__` | `{}` |

#### reset

```python
reset(sequence: MDASequence) -> None
```

Reset state to prepare for new `sequence`.

#### sequenceStarted

```python
sequenceStarted(seq: MDASequence, meta: SummaryMetaV1) -> None
```

On sequence started, simply store the sequence.

#### sequenceFinished

```python
sequenceFinished(seq: MDASequence) -> None
```

On sequence finished, clear the current sequence.

#### frameReady

```python
frameReady(frame: ndarray, event: MDAEvent, meta: FrameMetaV1) -> None
```

Write frame to the zarr array for the appropriate position.

#### isel

```python
isel(
    indexers: Mapping[str, int | slice] | None = None,
    **indexers_kwargs: int | slice,
) -> ndarray
```

Select data from the array.

#### new\_store

```python
new_store(
    frame: ndarray, seq: MDASequence | None, meta: FrameMetaV1
) -> Future[TensorStore]
```

#### get\_shape\_chunks\_labels

```python
get_shape_chunks_labels(
    frame_shape: tuple[int, ...], seq: MDASequence | None
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[str, ...]]
```

#### get\_spec

```python
get_spec() -> dict
```

Construct the tensorstore spec.

#### finalize\_metadata

```python
finalize_metadata() -> None
```

Finalize and flush metadata to storage.

## Functions

### handler\_for\_path

```python
handler_for_path(path: str | Path) -> object
```

Convert a string or Path into a handler object.

This method picks from the built-in handlers based on the extension of the path.
