"""
Build model-driven telemetry (MDT) subscription payloads (offline).
"""

def build_mdt_subscription(sensor_path, mode="periodic", period_ms=10000):
    payload = {
        "Cisco-IOS-XE-mdt-cfg:mdt-config-data": {
            "mdt-subscription": [{
                "subscription-id": 101,
                "base": {
                    "stream": "yang-push",
                    "encoding": "encode-kvgpb",
                    "xpath": sensor_path,
                }
            }]
        }
    }
    if mode == "periodic":
        payload["Cisco-IOS-XE-mdt-cfg:mdt-config-data"]["mdt-subscription"][0]["base"]["period"] = period_ms
    elif mode == "on-change":
        payload["Cisco-IOS-XE-mdt-cfg:mdt-config-data"]["mdt-subscription"][0]["base"]["dampening-period"] = period_ms
        payload["Cisco-IOS-XE-mdt-cfg:mdt-config-data"]["mdt-subscription"][0]["base"]["exclude-filter"] = "none"
    else:
        raise ValueError("mode must be 'periodic' or 'on-change'")
    return payload
