# Stability and versions

The API is built to be used in services that are meant to last.

- **`/api/v1` is frozen.** Paths, parameters and fields are not changed or removed.
- **New things are added on top:** new fields, new optional parameters and new endpoints. Programs must tolerate fields they do not know.
- **Removing or renaming happens in a new version** (`/api/v2`). The old one lives for at least 90 days after the new one exists, with `Deprecation`, `Sunset` and `Link` in the responses.
- **Exceptions:** which access level an endpoint requires, and whether a work or image is published. A work that is unpublished in the museum's collection system disappears from the API.
- **The Linked Art addresses are persistent** and can be used as links. A work that is unpublished gives `404` at its address, but the address is never reused.

The running version is shown at <https://api.nasjonalmuseet.no/api/health>. What has changed is in the
[Changelog](endringslogg.md), and what will be removed under [Deprecated endpoints](avviklet.md).

## The data changes

The catalogue is living. The museum corrects, extends and rewrites information
continuously, and the changes are copied to the API shortly after. Values you have stored
locally may therefore become out of date.
