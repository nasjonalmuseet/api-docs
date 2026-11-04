| Field | Description | Type | Example | Source in the catalogue | On the website |
| --- | --- | --- | --- | --- | --- |
| `nmId` | Identifier of the work (inventory number, URL form) | text | `NG.M.00939` | `nmId` | yes (i adressen) |
| `inventoryNumber` | Inventory number | text | `NG.M.00939` | `inventoryNumber` | yes |
| `publishable` | Whether the work is published | boolean | `true` | `publishable` | – |
| `productionYear` | First year of production (derived) | integer | `1893` | `productionYear` | no (nettsiden viser labelDate) |
| `productionYearTo` | Last year of production (derived) | integer | `1893` | `productionYearTo` | no (nettsiden viser labelDate) |
| `mainTitle` | Main title according to the title rule | text | `Skrik` | `titles[] (value` | yes (tom tittel: nettsiden viser betegnelsen) |
| `otherTitles` | Other titles | list | `The Scream` | `titles[] (value` | yes |
| `titles` | All published titles with type and language | list | `[{title, language}, …]` | `titles[] (value` | partly (uten type og datoer) |
| `titles[].title` | The title | text | `Skrik` | `titles[] (value` | – |
| `titles[].language` | Language of the title | text | `Norsk` | `titles[] (value` | – |
| `objectName` | Object name (painting, drawing, chair …) | text | `Maleri` | `objectName.value` | yes |
| `labelDate` | Date as shown on the label | text | `1893` | `labelDate` | yes |
| `production` | Creators and production, in catalogue order | list | `[{type, role, dateFrom, dateTo, …}, …]` | `production` | partly |
| `production[].type` | Type of production | text | `Produsert` | `production[].type.value` | – |
| `production[].role` | Role | text | `Kunstner` | `production[].person.role.value` | – |
| `production[].dateFrom` | Date from | text | `1893` | `production[].dateFrom` | – |
| `production[].dateTo` | Date to | text | `1893` | `production[].dateTo` | – |
| `production[].dateFromYear` | From year | integer | `1893` | `production[].dateFromYear` | – |
| `production[].dateToYear` | To year | integer | `1893` | `production[].dateToYear` | – |
| `production[].person.id` | Person id in MuseumPlus | integer | `56154` | `production[].person.personRef` | no |
| `production[].person.name` | Name | text | `Edvard Munch` | `production[].person._resolved.name` | yes |
| `production[].person.certainty` | Certainty of attribution | text | `sikker` | `production[].person.personCertainty.value` | no |
| `production[].place` | Place of production (name, type, certainty) | – | `{name, certainty}` | `production[].place._resolved.name` | yes |
| `production[].place.name` | Place name from the place register | – | `Vestlandet (Norge)` | `production[].place._resolved.name` | – |
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
| `cataloguingLevel` | Cataloguing level: single object, complex object, grouping, part of object | text | `Enkeltobjekt` | `cataloguingLevel.value` | yes («Registreringsnivå») |
| `publishingLevel` | Publishing level: code A–F and text. The website shows inscriptions, provenance and literature only for D | object | `{code, text}` | `publishingLevel.value` | no (styrer hva som vises) |
| `publishingLevel.code` | Code A–F | text | `D` | `publishingLevel.value` | – |
| `publishingLevel.text` | The level as text, for example «Bestandskatalog (D) Andre nivå katalogisering» | text | `Bestandskatalog (D) Andre nivå katalogisering` | `publishingLevel.value` | – |
| `relatedObjects` | Related published works | list | `[{nmId, title, type}, …]` | `relatedObjects` | yes («Relaterte objekter») |
| `relatedObjects[].nmId` | nmId of the related work | text | `NG.M.00939VERSO` | `_related.nmId` | – |
| `relatedObjects[].title` | Main title of the related work | text | `Skisse til Skrik` | `_related.title` | – |
| `relatedObjects[].type` | Relation: part of, contains, related motif, recto to … | text | `Recto til` | `relatedObjects[].type.value` | – |
| `motifType` | Motif type | list | `Landskap, Portrett` | `motif.type` | yes |
| `classification` | Classification | list | `532 - Bildende kunst` | `classification` | yes |
| `owner` | Owner | text | `Nasjonalmuseet for kunst, arkitektur og design` | `_ownerResolved.name` | yes |
| `inscriptions` | Inscriptions, signatures and stamps | list | `[{type, primarySecondary, subtype, transcription, …}, …]` | `publishingLevel.value` | yes |
| `inscriptions[].type` | Type: Inscription, Signature, Stamp … | text | `Signatur og datering` | – | – |
| `inscriptions[].primarySecondary` | Primary or secondary (possibly «(uncertain)») | text | `Primær` | – | – |
| `inscriptions[].subtype` | Subtype, for example «signature and date» | text | – | – | – |
| `inscriptions[].transcription` | The text as written on the work | text | `E. Munch 1893` | – | – |
| `inscriptions[].position` | Position on the work | text | `nede venstre` | – | – |
| `inscriptions[].method` | Method of the inscription | text | – | – | – |
| `inscriptions[].inscriber` | Inscriber | text | – | – | – |
| `inscriptions[].date` | Date of the inscription | text | – | – | – |
| `provenance` | Provenance | list | `[{type, owner, role, certainty, …}, …]` | `publishingLevel.value` | yes |
| `provenance[].type` | Type: Ownership, Accession, Acquisition … | text | `Aksesjon` | – | – |
| `provenance[].owner` | Owner's name from the person register | text | `Olaf Schou` | – | – |
| `provenance[].role` | Role, e.g. [40] Previous owner | text | `[20] Giver/siste eier` | – | – |
| `provenance[].certainty` | Certainty | text | `sikker` | – | – |
| `provenance[].dateFrom` | From (date text) | text | `1910` | – | – |
| `provenance[].dateTo` | To (date text) | text | `1910` | – | – |
| `provenance[].dateFromYear` | From year | text | `1910` | – | – |
| `provenance[].dateToYear` | To year | text | `1910` | – | – |
| `copyright` | Copyright: holder, manager, status and expiry | list | `[{holder, manager, status, dateTo}, …]` | `copyrights` | yes |
| `copyright[].holder` | Rights holder | text | `Jakob Weidemann` | `copyrights[]._resolved.name` | – |
| `copyright[].manager` | Rights manager, e.g. BONO | – | `BONO` | `copyrights[]._managerResolved.name` | – |
| `copyright[].status` | Status | text | `Aktiv` | `copyrights[].status.value` | – |
| `copyright[].dateTo` | When protection expires | text | `2071-01-01T00.00.00` | `copyrights[].dateTo` | – |
| `publicDomain` | Public domain | boolean | `true` | `publicDomain` | no |
| `literature` | Literature | list | `[{citation, pageRef, literatureRef}, …]` | `publishingLevel.value` | yes (nivå D) |
| `literature[].citation` | Chicago-style citation (italics as <i>) | text | `Lange, Marit. «Munch as Portrait Painter», i «Edvard Munc…` | – | – |
| `literature[].pageRef` | Page or catalogue number | integer | `128.` | – | – |
| `literature[].literatureRef` | Literature record id in MuseumPlus | integer | `9310` | – | – |
| `multimedia` | Published images | list | `[{imageId, originalFileName, thumbnail, usage, …}, …]` | `multimedia[] (published images only)` | yes (som bildevisning) |
| `multimedia[].imageId` | Image id (multimediaRef) | integer | `43925` | `multimedia[] (published images only)` | no |
| `multimedia[].originalFileName` | File name in the image archive | text | `54318.jpg` | `multimedia[] (published images only)` | no |
| `multimedia[].thumbnail` | Main image | boolean | `false` | `multimedia[] (published images only)` | – |
| `multimedia[].usage` | Usage | text | `Detaljbilde` | `multimedia[] (published images only)` | – |
| `multimedia[].photoCredit` | Photographer | text | `Børre Høstland` | `multimedia[] (published images only)` | yes |
| `multimedia[].iiifService` | IIIF Image API address | text | `https://ms01.nasjonalmuseet.no/iiif/tif/54318.tif` | `multimedia[] (published images only)` | – |
| `multimedia[].imageUrl` | Image URL (1200 px wide) | text | `https://ms01.nasjonalmuseet.no/iiif/tif/54318.tif/full/12…` | `multimedia[] (published images only)` | – |
| `primaryImage` | Main image (same shape as multimedia[]) | object | `{imageId, originalFileName, thumbnail, usage, …}` | `multimedia[] (thumbnail` | yes (som bildevisning) |
| `onDisplay` | On display now: room, exhibition and period | object | `{active, room, exhibition, dateFrom, …}` | `onDisplay.active` | yes («Utstilt i») |
| `onDisplay.active` | 1 when the work is on display | integer | `1` | – | – |
| `onDisplay.room` | Room | text | `Rom 060 Samlingspresentasjonen` | `onDisplay.room_no` | – |
| `onDisplay.exhibition` | Exhibition | text | `Edvard Munch` | `onDisplay.exhibition_no` | – |
| `onDisplay.dateFrom` | On display from | text | `2022-06-11T00.00.00` | `onDisplay.dateFrom` | – |
| `onDisplay.dateTo` | On display until | text | `2032-12-31T00.00.00` | `onDisplay.dateTo` | – |
