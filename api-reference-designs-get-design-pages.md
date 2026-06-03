Source: https://www.canva.dev/docs/connect/api-reference/designs/get-design-pages/

# Get design pages

Get metadata for pages in a design.

<Warning>This API is currently provided as a preview.</Warning>

## HTTP method and URL path

GET https://api.canva.com/rest/v1/designs/{designId}/pages

Rate limited to 100 requests per minute.

## Authentication and authorization

Requires scope: `design:content:read`

## Query parameters

- **offset** (integer, optional): 1-based page index, default 1, max 500
- **limit** (integer, optional): Number of pages, default 50, max 200

## Example request (cURL)

```sh
curl --request GET 'https://api.canva.com/rest/v1/designs/{designId}/pages' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `200` with `items` array containing: page_number, dimensions (width, height), thumbnail.