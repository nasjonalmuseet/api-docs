# Bilder og IIIF

Bildene ligger på museets bildeserver og hentes med IIIF, en internasjonal standard for
å dele bilder fra museer og arkiver. Med IIIF kan du be om akkurat den størrelsen og det
utsnittet du trenger, i stedet for å laste ned hele filen.

## Når bør du bruke hva?

| Du vil … | Bruk |
|---|---|
| vise et bilde på en nettside | `primaryImage.imageUrl` (1200 piksler bredt) |
| velge størrelse, utsnitt eller rotasjon selv | `iiifService` med IIIF Image API |
| vise verket i en IIIF-viser med zoom (Mirador, Universal Viewer) | IIIF-manifestet |
| finne bilder etter innhold | [Semantisk søk](semantisk-sok.md), ikke IIIF |

IIIF gir bilder og struktur, ikke søk. Verkene finner du med [Finn verk](finn-verk.md).

## Tre deler av IIIF

- **Image API:** selve bildet, i størrelsen og utsnittet du ber om (`iiifService`).
- **Presentation API:** manifestet, som samler verkets bilder og metadata for en viser.
- **Bildeviser:** et program som leser manifestet. Du trenger ikke skrive kode for å zoome.

## Steg 1: Finn bildet

Hvert verk har `primaryImage` (hovedbildet) og `multimedia[]` (alle publiserte bilder).

--8<-- "bilder.py"

## Steg 2: Bygg en IIIF-adresse

En IIIF Image-adresse har fem deler etter `iiifService`:

```
{iiifService}/{region}/{size}/{rotation}/{quality}.{format}
```

| Eksempel | Gir |
|---|---|
| `/full/1200,/0/default.jpg` | Hele bildet, 1200 piksler bredt |
| `/full/max/0/default.jpg` | Hele bildet i full oppløsning |
| `/pct:0,0,50,50/600,/0/default.jpg` | Øvre venstre kvadrant, 600 piksler bredt |
| `/square/300,/0/gray.jpg` | Kvadratisk utsnitt i gråtoner, 300 piksler |

## Steg 3: Åpne manifestet i en viser

!!! note "Foreløpig"
    Manifestet er ikke ferdig og kan endres.

Manifestet er åpent, uten nøkkel, fordi bildevisere ikke kan sende egne headere:

--8<-- "iiif-manifest.sh"

Lim adressen (`https://api.nasjonalmuseet.no/api/v1/iiif/manifest/NG.M.00939.json`) inn
i [Mirador](https://projectmirador.org/) eller
[Universal Viewer](https://universalviewer.io/), så kan du zoome i bildet.

## Vanlige feil

- **`imageUrl` er `null`:** bildet mangler fil i bildearkivet. Hopp over det.
- **Bilder er ikke det samme som rettigheter.** At et bilde kan hentes, betyr ikke at det er fritt å gjenbruke. Se [Vilkår og bruk](../vilkar.md).
- **Store bilder:** `full/max` kan være svært store (gigapikselbilder). Be om bredden du trenger.
