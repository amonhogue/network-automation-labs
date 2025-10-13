from pathlib import Path

def parse_show_ip_int_brief(text: str):
    lines = [ln for ln in text.splitlines() if ln.strip()]
    # skip header
    body = lines[1:]
    rows = []
    for ln in body:
        parts = ln.split()
        iface = parts[0]
        ip = parts[1]
        # last two tokens are status and protocol (handles "administratively down")
        status = parts[-2]
        protocol = parts[-1]
        rows.append({"interface": iface, "ip": ip, "status": status, "protocol": protocol})
    return rows

if __name__ == "__main__":
    text = Path("modules/m01_python_basics/data/show_ip_int_brief.txt").read_text()
    print(parse_show_ip_int_brief(text))
