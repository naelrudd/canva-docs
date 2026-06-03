Source: https://www.canva.dev/docs/connect/api-reference/users/get-user/

# Get user

Get the current user's profile.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/users/me

Rate limited to 100 requests per minute.

## Authentication and authorization

Requires scope: `user:read`

## Example request (cURL)

```sh
curl --request GET 'https://api.canva.com/rest/v1/users/me' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `200` with a `user` object: id, name, email, photo.

## Error responses

- **403**: `auth_required`