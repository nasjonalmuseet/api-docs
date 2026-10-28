# Fields

These are the fields a work has, as `GET /api/v1/objects/{nmId}` delivers them: all the fields at
the open level (pub), the fields ext adds, and briefly full. See also
[Access levels](tilgangsnivaer.md).

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

## How to read the tables

- **Example** is a value from a known work, usually The Scream (NG.M.00939). `{…}` is an object with
  the subfields named, and `[{…}, …]` is a list of them.
- **Source in the catalogue** is the field in the museum's collection management system (MuseumPlus)
  the value comes from, as stored in the database the API reads. `.value` is the catalogue's
  controlled value, and `[]` means each element of a list.
- **On the website** says whether nasjonalmuseet.no shows the field: *yes*, *no*, or *partly* (with what
  is shown). `–` means the field has not been compared.
- `–` under Example means the field is empty for the example works.

## All fields at pub

--8<-- "feltliste_pub.en.md"

## Fields at ext, in addition to pub

Ext is for partners and research and is issued by agreement. Ext has all the fields above, and these:

--8<-- "feltliste_ext.en.md"

## Full

Full is for the museum's own systems and is not available to external users. Full has all works,
including unpublished ones, and these fields in addition (top-level fields only):

--8<-- "feltliste_full.en.md"
