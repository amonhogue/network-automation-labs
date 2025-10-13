"""
Netmiko lab (offline-first).

When ready, install netmiko and replace the stub with a real connection:
from netmiko import ConnectHandler
"""

def build_netmiko_params(host, username="admin", password="admin", device_type="cisco_ios"):
    return {
        "device_type": device_type,
        "host": host,
        "username": username,
        "password": password,
        "fast_cli": True,
    }
