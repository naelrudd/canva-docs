Source: https://www.canva.dev/docs/connect/api-reference/webhooks/list-webhook-endpoints/

# List webhook endpoints

List all webhook endpoint subscriptions.

## HTTP method and URL path

GET https://api.canva.com/rest/v1/webhooks

Rate limited to 20 requests per minute.

## Authentication and authorization

Requires scope: `webhook:read`

## Query parameters

- **continuation** (string, optional): Pagination token (max 2048 chars)

## Success response

Returns `200` with `items` (array of webhook objects) and `continuation` token.