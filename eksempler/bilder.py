import os
import requests

API = "https://api.nasjonalmuseet.no/api/v1"
headers = {"X-API-Key": os.environ["NM_API_KEY"]}

verk = requests.get(f"{API}/objects/NG.M.00939", headers=headers, timeout=30).json()
bilde = verk["primaryImage"]
print("Bilde, 1200 px bredt:", bilde["imageUrl"])
print("IIIF Image API:", bilde["iiifService"])
# Et utsnitt: øvre venstre kvadrant, 600 px bredt
print("Utsnitt:", f"{bilde['iiifService']}/pct:0,0,50,50/600,/0/default.jpg")
print("IIIF-manifest (for visere):", f"{API}/iiif/manifest/{verk['nmId']}.json")
