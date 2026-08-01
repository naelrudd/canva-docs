Source: https://www.canva.dev/docs/connect/api-reference/brand-templates/get-brand-template-dataset/

# Get brand template dataset

Check if you can autofill a brand template and what information you can autofill.

Brand templates were migrated to use a new ID format in September 2025.

AVAILABILITY: Requires a plan with access to brand templates.

Gets the dataset definition of a brand template. Available data field types include:
* Images
* Text
* Charts (preview)

## HTTP method and URL path

GET https://api.canva.com/rest/v1/brand-templates/{brandTemplateId}/dataset

Rate limited to 100 requests per minute for each user of your integration.

## Authentication and authorization

Requires a valid access token with `brandtemplate:content:read` scope.

## Header parameters

* `Authorization`: Bearer token.

## Path parameters

* `brandTemplateId` (required): The brand template ID.

## Success response

Returns a `200` response with:
* `dataset`: An object where each key is a data field name and each value is an object with a `type` property (`image`, `text`, or `chart`).
