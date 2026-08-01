> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/print/llms.txt
> Use this file to discover all available pages before exploring further.

# Requests from Canva

To create and update orders on the print partner's system, Canva sends requests to the print partner's service. To facilitate this, the print partner must implement their side of the Print API and provide endpoints for Canva to access.

## API endpoints

The print partner must provide the following endpoints for Canva to access:

* [Create order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/create-order/)
* [Get order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/get-order/)
* [Update order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/update-order/)
* [Cancel order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/cancel-order/)
* [Find locations](https://www.canva.dev/docs/print/api-reference/requests-from-canva/find-locations/)

## Request verification

When print partners receive a request, they must verify the request came from Canva. Only Canva is authorized to send create and update Canva print orders.

Canva signs all requests with cryptographic keys using a [JSON Web Key Set (JWKS)](https://datatracker.ietf.org/doc/html/rfc7517#section-5). Each request includes a signature in a header named `X-Canva-Signature`.

Canva provides the [Get signing keys](https://www.canva.dev/docs/print/api-reference/requests-to-canva/keys/) endpoint for print partners to get Canva's Ed25519 public keys to verify the request signature.

The request verification process is as follows:

1. Retrieve Canva's public keys from the [Get signing keys](https://www.canva.dev/docs/print/api-reference/requests-to-canva/keys/) endpoint.
2. Verify the signature of each incoming request to your Print API endpoints, using Canva's public keys.
3. Check the following claims in the signature payload:

   * `iss` (issuer): This must be `Canva`.
   * `aud` (audience): This must match your OAuth client ID.
   * `sub` (subject): This must match your print client ID.
   * `order` (order): This must match the order ID in the request body (when present).

   A valid signature means the request is legitimate and hasn't been tampered with during transit.

<Note>
  We recommend that print partners cache Canva's public keys on their system and only call the [Get signing keys](https://www.canva.dev/docs/print/api-reference/requests-to-canva/keys/) endpoint to refresh the cache if an unrecognized key is detected.

  This reduces the number of network calls, while allowing Canva to rotate the keys when necessary.
</Note>
