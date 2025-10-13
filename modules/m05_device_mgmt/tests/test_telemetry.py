from modules.m05_device_mgmt.lab_telemetry import build_mdt_subscription

def test_periodic_subscription_has_period():
    p = build_mdt_subscription("/interfaces/interface/state", mode="periodic", period_ms=5000)
    base = p["Cisco-IOS-XE-mdt-cfg:mdt-config-data"]["mdt-subscription"][0]["base"]
    assert base["period"] == 5000

def test_onchange_subscription_has_dampening():
    p = build_mdt_subscription("/interfaces/interface/state", mode="on-change", period_ms=2000)
    base = p["Cisco-IOS-XE-mdt-cfg:mdt-config-data"]["mdt-subscription"][0]["base"]
    assert "dampening-period" in base
