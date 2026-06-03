Source: https://www.canva.dev/docs/connect/api-reference/folders/get-folder/

# Get folder

Retrieve a folder's metadata.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/folders/{folderId}

Rate limited to 100 requests per minute.

## Authentication and authorization

Requires scope: `folder:read`

## Path parameters

- **folderId** (string, required)

## Example request (cURL)

```sh
curl --request GET 'https://api.canva.com/rest/v1/folders/{folderId}' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `200` with a `folder` object.