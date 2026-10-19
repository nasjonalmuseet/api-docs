import os
import requests

API = "https://api.nasjonalmuseet.no/api/v1"
headers = {"X-API-Key": os.environ["NM_API_KEY"]}

r = requests.get(f"{API}/objects/text-search", params={"q": "vinterlandskap", "resultsPerPage": 5, "lang": "no"},
                 headers=headers, timeout=30)
r.raise_for_status()
for verk in r.json()["data"]:
    print(verk["nmId"], verk["mainTitle"])
