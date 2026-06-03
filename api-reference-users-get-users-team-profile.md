Source: https://www.canva.dev/docs/connect/api-reference/users/get-users-team-profile/

# Get user's team profile

Get the user's team profile.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/users/me/team-profile

Rate limited to 100 requests per minute.

## Authentication and authorization

Requires scope: `team:read`

## Example request (cURL)

```sh
curl --request GET 'https://api.canva.com/rest/v1/users/me/team-profile' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `200` with a `team_profile` object: team_id, team_name, display_name, role, brand_template_id, brand_kit_id.