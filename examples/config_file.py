"""Real-world example: working with config files."""

import json
from digin import NestedDict

# Simulated config loaded from JSON/YAML
config = {
    "app": {
        "name": "MyApp",
        "version": "2.1.0",
        "debug": False
    },
    "database": {
        "primary": {
            "host": "db.example.com",
            "port": 5432,
            "credentials": {
                "username": "admin",
                "password": "secret123"
            }
        },
        "replica": {
            "host": "replica.example.com",
            "port": 5432
        }
    },
    "features": {
        "dark_mode": True,
        "beta": ["feature_a", "feature_b"],
        "limits": {"max_upload_mb": 50, "max_users": 1000}
    }
}

cfg = NestedDict(config, ".")

# Read config values
print("App:", cfg.get("app.name"), cfg.get("app.version"))
print("DB host:", cfg.get("database.primary.host"))
print("DB user:", cfg.get("database.primary.credentials.username"))
print("Max upload:", cfg.get("features.limits.max_upload_mb"), "MB")

# Override for environment
cfg.set("database.primary.host", "localhost")
cfg.set("app.debug", True)
cfg("features.limits.max_users", 10)

print("\nAfter overrides:")
print("DB host:", cfg.get("database.primary.host"))
print("Debug:", cfg.get("app.debug"))
print("Max users:", cfg.get("features.limits.max_users"))

# Check beta features
beta = cfg.get("features.beta", modify=True)
print("\nBeta features:", beta)
beta.append("feature_c")
print("Updated beta:", cfg.get("features.beta", modify=True))

# Safe access for optional config
print("\nRedis:", cfg.get("cache.redis.host", default="not configured"))
