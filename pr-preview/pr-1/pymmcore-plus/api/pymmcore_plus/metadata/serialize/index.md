# pymmcore\_plus.metadata.serialize

**Functions**

| Name | Description |
| --- | --- |
| `encode_hook` | Hook to encode objects that are not JSON serializable. |
| `msgspec_json_dumps` | Serialize object to bytes. |
| `msgspec_json_loads` | Deserialize bytes to object. |
| `msgspec_to_builtins` | Convert object to built-in types. |
| `msgspec_to_schema` | Generate JSON schema for a given type. |
| `schema_hook` | Hook to convert objects to schema. |
| `std_json_dumps` | Serialize object to bytes. |
| `std_json_loads` | Deserialize bytes to object. |
| `std_to_builtins` | Convert object to built-in types. |

**Attributes**

| Name | Description |
| --- | --- |
| `json_loads` | Deserialize JSON bytes (or a string) to Python objects. |

## Functions

### encode\_hook

```python
encode_hook(obj: Any, raises: bool = True) -> Any
```

Hook to encode objects that are not JSON serializable.

### schema\_hook

```python
schema_hook(obj: type) -> dict[str, Any]
```

Hook to convert objects to schema.

### msgspec\_json\_dumps

```python
msgspec_json_dumps(obj: Any, *, indent: int | None = None) -> bytes
```

Serialize object to bytes.

### msgspec\_json\_loads

```python
msgspec_json_loads(s: bytes | str) -> Any
```

Deserialize bytes to object.

### msgspec\_to\_builtins

```python
msgspec_to_builtins(obj: Any) -> Any
```

Convert object to built-in types.

### msgspec\_to\_schema

```python
msgspec_to_schema(type: Any) -> Any
```

Generate JSON schema for a given type.

### std\_json\_dumps

```python
std_json_dumps(obj: Any, *, indent: int | None = None) -> bytes
```

Serialize object to bytes.

### std\_json\_loads

```python
std_json_loads(s: bytes | str) -> Any
```

Deserialize bytes to object.

### std\_to\_builtins

```python
std_to_builtins(obj: Any) -> Any
```

Convert object to built-in types.

## Attributes

### json\_loads

```python
json_loads = std_json_loads
```

Deserialize JSON bytes (or a string) to Python objects.

## Re-exports

These can also be imported from this module, but each is documented under its shortest import path (linked below).

| Name | Description |
| --- | --- |
| `json_dumps` | Serialize `obj` (e.g. a metadata dict) to JSON bytes. |
| `to_builtins` | Convert `obj` (e.g. a metadata dict) to builtin Python types. |
