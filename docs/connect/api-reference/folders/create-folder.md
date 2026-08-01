Source: https://www.canva.dev/docs/connect/api-reference/folders/create-folder/

# Create folder

Create a new folder in the user's Projects.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/folders

Rate limited to 20 requests per minute.

## Authentication and authorization

Requires scope: `folder:write`

## Body parameters

- **name** (string, required): 1-255 chars
- **parent_folder_id** (string, required): Use `root` or `uploads` or a folder ID, 1-50 chars

## Example request (cURL)

```sh
curl --request POST 'https://api.canva.com/rest/v1/folders' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data '{
  "name": "My awesome holiday",
  "parent_folder_id": "FAF2lZtloor"
}'
```

## Success response

Returns `200` with a `folder` object: id, name, created_at, updated_at, thumbnail.