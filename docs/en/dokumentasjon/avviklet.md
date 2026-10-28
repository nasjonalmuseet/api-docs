# Deprecated endpoints

A deprecated endpoint keeps working until the end of the deprecation period, but is no longer listed
in [Swagger](https://api.nasjonalmuseet.no/api/docs). Its responses carry the headers
`Deprecation: true` and `Sunset` with the removal date. After that date it answers `404`. The rules
are under [Stability and versions](stabilitet.md).

| Endpoint | Deprecated | Removed | Use instead |
|---|---|---|---|
| `GET /api/v1/objects/sources` | 26 October 2026 | 24 January 2027 | Nothing. The list was fixed and said nothing the key does not show itself. The fields each level gives are listed under [Fields](felt.md) |

## Removed

| Endpoint or parameter | Removed | Use instead |
|---|---|---|
| `GET /api/v1/iiif/collection.json` | 3.4.0 | `GET /api/v1/iiif/manifest/{nmId}.json` per work |
| `/api/...` without a version | 3.0.0 | `/api/v1/...` |
| `?format=` | 3.0.0 | Leave the parameter out. Linked Art has its own endpoints |
