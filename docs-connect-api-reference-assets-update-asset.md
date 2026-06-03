Source: https://www.canva.dev/docs/connect/api-reference/assets/update-asset/

# Update asset

Update the metadata for an asset in the users Projects.

You can update the name and tags of an asset by specifying its `assetId`. Updating the tags replaces all existing tags of the asset.

## HTTP method and URL path

PATCH https://api.canva.com/rest/v1/assets/{assetId}

Rate limited to 30 requests per minute for each user of your integration.

## Authentication and authorization

Requires a valid access token with `asset:write` scope.

## Header parameters

* `Authorization`: Bearer token.
* `Content-Type`: Must be `application/json`.

## Path parameters

* `assetId` (required): The ID of the asset.

## Body parameters

* `name` (optional): The name of the asset (max 50 characters).
* `tags` (optional): The replacement tags for the asset (max 50 items).

## Success response

Returns a `200` response with the updated asset object.
