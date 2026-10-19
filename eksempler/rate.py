import os
import time
import requests

API = "https://api.nasjonalmuseet.no/api/v1"
headers = {"X-API-Key": os.environ["NM_API_KEY"]}


def hent(url, **kw):
    """GET med respekt for ratebegrensningen: ved 429 venter vi Retry-After sekunder."""
    for _ in range(5):
        r = requests.get(url, headers=headers, timeout=30, **kw)
        if r.status_code != 429:
            r.raise_for_status()
            return r.json()
        time.sleep(int(r.headers.get("Retry-After", "5")))
    raise RuntimeError("Ga opp etter fem forsøk")


print(hent(f"{API}/objects/NG.M.00939")["mainTitle"])
