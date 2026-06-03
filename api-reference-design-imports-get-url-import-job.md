Source: https://www.canva.dev/docs/connect/api-reference/design-imports/get-url-import-job/

# Get URL import job

Get the status and results of a URL import job.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/url-imports/{jobId}

Rate limited to 120 requests per minute.

## Authentication and authorization

Requires scope: `design:content:write`

## Path parameters

- **jobId** (string, required)

## Example request (cURL)

```sh
curl --request GET 'https://api.canva.com/rest/v1/url-imports/{jobId}' \
--header 'Authorization: Bearer {token}'
```

## Success response

Returns `200` with the `job` object (same schema as create URL import response).