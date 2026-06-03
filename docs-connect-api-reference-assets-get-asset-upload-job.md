Source: https://www.canva.dev/docs/connect/api-reference/assets/get-asset-upload-job/

# Get asset upload job

Get the status and results of an upload asset job.

Get the result of an asset upload job that was created using the Create asset upload job API.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/asset-uploads/{jobId}

Rate limited to 180 requests per minute for each user of your integration.

## Authentication and authorization

Requires a valid access token with `asset:read` scope.

## Header parameters

* `Authorization`: Bearer token.

## Path parameters

* `jobId` (required): The asset upload job ID.

## Success response

Returns a `200` response with:
* `job.id`: The ID of the asset upload job.
* `job.status`: `in_progress`, `success`, or `failed`.
* `job.error`: Error details if failed.
* `job.asset`: The asset object (type, id, name, tags, owner, thumbnail, metadata, created_at, updated_at).
