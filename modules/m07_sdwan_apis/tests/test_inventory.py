from modules.m07_sdwan_apis.lab_inventory import parse_vmanage_inventory

def test_parse_inventory():
    rows = parse_vmanage_inventory()
    assert len(rows) == 2 and rows[0]["uuid"] == "R1"
