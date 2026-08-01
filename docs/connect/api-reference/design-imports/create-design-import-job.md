Source: https://www.canva.dev/docs/connect/api-reference/design-imports/create-design-import-job/

# Create design import job

Create an asynchronous job to import an external file as a new design in Canva.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/imports

Rate limited to 20 requests per minute.

## Authentication and authorization

Requires scope: `design:content:write`

## Header parameters

- **Authorization**: `Bearer {token}`
- **Content-Type**: `application/octet-stream`
- **Import-Metadata**: JSON object with `title_base64` (required) and `mime_type` (optional)

## Body parameters

Binary of the file to import.

## Example request (cURL)

```sh
curl --request POST 'https://api.canva.com/rest/v1/imports' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/octet-stream' \
--header 'Import-Metadata: { "title_base64": "TXkgQXdlc29tZSBEZXNpZ24g8J+YjQ==", "mime_type": "application/pdf" }' \
--data-binary '@/path/to/file'
```

## Success response

Returns `200` with a `job` object containing: id, status (failed/in_progress/success), result (designs array), error (if failed).

## Error codes

- `design_creation_throttled`, `design_import_throttled`, `duplicate_import`, `internal_error`, `invalid_file`, `fetch_failed`