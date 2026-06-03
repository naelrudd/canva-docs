Source: https://www.canva.dev/docs/apps/authenticating-users/oauth-multi-account/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Multi-account OAuth

Allow users to connect and manage multiple OAuth accounts from the same provider.

Multi-account OAuth enables users to connect multiple accounts from the same OAuth provider within your app. This is particularly useful for cases when users need to switch between different profiles on the same platform.

## Key concepts

### Single-account vs multi-account mode

OAuth can be initialized in two modes:

* **Single-account mode**: The traditional OAuth flow where only one account per provider can be connected at a time. When a user authorizes a new account, it replaces any previously connected account.
* **Multi-account mode**: Allows users to connect multiple accounts from the same provider. Each account is stored separately and can be accessed, refreshed, or disconnected individually.

### Provider configuration

The `provider` parameter identifies which OAuth configuration to use from the Developer Portal. This allows your app to configure provider-specific settings like scopes and endpoints.

### Account management

In multi-account mode, each connected account includes:

* **ID**: A unique identifier for the account in the external provider's system
* **Principal**: The user's unique identifier from the OAuth provider (for example, email address)
* **Display name**: The user's name as provided by the OAuth provider
* **Avatar URL**: The user's profile picture URL
* **Expiry status**: Whether the account's access token has expired

## When to use multi-account OAuth

Consider using multi-account OAuth when:

* Users need to manage multiple accounts from the same platform (for example, multiple social media accounts)
* Your app publishes content to external platforms and users want to choose the destination account
* Users switch between personal and business accounts on the same platform
* Your app integrates with team or organization accounts where users manage multiple profiles

If your app only needs access to a single account per provider, use the [traditional OAuth flow](https://www.canva.dev/docs/apps/authenticating-users/oauth/) instead.

If your app needs to integrate with multiple OAuth providers (for example, both Google and Meta), see [Multi-provider OAuth](https://www.canva.dev/docs/apps/authenticating-users/oauth-multi-provider/).

## Add multi-account OAuth to your app

### Prerequisites

Before implementing multi-account OAuth:

1. Configure your OAuth provider in the [Developer Portal](https://www.canva.com/developers/apps) following the [steps in the OAuth integration guide](https://www.canva.dev/docs/apps/authenticating-users/oauth/#prerequisite-configure-developer-portal).
2. Configure the **User profile endpoint** and **field mappings** in the Developer Portal. This endpoint is used to fetch user profile information (display name, avatar) after authentication.

#### Profile field mapping

When configuring your OAuth provider in the Developer Portal, you must map fields from your provider's user profile response to Canva's expected fields. This mapping tells Canva how to extract user information from your OAuth provider's profile endpoint.

The required field mappings are:

* **`externalId`**: Maps to the unique user identifier from your OAuth provider (for example, `sub` for OpenID Connect providers, `id` for many social platforms).
* **`displayName`**: Maps to the user's display name (for example, `name`, `display_name`, or `full_name`).
* **`principal`**: Maps to the user's primary identifier, typically their email address (for example, `email`).
* **`avatarUrl`** (optional): Maps to the user's profile picture URL (for example, `picture`, `avatar_url`, or `profile_image_url`).

For example, if your OAuth provider returns a profile response like:

```json
{
  "sub": "1234567890",
  "name": "Jane Doe",
  "email": "jane.doe@example.com",
  "picture": "https://example.com/avatar.jpg"
}
```

Your field mappings in the Developer Portal would be:

* **`externalId`**: `sub`
* **`displayName`**: `name`
* **`principal`**: `email`
* **`avatarUrl`**: `picture`

NOTE: The field mapping configuration is critical for multi-account OAuth to work correctly. Incorrect mappings prevents Canva from properly identifying and displaying user accounts.

### Important provider configuration notes

WARNING: When you create an OAuth provider in the Developer Portal, you can't change the multi-account setting. The multi-account flag is immutable after creating an OAuth provider.

If you need to switch between single-account and multi-account modes:

1. **Delete the existing provider** from the Developer Portal.
2. **Create a new provider** with the desired multi-account setting.
3. **Reconfigure all settings** including endpoints, scopes, and field mappings.

**Impact of provider deletion:**

* **All existing user authentications will be revoked**. Users who previously connected their accounts will need to re-authenticate.
* **All stored access and refresh tokens will be invalidated**. Your app will lose access to external APIs for all users.
* **User data associated with the provider may be lost**. Depending on how your app stores user information.

Consider the multi-account requirement carefully during initial setup to avoid disrupting existing users.

### Step 1: Initialize OAuth in multi-account mode

Import the required libraries and initialize OAuth with multi-account options:

```ts
import { auth } from "@canva/user";

const oauth = auth.initOauth({
  type: "multi_account",
  provider: "meta",
});
```

### Step 2: Create state variables and render the account switcher

Create state variables to track the selected account, then use `OauthAccountSwitcher` from `@canva/app-components` to let users sign in, switch, and manage linked accounts:

```tsx
import { useState } from "react";
import type { OauthAccount } from "@canva/user";
import { OauthAccountSwitcher } from "@canva/app-components";

const scope = new Set(["profile", "email"]);

export const App = () => {
  const [selectedAccount, setSelectedAccount] = useState<OauthAccount | null>(null);

  const handleAccountSwitch = (account: OauthAccount | null) => {
    setSelectedAccount(account);
  };

  return (
    <>
      <OauthAccountSwitcher
        oauth={oauth}
        scope={scope}
        signInLabel="Sign in"
        triggerLabel="Switch Account"
        appName="My app"
        onAccountSwitch={handleAccountSwitch}
      />
    </>
  );
};
```

### Step 3: Use access tokens for API requests

When making API requests, use the access token from the selected account:

```ts
const fetchData = async () => {
  if (!selectedAccount) {
    return;
  }

  try {
    // Get the access token for the selected account
    const tokenResponse = await selectedAccount.getAccessToken();

    if (!tokenResponse) {
      // Access token not available, user needs to re-authorize
      console.error("No access token available");
      return;
    }

    // Make an authenticated API request
    const response = await fetch("https://api.example.com/data", {
      headers: {
        Authorization: `Bearer ${tokenResponse.token}`,
      },
    });

    const data = await response.json();
    console.log("API response:", data);
  } catch (error) {
    console.error("Failed to fetch data:", error);
  }
};
```

## Complete example

For a complete working implementation, see:

* [Multi-account authentication example](https://www.canva.dev/docs/apps/examples/multi-account-authentication/)

## Recommended practices

### Account identification

* Use the `principal` field (for example, email address) to help users identify their accounts
* Display the `displayName` and `avatarUrl` to provide visual context
* Show the `expired` status to alert users when re-authorization is needed

### User experience

* Clearly indicate which account is currently selected
* Provide a way to switch between accounts without disconnecting
* Make it easy to add additional accounts
* Show account information (name, profile picture) in selection interfaces

### Error handling

* Handle cases where `getAccessToken()` returns `null` (token unavailable or expired)
* Provide clear error messages when authorization fails
* Gracefully handle network errors when fetching account lists
* Prompt users to re-authorize when tokens expire

### Security

* Always call `getAccessToken()` to get the latest token; don't cache tokens yourself
* Use the `deauthorize()` method to properly revoke access when disconnecting accounts
* Validate that the selected account exists before making API requests
* Handle token refresh automatically by relying on Canva's token management

## API reference

For more information about the multi-account OAuth API, see:

* [auth.initOauth](https://www.canva.dev/docs/apps/api/latest/user-auth-init-oauth/)
