# Om

## Hva er dette?

Nasjonalmuseets samlings-API gir deg samlingen som data: de samme verkene du finner på [Samlingen på nett](https://www.nasjonalmuseet.no/samlingen/), i et format som programmer, regneark og forskningsverktøy kan lese.

API-et dekker publiserte verk innen billedkunst, design, kunsthåndverk og arkitektur: titler, kunstnere, dateringer, teknikk og materiale, mål, emneord og bilder. Det er gratis å bruke. Du trenger bare en API-nøkkel, og den lager du selv på et par minutter.

## Hva kan jeg gjøre med det?

- Slå opp et verk med inventarnummeret, for eksempel `NG.M.00939` (Skrik).
- Bla gjennom hele samlingen side for side.
- Søke på ord i titler, kunstnernavn og andre tekstfelt.
- Hente bildene i høy oppløsning gjennom IIIF, som fungerer i de fleste bildevisere for kulturarv.
- Hente data som Linked Art, for koblet data og forskning.
- Lage egne visninger, undervisningsopplegg, kunstprosjekter, analyser eller tjenester. Se vilkårene for hva som gjelder.

## Kom i gang

1. **Lag en nøkkel:** <https://api.nasjonalmuseet.no/api/v1/keys/register>. Fyll inn navn, e-post og hva du skal bruke API-et til, og godta vilkårene. Nøkkelen vises én gang, så ta vare på den.
2. **Prøv i nettleseren:** Åpne <https://api.nasjonalmuseet.no/api/docs>, trykk **Authorize** og lim inn nøkkelen. Da kan du prøve alle kallene med **Try it out**.
3. **Bruk den i egne programmer:** Send nøkkelen i headeren `X-API-Key`. Den kan ikke sendes i adressen.

## Fem eksempler

Eksemplene som krever nøkkel, kan prøves i [dokumentasjonen](https://api.nasjonalmuseet.no/api/docs). Trykk **Authorize** og lim inn nøkkelen, åpne kallet som er nevnt, og trykk **Try it out**. Kodelinjen er det samme kallet med `curl`, der `$NOKKEL` er nøkkelen din (`export NOKKEL=…` i terminalen).

**1. Ett verk: Skrik (NG.M.00939)**
I dokumentasjonen: [**Objects → GET /api/v1/objects/{nmId}**](https://api.nasjonalmuseet.no/api/docs#/Objects/get_object_api_v1_objects__nmId__get), med `NG.M.00939`.

```bash
curl -H "X-API-Key: $NOKKEL" https://api.nasjonalmuseet.no/api/v1/objects/NG.M.00939
```

Du får tittel, kunstner, datering, teknikk og materiale, mål, emneord og bilder.

**2. Bla i samlingen**
I dokumentasjonen: [**Objects → GET /api/v1/objects**](https://api.nasjonalmuseet.no/api/docs#/Objects/browse_objects_api_v1_objects_get).

```bash
curl -H "X-API-Key: $NOKKEL" "https://api.nasjonalmuseet.no/api/v1/objects?page=1&resultsPerPage=10"
```

**3. Søk på et ord**
I dokumentasjonen: [**Objects → GET /api/v1/objects/text-search**](https://api.nasjonalmuseet.no/api/docs#/Objects/text_search_objects_api_v1_objects_text_search_get), med `q` = `Munch`.

```bash
curl -H "X-API-Key: $NOKKEL" "https://api.nasjonalmuseet.no/api/v1/objects/text-search?q=Munch"
```

**4. Bildene som IIIF (åpent, ingen nøkkel; foreløpig, kan endres)**
<https://api.nasjonalmuseet.no/api/v1/iiif/manifest/NG.M.00939.json>

Lim adressen inn i en IIIF-viser (for eksempel Mirador eller Universal Viewer), så kan du zoome i bildene.

**5. Linked Art (åpent, ingen nøkkel)**
<https://api.nasjonalmuseet.no/api/linkedart/object/c88bfbe7-645d-4ee4-922c-4a3afa7087f7>

Det samme verket beskrevet med Linked Art-modellen, med lenker til kunstneren og til internasjonale vokabularer (Getty AAT).

## Ordliste

| Ord | Betydning |
|---|---|
| **API** | En adresse som programmer kan hente data fra, i stedet for en nettside som mennesker leser. |
| **API-nøkkel** | En personlig kode som sendes med hvert kall. Den lages selv på registreringssiden og varer i 180 dager. Den kan fornyes. |
| **pub** | Nivået alle får: publiserte verk med katalogdata og bilder. |
| **ext** | Utvidet nivå for samarbeidspartnere og prosjekter. Gir blant annet **semantisk søk**. Søk om det på e-post. |
| **full** | Nivået for museets egne systemer. Det gis ikke til eksterne. |
| **Semantisk søk** | Søk på betydning i stedet for eksakte ord. «Hest på beite» finner også bilder der ordene ikke står i tittelen. Det bygger på maskinelt laget beskrivelse av bildene og er derfor ikke en del av det åpne nivået. |
| **IIIF** | En internasjonal standard for å dele bilder fra museer og arkiver, med zoom og utsnitt. |
| **Linked Art** | En internasjonal datamodell for kunst og kulturarv, bygget på koblet data (JSON-LD). |
| **Inventarnummer (nmId)** | Verkets nummer i samlingen, for eksempel `NG.M.00939`. Det står også på nettsiden. |

## Spørsmål og svar

**Koster det noe?** Nei.

**Hvorfor finner jeg ikke et verk jeg vet museet har?** API-et viser bare verk som er publisert på Samlingen på nett.

**Hvor mange kall kan jeg gjøre?** Det er et tak per nøkkel og minutt, med lavere tall for søk enn for oppslag. Tallene står i vilkårene og kan endres. Svarer API-et `429`, venter du til tiden i headeren `Retry-After` er ute.

**Kan jeg laste ned hele samlingen?** API-et er ikke laget for det. Trenger du hele datasettet, ta kontakt, så finner vi en bedre løsning.

**Kan jeg bruke tallene fra API-et som statistikk?** Tallene endrer seg med katalogarbeidet og er ikke offisielle. Trenger du offisielle tall om samlingen, ta kontakt.

**Kan jeg bruke bildene fritt?** Ikke nødvendigvis. Rettighetene varierer fra verk til verk. Sjekk rettighetsopplysningene for hvert verk (de står også i Linked Art og på nettsiden) før du bruker et bilde.

**Hvordan får jeg ext-nivået?** Send en e-post til api@nasjonalmuseet.no om hva du skal bruke det til og hvilken nøkkel det gjelder.

**Endrer API-et seg?** Den gjeldende versjonen (`/api/v1`) får bare nye felt og nye muligheter. Ingenting fjernes. Må noe fjernes, kommer det i en ny versjon (`/api/v2`), og den gamle lever videre i minst 90 dager.

**Jeg har funnet en feil i dataene.** Takk! Send en e-post til api@nasjonalmuseet.no med inventarnummeret og hva som er feil.

## Om dataene

Katalogdataene kommer fra en levende samlingskatalog med informasjon samlet siden 1830-årene, og API-et viser postene slik de står i øyeblikket. Noen poster kan være utdaterte. Noen kan inneholde språk eller idéer som i dag kan oppleves som utdaterte, støtende eller diskriminerende, knyttet til for eksempel kjønn, seksualitet, etnisitet eller funksjonsnedsettelse, og som kan være i utakt med museets verdier knyttet til likeverd og mangfold. Museet arbeider løpende med å forbedre postene og tar gjerne imot forslag til forbedringer.

API-et viser publiserte poster slik de står i øyeblikket, og tallene endrer seg med katalogarbeidet. Å hente offisielle tall og statistikk om samlingen ut fra API-et frarådes derfor. Trenger du offisielle tall, ta kontakt med museet.

## Kontakt

**api@nasjonalmuseet.no**: spørsmål, tilgang til ext-nivået, feil i data og ønske om hele datasettet.

Vilkårene står under [Vilkår og bruk](vilkar.md). Veiledninger og teknisk dokumentasjon står under [Veiledninger](veiledninger/index.md) og [Dokumentasjon](dokumentasjon/index.md).
