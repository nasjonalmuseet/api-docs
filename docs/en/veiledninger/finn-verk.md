# Find works

Three ways to find works with a pub key: look up one work, browse the whole collection, and
search for words.

## When to use what?

| You want to … | Use |
|---|---|
| fetch one specific work | `GET /api/v1/objects/{nmId}` |
| go through works page by page | `GET /api/v1/objects` (browse) |
| find works where a word appears in the title, artist name, object name, technique or keywords | `GET /api/v1/objects/text-search` |
| find works that *resemble* a description ("horse grazing") | [Semantic search](semantisk-sok.md) (ext) |

Think of text search as a search in the catalogue: it finds the words that are there. Semantic
search finds images that resemble the description, even when the words are not in the catalogue.

## Look up one work

```
GET https://api.nasjonalmuseet.no/api/v1/objects/NG.M.00939
```

`nmId` is not case-sensitive: `ng.m.00939` gives the same work. Use the `nmId` from the
response from then on. 404 means that the work does not exist or is not published.

## Browse the collection

`GET /api/v1/objects` gives the works page by page, with `page` and `resultsPerPage` (up to 200,
default 50).

--8<-- "bla.en.py"

The response has `totalResults` (the number of published works) and `data`. Continue until `data` is empty.

!!! tip "The whole dataset"
    The API is made for look-ups and search, not for downloading the whole collection. If you
    need the whole dataset, get in touch at api@nasjonalmuseet.no and we will find a better solution.

## Search for words

`GET /api/v1/objects/text-search?q=…` searches titles, artist names, inventory numbers,
object names, object types, keywords, materials, techniques and dates. The search tolerates
typos and finds word beginnings ("vinterland" finds "vinterlandskap"). The hits are
sorted by relevance, 20 per page by default (`resultsPerPage` up to 100).

=== "curl"

    --8<-- "tekstsok.en.sh"

=== "Python"

    --8<-- "tekstsok.en.py"

=== "JavaScript"

    --8<-- "tekstsok.en.js"

## Common mistakes

- **Compound words are not split.** "fløter" does not find "Tømmerfløtere" (Norwegian for "log drivers"). Search for the whole word, or for its beginning ("tømmerfløt").
- **Text search does not find motifs that are not in the catalogue.** A painting of a horse without "horse" in the title or keywords is found with semantic search, not with text search.

## See also

- [Fields](../dokumentasjon/felt.md): what each field means
- [Documentation](../dokumentasjon/index.md): all parameters
