"""Working with nested lists."""

from digin import NestedList, NestedDict

# List of records
users = [
    {"name": "Alice", "scores": [95, 87, 92]},
    {"name": "Bob", "scores": [78, 85, 90]},
    {"name": "Charlie", "scores": [88, 91, 76]}
]

nl = NestedList(users, ".")

# Access by index + key
print("First user:", nl.get("0.name"))
print("Bob's second score:", nl.get("1.scores.1"))
print("Charlie's last score:", nl.get("2.scores.2"))

# Modify
nl("1.scores.0", 80)
print("Updated Bob's first score:", nl.get("1.scores.0"))

# Dict containing lists
data = {
    "team": {
        "members": ["Alice", "Bob", "Charlie"],
        "scores": [100, 200, 300]
    }
}

nd = NestedDict(data, ".")
print("\nSecond member:", nd.get("team.members.1"))
print("Third score:", nd.get("team.scores.2"))

# Modify list element inside dict
nd["team.members.2"] = "Dave"
print("Updated member:", nd.get("team.members.2"))
