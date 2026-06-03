Source: https://www.canva.dev/docs/connect/api-reference/designs/get-design-export-formats/

# Get export formats

Get the export formats available for a design.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/designs/{designId}/export-formats

Rate limited to 100 requests per minute.

## Authentication and authorization

Requires scope: `design:content:read`

## Path parameters

- **designId** (string, required)

## Example request (cURL)

```sh
curl --request GET 'https://api.canva.com/rest/v1/designs/{designId}/export-formats' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `200` with `formats` object containing boolean flags for: pdf, jpg, png, svg, pptx, gif, mp4, html_bundle, html_standalone, csv.

```json
{
  "formats": {
    "pdf": {}, "jpg": {}, "png": {}, "svg": {}, "pptx": {},
    "gif": {}, "mp4": {}, "html_bundle": {}, "html_standalone": {}, "csv": {}
  }
}
```