| Felt | Beskrivelse | Type | På Samlingen på nett |
| --- | --- | --- | --- |
| `nmId` | Verkets identifikator (inventarnummer i URL-form) | tekst | ja (i adressen) |
| `inventoryNumber` | Inventarnummer | tekst | ja |
| `uuid` | Verkets UUID i MuseumPlus | tekst | nei |
| `publishable` | Om verket er publisert | boolsk |  |
| `productionYear` | Første produksjonsår (avledet) | heltall | nei (nettsiden viser labelDate) |
| `productionYearTo` | Siste produksjonsår (avledet) | heltall | nei (nettsiden viser labelDate) |
| `mainTitle` | Hovedtittel etter tittelregelen | tekst | ja (tom tittel: nettsiden viser betegnelsen) |
| `otherTitles` | Øvrige titler | liste | ja |
| `titles` | Alle publiserte titler med type og språk | liste | delvis (uten type og datoer) |
| `titles[].title` | Tittelen | tekst |  |
| `titles[].type` | Titteltype (anvendt, original, produsents tittel) | tekst |  |
| `titles[].language` | Tittelens språk | tekst |  |
| `titles[].dateFrom` | Gyldig fra | tekst |  |
| `titles[].dateTo` | Gyldig til | tekst |  |
| `objectName` | Betegnelse (maleri, tegning, stol …) | tekst | ja |
| `labelDate` | Datering slik den vises på etiketten | tekst | ja |
| `production` | Produsenter og produksjon, i katalogens rekkefølge | liste | delvis |
| `production[].type` | Produksjonstype | tekst |  |
| `production[].role` | Rolle | tekst |  |
| `production[].dateFrom` | Datering fra | tekst |  |
| `production[].dateTo` | Datering til | tekst |  |
| `production[].dateFromYear` | Fra år | heltall |  |
| `production[].dateToYear` | Til år | heltall |  |
| `production[].description` | Merknad til produksjonen | tekst |  |
| `production[].person.id` | Personens id i MuseumPlus | heltall | nei |
| `production[].person.uuid` | Personens UUID | tekst | nei |
| `production[].person.name` | Navn | tekst | ja |
| `production[].person.birthYear` | Fødselsår | tekst | nei |
| `production[].person.deathYear` | Dødsår | tekst | nei |
| `production[].person.gender` | Kjønn (fra personregisteret) | tekst | nei |
| `production[].person.nationality` | Nasjonalitet | liste | nei |
| `production[].person.certainty` | Sikkerhet for tilskrivningen | tekst | nei |
| `production[].place` | Produksjonssted (navn, type, sikkerhet) |  | ja |
| `production[].place.name` | Stedsnavn fra stedsregisteret |  |  |
| `production[].place.type` | Stedstype, for eksempel Produksjonssted |  |  |
| `production[].place.certainty` | Sikkerhet, for eksempel antatt |  |  |
| `materials` | Materialer | liste | ja |
| `techniques` | Teknikker | liste | ja |
| `materialTechniqueDescription` | Materiale og teknikk som fritekst | tekst | ja |
| `dimensions` | Mål | liste | nei (strukturert; nettsiden viser publishableDimensions) |
| `dimensions[].type` | Måltype | tekst |  |
| `dimensions[].value` | Verdi | heltall |  |
| `dimensions[].unit` | Enhet | tekst |  |
| `dimensions[].category` | Kategori | tekst |  |
| `publishableDimensions` | Mål som tekst for publisering | tekst | ja |
| `collection` | Samling | tekst | delvis (nettsiden viser også institusjon) |
| `creditLine` | Kreditering | tekst | ja |
| `keywords` | Emneord fra katalogen | liste | ja |
| `motifType` | Motivtype | liste | ja |
| `classification` | Klassifikasjon | liste | ja |
| `owner` | Eier | tekst | ja |
| `inscriptions` | Påskrifter, signaturer og stempler | liste | ja |
| `inscriptions[].type` | Type: Påskrift, Signatur, Stempel … | tekst |  |
| `inscriptions[].transcription` | Teksten slik den står på verket | tekst |  |
| `inscriptions[].position` | Plassering på verket | tekst |  |
| `inscriptions[].method` | Teknikk for påskriften | tekst |  |
| `inscriptions[].language` | Språk | tekst |  |
| `inscriptions[].inscriber` | Hvem som skrev | tekst |  |
| `inscriptions[].date` | Datering av påskriften | tekst |  |
| `provenance` | Proveniens | liste | ja |
| `provenance[].type` | Type: Eierskap, Aksesjon, Ervervelse … | tekst |  |
| `provenance[].owner` | Eierens navn fra personregisteret | tekst |  |
| `provenance[].role` | Rolle, for eksempel [40] Tidligere eier | tekst |  |
| `provenance[].certainty` | Sikkerhet | tekst |  |
| `provenance[].place` | Sted fra stedsregisteret |  |  |
| `provenance[].dateFrom` | Fra (datotekst) | tekst |  |
| `provenance[].dateTo` | Til (datotekst) | tekst |  |
| `provenance[].dateFromYear` | Fra år | heltall |  |
| `provenance[].dateToYear` | Til år | heltall |  |
| `copyright` | Opphavsrett: rettighetshaver, forvalter, status og utløp | liste | ja |
| `copyright[].holder` | Rettighetshaver | tekst |  |
| `copyright[].manager` | Forvalter, for eksempel BONO |  |  |
| `copyright[].status` | Status | tekst |  |
| `copyright[].dateTo` | Når vernet går ut | tekst |  |
| `publicDomain` | Fri bruk | boolsk | nei |
| `multimedia` | Publiserte bilder | liste | ja (som bildevisning) |
| `multimedia[].imageId` | Bildets id (multimediaRef) | heltall | nei |
| `multimedia[].uuid` | Bildets UUID | tekst | nei |
| `multimedia[].originalFileName` | Filnavn i bildearkivet | tekst | nei |
| `multimedia[].thumbnail` | Hovedbilde | boolsk |  |
| `multimedia[].usage` | Bruk (Standard-bilde o.l.) | tekst |  |
| `multimedia[].photoCredit` | Fotograf | tekst | ja |
| `multimedia[].creditLine` | Kreditering for bildet |  |  |
| `multimedia[].iiifService` | IIIF Image API-adresse | tekst |  |
| `multimedia[].imageUrl` | Bilde-URL (1200 px bredde) | tekst |  |
| `primaryImage` | Hovedbildet (samme form som multimedia[]) | objekt | ja (som bildevisning) |
