Source: https://www.canva.dev/docs/connect/api-reference/brand-templates/list-brand-templates/

# List brand templates

List all the user's brand templates.

Brand templates were migrated to use a new ID format in September 2025.

AVAILABILITY: Requires a plan with access to brand templates.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/brand-templates

Rate limited to 100 requests per minute for each user of your integration.

## Authentication and authorization

Requires a valid access token with `brandtemplate:meta:read` scope.

## Header parameters

* `Authorization`: Bearer token.

## Query parameters

* `query` (optional): Search term to filter brand templates.
* `continuation` (optional): Token for pagination.
* `limit` (optional): Number of templates to return (1-100, default 25).
* `ownership` (optional): Filter by ownership (`any`, `owned`, `shared`).
* `sort_by` (optional): Sort order (`relevance`, `modified_descending`, `modified_ascending`, `title_descending`, `title_ascending`).
* `dataset` (optional): Filter by dataset definition (`any`, `non_empty`).

## Success response

Returns a `200` response with:
* `items`: Array of brand template objects (id, title, view_url, create_url, thumbnail, created_at, updated_at).
* `continuation`: Token for retrieving more results (if present).
