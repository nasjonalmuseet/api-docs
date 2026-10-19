import os
import requests

API = "https://api.nasjonalmuseet.no/api/v1"
headers = {"X-API-Key": os.environ["NM_API_KEY_EXT"]}

verk = requests.get(f"{API}/objects/NG.M.00939", headers=headers, timeout=30).json()
bilde_id = verk["primaryImage"]["imageId"]
r = requests.post(f"{API}/search/similar/{bilde_id}", json={"nmId": "NG.M.00939", "resultsPerPage": 5, "lang": "no"},
                  headers=headers, timeout=60)
r.raise_for_status()
for t in r.json()["data"]:
    print(t["nmId"], t["mainTitle"])
