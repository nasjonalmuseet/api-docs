import os
import requests

API = "https://api.nasjonalmuseet.no/api/v1"
headers = {"X-API-Key": os.environ["NM_API_KEY_EXT"]}

filters = {"objectName": ["Painting"], "techniques": ["Oil paint"], "productionDateFrom": "1880",
           "productionDateTo": "1900", "resultsPerPage": 5, "lang": "en"}
r = requests.post(f"{API}/search/filter", json=filters, headers=headers, timeout=60)
r.raise_for_status()
response = r.json()
print("Total:", response["totalResults"])
for work in response["data"]:
    print(work["nmId"], work["mainTitle"], work.get("productionYear"))
