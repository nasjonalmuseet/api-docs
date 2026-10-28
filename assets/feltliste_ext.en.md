| Field | Description | Type | Example | Source in the catalogue | On the website |
| --- | --- | --- | --- | --- | --- |
| `production[].person.gender` | Gender (from the person register) | text | `Male` | `production[].person._resolved.gender` | no |
| `production[].person.nationality` | Nationality | list | `Norway` | `production[].person._resolved.nationality` | no |
| `multimedia[].ai` | AI keywords and groups (enrichment) | object | `{keywords, groups}` | `multimedia[] (published images only)` | no |
| `multimedia[].catalogueTerms` | Catalogue terms per image (written by enrichment) | list | `Papplate, Tempera, Fettstift, …` | `multimedia[] (published images only)` | no (skrevet av berikelsen) |
| `multimedia[].enrichmentId` | Id of the image enrichment | – | `723af58e-25bd-425d-8a5d-2ed8ff80d530` | `multimedia[] (published images only)` | – |
| `multimedia[].hasEnrichment` | Whether the image is enriched | boolean | `true` | `multimedia[] (published images only)` | – |
| `exhibitions` | Published exhibitions the work has been in | – | – | `exhibitions` | yes |
| `exhibitions[].id` | Exhibition id | – | – | `exhibitions[].exhibitionID` | – |
| `exhibitions[].title` | Exhibition title | – | – | `exhibitions[]._resolved.title` | – |
| `exhibitions[].venue` | Venue | – | – | `exhibitions[]._resolved.venue` | – |
| `exhibitions[].dateFrom` | From date | – | – | `exhibitions[]._resolved.dateFrom` | – |
| `exhibitions[].dateTo` | To date | – | – | `exhibitions[]._resolved.dateTo` | – |
| `objectType` | Object type | text | `Billedkunst` | `objectType.value` | – |
| `entityType` | Entity type in MuseumPlus | text | `ART` | `entityType` | – |
| `isArtwork` | Whether the object is an artwork | boolean | `true` | `isArtwork` | – |
| `stylePeriod` | Style period | list | – | `stylePeriod` | – |
| `onDisplay` | On display now: room, exhibition and period | object | `{active, room, exhibition, dateFrom, …}` | `onDisplay.active` | yes («Utstilt i») |
