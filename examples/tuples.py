"""Read-only access with NestedTuple."""

from digin import NestedTuple

# Immutable nested data
config = (
    {"env": "production", "debug": False},
    {"env": "staging", "debug": True},
    {"env": "development", "debug": True}
)

nt = NestedTuple(config, ".")

# Read access works
print("First env:", nt.get("0.env"))
print("Second debug:", nt.get("1.debug"))
print("Third env:", nt("2.env"))

# Index access
print("Raw first:", nt[0])

# Inner tuples stay wrapped
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

nt2 = NestedTuple(matrix, ".")
print("\nCenter value:", nt2.get("1.1"))
print("Corner:", nt2.get("2.2"))
