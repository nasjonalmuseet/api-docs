# Getting started

This tutorial takes you from nothing to a working request in ten minutes.

## 1. Create a key

Go to <https://api.nasjonalmuseet.no/api/v1/keys/register?lang=en>. Enter your name, e-mail
and what you will use the data for, read the terms and tick the box. The page checks that
you are human without using third-party services.

- The key is **shown once**. Keep it. If you lose it, create a new one.
- It lasts **180 days** and is renewed on the same page.
- It gives the **pub** level: published works, images and text search. See [Access levels](../dokumentasjon/tilgangsnivaer.md).

## 2. Try it in the browser

Open <https://api.nasjonalmuseet.no/api/docs>, press **Authorize** and paste the key.
You can then try every request with **Try it out**, without writing code.

## 3. Your first request

The key is **always** sent in the `X-API-Key` header.

=== "curl"

    --8<-- "forste-kall.en.sh"

=== "Python"

    --8<-- "forste-kall.en.py"

=== "JavaScript"

    --8<-- "forste-kall.en.js"

Response (shortened; `…` marks omitted fields):

```json
--8<-- "svar-verk.en.json"
```

The response is the work *The Scream* (NG.M.00939) as JSON. The most important fields:

| Field | Content |
|---|---|
| `nmId` | The work's id, the same as the inventory number |
| `mainTitle` | The main title |
| `production[].person.name` | The artist or producer |
| `labelDate` | The date as it appears on the label |
| `materialTechniqueDescription` | Material and technique |
| `primaryImage.imageUrl` | The main image, 1200 pixels wide |

`lang=en` gives English values where the catalogue has them.

!!! warning "From a web page"
    The API does not allow calls directly from the browser (no CORS), and the key must not
    be in code sent to visitors. Call the API from your own server and pass on what the web
    page needs. The JavaScript examples are written for Node.js 18 or later.
    Exception: IIIF images and manifests, and Linked Art, can be fetched directly.

## Common mistakes

- **401 even though you have a key:** the header is called `X-API-Key`. Other names, or the key in the URL, do not work.
- **403 on a request:** the request requires a higher level. Semantic search requires ext. See [Access levels](../dokumentasjon/tilgangsnivaer.md).
- **Empty `mainTitle`:** the work has no published title. Use `objectName` (the object name) as the heading, as the website does.

## Next steps

- [Find works](finn-verk.md): browse and search
- [Images and IIIF](bilder.md)
- [Errors and limits](../dokumentasjon/feil-og-grenser.md)
