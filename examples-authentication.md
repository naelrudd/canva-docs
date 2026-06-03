Source: https://www.canva.dev/docs/apps/examples/authentication/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

Third-party authentication integration for external platforms.

## Running this example

To run this example locally:

1. If you haven't already, create a new app in the [Developer Portal](https://www.canva.com/developers/apps). For more information, refer to our [Quickstart guide](https://www.canva.dev/docs/apps/quickstart/).

2. In your app's configuration on the [Developer Portal](https://www.canva.com/developers/apps), ensure the "Development URL" is set to \http://localhost:8080\.

3. Clone the starter kit:

   \\\shell
   git clone https://github.com/canva-sdks/canva-apps-sdk-starter-kit.git
   cd canva-apps-sdk-starter-kit
   \\\

4. Install dependencies:

   \\\shell
   npm install
   \\\

5. Run the example:
   \\\shell
   npm run start authentication
   \\\

6. Click the **Preview URL** link shown in the terminal to open the example in the Canva editor.

## Example app source code

<Tabs>
  <Tab name="app.tsx">
    \\\	ypescript
    // For usage information, see the README.md file.
    import {
      Button,
      LoadingIndicator,
      Rows,
      Title,
      Text,
      Box,
      MultilineInput,
      FormField,
    } from "@canva/app-ui-kit";
    import { useMemo, useState, useEffect, useCallback } from "react";
    import type { AccessTokenResponse } from "@canva/user";
    import { auth } from "@canva/user";
    import * as styles from "styles/components.css";

    const scope = new Set(["openid"]);

    const BACKEND_URL = \\/custom-route\;

    export function App() {
      // Initialize the Canva OAuth client for user authentication
      const oauth = useMemo(() => auth.initOauth(), []);

      const [accessTokenResponse, setAccessTokenResponse] = useState<
        AccessTokenResponse | undefined
      >(undefined);
      const [error, setError] = useState<string | null>(null);
      const loading = accessTokenResponse === undefined;
      const [responseBody, setResponseBody] = useState<unknown | undefined>(
        undefined,
      );

      useEffect(() => {
        // Check if the user is already authenticated when the component mounts
        retrieveAndSetToken();
      }, [oauth]);

      const authorize = useCallback(async () => {
        setAccessTokenResponse(undefined);
        setError(null);
        try {
          // Trigger the OAuth authorization flow - this opens Canva's authorization UI
          await oauth.requestAuthorization({ scope });
          await retrieveAndSetToken();
        } catch (error) {
          setError(error instanceof Error ? error.message : "Unknown error");
        }
      }, []);

      // IMPORTANT: Always call getAccessToken when you need a token - tokens can expire.
      // Canva automatically handles caching and refreshing tokens for you.
      const retrieveAndSetToken = useCallback(async (forceRefresh = false) => {
        try {
          setAccessTokenResponse(
            await oauth.getAccessToken({ forceRefresh, scope }),
          );
        } catch (error) {
          setError(error instanceof Error ? error.message : "Unknown error");
        }
      }, []);

      const logout = useCallback(async () => {
        setAccessTokenResponse(undefined);
        // Revoke the user's authorization and clear stored tokens
        await oauth.deauthorize();
        setAccessTokenResponse(null);
      }, []);

      const fetchData = useCallback(async () => {
        const accessToken = accessTokenResponse?.token;
        if (!accessToken) {
          return;
        }

        try {
          // Example of using the access token to make authenticated API requests
          const res = await fetch(BACKEND_URL, {
            headers: {
              Authorization: \Bearer \\,
            },
          });

          const data = await res.json();
          setResponseBody(data);
        } catch (error) {
          setError(error instanceof Error ? error.message : "Unknown error");
        }
      }, [accessTokenResponse]);

      const result = (
        <div className={styles.scrollContainer}>
          <Box
            justifyContent="center"
            width="full"
            alignItems="center"
            display="flex"
            height="full"
          >
            {error ? (
              <Rows spacing="2u">
                <Title>Authorization error</Title>
                <Text>{error}</Text>
                <Button variant="primary" onClick={authorize}>
                  Try again
                </Button>
              </Rows>
            ) : loading ? (
              <LoadingIndicator />
            ) : !accessTokenResponse ? (
              <Rows spacing="2u">
                <Title>Sign in required</Title>
                <Text>
                  This example demonstrates how apps can allow users to authorize
                  with the app via a third-party platform.
                </Text>
                <Text>
                  To set up please see the README.md in the
                  /examples/fundamentals/authentication folder
                </Text>
                <Text>
                  To use "Example App", you must sign in with your "Example"
                  account.
                </Text>
                <Button variant="primary" onClick={authorize}>
                  Sign in to Example
                </Button>
              </Rows>
            ) : (
              <Rows spacing="2u">
                <Text>Logged in!</Text>
                <Button variant="primary" onClick={async () => { logout(); }}>
                  Log out
                </Button>
                <Button variant="primary" onClick={fetchData}>
                  Fetch data
                </Button>
                {responseBody ? (
                  <FormField label="Response" value={JSON.stringify(responseBody, null, 2)} control={(props) => (<MultilineInput {...props} maxRows={5} autoGrow readOnly />)} />
                ) : null}
              </Rows>
            )}
          </Box>
        </div>
      );
      return result;
    }
    \\\
  </Tab>

  <Tab name="index.tsx">
    \\\	ypescript
    import { AppUiProvider } from "@canva/app-ui-kit";
    import { createRoot } from "react-dom/client";
    import { App } from "./app";
    import "@canva/app-ui-kit/styles.css";
    import type { DesignEditorIntent } from "@canva/intents/design";
    import { prepareDesignEditor } from "@canva/intents/design";

    async function render() {
      const root = createRoot(document.getElementById("root") as Element);
      root.render(
        <AppUiProvider>
          <App />
        </AppUiProvider>,
      );
    }

    const designEditor: DesignEditorIntent = { render };
    prepareDesignEditor(designEditor);

    if (module.hot) {
      module.hot.accept("./app", render);
    }
    \\\
  </Tab>

  <Tab name="README.md">
    \\\markdown
    # Authentication

    Demonstrates how to implement OAuth authentication flow for accessing external services on behalf of users. Shows token management, user authorization, and authenticated API requests.

    For API reference docs and instructions on running this example, see: https://www.canva.dev/docs/apps/examples/authentication/.

    Related examples: See fundamentals/fetch for general API communication, or design_interaction/design_token for design-specific authentication patterns.

    NOTE: This example differs from what is expected for public apps to pass a Canva review:

    - Token storage and security is simplified for demonstration. Production apps must implement secure token storage and follow OAuth security best practices
    - Error handling for authentication failures is simplified for demonstration. Production apps must implement comprehensive error handling with clear user feedback and graceful failure modes
    - Token refresh mechanisms are not implemented. Production apps should implement proper token lifecycle management
    - Internationalization is not implemented. Production apps must support multiple languages using the \@canva/app-i18n-kit\ package to pass Canva review requirements
    - The code structure is simplified: Production apps using [intents](https://www.canva.dev/docs/apps/intents/) are recommended to call the prepareDesignEditor function from src/intents/design_editor/index.tsx
    \\\
  </Tab>

  <Tab name="SETUP.md">
    \\\markdown
    # Setup

    ## Getting started

    Before using this example, you'll need to [configure your provider details](https://www.canva.dev/docs/apps/authenticating-users/oauth/#prerequisite-configure-developer-portal) in the developer portal.

    Once this is done, simply run the example from the root of \canva-apps-sdk-starter-kit\ with:

    \\\sh
    npm start authentication
    \\\
    \\\
  </Tab>
</Tabs>

## API reference

* [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/)
* [\uth.initOauth\](https://www.canva.dev/docs/apps/api/latest/user-auth-init-oauth/)
* [\prepareDesignEditor\](https://www.canva.dev/docs/apps/api/latest/intents-design-prepare-design-editor/)

## Need help?

* Join our [Community Forum](https://community.canva.dev/)
* Report issues with this example on [GitHub](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/issues)

