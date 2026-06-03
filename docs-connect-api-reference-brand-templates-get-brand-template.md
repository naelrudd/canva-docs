Source: https://www.canva.dev/docs/connect/api-reference/brand-templates/get-brand-template/

# Get brand template

Get the metadata for one of the user's brand templates.

Brand templates were migrated to use a new ID format in September 2025.

AVAILABILITY: Requires a plan with access to brand templates (Canva Pro, Teams, or Enterprise).

## HTTP method and URL path

GET https://api.canva.com/rest/v1/brand-templates/{brandTemplateId}

Rate limited to 100 requests per minute for each user of your integration.

## Authentication and authorization

Requires a valid access token with `brandtemplate:meta:read` scope.

## Header parameters

* `Authorization`: Bearer token.

## Path parameters

* `brandTemplateId` (required): The brand template ID.

## Success response

Returns a `200` response with:
* `brand_template.id`: The brand template ID.
* `brand_template.title`: The brand template title.
* `brand_template.view_url`: URL to view the brand template.
* `brand_template.create_url`: URL to create a new design from the template.
* `brand_template.thumbnail`: Thumbnail image.
* `brand_template.created_at`: Unix timestamp.
* `brand_template.updated_at`: Unix timestamp.
