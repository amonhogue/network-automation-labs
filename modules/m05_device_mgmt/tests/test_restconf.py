from modules.m05_device_mgmt.lab_restconf import build_restconf_url

def test_rest_url():
    url = build_restconf_url("ios-xe.example", "ietf-interfaces:interfaces/interface=GigabitEthernet1")
    assert url.startswith("https://ios-xe.example/restconf/data/")
    assert "interfaces/interface=GigabitEthernet1" in url
