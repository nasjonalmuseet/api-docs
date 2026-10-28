| Field | Description | Type | Example | Source in the catalogue | On the website |
| --- | --- | --- | --- | --- | --- |
| `nmId` | Identifier of the work (inventory number, URL form) | text | `NG.M.00939` | `nmId` | yes (i adressen) |
| `inventoryNumber` | Inventory number | text | `NG.M.00939` | `inventoryNumber` | yes |
| `uuid` | UUID of the work in MuseumPlus | text | `C88BFBE7-645D-4EE4-922C-4A3AFA7087F7` | `uuid` | no |
| `publishable` | Whether the work is published | boolean | `true` | `publishable` | – |
| `productionYear` | First year of production (derived) | integer | `1893` | `productionYear` | no (nettsiden viser labelDate) |
| `productionYearTo` | Last year of production (derived) | integer | `1893` | `productionYearTo` | no (nettsiden viser labelDate) |
| `mainTitle` | Main title according to the title rule | text | `Skrik` | `titles[] (value` | yes (tom tittel: nettsiden viser betegnelsen) |
| `otherTitles` | Other titles | list | `The Scream` | `titles[] (value` | yes |
| `titles` | All published titles with type and language | list | `[{title, type, language, dateFrom, …}, …]` | `titles[] (value` | partly (uten type og datoer) |
| `titles[].title` | The title | text | `Skrik` | `titles[] (value` | – |
| `titles[].type` | Title type | text | `anvendt` | `titles[] (value` | – |
| `titles[].language` | Language of the title | text | `Norsk` | `titles[] (value` | – |
| `titles[].dateFrom` | Valid from | text | – | `titles[] (value` | – |
| `titles[].dateTo` | Valid to | text | – | `titles[] (value` | – |
| `objectName` | Object name (painting, drawing, chair …) | text | `Maleri` | `objectName.value` | yes |
| `labelDate` | Date as shown on the label | text | `1893` | `labelDate` | yes |
| `production` | Creators and production, in catalogue order | list | `[{type, role, dateFrom, dateTo, …}, …]` | `production` | partly |
| `production[].type` | Type of production | text | `Produsert` | `production[].type.value` | – |
| `production[].role` | Role | text | `Kunstner` | `production[].person.role.value` | – |
| `production[].dateFrom` | Date from | text | `1893` | `production[].dateFrom` | – |
| `production[].dateTo` | Date to | text | `1893` | `production[].dateTo` | – |
| `production[].dateFromYear` | From year | integer | `1893` | `production[].dateFromYear` | – |
| `production[].dateToYear` | To year | integer | `1893` | `production[].dateToYear` | – |
| `production[].description` | Note on the production | text | – | `production[].description.value` | – |
| `production[].person.id` | Person id in MuseumPlus | integer | `56154` | `production[].person.personRef` | no |
| `production[].person.uuid` | Person UUID | text | `281F289C-1A53-4727-86F8-A335CB4AB072` | `production[].person.uuid` | no |
| `production[].person.name` | Name | text | `Edvard Munch` | `production[].person._resolved.name` | yes |
| `production[].person.birthYear` | Year of birth | text | `1863` | `production[].person._resolved.birthYear` | no |
| `production[].person.deathYear` | Year of death | text | `1944` | `production[].person._resolved.deathYear` | no |
| `production[].person.certainty` | Certainty of attribution | text | `sikker` | `production[].person.personCertainty.value` | no |
| `production[].place` | Place of production (name, type, certainty) | – | `{name, type, certainty}` | `production[].place._resolved.name` | yes |
| `production[].place.name` | Place name from the place register | – | `Vestlandet (Norge)` | `production[].place._resolved.name` | – |
| `production[].place.type` | Place type, e.g. Place of production | – | `Produksjonssted` | `production[].place.placeType.value` | – |
| `production[].place.certainty` | Certainty, e.g. assumed | – | `antatt` | `production[].place.placeCertainty.value` | – |
| `materials` | Materials | list | `Papplate` | `materials` | yes |
| `techniques` | Techniques | list | `Tempera, Fettstift` | `techniques` | yes |
| `materialTechniqueDescription` | Material and technique as free text | text | `Tempera og fettstift på papplate` | `materialTechniqueDescription` | yes |
| `dimensions` | Dimensions | list | `[{type, value, unit, category}, …]` | `dimensions` | no (strukturert; nettsiden viser publishableDimensions) |
| `dimensions[].type` | Type of measurement | text | `Bredde` | `dimensions[].type.value` | – |
| `dimensions[].value` | Value | integer | `73.5` | `dimensions[].value` | – |
| `dimensions[].unit` | Unit | text | `cm` | `dimensions[].unit.value` | – |
| `dimensions[].category` | Category | text | `Hovedmål` | `dimensions[].category.value` | – |
| `publishableDimensions` | Dimensions as text for publication | text | `91 x 73,5 cm` | `publishableDimensions` | yes |
| `collection` | Collection | text | `Billedkunstsamlingene` | `collection.value` | partly (nettsiden viser også institusjon) |
| `creditLine` | Credit line | text | `Gave fra Olaf Schou 1910` | `creditLine` | yes |
| `keywords` | Subject terms from the catalogue | list | `Bildende kunst` | `keywords` | yes |
| `motifType` | Motif type | list | `Landskap, Portrett` | `motif.type` | yes |
| `classification` | Classification | list | `532 - Bildende kunst` | `classification` | yes |
| `owner` | Owner | text | `Nasjonalmuseet for kunst, arkitektur og design` | `_ownerResolved.name` | yes |
| `inscriptions` | Inscriptions, signatures and stamps | list | `[{type, transcription, position, method, …}, …]` | `inscriptionsLabels` | yes |
| `inscriptions[].type` | Type: Inscription, Signature, Stamp … | text | `Signatur og datering` | `inscriptionsLabels[].type.value` | – |
| `inscriptions[].transcription` | The text as written on the work | text | `E. Munch 1893` | `inscriptionsLabels[].transcription.value` | – |
| `inscriptions[].position` | Position on the work | text | `nede venstre` | `inscriptionsLabels[].position.value` | – |
| `inscriptions[].method` | Method of the inscription | text | – | `inscriptionsLabels[].method.value` | – |
| `inscriptions[].language` | Language | text | – | `inscriptionsLabels[].language.value` | – |
| `inscriptions[].inscriber` | Inscriber | text | – | `inscriptionsLabels[].inscriber.value` | – |
| `inscriptions[].date` | Date of the inscription | text | – | `inscriptionsLabels[].date.value` | – |
| `provenance` | Provenance | list | `[{type, owner, role, certainty, …}, …]` | `provenanceOwnership` | yes |
| `provenance[].type` | Type: Ownership, Accession, Acquisition … | text | `Aksesjon` | `provenanceOwnership[].type.value` | – |
| `provenance[].owner` | Owner's name from the person register | text | `Olaf Schou` | `provenanceOwnership[].owner._resolved.name` | – |
| `provenance[].role` | Role, e.g. [40] Previous owner | text | `[20] Giver/siste eier` | `provenanceOwnership[].owner.role.value` | – |
| `provenance[].certainty` | Certainty | text | `sikker` | `provenanceOwnership[].owner.certainty.value` | – |
| `provenance[].place` | Place from the place register | – | `Elmholt Allé 13, Oslo (fylke) (Norge)` | `provenanceOwnership[].place._resolved.name` | – |
| `provenance[].dateFrom` | From (date text) | text | `1910` | `provenanceOwnership[].dateFrom` | – |
| `provenance[].dateTo` | To (date text) | text | `1910` | `provenanceOwnership[].dateTo` | – |
| `provenance[].dateFromYear` | From year | integer | `1910` | `provenanceOwnership[].dateFromYear` | – |
| `provenance[].dateToYear` | To year | integer | `1910` | `provenanceOwnership[].dateToYear` | – |
| `copyright` | Copyright: holder, manager, status and expiry | list | `[{holder, manager, status, dateTo}, …]` | `copyrights` | yes |
| `copyright[].holder` | Rights holder | text | `Jakob Weidemann` | `copyrights[]._resolved.name` | – |
| `copyright[].manager` | Rights manager, e.g. BONO | – | `BONO` | `copyrights[]._managerResolved.name` | – |
| `copyright[].status` | Status | text | `Aktiv` | `copyrights[].status.value` | – |
| `copyright[].dateTo` | When protection expires | text | `2071-01-01T00.00.00` | `copyrights[].dateTo` | – |
| `publicDomain` | Public domain | boolean | `true` | `publicDomain` | no |
| `multimedia` | Published images | list | `[{imageId, uuid, originalFileName, thumbnail, …}, …]` | `multimedia[] (published images only)` | yes (som bildevisning) |
| `multimedia[].imageId` | Image id (multimediaRef) | integer | `43925` | `multimedia[] (published images only)` | no |
| `multimedia[].uuid` | Image UUID | text | `1040531` | `multimedia[] (published images only)` | no |
| `multimedia[].originalFileName` | File name in the image archive | text | `54318.jpg` | `multimedia[] (published images only)` | no |
| `multimedia[].thumbnail` | Main image | boolean | `false` | `multimedia[] (published images only)` | – |
| `multimedia[].usage` | Usage | text | `Detaljbilde` | `multimedia[] (published images only)` | – |
| `multimedia[].photoCredit` | Photographer | text | `Børre Høstland` | `multimedia[] (published images only)` | yes |
| `multimedia[].creditLine` | Credit line for the image | – | – | `multimedia[] (published images only)` | – |
| `multimedia[].iiifService` | IIIF Image API address | text | `https://ms01.nasjonalmuseet.no/iiif/tif/54318.tif` | `multimedia[] (published images only)` | – |
| `multimedia[].imageUrl` | Image URL (1200 px wide) | text | `https://ms01.nasjonalmuseet.no/iiif/tif/54318.tif/full/12…` | `multimedia[] (published images only)` | – |
| `primaryImage` | Main image (same shape as multimedia[]) | object | `{imageId, uuid, originalFileName, thumbnail, …}` | `multimedia[] (thumbnail` | yes (som bildevisning) |
