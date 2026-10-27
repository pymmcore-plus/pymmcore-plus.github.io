# pymmcore\_plus.mda

Running multi-dimensional acquisitions: the runner, the default engine, and signals.

`MDARunner` (available as `core.mda`) runs an acquisition, and `MDAEngine` (`core.mda.engine`) drives the hardware for each event. See The Acquisition Engine for a guide.

**Submodules**

| Name | Description |
| --- | --- |
| `events` | Signals emitted by the MDA runner (`core.mda.events`) during an acquisition. |
| `handlers` | Deprecated data handlers (writers) for MDA acquisitions. |

**Classes**

| Name | Description |
| --- | --- |
| `FinishReason` | Reason why an MDA sequence finished. |
| `MDAEngine` | The default MDAEngine that ships with pymmcore-plus. |
| `MDARunner` | Object that executes a multi-dimensional experiment using an MDAEngine. |
| `PMDAEngine` | Protocol that all MDA engines must implement. |
| `PMDASignaler` | Declares the protocol for all signals that will be emitted from `pymmcore_plus.mda.MDARunner`. |
| `RunState` | State of the MDA acquisition runner. |
| `RunnerStatus` | Snapshot of the MDA runner's current state. |
| `SkipEvent` | Raised by an engine's `setup_event` to skip the current event. |

**Functions**

| Name | Description |
| --- | --- |
| `mda_listeners_connected` | Context in which MDA events are connected to listeners, in a thread by default. |

**Attributes**

| Name | Description |
| --- | --- |
| `SupportsFrameReady` |  |

## Classes

### MDAEngine

```python
MDAEngine(
    mmc: CMMCorePlus,
    *,
    use_hardware_sequencing: bool = True,
    force_set_xy_position: bool = True,
    restore_initial_state: bool | None = None,
    timeout_base: float = 5.0,
    timeout_multiplier: float = 5.0,
    timeout_first_frame: float | None = 20.0,
    timeout_action: Literal["raise", "warn"] = "raise",
)
```

Bases: `PMDAEngine`

The default MDAEngine that ships with pymmcore-plus.

This implements the `PMDAEngine` protocol, and uses a `CMMCorePlus` instance to control the hardware. For each event, it moves the stages, sets the channel preset, exposure, properties and ROI, waits for the system, and snaps an image (see what the engine does). Where the hardware allows it, consecutive events are merged into hardware-triggered sequences.

It may be subclassed to provide custom behavior, or to override specific methods. See Custom Acquisition Engines.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `mmcore` | `CMMCorePlus` | The `CMMCorePlus` instance to use for hardware control. |
| `use_hardware_sequencing` | `bool` | Whether to use hardware sequencing if possible. If `True`, the engine will attempt to combine MDAEvents into a single `SequencedEvent` when the hardware supports it (see `iter_sequenced_events`). This can be set after instantiation. By default, this is `True`, however in various testing and demo scenarios, you may wish to set it to `False` in order to avoid unexpected behavior. Note that events are merged without comparing their `metadata`, so set it to `False` if your engine depends on per-event metadata. |
| `force_set_xy_position` | `bool` | Whether to always set the XY position, even if the target position is the same as the last commanded position (this does *not* query the stage for the current position). By default, this is `True`. |
| `restore_initial_state` | `bool \| None` | Whether to restore the initial hardware state after the MDA sequence completes. If `True`, the engine will capture the initial state (XY and Z positions, config groups, exposure, autoshutter and ROI) before the sequence starts and restore it after completion. If `None` (the default), `restore_initial_state` will be set to `True` if FocusDirection is known (i.e. not Unknown). Stage positions are never restored while the focus direction is unknown. |
| `timeout_base` | `float` | Minimum per-image timeout in seconds for sequenced acquisitions. The actual timeout used is `max(timeout_base, exposure_s * timeout_multiplier)`. The deadline is reset after each received frame, so long sequences will not time out as long as frames keep arriving. By default, this is `5.0`. |
| `timeout_multiplier` | `float` | Multiplier applied to the camera exposure time (in seconds) to compute the per-image timeout for sequenced acquisitions. By default, this is `5.0`. |
| `timeout_first_frame` | `float \| None` | Separate timeout in seconds for waiting for the *first* frame of a sequenced acquisition. This is useful when the camera is waiting for an external trigger that may arrive much later than the exposure time would suggest. If `None`, the standard computed timeout is used for all frames including the first. By default, this is `20.0`. |
| `timeout_action` | `Literal['raise', 'warn']` | What to do when a sequenced acquisition times out. If `"raise"` (the default), a `TimeoutError` is raised. If `"warn"`, a warning is issued and `None` is yielded for any missing frames. |

#### use\_hardware\_sequencing

```python
use_hardware_sequencing: bool = use_hardware_sequencing
```

#### force\_set\_xy\_position

```python
force_set_xy_position: bool = force_set_xy_position
```

#### restore\_initial\_state

```python
restore_initial_state: bool | None = restore_initial_state
```

#### timeout\_base

```python
timeout_base: float = timeout_base
```

#### timeout\_multiplier

```python
timeout_multiplier: float = timeout_multiplier
```

#### timeout\_first\_frame

```python
timeout_first_frame: float | None = timeout_first_frame
```

#### timeout\_action

```python
timeout_action: Literal['raise', 'warn'] = timeout_action
```

#### include\_frame\_position\_metadata

```python
include_frame_position_metadata: IncludePositionArg
```

#### mmcore

```python
mmcore: CMMCorePlus
```

The `CMMCorePlus` instance to use for hardware control.

#### setup\_sequence

```python
setup_sequence(sequence: MDASequence) -> SummaryMetaV1 | None
```

Setup the hardware for the entire sequence.

#### get\_summary\_metadata

```python
get_summary_metadata(
    mda_sequence: MDASequence | None, *, include_property_details: bool = False
) -> SummaryMetaV1
```

#### setup\_event

```python
setup_event(event: MDAEvent) -> None
```

Set the system hardware (XY, Z, channel, exposure) as defined in the event.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `event` | `MDAEvent` | The event to use for the Hardware config | *required* |

#### exec\_event

```python
exec_event(event: MDAEvent) -> Iterable[PImagePayload | None]
```

Execute an individual event and return the image data.

#### event\_iterator

```python
event_iterator(events: Iterable[MDAEvent]) -> Iterator[MDAEvent]
```

Event iterator that merges events for hardware sequencing if possible.

This wraps `for event in events: ...` inside `MDARunner.run()` and combines sequenceable events into an instance of `SequencedEvent` if `self.use_hardware_sequencing` is `True`.

#### setup\_single\_event

```python
setup_single_event(event: MDAEvent) -> None
```

Setup hardware for a single (non-sequenced) event.

This method is not part of the PMDAEngine protocol (it is called by `setup_event`, which *is* part of the protocol), but it is made public in case a user wants to subclass this engine and override this method.

#### exec\_single\_event

```python
exec_single_event(event: MDAEvent) -> Iterator[PImagePayload | None]
```

Execute a single (non-triggered) event and return the image data.

This method is not part of the PMDAEngine protocol (it is called by `exec_event`, which *is* part of the protocol), but it is made public in case a user wants to subclass this engine and override this method.

#### get\_frame\_metadata

```python
get_frame_metadata(
    event: MDAEvent,
    prop_values: tuple[PropertyValue, ...] | None = None,
    runner_time_ms: float = 0.0,
    include_position: bool = True,
    camera_device: str | None = None,
) -> FrameMetaV1
```

#### teardown\_event

```python
teardown_event(event: MDAEvent) -> None
```

Teardown state of system (hardware, etc.) after `event`.

#### teardown\_sequence

```python
teardown_sequence(sequence: MDASequence) -> None
```

Perform any teardown required after the sequence has been executed.

#### setup\_sequenced\_event

```python
setup_sequenced_event(event: SequencedEvent) -> None
```

Setup hardware for a sequenced (triggered) event.

This method is not part of the PMDAEngine protocol (it is called by `setup_event`, which *is* part of the protocol), but it is made public in case a user wants to subclass this engine and override this method.

#### post\_sequence\_started

```python
post_sequence_started(event: SequencedEvent) -> None
```

Perform any actions after startSequenceAcquisition has been called.

This method is available to subclasses in case they need to perform any actions after a hardware-triggered sequence has been started (i.e. after core.startSequenceAcquisition has been called).

The default implementation does nothing.

#### exec\_sequenced\_event

```python
exec_sequenced_event(event: SequencedEvent) -> EventPayloadGenerator
```

Execute a sequenced (triggered) event and return the image data.

This method is not part of the PMDAEngine protocol (it is called by `exec_event`, which *is* part of the protocol), but it is made public in case a user wants to subclass this engine and override this method.

### PMDAEngine

Bases: `Protocol`

Protocol that all MDA engines must implement.

#### setup\_sequence

```python
setup_sequence(sequence: MDASequence) -> SummaryMetaV1 | None
```

Setup state of system (hardware, etc.) before an MDA is run.

This method is called once at the beginning of a sequence.

#### setup\_event

```python
setup_event(event: MDAEvent) -> None
```

Prepare state of system (hardware, etc.) for `event`.

This method is called before each event in the sequence. It is responsible for preparing the state of the system for the event. The engine should be in a state where it can call `exec_event` without any additional preparation. (This means that the engine should perform any waits or blocks required for system state changes to complete.)

If the engine cannot set up the event (e.g. hardware failure), it may raise `SkipEvent(num_frames)` to tell the runner to skip this event and inform the data sink of the missing frames. If `SkipEvent` is raised, `exec_event` will NOT be called for this event, but `teardown_event` will be.

#### exec\_event

```python
exec_event(event: MDAEvent) -> Iterable[PImagePayload | None]
```

Execute `event`.

This method is called after `setup_event` and is responsible for executing the event. The default assumption is to acquire an image, but more elaborate events will be possible.

Yields `(image, event, metadata)` tuples for each acquired frame. May yield `None` for frames that could not be acquired (e.g. partial hardware failure during a triggered sequence); the runner will call `sink.skip(frames=1)` for each `None`.

#### event\_iterator

```python
event_iterator(events: Iterable[MDAEvent]) -> Iterator[MDAEvent]
```

Wrapper on the event iterator.

**Optional.**

This can be used to wrap the event iterator to perform any event merging (e.g. if the engine supports HardwareSequencing) or event modification. The default implementation is just `iter(events)`.

Be careful when using this method. It is powerful and can result in unexpected event iteration if used incorrectly.

#### teardown\_event

```python
teardown_event(event: MDAEvent) -> None
```

Teardown state of system (hardware, etc.) after `event`.

**Optional.**

If the engine provides this function, it will be called after `exec_event` to perform any cleanup or teardown required after the event has been executed.

#### teardown\_sequence

```python
teardown_sequence(sequence: MDASequence) -> None
```

Perform any teardown required after the sequence has been executed.

**Optional.**

If the engine provides this function, it will be called after the last event in the sequence has been executed.

### FinishReason

Bases: `StrEnum`

Reason why an MDA sequence finished.

#### COMPLETED

```python
COMPLETED = 'completed'
```

#### CANCELED

```python
CANCELED = 'canceled'
```

#### ERRORED

```python
ERRORED = 'errored'
```

### MDARunner

```python
MDARunner()
```

Object that executes a multi-dimensional experiment using an MDAEngine.

This object is available at `CMMCorePlus.mda`.

This is the main object that runs a multi-dimensional experiment (the "runner"). It iterates over the events, waits until each one is due (`min_start_time`), handles pausing and cancelling, and sends the acquired frames to the `output` (if any). The hardware itself is driven by an acquisition engine (the `engine`, by default an `MDAEngine`) that implements the `PMDAEngine` protocol. It emits signals at specific times during the experiment (see `PMDASignaler` for details on the signals that are available to connect to and when they are emitted). See The Acquisition Engine for a guide.

The state machine modeled by this runner is as follows:

```
stateDiagram-v2
    [*] --> IDLE
    IDLE --> PREPARING : run()
    PREPARING --> running : sequence ready
    state running {
        WAITING --> ACQUIRING : next event ready
        ACQUIRING --> WAITING : event done
        WAITING --> PAUSED : <code>set_paused(True)</code>
        PAUSED --> WAITING : <code>set_paused(False)</code>
        ACQUIRING --> PAUSED : <code>set_paused(True)</code></br>(after event done)
    }
    running --> FINISHING : <code>cancel()</code>
    running --> FINISHING : all events exhausted
    FINISHING --> IDLE : cleanup done
```

You can query the current state of the runner using the `status` property, which returns a snapshot of the runner's current state, including the current phase of the acquisition, whether a cancel or pause has been requested, and the reason for finishing (once the acquisition is finished).

#### engine

```python
engine: MDAEngine | None
```

The `PMDAEngine` that is currently being used.

#### events

```python
events: PMDASignaler
```

Signals that are emitted during the MDA run.

See `PMDASignaler` for details on the signals that are available to connect to.

#### status

```python
status: RunnerStatus
```

Snapshot of the runner's current status.

#### set\_engine

```python
set_engine(engine: PMDAEngine) -> PMDAEngine | None
```

Set the `PMDAEngine` to use for the MDA run.

#### is\_running

```python
is_running() -> bool
```

Return True if an acquisition is currently underway.

This will return True at any point between the emission of the `sequenceStarted` and `sequenceFinished` signals, including when the acquisition is currently paused.

Returns:

| Type | Description |
| --- | --- |
| `bool` | Whether an acquisition is underway. |

#### is\_paused

```python
is_paused() -> bool
```

Return True if the acquisition is currently paused.

Use `set_paused` to change the paused state.

Returns:

| Type | Description |
| --- | --- |
| `bool` | Whether the current acquisition is paused. |

#### cancel

```python
cancel() -> None
```

Cancel the currently running acquisition.

This is a no-op if no acquisition is currently running. If an acquisition is running then this will cancel the acquisition and a sequenceCanceled signal, followed by a sequenceFinished signal will be emitted.

#### toggle\_pause

```python
toggle_pause() -> None
```

Toggle the paused state of the current acquisition.

> [!WARNING]
>
> **Deprecated**
>
> Use `set_paused` instead.

#### set\_paused

```python
set_paused(paused: bool) -> None
```

Set the paused state of the current acquisition.

This is a no-op if the acquisition is already in the requested state, or if no acquisition is currently underway.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `paused` | `bool` | Whether to pause (True) or unpause (False) the acquisition. | *required* |

#### run

```python
run(
    events: Iterable[MDAEvent],
    *,
    output: SingleOutput | Sequence[SingleOutput] | None = None,
    overwrite: bool = False,
    dimension_overrides: dict[str, DimensionOverride] | None = None,
) -> None
```

Run the multi-dimensional acquisition defined by `sequence`.

Most users should not use this directly as it will block further execution. Instead, use the `CMMCorePlus.run_mda` method which will run on a thread.

> [!IMPORTANT]
>
> If `output` is a sequence, it may contain no more than one `str | Path | AcquisitionSettings`.

Parameters:

<table>       <thead>         <tr>           <th>Name</th>           <th>Type</th>           <th>Description</th>           <th>Default</th>         </tr>       </thead>       <tbody>           <tr class="doc-section-item">             <td>                 <code>events</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.mda.MDARunner.run" backlink-type="used-by" hover="" identifier="collections.abc.Iterable" optional="">Iterable</autoref>[<autoref backlink-anchor="pymmcore_plus.mda.MDARunner.run" backlink-type="used-by" hover="" identifier="useq.MDAEvent" optional="">MDAEvent</autoref>]</code>             </td>             <td>               <div class="doc-md-description">                 <p>An iterable of <code>useq.MDAEvents</code> objects to execute.</p>                </div>             </td>             <td>                 <em>required</em>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>output</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.mda.MDARunner.run" backlink-type="used-by" hover="" identifier="pymmcore_plus.mda._runner.SingleOutput" optional="">SingleOutput</autoref> | <autoref backlink-anchor="pymmcore_plus.mda.MDARunner.run" backlink-type="used-by" hover="" identifier="collections.abc.Sequence" optional="">Sequence</autoref>[<autoref backlink-anchor="pymmcore_plus.mda.MDARunner.run" backlink-type="used-by" hover="" identifier="pymmcore_plus.mda._runner.SingleOutput" optional="">SingleOutput</autoref>] | None</code>             </td>             <td>               <div class="doc-md-description">                 <p>The output handler(s) to use.  If None, no output will be saved.</p> <p>The value may be either a single output or a sequence of outputs, where a &quot;single output&quot; can be any of the following:</p> <ol> <li> <p>A string or <code>Path</code>. This value is passed directly to     <autoref data-zensical-autoref="" domain="py" filepath="/Users/runner/work/pymmcore-plus.github.io/pymmcore-plus.github.io/.repos/pymmcore-plus/src/pymmcore_plus/mda/_runner.py" identifier="ome_writers.AcquisitionSettings" lineno="351" origin="pymmcore_plus.mda.MDARunner.run" role="meth"><code>ome_writers.AcquisitionSettings</code></autoref>, and the extension can be used     to determine the file format to create:</p> <ul> <li><code>[.ome].zarr</code> will result in an OME-Zarr at the specified path</li> <li><code>[.ome].tiff</code> will result in an OME-TIFF at the specified path, or,   if multiple positions are acquired, the output path will be treated   as a directory with individual OME-TIFF files for each position.</li> </ul> </li> <li> <p>An <autoref data-zensical-autoref="" domain="py" filepath="/Users/runner/work/pymmcore-plus.github.io/pymmcore-plus.github.io/.repos/pymmcore-plus/src/pymmcore_plus/mda/_runner.py" identifier="ome_writers.AcquisitionSettings" lineno="351" origin="pymmcore_plus.mda.MDARunner.run" role="meth"><code>ome_writers.AcquisitionSettings</code></autoref>, object which allows full   control over many parameters.  See <a href="https://pymmcore-plus.github.io/ome-writers/usage/">ome_writers   documentation</a> for   details.</p> </li> <li> <p>A handler object that implements the <code>DataHandler</code> protocol, currently   meaning it has a <code>frameReady</code> method.  Handlers are called from a   separate thread, so they don't block the acquisition.  See   <code>mda_listeners_connected</code> for more details.</p> </li> </ol> <p>During the course of the sequence, the <code>get_view</code> method can be used to get an array-like view of the current data sink, if the sink supports it.</p> <p>The array shape is taken from <code>events</code> when it is a <code>useq.MDASequence</code>. Any other iterable of events is written as a flat <code>(t, y, x)</code> stack.  See <autoref data-zensical-autoref="" domain="py" filepath="/Users/runner/work/pymmcore-plus.github.io/pymmcore-plus.github.io/.repos/pymmcore-plus/src/pymmcore_plus/mda/_runner.py" identifier="saving-data" lineno="351" origin="pymmcore_plus.mda.MDARunner.run" role="meth">Saving Data</autoref> for details.</p>                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>overwrite</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.mda.MDARunner.run" backlink-type="used-by" identifier="bool" optional="">bool</autoref></code>             </td>             <td>               <div class="doc-md-description">                 <p>Whether to overwrite existing files <em>when output is a <code>str</code> or <code>Path</code></em>. Ignored in all other cases.  Default is False.</p>                </div>             </td>             <td>                   <code>False</code>             </td>           </tr>           <tr class="doc-section-item">             <td>                 <code>dimension_overrides</code>             </td>             <td>                   <code><autoref backlink-anchor="pymmcore_plus.mda.MDARunner.run" backlink-type="used-by" identifier="dict" optional="">dict</autoref>[<autoref backlink-anchor="pymmcore_plus.mda.MDARunner.run" backlink-type="used-by" identifier="str" optional="">str</autoref>, <autoref backlink-anchor="pymmcore_plus.mda.MDARunner.run" backlink-type="used-by" hover="" identifier="pymmcore_plus.mda._runner.DimensionOverride" optional="">DimensionOverride</autoref>] | None</code>             </td>             <td>               <div class="doc-md-description">                 <p>Per-dimension storage overrides, keyed by dimension name. Values are dicts of Dimension fields (&quot;chunk_size&quot;, &quot;shard_size_chunks&quot;) to apply on top of the sequence-derived dimensions. Example: <code>{&quot;t&quot;: {&quot;chunk_size&quot;: 1}, &quot;y&quot;: {&quot;chunk_size&quot;: 256}}</code>.</p>                </div>             </td>             <td>                   <code>None</code>             </td>           </tr>       </tbody>     </table>

#### get\_view

```python
get_view() -> SinkView | None
```

Array-like view of the current data sink, if it exists.

#### get\_output\_handlers

```python
get_output_handlers() -> tuple[SupportsFrameReady, ...]
```

Return the data handlers that are currently connected.

> [!WARNING]
>
> **Deprecated**
>
> There is no full replacement. To look at the data while it is being acquired, use `get_view`.

Output handlers are connected by passing them to the `output` parameter of the `run` method; the run method accepts objects with a `frameReady` method *or* strings representing paths. If a string is passed, a handler will be created internally.

This method returns a tuple of currently connected handlers, including those that were explicitly passed to `run()`, as well as those that were created based on file paths. Internally, handlers are held by weak references, so if you want the handler to persist, you must keep a reference to it. The only guaranteed API that the handler will have is the `frameReady` method, but it could be any user-defined object that implements that method.

Handlers are cleared each time `run()` is called, (but not at the end of the sequence).

Returns:

| Type | Description |
| --- | --- |
| `tuple[SupportsFrameReady, ...]` | Tuple of objects that (minimally) support the `frameReady` method. |

#### seconds\_elapsed

```python
seconds_elapsed() -> float
```

Return the number of seconds since the start of the acquisition.

#### event\_seconds\_elapsed

```python
event_seconds_elapsed() -> float
```

Return the number of seconds on the "event clock".

This is the time since either the start of the acquisition or the last event with `reset_event_timer` set to `True`.

### RunnerStatus

```python
RunnerStatus(
    phase: RunState = IDLE,
    finish_reason: FinishReason | None = None,
    cancel_requested: bool = False,
    pause_requested: bool = False,
)
```

Snapshot of the MDA runner's current state.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `phase` | `RunState` |  |
| `finish_reason` | `FinishReason \| None` |  |
| `cancel_requested` | `bool` |  |
| `pause_requested` | `bool` |  |

#### phase

```python
phase: RunState = RunState.IDLE
```

#### finish\_reason

```python
finish_reason: FinishReason | None = field(default=None)
```

#### cancel\_requested

```python
cancel_requested: bool = False
```

#### pause\_requested

```python
pause_requested: bool = False
```

### RunState

Bases: `StrEnum`

State of the MDA acquisition runner.

#### IDLE

```python
IDLE = 'idle'
```

#### PREPARING

```python
PREPARING = 'preparing'
```

#### WAITING

```python
WAITING = 'waiting'
```

#### ACQUIRING

```python
ACQUIRING = 'acquiring'
```

#### PAUSED

```python
PAUSED = 'paused'
```

#### FINISHING

```python
FINISHING = 'finishing'
```

### SkipEvent

```python
SkipEvent(num_frames: int = 1, reason: str = '')
```

Bases: `Exception`

Raised by an engine's `setup_event` to skip the current event.

The `num_frames` parameter tells the runner how many sink frames to skip (e.g. `len(sequenced_event.events)` for a SequencedEvent).

#### num\_frames

```python
num_frames = num_frames
```

#### reason

```python
reason = reason
```

## Functions

### mda\_listeners\_connected

```python
mda_listeners_connected(
    *listeners: Any,
    mda_events: PMDASignaler | None = ...,
    name_map: dict[str, str] | None = ...,
    asynchronous: Literal[False],
    wait_on_exit: bool = ...,
) -> AbstractContextManager[None]
```

```python
mda_listeners_connected(
    *listeners: Any,
    mda_events: PMDASignaler | None = ...,
    name_map: dict[str, str] | None = ...,
    asynchronous: Literal[True] = ...,
    wait_on_exit: bool = ...,
) -> AbstractContextManager[MDARelayThread]
```

```python
mda_listeners_connected(
    *listeners: Any,
    mda_events: PMDASignaler | None = None,
    name_map: dict[str, str] | None = None,
    asynchronous: bool = True,
    wait_on_exit: bool = True,
) -> Iterator
```

Context in which MDA events are connected to listeners, in a thread by default.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `listeners` | `Any` | Object(s) that has methods matching the name of signals on `mda_events`. (Namely: `sequenceStarted`, `frameReady`, `sequenceFinished`, etc...) | `()` |
| `mda_events` | `PMDASignaler \| None` | The MDA events to connect to. If not provided, the `mda.events` attribute on the global `CMMCorePlus.instance()` will be used, by default None. | `None` |
| `name_map` | `dict[str, str] \| None` | Optionally map signal names to different method names on `listener`. This can be used to connect callbacks with different names. By default, the callbacks names must match the signal names exactly. | `None` |
| `asynchronous` | `bool` | Whether to execute callbacks on `listeners` in another thread. If True, the MDA will proceed without waiting for the callbacks to finish. A deque will collect events and pass them to handlers as they become ready (FIFO), by default True. | `True` |
| `wait_on_exit` | `bool` | Whether to wait for all callbacks on listeners to finish before exiting the context, by default True. | `True` |

## Attributes

### SupportsFrameReady

```python
SupportsFrameReady: TypeAlias = (
    "FrameReady0 | FrameReady1 | FrameReady2 | FrameReady3"
)
```
