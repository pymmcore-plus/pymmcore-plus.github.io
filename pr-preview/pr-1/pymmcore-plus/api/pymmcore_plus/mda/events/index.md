# pymmcore\_plus.mda.events

Signals emitted by the MDA runner (`core.mda.events`) during an acquisition.

**Classes**

| Name | Description |
| --- | --- |
| `MDASignaler` |  |
| `QMDASignaler` |  |

## Classes

### MDASignaler

Bases: `SignalGroup`

#### sequenceStarted

```python
sequenceStarted = Signal(MDASequence, dict)
```

#### sequencePauseToggled

```python
sequencePauseToggled = Signal(bool)
```

#### sequenceCanceled

```python
sequenceCanceled = Signal(MDASequence)
```

#### sequenceFinished

```python
sequenceFinished = Signal(MDASequence)
```

#### frameReady

```python
frameReady = Signal(np.ndarray, MDAEvent, dict)
```

#### awaitingEvent

```python
awaitingEvent = Signal(MDAEvent, float)
```

#### eventStarted

```python
eventStarted = Signal(MDAEvent)
```

### QMDASignaler

Bases: `QObject`

#### sequenceStarted

```python
sequenceStarted = Signal(object, dict)
```

#### sequencePauseToggled

```python
sequencePauseToggled = Signal(bool)
```

#### sequenceCanceled

```python
sequenceCanceled = Signal(object)
```

#### sequenceFinished

```python
sequenceFinished = Signal(object)
```

#### frameReady

```python
frameReady = Signal(object, object, dict)
```

#### awaitingEvent

```python
awaitingEvent = Signal(object, float)
```

#### eventStarted

```python
eventStarted = Signal(object)
```

## Re-exports

These can also be imported from this module, but each is documented under its shortest import path (linked below).

| Name | Description |
| --- | --- |
| `PMDASignaler` | Declares the protocol for all signals that will be emitted from `pymmcore_plus.mda.MDARunner`. |
