# pymmcore\_plus.metadata.serialize

Functions:

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

Keys:

| Name | Type | Description |
| --- | --- | --- |
| `json_loads` |  |  |

## json\_loads

```python
json_loads = std_json_loads
```

## encode\_hook

```python
encode_hook(obj: Any, raises: bool = True) -> Any
```

Hook to encode objects that are not JSON serializable.

## msgspec\_json\_dumps

```python
msgspec_json_dumps(obj: Any, *, indent: int | None = None) -> bytes
```

Serialize object to bytes.

## msgspec\_json\_loads

```python
msgspec_json_loads(s: bytes | str) -> Any
```

Deserialize bytes to object.

## msgspec\_to\_builtins

```python
msgspec_to_builtins(obj: Any) -> Any
```

Convert object to built-in types.

## msgspec\_to\_schema

```python
msgspec_to_schema(type: Any) -> Any
```

Generate JSON schema for a given type.

## schema\_hook

```python
schema_hook(obj: type) -> dict[str, Any]
```

Hook to convert objects to schema.

## std\_json\_dumps

```python
std_json_dumps(obj: Any, *, indent: int | None = None) -> bytes
```

Serialize object to bytes.

## std\_json\_loads

```python
std_json_loads(s: bytes | str) -> Any
```

Deserialize bytes to object.

## std\_to\_builtins

```python
std_to_builtins(obj: Any) -> Any
```

Convert object to built-in types.

## Re-exports

These names can be imported from this module, but are documented at their top-level location.

| Name | Description |
| --- | --- |
| `json_dumps` |  |
| `to_builtins` |  |
