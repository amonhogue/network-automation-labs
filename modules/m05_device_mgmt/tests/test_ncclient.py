from modules.m05_device_mgmt.lab_ncclient import build_netconf_filter_interface

def test_filter_contains_interface():
    xml = build_netconf_filter_interface("GigabitEthernet1")
    assert "<interfaces" in xml and "<name>GigabitEthernet1</name>" in xml
