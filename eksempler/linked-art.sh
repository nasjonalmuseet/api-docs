# Søk etter verk i Linked Art (åpent, ingen nøkkel), og hent første treff
ID=$(curl -s "https://api.nasjonalmuseet.no/api/linkedart/object/text-search?q=skrik" \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['data'][0]['id'])")
curl -s -H "Accept: application/ld+json" "$ID"
