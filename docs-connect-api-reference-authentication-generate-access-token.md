Source: https://www.canva.dev/docs/connect/api-reference/authentication/generate-access-token/

# Generate an access token

Generate access tokens to access the Connect APIs.

This endpoint implements the OAuth 2.0 `token` endpoint, as part of the Authorization Code flow with Proof Key for Code Exchange (PKCE).

To generate an access token, you must provide one of the following:
* An authorization code
* A refresh token

Access tokens may be up to 4 KB in size, and are only valid for a specified period of time (currently 4 hours).

**Endpoint authentication**: Requires authentication with your client ID and client secret using Basic access authentication (recommended) or body parameters.

Cannot be called from a web-browser client (blocked by CORS).

## HTTP method and URL path

POST https://api.canva.com/rest/v1/oauth/token

## Authentication and authorization

This endpoint uses HTTP basic access authentication.

## Header parameters

* `Authorization`: Basic access authentication credentials.
* `Content-Type`: Must be `application/x-www-form-urlencoded`.

## Body parameters (authorization_code)

* `grant_type`: Must be `authorization_code`.
* `code_verifier`: The code_verifier value from the authorization URL.
* `code`: The authorization code received after user authorization.
* `client_id` (optional): Your integration's client ID.
* `client_secret` (optional): Your integration's client secret.
* `redirect_uri` (optional): Required if a redirect URL was supplied in the authorization URL.

## Body parameters (refresh_token)

* `grant_type`: Must be `refresh_token`.
* `refresh_token`: The refresh token from a previous token request.
* `client_id` (optional): Your integration's client ID.
* `client_secret` (optional): Your integration's client secret.
* `scope` (optional): Optional scope value when refreshing.

## Success response

Returns a `200` response with:
* `access_token`: The bearer access token.
* `refresh_token`: Token to refresh the access token.
* `token_type`: Always `Bearer`.
* `expires_in`: Expiry time in seconds.
* `scope`: The scopes granted.
