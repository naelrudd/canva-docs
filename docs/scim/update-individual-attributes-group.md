Source: https://www.canva.dev/docs/scim/update-individual-attributes-group/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/scim/llms.txt
> Use this file to discover all available pages before exploring further.

# Update individual attributes for a group

Updates individual attributes for a group using SCIM PATCH syntax.

The `value` attribute of an operation on the `members` path is an array of users, with each user represented as a `value` attribute that corresponds to the user's Canva SCIM ID.

WARNING: Doing a `replace` operation on the `members` path replaces the entire member list. This should be done in a separate request from any `add` or `remove` operations on group membership.

NOTE: For `add` or `remove` operations, a maximum of 1000 group members are allowed in each `value` array. The `members` array in responses is always empty.

## HTTP method and URL path

PATCH https://www.canva.com/_scim/v2/Groups/{canva_scim_id}

## Header parameters

* `Authorization: Bearer {token}` (required)
* `Content-Type: application/scim+json` (required)

## Path parameters

* `canva_scim_id` (string, required): The Canva-generated SCIM ID for the group.

## Body parameters

* `schemas` (string[], required): Must be `urn:ietf:params:scim:api:messages:2.0:PatchOp`
* `Operations` (object[], required): List of patch operations with:
  * `op` (string, required): `add`, `remove`, or `replace`
  * `path` (string): An attribute path describing the target
  * `value` (object): The value to add, remove, or replace

## Example request (cURL)

```sh
curl --request PATCH 'https://www.canva.com/_scim/v2/Groups/{canva_scim_id}' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/scim+json' \
--data '{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
  "Operations": [
    {"op": "add", "path": "members", "value": [{"value": "UAFdxcd1cdE"}]}
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
