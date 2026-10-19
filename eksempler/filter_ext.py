import os
import requests

API = "https://api.nasjonalmuseet.no/api/v1"
headers = {"X-API-Key": os.environ["NM_API_KEY_EXT"]}

filtre = {"objectName": ["Maleri"], "techniques": ["Olje"], "productionDateFrom": "1880",
          "productionDateTo": "1900", "resultsPerPage": 5, "lang": "no"}
r = requests.post(f"{API}/search/filter", json=filtre, headers=headers, timeout=60)
r.raise_for_status()
svar = r.json()
print("Totalt:", svar["totalResults"])
for verk in svar["data"]:
    print(verk["nmId"], verk["mainTitle"], verk.get("productionYear"))
