# Documentation

The technical reference for the API. The tutorials show how it is used in practice; here
you find all endpoints, parameters, fields and rules.

## Basics

| | |
|---|---|
| Address | `https://api.nasjonalmuseet.no` |
| Version | `/api/v1` (see [Stability](stabilitet.md)) |
| Format | JSON, UTF-8. Linked Art as JSON-LD |
| Key | The `X-API-Key` header |
| Language | `lang=no` or `lang=en` |
| Running version | `GET /api/health` |

## Endpoints

Every request can be tried in [Swagger](https://api.nasjonalmuseet.no/api/docs).

| Endpoint | Level | Description |
|---|---|---|
| [`GET /api/v1/objects/{nmId}`](https://api.nasjonalmuseet.no/api/docs#/Objects/get_object_api_v1_objects__nmId__get) | pub | One work |
| [`GET /api/v1/objects`](https://api.nasjonalmuseet.no/api/docs#/Objects/browse_objects_api_v1_objects_get) | pub | Browse the collection |
| [`GET /api/v1/objects/text-search`](https://api.nasjonalmuseet.no/api/docs#/Objects/text_search_objects_api_v1_objects_text_search_get) | pub | Search for words in the catalogue |
| [`GET /api/v1/objects/{nmId}/multimedia`](https://api.nasjonalmuseet.no/api/docs#/Multimedia/list_object_multimedia_api_v1_objects__nmId__multimedia_get) | pub | The work's images (preliminary: the structure may change) |
| [`GET /api/v1/iiif/manifest/{nmId}.json`](https://api.nasjonalmuseet.no/api/docs#/IIIF/get_manifest_api_v1_iiif_manifest__nmId__json_get) | open | IIIF manifest (preliminary: may change) |
| [`GET /api/linkedart/object/{id}`](https://api.nasjonalmuseet.no/api/docs#/LinkedArt/get_linkedart_object_api_linkedart_object___id__get) | open | Linked Art: work |
| [`GET /api/linkedart/object/text-search`](https://api.nasjonalmuseet.no/api/docs#/LinkedArt/text_search_linkedart_objects_api_linkedart_object_text_search_get) | open | Linked Art: search |
| [`GET /api/v1/objects/linkedart/{nmId}`](https://api.nasjonalmuseet.no/api/docs#/LinkedArt/get_object_linkedart_api_v1_objects_linkedart__nmId__get) | pub | Linked Art by inventory number |
| [`POST /api/v1/search/interpret`](https://api.nasjonalmuseet.no/api/docs#/Search/interpret_search_api_v1_search_interpret_post) | pub | Suggested search text and filters |
| [`POST /api/v1/objects/find`](https://api.nasjonalmuseet.no/api/docs#/Objects/find_objects_api_v1_objects_find_post) | pub | Look up works with a filter on the fields |
| [`POST /api/v1/search/semantic`](https://api.nasjonalmuseet.no/api/docs#/Search/semantic_search_api_v1_search_semantic_post) | ext | Semantic search |
| [`POST /api/v1/search/filter`](https://api.nasjonalmuseet.no/api/docs#/Search/filter_search_api_v1_search_filter_post) | ext | Filtering |
| [`POST /api/v1/search/similar/{imageId}`](https://api.nasjonalmuseet.no/api/docs#/Search/similar_search_api_v1_search_similar__imageId__post) | ext | Similar images |
| [`POST /api/v1/search/similar`](https://api.nasjonalmuseet.no/api/docs#/Search/similar_search_by_work_api_v1_search_similar_post) | ext | Similar works, from the work's main image |
| [`POST /api/v1/search/explain`](https://api.nasjonalmuseet.no/api/docs#/Search/explain_search_api_v1_search_explain_post) | ext | Why an image matched |
| [`GET /api/health`](https://api.nasjonalmuseet.no/api/docs#/System/health_check_api_health_get) | open | Status and version |

## More

- [Access levels](tilgangsnivaer.md): what pub, ext and full give
- [Fields](felt.md): every field, with source and example, and the field list as Excel
- [Errors and limits](feil-og-grenser.md): 401, 403, 429 and rate budget
- [Stability and versions](stabilitet.md)
