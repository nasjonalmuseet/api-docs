# Dokumentasjon for Nasjonalmuseets samlings-API

Kilden til den offentlige dokumentasjonen for <https://api.nasjonalmuseet.no>, på norsk og
engelsk. Publiseres med GitHub Pages ved hver endring på `main`.

## Struktur

| Sti | Innhold |
|---|---|
| `docs/no/`, `docs/en/` | Sidene. Samme filnavn på begge språk |
| `eksempler/` | Kjørbare eksempler. Sidene henter dem inn med `--8<-- "fil"`. Engelske varianter har `.en` før endelsen |
| `assets/` | Stil, feltlista (`feltliste.xlsx`) og felttabellene. Kopieres inn i hvert språk ved bygging |
| `mkdocs.no.yml`, `mkdocs.en.yml` | Ett nettsted per språk, under `/no/` og `/en/` |
| `index.html` | Forsiden, som sender videre til riktig språk |

## Bygge lokalt

```bash
pip install -r requirements.txt
scripts/bygg.sh                     # bygger til site/
python -m http.server -d site 8000  # http://localhost:8000
```

Byggingen kjører i strict-modus: brutte lenker eller manglende eksempelfiler stopper den.

## Eksemplene testes

`scripts/kjor_eksempler.py` kjører alle eksemplene mot API-et. Workflowen «Test eksempler»
gjør det på hver PR og hver mandag, med nøklene i repo-hemmelighetene `NM_API_KEY` (pub) og
`NM_API_KEY_EXT` (ext). Uten nøkler hoppes testen over. Eksempler med `_ext` i navnet krever
ext-nøkkelen.

```bash
NM_API_KEY=… NM_API_KEY_EXT=… python scripts/kjor_eksempler.py
```

## Feltlista kommer fra API-et

Feltlista lages fra visningene i API-v2 og kopieres hit, aldri for hånd:

```bash
python scripts/synk_fra_api.py /sti/til/API-v2
```

Kjør etter hver endring i visningene, og legg resultatet i en PR.

## Endre en side

1. Endre den norske og den engelske siden i samme PR.
2. Står det kode på siden, legg den i `eksempler/` og hent den inn, så blir den testet.
3. Bygg lokalt før PR.

Kontakt: api@nasjonalmuseet.no
