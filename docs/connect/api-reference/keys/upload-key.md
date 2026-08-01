Source: https://www.canva.dev/docs/connect/api-reference/keys/upload-key/

# Upload key

Upload a key for a design. The key file is an XLSX file with field definitions for merge operations.

## HTTP method and URL path

PUT https://api.canva.com/rest/v1/keys/{keyId}

Rate limited to 20 requests per minute.

## Authentication and authorization

Requires scope: `design:content:write`

## Path parameters

- **keyId** (string, required)

## Header parameters

- **Content-Type**: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`

## Body parameters

Binary XLSX data.

## Success response

Returns `201 Created`.

## Error codes

- `invalid_file`, `invalid_key`, `key_not_supported`