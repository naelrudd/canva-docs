Source: https://www.canva.dev/docs/connect/api-reference/folders/update-folder/

# Update folder

Update a folder's metadata (currently only name).

## HTTP method and URL path

PATCH https://api.canva.com/rest/v1/folders/{folderId}

Rate limited to 20 requests per minute.

## Authentication and authorization

Requires scope: `folder:write`

## Path parameters

- **folderId** (string, required)

## Body parameters

- **name** (string, required): 1-255 chars

## Example request (cURL)

```sh
curl --request PATCH 'https://api.canva.com/rest/v1/folders/{folderId}' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data '{
  "name": "My awesome holiday"
}'
```

## Success response

Returns `200` with the updated `folder` object.