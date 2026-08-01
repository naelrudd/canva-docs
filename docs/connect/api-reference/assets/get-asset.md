Source: https://www.canva.dev/docs/connect/api-reference/assets/get-asset/

# Get asset

Get the metadata for an asset in the user's Project.

You can retrieve the metadata of an asset by specifying its `assetId`.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/assets/{assetId}

Rate limited to 100 requests per minute for each user of your integration.

## Authentication and authorization

Requires a valid access token with `asset:read` scope.

## Header parameters

* `Authorization`: Bearer token.

## Path parameters

* `assetId` (required): The ID of the asset.

## Success response

Returns a `200` response with:
* `asset`: The asset object (type, id, name, tags, owner, thumbnail, metadata, created_at, updated_at).
