# pymmcore\_plus.mda.events

Classes:

| Name | Description |
| --- | --- |
| `MDASignaler` |  |
| `QMDASignaler` |  |

Functions:

| Name | Description |
| --- | --- |
| `_get_auto_MDA_callback_class` |  |

## MDASignaler

Bases: `SignalGroup`

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `sequenceStarted` |  |  |
| `sequencePauseToggled` |  |  |
| `sequenceCanceled` |  |  |
| `sequenceFinished` |  |  |
| `frameReady` |  |  |
| `awaitingEvent` |  |  |
| `eventStarted` |  |  |

### sequenceStarted

```python
sequenceStarted = Signal(MDASequence, dict)
```

### sequencePauseToggled

```python
sequencePauseToggled = Signal(bool)
```

### sequenceCanceled

```python
sequenceCanceled = Signal(MDASequence)
```

### sequenceFinished

```python
sequenceFinished = Signal(MDASequence)
```

### frameReady

```python
frameReady = Signal(np.ndarray, MDAEvent, dict)
```

### awaitingEvent

```python
awaitingEvent = Signal(MDAEvent, float)
```

### eventStarted

```python
eventStarted = Signal(MDAEvent)
```

## QMDASignaler

Bases: `QObject`

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `sequenceStarted` |  |  |
| `sequencePauseToggled` |  |  |
| `sequenceCanceled` |  |  |
| `sequenceFinished` |  |  |
| `frameReady` |  |  |
| `awaitingEvent` |  |  |
| `eventStarted` |  |  |

### sequenceStarted

```python
sequenceStarted = Signal(object, dict)
```

### sequencePauseToggled

```python
sequencePauseToggled = Signal(bool)
```

### sequenceCanceled

```python
sequenceCanceled = Signal(object)
```

### sequenceFinished

```python
sequenceFinished = Signal(object)
```

### frameReady

```python
frameReady = Signal(object, object, dict)
```

### awaitingEvent

```python
awaitingEvent = Signal(object, float)
```

### eventStarted

```python
eventStarted = Signal(object)
```

## \_get\_auto\_MDA\_callback\_class

```python
_get_auto_MDA_callback_class() -> type[PMDASignaler]
```

## Re-exports

These names can be imported from this module, but are documented at their top-level location.

| Name | Description |
| --- | --- |
| `PMDASignaler` | Declares the protocol for all signals that will be emitted from `pymmcore_plus.mda.MDARunner`. |
