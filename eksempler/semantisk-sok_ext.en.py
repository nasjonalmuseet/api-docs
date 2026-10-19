import os
import requests

API = "https://api.nasjonalmuseet.no/api/v1"
headers = {"X-API-Key": os.environ["NM_API_KEY_EXT"]}

search = {
    "query": "boat in a storm",
    "lang": "en",
    "resultsPerPage": 5,
    "filters": {"objectName": ["Painting"]},
}
r = requests.post(f"{API}/search/semantic", json=search, headers=headers, timeout=60)
r.raise_for_status()
for hit in r.json()["data"]:
    print(round(hit["score"], 3), hit["nmId"], hit["mainTitle"])
