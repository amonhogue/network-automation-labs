"""
NETCONF lab (offline-first).
When ready, pip install ncclient and use a real manager.connect().
"""

def build_netconf_filter_interface(name="GigabitEthernet1"):
    return f"""<filter xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>{name}</name>
    </interface>
  </interfaces>
</filter>"""
