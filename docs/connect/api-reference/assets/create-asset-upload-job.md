Source: https://www.canva.dev/docs/connect/api-reference/assets/create-asset-upload-job/

# Create asset upload job

Create an asynchronous job to upload an asset.

Starts a new asynchronous job to upload an asset to the user's content library. The request format is an `application/octet-stream` body of bytes. Attach information about the upload using an `Asset-Upload-Metadata` header.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/asset-uploads

Rate limited to 30 requests per minute for each user of your integration.

## Authentication and authorization

Requires a valid access token with `asset:write` scope.

## Header parameters

* `Authorization`: Bearer token.
* `Content-Type`: Must be `application/octet-stream`.
* `Asset-Upload-Metadata`: JSON object with `name_base64` (Base64-encoded asset name, max 50 characters unencoded).

## Body parameters

Binary of the asset to upload.

## Success response

Returns a `200` response with:
* `job.id`: The ID of the asset upload job.
* `job.status`: `in_progress`, `success`, or `failed`.
* `job.error`: Error details if failed (code: `file_too_big`, `import_failed`, `fetch_failed`).
* `job.asset`: The asset object (type, id, name, tags, owner, thumbnail, metadata, created_at, updated_at).
