# Stabilitet og versjoner

API-et er bygget for å kunne brukes i tjenester som skal leve lenge.

- **`/api/v1` er fryst.** Stier, parametre og felt endres ikke og fjernes ikke.
- **Nye ting kommer i tillegg:** nye felt, nye valgfrie parametre og nye endepunkter. Programmer må tåle felt de ikke kjenner.
- **Fjerning eller omdøping skjer i en ny versjon** (`/api/v2`). Den gamle lever i minst 90 dager etter at den nye finnes, med `Deprecation`, `Sunset` og `Link` i svarene.
- **Unntak:** hvilket tilgangsnivå et endepunkt krever, og om et verk eller bilde er publisert. Et verk som avpubliseres i museets samlingssystem, forsvinner fra API-et.
- **Linked Art-adressene er varige** og kan brukes som lenker. Et verk som avpubliseres, gir `404` på sin adresse, men adressen gjenbrukes aldri.

Kjørende versjon står på <https://api.nasjonalmuseet.no/api/health>.

## Dataene endres

Katalogen er levende. Museet retter, utvider og omskriver opplysninger løpende, og det
kopieres til API-et innen kort tid. Verdier du har lagret lokalt, kan derfor bli utdatert.
