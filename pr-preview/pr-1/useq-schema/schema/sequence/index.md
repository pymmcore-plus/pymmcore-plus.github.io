# Sequence

## useq.MDASequence

Bases: `UseqModel`

A sequence of MDA (Multi-Dimensional Acquisition) events.

This is the core object in the `useq` library, and is used define a sequence of events to be run on a microscope. It object may be constructed manually, or from file (e.g. json or yaml).

The object itself acts as an iterator for `useq.MDAEvent` objects:

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `uid` | `UUID` | A read-only unique identifier (uuid version 4) for the sequence. This will be generated, do not set. |

Examples:

Create a MDASequence

```pycon
>>> from useq import MDASequence, Position, Channel, TIntervalDuration
>>> seq = MDASequence(
...     axis_order="tpgcz",
...     time_plan={"interval": 0.1, "loops": 2},
...     stage_positions=[(1, 1, 1)],
...     grid_plan={"rows": 2, "columns": 2},
...     z_plan={"range": 3, "step": 1},
...     channels=[{"config": "DAPI", "exposure": 1}]
... )
```

Print the sequence to visualize its structure

```pycon
>>> print(seq)
... MDASequence(
...     stage_positions=(Position(x=1.0, y=1.0, z=1.0, name=None),),
...     grid_plan=GridRowsColumns(
...         fov_width=None,
...         fov_height=None,
...         overlap=(0.0, 0.0),
...         mode=<OrderMode.row_wise_snake: 'row_wise_snake'>,
...         rows=2,
...         columns=2,
...         relative_to=<RelativeTo.center: 'center'>
...     ),
...     channels=(
...         Channel(
...             config='DAPI',
...             group='Channel',
...             exposure=1.0,
...             do_stack=True,
...             z_offset=0.0,
...             acquire_every=1,
...             camera=None
...         ),
...     ),
...     time_plan=TIntervalLoops(
...         prioritize_duration=False,
...         interval=datetime.timedelta(microseconds=100000),
...         loops=2
...     ),
...     z_plan=ZRangeAround(go_up=True, range=3.0, step=1.0)
... )
```

Iterate over the events in the sequence

```pycon
>>> print(list(seq))
... [
...     MDAEvent(
...         index=mappingproxy({'t': 0, 'p': 0, 'g': 0, 'c': 0, 'z': 0}),
...         channel=Channel(config='DAPI'),
...         exposure=1.0,
...         min_start_time=0.0,
...         x_pos=0.5,
...         y_pos=1.5,
...         z_pos=-0.5
...     ),
...     MDAEvent(
...         index=mappingproxy({'t': 0, 'p': 0, 'g': 0, 'c': 0, 'z': 1}),
...         channel=Channel(config='DAPI'),
...         exposure=1.0,
...         min_start_time=0.0,
...         x_pos=0.5,
...         y_pos=1.5,
...         z_pos=0.5
...     ),
...     ...
... ]
```

Print the sequence as yaml

```pycon
>>> print(seq.yaml())
```

```yaml
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
   interval: '0:00:00.100000'
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

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `metadata` | `dict[str, Any]` | dict() -\> new empty dictionary dict(mapping) -\> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -\> new dictionary initialized as if via: d = {} for k, v in iterable: d\[k\] = v dict(\*\*kwargs) -\> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) | `<class 'dict'>` |
| `axis_order` | `tuple[str, ...]` |  | `(<Axis.TIME: 't'>, <Axis.POSITION: 'p'>, <Axis.GRID: 'g'>, <Axis.CHANNEL: 'c'>, <Axis.Z: 'z'>)` |
| `stage_positions` | `WellPlatePlan \| tuple[AbsolutePosition, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |
| `grid_plan` | `GridFromEdges \| GridFromPolygon \| GridRowsColumns \| GridWidthHeight \| RandomPoints \| RelativePosition \| None` |  | `None` |
| `channels` | `tuple[Channel, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |
| `time_plan` | `MultiPhaseTimePlan \| TIntervalDuration \| TIntervalLoops \| TDurationLoops \| None` |  | `None` |
| `z_plan` | `ZTopBottom \| ZAboveBelow \| ZRangeAround \| ZAbsolutePositions \| ZRelativePositions \| None` |  | `None` |
| `autofocus_plan` | `AxesBasedAF \| None` |  | `None` |
| `setup` | `MDAEvent \| None` |  | `None` |
| `keep_shutter_open_across` | `tuple[str, ...]` | Built-in immutable sequence.<br><br>If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.<br><br>If the argument is a tuple, the return value is the same object. | `<dynamic>` |

Methods:

| Name | Description |
| --- | --- |
| `iter_axis` | Iterate over the positions or items of a given axis. |
| `iter_events` | Iterate over all events in the MDA sequence. |
| `estimate_duration` | Estimate duration and other timing issues of an MDASequence. |

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

Notable mis-estimations may include: - when the time interval is shorter than the time it takes to acquire the data and any of the channels have `acquire_every` \> 1 - when channel exposure times are omitted. In this case, we assume 1ms exposure.

Returns:

| Type | Description |
| --- | --- |
| `TimeEstimate` | A named 3-tuple with the following fields: - total\_duration: float Estimated total duration of the experiment, in seconds. - per\_t\_duration: float Estimated duration of a single timepoint, in seconds. - time\_interval\_exceeded: bool Whether the time interval between timepoints is shorter than the time it takes to acquire the data |

## How sequences are iterated

Iterating an `MDASequence` yields `MDAEvent` objects. The logic lives in `iter_sequence`, which is shown here for reference:

### useq.\_iter\_sequence.iter\_sequence

```python
iter_sequence(sequence)
```

Iterate over all events in the MDA sequence.'.

> [!NOTE]
>
> This method will usually be used via `useq.MDASequence.iter_events`, or by simply iterating over the sequence.

This does the job of iterating over all the frames in the MDA sequence, handling the logic of merging all z plans in channels and stage positions defined in the plans for each axis.

The is the most "logic heavy" part of `useq-schema` (the rest of which is almost entirely declarative). This iterator is useful for consuming `MDASequence` objects in a python runtime, but it isn't considered a "core" part of the schema.

The `sequence.setup` event is not yielded during iteration. It is intended to be handled separately by an engine.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `sequence` | `MDASequence` | The sequence to iterate over. | *required* |

Yields:

| Type | Description |
| --- | --- |
| `MDAEvent` | Each event in the MDA sequence. |
