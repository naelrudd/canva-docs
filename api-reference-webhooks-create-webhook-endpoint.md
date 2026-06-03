Source: https://www.canva.dev/docs/connect/api-reference/webhooks/create-webhook-endpoint/

# Create webhook endpoint

Subscribe to events by creating a webhook endpoint.

## HTTP method and URL path

POST https://api.canva.com/rest/v1/webhooks

Rate limited to 5 requests per minute.

## Authentication and authorization

Requires scope: `webhook:write`

## Body parameters

- **url** (string, required): HTTPS URL for events, 1-2048 chars
- **events** (string[], required): Array of event types (max 50)
- **metadata** (object, optional): max 5 keys

## Success response

Returns `200` with a `webhook` object: id, url, created_at, events, metadata, subscription_status (active, suspended, requires_configuration).

## Error codes

- `already_subscribed`, `invalid_event`, `invalid_url`, `url_unreachable`, `max_subscriptions_reached`