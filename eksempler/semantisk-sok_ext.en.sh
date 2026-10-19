curl -s -X POST "https://api.nasjonalmuseet.no/api/v1/search/semantic" \
  -H "X-API-Key: $NM_API_KEY_EXT" -H "Content-Type: application/json" \
  -d '{"query": "two horses behind a fence", "lang": "en", "resultsPerPage": 5}'
