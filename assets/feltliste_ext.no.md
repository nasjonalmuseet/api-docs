| Felt | Beskrivelse | Type | Eksempel | Kilde i katalogen | På Samlingen på nett |
| --- | --- | --- | --- | --- | --- |
| `titles[].type` | Titteltype (anvendt, original, produsents tittel) | tekst | `anvendt` | `titles[] (value` | – |
| `titles[].dateFrom` | Gyldig fra | tekst | – | `titles[] (value` | – |
| `titles[].dateTo` | Gyldig til | tekst | – | `titles[] (value` | – |
| `production[].description` | Merknad til produksjonen | tekst | – | `production[].description.value` | – |
| `production[].person.uuid` | Personens UUID | tekst | `281F289C-1A53-4727-86F8-A335CB4AB072` | `production[].person.uuid` | nei |
| `production[].person.birthYear` | Fødselsår | tekst | `1863` | `production[].person._resolved.birthYear` | nei |
| `production[].person.deathYear` | Dødsår | tekst | `1944` | `production[].person._resolved.deathYear` | nei |
| `production[].person.gender` | Kjønn (fra personregisteret) | tekst | `Male` | `production[].person._resolved.gender` | nei |
| `production[].person.nationality` | Nasjonalitet | liste | `Norway` | `production[].person._resolved.nationality` | nei |
| `production[].place.type` | Stedstype, for eksempel Produksjonssted | – | `Produksjonssted` | `production[].place.placeType.value` | – |
| `multimedia[].uuid` | Bildets UUID | tekst | `1040531` | `multimedia[] (bare publiserte bilder)` | nei |
| `multimedia[].creditLine` | Kreditering for bildet | – | – | `multimedia[] (bare publiserte bilder)` | – |
| `multimedia[].ai` | KI-data per bilde (berikelse): nøkkelord, grupper, koblede uttrykk (boundTerms), scenesetninger (scene), signaturer og versjoner | objekt | `{keywords, groups, signatures, version}` | `multimedia[] (bare publiserte bilder)` | nei |
| `multimedia[].catalogueTerms` | Katalogtermer per bilde (skrevet av berikelsen) | liste | `Papplate, Tempera, Fettstift, …` | `multimedia[] (bare publiserte bilder)` | nei (skrevet av berikelsen) |
| `multimedia[].enrichmentId` | Id for berikelsen av bildet | – | `723af58e-25bd-425d-8a5d-2ed8ff80d530` | `multimedia[] (bare publiserte bilder)` | – |
| `multimedia[].hasEnrichment` | Om bildet er beriket | boolsk | `true` | `multimedia[] (bare publiserte bilder)` | – |
| `uuid` | Verkets UUID i MuseumPlus | tekst | `C88BFBE7-645D-4EE4-922C-4A3AFA7087F7` | `uuid` | nei |
| `literature` | Litteratur | liste | `[{citation, pageRef, literatureRef}, …]` | `literature` | ja (nivå D) |
| `literature[].citation` | Henvisning i Chicago-stil (kursiv som <i>) | tekst | `Lange, Marit. «Munch as Portrait Painter», i «Edvard Munc…` | `literature[].chicagoCitation` | – |
| `literature[].pageRef` | Side eller katalognummer | tekst | `128.` | `literature[].pageRef` | – |
| `literature[].literatureRef` | Litteraturpostens id i MuseumPlus | heltall | `9310` | `literature[].literatureRef` | – |
| `inscriptions` | Påskrifter, signaturer og stempler | liste | `[{type, primarySecondary, subtype, transcription, …}, …]` | `inscriptionsLabels` | ja |
| `inscriptions[].type` | Type: Påskrift, Signatur, Stempel … | tekst | `Signatur og datering` | `inscriptionsLabels[].type.value` | – |
| `inscriptions[].primarySecondary` | Primær eller sekundær (eventuelt «(usikker)») | tekst | `Primær` | `inscriptionsLabels[].primarySecondary` | – |
| `inscriptions[].subtype` | Undertype, for eksempel «signatur og datering» | tekst | – | `inscriptionsLabels[].subtype.value` | – |
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
| `exhibitions` | Publiserte utstillinger verket har vært med i | – | – | `exhibitions` | ja |
| `exhibitions[].id` | Utstillingens id | – | – | `exhibitions[].exhibitionID` | – |
| `exhibitions[].title` | Utstillingens tittel | – | – | `exhibitions[]._resolved.title` | – |
| `exhibitions[].venue` | Sted | – | – | `exhibitions[]._resolved.venue` | – |
| `exhibitions[].dateFrom` | Fra dato | – | – | `exhibitions[]._resolved.dateFrom` | – |
| `exhibitions[].dateTo` | Til dato | – | – | `exhibitions[]._resolved.dateTo` | – |
| `objectType` | Objekttype (Fine Art, Design, Architecture) | tekst | `Billedkunst` | `objectType.value` | – |
| `entityType` | Enhetstype i MuseumPlus | tekst | `ART` | `entityType` | – |
| `isArtwork` | Om objektet er et kunstverk | boolsk | `true` | `isArtwork` | – |
| `stylePeriod` | Stilperiode | liste | – | `stylePeriod` | – |
