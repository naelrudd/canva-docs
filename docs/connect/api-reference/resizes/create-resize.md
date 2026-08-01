Source: https://www.canva.dev/docs/connect/api-reference/resizes/create-resize/

# Create resize

Resize a design, optionally using AI to rearrange content for new dimensions.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/resizes

<Warning>This API is currently provided as a preview.</Warning>

Rate limited to 20 requests per minute.

## Authentication and authorization

Requires scope: `design:content:write`

## Body parameters

- **design_id** (string, required)
- **resize_types** (array, required): Each item can be:
  - `{ "design_type": { "type": "preset", "name": "doc"|"email"|"presentation"|"whiteboard" } }`
  - `{ "design_type": { "type": "custom", "width": 40-8000, "height": 40-8000 } }`
  - `{ "design_type": { "type": "brand_template", "brand_template_id": "..." } }`
- **quality** (string, optional): "normal" (default, faster) or "premium" (higher quality, slower)
- **title** (string, optional)

## Success response

Returns `200` with a `job` object: id, status (in_progress).