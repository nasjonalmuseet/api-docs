# Nasjonalmuseets samlings-API

Nasjonalmuseets samlings-API gir samlingen som data: de samme verkene som på
[Samlingen på nett](https://www.nasjonalmuseet.no/samlingen/), i et format som programmer,
regneark og forskningsverktøy kan lese. API-et er gratis å bruke. Du trenger en API-nøkkel,
og den lager du selv på et par minutter.

## Hva du finner her

- **Over 60 000 publiserte verk** innen billedkunst, design, kunsthåndverk og arkitektur
- **Titler, kunstnere, datering, teknikk, materiale, mål og emneord** fra museets katalog
- **Bilder i høy oppløsning** gjennom IIIF, med zoom og utsnitt
- **Linked Art** (JSON-LD) for koblet data og forskning
- **Semantisk søk** i KI-genererte bildebeskrivelser, for partnere og forskning

## Fire deler

<div class="grid cards" markdown>

- **[Veiledninger](veiledninger/index.md)**
  Steg for steg, fra første kall til søk og bilder. Start her.

- **[Dokumentasjon](dokumentasjon/index.md)**
  Endepunkter, tilgangsnivåer, felt, feilsvar og stabilitet.

- **[Vilkår og bruk](vilkar.md)**
  Hva du kan bruke dataene til, kreditering og datakvalitet.

- **[Om](om.md)**
  Hva API-et er, for hvem, ordliste og kontakt.

</div>

## Kom raskt i gang

1. Lag en nøkkel på <https://api.nasjonalmuseet.no/api/v1/keys/register>.
2. Gjør det første kallet:

--8<-- "forste-kall.sh"

Mer i [Kom i gang](veiledninger/kom-i-gang.md).
