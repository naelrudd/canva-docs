Source: https://www.canva.dev/docs/connect/api-reference/resizes/get-resize/

# Get resize

Get the status and results of a resize job.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/resizes/{resizeId}

Rate limited to 120 requests per minute.

## Authentication and authorization

Requires scope: `design:content:write`

## Path parameters

- **resizeId** (string, required)

## Success response

Returns `200` with a `job` object: id, status, result (designs array with design_type info), error.