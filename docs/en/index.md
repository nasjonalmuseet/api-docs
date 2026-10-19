# Nasjonalmuseet Collection API

The collection API of Nasjonalmuseet (The National Museum of Art, Architecture and Design,
Norway) gives you the collection as data: the same works as in
[the Collection Online](https://www.nasjonalmuseet.no/en/collection/), in a format that
programs, spreadsheets and research tools can read. The API is free to use. You need an
API key, which you create yourself in a couple of minutes.

## What you find here

- **Over 60,000 published works** of fine art, design, crafts and architecture
- **Titles, artists, dates, technique, materials, dimensions and keywords** from the museum's catalogue
- **High-resolution images** through IIIF, with zoom and cropping
- **Linked Art** (JSON-LD) for linked data and research
- **Semantic search** in AI-generated image descriptions, for partners and research

## Four parts

<div class="grid cards" markdown>

- **[Tutorials](veiledninger/index.md)**
  Step by step, from the first request to search and images. Start here.

- **[Documentation](dokumentasjon/index.md)**
  Endpoints, access levels, fields, error responses and stability.

- **[Terms of use](vilkar.md)**
  What you can use the data for, credits and data quality.

- **[About](om.md)**
  What the API is, who it is for, glossary and contact.

</div>

## Get started quickly

1. Create a key at <https://api.nasjonalmuseet.no/api/v1/keys/register?lang=en>.
2. Make the first request:

--8<-- "forste-kall.en.sh"

More in [Getting started](veiledninger/kom-i-gang.md).
