"""
RESTCONF lab (offline-first).
"""

def build_restconf_url(host, resource="ietf-interfaces:interfaces"):
    host = host.rstrip("/")
    return f"https://{host}/restconf/data/{resource}"
