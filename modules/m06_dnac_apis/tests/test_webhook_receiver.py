from modules.m06_dnac_apis.lab_webhook_receiver import validate_event

def test_validate_event_true():
    payload = {"instanceId":"1","eventId":"EV-1","category":"NETWORK","severity":"INFO","timestamp":1234567890}
    assert validate_event(payload) is True
