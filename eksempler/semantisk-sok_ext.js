const API = "https://api.nasjonalmuseet.no/api/v1";
const headers = { "X-API-Key": process.env.NM_API_KEY_EXT, "Content-Type": "application/json" };

const r = await fetch(`${API}/search/semantic`, {
  method: "POST",
  headers,
  body: JSON.stringify({ query: "kvinne ved et vindu", lang: "no", resultsPerPage: 5 }),
});
if (!r.ok) throw new Error(`HTTP ${r.status}`);
for (const t of (await r.json()).data) console.log(t.score.toFixed(3), t.nmId, t.mainTitle);
