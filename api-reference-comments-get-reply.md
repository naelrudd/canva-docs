Source: https://www.canva.dev/docs/connect/api-reference/comments/get-reply/

# Get reply

Get a comment reply.

<Warning>
  This API is currently provided as a preview.
</Warning>

## HTTP method and URL path

GET https://api.canva.com/rest/v1/designs/{designId}/comments/{threadId}/replies/{replyId}

Rate limited to 100 requests per minute.

## Authentication and authorization

Requires scope: `comment:read`

## Path parameters

- **designId** (string, required)
- **threadId** (string, required)
- **replyId** (string, required)

## Example request (cURL)

```sh
curl --request GET 'https://api.canva.com/rest/v1/designs/{designId}/comments/{threadId}/replies/{replyId}' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `200` with a `reply` object.

## Error responses

- **403**: `permission_denied`
- **404**: `reply_not_found`