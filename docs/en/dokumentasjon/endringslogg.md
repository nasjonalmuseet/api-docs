# Changelog

Changes that affect users of the API, newest first. The running version is shown at
<https://api.nasjonalmuseet.no/api/health>. The rules for changes are under
[Stability and versions](stabilitet.md).

## 3.13.0 — 27 October 2026
- The producer's gender and nationality (`production[].person.gender` and `.nationality`) are at ext only, not pub. `POST /objects/find` at pub rejects filters on them.

## 3.12.0 — 26 October 2026
- New fields at pub and ext: `motifType`, `owner`, `production[].place`, `inscriptions[]`, `provenance[]`, `copyright[]` and `publicDomain`. `classification` moved from ext to pub. The fields can be used in `POST /objects/find`. See [Fields](felt.md).
- `GET /objects/sources` is deprecated and will be removed on 24 January 2027. See [Deprecated endpoints](avviklet.md).
- The IIIF manifest and `GET /objects/{nmId}/multimedia` are marked preliminary: the structure may change.

## 3.11.0 — 23 October 2026
- New `POST /objects/find`: look up works with a filter expression on the fields in the response, at every level.
- Similarity search has `mode: visual` (similarity in the image itself), and the new `POST /search/similar` finds works similar to the main image of an `nmId` (ext).
- Text search ranks exact words before near matches.

## 3.10.0 — 23 October 2026
- `catalogueTerms` on images is at ext only.
- Titles are trimmed of spaces at the ends.
- `productionYear` comes from the work's own production (motif, model and original do not count), and from the date text when the year is missing.
- Text search only matches the titles that are shown.

## 3.9.6 — 19 October 2026
- The IIIF manifests can be fetched from the browser on other domains (CORS), so IIIF viewers can load them.

## 3.9.5 — 19 October 2026
- Text search only searches catalogue fields, not machine-made text.

## 3.8.0 — 16 October 2026
- New `POST /search/interpret`: suggested search text and filters from free text.

## 3.6.0 — 16 October 2026
- The filters `objectName`, `techniques` and `materials` in semantic search and filter search, in Norwegian or English.

## 3.5.0 — 15 October 2026
- `mainTitle` follows the museum's title rules. New fields `titles[]` and `production[].description`.

## 3.4.0 — 15 October 2026
- Keys are created on the registration page. `GET /iiif/collection.json` is removed.

## 3.3.0 — 15 October 2026
- **All data endpoints require a key.** Without one they answer `401` with a link to registration.

## 3.2.0 — 14 October 2026
- The `creatorGender` filter in semantic search and filter search.

## 3.1.0 — 14 October 2026
- Semantic search merges in word search in the work's text. `channel` can be `lexical`.

## 3.0.1 — 14 October 2026
- Linked Art addresses can be resolved directly (`application/ld+json`). Filter search pages by work, and similarity search gives the same order whatever the page size.

## 3.0.0 — 13 October 2026
- First version of the fixed contract: `/api/v1` only, camelCase, one error format with `requestId`, always flat JSON in the chosen language, unknown fields in requests are ignored.
