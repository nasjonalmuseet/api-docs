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
| `inscriptions[].language` | Språk | tekst | – | `inscriptionsLabels[].language.value` | – |
| `provenance[].place` | Sted fra stedsregisteret | – | `Elmholt Allé 13, Oslo (fylke) (Norge)` | `provenanceOwnership[].place._resolved.name` | – |
| `multimedia[].uuid` | Bildets UUID | tekst | `1040531` | `multimedia[] (bare publiserte bilder)` | nei |
| `multimedia[].creditLine` | Kreditering for bildet | – | – | `multimedia[] (bare publiserte bilder)` | – |
| `multimedia[].ai` | KI-data per bilde (berikelse): nøkkelord, grupper, koblede uttrykk (boundTerms), scenesetninger (scene), signaturer og versjoner | objekt | `{keywords, groups, signatures, version}` | `multimedia[] (bare publiserte bilder)` | nei |
| `multimedia[].catalogueTerms` | Katalogtermer per bilde (skrevet av berikelsen) | liste | `Papplate, Tempera, Fettstift, …` | `multimedia[] (bare publiserte bilder)` | nei (skrevet av berikelsen) |
| `multimedia[].enrichmentId` | Id for berikelsen av bildet | – | `723af58e-25bd-425d-8a5d-2ed8ff80d530` | `multimedia[] (bare publiserte bilder)` | – |
| `multimedia[].hasEnrichment` | Om bildet er beriket | boolsk | `true` | `multimedia[] (bare publiserte bilder)` | – |
| `uuid` | Verkets UUID i MuseumPlus | tekst | `C88BFBE7-645D-4EE4-922C-4A3AFA7087F7` | `uuid` | nei |
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
