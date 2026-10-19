# About

## What is this?

The Nasjonalmuseet collection API gives you the collection as data. It holds the same works you find in the [online collection](https://www.nasjonalmuseet.no/en/collection/), in a format that programs, spreadsheets and research tools can read.

The API covers published works of fine art, design, crafts and architecture, with titles, artists, dates, technique and materials, dimensions, keywords and images. It is free to use. You only need an API key, which you create yourself in a couple of minutes.

## What can I do with it?

- Look up a work by its inventory number, for example `NG.M.00939` (The Scream).
- Browse the whole collection page by page.
- Search for words in titles, artist names and other text fields.
- Get the images in high resolution through IIIF, which works in most cultural heritage image viewers.
- Get the data as Linked Art, for linked data and research.
- Build your own displays, teaching material, art projects, analyses or services, within the terms of use.

## Getting started

1. **Create a key:** <https://api.nasjonalmuseet.no/api/v1/keys/register?lang=en>
   - Enter your name, your e-mail and what you will use the API for, and accept the terms.
   - The key is shown only once, so keep it.
2. **Try it in the browser:**
   - Open <https://api.nasjonalmuseet.no/api/docs>, press **Authorize** and paste the key.
   - You can then try every request with **Try it out**.
3. **Use it in your own code:** send the key in the `X-API-Key` header. It cannot be sent in the URL.

## Five examples

The examples that need a key can be tried in the [documentation](https://api.nasjonalmuseet.no/api/docs). Press **Authorize** and paste the key, open the request named in the example, and press **Try it out**. The code line shows the same request with `curl`, where `$KEY` is your key (`export KEY=…` in the terminal).

**1. One work: The Scream (NG.M.00939)**

In the documentation, open [**Objects → GET /api/v1/objects/{nmId}**](https://api.nasjonalmuseet.no/api/docs#/Objects/get_object_api_v1_objects__nmId__get) with `NG.M.00939` and `lang` = `en`.

```bash
curl -H "X-API-Key: $KEY" "https://api.nasjonalmuseet.no/api/v1/objects/NG.M.00939?lang=en"
```

You get the title, artist, date, technique and materials, dimensions, keywords and images.

**2. Browse the collection**

In the documentation, open [**Objects → GET /api/v1/objects**](https://api.nasjonalmuseet.no/api/docs#/Objects/browse_objects_api_v1_objects_get).

```bash
curl -H "X-API-Key: $KEY" "https://api.nasjonalmuseet.no/api/v1/objects?page=1&resultsPerPage=10&lang=en"
```

**3. Search for a word**

In the documentation, open [**Objects → GET /api/v1/objects/text-search**](https://api.nasjonalmuseet.no/api/docs#/Objects/text_search_objects_api_v1_objects_text_search_get) with `q` = `Munch`.

```bash
curl -H "X-API-Key: $KEY" "https://api.nasjonalmuseet.no/api/v1/objects/text-search?q=Munch&lang=en"
```

**4. The images as IIIF (open, no key)**

<https://api.nasjonalmuseet.no/api/v1/iiif/manifest/NG.M.00939.json>

Paste the address into a IIIF viewer (for example Mirador or Universal Viewer) to zoom into the images.

**5. Linked Art (open, no key)**

<https://api.nasjonalmuseet.no/api/linkedart/object/c88bfbe7-645d-4ee4-922c-4a3afa7087f7>

This is the same work described with the Linked Art model, with links to the artist and to international vocabularies (Getty AAT).

## Glossary

| Term | Meaning |
|---|---|
| **API** | An address that programs can fetch data from, rather than a web page for people to read. |
| **API key** | A personal code sent with every request. You create it yourself on the registration page. It lasts 180 days and can be renewed. |
| **pub** | The level everyone gets: published works with catalogue data and images. |
| **ext** | An extended level for partners and projects. Among other things it gives you **semantic search**. Apply by e-mail. |
| **full** | The level for the museum's own systems. It is not given to external users. |
| **Semantic search** | Search by meaning rather than exact words: "horse grazing" also finds images where those words are not in the title. It is built on machine-generated descriptions of the images, and is therefore not part of the open level. |
| **IIIF** | An international standard for sharing images from museums and archives, with zoom and cropping. |
| **Linked Art** | An international data model for art and cultural heritage, built on linked data (JSON-LD). |
| **Inventory number (nmId)** | The work's number in the collection, for example `NG.M.00939`. It is also shown on the website. |

## Questions and answers

**Does it cost anything?** No.

**Why can't I find a work I know the museum has?** The API only shows works that are published in the online collection.

**How many requests can I make?**
- There is a limit per key and minute, lower for searches than for look-ups.
- The numbers are in the terms of use and may change.
- If the API answers `429`, wait until the time in the `Retry-After` header has passed.

**Can I download the whole collection?** The API is not made for that. If you need the whole dataset, get in touch and we will find a better solution.

**Can I use the numbers from the API as statistics?** The numbers change with ongoing cataloguing and are not official. If you need official figures about the collection, get in touch.

**Can I use the images freely?** Not necessarily. Rights differ from work to work. Check the rights information for each work before you use an image. It is also given in Linked Art and on the website.

**How do I get the ext level?** E-mail api@nasjonalmuseet.no. Say what you will use it for and which key it concerns.

**Will the API change?**
- The current version (`/api/v1`) only gets new fields and new features. Nothing is removed.
- If something has to be removed, that happens in a new version (`/api/v2`), and the old one stays available for at least 90 days.

**I have found an error in the data.** Thank you! E-mail api@nasjonalmuseet.no with the inventory number and what is wrong.

## About the data

The catalogue data comes from a living collection catalogue, with information gathered since the 1830s. The API shows the records as they stand at the moment, and some records may be out of date. Some may contain language or ideas that today may be perceived as outdated, offensive or discriminatory, relating for example to gender, sexuality, ethnicity or disability, and that may be at odds with the museum's values of equality and diversity. The museum works continuously to improve the records and welcomes suggestions for improvement.

Because the numbers change with ongoing cataloguing, extracting official figures and statistics about the collection from the API is discouraged. If you need official figures, contact the museum.

## Contact

**api@nasjonalmuseet.no**: questions, access to the ext level, errors in the data and requests for the whole dataset.

The terms are under [Terms of use](vilkar.md). Tutorials and technical documentation are under [Tutorials](veiledninger/index.md) and [Documentation](dokumentasjon/index.md).
