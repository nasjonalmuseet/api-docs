const API = "https://api.nasjonalmuseet.no/api/v1";
const headers = { "X-API-Key": process.env.NM_API_KEY };

const r = await fetch(`${API}/objects/NG.M.00939?lang=no`, { headers });
if (!r.ok) throw new Error(`HTTP ${r.status}`);
const verk = await r.json();
console.log(verk.mainTitle, verk.production[0].person.name, verk.labelDate);
