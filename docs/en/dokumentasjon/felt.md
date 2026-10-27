# Fields

These are the fields a work has at the open level (pub), as `GET /api/v1/objects/{nmId}`
delivers them. The fields ext adds are listed under [Access levels](tilgangsnivaer.md).

[Download the field list as Excel](../assets/feltliste.xlsx){ .md-button } (one sheet per
level, with the source in the database and a description in Norwegian and English)

## Rules worth knowing

**Main title (`mainTitle`).** Only titles of the types *applied*, *original* and *producer's
title* are published. The main title is chosen like this:

1. Sami, Kven, Romani and Finnish first.
2. Then the type: applied before original before producer's title.
3. Then the language: Norwegian on Norwegian pages, English on English pages.

If the work has none of the three types, `mainTitle` is empty. Show the object name
(`objectName`) instead, as the Collection Online does.

**Producers (`production[]`).** All producers are listed in the catalogue's order, with role
and date. The API does not choose one main producer.

**Production year (`productionYear`, `productionYearTo`).** Derived from the production date,
otherwise from years in `labelDate`. Used for sorting and filtering. Show `labelDate`.

**Names of owners, places and rights holders.** `owner`, `production[].place`, `provenance[]` and
`copyright[]` carry names from the museum's person and place registers. Previous owners in the
provenance may be private individuals.

**Copyright (`copyright[]`, `publicDomain`).** Shows the rights holder, the manager and when
protection expires. Check these fields before reusing an image, see [Terms](../vilkar.md).

**Images.** Only published images are included. `primaryImage` is the main image.

**No AI data at pub.** The open level contains only catalogue data from the museum's
collection management system.

## All fields at pub

--8<-- "feltliste_pub.en.md"
