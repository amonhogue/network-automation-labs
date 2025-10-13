# tests/test_napalm_offline.py
from napalm.base.test import double

def _facts_for(os_name: str):
    # NAPALM's test double mimics real devices using bundled fixtures
    driver = double.get_network_driver(os_name)
    device = driver(hostname="dummy", username="x", password="x")
    device.open()
    facts = device.get_facts()
    device.close()
    return facts

def test_ios_facts_has_hostname():
    facts = _facts_for("ios")
    assert "hostname" in facts and facts["hostname"]

def test_junos_facts_has_uptime():
    facts = _facts_for("junos")
    assert facts.get("uptime", 0) >= 0

def test_eos_facts_has_model():
    facts = _facts_for("eos")
    assert "model" in facts and facts["model"]
