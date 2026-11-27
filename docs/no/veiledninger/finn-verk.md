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

Svar (forkortet; `…` betyr at felt er utelatt):

```json
--8<-- "svar-verk.json"
```

`nmId` er ikke følsom for store og små bokstaver: `ng.m.00939` gir samme verk. Bruk
`nmId` fra svaret videre. 404 betyr at verket ikke finnes eller ikke er publisert.

## Bla i samlingen

`GET /api/v1/objects` gir verkene side for side, med `page` og `resultsPerPage` (opptil 200,
standard 50).

```python
--8<-- "bla.py"
```

Svar (forkortet; `…` betyr at felt er utelatt):

```json
--8<-- "svar-bla.json"
```

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

    ```bash
    --8<-- "tekstsok.sh"
    ```

=== "Python"

    ```python
    --8<-- "tekstsok.py"
    ```

=== "JavaScript"

    ```javascript
    --8<-- "tekstsok.js"
    ```

Svar (forkortet; `…` betyr at felt er utelatt):

```json
--8<-- "svar-tekstsok.json"
```

## Finn verk med filter

`POST /api/v1/objects/find` finner verk ut fra verdier i feltene, for eksempel alle malerier fra
1880–1900. Kroppen er et filteruttrykk på feltene slik de står i svaret (som i MongoDB):

```bash
curl -s -X POST -H "X-API-Key: $NM_API_KEY" -H "Content-Type: application/json" \
  -d '{"filter": {"objectName": "Maleri", "productionYear": {"$gte": 1880, "$lte": 1900}},
       "sort": "productionYear", "resultsPerPage": 3}' \
  "https://api.nasjonalmuseet.no/api/v1/objects/find"
```

| I kroppen | Betydning |
|---|---|
| `filter` | Påkrevd. Feltnavn som i svaret, med punktum for underfelt (`production.person.name`) |
| `sort` | `nmId` (standard), `productionYear` eller `mainTitle`; `-` foran gir synkende |
| `page`, `resultsPerPage` | Sider som ved bla, høyst 100 per side |
| `lang` | `no` (standard) eller `en`: språket i svaret og i verdiene filteret ser |

- **Operatorer:** `$and`, `$or`, `$nor`, `$not`, `$eq`, `$ne`, `$in`, `$nin`, `$gt`, `$gte`, `$lt`,
  `$lte`, `$exists`, `$regex` (med `$options`, høyst 100 tegn), `$size` og `$elemMatch`.
- **Tekst og tall:** `labelDate` er fritekst («ca. 1890»). Bruk `productionYear` (tall) for år.
- **Del av tittel:** `{"mainTitle": {"$regex": "^vinter", "$options": "i"}}`.
- **Raskt og tregt:** filter på `objectName`, `productionYear`, `owner`, `motifType`,
  `classification`, `production.place.name` og titlene går raskt. Andre felt kan ta noen sekunder
  for hele samlingen; kombiner dem gjerne med ett av disse.
- **Feil:** ukjent felt eller operator gir `422` med lista over tillatte felt og operatorer.

## Vanlige feil

- **Sammensatte ord deles ikke.** «fløter» finner ikke «Tømmerfløtere». Søk på hele ordet, eller på starten («tømmerfløt»).
- **Tekstsøket finner ikke motiver som ikke står i katalogen.** Et maleri av en hest uten «hest» i tittel eller emneord, finnes med semantisk søk, ikke med tekstsøk.

## Se også

- [Felt på verket](../dokumentasjon/felt.md): hva hvert felt betyr
- [Dokumentasjon](../dokumentasjon/index.md): alle parametre
