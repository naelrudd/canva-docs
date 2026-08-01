Source: https://www.canva.dev/docs/connect/guidelines/security/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/connect/llms.txt
> Use this file to discover all available pages before exploring further.

# Security recommendations for the Connect APIs

Recommended security practices for your integration.

<Warning>
  **Important Note:** The Connect APIs integrations must be associated with a web app. We don't support integrations in environments where it's difficult to securely store credentials, such as mobile or desktop apps, browser extensions, Progressive Web Apps (with no backend), and Single Page Apps.

  Avoid using the Connect APIs in these environments, because they don't offer the necessary security features to protect the API credentials.
</Warning>

<Note>
  Canva uses a shared responsibility model to define what developers are responsible for when creating integrations, and what Canva is responsible for as the owner of the platform. For a list of security responsibilities that you'll need to consider when creating your integration, see the [Shared responsibility model for the Connect APIs](https://www.canva.dev/docs/connect/guidelines/shared-responsibility/).
</Note>

## Redirect URIs

Redirect URIs appear as URLs and are safe to include in published code. However, make sure that the redirect URIs defined in your integrations are only limited to domain names that you directly control.
After you complete local development and testing, you must remove `127.0.0.1`, `localhost`, and related domains from your integration's configuration.

## Scopes

Your integration should only request the minimum scopes needed to perform its functions. If any of your integration tokens become compromised, this can help limit the amount of damage that can occur.
You should periodically review the list of scopes requested by your integration, and remove any scopes that are unused or no longer required.

## Secure secret storage

A *client ID* identifies your integration, and frequently appears in OAuth requests and other contexts. Your client ID can be shared freely in code and email, and cannot be used alone to act on your integration's behalf. A *client secret* asserts your application's access rights and identity, when generating the user access tokens or refresh tokens.

Using your client secret, you can generate:

* User access tokens to access Connect APIs on a user's behalf.
* Refresh tokens that can generate new user access tokens.

You must securely store your client secret and any generated user access tokens and refresh tokens. Secure storage depends on your application's architecture and security risk model, so there isn't a single approach that suits everyone.

### Client secrets

Don't distribute client secrets in email, chat, public code repositories, or anywhere else where it might be leaked to unauthorized users.

If you are generating access or refresh tokens using a web app or backend server, consider storing your client secret in a secrets storage vault, such as AWS Secrets Manager or HashiCorp Vault. If these options aren't available, an encrypted environment variable or server secret might be adequate.

Don't expose client secrets in source code or application configuration, and never retrieve secrets using HTTP API calls (or similar) when generating access tokens on the client.

## User access tokens and refresh tokens

User access tokens should be encrypted and stored separately from refresh tokens. Think carefully about the systems and processes that can access these tokens. Discard tokens when they are no longer needed.

## GitHub secret scanning

Canva has partnered with GitHub secret scanning to automatically detect and revoke Canva secrets that have been published to GitHub repositories. As a result, if GitHub detects your access token or client secret in a public GitHub repository, we will automatically revoke it to help minimize the harm of leaked secrets.

## Integration security

This is a list of good practices to help secure your integration.

* Don't expose tokens to the end-user after they're stored in your database.
* Ensure there's no functionality that echoes tokens (or any other customer secrets) back to the user.
* If a secret storage vault is not an option, consider creating a middleware layer instead of storing the token in your integration's code.
* To help prevent misuse of the token, lock down the usage of your integration itself.
* Consider how an attacker can abuse your integration's functionality to gain access to a token, or trigger functionality that might be undesirable.
* Implement rate-limiting.
* Use a database to store tokens, and don't store tokens in the code.
* Ensure there is no way to expose one user's token to another user.
* Ensure tokens are stored in a way that directly links them to the Canva user and team.
* If a user deletes their account or revokes consent, ensure you delete any tokens for the user from your systems.
* If you no longer need a customer's token, delete it immediately.
* Conduct regular vulnerability scans against your integration.
* Ensure that client secrets, user access tokens, and refresh tokens aren't sent to application logs.

## External services

External services should be used in a secure way. This includes the following good practices:

* Don't share service credentials across different applications.
* Ensure that service credentials have the minimal set of permissions to perform operations.
* Ensure that all communications to external services use secure transport mechanisms.
* Require secure transport mechanisms (such as HTTPS/TLS) that are resistant to eavesdropping.
* Requests must fail if they return a transport security error.

## Logging

We recommend adding security-specific logging and telemetry to your application. A security log should include the following:

* Authentication and authorization events. This should include failed attempts.
* Service configuration changes.
* Object reads and writes.
* Permission changes.

Your logs should use consistent timestamps for each event. Logs should also include a reference to the user's identity and an IP address.

<Note>Don't log client secrets, user access tokens, or refresh tokens.</Note>

## Infrastructure and hosting

Ensure you follow the security recommendations from your cloud service or hosting provider. This can include:

* Enabling Multi-Factor Authentication (MFA).
* Using strong passwords.
* Ensuring that accounts with access to your production systems actually need that access.
* If you are backing up your data, ensure that you store it in a safe location.
