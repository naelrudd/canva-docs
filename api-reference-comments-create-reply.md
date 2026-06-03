Source: https://www.canva.dev/docs/connect/api-reference/comments/create-reply/

# Create reply

Reply to a comment on a design.

<Warning>
  This API is currently provided as a preview. Be aware of the following:

  * There might be unannounced breaking changes.
  * Any breaking changes to preview APIs won't produce a new [API version](https://www.canva.dev/docs/connect/versions/).
  * Public integrations that use preview APIs will not pass the review process, and can't be made available to all Canva users.
</Warning>

Creates a reply to a comment or suggestion thread on a design. Each thread can have a maximum of 100 replies.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/designs/{designId}/comments/{threadId}/replies

Rate limited to 20 requests per minute for each user.

## Authentication and authorization

Requires a valid access token with scope: `comment:write`

## Header parameters

- **Authorization** (string, required): `Bearer {token}`
- **Content-Type** (string, required): `application/json`

## Path parameters

- **designId** (string, required): The design ID.
- **threadId** (string, required): The ID of the thread.

## Body parameters

- **message_plaintext** (string, required): The reply message in plaintext. Minimum: `1`, Maximum: `2048`

## Example request (cURL)

```sh
curl --request POST 'https://api.canva.com/rest/v1/designs/{designId}/comments/{threadId}/replies' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data '{
  "message_plaintext": "Thanks!"
}'
```

## Success response

Returns `200` with a `reply` object containing: id, design_id, thread_id, content, mentions, created_at, updated_at, author.

## Error responses

- **400**: `message_too_long`
- **403**: `too_many_replies`, `permission_denied`
- **404**: `design_not_found`