# Hardware Autofocus Plan

Ways to describe a hardware-based autofocus plan. An `autofocus_plan` on an [`MDASequence`](<https://pymmcore-plus.github.io/useq-schema/schema/sequence/index.md>) inserts events with a `HardwareAutofocus` action into the sequence (for example, every time the stage position changes).

## useq.AutoFocusPlan

Bases: `FrozenModel`

Base class for hardware autofocus plans.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `autofocus_device_name` | `str \| None` | Optional name of the offset motor device. If `None`, acquisition engines may attempt to set the offset however they see fit (such as using a current or default autofocus device.) |
| `autofocus_motor_offset` | `float \| None` | Before autofocus is performed, the autofocus motor should be moved to this offset, if applicable. (Not all autofocus devices have an offset motor.) If None, the autofocus motor should not be moved. |

### as\_action

```python
as_action() -> HardwareAutofocus
```

Return a `useq.HardwareAutofocus` for this autofocus plan.

### event

```python
event(event: MDAEvent) -> MDAEvent | None
```

Return an autofocus `useq.MDAEvent` if autofocus should be performed.

The z position of the new `useq.MDAEvent` is also updated if a relative zplan is provided since autofocus should be performed on the home z stack position.

### should\_autofocus

```python
should_autofocus(event: MDAEvent) -> bool
```

Method that must be implemented by a subclass.

Should return True if autofocus should be performed (see `useq.AxesBasedAF`).

## useq.AxesBasedAF

Bases: `AutoFocusPlan`

Autofocus plan that performs autofocus when any of the specified axes change.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `axes` | `tuple[str, ...]` | Tuple of axis label to use for hardware autofocus. At every event in which *any* axis in this tuple changes, autofocus will be performed. For example, if `axes` is `('p',)` then autofocus will be performed every time the `p` axis changes (in other words: every time the position is changed). |
| `autofocus_device_name` | `str \| None` | Optional name of the offset motor device. If `None`, acquisition engines may attempt to set the offset however they see fit (such as using a current or default autofocus device.) |
| `autofocus_motor_offset` | `float \| None` | Before autofocus is performed, the autofocus motor should be moved to this offset, if applicable. (Not all autofocus devices have an offset motor.) If None, the autofocus motor should not be moved. |

### should\_autofocus

```python
should_autofocus(event: MDAEvent) -> bool
```

Return `True` if autofocus should be performed at this event.

Will return `True` if any of the axes specified in `axes` have changed from the previous event.
