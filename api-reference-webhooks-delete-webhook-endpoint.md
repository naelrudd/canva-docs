Source: https://www.canva.dev/docs/connect/api-reference/webhooks/delete-webhook-endpoint/

# Delete webhook endpoint

Delete a webhook endpoint subscription.

## HTTP method and URL path

DELETE https://api.canva.com/rest/v1/webhooks/{webhookId}

Rate limited to 5 requests per minute.

## Authentication and authorization

Requires scope: `webhook:write`

## Path parameters

- **webhookId** (string, required): 1-50 chars

## Success response

Returns `204 No content`.