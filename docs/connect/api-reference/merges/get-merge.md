Source: https://www.canva.dev/docs/connect/api-reference/merges/get-merge/

# Get merge

Get the status and results of a merge job.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/merges/{mergeId}

Rate limited to 120 requests per minute.

## Authentication and authorization

Requires scope: `design:content:write`

## Path parameters

- **mergeId** (string, required)

## Success response

Returns `200` with a `job` object: id, status, result (designs array), error.