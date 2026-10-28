# Semantic search

!!! note "Requires ext"
    Semantic search, filter, similarity and explanation require the **ext** level, which is
    given to partners and research projects. Apply at api@nasjonalmuseet.no.

Semantic search finds images by *meaning*, not exact words. "Two horses behind a fence"
finds images that show that, even when the words are not in the title.

## When to use what?

| You want to … | Use |
|---|---|
| describe a motif in plain words | `POST /search/semantic` |
| filter on object name, technique, year or the artist's gender, without ranking | `POST /search/filter` |
| find images that resemble an image | `POST /search/similar/{imageId}` |
| understand why an image matched | `POST /search/explain` |
| get a suggested search text and filters from free text (pub) | `POST /search/interpret` |
| find a word that is in the catalogue | [Text search](finn-verk.md#search-for-words), not semantic search |

## How it works

Every image has been given keywords made by a language model (AI), in Norwegian and English.
The search compares the search text with them and ranks the images by similarity. In
addition, words in the catalogue are searched, and the two lists are merged.

Because the ranking is built on AI-generated keywords, the hits may contain errors. That is
why it is not part of the open level.

## Step 1: Search with a description

=== "curl"

    --8<-- "semantisk-sok_ext.en.sh"

=== "Python"

    --8<-- "semantisk-sok_ext.en.py"

=== "JavaScript"

    --8<-- "semantisk-sok_ext.en.js"

Response (shortened; `…` marks omitted fields):

```json
--8<-- "svar-semantisk.en.json"
```

`lang` chooses the language of the search and the response. Without `lang`, both languages
are searched. Each hit has `score` and `bestMatchImage` (the image that matched best).

## Step 2: Narrow down with filters

The filters are applied before the ranking: `objectName`, `techniques` and `materials` (the
catalogue's values in Norwegian or English), `productionDateFrom`/`To` (years) and
`creatorGender` (`female`, `male`, `nonBinary`, `unknown`). Without a search text, sorted by
inventory number:

--8<-- "filter_ext.en.py"

Response (shortened; `…` marks omitted fields):

```json
--8<-- "svar-filter.en.json"
```

## Step 3: Find similar images

--8<-- "likhet_ext.en.py"

Response (shortened; `…` marks omitted fields):

```json
--8<-- "svar-likhet.en.json"
```

## Step 4: Get a suggested search text

`/search/interpret` suggests how a free text can be split into a search text and filters. It
does not search, and the suggestion is only used if you choose it. This request also works
with pub.

--8<-- "tolk.en.sh"

Response (shortened; `…` marks omitted fields):

```json
--8<-- "svar-tolk.en.json"
```

## Good advice

- **Describe the motif with several words.** "Boat in a storm" gives better hits than "boat". Filler words such as "a" and "of" do no harm.
- **Use `objectName` when you want a type of work.** "Painting of a boat" works better as `query: "boat"` with `filters.objectName: ["Painting"]`. `/search/interpret` gives that suggestion.
- **Page with `page` and `hasMore`.** `totalResults` applies to the page, not the whole collection.
- **Some searches are blocked or rewritten** according to the museum's search rules. The response then has `blocked: true` or `queryRewritten`.

## Common mistakes

- **403:** the key is pub. Semantic search requires ext.
- **Few hits with `creatorExact`:** the name must be exactly as it is in the catalogue, for example "Edvard Munch".
