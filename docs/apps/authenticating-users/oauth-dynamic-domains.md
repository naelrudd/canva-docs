Source: https://www.canva.dev/docs/apps/authenticating-users/oauth-dynamic-domains/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynamic domains OAuth

Configure OAuth providers with wildcard subdomains

WARNING: Dynamic domains support for OAuth is provided as a preview. Preview APIs are unstable and may change without warning. You can't release public apps using a preview API until it's stable.

Some OAuth providers require tenant-specific subdomains in their authorization URLs. For example, a provider might use `https://{workspace}.example.com/oauth/authorize`, where each workspace has its own subdomain.

Previously, apps had to configure a fixed URL for each tenant, making it impractical for multi-tenant scenarios. Dynamic domains support enables apps to configure a single wildcard URL pattern (for example, `https://*.example.com/oauth`) and dynamically replace the subdomain during the OAuth flow.

Dynamic domains support lets you:

* Configure OAuth providers with wildcard subdomains (for example, `https://*.example.com/oauth`)
* Use the same OAuth configuration for multiple tenants
* Collect the subdomain from users during authorization
* Automatically use the subdomain for all subsequent OAuth operations (token refresh, revocation, user info)

The SDK handles subdomain collection through a connection screen that prompts users to enter their subdomain when required. The subdomain is stored securely and used consistently throughout the OAuth lifecycle.

## When to use dynamic domains

Use dynamic domains support when:

* Your OAuth provider requires tenant-specific subdomains (for example, Slack workspaces or other multi-tenant providers)
* Each user needs to specify their organization's subdomain during authentication
* Your provider uses subdomain-based routing for different customer instances

If your OAuth provider uses static URLs without subdomain requirements, use the [standard OAuth integration](https://www.canva.dev/docs/apps/authenticating-users/oauth/) instead.

## How it works

When you configure an OAuth provider with a wildcard subdomain pattern, the following flow occurs:

1. **Configuration**: You configure the OAuth provider in the Developer Portal with a wildcard URL pattern (for example, `https://*.example.com/oauth/authorize`).

2. **Authorization request**: When your app calls `oauth.requestAuthorization()`, Canva detects the wildcard pattern.

3. **Subdomain collection**: If no subdomain is provided, Canva displays a connection screen prompting the user to enter their subdomain. The screen shows:
   * App name and icon
   * Domain suffix (for example, ".example.com")
   * Input field for subdomain entry
   * Validation feedback for invalid subdomain formats

4. **URL replacement**: Canva automatically replaces the wildcard (`*`) with the user's subdomain for:
   * Authorization URL
   * Token exchange URL
   * Token refresh URL
   * Token revocation URL
   * User info URL (when multi-account mode is enabled)

## Configuration

### URL validation rules

When configuring OAuth providers with wildcard subdomains, follow these validation rules:

* **Wildcard position**: The wildcard (`*`) must be in the subdomain position only
* **Single wildcard**: Only one wildcard is allowed per URL
* **Domain requirement**: The URL must include a valid domain after the wildcard

**Valid examples:**

* `https://*.example.com/oauth/authorize`
* `https://*.example.com/oauth/token`
* `https://*.slack.com/api/oauth.authorize`

**Invalid examples:**

* `https://example.*.com/oauth` (wildcard not in subdomain position)
* `https://*.example.*.com/oauth` (multiple wildcards)
* `https://*.com/oauth` (no domain after wildcard)

### Developer Portal configuration

Configure dynamic domains support in the [Developer Portal](https://www.canva.com/developers/apps):

1. Navigate to your app's **Authentication** page.
2. Select **This app requires authentication**.
3. Select the **Open Authorization** protocol.
4. In the **Provider** field, enter a name (for example, `myprovider`).
5. In the **Credentials** section, configure the following URLs with wildcard patterns:
   * **Authorization server URL**: `https://*.example.com/oauth/authorize`
   * **Token exchange URL**: `https://*.example.com/oauth/token`
   * **Revocation exchange URL** (optional): `https://*.example.com/oauth/revoke`
   * **User info URL** (optional, for multi-account mode): `https://*.example.com/oauth/userinfo`

<Note>
  You can configure combinations where the authorization URL uses a wildcard subdomain, but other fields use static URLs. However, if the authorization URL is static, other fields can't contain wildcards in the subdomain position.
</Note>

For more information about configuring OAuth providers, see [Prerequisite: Configure Developer Portal](https://www.canva.dev/docs/apps/authenticating-users/oauth/#prerequisite-configure-developer-portal).

<Note>
  When using subdomains for OAuth providers, it's important to maintain ownership and proper lifecycle management of these subdomains to prevent security risks. For more information, see [Security guidelines](https://www.canva.dev/docs/apps/security-guidelines/#maintain-ownership-of-subdomains).
</Note>

## API usage

The SDK exposes the `subdomain` field in `AccessTokenResponse` and `OauthAccount`, allowing you to construct full URLs for API calls or differentiate between different accounts in multi-account mode.

### Single-account usage

When using single-account OAuth mode, retrieve the subdomain from the `AccessTokenResponse`:

```typescript
import { auth } from '@canva/user';

const oauth = auth.initOauth({
  type: 'single_account',
  provider: 'myprovider',
  scope: new Set(['openid']),
});

const getBaseUrl = (subdomain: string) =>
  `https://${subdomain}.example.com/api`;

async function requestData() {
  let response = await oauth.getAccessToken();
  if (!response) {
    await oauth.requestAuthorization();
    response = await oauth.getAccessToken();
  }
  if (!response || !response.subdomain) {
    throw new Error('No access token or subdomain available');
  }
  return fetch(getBaseUrl(response.subdomain), {
    headers: {
      Authorization: `Bearer ${response.token}`,
    },
  });
}
```

For more information about single-account OAuth, see [OAuth integration](https://www.canva.dev/docs/apps/authenticating-users/oauth/).

### Multi-account usage

When using multi-account OAuth mode, retrieve the subdomain from the `OauthAccount`:

```typescript
import { auth, type OauthAccount } from '@canva/user';

const oauth = auth.initOauth({
  type: 'multi_account',
  provider: 'myprovider',
  scope: new Set(['openid']),
});

const getBaseUrl = (subdomain: string) =>
  `https://${subdomain}.example.com/api`;

async function requestData(account: OauthAccount) {
  let response = await account.getAccessToken();
  if (!response) {
    await oauth.requestAuthorization();
    return;
  }
  if (!response.subdomain) {
    throw new Error('No subdomain available');
  }
  return fetch(getBaseUrl(response.subdomain), {
    headers: {
      Authorization: `Bearer ${response.token}`,
    },
  });
}
```

For more information about multi-account OAuth, see [Multi-account OAuth](https://www.canva.dev/docs/apps/authenticating-users/oauth-multi-account/).

## Backward compatibility

Dynamic domains support is fully backward compatible:

* **Existing configurations**: OAuth configurations without wildcards continue to work unchanged
* **No breaking changes**: Apps using static OAuth URLs are unaffected
* **Gradual adoption**: You can migrate to wildcard URLs when needed without affecting existing users

## Limitations

The following limitations apply to dynamic domains support:

* **Subdomain alias**: Developer-configurable subdomain aliases aren't currently supported. Users must enter the exact subdomain required by their OAuth provider.
* **URL combinations**: While you can mix wildcard authorization URLs with static token exchange URLs, you can't use wildcards in token exchange, revocation, or user info URLs if the authorization URL is static.
* **Subdomain validation**: Subdomains must contain only alphanumeric characters and hyphens, and can't start or end with a hyphen.

## Error handling

When using dynamic domains, be aware of these error scenarios:

* **Missing subdomain**: If a wildcard URL is configured but no subdomain is stored, token refresh and revocation operations will fail. In this case, the user must re-authenticate.
* **Invalid subdomain format**: The connection screen validates subdomain format and provides feedback to users.
* **Configuration mismatch**: If the OAuth configuration changes to include wildcards after accounts are created, existing accounts may need to be re-authenticated.

For more information about OAuth error handling, see [OAuth troubleshooting](https://www.canva.dev/docs/apps/authenticating-users/oauth-troubleshooting/).

## Related documentation

* [OAuth integration](https://www.canva.dev/docs/apps/authenticating-users/oauth/) - General OAuth concepts and setup
* [Multi-account OAuth](https://www.canva.dev/docs/apps/authenticating-users/oauth-multi-account/) - Managing multiple accounts from the same provider
* [Multi-provider OAuth](https://www.canva.dev/docs/apps/authenticating-users/oauth-multi-provider/) - Integrating with multiple OAuth providers
* [OAuth troubleshooting](https://www.canva.dev/docs/apps/authenticating-users/oauth-troubleshooting/) - Error codes and troubleshooting
* [Security guidelines](https://www.canva.dev/docs/apps/security-guidelines/#maintain-ownership-of-subdomains) - Security best practices for subdomain management

## API reference

For more information about the OAuth API, see:

* [auth.initOauth](https://www.canva.dev/docs/apps/api/preview/user-auth-init-oauth/) - OAuth initialization and methods
