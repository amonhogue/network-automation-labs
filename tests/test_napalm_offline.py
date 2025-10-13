# tests/test_napalm_offline.py
import napalm
import pytest

def _fake_get_network_driver_factory(os_name_expected):
    """Return a fake get_network_driver that yields a minimal device class."""

    class FakeDevice:
        def __init__(self, hostname, username, password, **kwargs):
            self.hostname = hostname
            self.username = username
            self.password = password
            self.os_name = os_name_expected

        def open(self):  # no-op
            pass

        def close(self):  # no-op
            pass

        def get_facts(self):
            # minimal, cross-vendor style facts
            return {
                "hostname": f"{self.os_name}-device",
                "model": "virtual",
                "uptime": 123,
                "os_version": "stub",
                "vendor": self.os_name.upper(),
            }

    def _fake_get_network_driver(os_name):
        # Assert we’re being asked for the driver we expect in each test
        assert os_name == os_name_expected
        # Return a callable that constructs our FakeDevice (same signature as real driver)
        return lambda hostname, username, password, **kwargs: FakeDevice(
            hostname, username, password, **kwargs
        )

    return _fake_get_network_driver


@pytest.mark.parametrize("os_name", ["ios", "junos", "eos"])
def test_facts_multivendor(monkeypatch, os_name):
    # Patch napalm.get_network_driver to our fake for this os_name
    monkeypatch.setattr(napalm, "get_network_driver", _fake_get_network_driver_factory(os_name))

    # Use NAPALM exactly as normal client code would
    driver = napalm.get_network_driver(os_name)
    device = driver(hostname="dummy", username="x", password="x")
    device.open()
    facts = device.get_facts()
    device.close()

    # Assertions prove vendor-agnostic shape and non-empty values
    assert facts["hostname"]
    assert facts["model"]
    assert facts["uptime"] >= 0
