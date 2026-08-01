> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/print/llms.txt
> Use this file to discover all available pages before exploring further.

# Requests to Canva

Canva exposes API endpoints to enable print partners to send order status events to Canva.

Although the Print API returns an immediate response to order event requests, the processing of the requests in Canva's order system might be delayed.

If the Print API rejects a request because of rate limits, authentication issues, or other transient issues, print partners are expected to retry sending order updates.

Canva also provides endpoints for generating access tokens and getting signing keys.

## API endpoints

Canva provides the following endpoints for print partners to access:

* [Generate an access token](https://www.canva.dev/docs/print/api-reference/requests-to-canva/oauth/generate-access-token/)
* [Create order production event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-production-event/)
* [Create order shipment event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-shipment-event/)
* [Create order cost summary event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-cost-summary-event/)
* [Create order error event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-error-event/)
* [Get signing keys](https://www.canva.dev/docs/print/api-reference/requests-to-canva/keys/)

## Authentication and authorization

The order event endpoints use an OAuth 2.0 bearer token to authenticate print partner requests, as part of the OAuth [Client Credentials flow](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4).

Print partners must use their partner OAuth client ID and client secret with the [Generate an access token](https://www.canva.dev/docs/print/api-reference/requests-to-canva/oauth/generate-access-token/) endpoint to generate access tokens. The OAuth client ID and client secret are provided to print partners during the onboarding process.

The authentication and authorization process works as follows:

1. Print partners generate an access token using the [Generate an access token](https://www.canva.dev/docs/print/api-reference/requests-to-canva/oauth/generate-access-token/) endpoint.
2. Print partners use the access token in a request's `Authorization` header to authenticate to Canva's order event endpoints.
3. When the access token expires, print partners must generate a new access token using the [Generate an access token](https://www.canva.dev/docs/print/api-reference/requests-to-canva/oauth/generate-access-token/) endpoint.
