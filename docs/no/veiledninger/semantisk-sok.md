# Semantisk søk

!!! note "Krever ext"
    Semantisk søk, filter, likhet og forklaring krever nivået **ext**, som deles ut til
    partnere og forskningsprosjekter. Søk om det på api@nasjonalmuseet.no.

Semantisk søk finner bilder etter *betydning*, ikke eksakte ord. «To hester bak et gjerde»
finner bilder som viser det, også når ordene ikke står i tittelen.

## Når bør du bruke hva?

| Du vil … | Bruk |
|---|---|
| beskrive et motiv med vanlige ord | `POST /search/semantic` |
| filtrere på verkstype, teknikk, år eller kunstnerens kjønn, uten rangering | `POST /search/filter` |
| finne bilder som ligner et bilde | `POST /search/similar/{imageId}` |
| forstå hvorfor et bilde traff | `POST /search/explain` |
| få et forslag til søketekst og filtre fra en fritekst (pub) | `POST /search/interpret` |
| finne et ord som står i katalogen | [Tekstsøk](finn-verk.md#sk-pa-ord), ikke semantisk søk |

## Slik virker det

Hvert bilde har fått nøkkelord laget av en språkmodell (KI), på norsk og engelsk. Søket
sammenligner søketeksten med dem og rangerer bildene etter likhet. I
tillegg søkes det på ord i katalogen, og de to listene flettes.

Fordi rangeringen bygger på KI-genererte nøkkelord, kan treffene inneholde feil. Det er
derfor ikke på det åpne nivået.

## Steg 1: Søk med en beskrivelse

=== "curl"

    --8<-- "semantisk-sok_ext.sh"

=== "Python"

    --8<-- "semantisk-sok_ext.py"

=== "JavaScript"

    --8<-- "semantisk-sok_ext.js"

Svar (forkortet; `…` betyr at felt er utelatt):

```json
--8<-- "svar-semantisk.json"
```

`lang` velger språket i søket og svaret. Uten `lang` søkes begge språk. Hvert treff har
`score` og `bestMatchImage` (bildet som traff best).

## Steg 2: Avgrens med filtre

Filtrene brukes før rangeringen: `objectName`, `techniques` og `materials` (katalogens
verdier på norsk eller engelsk), `productionDateFrom`/`To` (årstall) og `creatorGender`
(`female`, `male`, `nonBinary`, `unknown`). Uten søketekst, sortert på inventarnummer:

--8<-- "filter_ext.py"

Svar (forkortet; `…` betyr at felt er utelatt):

```json
--8<-- "svar-filter.json"
```

## Steg 3: Finn lignende bilder

--8<-- "likhet_ext.py"

Svar (forkortet; `…` betyr at felt er utelatt):

```json
--8<-- "svar-likhet.json"
```

## Steg 4: Få forslag til søketekst

`/search/interpret` foreslår hvordan en fritekst kan deles i søketekst og filtre. Det søker
ikke, og forslaget brukes bare hvis du velger det. Dette kallet virker også med pub.

--8<-- "tolk.sh"

Svar (forkortet; `…` betyr at felt er utelatt):

```json
--8<-- "svar-tolk.json"
```

## Gode råd

- **Beskriv motivet med flere ord.** «Båt i stormvær» gir bedre treff enn «båt». Fyllord som «et» og «av» gjør ingen skade.
- **Bruk `objectName` når du vil ha en verkstype.** «Maleri av en båt» blir bedre som `query: "båt"` med `filters.objectName: ["Maleri"]`. `/search/interpret` gir det forslaget.
- **Bla med `page` og `hasMore`.** `totalResults` gjelder siden, ikke hele samlingen.
- **Noen søk blokkeres eller skrives om** etter museets søkeregler. Svaret har da `blocked: true` eller `queryRewritten`.

## Vanlige feil

- **403:** nøkkelen er pub. Semantisk søk krever ext.
- **Få treff med `creatorExact`:** navnet må være nøyaktig slik det står i katalogen, for eksempel «Edvard Munch».
