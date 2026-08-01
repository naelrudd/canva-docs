Source: https://www.canva.dev/docs/connect/api-reference/autofills/get-design-autofill-job/

# Get design autofill job

Get the status and results of an autofill job, including the autofilled design.

AVAILABILITY: Requires the user to be a member of a Canva Enterprise organization.

Get the result of a design autofill job that was created using the Create design autofill job API.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/autofills/{jobId}

Rate limited to 60 requests per minute for each user of your integration.

## Authentication and authorization

Requires a valid access token with `design:meta:read` scope.

## Header parameters

* `Authorization`: Bearer token.

## Path parameters

* `jobId` (required): The design autofill job ID.

## Success response

Returns a `200` response with:
* `job.id`: The autofill job ID.
* `job.status`: `in_progress`, `success`, or `failed`.
* `job.result`: Result when status is `success` (includes design summary with id, urls, title, thumbnail, page_count).
* `job.error`: Error details if failed (codes: `autofill_error`, `thumbnail_generation_error`, `create_design_error`, `design_approval_error`, `trial_quota_exceeded`).
