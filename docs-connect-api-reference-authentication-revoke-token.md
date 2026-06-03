Source: https://www.canva.dev/docs/connect/api-reference/authentication/revoke-token/

# Revoke a token

Revoke a token and its lineage.

Revoke an access token or a refresh token. If you revoke a refresh token, the refresh token's lineage is also revoked (access tokens created from it are also revoked), and the user's consent for your integration is also revoked.

Requests to this endpoint require authentication with your client ID and client secret using Basic access authentication (recommended) or body parameters.

Cannot be called from a web-browser client (blocked by CORS).

## HTTP method and URL path

POST https://api.canva.com/rest/v1/oauth/revoke

## Authentication and authorization

This endpoint uses HTTP basic access authentication.

## Header parameters

* `Authorization`: Basic access authentication credentials.
* `Content-Type`: Must be `application/x-www-form-urlencoded`.

## Body parameters

* `token` (required): The token to revoke.
* `client_id` (optional): Your integration's client ID.
* `client_secret` (optional): Your integration's client secret.

## Success response

Returns a `200` response with an empty JSON body: `{}`
