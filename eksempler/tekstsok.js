const API = "https://api.nasjonalmuseet.no/api/v1";
const headers = { "X-API-Key": process.env.NM_API_KEY };

const url = new URL(`${API}/objects/text-search`);
url.search = new URLSearchParams({ q: "vinterlandskap", resultsPerPage: 5, lang: "no" });
const r = await fetch(url, { headers });
if (!r.ok) throw new Error(`HTTP ${r.status}`);
for (const verk of (await r.json()).data) console.log(verk.nmId, verk.mainTitle);
