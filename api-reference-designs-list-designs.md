Source: https://www.canva.dev/docs/connect/api-reference/designs/list-designs/

# List designs

List all the user's designs with optional search, filtering, and sorting.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/designs

Rate limited to 100 requests per minute.

## Authentication and authorization

Requires scope: `design:meta:read`

## Query parameters

- **query** (string, optional): Search term, max 255 chars
- **continuation** (string, optional): Pagination token
- **ownership** (string, optional): `any` (default), `owned`, or `shared`
- **sort_by** (string, optional): `relevance` (default), `modified_descending`, `modified_ascending`, `title_descending`, `title_ascending`
- **limit** (integer, optional): 1-100, default 25

## Example request (cURL)

```sh
curl --request GET 'https://api.canva.com/rest/v1/designs' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `200` with `items` (array of Design) and `continuation` (string, optional).