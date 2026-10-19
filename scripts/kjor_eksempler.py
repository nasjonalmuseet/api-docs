"""
Kjører alle eksemplene i eksempler/ mot prod, slik de står i veiledningen.

  NM_API_KEY=<pub-nøkkel> [NM_API_KEY_EXT=<ext-nøkkel>] python scripts/kjor_eksempler.py

Et eksempel består når det avslutter med 0, skriver noe, og svaret ikke er en feilkonvolutt.
Eksempler med _ext i navnet hoppes over uten NM_API_KEY_EXT. feilsvar-eksemplene skal gi 401.
Brukes av workflowen «Test eksempler» og lokalt før endringer publiseres.
"""
import json
import os
import pathlib
import subprocess
import sys
import time

MAPPE = pathlib.Path(__file__).resolve().parent.parent / "eksempler"
KJOR = {".sh": ["bash"], ".py": [sys.executable], ".js": ["node", "--input-type=module"]}


def kjor(fil: pathlib.Path) -> tuple:
    cmd = KJOR[fil.suffix]
    if fil.suffix == ".js":
        p = subprocess.run(cmd, input=fil.read_text(), capture_output=True, text=True, timeout=120)
    else:
        p = subprocess.run(cmd + [str(fil)], capture_output=True, text=True, timeout=120)
    ut = p.stdout.strip()
    if p.returncode != 0:
        return False, (p.stderr.strip() or ut)[-300:]
    if not ut:
        return False, "ingen utskrift"
    if fil.name.startswith("feilsvar"):
        return ("HTTP 401" in ut), ut[-120:]
    if ut.startswith("{"):
        try:
            d = json.loads(ut.split("\nHTTP")[0])
            if "error" in d:
                return False, ut[:300]
        except json.JSONDecodeError:
            pass
    return True, ut.splitlines()[0][:120]


def main() -> int:
    if not os.environ.get("NM_API_KEY"):
        print("NM_API_KEY mangler (pub-nøkkel).")
        return 2
    feil = 0
    for fil in sorted(MAPPE.iterdir()):
        if fil.suffix not in KJOR:
            continue
        if "_ext" in fil.name and not os.environ.get("NM_API_KEY_EXT"):
            print(f"HOPPET  {fil.name} (krever ext)")
            continue
        ok, info = kjor(fil)
        feil += not ok
        print(f"{'OK    ' if ok else 'FEIL  '}  {fil.name}: {info}")
        time.sleep(2.5)  # holder oss godt under ratebegrensningen
    return 1 if feil else 0


if __name__ == "__main__":
    sys.exit(main())
