Source: https://www.canva.dev/docs/connect/api-reference/assets/get-url-asset-upload-job/

# Get asset upload job via URL

Get the status and results of job to upload asset from a URL.

**Preview API**: Breaking changes may occur without a new API version. Public integrations using preview features will not pass review.

Get the result of an asset upload job that was created using the Create asset upload job via URL API.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/url-asset-uploads/{jobId}

Rate limited to 180 requests per minute for each user of your integration.

## Authentication and authorization

Requires a valid access token with `asset:read` scope.

## Header parameters

* `Authorization`: Bearer token.

## Path parameters

* `jobId` (required): The asset upload job ID.

## Success response

Returns a `200` response with job details (same structure as Get asset upload job).
