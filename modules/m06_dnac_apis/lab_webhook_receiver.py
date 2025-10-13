"""
Simple validator for Catalyst Center event webhooks (offline).
"""

REQUIRED_KEYS = {"instanceId", "eventId", "category", "severity", "timestamp"}

def validate_event(payload: dict) -> bool:
    return REQUIRED_KEYS.issubset(payload.keys())
