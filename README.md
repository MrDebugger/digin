[![PyPI version](https://img.shields.io/pypi/v/digin.svg)](https://pypi.python.org/pypi/digin/)
[![PyPI downloads](https://img.shields.io/pypi/dm/digin.svg)](https://pypi.python.org/pypi/digin/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/digin.svg)](https://pypi.python.org/pypi/digin/)
[![PyPI license](https://img.shields.io/pypi/l/digin.svg)](https://pypi.python.org/pypi/digin/)
[![GitHub stars](https://img.shields.io/github/stars/MrDebugger/digin.svg)](https://github.com/MrDebugger/digin/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/MrDebugger/digin.svg)](https://github.com/MrDebugger/digin/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/MrDebugger/digin.svg)](https://github.com/MrDebugger/digin/commits)

<div align="center">
  <img src="https://raw.githubusercontent.com/MrDebugger/digin/master/assets/logo.svg" alt="digin logo" width="400"/>
</div>

<div align="center">

Access and modify deeply nested data structures using simple delimiter-separated paths.
No more chaining `[]` operators — just `"a->b->0"`.

**Python 3.8+** | Zero dependencies

</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/MrDebugger/digin/master/assets/how-it-works.svg" alt="how it works" width="700"/>
</div>

---

<details open>
<summary><b>Table of Contents</b></summary>
<br>

| Section | Description |
|---------|-------------|
| [Installation](#installation) | How to install |
| [Quick Start](#quick-start) | Basic usage |
| [Access Methods](#access-methods) | get, [], dot notation, callable |
| [Modification](#modification) | set, []=, dot notation, callable |
| [Options](#options) | Delimiters, defaults, modify flag |
| [Classes](#classes) | NestedDict, NestedList, NestedTuple |
| [API Reference](#api-reference) | Full method reference |
| [Contributing](#contributing) | How to contribute |

</details>

---

## Installation

```bash
pip install -U digin
```

---

## Quick Start

```python
from digin import NestedDict

data = {
    "users": {
        "alice": {"age": 30, "hobbies": ["reading", "coding"]},
        "bob": {"age": 25, "hobbies": ["gaming", "cooking"]}
    }
}

nd = NestedDict(data)

# Read nested values
nd.get("users->alice->age")           # 30
nd["users->bob->hobbies->0"]          # 'gaming'
nd.users.alice.hobbies                # NestedList(['reading', 'coding'])

# Modify nested values
nd.set("users->alice->age", 31)
nd["users->bob->hobbies->1"] = "hiking"
nd.users.bob.age = 26
nd("users->alice->hobbies->0", "writing")  # set via callable
```

---

## Access Methods

<details open>
<summary><b>get()</b></summary>
<br>

```python
nd = NestedDict(data)

# String path with delimiter
nd.get("users->alice->age")              # 30

# List/tuple of keys
nd.get(["users", "alice", "age"])         # 30
nd.get(("users", "alice", "hobbies", 0)) # 'reading'

# Integer key (for lists)
nl = NestedList([10, 20, 30])
nl.get(1)                                # 20

# Default value if not found
nd.get("users->charlie->age", default=0) # 0
```

</details>

<details open>
<summary><b>[] bracket notation</b></summary>
<br>

```python
nd["users->alice->age"]          # 30
nd[["users", "bob", "hobbies"]]  # NestedList(['gaming', 'cooking'])
```

</details>

<details>
<summary><b>Dot notation</b></summary>
<br>

```python
nd.users.alice.age       # 30
nd.users.bob.hobbies     # NestedList(['gaming', 'cooking'])
```

Note: dot notation only works with string keys that are valid Python identifiers.

</details>

<details>
<summary><b>Callable</b></summary>
<br>

```python
# Get value
nd("users->alice->age")                    # 30

# Get with default
nd("users->charlie->age", default="N/A")   # 'N/A'

# Set value (pass value as second argument)
nd("users->alice->age", 31)               # sets age to 31
```

</details>

---

## Modification

<details open>
<summary><b>set()</b></summary>
<br>

```python
nd.set("users->alice->age", 31)
nd.set(["users", "bob", "age"], 26)
```

</details>

<details open>
<summary><b>[]= bracket assignment</b></summary>
<br>

```python
nd["users->alice->age"] = 31
nd[["users", "bob", "age"]] = 26
```

</details>

<details>
<summary><b>Dot notation assignment</b></summary>
<br>

```python
nd.users.alice.age = 31
nd.users.bob.age = 26
```

</details>

<details>
<summary><b>Callable assignment</b></summary>
<br>

```python
nd("users->alice->age", 31)
nd("users->bob->hobbies->0", "swimming")
```

Works with falsy values too — `0`, `""`, `False`, `[]`, `{}` are all valid:

```python
nd("users->alice->active", False)   # sets to False, not a get
nd("users->alice->score", 0)        # sets to 0
```

</details>

---

## Options

<details open>
<summary><b>Custom Delimiter</b></summary>
<br>

Default delimiter is `"->"`. Change it in the constructor:

```python
nd = NestedDict(data, delimiter=".")
nd.get("users.alice.age")     # 30
nd["users.bob.hobbies.0"]     # 'gaming'

nd2 = NestedDict(data, delimiter="/")
nd2.get("users/alice/age")    # 30
```

</details>

<details>
<summary><b>Modify Flag</b></summary>
<br>

By default, `get()` wraps dicts/lists/tuples in Nested objects. Use `modify=True` to get the raw value:

```python
# Returns NestedDict (wrapped)
nd.get("users->alice")
# NestedDict({'age': 30, 'hobbies': ['reading', 'coding']})

# Returns plain dict (raw)
nd.get("users->alice", modify=True)
# {'age': 30, 'hobbies': ['reading', 'coding']}
```

</details>

---

## Classes

<details open>
<summary><b>NestedDict</b></summary>
<br>

Extends `dict` with nested path access. Supports all dict methods plus nested get/set:

```python
from digin import NestedDict

nd = NestedDict({"a": {"b": {"c": 1}}})
nd.get("a->b->c")  # 1
nd.keys()           # dict_keys(['a'])
len(nd)             # 1
```

</details>

<details>
<summary><b>NestedList</b></summary>
<br>

Extends `list` with nested path access:

```python
from digin import NestedList

nl = NestedList([{"name": "Alice"}, {"name": "Bob"}])
nl.get("0->name")  # 'Alice'
nl[1]               # {'name': 'Bob'}
len(nl)             # 2
```

</details>

<details>
<summary><b>NestedTuple</b></summary>
<br>

Extends `tuple` with nested path access (read-only):

```python
from digin import NestedTuple

nt = NestedTuple(({"a": 1}, {"b": 2}))
nt.get("0->a")  # 1
nt[0]            # {'a': 1}
```

</details>

---

## API Reference

<details open>
<summary><b>Nested (base class)</b></summary>
<br>

| Method | Description |
|--------|-------------|
| `__init__(data, delimiter="->")` | Wrap data with given delimiter |
| `.get(key, default, modify=False)` | Get value at key path |
| `.set(key, value)` | Set value at key path |
| `.parse(value, modify=False)` | Wrap value in Nested subclass |
| `(key)` | Get value (callable) |
| `(key, value)` | Set value (callable) |
| `[key]` | Get value (bracket) |
| `[key] = value` | Set value (bracket) |
| `.key` | Get value (dot notation) |
| `.key = value` | Set value (dot notation) |

</details>

<details open>
<summary><b>Key formats</b></summary>
<br>

| Format | Example | Description |
|--------|---------|-------------|
| String | `"a->b->0"` | Delimiter-separated path |
| List | `["a", "b", 0]` | List of keys |
| Tuple | `("a", "b", 0)` | Tuple of keys |
| Int | `0` | Direct index |
| None | `None` | Returns self |

</details>

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, versioning guide, and how to submit changes.

<a href="https://github.com/MrDebugger/digin/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=MrDebugger/digin"/>
</a>
