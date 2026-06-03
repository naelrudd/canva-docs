Source: https://www.canva.dev/docs/scim/update-all-information-group/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/scim/llms.txt
> Use this file to discover all available pages before exploring further.

# Update all information for a group

Replaces an existing group's information. You must provide all the information for the group, as if you're creating the group for the first time. Any existing information for the group that isn't provided, including group members, is removed.

The `members` attribute of a group is an array of users, with each user represented as a `value` attribute that corresponds to the user's Canva SCIM ID.

NOTE: A maximum of 1000 group members are allowed in a `PUT` request.

NOTE: The `members` array returned in a group's API response is always empty, even if there are members in the group.

## HTTP method and URL path

PUT https://www.canva.com/_scim/v2/Groups/{canva_scim_id}

## Header parameters

* `Authorization: Bearer {token}` (required)
* `Content-Type: application/scim+json` (required)

## Path parameters

* `canva_scim_id` (string, required): The Canva-generated SCIM ID for the group.

## Body parameters

* `schemas` (string[], required): Must be `urn:ietf:params:scim:schemas:core:2.0:Group`
* `displayName` (string, required): The name of the group
* `members` (object[], required): Array of members with `value` (string, required) — the Canva-generated SCIM ID for the user.

## Example request (cURL)

```sh
curl --request PUT 'https://www.canva.com/_scim/v2/Groups/{canva_scim_id}' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/scim+json' \
--data '{
  "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
  "displayName": "White rabbits",
  "members": [
    {"value": "UAFdxab1abC"}
  ]
}'
```

## Success response (200)

```json
{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"],
  "id": "GAFgrpb1abC",
  "meta": {"resourceType": "Group", "created": "2023-09-18T06:08:35Z"},
  "displayName": "White rabbits",
  "members": []
}
```

## Error responses

* **404 Not found**: `group {canva_scim_id} not found`
* **409 Conflict**: `Group with name {group_name} already exists.`
