# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2026-03-17

### Breaking Changes

- **`NODEFAULT` sentinel** changed from string `"THROWERROR"` to `object()`. Code comparing against the string will break.
- **Migrated from `setup.py` to `pyproject.toml`.**
- **Removed `typing` from dependencies** (stdlib since Python 3.5).

### Fixed

- **Falsy value bug in `__call__`** — `nested("key", 0)` now correctly sets the value instead of treating 0 as "no value". Same for `""`, `False`, `[]`, `{}`.
- **`NODEFAULT` sentinel collision** — using `object()` instead of a string means you can store any string value without collision.
- **`unittest.main()` guard** — tests now work with pytest.

### Added

- **`__repr__`** on all Nested classes for debugging.
- **Type hints and docstrings** on all public methods.
- **`Nested` base class** exported from package.
- **`.gitignore`** with proper Python/IDE patterns.

## [0.2.0] - 2023-01-01

### Added

- `NestedTuple` for immutable nested access.
- `__call__` interface for get/set.
- `__getattr__`/`__setattr__` for dot notation access.
- `default` parameter for `get()` and `__call__`.
- `modify` flag for returning raw values.
- `_get_list_index` for accessing dict keys inside lists.

## [0.1.0] - 2023-01-01

### Added

- Initial release.
- `NestedDict` and `NestedList` with delimiter-based access.
- `get()`, `set()`, `__getitem__`, `__setitem__`.
