# Search for works in Linked Art (open, no key), and fetch the first hit
ID=$(curl -s "https://api.nasjonalmuseet.no/api/linkedart/object/text-search?q=scream" \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['data'][0]['id'])")
curl -s -H "Accept: application/ld+json" "$ID"
