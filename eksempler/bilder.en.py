import os
import requests

API = "https://api.nasjonalmuseet.no/api/v1"
headers = {"X-API-Key": os.environ["NM_API_KEY"]}

work = requests.get(f"{API}/objects/NG.M.00939", headers=headers, timeout=30).json()
image = work["primaryImage"]
print("Image, 1200 px wide:", image["imageUrl"])
print("IIIF Image API:", image["iiifService"])
# A crop: upper left quadrant, 600 px wide
print("Crop:", f"{image['iiifService']}/pct:0,0,50,50/600,/0/default.jpg")
print("IIIF manifest (for viewers):", f"{API}/iiif/manifest/{work['nmId']}.json")
