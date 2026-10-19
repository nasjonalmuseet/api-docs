import os
import requests

API = "https://api.nasjonalmuseet.no/api/v1"
headers = {"X-API-Key": os.environ["NM_API_KEY"]}

page = 1
while page <= 3:  # in practice: until data is empty
    r = requests.get(f"{API}/objects", params={"page": page, "resultsPerPage": 50, "lang": "en"},
                     headers=headers, timeout=60)
    r.raise_for_status()
    response = r.json()
    if not response["data"]:
        break
    print(f"page {page}: {len(response['data'])} works of {response['totalResults']}")
    page += 1
