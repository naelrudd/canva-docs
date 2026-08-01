Source: https://www.canva.dev/docs/connect/api-reference/autofills/create-design-autofill-job/

# Create design autofill job

Create an asynchronous job to autofill a design from a brand template with your input information.

Brand templates were migrated to use a new ID format in September 2025.

AVAILABILITY: Requires the user to be a member of a Canva Enterprise organization.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/autofills

Rate limited to 60 requests per minute for each user of your integration.

## Authentication and authorization

Requires a valid access token with `design:content:write` scope.

## Header parameters

* `Authorization`: Bearer token.
* `Content-Type`: Must be `application/json`.

## Body parameters

* `brand_template_id` (required): ID of the input brand template.
* `title` (optional): Title for the autofilled design (1-255 characters).
* `data` (required): Data object containing the data fields and values to autofill.

### Data field types

* **image**: Requires `type: "image"` and `asset_id`.
* **text**: Requires `type: "text"` and `text` string.
* **chart** (preview): Requires `type: "chart"` and `chart_data` with `column_configs` and `rows`.

## Success response

Returns a `200` response with:
* `job.id`: The autofill job ID.
* `job.status`: `in_progress`, `success`, or `failed`.
* `job.result`: Result when status is `success` (includes design details with id, urls, title, thumbnail).
* `job.error`: Error details if failed.
