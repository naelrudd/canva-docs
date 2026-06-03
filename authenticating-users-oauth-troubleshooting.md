Source: https://www.canva.dev/docs/apps/authenticating-users/oauth-troubleshooting/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# OAuth troubleshooting

Reference for OAuth error codes.

This article lists OAuth error codes, their causes, and actions you can take to resolve them. Your app should catch all these errors and handle them appropriately.

Canva handles the OAuth flow and token retrieval, so you might need to [contact Canva support](https://canva-external.atlassian.net/servicedesk/customer/portal/2/group/2) for certain errors.

## Error types

The `requestAuthorization` and `getAccessToken` methods can throw two types of errors:

* `CanvaError`
* `OauthError`. A subclass of `CanvaError`, this contains an `oauthCode` property and a `code` property. The possible values are listed in the following tables.

To handle errors, we recommend displaying a message to let the user know that something has gone wrong, and offer them an opportunity to retry. You can then extend this approach, for example, if the user denies the request, then offer reassurance that the app requires them to login and grant permissions. Your app can also retry transient errors, such as server errors.

## Error codes

| `oauthCode`               | `code`                          | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `invalid_request`         | `bad_request`                   | <ul><li>**Cause:** The request is missing required parameters, has invalid values, or is malformed (for example, duplicated parameters).</li><li>**Manifests by:** Identity provider-specific requirements that are separate from the OAuth protocol.</li><li>**Fix:** Check that all required parameters are included, make sure values are valid, and avoid duplicates. This might be fixed with the `query_params` argument, but might also be a Canva issue.</li></ul> |
| `access_denied`           | `permission_denied`             | <ul><li>**Cause:** The user or authorization server denied the request.</li><li>**Manifests by:** <ul><li>User denies the app permissions for Canva to access the resources.</li></ul><ul><li>App server denies the access because the resource owner or authorization server denying the request.</li></ul></li><li>**Fix:** Notify the user and suggest retrying the authorization, making sure they approve the request.</li></ul>                                      |
| `unauthorized_client`     | `not_allowed`                   | <ul><li>**Cause:** The client isn't authorized to request authorization using this method.</li><li>**Manifests by:** Identity provider might restrict certain clients (like mobile), or the client might be disabled or blocked.</li><li>**Fix:** Verify that the client has the correct permissions and is using a valid grant type.</li></ul>                                                                                                                            |
| `invalid_client`          | `bad_request`                   | <ul><li>**Cause:** Client authentication failed (for example, an unknown client or unsupported authentication method).</li><li>**Manifests by:** Client authentication failed, possibly because of an incorrect client URL, secret, or ID.</li><li>**Fix:** Make sure that the client ID and secret are correct, and that a supported authentication method is used.</li></ul>                                                                                             |
| `invalid_scope`           | `bad_request`                   | <ul><li>**Cause:** The requested scope is invalid, unknown, or malformed.</li><li>**Manifests by:** Introduced in the app code. Also occurs when requesting a scope the user doesn't have access to, or the user's scope has been revoked.</li><li>**Fix:** Confirm that the requested scope is valid and supported by the authorization server.</li></ul>                                                                                                                 |
| `server_error`            | `bad_external_service_response` | <ul><li>**Cause:** An unexpected internal server issue occurred.</li><li>**Fix:** Retry the request after a short delay, or contact support if the issue persists.</li></ul>                                                                                                                                                                                                                                                                                               |
| `temporarily_unavailable` | `bad_external_service_response` | <ul><li>**Cause:** The server is temporarily overloaded or undergoing maintenance.</li><li>**Fix:** Wait and retry the request later. Monitor the server status, if possible.</li></ul>                                                                                                                                                                                                                                                                                    |
| `invalid_grant`           | `bad_request`                   | <ul><li>**Cause:** The provided authorization grant or refresh token is invalid, expired, revoked, or doesn't match the original request.</li><li>**Manifests by:** Grant token or refresh token is incorrect, invalid, expired, or revoked.</li><li>**Fix:** Unlikely to occur, but retry the authorization call again, and make sure that the auth flows are supported. </li></ul>                                                                                       |

## Error codes for identity providers

The following errors can occur because of the way an identity provider has implemented OAuth. As a result, you might not be able to resolve them yourself, and might have to contact your identity provider's support team.

| `oauthCode`                 | `code`        | Details                                                                                                                                                                                                                                                                                                            |
| --------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `unsupported_response_type` | `bad_request` | <ul><li>**Cause:** The server doesn't support the requested response type.</li><li>**Manifests by:** For example, some identity providers expect requests with specific headers.</li><li>**Fix:** You might not be able to fix this yourself, because it's likely the identity provider is incompatible.</li></ul> |
| `unsupported_grant_type`    | `bad_request` | <ul><li>**Cause:** The server doesn't support the requested grant type.</li><li>**Fix:** You might not be able to fix this yourself, because it's likely the identity provider is incompatible. The authorization code grant flow or refresh token flow might not be supported by the identity provider.</li></ul> |
| `unsupported_token_type`    | `bad_request` | <ul><li>**Cause:** The requested token type isn't supported by the server.</li><li>**Fix:** You might not be able to fix this yourself, because it's likely the identity provider is incompatible.</li></ul>                                                                                                       |

## Testing OAuth

When testing your app's OAuth integration, we recommended building a test plan that includes these practices:

* **Scenario exploration**: Document how you think these errors might manifest themselves in your app.
* **Test data**: Link your test data used for these scenarios.
* **Management approach**: Describe how you will manage these errors and provide sample screenshots.

### Test environments and users

It's good practice to test using a comprehensive list of users and roles that are reflective of your user base. This helps ensure that your users have a good authorization experience, and see the right data.

For example, these questions can help you get started:

* Planning for account types and user roles:
  * What account types and user roles will your end users use with this app?
  * What scopes do the users have access to?

* Test environment: User account data
  * List links to the test environment, user account, and test data that was used during testing. This should be representative of the types of users that will use the app. For example:
    * User Account: `Joe Bloggs`
    * Environment (link): `[Link to Environment]`
    * Notes: `[Additional Notes]`

### Basic test flow

To help you get started, this is an example of a basic OAuth test flow. This isn't a complete list of everything you should test.

1. Users can successfully log in and log out.
2. If users grant access using the consent prompt, they are then given access to the data.
3. If users deny access to the consent prompt, they aren't logged in.
4. Token refresh and expiry are working as expected.
5. If the user removes the app and then uses it again, they are prompted for reauthorization.
6. OAuth works on the Canva desktop application and mobile website.
