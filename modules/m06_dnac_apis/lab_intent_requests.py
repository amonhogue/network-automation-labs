BASE = "https://dnac.example/dna/intent/api/v1"

def build_intent_url(kind="network-device"):
    return f"{BASE}/{kind}"
