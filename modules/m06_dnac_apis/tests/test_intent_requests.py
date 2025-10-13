from modules.m06_dnac_apis.lab_intent_requests import build_intent_url

def test_build_intent_url():
    u = build_intent_url("network-device")
    assert u.endswith("/network-device")
