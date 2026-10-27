# Sequence

An `MDASequence` describes a whole experiment: a plan for each axis (time, stage positions, grid, channels and z), and the order in which to iterate them. See [Building Sequences](<https://pymmcore-plus.github.io/useq-schema/guides/sequences/index.md>) for examples.

## useq.MDASequence

Bases: `UseqModel`

A sequence of MDA (Multi-Dimensional Acquisition) events.

This is the core object in the `useq` library, and is used to define a sequence of events to be run on a microscope. The object may be constructed manually, or loaded from a file (JSON or YAML) with `MDASequence.from_file`.

Iterating over the sequence yields `useq.MDAEvent` objects (see Examples).

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `metadata` | `dict[str, Any]` | A dictionary of user metadata to be stored with the sequence. |
| `axis_order` | `tuple[str, ...]` | The order in which the axes are iterated, slowest first. May be given as a string (e.g. `"tpcz"`). Each axis may appear once, and axes that are left out are not iterated (even if they have a plan). The default is `"tpgcz"`. |
| `stage_positions` | `WellPlatePlan \| tuple[AbsolutePosition, ...]` | The stage positions to visit (each with `x`, `y`, `z`, `name`, and `sequence`, all of which are optional), or a `WellPlatePlan`. |
| `grid_plan` | `GridFromEdges \| GridFromPolygon \| GridRowsColumns \| GridWidthHeight \| RandomPoints \| RelativePosition \| None` | The grid plan to follow at each position, or `None`. |
| `channels` | `tuple[Channel, ...]` | The channels to acquire. See `Channel`. |
| `time_plan` | `MultiPhaseTimePlan \| TIntervalDuration \| TIntervalLoops \| TDurationLoops \| None` | The time plan to follow. One of `TIntervalDuration`, `TIntervalLoops`, `TDurationLoops`, `MultiPhaseTimePlan`, or `None` |
| `z_plan` | `ZTopBottom \| ZAboveBelow \| ZRangeAround \| ZAbsolutePositions \| ZRelativePositions \| None` | The z plan to follow. One of `ZTopBottom`, `ZRangeAround`, `ZAboveBelow`, `ZRelativePositions`, `ZAbsolutePositions`, or `None`. Relative plans (`ZRangeAround`, `ZAboveBelow`, `ZRelativePositions`) are added to the `z` of each stage position; if a position has no `z` (or there are no positions), they are relative to `z=0`, *not* to the current focus. |
| `uid` | `UUID` | A read-only unique identifier (uuid version 4) for the sequence. This will be generated, do not set. |
| `autofocus_plan` | `AxesBasedAF \| None` | The hardware autofocus plan to follow. One of `AxesBasedAF` or `None`. |
| `setup` | `MDAEvent \| None` | An optional setup event for the sequence. This event is **not** yielded during iteration; it is intended to be handled separately by the engine. It can be used to set hardware state (e.g. device properties, ROI) before the main acquisition events. By default, `None`. |
| `keep_shutter_open_across` | `tuple[str, ...]` | A tuple of axes `str` across which the illumination shutter should be kept open. Resulting events will have `keep_shutter_open` set to `True` if and only if ALL axes whose indices are changing are in this tuple. For example, if `keep_shutter_open_across=('z',)`, then the shutter would be kept open between events axes {'t': 0, 'z': 0} and {'t': 0, 'z': 1}, but not between {'t': 0, 'z': 0} and {'t': 1, 'z': 0}. |

Examples:

Create a MDASequence

```pycon
>>> from useq import MDASequence
>>> seq = MDASequence(
...     axis_order="tpgcz",
...     time_plan={"interval": 0.1, "loops": 2},
...     stage_positions=[(1, 1, 1)],
...     grid_plan={"rows": 2, "columns": 2},
...     z_plan={"range": 3, "step": 1},
...     channels=[{"config": "DAPI", "exposure": 1}],
... )
```

Look at the sequence to visualize its structure (only fields that were set are shown, and long outputs here are wrapped for readability)

```pycon
>>> seq
MDASequence(
    stage_positions=(AbsolutePosition(x=1.0, y=1.0, z=1.0),),
    grid_plan=GridRowsColumns(rows=2, columns=2),
    channels=(Channel(config='DAPI', exposure=1.0),),
    time_plan=TIntervalLoops(
        interval=datetime.timedelta(microseconds=100000), loops=2
    ),
    z_plan=ZRangeAround(range=3.0, step=1.0),
)
```

Iterate over the events in the sequence

```pycon
>>> events = list(seq)
>>> len(events)
32
>>> events[:2]
[
    MDAEvent(
        index={'t': 0, 'p': 0, 'g': 0, 'c': 0, 'z': 0},
        channel=Channel(config='DAPI'),
        exposure=1.0,
        min_start_time=0.0,
        x_pos=0.5,
        y_pos=1.5,
        z_pos=-0.5,
        reset_event_timer=True,
    ),
    MDAEvent(
        index={'t': 0, 'p': 0, 'g': 0, 'c': 0, 'z': 1},
        channel=Channel(config='DAPI'),
        exposure=1.0,
        min_start_time=0.0,
        x_pos=0.5,
        y_pos=1.5,
        z_pos=0.5,
    ),
]
```

Print the sequence as yaml

```pycon
>>> print(seq.yaml())
axis_order:
- t
- p
- g
- c
- z
channels:
- config: DAPI
  exposure: 1.0
grid_plan:
  columns: 2
  rows: 2
stage_positions:
- x: 1.0
  y: 1.0
  z: 1.0
time_plan:
  interval: 0.1
  loops: 2
z_plan:
  range: 3.0
  step: 1.0
```

Create a sequence with a setup event

```pycon
>>> from useq import MDASequence, MDAEvent
>>> seq = MDASequence(
...     setup=MDAEvent(
...         properties=[("Camera", "Binning", "2")],
...         roi=(0, 0, 512, 512),
...     ),
...     channels=["GFP"],
...     time_plan={"interval": 1, "loops": 5},
... )
```

The setup event is accessible via `seq.setup` but is not yielded during iteration (it should be handled separately by implementing engines):

```pycon
>>> seq.setup.action.name
'setup'
>>> seq.setup.roi
CameraROI(offset_x=0, offset_y=0, width=512, height=512)
```

Print setup sequence as yaml

```pycon
>>> print(seq.yaml())
channels:
- config: GFP
setup:
  action:
    name: setup
  properties:
  - - Camera
    - Binning
    - '2'
  roi:
    height: 512
    offset_x: 0
    offset_y: 0
    width: 512
time_plan:
  interval: 1.0
  loops: 5
```

### metadata

```python
metadata: dict[str, Any] = Field(default_factory=dict)
```

### axis\_order

```python
axis_order: tuple[str, ...] = AXES
```

### stage\_positions

```python
stage_positions: WellPlatePlan | tuple[Position, ...] = Field(
    default_factory=tuple, union_mode="left_to_right"
)
```

### grid\_plan

```python
grid_plan: MultiPointPlan | None = Field(
    default=None, union_mode="left_to_right"
)
```

### channels

```python
channels: tuple[Channel, ...] = Field(default_factory=tuple)
```

### time\_plan

```python
time_plan: AnyTimePlan | None = None
```

### z\_plan

```python
z_plan: AnyZPlan | None = None
```

### autofocus\_plan

```python
autofocus_plan: AnyAutofocusPlan | None = None
```

### setup

```python
setup: MDAEvent | None = None
```

### keep\_shutter\_open\_across

```python
keep_shutter_open_across: tuple[str, ...] = Field(default_factory=tuple)
```

### uid

```python
uid: UUID
```

A unique identifier for this sequence.

### shape

```python
shape: tuple[int, ...]
```

Return the shape of this sequence.

> [!NOTE]
>
> This doesn't account for jagged arrays, like channels that exclude z stacks or skip timepoints.

### sizes

```python
sizes: Mapping[str, int]
```

Mapping of axis name to size of that axis.

### used\_axes

```python
used_axes: str
```

Single letter string of axes used in this sequence, e.g. `ztc`.

### iter\_axis

```python
iter_axis(axis: str) -> Iterator[Channel | float | PositionBase]
```

Iterate over the positions or items of a given axis.

### iter\_events

```python
iter_events() -> Iterator[MDAEvent]
```

Iterate over all events in the MDA sequence.

See source of `iter_sequence` for details on how events are constructed and yielded.

Yields:

| Type | Description |
| --- | --- |
| `MDAEvent` | Each event in the MDA sequence. |

### estimate\_duration

```python
estimate_duration() -> TimeEstimate
```

Estimate duration and other timing issues of an MDASequence.

Notable mis-estimations may include:

- when the time interval is shorter than the time it takes to acquire the data and any of the channels have `acquire_every` \> 1
- when channel exposure times are omitted. In this case, we assume 1ms exposure.

Returns:

<table>       <thead>         <tr>           <th>Type</th>           <th>Description</th>         </tr>       </thead>       <tbody>           <tr class="doc-section-item">             <td>                   <code><autoref backlink-anchor="useq.MDASequence.estimate_duration" backlink-type="returned-by" hover="" identifier="useq._utils.TimeEstimate" optional="">TimeEstimate</autoref></code>             </td>             <td>               <div class="doc-md-description">                 <p>A named 3-tuple with the following fields:</p> <ul> <li><code>total_duration</code> (<code>float</code>): Estimated total duration of the experiment,   in seconds.</li> <li><code>per_t_duration</code> (<code>float</code>): Estimated duration of a single timepoint, in   seconds.</li> <li><code>time_interval_exceeded</code> (<code>bool</code>): Whether the time interval between   timepoints is shorter than the time it takes to acquire the data.</li> </ul>                </div>             </td>           </tr>       </tbody>     </table>

## How sequences are iterated

Iterating an `MDASequence` yields `MDAEvent` objects. The logic lives in `iter_sequence`, an implementation detail (it isn't part of the schema itself) that is shown here for reference:

### iter\_sequence

```python
iter_sequence(sequence)
```

Iterate over all events in the MDA sequence.

> [!NOTE]
>
> This method will usually be used via `useq.MDASequence.iter_events`, or by simply iterating over the sequence.

This does the job of iterating over all the frames in the MDA sequence, handling the logic of merging all z plans in channels and stage positions defined in the plans for each axis.

This is the most "logic heavy" part of `useq-schema` (the rest of which is almost entirely declarative). This iterator is useful for consuming `MDASequence` objects in a python runtime, but it isn't considered a "core" part of the schema.

The `sequence.setup` event is not yielded during iteration. It is intended to be handled separately by an engine.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `sequence` | `MDASequence` | The sequence to iterate over. | *required* |

Yields:

| Type | Description |
| --- | --- |
| `MDAEvent` | Each event in the MDA sequence. |
