# Errors and limits

## Error responses

All errors have the same shape, with a `requestId` you can give if you contact us. It is
also in the `X-Request-ID` header on every response.

```json
{"error": {"status": 401, "message": "…", "requestId": "9c38fd23f4c14471b86c023902341627"}}
```

| Status | Means | Do this |
|---|---|---|
| `400` | Invalid request | Read `message` |
| `401` | Key is missing, invalid, expired or revoked | Send the key in `X-API-Key`. The response has `registerUrl` |
| `403` | The request requires a higher level | Semantic search requires ext. See [Access levels](tilgangsnivaer.md) |
| `404` | The work does not exist, or is not published | Check `nmId` |
| `422` | Error in parameters or body | `details` says which field |
| `429` | Too many requests | Wait as many seconds as `Retry-After` says |
| `5xx` | Error on our side | Try again a little later. If it persists, contact us with the `requestId` |

One exception: when the key is missing, `message` is an object with links to the terms and
the registration page (`registerUrl`, `termsUrl`). Programs that display `message` must handle both forms.

Without a key:

--8<-- "feilsvar.en.sh"

## Rate budget

| Requests | Limit per key |
|---|---|
| Works, browse, text search, IIIF | 120 per minute |
| Images (`/multimedia`) | 60 per minute |
| Search (`/search/*`) | 30 per minute |
| Linked Art (`/api/linkedart/*`) | 120 per minute per IP address |

When the limit is exceeded, the API answers `429` with `Retry-After` (seconds),
`X-RateLimit-Remaining` and `X-RateLimit-Reset`. Wait and try again:

--8<-- "rate.en.py"

If a public service needs more, the key can get its own limit. Contact us.

## Page sizes

| Call | Default | Maximum per page |
|---|---|---|
| `GET /objects` (browse) | 50 | 200 |
| `GET /objects/text-search` | 20 | 100 |
| `POST /objects/find` | 50 | 100, and `(page − 1) × resultsPerPage` at most 20,000 |
| `POST /search/*` | 20 | 100 |

## Caching

Responses are cached for a while. A change in the catalogue can therefore take up to six hours to
show.

| Call | Cached for |
|---|---|
| Works, text search, images and Linked Art | 6 hours |
| `POST /objects/find` | 5 minutes, or 1 hour when the filter must read every work |
| `POST /search/semantic` | 10 minutes |
| `POST /search/filter` | 1 hour |
| `GET /objects` (browse) | Not cached |

## The key

- It lasts 180 days. Renew it on the registration page before it expires.
- Do not share it. Each person or service creates their own.
- Do not put it in the URL (`?api_key=`). It does not work there, and it ends up in logs.
