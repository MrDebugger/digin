"""All supported key formats."""

from digin import NestedDict

data = {
    "a": {
        "b": {
            "c": [10, 20, 30]
        }
    }
}

nd = NestedDict(data, ".")

# String path (delimiter-separated)
print("String path:", nd.get("a.b.c.1"))

# List of keys
print("List keys:", nd.get(["a", "b", "c", 1]))

# Tuple of keys
print("Tuple keys:", nd.get(("a", "b", "c", 2)))

# Integer key (direct index for lists/dicts with int keys)
from digin import NestedList
nl = NestedList([100, 200, 300])
print("Int key:", nl.get(1))

# None key (returns self)
print("None key:", type(nd.get(None)).__name__)

# Mixed: string indices in list paths
print("String index:", nd.get("a.b.c.0"))
