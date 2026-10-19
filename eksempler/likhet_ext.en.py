import os
import requests

API = "https://api.nasjonalmuseet.no/api/v1"
headers = {"X-API-Key": os.environ["NM_API_KEY_EXT"]}

work = requests.get(f"{API}/objects/NG.M.00939", headers=headers, timeout=30).json()
image_id = work["primaryImage"]["imageId"]
r = requests.post(f"{API}/search/similar/{image_id}", json={"nmId": "NG.M.00939", "resultsPerPage": 5, "lang": "en"},
                  headers=headers, timeout=60)
r.raise_for_status()
for hit in r.json()["data"]:
    print(hit["nmId"], hit["mainTitle"])
