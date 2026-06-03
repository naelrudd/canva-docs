Source: https://www.canva.dev/docs/connect/api-reference/merges/create-merge/

# Create merge

Merge data into a template design. Creates a new design for each row of data.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/merges

Rate limited to 20 requests per minute.

## Authentication and authorization

Requires scope: `design:content:write`

## Body parameters

- **design_id** (string, required): The template design ID
- **data** (merge_data, required): Array of merge rows with field values

## Success response

Returns `200` with a `job` object: id, status (in_progress).

## Error codes

- `internal_error`, `validation_error`, `merge_fields_mismatch`, `merge_rows_limit_exceeded`, `merge_fields_limit_exceeded`