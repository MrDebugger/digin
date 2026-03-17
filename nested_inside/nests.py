from typing import Union, Any

_NODEFAULT = object()  # Unique sentinel — can't collide with any stored value


class Nested:
    """Base class for nested data access using delimiter-separated key paths.

    Wraps a data structure (dict, list, tuple) and allows access/modification
    using paths like "a->b->0" instead of chaining [] operators.
    """

    def __init__(self, data: Any, delimiter: str = "->"):
        self._parent = None
        super().__init__(data)
        self._delimiter = delimiter

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"{cls}({super().__repr__()}, delimiter={self._delimiter!r})"

    def parse(self, value: Any, modify: bool = False) -> Any:
        """Wrap value in a Nested subclass unless modify=True.

        Args:
            value: The value to potentially wrap.
            modify: If True, return raw value. If False, wrap in NestedDict/List/Tuple.
        """
        if modify:
            return value
        if isinstance(value, dict):
            value = NestedDict(value, self._delimiter)
            value._parent = self
        elif isinstance(value, list):
            value = NestedList(value, self._delimiter)
            value._parent = self
        elif isinstance(value, tuple):
            value = NestedTuple(value, self._delimiter)
            value._parent = self
        return value

    def get(self, key: Union[int, str, list, tuple, None] = None,
            default: Any = _NODEFAULT, modify: bool = False) -> Any:
        """Retrieve a value at the specified key path.

        Args:
            key: Delimiter-separated string, list/tuple of keys, int index, or None for self.
            default: Value to return if key not found. Raises if not provided.
            modify: If True, return raw value instead of Nested wrapper.
        """
        if key is None:
            return self.parse(self, modify)
        self._last_key = key
        try:
            if isinstance(key, (str, list, tuple)):
                keys = key.split(self._delimiter) if isinstance(key, str) else key
                value = self
                for k in keys:
                    if isinstance(value, (list, tuple)):
                        if isinstance(k, int) or (isinstance(k, str) and k.lstrip('-').isdigit()):
                            value = value[int(k)]
                        else:
                            value = value[self._get_list_index(k, value)]
                    else:
                        if isinstance(k, str) and k.isdigit() and int(k) in value.keys():
                            value = value[int(k)]
                        else:
                            value = value[k]
            elif isinstance(key, int):
                value = self[key]
            else:
                raise SyntaxError(f"Key of type {key.__class__.__name__} is not supported")
        except (AttributeError, IndexError, KeyError) as e:
            if default is _NODEFAULT:
                raise e
            return default

        return self.parse(value, modify)

    def set(self, key: Union[int, str, list, tuple], value: Any) -> None:
        """Set a value at the specified key path.

        Args:
            key: Delimiter-separated string, list/tuple of keys, or int index.
            value: The value to set.
        """
        self.__setitem__(key, value)

    def _get_list_index(self, key: Union[int, str], lst: list) -> int:
        """Find the index of a dict containing key in a list of dicts."""
        for i, d in enumerate(lst):
            if isinstance(d, dict) and key in d:
                return i
        raise KeyError(key)

    def __call__(self, key: Any = None, value: Any = _NODEFAULT,
                 default: Any = _NODEFAULT) -> Any:
        """Call instance as function for get/set.

        With key only: get value.
        With key and value: set value.
        Without arguments: return self.
        """
        if value is not _NODEFAULT:
            return self.set(key, value)
        return self.get(key, default)

    def __getitem__(self, key: Union[str, int, list, tuple]) -> Any:
        if (isinstance(key, str) and self._delimiter in key) or isinstance(key, (list, tuple)):
            return self.get(key)
        return super().__getitem__(key)

    def __setitem__(self, key: Union[str, int, list, tuple], value: Any) -> None:
        if (isinstance(key, str) and self._delimiter in key) or isinstance(key, (list, tuple)):
            keys = key.split(self._delimiter) if isinstance(key, str) else key
            parent_key = self._delimiter.join(str(k) for k in keys[:-1]) if len(keys) > 1 else None
            d = self.get(parent_key, modify=True) if parent_key else self
            last_key = keys[-1]
            if isinstance(d, (list, tuple)) and isinstance(last_key, str) and last_key.lstrip('-').isdigit():
                d[int(last_key)] = value
            else:
                d[last_key] = value
        else:
            super().__setitem__(key, value)

    def __getattr__(self, key: str) -> Any:
        try:
            return self.get(key)
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key: str, value: Any) -> None:
        if key.startswith('_'):
            super().__setattr__(key, value)
        elif self._parent is not None and hasattr(self._parent, '_last_key') and self._parent._last_key:
            if isinstance(self._parent._last_key, str):
                full_key = self._delimiter.join([self._parent._last_key, key])
            else:
                full_key = self._parent._last_key
            self._parent[full_key] = value
        else:
            self[key] = value


class NestedDict(Nested, dict):
    """A dict with nested access via delimiter-separated key paths."""
    pass


class NestedList(Nested, list):
    """A list with nested access via delimiter-separated key paths."""
    pass


class NestedTuple(Nested, tuple):
    """A tuple with nested access via delimiter-separated key paths (read-only)."""
    pass
