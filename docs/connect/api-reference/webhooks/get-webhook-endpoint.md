Source: https://www.canva.dev/docs/connect/api-reference/webhooks/get-webhook-endpoint/

# Get webhook endpoint

Get a webhook endpoint.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/webhooks/{webhookId}

Rate limited to 20 requests per minute.

## Authentication and authorization

Requires scope: `webhook:read`

## Path parameters

- **webhookId** (string, required): 1-50 chars

## Success response

Returns `200` with a `webhook` object.