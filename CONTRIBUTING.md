# Contributing to nested_inside

We appreciate all contributions! Here's how to get involved.

## Bug Fixes

If you're fixing a bug, please go ahead and submit a pull request without prior discussion.

Include:
- A test that reproduces the bug
- A clear commit message explaining what was broken and why

## New Features

If you plan to contribute new features, **please first open an issue** and discuss the feature with us.

## Development Setup

```bash
git clone https://github.com/MrDebugger/nested_inside.git
cd nested_inside
pip install -e .
python3 -m pytest tests/tests.py -v
```

## Project Structure

```
nested_inside/
├── __init__.py    # Exports: Nested, NestedDict, NestedList, NestedTuple
└── nests.py       # All classes and logic
```

## Testing

All changes must include tests:

```bash
python3 -m pytest tests/tests.py -v
```

## Versioning

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** (x.0.0): Breaking changes to public API or behavior
- **MINOR** (0.x.0): New features, backward-compatible
- **PATCH** (0.0.x): Bug fixes

### Public API

- `NestedDict`, `NestedList`, `NestedTuple`, `Nested` classes
- `get()`, `set()`, `parse()` methods
- `__getitem__`, `__setitem__`, `__getattr__`, `__setattr__`, `__call__` behavior
- Delimiter-based key path format

## Pull Request Process

1. Create a feature branch from `master`
2. Make your changes with tests
3. Run the full test suite
4. Submit a PR with a clear description

## Contributors

<a href="https://github.com/MrDebugger/nested_inside/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=MrDebugger/nested_inside"/>
</a>
