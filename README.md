# Network Automation Labs

**Learn Python the network engineer’s way** — every lab uses constructs you already know (interfaces, ACLs, OSPF, VLANs, APIs). Run locally or in **GitHub Codespaces** with zero setup.

## Run in Codespaces (1‑click)
1) Push this repo to GitHub.
2) Click the green **Code** button → **Codespaces** → **Create codespace**.
3) In the terminal: `pytest -q` (to run all tests) or run a lab, e.g.:
   ```bash
   python modules/m03_config_drift/lab.py
   ```

## Run locally
```bash
python -m venv .venv
# mac/linux
source .venv/bin/activate
# windows powershell
# .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
pytest -q
python modules/m01_python_basics/lab.py
```

## Modules
- **m01_python_basics** — parse *show ip int brief* into structured data
- **m02_data_models** — (placeholder) model OSPF, ACLs, VLANs in JSON/YAML
- **m03_config_drift** — unified diff: golden vs running configs
- **m04_apis** — (placeholder) Meraki / Catalyst Center inventory (record & replay)

> Tip: Each module has a `lab.py` and a minimal test under `tests/`.


- **m05_device_mgmt** — Netmiko (SSH), ncclient (NETCONF), RESTCONF, Ansible, MDT payloads
- **m06_dnac_apis** — Catalyst Center (Intent, Sites, Assurance, Events, Webhooks)
- **m07_sdwan_apis** — vManage inventory / config / monitoring (record & replay)
