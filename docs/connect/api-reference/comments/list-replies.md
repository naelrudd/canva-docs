Source: https://www.canva.dev/docs/connect/api-reference/comments/list-replies/

# List replies

List the replies to a comment on a design.

<Warning>
  This API is currently provided as a preview.
</Warning>

## HTTP method and URL path

GET https://api.canva.com/rest/v1/designs/{designId}/comments/{threadId}/replies

Rate limited to 100 requests per minute.

## Authentication and authorization

Requires scope: `comment:read`

## Path parameters

- **designId** (string, required)
- **threadId** (string, required)

## Query parameters

- **limit** (integer, optional): 1-100, default 50
- **continuation** (string, optional): Token for pagination

## Example request (cURL)

```sh
curl --request GET 'https://api.canva.com/rest/v1/designs/{designId}/comments/{threadId}/replies' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `200` with `items` (array of Reply) and `continuation` (string, optional).

## Error responses

- **403**: `permission_denied`
- **404**: `design_or_thread_not_found`