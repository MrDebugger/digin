"""Using modify=True to get raw values instead of Nested wrappers."""

from digin import NestedDict

data = {
    "users": {
        "alice": {"age": 30, "tags": ["admin", "active"]},
        "bob": {"age": 25, "tags": ["user"]}
    }
}

nd = NestedDict(data, ".")

# Default: returns wrapped NestedDict
wrapped = nd.get("users.alice")
print("Wrapped:", type(wrapped).__name__, wrapped)

# modify=True: returns raw dict
raw = nd.get("users.alice", modify=True)
print("Raw:", type(raw).__name__, raw)

# Useful when you need to pass data to code that expects plain dicts
import json
raw_data = nd.get("users", modify=True)
print("\nJSON:", json.dumps(raw_data, indent=2))

# Modify the raw dict directly (changes propagate to parent)
raw_tags = nd.get("users.alice.tags", modify=True)
raw_tags.append("superuser")
print("Updated tags:", nd.get("users.alice.tags", modify=True))
