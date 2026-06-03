Source: https://www.canva.dev/docs/apps/authenticating-users/oauth-multi-provider/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Multi-provider OAuth

Allow users to connect to multiple OAuth providers simultaneously.

Multi-provider OAuth enables your app to integrate with multiple OAuth providers (for example, Meta and Google) simultaneously, allowing users to connect to different platforms independently. Each provider maintains its own authentication state and tokens.

## Key concepts

### Multi-provider vs multi-account

It's important to understand the difference between these two concepts:

* **Multi-provider OAuth**: Your app connects to multiple different OAuth providers (for example, Meta and Google). Each provider is configured separately and maintains independent authentication state.
* **Multi-account OAuth**: Your app connects to multiple accounts from the same OAuth provider (for example, multiple Meta accounts). See [Multi-account OAuth](https://www.canva.dev/docs/apps/authenticating-users/oauth-multi-account/) for more information.

You can combine both approaches: use multi-provider OAuth to support multiple providers, and use multi-account OAuth for each provider to allow multiple accounts per provider.

### Provider configuration

Each OAuth provider must be configured separately in the Developer Portal. The `provider` parameter identifies which OAuth configuration to use:

* Each provider has its own authorization endpoint, token endpoint, client ID, and client secret
* Providers can have different scopes and settings
* Each provider maintains independent authentication state

### Independent state management

When using multiple providers, each provider's authentication state is managed independently:

* Tokens are stored separately for each provider
* Authorization flows are independent
* Users can connect or disconnect providers independently
* API requests use provider-specific tokens

## When to use multi-provider OAuth

Consider using multi-provider OAuth when:

* Your app needs to integrate with multiple external platforms (for example, social media platforms, cloud storage services)
* Users need to connect to different services simultaneously
* Your app publishes content to multiple platforms and users need to choose destinations
* You want to provide users with flexibility to connect only the services they use

If your app only needs to integrate with a single OAuth provider, use the [traditional OAuth flow](https://www.canva.dev/docs/apps/authenticating-users/oauth/) instead.

## Add multi-provider OAuth to your app

### Prerequisites

Before implementing multi-provider OAuth:

1. Configure each OAuth provider in the [Developer Portal](https://www.canva.com/developers/apps) following the [steps in the OAuth integration guide](https://www.canva.dev/docs/apps/authenticating-users/oauth/#prerequisite-configure-developer-portal).
2. Each provider needs to be configured separately with its own:
   * Authorization endpoint
   * Token endpoint
   * Client ID and Client Secret
   * Provider name (used to identify the provider in your code)

For example, if you're integrating with Meta and Google, you would configure:

* A Meta provider with provider name `meta`
* A Google provider with provider name `google`

### Step 1: Initialize OAuth clients for each provider

Import the required libraries and initialize separate OAuth clients for each provider:

```ts
import { auth } from "@canva/user";

// Provider names as defined in the Developer Portal
const META_PROVIDER = "meta" as const;
const GOOGLE_PROVIDER = "google" as const;

// Initialize separate OAuth clients for each provider
const metaOauth = auth.initOauth({
  type: "single_account",
  provider: META_PROVIDER,
});

const googleOauth = auth.initOauth({
  type: "single_account",
  provider: GOOGLE_PROVIDER,
});
```

NOTE: You can use `multi_account` type instead of `single_account` if you want to support multiple accounts per provider. See [Multi-account OAuth](https://www.canva.dev/docs/apps/authenticating-users/oauth-multi-account/) for more information.

### Step 2: Create state variables for each provider

Create separate state variables to track the authentication status for each provider:

```tsx
import { useState, useEffect, useMemo, useCallback } from "react";
import type { AccessTokenResponse } from "@canva/user";

type ProviderStatus = {
  accessTokenResponse: AccessTokenResponse | null | undefined;
  error: string | null;
  loading: boolean;
  responseBody: unknown | undefined;
};

export const App = () => {
  // Track state for each provider independently
  const [metaStatus, setMetaStatus] = useState<ProviderStatus>({
    accessTokenResponse: undefined,
    error: null,
    loading: false,
    responseBody: undefined,
  });

  const [googleStatus, setGoogleStatus] = useState<ProviderStatus>({
    accessTokenResponse: undefined,
    error: null,
    loading: false,
    responseBody: undefined,
  });
```

### Step 3: Create helper functions

Create helper functions to manage provider-specific operations:

```tsx
// Define provider-specific scopes
const metaScope = new Set(["openid"]);
const googleScope = new Set(["openid", "profile", "email"]);

// Helper function to get the OAuth client for a provider
const getOauthClient = (provider: typeof META_PROVIDER | typeof GOOGLE_PROVIDER) => {
  return provider === META_PROVIDER ? metaOauth : googleOauth;
};

// Helper function to get scopes for a provider
const getScope = (provider: typeof META_PROVIDER | typeof GOOGLE_PROVIDER) => {
  return provider === META_PROVIDER ? metaScope : googleScope;
};

// Helper function to get status for a provider
const getStatus = (provider: typeof META_PROVIDER | typeof GOOGLE_PROVIDER) => {
  return provider === META_PROVIDER ? metaStatus : googleStatus;
};

// Helper function to set status for a provider
const setStatus = (
  provider: typeof META_PROVIDER | typeof GOOGLE_PROVIDER,
  updates: Partial<ProviderStatus>,
) => {
  if (provider === META_PROVIDER) {
    setMetaStatus((prev) => ({ ...prev, ...updates }));
  } else {
    setGoogleStatus((prev) => ({ ...prev, ...updates }));
  }
};
```

### Step 4: Check existing authentication on mount

Check if users are already authenticated when the component mounts:

```tsx
useEffect(() => {
  // Check if users are already authenticated when the component mounts
  retrieveAndSetToken(META_PROVIDER);
  retrieveAndSetToken(GOOGLE_PROVIDER);
}, [metaOauth, googleOauth]);
```

### Step 5: Implement authorization flow

Create a function to authorize users for a specific provider:

```tsx
const authorize = useCallback(
  async (provider: typeof META_PROVIDER | typeof GOOGLE_PROVIDER) => {
    const oauth = getOauthClient(provider);
    const scope = getScope(provider);

    setStatus(provider, {
      accessTokenResponse: undefined,
      error: null,
      loading: true,
    });

    try {
      // Trigger the OAuth authorization flow for the specific provider
      await oauth.requestAuthorization({ scope });
      await retrieveAndSetToken(provider);
    } catch (error) {
      setStatus(provider, {
        error: error instanceof Error ? error.message : "Unknown error",
        loading: false,
      });
    }
  },
  [metaOauth, googleOauth],
);
```

### Step 6: Retrieve and manage access tokens

Create a function to retrieve access tokens for a provider:

```tsx
// IMPORTANT: Always call getAccessToken when you need a token - tokens can expire.
// Canva automatically handles caching and refreshing tokens for you.
const retrieveAndSetToken = useCallback(
  async (
    provider: typeof META_PROVIDER | typeof GOOGLE_PROVIDER,
    forceRefresh = false,
  ) => {
    const oauth = getOauthClient(provider);
    const scope = getScope(provider);

    setStatus(provider, { loading: true });
    try {
      const accessTokenResponse = await oauth.getAccessToken({
        forceRefresh,
        scope,
      });
      setStatus(provider, {
        accessTokenResponse,
        loading: false,
      });
    } catch (error) {
      setStatus(provider, {
        error: error instanceof Error ? error.message : "Unknown error",
        loading: false,
      });
    }
  },
  [metaOauth, googleOauth],
);
```

### Step 7: Implement logout

Create a function to disconnect a provider:

```tsx
const logout = useCallback(
  async (provider: typeof META_PROVIDER | typeof GOOGLE_PROVIDER) => {
    const oauth = getOauthClient(provider);
    setStatus(provider, {
      accessTokenResponse: undefined,
      loading: true,
    });
    // Revoke the user's authorization and clear stored tokens for the specific provider
    await oauth.deauthorize();
    setStatus(provider, {
      accessTokenResponse: null,
      loading: false,
      responseBody: undefined,
    });
  },
  [metaOauth, googleOauth],
);
```

### Step 8: Make authenticated API requests

When making API requests, use the access token from the appropriate provider:

```tsx
const fetchData = useCallback(
  async (provider: typeof META_PROVIDER | typeof GOOGLE_PROVIDER) => {
    const status = getStatus(provider);
    const accessToken = status.accessTokenResponse?.token;
    if (!accessToken) {
      return;
    }

    // Use provider-specific backend URL
    const backendUrl =
      provider === META_PROVIDER ? META_BACKEND_URL : GOOGLE_BACKEND_URL;

    setStatus(provider, { loading: true });
    try {
      // Example of using the access token to make authenticated API requests
      const res = await fetch(backendUrl, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });

      const data = await res.json();
      setStatus(provider, {
        responseBody: data,
        loading: false,
      });
    } catch (error) {
      setStatus(provider, {
        error: error instanceof Error ? error.message : "Unknown error",
        loading: false,
      });
    }
  },
  [metaStatus.accessTokenResponse, googleStatus.accessTokenResponse],
);
```

### Step 9: Display provider sections in UI

Create a reusable component to render the UI for each provider:

```tsx
import { Button, Text, Title, Rows, Box, LoadingIndicator } from "@canva/app-ui-kit";

const renderProviderSection = (
  provider: typeof META_PROVIDER | typeof GOOGLE_PROVIDER,
  providerDisplayName: string,
) => {
  const status = getStatus(provider);
  const loading = status.loading && status.accessTokenResponse === undefined;
  const isConnected = status.accessTokenResponse != null;

  return (
    <Box
      padding="3u"
      border="control"
      borderRadius="standard"
      background="neutral"
    >
      <Rows spacing="2u">
        <Title size="small">{providerDisplayName} Provider</Title>

        {status.error ? (
          <Rows spacing="1u">
            <Text tone="critical">Error: {status.error}</Text>
            <Button
              variant="primary"
              onClick={() => authorize(provider)}
              disabled={loading}
            >
              Try again
            </Button>
          </Rows>
        ) : loading ? (
          <LoadingIndicator />
        ) : !isConnected ? (
          <Rows spacing="2u">
            <Text>
              Connect your {providerDisplayName} account to use this provider.
            </Text>
            <Button
              variant="primary"
              onClick={() => authorize(provider)}
              disabled={loading}
            >
              {`Sign in to ${providerDisplayName}`}
            </Button>
          </Rows>
        ) : (
          <Rows spacing="2u">
            <Text>Connected to {providerDisplayName}!</Text>
            <Button
              variant="secondary"
              onClick={() => logout(provider)}
              disabled={loading}
            >
              Log out
            </Button>
            <Button
              variant="primary"
              onClick={() => fetchData(provider)}
              disabled={loading}
            >
              Fetch data
            </Button>
          </Rows>
        )}
      </Rows>
    </Box>
  );
};

// Use in your component
return (
  <Rows spacing="3u">
    <Title>Multi-provider authentication</Title>
    {renderProviderSection(META_PROVIDER, "Meta")}
    {renderProviderSection(GOOGLE_PROVIDER, "Google")}
  </Rows>
);
```

## Complete example

For a complete working example, see the [multi-provider authentication example](https://www.canva.dev/docs/apps/examples/multi-provider-authentication/) in the starter kit.

## Recommended practices

### Provider management

* Initialize OAuth clients using `useMemo` to avoid recreating them on every render
* Use consistent provider names that match your Developer Portal configuration
* Create helper functions to manage provider-specific operations

### State management

* Track state independently for each provider
* Use separate state variables or a state object keyed by provider
* Handle loading and error states per provider

### User experience

* Clearly indicate which provider each section represents
* Show connection status for each provider independently
* Allow users to connect or disconnect providers independently
* Provide clear error messages specific to each provider

### Token management

* Always call `getAccessToken()` when you need a token; don't cache tokens yourself
* Canva automatically handles token caching and refreshing
* Use provider-specific tokens for API requests
* Handle token expiration gracefully per provider

### Error handling

* Handle errors independently for each provider
* Provide clear error messages when authorization fails
* Allow users to retry authorization for specific providers
* Gracefully handle network errors when making API requests

### Security

* Use the `deauthorize()` method to properly revoke access when disconnecting providers
* Validate that tokens exist before making API requests
* Handle token refresh automatically by relying on Canva's token management
* Never expose tokens in client-side code or logs

## Related documentation

* [OAuth integration](https://www.canva.dev/docs/apps/authenticating-users/oauth/): Single-provider OAuth authentication
* [Multi-account OAuth](https://www.canva.dev/docs/apps/authenticating-users/oauth-multi-account/): Multiple accounts from the same provider
* [Multi-provider authentication example](https://www.canva.dev/docs/apps/examples/multi-provider-authentication/): Complete working example

## API reference

For more information about the OAuth API, see:

* [auth.initOauth](https://www.canva.dev/docs/apps/api/preview/user-auth-init-oauth/)
