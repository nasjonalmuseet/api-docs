import os
import requests

API = "https://api.nasjonalmuseet.no/api/v1"
headers = {"X-API-Key": os.environ["NM_API_KEY"]}

side = 1
while side <= 3:  # i praksis: til data er tom
    r = requests.get(f"{API}/objects", params={"page": side, "resultsPerPage": 50, "lang": "no"},
                     headers=headers, timeout=60)
    r.raise_for_status()
    svar = r.json()
    if not svar["data"]:
        break
    print(f"side {side}: {len(svar['data'])} verk av {svar['totalResults']}")
    side += 1
