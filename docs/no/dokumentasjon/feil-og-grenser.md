# Feilsvar og grenser

## Feilsvar

Alle feil har samme form, med `requestId` som du kan oppgi hvis du kontakter oss. Den står
også i headeren `X-Request-ID` på alle svar.

```json
{"error": {"status": 401, "message": "…", "requestId": "9c38fd23f4c14471b86c023902341627"}}
```

| Status | Betyr | Gjør dette |
|---|---|---|
| `400` | Ugyldig forespørsel | Les `message` |
| `401` | Nøkkel mangler, er ugyldig, utløpt eller tilbakekalt | Send nøkkelen i `X-API-Key`. Svaret har `registerUrl` |
| `403` | Kallet krever et høyere nivå | Semantisk søk krever ext. Se [Tilgangsnivåer](tilgangsnivaer.md) |
| `404` | Verket finnes ikke, eller er ikke publisert | Sjekk `nmId` |
| `422` | Feil i parametre eller kropp | `details` sier hvilket felt |
| `429` | For mange kall | Vent så mange sekunder som `Retry-After` sier |
| `5xx` | Feil hos oss | Prøv igjen litt senere. Vedvarer det, kontakt oss med `requestId` |

Ett unntak: når nøkkelen mangler, er `message` et objekt med lenker til vilkårene og
registreringen (`registerUrl`, `termsUrl`). Programmer som viser `message`, må tåle begge formene.

Uten nøkkel:

--8<-- "feilsvar.sh"

## Ratebudsjett

| Kall | Grense per nøkkel |
|---|---|
| Verk, bla, tekstsøk, IIIF | 120 per minutt |
| Bilder (`/multimedia`) | 60 per minutt |
| Søk (`/search/*`) | 30 per minutt |
| Linked Art (`/api/linkedart/*`) | 120 per minutt per IP-adresse |

Ved overskridelse svarer API-et `429` med `Retry-After` (sekunder), `X-RateLimit-Remaining`
og `X-RateLimit-Reset`. Vent og prøv igjen:

--8<-- "rate.py"

Trenger en offentlig tjeneste mer, kan nøkkelen få egen grense. Kontakt oss.

## Sidestørrelser

| Kall | Standard | Høyst per side |
|---|---|---|
| `GET /objects` (bla) | 50 | 200 |
| `GET /objects/text-search` | 20 | 100 |
| `POST /objects/find` | 50 | 100, og `(page − 1) × resultsPerPage` høyst 20 000 |
| `POST /search/*` | 20 | 100 |

## Mellomlagring

Svarene mellomlagres en tid. En endring i katalogen kan derfor bruke opptil seks timer på å vises.

| Kall | Lagres i |
|---|---|
| Verk, tekstsøk, bilder og Linked Art | 6 timer |
| `POST /objects/find` | 5 minutter, eller 1 time når filteret må lese alle verkene |
| `POST /search/semantic` | 10 minutter |
| `POST /search/filter` | 1 time |
| `GET /objects` (bla) | Lagres ikke |

## Nøkkelen

- Varer i 180 dager. Forny den på registreringssiden før den går ut.
- Del den ikke. Hver person eller tjeneste lager sin egen.
- Legg den ikke i adressen (`?api_key=`). Den virker ikke der, og havner i logger.
