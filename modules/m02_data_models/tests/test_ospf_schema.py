# modules/m02_data_models/tests/test_ospf_schema.py
import json
from modules.m02_data_models.lab_ospf_schema import validate_ospf_schema

def test_valid_sample_passes():
    with open("modules/m02_data_models/sample/ospf.json") as f:
        data = json.load(f)
    problems = validate_ospf_schema(data)
    assert problems == []

def test_bad_network_type_fails():
    data = {
        "ospf": {
            "process_id": "1",
            "areas": [{"area_id": "0.0.0.0", "networks": ["10.0.0.0/8"]}],
            "interfaces": [{"name": "Gig0/0", "area_id": "0.0.0.0", "network_type": "banana"}]
        }
    }
    problems = validate_ospf_schema(data)
    assert any("bad network_type" in p for p in problems)
