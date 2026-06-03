Source: https://www.canva.dev/docs/connect/api-reference/comments/create-thread/

# Create thread

Create a new comment thread on a design.

<Warning>
  This API is currently provided as a preview. Be aware of the following:

  * There might be unannounced breaking changes.
  * Any breaking changes to preview APIs won't produce a new [API version](https://www.canva.dev/docs/connect/versions/).
  * Public integrations that use preview APIs will not pass the review process, and can't be made available to all Canva users.
</Warning>

Creates a new comment thread on a design.
For information on comments and how they're used in the Canva UI, see the
[Canva Help Center](https://www.canva.com/help/comments/).

## HTTP method and URL path

POST https://api.canva.com/rest/v1/designs/{designId}/comments

This operation is rate limited to 100 requests per minute for each user of your integration.

## Authentication and authorization

This endpoint requires a valid access token that acts on behalf of a user.

### Scopes

The access token must have all the following [scopes](/docs/connect/appendix/scopes) (permissions):

* `comment:write`

## Header parameters

- **Authorization** (string, required): Provides credentials to authenticate the request, in the form of a `Bearer` token. For example: `Authorization: Bearer {token}`
- **Content-Type** (string, required): Indicates the media type of the information sent in the request. This must be set to `application/json`. For example: `Content-Type: application/json`

## Path parameters

- **designId** (string, required): The design ID.

## Body parameters

- **message_plaintext** (string, required): The comment message in plaintext. This is the comment body shown in the Canva UI. You can also mention users in your message by specifying their User ID and Team ID using the format `[user_id:team_id]`. If the `assignee_id` parameter is specified, you must mention the assignee in the message. Minimum length: `1`, Maximum length: `2048`
- **assignee_id** (string): Lets you assign the comment to a Canva user using their User ID. You *must* mention the assigned user in the `message`.

## Example request (cURL)

```sh
curl --request POST 'https://api.canva.com/rest/v1/designs/{designId}/comments' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data '{
  "message_plaintext": "Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
  "assignee_id": "oUnPjZ2k2yuhftbWF7873o"
}'
```

## Success response

If successful, the endpoint returns a `200` response with a JSON body with the `thread` object containing:
- **id**: The ID of the thread
- **design_id**: The ID of the design
- **thread_type**: The type of the discussion thread (comment or suggestion)
- **created_at**: Unix timestamp
- **updated_at**: Unix timestamp
- **author**: User metadata (optional)

## Example response

```json
{
  "thread": {
    "id": "KeAbiEAjZEj",
    "design_id": "DAFVztcvd9z",
    "thread_type": {
      "type": "comment",
      "content": {
        "plaintext": "Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
        "markdown": "*_Great work_* [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!"
      },
      "mentions": { ... },
      "assignee": { "id": "...", "display_name": "John Doe" },
      "resolver": { "id": "...", "display_name": "John Doe" }
    },
    "author": { "id": "...", "display_name": "John Doe" },
    "created_at": 1692928800,
    "updated_at": 1692928900
  }
}
```

## Error responses

- **400 Bad Request**: `bad_request_body` (e.g., "Assignee must be mentioned in comment content"), `message_too_long`
- **403 Forbidden**: `too_many_comments`, `permission_denied`
- **404 Not Found**: `design_not_found`