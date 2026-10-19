curl -s -G -H "X-API-Key: $NM_API_KEY" \
  "https://api.nasjonalmuseet.no/api/v1/objects/text-search" \
  --data-urlencode "q=vinterlandskap" -d resultsPerPage=5 -d lang=no
