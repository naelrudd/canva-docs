Source: https://www.canva.dev/docs/connect/api-reference/designs/create-design/

# Create design

Create a Canva design. Supports preset design types, custom dimensions, copying existing designs, and creating from brand templates.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/designs

Rate limited to 20 requests per minute.

## Authentication and authorization

Requires scope: `design:content:write`

## Body parameters

Three modes:

### type_and_asset
- **type**: "type_and_asset"
- **design_type** (optional): `{ type: "preset", name: "doc"|"email"|"presentation"|"whiteboard" }` or `{ type: "custom", width: 40-8000, height: 40-8000 }`
- **asset_id** (string, optional): Image asset ID to insert
- **title** (string, optional): 1-255 characters

### design (preview - copy existing design)
- **type**: "design"
- **design_id** (string, required)
- **page_numbers** (integer[], optional): 1-based page numbers to copy

### brand_template (preview)
- **type**: "brand_template"
- **brand_template_id** (string, required)
- **page_numbers** (integer[], optional)

## Example request (cURL)

```sh
curl --request POST 'https://api.canva.com/rest/v1/designs' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data '{
  "type": "type_and_asset",
  "design_type": { "type": "preset", "name": "doc" },
  "asset_id": "Msd59349ff",
  "title": "My Holiday Presentation"
}'
```

## Success response

Returns `200` with a `design` object containing: id, owner, urls (edit_url, view_url), created_at, updated_at, title, thumbnail, page_count.

## Error responses

- **404**: `not_found` (design or brand template not found)