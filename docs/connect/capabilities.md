Source: https://www.canva.dev/docs/connect/capabilities/

# Capabilities

Capabilities are features or permissions associated with a user's account, and are often tied to a user's Canva plan. Capabilities are used to control access to premium Canva functionality, and to help integrations expose features in a responsive and user-friendly way.

For example, the resize API requires the `resize` capability. If a user doesn't have the capability, any request on behalf of the user to that API fails with an error response.

## APIs that require capabilities

If an API requires a capability, it's listed in the reference documentation for the API operation, as well as in its OpenAPI specification under the `x-required-capabilities` property.

NOTE: If an API operation lists multiple capabilities, only one capability is required for a user to access the API.

## Check user capabilities

Before making a request to an API that requires a capability, integrations should use the [Get user capabilities API](https://www.canva.dev/docs/connect/api-reference/users/get-user-capabilities/) to check whether a user has a required capability.

## Error handling

If an integration attempts to access an API on behalf of a user that doesn't have a required capability, the API returns a `403 Forbidden` error with a descriptive error message.
