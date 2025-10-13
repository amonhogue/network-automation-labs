import difflib
from pathlib import Path

def unified_diff(golden_path, running_path):
    g = Path(golden_path).read_text().splitlines()
    r = Path(running_path).read_text().splitlines()
    return "\n".join(difflib.unified_diff(g, r, fromfile="golden", tofile="running", lineterm=""))

if __name__ == "__main__":
    print(unified_diff("modules/m03_config_drift/data/golden.txt",
                       "modules/m03_config_drift/data/running.txt"))
