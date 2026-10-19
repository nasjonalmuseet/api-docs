# Linked Art

[Linked Art](https://linked.art) is an international data model for art and cultural
heritage, built on CIDOC-CRM and delivered as JSON-LD. The works link to artists and to
international vocabularies, such as the Getty AAT. Use Linked Art when you want to connect
the collection with other sources, or use tools that understand linked data.

## When to use it?

| You want to … | Use |
|---|---|
| connect works and artists with other collections and vocabularies | Linked Art |
| show works in an app or web page | [Find works](finn-verk.md): simpler JSON |
| fetch images | [Images and IIIF](bilder.md) |

## Endpoints

Linked Art is open, without a key:

| Endpoint | Gives |
|---|---|
| `GET /api/linkedart/object/text-search?q=…` | Search for works |
| `GET /api/linkedart/object/{id}` | One work (`HumanMadeObject`) |
| `GET /api/linkedart/visual/{id}` | The visual content (`VisualItem`) |
| `GET /api/linkedart/actor/{id}` | A person or group |
| `GET /api/v1/objects/linkedart/{nmId}` | The work by inventory number (requires a key) |

The addresses in the documents' `id` are persistent and can be used as links. Linked Art can
be fetched directly from the browser (CORS is open), with a limit of 120 calls per minute per IP address.

## Example

--8<-- "linked-art.en.sh"

## Common mistakes

- **422:** the id is not a UUID. Use the end of the `id` address, not the inventory number.
- **404:** the work does not exist or is not published.
