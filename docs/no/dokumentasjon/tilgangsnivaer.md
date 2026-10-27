# Tilgangsnivåer

Nøkkelen bestemmer hva du får. Uten nøkkel er bare noen få åpne adresser tilgjengelige.

| Nivå | Hvem | Verk | Endepunkter |
|---|---|---|---|
| uten nøkkel | alle | ingen samlingsdata | helse, dokumentasjon, vilkår, registrering, IIIF-manifester, Linked Art |
| **pub** | alle, selvbetjent | publiserte verk og bilder | oppslag, bla, tekstsøk, bilder, IIIF, Linked Art, `interpret` |
| **ext** | partnere og forskning, etter søknad | publiserte verk og bilder | som pub, pluss semantisk søk, filter, likhet og forklaring |
| **full** | museets egne systemer | alle verk | ikke for eksterne |

## Felt per nivå

Hvert nivå har alle feltene fra nivået over, pluss:

| Nivå | Felt |
|---|---|
| pub | Katalogdata: id og inventarnummer, titler, betegnelse, datering og produksjonsår, produsenter og produksjonssted, materialer og teknikker, mål, samling, kreditering, emneord, motivtype, klassifikasjon, eier, påskrifter, proveniens, opphavsrett og publiserte bilder. **Ingen KI-genererte data.** |
| ext | Objekttype, stilperiode, produsentens kjønn og nasjonalitet, utstillinger, **utstilt nå** (rom og utstilling), og på bildene KI-nøkkelord |
| full | Ikke tilgjengelig for eksterne |

Den fullstendige feltlista per nivå står i [Felt på verket](felt.md).

## Søke om ext

Send en e-post til api@nasjonalmuseet.no med hvem du er, prosjektet og hva du trenger
semantisk søk eller ext-feltene til. Du får svar fra museet.
