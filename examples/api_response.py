"""Real-world example: parsing an API response."""

from digin import NestedDict

# Simulated API response
response = {
    "status": 200,
    "data": {
        "user": {
            "id": 12345,
            "profile": {
                "name": "Alice Johnson",
                "email": "alice@example.com",
                "address": {
                    "street": "123 Main St",
                    "city": "Springfield",
                    "state": "IL",
                    "zip": "62701"
                }
            },
            "orders": [
                {"id": 1001, "total": 59.99, "items": [
                    {"name": "Widget", "qty": 2},
                    {"name": "Gadget", "qty": 1}
                ]},
                {"id": 1002, "total": 129.50, "items": [
                    {"name": "Thingamajig", "qty": 3}
                ]}
            ]
        }
    },
    "meta": {
        "request_id": "abc-123",
        "timestamp": "2026-03-17T12:00:00Z"
    }
}

r = NestedDict(response, ".")

# Extract deeply nested values easily
print("User:", r.get("data.user.profile.name"))
print("City:", r.get("data.user.profile.address.city"))
print("First order total:", r.get("data.user.orders.0.total"))
print("Second order item:", r.get("data.user.orders.1.items.0.name"))
print("Request ID:", r.get("meta.request_id"))

# Safely handle missing fields
print("Phone:", r.get("data.user.profile.phone", default="N/A"))
print("Notes:", r.get("data.user.notes", default=[]))

# Dot notation for quick access
print("\nVia dot notation:")
print("Email:", r.data.user.profile.email)
print("Zip:", r.data.user.profile.address.zip)
print("Status:", r.status)
