Source: https://www.canva.dev/docs/connect/api-reference/designs/get-design/

# Get design

Get the metadata for one of the user's designs.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/designs/{designId}

Rate limited to 100 requests per minute.

## Authentication and authorization

Requires scope: `design:meta:read`

## Path parameters

- **designId** (string, required)

## Example request (cURL)

```sh
curl --request GET 'https://api.canva.com/rest/v1/designs/{designId}' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `200` with a `design` object (same schema as create design response).