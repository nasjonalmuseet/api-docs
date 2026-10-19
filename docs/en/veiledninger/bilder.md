# Images and IIIF

The images are on the museum's image server and are fetched with IIIF, an international
standard for sharing images from museums and archives. With IIIF you can ask for exactly the
size and crop you need, instead of downloading the whole file.

## When to use what?

| You want to … | Use |
|---|---|
| show an image on a web page | `primaryImage.imageUrl` (1200 pixels wide) |
| choose size, crop or rotation yourself | `iiifService` with the IIIF Image API |
| show the work in a IIIF viewer with zoom (Mirador, Universal Viewer) | The IIIF manifest |
| find images by content | [Semantic search](semantisk-sok.md), not IIIF |

IIIF gives images and structure, not search. You find the works with [Find works](finn-verk.md).

## Three parts of IIIF

- **Image API:** the image itself, in the size and crop you ask for (`iiifService`).
- **Presentation API:** the manifest, which brings together the work's images and metadata for a viewer.
- **Image viewer:** a program that reads the manifest. You do not need to write code to zoom.

## Step 1: Find the image

Every work has `primaryImage` (the main image) and `multimedia[]` (all published images).

--8<-- "bilder.en.py"

## Step 2: Build a IIIF address

A IIIF Image address has five parts after `iiifService`:

```
{iiifService}/{region}/{size}/{rotation}/{quality}.{format}
```

| Example | Gives |
|---|---|
| `/full/1200,/0/default.jpg` | The whole image, 1200 pixels wide |
| `/full/max/0/default.jpg` | The whole image in full resolution |
| `/pct:0,0,50,50/600,/0/default.jpg` | Upper left quadrant, 600 pixels wide |
| `/square/300,/0/gray.jpg` | Square crop in greyscale, 300 pixels |

## Step 3: Open the manifest in a viewer

The manifest is open, without a key, because image viewers cannot send their own headers:

--8<-- "iiif-manifest.en.sh"

Paste the address (`https://api.nasjonalmuseet.no/api/v1/iiif/manifest/NG.M.00939.json`)
into [Mirador](https://projectmirador.org/) or
[Universal Viewer](https://universalviewer.io/), and you can zoom into the image.

## Common mistakes

- **`imageUrl` is `null`:** the image has no file in the image archive. Skip it.
- **Images are not the same as rights.** That an image can be fetched does not mean it is free to reuse. See [Terms of use](../vilkar.md).
- **Large images:** `full/max` can be very large (gigapixel images). Ask for the width you need.
