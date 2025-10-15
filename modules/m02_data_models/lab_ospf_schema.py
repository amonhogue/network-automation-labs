# modules/m02_data_models/lab_ospf_schema.py
from typing import Any, Dict, List

REQUIRED_TOP_KEYS = ["ospf"]
REQUIRED_OSPF_KEYS = ["process_id", "areas", "interfaces"]
REQUIRED_AREA_KEYS = ["area_id", "networks"]
REQUIRED_IF_KEYS = ["name", "area_id", "network_type"]

def validate_ospf_schema(data: Dict[str, Any]) -> List[str]:
    """
    Minimal OSPF schema validator (YANG-ish): returns list of problems (empty = OK)
    Expected shape:
      {
        "ospf": {
          "process_id": "1",
          "areas": [{"area_id":"0.0.0.0","networks":["10.0.0.0/8"]}],
          "interfaces": [{"name":"Gig0/0","area_id":"0.0.0.0","network_type":"point-to-point"}]
        }
      }
    """
    problems: List[str] = []

    # top-level
    for k in REQUIRED_TOP_KEYS:
        if k not in data:
            problems.append(f"missing top key: {k}")
    if problems:
        return problems

    ospf = data["ospf"]
    for k in REQUIRED_OSPF_KEYS:
        if k not in ospf:
            problems.append(f"missing ospf key: {k}")

    # areas
    areas = ospf.get("areas", [])
    if not isinstance(areas, list) or not areas:
        problems.append("areas must be a non-empty list")
    else:
        for i, area in enumerate(areas):
            for k in REQUIRED_AREA_KEYS:
                if k not in area:
                    problems.append(f"area[{i}] missing key: {k}")

    # interfaces
    ints = ospf.get("interfaces", [])
    if not isinstance(ints, list) or not ints:
        problems.append("interfaces must be a non-empty list")
    else:
        for i, iface in enumerate(ints):
            for k in REQUIRED_IF_KEYS:
                if k not in iface:
                    problems.append(f"interfaces[{i}] missing key: {k}")
            nt = iface.get("network_type", "")
            if nt not in {"broadcast", "non-broadcast", "point-to-point", "point-to-multipoint"}:
                problems.append(f"interfaces[{i}] bad network_type: {nt!r}")

    return problems
