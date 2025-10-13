from modules.m03_config_drift.lab import unified_diff

def test_diff_shows_vlan_change():
    diff = unified_diff("modules/m03_config_drift/data/golden.txt",
                        "modules/m03_config_drift/data/running.txt")
    assert "- switchport access vlan 20" in diff
    assert "+ switchport access vlan 10" in diff
