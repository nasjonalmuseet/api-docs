| Felt | Beskrivelse | Type | Eksempel | Kilde i katalogen | På Samlingen på nett |
| --- | --- | --- | --- | --- | --- |
| `nmId` | Verkets identifikator (inventarnummer i URL-form) | tekst | `NG.M.00939` | `nmId` | ja (i adressen) |
| `inventoryNumber` | Inventarnummer | tekst | `NG.M.00939` | `inventoryNumber` | ja |
| `publishable` | Om verket er publisert | boolsk | `true` | `publishable` | – |
| `productionYear` | Første produksjonsår (avledet) | heltall | `1893` | `productionYear` | nei (nettsiden viser labelDate) |
| `productionYearTo` | Siste produksjonsår (avledet) | heltall | `1893` | `productionYearTo` | nei (nettsiden viser labelDate) |
| `mainTitle` | Hovedtittel etter tittelregelen | tekst | `Skrik` | `titles[] (value` | ja (tom tittel: nettsiden viser betegnelsen) |
| `otherTitles` | Øvrige titler | liste | `The Scream` | `titles[] (value` | ja |
| `titles` | Alle publiserte titler med type og språk | liste | `[{title, language}, …]` | `titles[] (value` | delvis (uten type og datoer) |
| `titles[].title` | Tittelen | tekst | `Skrik` | `titles[] (value` | – |
| `titles[].language` | Tittelens språk | tekst | `Norsk` | `titles[] (value` | – |
| `objectName` | Betegnelse (maleri, tegning, stol …) | tekst | `Maleri` | `objectName.value` | ja |
| `labelDate` | Datering slik den vises på etiketten | tekst | `1893` | `labelDate` | ja |
| `production` | Produsenter og produksjon, i katalogens rekkefølge | liste | `[{type, role, dateFrom, dateTo, …}, …]` | `production` | delvis |
| `production[].type` | Produksjonstype | tekst | `Produsert` | `production[].type.value` | – |
| `production[].role` | Rolle | tekst | `Kunstner` | `production[].person.role.value` | – |
| `production[].dateFrom` | Datering fra | tekst | `1893` | `production[].dateFrom` | – |
| `production[].dateTo` | Datering til | tekst | `1893` | `production[].dateTo` | – |
| `production[].dateFromYear` | Fra år | heltall | `1893` | `production[].dateFromYear` | – |
| `production[].dateToYear` | Til år | heltall | `1893` | `production[].dateToYear` | – |
| `production[].person.id` | Personens id i MuseumPlus | heltall | `56154` | `production[].person.personRef` | nei |
| `production[].person.name` | Navn | tekst | `Edvard Munch` | `production[].person._resolved.name` | ja |
| `production[].person.certainty` | Sikkerhet for tilskrivningen | tekst | `sikker` | `production[].person.personCertainty.value` | nei |
| `production[].place` | Produksjonssted (navn, type, sikkerhet) | – | `{name, certainty}` | `production[].place._resolved.name` | ja |
| `production[].place.name` | Stedsnavn fra stedsregisteret | – | `Vestlandet (Norge)` | `production[].place._resolved.name` | – |
| `production[].place.certainty` | Sikkerhet, for eksempel antatt | – | `antatt` | `production[].place.placeCertainty.value` | – |
| `materials` | Materialer | liste | `Papplate` | `materials` | ja |
| `techniques` | Teknikker | liste | `Tempera, Fettstift` | `techniques` | ja |
| `materialTechniqueDescription` | Materiale og teknikk som fritekst | tekst | `Tempera og fettstift på papplate` | `materialTechniqueDescription` | ja |
| `dimensions` | Mål | liste | `[{type, value, unit, category}, …]` | `dimensions` | nei (strukturert; nettsiden viser publishableDimensions) |
| `dimensions[].type` | Måltype | tekst | `Bredde` | `dimensions[].type.value` | – |
| `dimensions[].value` | Verdi | heltall | `73.5` | `dimensions[].value` | – |
| `dimensions[].unit` | Enhet | tekst | `cm` | `dimensions[].unit.value` | – |
| `dimensions[].category` | Kategori | tekst | `Hovedmål` | `dimensions[].category.value` | – |
| `publishableDimensions` | Mål som tekst for publisering | tekst | `91 x 73,5 cm` | `publishableDimensions` | ja |
| `collection` | Samling | tekst | `Billedkunstsamlingene` | `collection.value` | delvis (nettsiden viser også institusjon) |
| `creditLine` | Kreditering | tekst | `Gave fra Olaf Schou 1910` | `creditLine` | ja |
| `keywords` | Emneord fra katalogen | liste | `Bildende kunst` | `keywords` | ja |
| `motifType` | Motivtype | liste | `Landskap, Portrett` | `motif.type` | ja |
| `classification` | Klassifikasjon | liste | `532 - Bildende kunst` | `classification` | ja |
| `owner` | Eier | tekst | `Nasjonalmuseet for kunst, arkitektur og design` | `_ownerResolved.name` | ja |
| `inscriptions` | Påskrifter, signaturer og stempler | liste | `[{type, transcription, position, method, …}, …]` | `publishingLevel.value` | ja |
| `inscriptions[].type` | Type: Påskrift, Signatur, Stempel … | tekst | `Signatur og datering` | – | – |
| `inscriptions[].transcription` | Teksten slik den står på verket | tekst | `E. Munch 1893` | – | – |
| `inscriptions[].position` | Plassering på verket | tekst | `nede venstre` | – | – |
| `inscriptions[].method` | Teknikk for påskriften | tekst | – | – | – |
| `inscriptions[].inscriber` | Hvem som skrev | tekst | – | – | – |
| `inscriptions[].date` | Datering av påskriften | tekst | – | – | – |
| `provenance` | Proveniens | liste | `[{type, owner, role, certainty, …}, …]` | `publishingLevel.value` | ja |
| `provenance[].type` | Type: Eierskap, Aksesjon, Ervervelse … | tekst | `Aksesjon` | – | – |
| `provenance[].owner` | Eierens navn fra personregisteret | tekst | `Olaf Schou` | – | – |
| `provenance[].role` | Rolle, for eksempel [40] Tidligere eier | tekst | `[20] Giver/siste eier` | – | – |
| `provenance[].certainty` | Sikkerhet | tekst | `sikker` | – | – |
| `provenance[].dateFrom` | Fra (datotekst) | tekst | `1910` | – | – |
| `provenance[].dateTo` | Til (datotekst) | tekst | `1910` | – | – |
| `provenance[].dateFromYear` | Fra år | tekst | `1910` | – | – |
| `provenance[].dateToYear` | Til år | tekst | `1910` | – | – |
| `copyright` | Opphavsrett: rettighetshaver, forvalter, status og utløp | liste | `[{holder, manager, status, dateTo}, …]` | `copyrights` | ja |
| `copyright[].holder` | Rettighetshaver | tekst | `Jakob Weidemann` | `copyrights[]._resolved.name` | – |
| `copyright[].manager` | Forvalter, for eksempel BONO | – | `BONO` | `copyrights[]._managerResolved.name` | – |
| `copyright[].status` | Status | tekst | `Aktiv` | `copyrights[].status.value` | – |
| `copyright[].dateTo` | Når vernet går ut | tekst | `2071-01-01T00.00.00` | `copyrights[].dateTo` | – |
| `publicDomain` | Fri bruk | boolsk | `true` | `publicDomain` | nei |
| `multimedia` | Publiserte bilder | liste | `[{imageId, originalFileName, thumbnail, usage, …}, …]` | `multimedia[] (bare publiserte bilder)` | ja (som bildevisning) |
| `multimedia[].imageId` | Bildets id (multimediaRef) | heltall | `43925` | `multimedia[] (bare publiserte bilder)` | nei |
| `multimedia[].originalFileName` | Filnavn i bildearkivet | tekst | `54318.jpg` | `multimedia[] (bare publiserte bilder)` | nei |
| `multimedia[].thumbnail` | Hovedbilde | boolsk | `false` | `multimedia[] (bare publiserte bilder)` | – |
| `multimedia[].usage` | Bruk (Standard-bilde o.l.) | tekst | `Detaljbilde` | `multimedia[] (bare publiserte bilder)` | – |
| `multimedia[].photoCredit` | Fotograf | tekst | `Børre Høstland` | `multimedia[] (bare publiserte bilder)` | ja |
| `multimedia[].iiifService` | IIIF Image API-adresse | tekst | `https://ms01.nasjonalmuseet.no/iiif/tif/54318.tif` | `multimedia[] (bare publiserte bilder)` | – |
| `multimedia[].imageUrl` | Bilde-URL (1200 px bredde) | tekst | `https://ms01.nasjonalmuseet.no/iiif/tif/54318.tif/full/12…` | `multimedia[] (bare publiserte bilder)` | – |
| `primaryImage` | Hovedbildet (samme form som multimedia[]) | objekt | `{imageId, originalFileName, thumbnail, usage, …}` | `multimedia[] (thumbnail` | ja (som bildevisning) |
