Source: https://www.canva.dev/docs/connect/api-reference/folders/move-folder-item/

# Move folder item

Move an item from one folder to another.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/folders/move

Rate limited to 100 requests per minute.

## Authentication and authorization

Requires scope: `folder:write`

## Body parameters

- **to_folder_id** (string, required): Destination folder ID or `root`. 1-50 chars.
- **item_id** (string, required): Item to move. 1-50 chars.

## Example request (cURL)

```sh
curl --request POST 'https://api.canva.com/rest/v1/folders/move' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data '{
  "to_folder_id": "FAF2lZtloor",
  "item_id": "Msd59349ff"
}'
```

## Success response

Returns `204 No content`.