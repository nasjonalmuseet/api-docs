| Field | Description | Type | Example | Source in the catalogue | On the website |
| --- | --- | --- | --- | --- | --- |
| `titles[].type` | Title type | text | `anvendt` | `titles[] (value` | – |
| `titles[].dateFrom` | Valid from | text | – | `titles[] (value` | – |
| `titles[].dateTo` | Valid to | text | – | `titles[] (value` | – |
| `production[].description` | Note on the production | text | – | `production[].description.value` | – |
| `production[].person.uuid` | Person UUID | text | `281F289C-1A53-4727-86F8-A335CB4AB072` | `production[].person.uuid` | no |
| `production[].person.birthYear` | Year of birth | text | `1863` | `production[].person._resolved.birthYear` | no |
| `production[].person.deathYear` | Year of death | text | `1944` | `production[].person._resolved.deathYear` | no |
| `production[].person.gender` | Gender (from the person register) | text | `Male` | `production[].person._resolved.gender` | no |
| `production[].person.nationality` | Nationality | list | `Norway` | `production[].person._resolved.nationality` | no |
| `production[].place.type` | Place type, e.g. Place of production | – | `Produksjonssted` | `production[].place.placeType.value` | – |
| `inscriptions[].language` | Language | text | – | `inscriptionsLabels[].language.value` | – |
| `provenance[].place` | Place from the place register | – | `Elmholt Allé 13, Oslo (fylke) (Norge)` | `provenanceOwnership[].place._resolved.name` | – |
| `multimedia[].uuid` | Image UUID | text | `1040531` | `multimedia[] (published images only)` | no |
| `multimedia[].creditLine` | Credit line for the image | – | – | `multimedia[] (published images only)` | – |
| `multimedia[].ai` | AI data per image (enrichment): keywords, groups, bound terms (boundTerms), scene sentences (scene), signatures and versions | object | `{keywords, groups, signatures, version}` | `multimedia[] (published images only)` | no |
| `multimedia[].catalogueTerms` | Catalogue terms per image (written by enrichment) | list | `Papplate, Tempera, Fettstift, …` | `multimedia[] (published images only)` | no (skrevet av berikelsen) |
| `multimedia[].enrichmentId` | Id of the image enrichment | – | `723af58e-25bd-425d-8a5d-2ed8ff80d530` | `multimedia[] (published images only)` | – |
| `multimedia[].hasEnrichment` | Whether the image is enriched | boolean | `true` | `multimedia[] (published images only)` | – |
| `uuid` | UUID of the work in MuseumPlus | text | `C88BFBE7-645D-4EE4-922C-4A3AFA7087F7` | `uuid` | no |
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
