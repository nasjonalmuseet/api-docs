| Felt | Beskrivelse | Type | Eksempel | Kilde i katalogen | På Samlingen på nett |
| --- | --- | --- | --- | --- | --- |
| `production[].person.gender` | Kjønn (fra personregisteret) | tekst | `Male` | `production[].person._resolved.gender` | nei |
| `production[].person.nationality` | Nasjonalitet | liste | `Norway` | `production[].person._resolved.nationality` | nei |
| `multimedia[].ai` | KI-nøkkelord og -grupper (berikelse) | objekt | `{keywords, groups}` | `multimedia[] (bare publiserte bilder)` | nei |
| `multimedia[].catalogueTerms` | Katalogtermer per bilde (skrevet av berikelsen) | liste | `Papplate, Tempera, Fettstift, …` | `multimedia[] (bare publiserte bilder)` | nei (skrevet av berikelsen) |
| `multimedia[].enrichmentId` | Id for berikelsen av bildet | – | `723af58e-25bd-425d-8a5d-2ed8ff80d530` | `multimedia[] (bare publiserte bilder)` | – |
| `multimedia[].hasEnrichment` | Om bildet er beriket | boolsk | `true` | `multimedia[] (bare publiserte bilder)` | – |
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
| `onDisplay` | Utstilt nå: rom, utstilling og periode | objekt | `{active, room, exhibition, dateFrom, …}` | `onDisplay.active` | ja («Utstilt i») |
