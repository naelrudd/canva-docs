Source: https://www.canva.dev/docs/connect/authentication/

# Authentication

To start using the Canva Connect APIs, you need to authorize your users using [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749).

OAuth lets your integration authenticate the user, get their authorization to access the Connect API endpoints, and then perform actions on their behalf. Specifically, the Connect APIs use OAuth 2.0 with the [Authorization Code flow with Proof Key for Code Exchange (PKCE)](https://datatracker.ietf.org/doc/html/rfc7636) using SHA-256.

The authorization and authentication process involves the following steps:

1. Obtain authorization from the Canva user for the scopes that your integration requires. After the user authorizes your integration, you'll receive an authorization code at your specified redirect URL.
2. Use the authorization code to generate access tokens, which lets your integration access Connect API resources. This lets your integration act on the user's behalf.

## Prerequisites

Before authenticating to the Canva Connect APIs, you must first create and configure your integration in the Developer Portal, including:
* Setting an integration name
* Generating and saving a client secret
* Selecting scopes
* Setting at least one authentication redirect URL

## Obtain user authorization

To obtain user authorization, you must direct your users to Canva's authorization URL. This lets a user review and approve access for your integration.

### Create the authorization URL

The authorization URL that you direct users to is in the following format:

```
https://www.canva.com/api/oauth/authorize?code_challenge=<code challenge string>&code_challenge_method=s256&scope=<list of scopes>&response_type=code&client_id=<client ID>&state=<optional state>&redirect_uri=<redirect uri for your integration>
```

Create the URL, starting with `https://www.canva.com/api/oauth/authorize?` and add the following query parameters:

1. **`code_challenge`**: Derived from a `code_verifier` string. Create a `code_verifier` (43-128 characters, cryptographically random), then SHA-256 hash it and encode as URL-safe base64.
2. **`code_challenge_method`**: Must be `S256`.
3. **`scope`**: A space-separated list of [scopes](https://www.canva.dev/docs/connect/appendix/scopes/) requested by your integration.
4. **`response_type`**: Must be `code`.
5. **`client_id`**: Your integration's unique ID.
6. **`state`** (Optional): Countermeasure against CSRF attacks.
7. **`redirect_uri`** (Optional): The URL to redirect the user to after they authorize your integration.

### Send the user to the authorization URL

You must direct your users to the authorization URL that you created to get their approval for your integration and the requested scopes.

After they authorize your integration, they are redirected to your redirect URL with the following query parameters:
* `code`: The authorization code you can use to generate an access token.
* `state`: The value of the `state` parameter, if it was provided with the initial request.

## Generate access tokens

After you've obtained user authorization and received an authorization code, you can exchange the code for an access token and a refresh token.

### Use an authorization code

To exchange an authorization code for an access token, use the [Generate an access token endpoint](https://www.canva.dev/docs/connect/api-reference/authentication/generate-access-token/). Requests must come from your integration's backend.

### Use a refresh token

When an access token expires or becomes invalid, you can use a refresh token from a previous access token request to get a new access token.

## Introspect an access token

You can use the [Introspect an access token](https://www.canva.dev/docs/connect/api-reference/authentication/introspect-access-token/) endpoint to see whether an access token or refresh token is valid and active.

## Revoke a token

If necessary, you can use the [Revoke a token](https://www.canva.dev/docs/connect/api-reference/authentication/revoke-token/) endpoint to revoke an access token or refresh token.
