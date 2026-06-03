Source: https://www.canva.dev/docs/connect/api-reference/exports/get-design-export-job/

# Get design export job

Get the status and results of an export job, including download URLs.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/exports/{exportId}

Rate limited to 120 requests per minute.

## Authentication and authorization

Requires scope: `design:content:read`

## Path parameters

- **exportId** (string, required)

## Example request (cURL)

```sh
curl --request GET 'https://api.canva.com/rest/v1/exports/{exportId}' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `200` with the `job` object (same schema as create export response).

## Error responses

- **403**: `permission_denied`
- **404**: `not_found` (export expired)