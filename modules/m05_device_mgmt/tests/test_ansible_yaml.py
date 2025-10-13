import yaml, pathlib

def test_playbook_parses_yaml():
    data = pathlib.Path("modules/m05_device_mgmt/ansible_playbook.yml").read_text()
    y = yaml.safe_load(data)
    assert isinstance(y, list) and y[0]["name"].lower().startswith("configure")
