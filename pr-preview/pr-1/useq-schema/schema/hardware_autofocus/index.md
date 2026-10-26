# Hardware Autofocus Plan

Ways to describe a hardware-based autofocus plan.

## useq.AutoFocusPlan

Bases: `FrozenModel`

Base class for hardware autofocus plans.

Attributes:

| Name | Type | Description |
| --- | --- | --- |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `autofocus_device_name` | `str \| None` |  | `None` |
| `autofocus_motor_offset` | `float \| None` |  | `None` |

Methods:

| Name | Description |
| --- | --- |
| `as_action` | Return a `useq.HardwareAutofocus` for this autofocus plan. |
| `event` | Return an autofocus `useq.MDAEvent` if autofocus should be performed. |
| `should_autofocus` | Method that must be implemented by a subclass. |

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

The z position of the new `useq.MDAEvent` is also updated if a relative zplan is provided since autofocus shuld be performed on the home z stack position.

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

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `autofocus_device_name` | `str \| None` |  | `None` |
| `autofocus_motor_offset` | `float \| None` |  | `None` |
| `axes` | `tuple[str, ...]` |  | *required* |

Methods:

| Name | Description |
| --- | --- |
| `should_autofocus` | Return `True` if autofocus should be performed at this event. |

### should\_autofocus

```python
should_autofocus(event: MDAEvent) -> bool
```

Return `True` if autofocus should be performed at this event.

Will return `True` if any of the axes specified in `axes` have changed from the previous event.
