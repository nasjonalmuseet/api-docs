const API = "https://api.nasjonalmuseet.no/api/v1";
const headers = { "X-API-Key": process.env.NM_API_KEY };

const r = await fetch(`${API}/objects/NG.M.00939?lang=en`, { headers });
if (!r.ok) throw new Error(`HTTP ${r.status}`);
const work = await r.json();
console.log(work.mainTitle, work.production[0].person.name, work.labelDate);
