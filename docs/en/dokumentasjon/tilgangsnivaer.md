# Access levels

The key decides what you get. Without a key, only a few open addresses are available.

| Level | Who | Works | Endpoints |
|---|---|---|---|
| no key | everyone | no collection data | health, documentation, terms, registration, IIIF manifests, Linked Art |
| **pub** | everyone, self-service | published works and images | look-up, browse, text search, images, IIIF, Linked Art, `interpret` |
| **ext** | partners and research, on application | published works and images | as pub, plus semantic search, filter, similarity and explanation |
| **full** | the museum's own systems | all works | not for external users |

## Fields per level

Each level has all the fields from the level above, plus:

| Level | Fields |
|---|---|
| pub | Catalogue data: id and inventory number, titles, object name, date and production year, producers and place of production, materials and techniques, dimensions, collection, credit line, keywords, motif type, classification, owner, inscriptions, provenance, copyright and published images. **No AI-generated data.** |
| ext | Object type, style period, exhibitions, **on display now** (room and exhibition), and AI keywords on the images |
| full | Not available to external users |

The complete field list per level is in [Fields](felt.md).

## Applying for ext

Send an e-mail to api@nasjonalmuseet.no saying who you are, what the project is and what you
need semantic search or the ext fields for. The museum will reply.
