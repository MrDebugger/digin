"""Basic usage of digin — dig into nested data."""

from digin import NestedDict

data = {
    "users": {
        "alice": {"age": 30, "role": "admin"},
        "bob": {"age": 25, "role": "user"}
    },
    "settings": {
        "theme": "dark",
        "notifications": True
    }
}

nd = NestedDict(data)

# Read with get()
print("Alice's age:", nd.get("users->alice->age"))
print("Theme:", nd.get("settings->theme"))

# Read with []
print("Bob's role:", nd["users->bob->role"])

# Read with dot notation
print("Notifications:", nd.settings.notifications)

# Read with callable
print("Alice's role:", nd("users->alice->role"))
