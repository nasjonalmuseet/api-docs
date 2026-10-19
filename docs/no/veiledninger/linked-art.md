# Linked Art

[Linked Art](https://linked.art) er en internasjonal datamodell for kunst og kulturarv,
bygget på CIDOC-CRM og levert som JSON-LD. Verkene lenker til kunstnere og til
internasjonale vokabularer, som Getty AAT. Bruk Linked Art når du vil koble samlingen med
andre kilder, eller bruke verktøy som forstår koblet data.

## Når bør du bruke det?

| Du vil … | Bruk |
|---|---|
| koble verk og kunstnere med andre samlinger og vokabularer | Linked Art |
| vise verk i en app eller nettside | [Finn verk](finn-verk.md): enklere JSON |
| hente bilder | [Bilder og IIIF](bilder.md) |

## Endepunkter

Linked Art er åpent, uten nøkkel:

| Endepunkt | Gir |
|---|---|
| `GET /api/linkedart/object/text-search?q=…` | Søk etter verk |
| `GET /api/linkedart/object/{id}` | Ett verk (`HumanMadeObject`) |
| `GET /api/linkedart/visual/{id}` | Bildeinnholdet (`VisualItem`) |
| `GET /api/linkedart/actor/{id}` | En person eller gruppe |
| `GET /api/v1/objects/linkedart/{nmId}` | Verket med inventarnummer (krever nøkkel) |

Adressene i dokumentenes `id` er varige og kan brukes som lenker. Linked Art kan hentes
direkte fra nettleseren (CORS er åpent), med en grense på 120 kall i minuttet per IP-adresse.

## Eksempel

--8<-- "linked-art.sh"

## Vanlige feil

- **422:** id-en er ikke en UUID. Bruk halen av `id`-adressen, ikke inventarnummeret.
- **404:** verket finnes ikke eller er ikke publisert.
