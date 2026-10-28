# Avviklede endepunkter

Et avviklet endepunkt virker ut avviklingsperioden, men står ikke lenger i
[Swagger](https://api.nasjonalmuseet.no/api/docs). Svarene har headerne `Deprecation: true` og
`Sunset` med datoen det fjernes. Etter datoen gir det `404`. Reglene står under
[Stabilitet og versjoner](stabilitet.md).

| Endepunkt | Avviklet | Fjernes | Bruk i stedet |
|---|---|---|---|
| `GET /api/v1/objects/sources` | 26. oktober 2026 | 24. januar 2027 | Ingenting. Lista var fast og sa ikke noe nøkkelen ikke viser selv. Hvilke felt hvert nivå gir, står under [Felt på verket](felt.md) |

## Fjernet

| Endepunkt eller parameter | Fjernet | Bruk i stedet |
|---|---|---|
| `GET /api/v1/iiif/collection.json` | 3.4.0 | `GET /api/v1/iiif/manifest/{nmId}.json` per verk |
| `/api/...` uten versjon | 3.0.0 | `/api/v1/...` |
| `?format=` | 3.0.0 | Utelat parameteren. Linked Art har egne endepunkter |
