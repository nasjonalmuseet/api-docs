import os
import requests

API = "https://api.nasjonalmuseet.no/api/v1"
headers = {"X-API-Key": os.environ["NM_API_KEY"]}

r = requests.get(f"{API}/objects/NG.M.00939", params={"lang": "no"}, headers=headers, timeout=30)
r.raise_for_status()
verk = r.json()
print(verk["mainTitle"], verk["production"][0]["person"]["name"], verk["labelDate"])
