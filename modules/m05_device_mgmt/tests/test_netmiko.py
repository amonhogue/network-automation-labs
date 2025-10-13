from modules.m05_device_mgmt.lab_netmiko import build_netmiko_params

def test_build_params():
    params = build_netmiko_params("192.0.2.10", "amon", "secret", "cisco_ios")
    assert params["host"] == "192.0.2.10"
    assert params["device_type"] == "cisco_ios"
    assert params["fast_cli"] is True
