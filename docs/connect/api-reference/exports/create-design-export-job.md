Source: https://www.canva.dev/docs/connect/api-reference/exports/create-design-export-job/

# Create design export job

Create an asynchronous job to export a design from Canva.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/exports

Rate limited to 20 requests per minute. Additional rate limits: 750 exports per 5 min per integration, 5000 per 24h; 75 per 5 min per document; 75 per 5 min per user, 500 per 24h.

## Authentication and authorization

Requires scope: `design:content:read`

## Body parameters

- **design_id** (string, required)
- **format** (object, required): Type-specific format configuration
  - **pdf**: type "pdf", optional export_quality, size (a4/a3/letter/legal), pages
  - **jpg**: type "jpg", required quality (1-100), optional export_quality, height, width, pages
  - **png**: type "png", optional export_quality, height, width, lossless, transparent_background, as_single_image, pages
  - **pptx**: type "pptx", optional pages
  - **gif**: type "gif", optional export_quality, height, width, pages
  - **mp4**: type "mp4", required quality (horizontal_480p/720p/1080p/4k, vertical_480p/720p/1080p/4k), optional export_quality, pages
  - **html_bundle**: type "html_bundle", optional pages
  - **html_standalone**: type "html_standalone", optional pages
  - **csv**: type "csv", optional pages

## Example request (cURL)

```sh
curl --request POST 'https://api.canva.com/rest/v1/exports' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data '{
  "design_id": "DAVZr1z5464",
  "format": { "type": "pdf", "size": "a4", "pages": [2, 3, 4] }
}'
```

## Success response

Returns `200` with `job` object: id, status, urls (download URLs, valid 24h), error.

## Error codes

- `license_required`, `approval_required`, `internal_failure`
- **400**: `invalid_request`, `bad_request_body`
- **403**: `permission_denied`, `license_required`, `feature_not_available`
- **404**: `design_not_found`
- **429**: `too_many_requests`