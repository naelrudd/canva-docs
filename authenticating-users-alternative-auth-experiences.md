Source: https://www.canva.dev/docs/apps/authenticating-users/alternative-auth-experiences/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Alternative authentication experiences

Alternatives for non-standard authentication scenarios.

Managing sensitive information like API keys responsibly is an important part of building secure, user-trusted apps.

This guide outlines preferred patterns for managing user authentication and sensitive information, with solutions tailored to the capabilities and constraints of Canva's environment.

Before you begin, review the [Authentication design guidelines](https://www.canva.dev/docs/apps/design-guidelines/authentication/).

## When not to use alternative authentication

Alternative authentication patterns should only be used when no Canva pattern can support your use case. In almost all situations, you should avoid building custom auth flows and instead use one of the following:

* [Frictionless authentication](https://www.canva.dev/docs/apps/authenticating-users/frictionless/)
* [OAuth integration](https://www.canva.dev/docs/apps/authenticating-users/oauth/)

If your app can be redesigned to avoid handling secrets in the frontend — or to rely on Canva's built-in authentication APIs — you should always choose those options first.

Alternative authentication is a last resort, and should be used only when the recommended approaches cannot meet functional or product requirements.

For a full explanation of Canva's authentication model, see [Authenticating users](https://www.canva.dev/docs/apps/authenticating-users/).

## Key principles for success

* **Design for minimal exposure.** Secrets should only be handled in the frontend when absolutely necessary and for the shortest possible time.
* **Prioritize secure backend operations.** Whenever possible, use our OAuth integration which handles the OAuth flow and the management of access and refresh tokens for you.
* **Use short-lived, scoped tokens.** When secrets must be used in the frontend, prefer API keys that expire and are limited in what they can access.

## Recommended approaches

### Frictionless authentication (preferred)

**Best for:** Apps that don't require traditional login upfront, or may not need authentication at all.

You can use the `auth.getCanvaUserToken()` method to access a signed-in user's data without requiring a separate login flow. This approach enables users to interact with your app immediately (no password prompts or popups), allowing them to explore functionality first and authenticate only when necessary.

**Why choose it:**

* Reduces user friction by avoiding login walls.
* Lets users experience value before being asked to authenticate.
* Simplifies the developer experience; no token handling required.

See [Frictionless authentication](https://www.canva.dev/docs/apps/authenticating-users/frictionless/).

### OAuth integration (recommended for third-party access)

**Best for:** Apps that connect to external platforms like Google Drive, Dropbox, or similar.

OAuth allows users to securely authorize your app to access third-party resources without exposing their credentials. Canva simplifies this process by handling the full OAuth flow (including token exchange and refreshes) on your behalf.

**Why choose it:**

* Canva manages both access and refresh tokens securely.
* Reduces your app's need to store or handle secrets directly.
* Aligns with industry standards using the OAuth 2 Authorization Code flow (with or without Proof Key Code Exchange (PKCE)).

This approach not only strengthens security but also improves the user experience by streamlining how users grant permissions. Canva's authentication API takes care of all server-side interactions with your selected Identity Provider (IdP).

See [OAuth integration](https://www.canva.dev/docs/apps/authenticating-users/oauth/).

### JavaScript closures for temporary secret storage (use only when needed)

WARNING: Closures should only be used when other, more secure options aren't viable.

**Best for:** Temporarily holding secrets in memory during a session when backend-based or Canva-managed storage isn't feasible, for example API keys.

In rare cases where secrets must be handled directly in the frontend, a JavaScript closure offers a lightweight way to store them temporarily in memory.

```ts
function createSecretStore() {
  let secret = null;
  return {
    setSecret(newSecret) {
      secret = newSecret;
    },
    getSecret() {
      return secret;
    },
    clearSecret() {
      secret = null;
    }
  };
}
const secretStore = createSecretStore();
```

Use responsibly:

* Set secrets only when needed, and clear them promptly.
* Never expose secret storage functions globally.
* Understand that this offers limited protection — secrets can still be accessed through memory inspection.

## What to avoid

To maintain a secure app environment, avoid using storage APIs and browser features that persist data in an inspectable or unsafe way:

Avoid:

* `localStorage`, `sessionStorage`, and `IndexedDB` — not encrypted and easily inspected.

  ```ts
  // Don't
  localStorage.setItem('apiKey', apiKey);
  sessionStorage.setItem('userToken', userToken);
  ```

* Embedding secrets in your JavaScript bundle.

  ```ts
  // Don't
  const token = 'api-key-123';
  ```

* Logging secrets to the browser console or exposing them through query parameters.

  ```ts
  // Don't
  console.log('API key:', token);
  fetch(`https://api.example.com/data?api_key=${token}`);
  ```

## Encoding or encrypting secrets in WebStorage

It's a common misconception that encoding (for example, Base64) or even encrypting secrets in the frontend before storing them in `localStorage` or `sessionStorage` can make them safe.

While these techniques may obscure the data, they don't secure it.

Here's why:

* **Base64 isn't encryption.** It's merely an encoding format. Anyone can decode it with minimal effort.
* **Frontend encryption still requires access to a key.** If you encrypt something in the browser, the encryption key also needs to be present in the browser, which means a user (or an attacker) can extract both the encrypted data and the key. If both are accessible, the encryption provides no meaningful protection.
* **WebStorage is inspectable.** All values stored in `localStorage` or `sessionStorage` can be viewed, copied, and manipulated using browser developer tools, regardless of whether they're encrypted.
* **Encryption doesn't protect against Cross-Site Scripting.** If an attacker exploits a cross-site scripting (XSS) vulnerability, they can access both the stored encrypted value and any in-memory decryption logic or keys, rendering encryption ineffective.
