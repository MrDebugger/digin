"""Handling missing keys with defaults."""

from digin import NestedDict

data = {
    "user": {
        "name": "Alice",
        "preferences": {"theme": "dark"}
    }
}

nd = NestedDict(data, ".")

# Key exists — returns value
print("Name:", nd.get("user.name"))

# Key missing — with default
print("Email:", nd.get("user.email", default="not set"))
print("Language:", nd.get("user.preferences.language", default="en"))

# Callable with default
print("Avatar:", nd("user.avatar", default="/default.png"))

# Falsy defaults work correctly
print("Score:", nd.get("user.score", default=0))
print("Active:", nd.get("user.active", default=False))
print("Bio:", nd.get("user.bio", default=""))
print("Tags:", nd.get("user.tags", default=None))

# Without default — raises KeyError
try:
    nd.get("user.nonexistent")
except KeyError as e:
    print(f"\nKeyError raised: {e}")

# IndexError for out-of-range list access
data2 = {"items": [1, 2, 3]}
nd2 = NestedDict(data2, ".")
try:
    nd2.get("items.10")
except IndexError:
    print("IndexError raised for items.10")
