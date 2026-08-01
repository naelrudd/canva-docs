Source: https://www.canva.dev/docs/connect/api-reference/folders/delete-folder/

# Delete folder

Delete a folder. Moves user's content to Trash; other users' content moves to their Projects root.

## HTTP method and URL path

DELETE https://api.canva.com/rest/v1/folders/{folderId}

Rate limited to 20 requests per minute.

## Authentication and authorization

Requires scope: `folder:write`

## Path parameters

- **folderId** (string, required)

## Example request (cURL)

```sh
curl --request DELETE 'https://api.canva.com/rest/v1/folders/{folderId}' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `204 No content`.