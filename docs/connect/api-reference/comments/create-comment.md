Source: https://www.canva.dev/docs/connect/api-reference/comments/create-comment/

# Create comment (deprecated)

<Warning>
  This preview API is deprecated. You should use the [Create thread](https://www.canva.dev/docs/connect/api-reference/comments/create-thread/) API instead.
</Warning>

Create a new top-level comment on a design. A design can have a maximum of 1000 comments.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/comments

Rate limited to 20 requests per minute.

## Authentication and authorization

Requires scope: `comment:write`

## Body parameters

- **attached_to** (object, required): Contains `type` ("design") and `design_id`
- **message** (string, required): 1-2048 characters
- **assignee_id** (string, optional)

## Example request (cURL)

```sh
curl --request POST 'https://api.canva.com/rest/v1/comments' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data '{
  "attached_to": {
    "design_id": "DAFVztcvd9z",
    "type": "design"
  },
  "message": "Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
  "assignee_id": "oUnPjZ2k2yuhftbWF7873o"
}'
```

## Error responses

- **400**: `bad_request_body`, `message_too_long`
- **403**: `too_many_comments`, `permission_denied`
- **404**: `design_not_found`