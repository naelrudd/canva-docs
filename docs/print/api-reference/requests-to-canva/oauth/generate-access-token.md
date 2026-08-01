> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/print/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate an access token

This endpoint implements the OAuth 2.0 `token` endpoint, as part of the [Client Credentials flow](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4). It lets you generate an access token that is used to authenticate requests to other endpoints in the Canva Print API.

Requests to this endpoint require authentication with your OAuth client ID and client secret, which were provided to you during the print partner onboarding process.

You must use [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), where the `{credentials}` string must be a Base64 encoded value of `{client id}:{client secret}`.

## HTTP method and URL path

POST https\://api.canva.com/auth/v1/oauth/token

## Header parameters

<Prop.List>
  <Prop name="Authorization" type="string" required>
    Provides credentials to authenticate the request, in the form of [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication). The `{credentials}` string must be a Base64 encoded value of `{client id}:{client secret}`.

    For example: `Authorization: Basic {credentials}`
  </Prop>

  <Prop name="Content-Type" type="string" required>
    Indicates the media type of the information sent in the request. This must be set to `application/x-www-form-urlencoded`.

    For example: `Content-Type: application/x-www-form-urlencoded`
  </Prop>
</Prop.List>

## Body parameters

<Prop.List>
  <Prop name="grant_type" type="string" required>
    Must be set to `client_credentials`.
  </Prop>
</Prop.List>

## Example request

Examples for using the `/v1/oauth/token` endpoint:

<Tabs storageKey="example.language" disableContentTransition>
  <Tab name="cURL">
    ```sh
    curl --request POST 'https://api.canva.com/auth/v1/oauth/token' \
    --header 'Authorization: Basic {credentials}' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=client_credentials'
    ```
  </Tab>
</Tabs>

## Success response

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

<Prop.List>
  <Prop name="access_token" type="string" required mode="output">
    The bearer access token to use to authenticate to Canva Print API endpoints.
  </Prop>

  <Prop name="token_type" type="string" required mode="output">
    The token type returned. This is always `Bearer`.
  </Prop>

  <Prop name="expires_in" type="integer" required mode="output">
    The expiry time (in seconds) for the token.
  </Prop>
</Prop.List>

### Example response

```json
{
  "access_token" : "JagALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206Z",
  "token_type" : "Bearer",
  "expires_in" : 14400
}
```

## Error responses

### 400 Invalid request. For example, missing parameters.

### 401 Invalid or unauthorized client ID or secret.
