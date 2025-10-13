import json
from pathlib import Path

def parse_vmanage_inventory(path="modules/m07_sdwan_apis/sample_inventory.json"):
    data = json.loads(Path(path).read_text())
    rows = []
    for item in data.get("data", []):
        rows.append({
            "uuid": item.get("uuid"),
            "model": item.get("deviceModel"),
            "system_ip": item.get("system-ip"),
            "site_id": item.get("site-id"),
        })
    return rows
