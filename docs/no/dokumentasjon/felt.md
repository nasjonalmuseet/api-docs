# Felt på verket

Dette er feltene et verk har på det åpne nivået (pub), slik `GET /api/v1/objects/{nmId}`
leverer dem. Feltene ext gir i tillegg, står under [Tilgangsnivåer](tilgangsnivaer.md).

[Last ned feltlista som Excel](../assets/feltliste.xlsx){ .md-button } (én fane per nivå,
med kilde i databasen og beskrivelse på norsk og engelsk)

## Regler som er verdt å kjenne

**Hovedtittel (`mainTitle`).** Bare titler av typene *anvendt*, *original* og *produsents
tittel* publiseres. Hovedtittelen velges slik:

1. Samisk, kvensk, romani og finsk først.
2. Deretter typen: anvendt før original før produsents tittel.
3. Deretter språket: norsk på norske sider, engelsk på engelske.

Har verket ingen av de tre typene, er `mainTitle` tom. Vis da betegnelsen (`objectName`),
slik Samlingen på nett gjør.

**Produsenter (`production[]`).** Alle produsentene står i katalogens rekkefølge, med rolle
og datering. API-et velger ikke én hovedprodusent.

**Produksjonsår (`productionYear`, `productionYearTo`).** Avledet fra produksjonsdateringen,
ellers fra årstall i `labelDate`. Brukes til sortering og filtrering. Vis `labelDate`.

**Navn på eier, steder og rettighetshavere.** `owner`, `production[].place`, `provenance[]` og
`copyright[]` har navn fra museets person- og stedsregister. Tidligere eiere i proveniensen kan
være privatpersoner.

**Opphavsrett (`copyright[]`, `publicDomain`).** Viser rettighetshaver, forvalter og når vernet går
ut. Sjekk feltene før du gjenbruker et bilde, se [Vilkår](../vilkar.md).

**Bilder.** Bare publiserte bilder er med. `primaryImage` er hovedbildet.

**Ingen KI-data på pub.** Det åpne nivået inneholder bare katalogdata fra museets
samlingsforvaltningssystem.

## Alle felt på pub

--8<-- "feltliste_pub.no.md"
