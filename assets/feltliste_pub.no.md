| Felt | Beskrivelse | Type | Eksempel | Kilde i katalogen | På Samlingen på nett |
| --- | --- | --- | --- | --- | --- |
| `nmId` | Verkets identifikator (inventarnummer i URL-form) | tekst | `NG.M.00939` | `nmId` | ja (i adressen) |
| `inventoryNumber` | Inventarnummer | tekst | `NG.M.00939` | `inventoryNumber` | ja |
| `uuid` | Verkets UUID i MuseumPlus | tekst | `C88BFBE7-645D-4EE4-922C-4A3AFA7087F7` | `uuid` | nei |
| `publishable` | Om verket er publisert | boolsk | `true` | `publishable` | – |
| `productionYear` | Første produksjonsår (avledet) | heltall | `1893` | `productionYear` | nei (nettsiden viser labelDate) |
| `productionYearTo` | Siste produksjonsår (avledet) | heltall | `1893` | `productionYearTo` | nei (nettsiden viser labelDate) |
| `mainTitle` | Hovedtittel etter tittelregelen | tekst | `Skrik` | `titles[] (value` | ja (tom tittel: nettsiden viser betegnelsen) |
| `otherTitles` | Øvrige titler | liste | `The Scream` | `titles[] (value` | ja |
| `titles` | Alle publiserte titler med type og språk | liste | `[{title, type, language, dateFrom, …}, …]` | `titles[] (value` | delvis (uten type og datoer) |
| `titles[].title` | Tittelen | tekst | `Skrik` | `titles[] (value` | – |
| `titles[].type` | Titteltype (anvendt, original, produsents tittel) | tekst | `anvendt` | `titles[] (value` | – |
| `titles[].language` | Tittelens språk | tekst | `Norsk` | `titles[] (value` | – |
| `titles[].dateFrom` | Gyldig fra | tekst | – | `titles[] (value` | – |
| `titles[].dateTo` | Gyldig til | tekst | – | `titles[] (value` | – |
| `objectName` | Betegnelse (maleri, tegning, stol …) | tekst | `Maleri` | `objectName.value` | ja |
| `labelDate` | Datering slik den vises på etiketten | tekst | `1893` | `labelDate` | ja |
| `production` | Produsenter og produksjon, i katalogens rekkefølge | liste | `[{type, role, dateFrom, dateTo, …}, …]` | `production` | delvis |
| `production[].type` | Produksjonstype | tekst | `Produsert` | `production[].type.value` | – |
| `production[].role` | Rolle | tekst | `Kunstner` | `production[].person.role.value` | – |
| `production[].dateFrom` | Datering fra | tekst | `1893` | `production[].dateFrom` | – |
| `production[].dateTo` | Datering til | tekst | `1893` | `production[].dateTo` | – |
| `production[].dateFromYear` | Fra år | heltall | `1893` | `production[].dateFromYear` | – |
| `production[].dateToYear` | Til år | heltall | `1893` | `production[].dateToYear` | – |
| `production[].description` | Merknad til produksjonen | tekst | – | `production[].description.value` | – |
| `production[].person.id` | Personens id i MuseumPlus | heltall | `56154` | `production[].person.personRef` | nei |
| `production[].person.uuid` | Personens UUID | tekst | `281F289C-1A53-4727-86F8-A335CB4AB072` | `production[].person.uuid` | nei |
| `production[].person.name` | Navn | tekst | `Edvard Munch` | `production[].person._resolved.name` | ja |
| `production[].person.birthYear` | Fødselsår | tekst | `1863` | `production[].person._resolved.birthYear` | nei |
| `production[].person.deathYear` | Dødsår | tekst | `1944` | `production[].person._resolved.deathYear` | nei |
| `production[].person.certainty` | Sikkerhet for tilskrivningen | tekst | `sikker` | `production[].person.personCertainty.value` | nei |
| `production[].place` | Produksjonssted (navn, type, sikkerhet) | – | `{name, type, certainty}` | `production[].place._resolved.name` | ja |
| `production[].place.name` | Stedsnavn fra stedsregisteret | – | `Vestlandet (Norge)` | `production[].place._resolved.name` | – |
| `production[].place.type` | Stedstype, for eksempel Produksjonssted | – | `Produksjonssted` | `production[].place.placeType.value` | – |
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
| `inscriptions` | Påskrifter, signaturer og stempler | liste | `[{type, transcription, position, method, …}, …]` | `inscriptionsLabels` | ja |
| `inscriptions[].type` | Type: Påskrift, Signatur, Stempel … | tekst | `Signatur og datering` | `inscriptionsLabels[].type.value` | – |
| `inscriptions[].transcription` | Teksten slik den står på verket | tekst | `E. Munch 1893` | `inscriptionsLabels[].transcription.value` | – |
| `inscriptions[].position` | Plassering på verket | tekst | `nede venstre` | `inscriptionsLabels[].position.value` | – |
| `inscriptions[].method` | Teknikk for påskriften | tekst | – | `inscriptionsLabels[].method.value` | – |
| `inscriptions[].language` | Språk | tekst | – | `inscriptionsLabels[].language.value` | – |
| `inscriptions[].inscriber` | Hvem som skrev | tekst | – | `inscriptionsLabels[].inscriber.value` | – |
| `inscriptions[].date` | Datering av påskriften | tekst | – | `inscriptionsLabels[].date.value` | – |
| `provenance` | Proveniens | liste | `[{type, owner, role, certainty, …}, …]` | `provenanceOwnership` | ja |
| `provenance[].type` | Type: Eierskap, Aksesjon, Ervervelse … | tekst | `Aksesjon` | `provenanceOwnership[].type.value` | – |
| `provenance[].owner` | Eierens navn fra personregisteret | tekst | `Olaf Schou` | `provenanceOwnership[].owner._resolved.name` | – |
| `provenance[].role` | Rolle, for eksempel [40] Tidligere eier | tekst | `[20] Giver/siste eier` | `provenanceOwnership[].owner.role.value` | – |
| `provenance[].certainty` | Sikkerhet | tekst | `sikker` | `provenanceOwnership[].owner.certainty.value` | – |
| `provenance[].place` | Sted fra stedsregisteret | – | `Elmholt Allé 13, Oslo (fylke) (Norge)` | `provenanceOwnership[].place._resolved.name` | – |
| `provenance[].dateFrom` | Fra (datotekst) | tekst | `1910` | `provenanceOwnership[].dateFrom` | – |
| `provenance[].dateTo` | Til (datotekst) | tekst | `1910` | `provenanceOwnership[].dateTo` | – |
| `provenance[].dateFromYear` | Fra år | heltall | `1910` | `provenanceOwnership[].dateFromYear` | – |
| `provenance[].dateToYear` | Til år | heltall | `1910` | `provenanceOwnership[].dateToYear` | – |
| `copyright` | Opphavsrett: rettighetshaver, forvalter, status og utløp | liste | `[{holder, manager, status, dateTo}, …]` | `copyrights` | ja |
| `copyright[].holder` | Rettighetshaver | tekst | `Jakob Weidemann` | `copyrights[]._resolved.name` | – |
| `copyright[].manager` | Forvalter, for eksempel BONO | – | `BONO` | `copyrights[]._managerResolved.name` | – |
| `copyright[].status` | Status | tekst | `Aktiv` | `copyrights[].status.value` | – |
| `copyright[].dateTo` | Når vernet går ut | tekst | `2071-01-01T00.00.00` | `copyrights[].dateTo` | – |
| `publicDomain` | Fri bruk | boolsk | `true` | `publicDomain` | nei |
| `multimedia` | Publiserte bilder | liste | `[{imageId, uuid, originalFileName, thumbnail, …}, …]` | `multimedia[] (bare publiserte bilder)` | ja (som bildevisning) |
| `multimedia[].imageId` | Bildets id (multimediaRef) | heltall | `43925` | `multimedia[] (bare publiserte bilder)` | nei |
| `multimedia[].uuid` | Bildets UUID | tekst | `1040531` | `multimedia[] (bare publiserte bilder)` | nei |
| `multimedia[].originalFileName` | Filnavn i bildearkivet | tekst | `54318.jpg` | `multimedia[] (bare publiserte bilder)` | nei |
| `multimedia[].thumbnail` | Hovedbilde | boolsk | `false` | `multimedia[] (bare publiserte bilder)` | – |
| `multimedia[].usage` | Bruk (Standard-bilde o.l.) | tekst | `Detaljbilde` | `multimedia[] (bare publiserte bilder)` | – |
| `multimedia[].photoCredit` | Fotograf | tekst | `Børre Høstland` | `multimedia[] (bare publiserte bilder)` | ja |
| `multimedia[].creditLine` | Kreditering for bildet | – | – | `multimedia[] (bare publiserte bilder)` | – |
| `multimedia[].iiifService` | IIIF Image API-adresse | tekst | `https://ms01.nasjonalmuseet.no/iiif/tif/54318.tif` | `multimedia[] (bare publiserte bilder)` | – |
| `multimedia[].imageUrl` | Bilde-URL (1200 px bredde) | tekst | `https://ms01.nasjonalmuseet.no/iiif/tif/54318.tif/full/12…` | `multimedia[] (bare publiserte bilder)` | – |
| `primaryImage` | Hovedbildet (samme form som multimedia[]) | objekt | `{imageId, uuid, originalFileName, thumbnail, …}` | `multimedia[] (thumbnail` | ja (som bildevisning) |
