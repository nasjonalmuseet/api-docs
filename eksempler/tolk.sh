curl -s -X POST "https://api.nasjonalmuseet.no/api/v1/search/interpret" \
  -H "X-API-Key: $NM_API_KEY" -H "Content-Type: application/json" \
  -d '{"query": "maleri av en fin soloppgang", "lang": "no"}'
