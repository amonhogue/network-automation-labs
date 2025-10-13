from pathlib import Path
from modules.m01_python_basics.lab import parse_show_ip_int_brief

def test_parse_show_ip_int_brief():
    text = Path("modules/m01_python_basics/data/show_ip_int_brief.txt").read_text()
    rows = parse_show_ip_int_brief(text)
    assert isinstance(rows, list) and rows, "expected non-empty list"
    assert rows[0]["interface"].lower().startswith("gigabit")
    assert rows[0]["status"] == "up"
    assert rows[1]["protocol"] == "down"
