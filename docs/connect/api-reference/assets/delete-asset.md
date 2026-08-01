Source: https://www.canva.dev/docs/connect/api-reference/assets/delete-asset/

# Delete asset

Delete an asset from the user's Projects.

You can delete an asset by specifying its `assetId`. This operation mirrors the behavior in the Canva UI. Deleting an item moves it to the trash. Deleting an asset doesn't remove it from designs that already use it.

## HTTP method and URL path

DELETE https://api.canva.com/rest/v1/assets/{assetId}

Rate limited to 30 requests per minute for each user of your integration.

## Authentication and authorization

Requires a valid access token with `asset:write` scope.

## Header parameters

* `Authorization`: Bearer token.

## Path parameters

* `assetId` (required): The ID of the asset.

## Success response

Returns a `204 No content` status without a response body.
