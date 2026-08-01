> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/print/llms.txt
> Use this file to discover all available pages before exploring further.

# Verifying requests from Canva

Authenticate and verify requests from Canva to your print fulfillment system using JWT signatures.

This guide demonstrates how to authenticate and verify requests from Canva to your print partner system using JSON Web Tokens (JWTs).

When Canva sends requests to your print partner endpoints, each request includes a digital signature in the `X-Canva-Signature` header. You must validate this signature to confirm the request originated from Canva and hasn't been tampered with.

## Workflow

When your print partner system receives a request from Canva:

1. Extract the JWT from the `X-Canva-Signature` header.
2. Decode the JWT header to identify the signing key.
3. Retrieve the public key from your cache or from Canva's keys API.
4. Verify the JWT signature using the public key.
5. Validate the JWT claims (issuer, audience, subject, expiration, and order).
6. Process the request if validation succeeds, or return a `401 Unauthorized` response if validation fails.



## Prerequisites

To complete this guide, you need:

1. A print partner account with Canva.
2. Your client ID and print client ID provided during onboarding.
3. A JWT verification library that supports EdDSA (Edwards-Curve Digital Signature Algorithm).

## Signed endpoints

Canva includes the `X-Canva-Signature` header in the following requests to your print partner system:

| API endpoint                                                                                         | HTTP method | Description                                                         |
| ---------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------- |
| [Create order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/create-order/)     | POST        | Create an order on your system.                                     |
| [Update order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/update-order/)     | PATCH       | Update an order's address and customer contact information.         |
| [Cancel order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/cancel-order/)     | POST        | Cancel items on an order.                                           |
| [Get order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/get-order/)           | GET         | Retrieve details on an order.                                       |
| [Find locations](https://www.canva.dev/docs/print/api-reference/requests-from-canva/find-locations/) | GET         | Retrieve address and pickup hour details for your pickup locations. |

## Understanding the JWT structure

The JWT in the `X-Canva-Signature` header consists of three Base64URL-encoded parts separated by periods (`.`):

```
{header}.{payload}.{signature}
```

For example:

```
eyJ0eXAiOiJKV1QiLCJraWQiOiI2NjdiYTM4Mi01Mjk4LTQ4MjMtYTQzMi0yNDY5ZGFmNjgyMWEiLCJhbGciOiJFZERTQSJ9.eyJqdGkiOiJ1V2REWEVlZWcyOXZYcW5XaXJEZHNnIiwiaXNzIjoiQ2FudmEiLCJhdWQiOiJPQ0E0XzEyM0dISiIsInN1YiI6IlBDXzg5QUJjNFIiLCJpYXQiOjE3MzE0MTEsIm9yZGVyIjoib3JkZXJSZWZlcmVuY2VJZCIsImV4cCI6MTczMTQ0MX0.qqh8Yw4O4brSPaIQKgKpMu2c0tYGANProyKDVJLi6AVbmDaRfIwVobBA23ikLN-nHUUjiMvfQ2x1a-djtmTEAw
```

### JWT header

The header describes the cryptographic operations applied to the JWT. When decoded, the header contains:

```json
{
  "alg": "EdDSA",
  "typ": "JWT",
  "kid": "667ba382-5298-4823-a432-2469daf6821a"
}
```

<Prop.List>
  <Prop name="alg" type="string" required mode="output">
    The signing algorithm. This is always `EdDSA` (Edwards-Curve Digital Signature Algorithm) and is case-sensitive.
  </Prop>

  <Prop name="typ" type="string" required mode="output">
    The token type. This is always `JWT` and is case-sensitive.
  </Prop>

  <Prop name="kid" type="string" required mode="output">
    The key ID that identifies which public key was used to sign the JWT. Use this value to retrieve the correct public
    key from your cache or from Canva's [Get signing keys API](https://www.canva.dev/docs/print/api-reference/requests-to-canva/keys/).
  </Prop>
</Prop.List>

### JWT payload

The payload contains claims, which are statements about the request. When decoded, the payload contains:

```json
{
  "jti": "uWdDXEeeg29vXqnWirDdsg",
  "iss": "Canva",
  "aud": "OCA4_123GHJ",
  "sub": "PC_89ABc4R",
  "order": "orderReferenceId",
  "iat": 1731411,
  "exp": 1731441
}
```

<Prop.List>
  <Prop name="jti" type="string" required mode="output">
    JWT ID. A unique identifier for the JWT that prevents replay attacks. This value is case-sensitive.
  </Prop>

  <Prop name="iss" type="string" required mode="output">
    Issuer. The principal that issued the JWT. This is always `Canva` and is case-sensitive.
  </Prop>

  <Prop name="aud" type="string" required mode="output">
    Audience. The client ID provided to you during onboarding. Your system must verify this matches your client ID.
  </Prop>

  <Prop name="sub" type="string" required mode="output">
    Subject. The print client ID provided to you during onboarding. Your system must verify this matches your print
    client ID.
  </Prop>

  <Prop name="order" type="string" optional>
    Order reference ID. The order ID in the request path and body for create, update, cancel, and get order requests.
    This claim isn't present for find locations requests.
  </Prop>

  <Prop name="iat" type="number" required mode="output">
    Issued at. The time when the JWT was issued, in seconds since the Unix epoch.
  </Prop>

  <Prop name="exp" type="number" required mode="output">
    Expiration time. The time when the JWT expires, in seconds since the Unix epoch. Your system must reject JWTs after
    this time, with a small leeway (recommended 60 seconds) to account for clock skew.
  </Prop>
</Prop.List>

### JWT signature

The signature verifies that the JWT hasn't been altered. Canva creates the signature by encoding the header and payload, then signing them with a private key using the EdDSA algorithm.

## Retrieve Canva's public keys

To verify the JWT signature, you need Canva's public keys. Canva provides these keys through the [Get signing keys API](https://www.canva.dev/docs/print/api-reference/requests-to-canva/keys/).

### Step 1. Call the keys API

Make a GET request to retrieve the JSON Web Key Set (JWKS):

```shell
curl --request GET 'https://api.canva.com/print/v1/keys'
```

The endpoint returns a list of public keys. For complete API details, including additional request examples and error responses, see [Get signing keys](https://www.canva.dev/docs/print/api-reference/requests-to-canva/keys/).

Example response:

```json
{
  "keys": [
    {
      "kid": "667ba382-5298-4823-a432-2469daf6821a",
      "kty": "OKP",
      "crv": "Ed25519",
      "x": "y0V6Y6r-xJ7SVuOK0K33OF0OLRrtbNYPp7cgQ_IaZGI"
    }
  ]
}
```

Each public key contains:

<Prop.List>
  <Prop name="kid" type="string" required mode="output">
    The key ID. This matches the `kid` value in the JWT header.
  </Prop>

  <Prop name="kty" type="string" required mode="output">
    The key type. This is always `OKP` (Octet Key Pair) and is case-sensitive.
  </Prop>

  <Prop name="crv" type="string" required mode="output">
    The elliptic curve. This is always `Ed25519` and is case-sensitive.
  </Prop>

  <Prop name="x" type="string" required mode="output">
    The public key, encoded with Base64urlUInt.
  </Prop>
</Prop.List>

### Step 2. Cache the public keys

Cache the public keys in your system to avoid calling the keys API for every request. Canva may rotate keys periodically for security purposes.

When you receive a JWT with an unrecognized `kid` in the header, refresh your cache by calling the keys API again.



## Verify the JWT

You should use a JWT verification library that supports EdDSA to verify the signature and validate the claims. Don't implement custom verification logic, as JWT verification involves complex cryptographic operations.

For a list of JWT libraries by programming language, see [JWT.IO - JSON Web Tokens Libraries](https://jwt.io/libraries).

### Step 1. Choose a verification library

Select a library that supports:

* EdDSA signature verification
* JWT claim validation (issuer, audience, subject, expiration, and type)

### Step 2. Verify the signature and claims

When you receive a request from Canva:

1. Extract the JWT from the `X-Canva-Signature` header.
2. Decode the JWT header to get the `kid` value.
3. Retrieve the public key with the matching `kid` from your cache.
4. Use your JWT library to verify the signature and validate the claims.

You must verify the following claims:

* `iss` (issuer): Must be `Canva`.
* `aud` (audience): Must match your client ID.
* `sub` (subject): Must match your print client ID.
* `exp` (expiration): Must not be before the current time. Allow 60 seconds of leeway for clock skew.
* `typ` (type): Must be `JWT`.
* `order` (order reference ID): Must match the order ID in the request path and body for order-related requests.

The following examples show how to verify a JWT using popular JWT libraries:

<Tabs storageKey="example.language" disableContentTransition>
  <Tab name="Node.js">
    ```js
    const jose = require('jose');

    // Decode the JWT header to extract the kid (key ID)
    const header = jose.decodeProtectedHeader(signature);
    const kid = header.kid;

    // Retrieve cached public keys from your cache
    // Keys structure: {keys: [{kid: "...", kty: "OKP", crv: "Ed25519", x: "..."}]}
    const cachedKeys = await getKeysFromCache();

    // Create a JWKS from the cached public keys
    const JWKS = jose.createLocalJWKSet(cachedKeys);

    try {
    const {payload} = await jose.jwtVerify(signature, JWKS, {
    issuer: 'Canva',
    audience: 'OCA4_123GHJ', // Your client ID
    subject: 'PC_89ABc4R',   // Your print client ID
    typ: 'JWT',
    clockTolerance: 60
    });

    // Verify the order claim separately (not present for find locations requests)
    if (isOrderRequest && payload.order !== request.orderReferenceId) {
    // Return 401 Unauthorized
    return unauthorized();
    }

    // JWT is valid, process the request
    return handleRequest(request);

    } catch (error) {
    // JWT validation failed, return 401 Unauthorized
    return unauthorized();
    }
    ```
  </Tab>

  <Tab name="Java">
    ```java
    // Decode the JWT header to extract the kid (key ID)
    var jwtContext = new JwtConsumerBuilder()
    .setSkipAllValidators()
    .setDisableRequireSignature()
    .setSkipSignatureVerification()
    .build()
    .process(signature);
    var kid = jwtContext.getJoseObjects().get(0).getKeyIdHeaderValue();

    // Retrieve the cached key data from your cache
    // Key structure: {kty: "OKP", kid: "...", alg: "EdDSA", crv: "Ed25519", x: "..."}
    var cachedKeyData = getPublicKeyFromCache(kid);

    // Convert the cached key data to a JsonWebKey
    var jsonWebKey = new OctetKeyPairJsonWebKey(cachedKeyData);
    var publicKey = jsonWebKey.getKey();

    var consumer = new JwtConsumerBuilder()
    .setExpectedType(true, "JWT")
    .setEvaluationTime(NumericDate.fromMilliseconds(System.currentTimeMillis()))
    .setExpectedAudience("OCA4_123GHJ") // Your client ID
    .setExpectedSubject("PC_89ABc4R") // Your print client ID
    .setExpectedIssuer("Canva")
    .setVerificationKey(publicKey)
    .setAllowedClockSkewInSeconds(60)
    .setRequireExpirationTime()
    .build();

    try {
    var claims = consumer.processToClaims(signature);

    // Verify the order claim separately (not present for find locations requests)
    if (isOrderRequest) {
    var orderClaim = claims.getClaimValueAsString("order");
    if (!orderClaim.equals(request.getOrderReferenceId())) {
    // Return 401 Unauthorized
    return unauthorized();
    }
    }

    // JWT is valid, process the request
    return handleRequest(request);

    } catch (InvalidJwtException e) {
    // JWT validation failed, return 401 Unauthorized
    return unauthorized();
    }
    ```
  </Tab>

  <Tab name="Python">
    ```py
    import jwt
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    import base64
    import json

    # Decode the JWT header to extract the kid (key ID)
    header_part = signature.split('.')[0]
    header_json = base64.urlsafe_b64decode(header_part + '==')
    header = json.loads(header_json)
    kid = header['kid']

    # Retrieve the public key from your cache
    # Key structure: {'kid': '...', 'kty': 'OKP', 'crv': 'Ed25519', 'x': '...'}
    cached_key = get_public_key_from_cache(kid)

    # Load the public key from the cached JWKS
    x_bytes = base64.urlsafe_b64decode(cached_key['x'] + '==')
    public_key_obj = Ed25519PublicKey.from_public_bytes(x_bytes)

    try:
    payload = jwt.decode(
    signature,
    public_key_obj,
    algorithms=['EdDSA'],
    issuer='Canva',
    audience='OCA4_123GHJ', # Your client ID
    options={
    'verify_signature': True,
    'verify_exp': True,
    'verify_iss': True,
    'verify_aud': True,
    'require': ['exp', 'iss', 'aud', 'sub']
    },
    leeway=60
    )

    # Verify the subject claim
    if payload.get('sub') != 'PC_89ABc4R': # Your print client ID
    # Return 401 Unauthorized
    return unauthorized()

    # Verify the order claim separately (not present for find locations requests)
    if is_order_request and payload.get('order') != request.order_reference_id:
    # Return 401 Unauthorized
    return unauthorized()

    # JWT is valid, process the request
    return handle_request(request)

    except jwt.InvalidTokenError:
    # JWT validation failed, return 401 Unauthorized
    return unauthorized()
    ```
  </Tab>

  <Tab name="C#">
    ```csharp
    using System.IdentityModel.Tokens.Jwt;
    using Microsoft.IdentityModel.Tokens;

    // Decode the JWT header to extract the kid (key ID)
    var handler = new JwtSecurityTokenHandler();
    var jwtToken = handler.ReadJwtToken(signature);
    var kid = jwtToken.Header.Kid;

    // Retrieve the cached key data from your cache
    // Key structure: {Kty: "OKP", Kid: "...", Crv: "Ed25519", X: "..."}
    var cachedKeyData = GetPublicKeyDataFromCache(kid);

    // Convert the cached key data to a JsonWebKey
    var publicKey = new JsonWebKey
    {
      Kty = cachedKeyData.Kty,
      Kid = cachedKeyData.Kid,
      Crv = cachedKeyData.Crv,
      X = cachedKeyData.X
    };

    var validationParameters = new TokenValidationParameters
    {
      ValidateIssuerSigningKey = true,
      IssuerSigningKey = publicKey,
      ValidateIssuer = true,
      ValidIssuer = "Canva",
      ValidateAudience = true,
      ValidAudience = "OCA4_123GHJ", // Your client ID
      ValidateLifetime = true,
      ClockSkew = TimeSpan.FromSeconds(60)
    };

    try
    {
      var principal = handler.ValidateToken(signature, validationParameters, out var validatedToken);

      var jwt = (JwtSecurityToken)validatedToken;

      // Verify the subject claim
      if (jwt.Subject != "PC_89ABc4R") // Your print client ID
    {
      // Return 401 Unauthorized
      return Unauthorized();
    }

      // Verify the order claim separately (not present for find locations requests)
      if (isOrderRequest)
    {
      var orderClaim = jwt.Claims.FirstOrDefault(c => c.Type == "order")?.Value;
      if (orderClaim != request.OrderReferenceId)
    {
      // Return 401 Unauthorized
      return Unauthorized();
    }
    }

      // JWT is valid, process the request
      return HandleRequest(request);
    }
    catch (SecurityTokenException)
    {
      // JWT validation failed, return 401 Unauthorized
      return Unauthorized();
    }
    ```
  </Tab>

  <Tab name="Go">
    ```go
    import (
    "encoding/base64"
    "encoding/json"
    "errors"
    "strings"
    "github.com/golang-jwt/jwt/v5"
    )

    // Create a custom claims struct
    type CustomClaims struct {
    Order string `json:"order,omitempty"`
    jwt.RegisteredClaims
    }

    func verifyJWT(signature string) error {
    // Decode the JWT header to extract the kid (key ID)
    parts := strings.Split(signature, ".")
    headerBytes, err := base64.RawURLEncoding.DecodeString(parts[0])
    if err != nil {
    return errors.New("failed to decode header")
    }

    var header map[string]interface{}
    json.Unmarshal(headerBytes, &header)
    kid := header["kid"].(string)

    // Retrieve the public key from your cache
    // Key structure: { kid: "...", kty: "OKP", crv: "Ed25519", x: "..." }
    publicKey := getPublicKeyFromCache(kid)

    token, err := jwt.ParseWithClaims(signature, &CustomClaims{}, func(token *jwt.Token) (interface{}, error) {
    // Verify the signing method
    if _, ok := token.Method.(*jwt.SigningMethodEd25519); !ok {
    return nil, errors.New("unexpected signing method")
    }
    return publicKey, nil
    })

    if err != nil {
    // JWT validation failed, return 401 Unauthorized
    return err
    }

    claims, ok := token.Claims.(*CustomClaims)
    if !ok || !token.Valid {
    // JWT validation failed, return 401 Unauthorized
    return errors.New("invalid token")
    }

    // Verify the issuer, audience, and subject
    if claims.Issuer != "Canva" {
    return errors.New("invalid issuer")
    }
    if claims.Audience[0] != "OCA4_123GHJ" { // Your client ID
    return errors.New("invalid audience")
    }
    if claims.Subject != "PC_89ABc4R" { // Your print client ID
    return errors.New("invalid subject")
    }

    // Verify the order claim separately (not present for find locations requests)
    if isOrderRequest && claims.Order != request.OrderReferenceId {
    return errors.New("invalid order")
    }

    // JWT is valid, process the request
    return nil
    }
    ```
  </Tab>

  <Tab name="PHP">
    ```php
    use Firebase\JWT\JWT;
    use Firebase\JWT\Key;

    // Decode the JWT header to extract the kid (key ID)
    $parts = explode('.', $signature);
    $headerJson = base64_decode(strtr($parts[0], '-_', '+/'));
    $header = json_decode($headerJson, true);
    $kid = $header['kid'];

    // Retrieve the public key from your cache
    // Key structure: [ 'kty' => 'OKP', 'kid' => '...', 'crv' => 'Ed25519', 'x' => '...' ]
    $publicKey = getPublicKeyFromCache($kid);

    try {
    // Decode and verify the JWT
    $decoded = JWT::decode($signature, new Key($publicKey, 'EdDSA'));

    // Verify the issuer, audience, and subject
    if ($decoded->iss !== 'Canva') {
    // Return 401 Unauthorized
    return unauthorized();
    }
    if ($decoded->aud !== 'OCA4_123GHJ') { // Your client ID
    // Return 401 Unauthorized
    return unauthorized();
    }
    if ($decoded->sub !== 'PC_89ABc4R') { // Your print client ID
    // Return 401 Unauthorized
    return unauthorized();
    }

    // Verify the order claim separately (not present for find locations requests)
    if ($isOrderRequest && $decoded->order !== $request->orderReferenceId) {
    // Return 401 Unauthorized
    return unauthorized();
    }

    // JWT is valid, process the request
    return handleRequest($request);

    } catch (Exception $e) {
    // JWT validation failed, return 401 Unauthorized
    return unauthorized();
    }
    ```
  </Tab>

  <Tab name="Ruby">
    ```ruby
    require 'jwt'
    require 'ed25519'
    require 'base64'
    require 'json'

    # Decode the JWT header to extract the kid (key ID)
    parts = signature.split('.')
    header_json = Base64.urlsafe_decode64(parts[0])
    header = JSON.parse(header_json)
    kid = header['kid']

    # Retrieve the public key from your cache
    # Key structure: {'kid' => '...', 'kty' => 'OKP', 'crv' => 'Ed25519', 'x' => '...'}
    cached_key = get_public_key_from_cache(kid)

    # Load the public key from the cached JWKS
    x_bytes = Base64.urlsafe_decode64(cached_key['x'])
    public_key_obj = Ed25519::VerifyKey.new(x_bytes)

    begin
    decoded_token = JWT.decode(
    signature,
    public_key_obj,
    true,
    {
      algorithm: 'EdDSA',
      iss: 'Canva',
      aud: 'OCA4_123GHJ', # Your client ID
      verify_iss: true,
      verify_aud: true,
      verify_expiration: true,
      leeway: 60
    }
    )

    payload = decoded_token[0]

    # Verify the subject claim
    if payload['sub'] != 'PC_89ABc4R' # Your print client ID
    # Return 401 Unauthorized
    return unauthorized
    end

    # Verify the order claim separately (not present for find locations requests)
    if is_order_request && payload['order'] != request.order_reference_id
    # Return 401 Unauthorized
    return unauthorized
    end

    # JWT is valid, process the request
    handle_request(request)

    rescue JWT::DecodeError
    # JWT validation failed, return 401 Unauthorized
    unauthorized
    end
    ```
  </Tab>
</Tabs>

### Step 3. Handle verification failures

If JWT verification fails for any reason, return a `401 Unauthorized` response and don't process the request.



Common failure scenarios include:

* **Invalid signature**: The JWT signature doesn't match the public key.
* **Expired token**: The current time is after the expiration time in the `exp` claim.
* **Invalid claims**: The issuer, audience, subject, or order claims don't match the expected values.
* **Unrecognized key**: The `kid` in the JWT header doesn't match any key in your cache, even after refreshing from the keys API.



## Example verification

The following example demonstrates complete JWT verification using the token and public key from earlier sections:

### Token

```
eyJ0eXAiOiJKV1QiLCJraWQiOiI2NjdiYTM4Mi01Mjk4LTQ4MjMtYTQzMi0yNDY5ZGFmNjgyMWEiLCJhbGciOiJFZERTQSJ9.eyJqdGkiOiJ1V2REWEVlZWcyOXZYcW5XaXJEZHNnIiwiaXNzIjoiQ2FudmEiLCJhdWQiOiJPQ0E0XzEyM0dISiIsInN1YiI6IlBDXzg5QUJjNFIiLCJpYXQiOjE3MzE0MTEsIm9yZGVyIjoib3JkZXJSZWZlcmVuY2VJZCIsImV4cCI6MTczMTQ0MX0.qqh8Yw4O4brSPaIQKgKpMu2c0tYGANProyKDVJLi6AVbmDaRfIwVobBA23ikLN-nHUUjiMvfQ2x1a-djtmTEAw
```

### Public key

The public key retrieved from the keys API:

```json
{
  "kty": "OKP",
  "kid": "667ba382-5298-4823-a432-2469daf6821a",
  "crv": "Ed25519",
  "x": "y0V6Y6r-xJ7SVuOK0K33OF0OLRrtbNYPp7cgQ_IaZGI"
}
```

### Verification

<Tabs storageKey="example.language" disableContentTransition>
  <Tab name="Node.js">
    ```js
    const jose = require('jose');

    const signature =
    'eyJ0eXAiOiJKV1QiLCJraWQiOiI2NjdiYTM4Mi01Mjk4LTQ4MjMtYTQzMi0yNDY5ZGFmNjgyMWEiLCJhbGciOiJFZERTQSJ9.eyJqdGkiOiJ1V2REWEVlZWcyOXZYcW5XaXJEZHNnIiwiaXNzIjoiQ2FudmEiLCJhdWQiOiJPQ0E0XzEyM0dISiIsInN1YiI6IlBDXzg5QUJjNFIiLCJpYXQiOjE3MzE0MTEsIm9yZGVyIjoib3JkZXJSZWZlcmVuY2VJZCIsImV4cCI6MTczMTQ0MX0.qqh8Yw4O4brSPaIQKgKpMu2c0tYGANProyKDVJLi6AVbmDaRfIwVobBA23ikLN-nHUUjiMvfQ2x1a-djtmTEAw';

    // Retrieve cached public keys from your cache
    // Keys structure: {keys: [{kid: "...", kty: "OKP", crv: "Ed25519", x: "..."}]}
    const cachedKeys = await getKeysFromCache();

    // Create a JWKS from the cached public keys
    const JWKS = jose.createLocalJWKSet(cachedKeys);

    const {payload} = await jose.jwtVerify(signature, JWKS, {
    issuer: 'Canva',
    audience: 'OCA4_123GHJ',
    subject: 'PC_89ABc4R',
    typ: 'JWT',
    clockTolerance: 60
    });

    // Verify the order claim separately
    const isValidOrder = payload.order === 'orderReferenceId';
    console.log('Valid order:', isValidOrder);
    ```
  </Tab>

  <Tab name="Java">
    ```java
    var signature =
    "eyJ0eXAiOiJKV1QiLCJraWQiOiI2NjdiYTM4Mi01Mjk4LTQ4MjMtYTQzMi0yNDY5ZGFmNjgyMWEiLCJhbGciOiJFZERTQSJ9.eyJqdGkiOiJ1V2REWEVlZWcyOXZYcW5XaXJEZHNnIiwiaXNzIjoiQ2FudmEiLCJhdWQiOiJPQ0E0XzEyM0dISiIsInN1YiI6IlBDXzg5QUJjNFIiLCJpYXQiOjE3MzE0MTEsIm9yZGVyIjoib3JkZXJSZWZlcmVuY2VJZCIsImV4cCI6MTczMTQ0MX0.qqh8Yw4O4brSPaIQKgKpMu2c0tYGANProyKDVJLi6AVbmDaRfIwVobBA23ikLN-nHUUjiMvfQ2x1a-djtmTEAw";

    // Retrieve the cached key data from your cache
    // Key structure: {kty: "OKP", kid: "...", alg: "EdDSA", crv: "Ed25519", x: "..."}
    var cachedKeyData = getPublicKeyFromCache("667ba382-5298-4823-a432-2469daf6821a");

    // Convert the cached key data to a JsonWebKey
    var jsonWebKey = new OctetKeyPairJsonWebKey(cachedKeyData);
    var publicKey = jsonWebKey.getKey();

    var consumer = new JwtConsumerBuilder()
    .setExpectedType(true, "JWT")
    .setEvaluationTime(NumericDate.fromMilliseconds(1731411892))
    .setExpectedAudience("OCA4_123GHJ")
    .setExpectedSubject("PC_89ABc4R")
    .setExpectedIssuer("Canva")
    .setVerificationKey(publicKey)
    .setAllowedClockSkewInSeconds(60)
    .setRequireExpirationTime()
    .build();

    // This passes if all claims are valid, otherwise an exception is thrown
    var claims = consumer.processToClaims(signature);

    // Verify the order claim separately
    var isValidOrder = claims.getClaimValueAsString("order").equals("orderReferenceId");
    System.out.println("Valid order: " + isValidOrder);
    ```
  </Tab>

  <Tab name="Python">
    ```py
    import jwt
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    import base64

    signature =
    'eyJ0eXAiOiJKV1QiLCJraWQiOiI2NjdiYTM4Mi01Mjk4LTQ4MjMtYTQzMi0yNDY5ZGFmNjgyMWEiLCJhbGciOiJFZERTQSJ9.eyJqdGkiOiJ1V2REWEVlZWcyOXZYcW5XaXJEZHNnIiwiaXNzIjoiQ2FudmEiLCJhdWQiOiJPQ0E0XzEyM0dISiIsInN1YiI6IlBDXzg5QUJjNFIiLCJpYXQiOjE3MzE0MTEsIm9yZGVyIjoib3JkZXJSZWZlcmVuY2VJZCIsImV4cCI6MTczMTQ0MX0.qqh8Yw4O4brSPaIQKgKpMu2c0tYGANProyKDVJLi6AVbmDaRfIwVobBA23ikLN-nHUUjiMvfQ2x1a-djtmTEAw'

    # Retrieve the public key from your cache
    # Key structure: {'kid': '...', 'kty': 'OKP', 'crv': 'Ed25519', 'x': '...'}
    cached_key = get_public_key_from_cache('667ba382-5298-4823-a432-2469daf6821a')

    # Load the public key from the cached JWKS
    x_bytes = base64.urlsafe_b64decode(cached_key['x'] + '==')
    public_key_obj = Ed25519PublicKey.from_public_bytes(x_bytes)

    payload = jwt.decode(
    signature,
    public_key_obj,
    algorithms=['EdDSA'],
    issuer='Canva',
    audience='OCA4_123GHJ',
    options={
    'verify_signature': True,
    'verify_exp': True,
    'verify_iss': True,
    'verify_aud': True
    },
    leeway=60
    )

    # Verify the order claim separately
    is_valid_order = payload.get('order') == 'orderReferenceId'
    print(f'Valid order: {is_valid_order}')
    ```
  </Tab>

  <Tab name="C#">
    ```csharp
    using System.IdentityModel.Tokens.Jwt;
    using Microsoft.IdentityModel.Tokens;

    var signature =
    "eyJ0eXAiOiJKV1QiLCJraWQiOiI2NjdiYTM4Mi01Mjk4LTQ4MjMtYTQzMi0yNDY5ZGFmNjgyMWEiLCJhbGciOiJFZERTQSJ9.eyJqdGkiOiJ1V2REWEVlZWcyOXZYcW5XaXJEZHNnIiwiaXNzIjoiQ2FudmEiLCJhdWQiOiJPQ0E0XzEyM0dISiIsInN1YiI6IlBDXzg5QUJjNFIiLCJpYXQiOjE3MzE0MTEsIm9yZGVyIjoib3JkZXJSZWZlcmVuY2VJZCIsImV4cCI6MTczMTQ0MX0.qqh8Yw4O4brSPaIQKgKpMu2c0tYGANProyKDVJLi6AVbmDaRfIwVobBA23ikLN-nHUUjiMvfQ2x1a-djtmTEAw";

    // Retrieve the cached key data from your cache
    // Key structure: {Kty: "OKP", Kid: "...", Crv: "Ed25519", X: "..."}
    var cachedKeyData = GetPublicKeyDataFromCache("667ba382-5298-4823-a432-2469daf6821a");

    // Convert the cached key data to a JsonWebKey
    var publicKey = new JsonWebKey
    {
      Kty = cachedKeyData.Kty,
      Kid = cachedKeyData.Kid,
      Crv = cachedKeyData.Crv,
      X = cachedKeyData.X
    };

    var validationParameters = new TokenValidationParameters
    {
      ValidateIssuerSigningKey = true,
      IssuerSigningKey = publicKey,
      ValidateIssuer = true,
      ValidIssuer = "Canva",
      ValidateAudience = true,
      ValidAudience = "OCA4_123GHJ",
      ValidateLifetime = true,
      ClockSkew = TimeSpan.FromSeconds(60)
    };

    var handler = new JwtSecurityTokenHandler();
    var principal = handler.ValidateToken(signature, validationParameters, out var validatedToken);
    var jwtToken = (JwtSecurityToken)validatedToken;

    // Verify the order claim separately
    var orderClaim = jwtToken.Claims.FirstOrDefault(c => c.Type == "order")?.Value;
    var isValidOrder = orderClaim == "orderReferenceId";
    Console.WriteLine($"Valid order: {isValidOrder}");
    ```
  </Tab>

  <Tab name="Go">
    ```go
    import (
    "fmt"
    "github.com/golang-jwt/jwt/v5"
    )

    signature :=
    "eyJ0eXAiOiJKV1QiLCJraWQiOiI2NjdiYTM4Mi01Mjk4LTQ4MjMtYTQzMi0yNDY5ZGFmNjgyMWEiLCJhbGciOiJFZERTQSJ9.eyJqdGkiOiJ1V2REWEVlZWcyOXZYcW5XaXJEZHNnIiwiaXNzIjoiQ2FudmEiLCJhdWQiOiJPQ0E0XzEyM0dISiIsInN1YiI6IlBDXzg5QUJjNFIiLCJpYXQiOjE3MzE0MTEsIm9yZGVyIjoib3JkZXJSZWZlcmVuY2VJZCIsImV4cCI6MTczMTQ0MX0.qqh8Yw4O4brSPaIQKgKpMu2c0tYGANProyKDVJLi6AVbmDaRfIwVobBA23ikLN-nHUUjiMvfQ2x1a-djtmTEAw"

    // Retrieve the public key from your cache
    // Key structure: {kid: "...", kty: "OKP", crv: "Ed25519", x: "..."}
    publicKey := getPublicKeyFromCache("667ba382-5298-4823-a432-2469daf6821a")

    parsed, err := jwt.ParseWithClaims(signature, &CustomClaims{}, func(token *jwt.Token) (interface{}, error) {
    return publicKey, nil
    })

    if err != nil {
    panic(err)
    }

    claims := parsed.Claims.(*CustomClaims)

    // Verify the order claim separately
    isValidOrder := claims.Order == "orderReferenceId"
    fmt.Printf("Valid order: %v\n", isValidOrder)
    ```
  </Tab>

  <Tab name="PHP">
    ```php
    use Firebase\JWT\JWT;
    use Firebase\JWT\Key;

    $signature =
    'eyJ0eXAiOiJKV1QiLCJraWQiOiI2NjdiYTM4Mi01Mjk4LTQ4MjMtYTQzMi0yNDY5ZGFmNjgyMWEiLCJhbGciOiJFZERTQSJ9.eyJqdGkiOiJ1V2REWEVlZWcyOXZYcW5XaXJEZHNnIiwiaXNzIjoiQ2FudmEiLCJhdWQiOiJPQ0E0XzEyM0dISiIsInN1YiI6IlBDXzg5QUJjNFIiLCJpYXQiOjE3MzE0MTEsIm9yZGVyIjoib3JkZXJSZWZlcmVuY2VJZCIsImV4cCI6MTczMTQ0MX0.qqh8Yw4O4brSPaIQKgKpMu2c0tYGANProyKDVJLi6AVbmDaRfIwVobBA23ikLN-nHUUjiMvfQ2x1a-djtmTEAw';

    // Retrieve the public key from your cache
    // Key structure: [ 'kty' => 'OKP', 'kid' => '...', 'crv' => 'Ed25519', 'x' => '...' ]
    $publicKey = getPublicKeyFromCache('667ba382-5298-4823-a432-2469daf6821a');

    $decoded = JWT::decode($signature, new Key($publicKey, 'EdDSA'));

    // Verify the order claim separately
    $isValidOrder = $decoded->order === 'orderReferenceId';
    echo "Valid order: " . ($isValidOrder ? 'true' : 'false');
    ```
  </Tab>

  <Tab name="Ruby">
    ```ruby
    require 'jwt'
    require 'ed25519'
    require 'base64'

    signature =
    'eyJ0eXAiOiJKV1QiLCJraWQiOiI2NjdiYTM4Mi01Mjk4LTQ4MjMtYTQzMi0yNDY5ZGFmNjgyMWEiLCJhbGciOiJFZERTQSJ9.eyJqdGkiOiJ1V2REWEVlZWcyOXZYcW5XaXJEZHNnIiwiaXNzIjoiQ2FudmEiLCJhdWQiOiJPQ0E0XzEyM0dISiIsInN1YiI6IlBDXzg5QUJjNFIiLCJpYXQiOjE3MzE0MTEsIm9yZGVyIjoib3JkZXJSZWZlcmVuY2VJZCIsImV4cCI6MTczMTQ0MX0.qqh8Yw4O4brSPaIQKgKpMu2c0tYGANProyKDVJLi6AVbmDaRfIwVobBA23ikLN-nHUUjiMvfQ2x1a-djtmTEAw'

    # Retrieve the public key from your cache
    # Key structure: {'kid' => '...', 'kty' => 'OKP', 'crv' => 'Ed25519', 'x' => '...'}
    cached_key = get_public_key_from_cache('667ba382-5298-4823-a432-2469daf6821a')

    # Load the public key from the cached JWKS
    x_bytes = Base64.urlsafe_decode64(cached_key['x'])
    public_key_obj = Ed25519::VerifyKey.new(x_bytes)

    decoded_signature = JWT.decode(
    signature,
    public_key_obj,
    true,
    {
      algorithm: 'EdDSA',
      iss: 'Canva',
      aud: 'OCA4_123GHJ',
      verify_iss: true,
      verify_aud: true,
      verify_expiration: true,
      leeway: 60
    }
    )

    payload = decoded_signature[0]

    # Verify the order claim separately
    is_valid_order = payload['order'] == 'orderReferenceId'
    puts "Valid order: #{is_valid_order}"
    ```
  </Tab>
</Tabs>

## Security considerations

Follow these best practices to ensure secure JWT verification:

* **Always verify the signature**: Never trust a JWT without verifying its signature against Canva's public keys.
* **Validate all claims**: Check every required claim, including `iss`, `aud`, `sub`, `exp`, and `order`.
* **Use a trusted library**: Don't implement custom JWT verification. Use a well-maintained library that supports EdDSA.
* **Cache public keys**: Store Canva's public keys in your system and only call the keys API when you encounter an unrecognized key.
* **Handle key rotation**: Be prepared to refresh your key cache when Canva rotates its signing keys.
* **Reject expired tokens**: Don't accept JWTs after their expiration time, even with clock skew leeway.
* **Prevent replay attacks**: The `jti` claim provides a unique identifier for each JWT. Consider tracking recent `jti` values to prevent the same JWT from being processed multiple times.
* **Return 401 for failures**: Always return a `401 Unauthorized` response when verification fails. Don't process the request or provide detailed error information that could help attackers.

## Further reading

For more information about JWTs and security best practices, see:

* [JSON Web Tokens Introduction](https://jwt.io/introduction)
* [Get Started with JSON Web Tokens](https://auth0.com/learn/json-web-tokens)
* [RFC 7519: JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519)
* [JWT signing and verification libraries](https://jwt.io/libraries)
