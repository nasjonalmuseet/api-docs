# Finn verk

Tre måter å finne verk på med en pub-nøkkel: slå opp ett verk, bla i hele samlingen, og
søke på ord.

## Når bør du bruke hva?

| Du vil … | Bruk |
|---|---|
| hente ett bestemt verk | `GET /api/v1/objects/{nmId}` |
| gå gjennom verk side for side | `GET /api/v1/objects` (bla) |
| finne verk der et ord står i tittel, kunstnernavn, betegnelse, teknikk eller emneord | `GET /api/v1/objects/text-search` |
| finne verk som *ligner* en beskrivelse («hest på beite») | [Semantisk søk](semantisk-sok.md) (ext) |

Tenk på tekstsøket som et søk i katalogen: det finner ordene som står der. Det semantiske
søket finner bilder som ligner beskrivelsen, også når ordene ikke står i katalogen.

## Slå opp ett verk

```
GET https://api.nasjonalmuseet.no/api/v1/objects/NG.M.00939
```

`nmId` er ikke følsom for store og små bokstaver: `ng.m.00939` gir samme verk. Bruk
`nmId` fra svaret videre. 404 betyr at verket ikke finnes eller ikke er publisert.

## Bla i samlingen

`GET /api/v1/objects` gir verkene side for side, med `page` og `resultsPerPage` (opptil 200,
standard 50).

--8<-- "bla.py"

Svaret har `totalResults` (antall publiserte verk) og `data`. Fortsett til `data` er tom.

!!! tip "Hele datasettet"
    API-et er laget for oppslag og søk, ikke for å laste ned hele samlingen. Trenger du
    hele datasettet, ta kontakt på api@nasjonalmuseet.no, så finner vi en bedre løsning.

## Søk på ord

`GET /api/v1/objects/text-search?q=…` søker i titler, kunstnernavn, inventarnummer,
betegnelse, objekttype, emneord, materialer, teknikker og datering. Søket tåler
skrivefeil og finner ordstarter («vinterland» finner «vinterlandskap»). Treffene er
sortert etter relevans, 20 per side som standard (`resultsPerPage` opptil 100).

=== "curl"

    --8<-- "tekstsok.sh"

=== "Python"

    --8<-- "tekstsok.py"

=== "JavaScript"

    --8<-- "tekstsok.js"

## Vanlige feil

- **Sammensatte ord deles ikke.** «fløter» finner ikke «Tømmerfløtere». Søk på hele ordet, eller på starten («tømmerfløt»).
- **Tekstsøket finner ikke motiver som ikke står i katalogen.** Et maleri av en hest uten «hest» i tittel eller emneord, finnes med semantisk søk, ikke med tekstsøk.

## Se også

- [Felt på verket](../dokumentasjon/felt.md): hva hvert felt betyr
- [Dokumentasjon](../dokumentasjon/index.md): alle parametre
