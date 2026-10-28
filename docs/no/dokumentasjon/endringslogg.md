# Endringslogg

Endringene som angår brukere av API-et, nyeste først. Kjørende versjon står på
<https://api.nasjonalmuseet.no/api/health>. Reglene for endringer står under
[Stabilitet og versjoner](stabilitet.md).

## 3.13.0 — 27. oktober 2026
- Produsentens kjønn og nasjonalitet (`production[].person.gender` og `.nationality`) er bare på ext, ikke på pub. `POST /objects/find` på pub avviser filter på dem.

## 3.12.0 — 26. oktober 2026
- Nye felt på pub og ext: `motifType`, `owner`, `production[].place`, `inscriptions[]`, `provenance[]`, `copyright[]` og `publicDomain`. `classification` er flyttet fra ext til pub. Feltene kan brukes i `POST /objects/find`. Se [Felt på verket](felt.md).
- `GET /objects/sources` er avviklet og fjernes 24. januar 2027. Se [Avviklede endepunkter](avviklet.md).
- IIIF-manifestet og `GET /objects/{nmId}/multimedia` er merket foreløpige: strukturen kan endres.

## 3.11.0 — 23. oktober 2026
- Nytt `POST /objects/find`: oppslag med filteruttrykk på feltene i svaret, på alle nivåer.
- Likhetssøket har `mode: visual` (likhet i selve bildet), og nytt `POST /search/similar` finner verk som ligner hovedbildet til et `nmId` (ext).
- Tekstsøket rangerer eksakte ord foran nesten-treff.

## 3.10.0 — 23. oktober 2026
- `catalogueTerms` på bildene er bare på ext.
- Titler trimmes for mellomrom i endene.
- `productionYear` regnes fra verkets egen produksjon (motiv, forlegg og originalen teller ikke), og fra datoteksten når årstallet mangler.
- Tekstsøket treffer bare titlene som vises.

## 3.9.6 — 19. oktober 2026
- IIIF-manifestene kan hentes fra nettleseren på andre domener (CORS), så IIIF-visere kan laste dem.

## 3.9.5 — 19. oktober 2026
- Tekstsøket søker bare i katalogfelt, ikke i maskinelt laget tekst.

## 3.8.0 — 16. oktober 2026
- Nytt `POST /search/interpret`: forslag til søketekst og filtre fra en fritekst.

## 3.6.0 — 16. oktober 2026
- Filtrene `objectName`, `techniques` og `materials` i semantisk søk og filtersøk, på norsk eller engelsk.

## 3.5.0 — 15. oktober 2026
- `mainTitle` følger museets tittelregler. Nye felt `titles[]` og `production[].description`.

## 3.4.0 — 15. oktober 2026
- Nøkkelen lages på registreringssiden. `GET /iiif/collection.json` er fjernet.

## 3.3.0 — 15. oktober 2026
- **Alle dataendepunkter krever nøkkel.** Uten nøkkel svarer de `401` med lenke til registreringen.

## 3.2.0 — 14. oktober 2026
- Filteret `creatorGender` i semantisk søk og filtersøk.

## 3.1.0 — 14. oktober 2026
- Semantisk søk fletter inn ordsøk i verkets tekst. `channel` kan være `lexical`.

## 3.0.1 — 14. oktober 2026
- Linked Art-adressene kan slås opp direkte (`application/ld+json`). Filtersøket blar på verk, og likhetssøket gir samme rekkefølge uansett sidestørrelse.

## 3.0.0 — 13. oktober 2026
- Første versjon av den faste kontrakten: bare `/api/v1`, camelCase, feil i én form med `requestId`, alltid flat JSON på valgt språk, ukjente felt i forespørsler ignoreres.
