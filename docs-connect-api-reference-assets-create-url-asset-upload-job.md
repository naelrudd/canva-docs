Source: https://www.canva.dev/docs/connect/api-reference/assets/create-url-asset-upload-job/

# Create asset upload job via URL

Create an asynchronous job to upload an asset from a URL.

**Preview API**: Breaking changes may occur without a new API version. Public integrations using preview features will not pass review.

Uploading a video asset from a URL is limited to a maximum 100MB file size.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/url-asset-uploads

Rate limited to 30 requests per minute for each user of your integration.

## Authentication and authorization

Requires a valid access token with `asset:write` scope.

## Header parameters

* `Authorization`: Bearer token.
* `Content-Type`: Must be `application/json`.

## Body parameters

* `name` (required): A name for the asset (1-255 characters).
* `url` (required): The URL of the file to import (8-2048 characters). Must be publicly accessible.

## Success response

Returns a `200` response with job details (same structure as Create asset upload job).
