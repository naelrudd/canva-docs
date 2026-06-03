Source: https://www.canva.dev/docs/connect/api-reference/authentication/introspect-access-token/

# Introspect an access token

Introspect a token to see its validity and properties.

Requests to this endpoint require authentication with your client ID and client secret using Basic access authentication (recommended) or body parameters.

Cannot be called from a web-browser client (blocked by CORS).

## HTTP method and URL path

POST https://api.canva.com/rest/v1/oauth/introspect

## Authentication and authorization

This endpoint uses HTTP basic access authentication.

## Header parameters

* `Authorization`: Basic access authentication credentials.
* `Content-Type`: Must be `application/x-www-form-urlencoded`.

## Body parameters

* `token` (required): The token to introspect.
* `client_id` (optional): Your integration's client ID.
* `client_secret` (optional): Your integration's client secret.

## Success response

Returns a `200` response with:
* `active`: Whether the access token is active (boolean).
* `scope`: The scopes granted.
* `client`: The ID of the client that requested the token.
* `exp`: Expiration time (Unix timestamp).
* `iat`: When the token was issued (Unix timestamp).
* `nbf`: "Not before" time (Unix timestamp).
* `jti`: Unique ID for the access token.
* `sub`: The subject (user ID) the token acts on behalf of.
