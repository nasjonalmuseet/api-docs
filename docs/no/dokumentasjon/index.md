# Dokumentasjon

Den tekniske referansen for API-et. Veiledningene viser hvordan det brukes i praksis; her
står alle endepunkter, parametre, felt og regler.

## Grunnleggende

| | |
|---|---|
| Adresse | `https://api.nasjonalmuseet.no` |
| Versjon | `/api/v1` (se [Stabilitet](stabilitet.md)) |
| Format | JSON, UTF-8. Linked Art som JSON-LD |
| Nøkkel | Headeren `X-API-Key` |
| Språk | `lang=no` eller `lang=en` |
| Kjørende versjon | `GET /api/health` |

## Endepunkter

Hvert kall kan prøves i [Swagger](https://api.nasjonalmuseet.no/api/docs).

| Endepunkt | Nivå | Beskrivelse |
|---|---|---|
| [`GET /api/v1/objects/{nmId}`](https://api.nasjonalmuseet.no/api/docs#/Objects/get_object_api_v1_objects__nmId__get) | pub | Ett verk |
| [`GET /api/v1/objects`](https://api.nasjonalmuseet.no/api/docs#/Objects/browse_objects_api_v1_objects_get) | pub | Bla i samlingen |
| [`GET /api/v1/objects/text-search`](https://api.nasjonalmuseet.no/api/docs#/Objects/text_search_objects_api_v1_objects_text_search_get) | pub | Søk på ord i katalogen |
| [`GET /api/v1/objects/{nmId}/multimedia`](https://api.nasjonalmuseet.no/api/docs#/Multimedia/list_object_multimedia_api_v1_objects__nmId__multimedia_get) | pub | Verkets bilder (foreløpig: strukturen kan endres) |
| [`GET /api/v1/iiif/manifest/{nmId}.json`](https://api.nasjonalmuseet.no/api/docs#/IIIF/get_manifest_api_v1_iiif_manifest__nmId__json_get) | åpent | IIIF-manifest (foreløpig: kan endres) |
| [`GET /api/linkedart/object/{id}`](https://api.nasjonalmuseet.no/api/docs#/LinkedArt/get_linkedart_object_api_linkedart_object___id__get) | åpent | Linked Art: verk |
| [`GET /api/linkedart/object/text-search`](https://api.nasjonalmuseet.no/api/docs#/LinkedArt/text_search_linkedart_objects_api_linkedart_object_text_search_get) | åpent | Linked Art: søk |
| [`GET /api/v1/objects/linkedart/{nmId}`](https://api.nasjonalmuseet.no/api/docs#/LinkedArt/get_object_linkedart_api_v1_objects_linkedart__nmId__get) | pub | Linked Art med inventarnummer |
| [`POST /api/v1/search/interpret`](https://api.nasjonalmuseet.no/api/docs#/Search/interpret_search_api_v1_search_interpret_post) | pub | Forslag til søketekst og filtre |
| [`POST /api/v1/search/semantic`](https://api.nasjonalmuseet.no/api/docs#/Search/semantic_search_api_v1_search_semantic_post) | ext | Semantisk søk |
| [`POST /api/v1/search/filter`](https://api.nasjonalmuseet.no/api/docs#/Search/filter_search_api_v1_search_filter_post) | ext | Filtrering |
| [`POST /api/v1/search/similar/{imageId}`](https://api.nasjonalmuseet.no/api/docs#/Search/similar_search_api_v1_search_similar__imageId__post) | ext | Lignende bilder |
| [`POST /api/v1/search/explain`](https://api.nasjonalmuseet.no/api/docs#/Search/explain_search_api_v1_search_explain_post) | ext | Hvorfor et bilde traff |
| [`GET /api/health`](https://api.nasjonalmuseet.no/api/docs#/System/health_check_api_health_get) | åpent | Status og versjon |

## Mer

- [Tilgangsnivåer](tilgangsnivaer.md): hva pub, ext og full gir
- [Felt på verket](felt.md): hvert felt, med kilde og eksempel, og feltlista som Excel
- [Feilsvar og grenser](feil-og-grenser.md): 401, 403, 429 og ratebudsjett
- [Stabilitet og versjoner](stabilitet.md)
