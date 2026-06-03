Source: https://www.canva.dev/docs/connect/api-reference/comments/get-thread/

# Get thread

Get metadata for a comment thread.

<Warning>
  This API is currently provided as a preview.
</Warning>

## HTTP method and URL path

GET https://api.canva.com/rest/v1/designs/{designId}/comments/{threadId}

Rate limited to 100 requests per minute.

## Authentication and authorization

Requires scope: `comment:read`

## Path parameters

- **designId** (string, required)
- **threadId** (string, required)

## Example request (cURL)

```sh
curl --request GET 'https://api.canva.com/rest/v1/designs/{designId}/comments/{threadId}' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `200` with a `thread` object (same schema as create thread response) and a deprecated `comment` object.

## Error responses

- **403**: `permission_denied`
- **404**: `thread_not_found`