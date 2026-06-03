Source: https://www.canva.dev/docs/scim/delete-group/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/scim/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a group

Deletes a user group. Users in the group are not removed.

## HTTP method and URL path

DELETE https://www.canva.com/_scim/v2/Groups/{canva_scim_id}

## Header parameters

* `Authorization: Bearer {token}` (required)

## Path parameters

* `canva_scim_id` (string, required): The Canva-generated SCIM ID for the group.

## Example request (cURL)

```sh
curl --request DELETE 'https://www.canva.com/_scim/v2/Groups/{canva_scim_id}' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `204 No content` without a response body.

## Error responses

* **404 Not found**: `group {canva_scim_id} not found`
