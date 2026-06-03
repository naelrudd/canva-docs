Source: https://www.canva.dev/docs/connect/api-reference/design-imports/create-url-import-job/

# Create URL import job

Create an asynchronous job to import a design from a URL.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/url-imports

Rate limited to 20 requests per minute.

## Authentication and authorization

Requires scope: `design:content:write`

## Body parameters

- **title** (string, required): 1-255 chars
- **url** (string, required): Publicly accessible URL, 1-2048 chars
- **mime_type** (string, optional): 1-100 chars

## Example request (cURL)

```sh
curl --request POST 'https://api.canva.com/rest/v1/url-imports' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data '{
  "title": "My Awesome Design",
  "url": "https://example.com/file.key",
  "mime_type": "application/vnd.apple.keynote"
}'
```

## Success response

Same job schema as create design import job.