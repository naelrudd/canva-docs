Source: https://www.canva.dev/docs/connect/api-reference/folders/list-folder-items/

# List folder items

List the contents of a folder.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/folders/{folderId}/items

Rate limited to 100 requests per minute.

## Authentication and authorization

Requires scope: `folder:read`

## Path parameters

- **folderId** (string, required)

## Query parameters

- **continuation** (string, optional): Pagination token
- **limit** (integer, optional): 1-100, default 50
- **item_types** (string[], optional): `design`, `folder`, `image` (comma-delimited)
- **sort_by** (string, optional): `created_ascending`, `created_descending`, `modified_ascending`, `modified_descending` (default), `title_ascending`, `title_descending`
- **pin_status** (string, optional): `any` (default), `pinned`

## Example request (cURL)

```sh
curl --request GET 'https://api.canva.com/rest/v1/folders/{folderId}/items' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `200` with `items` array (folder/design/image types) and `continuation` token.