| Field | Description | Type |
| --- | --- | --- |
| `nmId` | Identifier of the work (inventory number, URL form) | text |
| `inventoryNumber` | Inventory number | text |
| `uuid` | UUID of the work in MuseumPlus | text |
| `publishable` | Whether the work is published | boolean |
| `productionYear` | First year of production (derived) | integer |
| `productionYearTo` | Last year of production (derived) | integer |
| `mainTitle` | Main title according to the title rule | text |
| `otherTitles` | Other titles | list |
| `titles` | All published titles with type and language | list |
| `titles[].title` | The title | text |
| `titles[].type` | Title type | text |
| `titles[].language` | Language of the title | text |
| `titles[].dateFrom` | Valid from | text |
| `titles[].dateTo` | Valid to | text |
| `objectName` | Object name (painting, drawing, chair …) | text |
| `labelDate` | Date as shown on the label | text |
| `production` | Creators and production, in catalogue order | list |
| `production[].type` | Type of production | text |
| `production[].role` | Role | text |
| `production[].dateFrom` | Date from | text |
| `production[].dateTo` | Date to | text |
| `production[].dateFromYear` | From year | integer |
| `production[].dateToYear` | To year | integer |
| `production[].description` | Note on the production | text |
| `production[].person.id` | Person id in MuseumPlus | integer |
| `production[].person.uuid` | Person UUID | text |
| `production[].person.name` | Name | text |
| `production[].person.birthYear` | Year of birth | text |
| `production[].person.deathYear` | Year of death | text |
| `production[].person.gender` | Gender (from the person register) | text |
| `production[].person.nationality` | Nationality | list |
| `production[].person.certainty` | Certainty of attribution | text |
| `materials` | Materials | list |
| `techniques` | Techniques | list |
| `materialTechniqueDescription` | Material and technique as free text | text |
| `dimensions` | Dimensions | list |
| `dimensions[].type` | Type of measurement | text |
| `dimensions[].value` | Value | integer |
| `dimensions[].unit` | Unit | text |
| `dimensions[].category` | Category | text |
| `publishableDimensions` | Dimensions as text for publication | text |
| `collection` | Collection | text |
| `creditLine` | Credit line | text |
| `keywords` | Subject terms from the catalogue | list |
| `multimedia` | Published images | list |
| `multimedia[].imageId` | Image id (multimediaRef) | integer |
| `multimedia[].uuid` | Image UUID | text |
| `multimedia[].originalFileName` | File name in the image archive | text |
| `multimedia[].thumbnail` | Main image | boolean |
| `multimedia[].usage` | Usage | text |
| `multimedia[].photoCredit` | Photographer | text |
| `multimedia[].creditLine` | Credit line for the image |  |
| `multimedia[].iiifService` | IIIF Image API address | text |
| `multimedia[].imageUrl` | Image URL (1200 px wide) | text |
| `multimedia[].catalogueTerms` | Catalogue terms per image (written by enrichment) |  |
| `primaryImage` | Main image (same shape as multimedia[]) | object |
