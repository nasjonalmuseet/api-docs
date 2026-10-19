import os
import requests

API = "https://api.nasjonalmuseet.no/api/v1"
headers = {"X-API-Key": os.environ["NM_API_KEY_EXT"]}

sok = {
    "query": "båt i stormvær",
    "lang": "no",
    "resultsPerPage": 5,
    "filters": {"objectName": ["Maleri"]},
}
r = requests.post(f"{API}/search/semantic", json=sok, headers=headers, timeout=60)
r.raise_for_status()
for treff in r.json()["data"]:
    print(round(treff["score"], 3), treff["nmId"], treff["mainTitle"])
