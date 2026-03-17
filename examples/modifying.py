"""All ways to modify nested data."""

from digin import NestedDict

data = {
    "config": {
        "db": {"host": "localhost", "port": 5432},
        "cache": {"ttl": 300, "enabled": True}
    }
}

nd = NestedDict(data, ".")

# set()
nd.set("config.db.host", "prod-db.example.com")
print("After set():", nd.get("config.db.host"))

# [] assignment
nd["config.db.port"] = 3306
print("After []=:", nd.get("config.db.port"))

# dot notation
nd.config.cache.ttl = 600
print("After dot=:", nd.get("config.cache.ttl"))

# callable
nd("config.cache.enabled", False)
print("After call():", nd.get("config.cache.enabled"))

# list key
nd[["config", "db", "host"]] = "staging-db.example.com"
print("After list key:", nd.get("config.db.host"))

print("\nFinal state:")
print(nd)
