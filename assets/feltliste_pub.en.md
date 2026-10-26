| Field | Description | Type |
| --- | --- | --- |
| `nmId` | Identifier of the work (inventory number, URL form) | text |
| `inventoryNumber` | Inventory number | text |
| `uuid` | UUID of the work in MuseumPlus | text |
| `publishable` | Whether the work is published | boolean |
| `productionYear` | First year of production (derived) | integer |
| `productionYearTo` | Last year of production (derived) | integer |
| `mainTitle` | Main title according to the title rule | text |
| `otherTitles` | Other titles | list |
| `titles` | All published titles with type and language | list |
| `titles[].title` | The title | text |
| `titles[].type` | Title type | text |
| `titles[].language` | Language of the title | text |
| `titles[].dateFrom` | Valid from | text |
| `titles[].dateTo` | Valid to | text |
| `objectName` | Object name (painting, drawing, chair …) | text |
| `labelDate` | Date as shown on the label | text |
| `production` | Creators and production, in catalogue order | list |
| `production[].type` | Type of production | text |
| `production[].role` | Role | text |
| `production[].dateFrom` | Date from | text |
| `production[].dateTo` | Date to | text |
| `production[].dateFromYear` | From year | integer |
| `production[].dateToYear` | To year | integer |
| `production[].description` | Note on the production | text |
| `production[].person.id` | Person id in MuseumPlus | integer |
| `production[].person.uuid` | Person UUID | text |
| `production[].person.name` | Name | text |
| `production[].person.birthYear` | Year of birth | text |
| `production[].person.deathYear` | Year of death | text |
| `production[].person.gender` | Gender (from the person register) | text |
| `production[].person.nationality` | Nationality | list |
| `production[].person.certainty` | Certainty of attribution | text |
| `production[].place` | Place of production (name, type, certainty) |  |
| `production[].place.name` | Place name from the place register |  |
| `production[].place.type` | Place type, e.g. Place of production |  |
| `production[].place.certainty` | Certainty, e.g. assumed |  |
| `materials` | Materials | list |
| `techniques` | Techniques | list |
| `materialTechniqueDescription` | Material and technique as free text | text |
| `dimensions` | Dimensions | list |
| `dimensions[].type` | Type of measurement | text |
| `dimensions[].value` | Value | integer |
| `dimensions[].unit` | Unit | text |
| `dimensions[].category` | Category | text |
| `publishableDimensions` | Dimensions as text for publication | text |
| `collection` | Collection | text |
| `creditLine` | Credit line | text |
| `keywords` | Subject terms from the catalogue | list |
| `motifType` | Motif type | list |
| `classification` | Classification | list |
| `owner` | Owner | text |
| `inscriptions` | Inscriptions, signatures and stamps | list |
| `inscriptions[].type` | Type: Inscription, Signature, Stamp … | text |
| `inscriptions[].transcription` | The text as written on the work | text |
| `inscriptions[].position` | Position on the work | text |
| `inscriptions[].method` | Method of the inscription | text |
| `inscriptions[].language` | Language | text |
| `inscriptions[].inscriber` | Inscriber | text |
| `inscriptions[].date` | Date of the inscription | text |
| `provenance` | Provenance | list |
| `provenance[].type` | Type: Ownership, Accession, Acquisition … | text |
| `provenance[].owner` | Owner's name from the person register | text |
| `provenance[].role` | Role, e.g. [40] Previous owner | text |
| `provenance[].certainty` | Certainty | text |
| `provenance[].place` | Place from the place register |  |
| `provenance[].dateFrom` | From (date text) | text |
| `provenance[].dateTo` | To (date text) | text |
| `provenance[].dateFromYear` | From year | integer |
| `provenance[].dateToYear` | To year | integer |
| `copyright` | Copyright: holder, manager, status and expiry | list |
| `copyright[].holder` | Rights holder | text |
| `copyright[].manager` | Rights manager, e.g. BONO |  |
| `copyright[].status` | Status | text |
| `copyright[].dateTo` | When protection expires | text |
| `publicDomain` | Public domain | boolean |
| `multimedia` | Published images | list |
| `multimedia[].imageId` | Image id (multimediaRef) | integer |
| `multimedia[].uuid` | Image UUID | text |
| `multimedia[].originalFileName` | File name in the image archive | text |
| `multimedia[].thumbnail` | Main image | boolean |
| `multimedia[].usage` | Usage | text |
| `multimedia[].photoCredit` | Photographer | text |
| `multimedia[].creditLine` | Credit line for the image |  |
| `multimedia[].iiifService` | IIIF Image API address | text |
| `multimedia[].imageUrl` | Image URL (1200 px wide) | text |
| `primaryImage` | Main image (same shape as multimedia[]) | object |
