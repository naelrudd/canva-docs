Source: https://www.canva.dev/docs/apps/intents/url-expander/implementation-guide/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# URL Expander intent implementation guide

Import content from external URLs into Canva AI.

This guide helps you implement the [URL Expander intent](https://www.canva.dev/docs/apps/intents/url-expander/) to enable users to paste URLs from your platform and have the content automatically imported into Canva when using Canva AI.

**Warning:** The URL Expander intent is provided as a preview. Preview intents are unstable and may change without warning. You can't release public apps using a preview intent until it's stable.

## How URL Expander works

When a user pastes a URL into Canva AI, the URL Expander flow allows your app to:

1. **Recognize supported URLs**: Identify URLs from your platform or service based on registered patterns.
2. **Fetch content metadata**: Retrieve information about what the URL points to and display it as a preview.
3. **Import the asset**: Download and add the content to Canva when the user interacts with it.

This creates a seamless experience where users can simply paste a link and immediately work with the content in Canva.

## Creating a URL Expander

### Step 1: Enable the intent

Before an intent can be implemented, it must be enabled. Enabling an intent informs Canva of when and where the app should be invoked throughout the user experience.

You can configure intents for your app with either the Developer Portal or the Canva CLI:

<Tabs storageKey="configuration">
  <Tab name="Developer Portal">
    1. Navigate to an app through the [Your apps](https://www.canva.com/developers/apps) page.
    2. On the **Intents** page, find the "Available intents" section.
    3. For the "URL Expander" intent, click **Set up**.
    4. In the "Configure URL Expander" dialog that appears, you can configure your supported URLs (URL patterns). You can add URL patterns here or configure them later. Click **Done** when finished.
    5. The following sections in this guide will walk you through implementing the intent in your code and configuring URL patterns.
  </Tab>

  <Tab name="Canva CLI">
    1. Set up your app to use the Canva CLI to manage settings using the [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/#manage-configuration-using-the-canva-cli) file.
    2. Set the `intent.url_expander` property to be enrolled. For more information, see [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/#intent-optional).

       For example, the following enables the URL Expander intent.

       ```json
       {
         "intent": {
           "url_expander": {
             "enrolled": true
           }
         }
       }
       ```
  </Tab>
</Tabs>

### Step 2: Enable the required scopes

In the Apps SDK, certain methods require certain scopes to be enabled. If an app attempts to call methods without the required scopes being enabled, the SDK will throw an error.

The URL Expander intent requires the following scopes:

* **Asset write (`canva:asset:private:write`)**

To learn more, see [Configuring scopes](https://www.canva.dev/docs/apps/configuring-scopes/).

### Step 3: Register URL patterns

Before registering the intent, you must define which URL patterns your app can expand. URL patterns use wildcards to match URLs from your platform.

For example, to expand Google Docs URLs:

```typescript
const urlPatterns = [
  "https://docs.google.com/document/d/*",
  "https://docs.google.com/presentation/d/*",
];
```

For detailed information on URL pattern requirements and best practices, see [URL pattern validation rules](https://www.canva.dev/docs/apps/intents/url-expander/url-pattern-validation-rules/).

### Step 4: Register the intent

<Warning>
  During the preview period, you must install and use the beta version of the Canva intents package. Make sure you do this before updating your code to use the intent:

  ```shell
  npm install @canva/intents@beta
  ```
</Warning>

Before an intent can be implemented, it must be registered. Registering the URL Expander intent establishes which URLs your app can expand and how to fetch their content.

To register the intent, call the `prepareUrlExpander` method as soon as the app loads:

```tsx
import { prepareUrlExpander } from "@canva/intents/asset";

// Register the URL Expander when your app loads
prepareUrlExpander({
  urlPatterns: [
    "https://docs.google.com/document/d/*",
    "https://docs.google.com/presentation/d/*",
  ],
  expandUrl: async (request) => {
    // Implement the logic to expand URL into metadata
  },
  getContent: async (request) => {
    // Implement the logic to retrieve the full asset
  },
});
```

**Note:** Intents must only be registered once. To learn more, see [Technical requirements](https://www.canva.dev/docs/apps/intents/#technical-requirements).

### Step 5: Implement URL expansion

The `expandUrl` method determines whether your app can handle a given URL and returns basic metadata about the content. This metadata is displayed to users as a preview before they choose to import the content.

```typescript
import type { ExpandUrlRequest, ExpandUrlResponse } from "@canva/intents/asset";

async function expandUrl(request: ExpandUrlRequest): Promise<ExpandUrlResponse> {
  const { url, requestConnection } = request;

  // Check if authentication is needed
  let { token } = await oauth.getAccessToken() ?? {};
  if (!token) {
    // Request user to connect to the platform
    await requestConnection();
    const response = await oauth.requestAuthorization();
    if (response.status === "aborted") {
      throw new Error("Authentication was aborted.");
    }
    ({ token } = await oauth.getAccessToken() ?? {});
  }

  try {
    // Extract the document ID from the URL
    const docId = extractDocumentId(url);

    // Fetch metadata from your platform
    const metadata = await fetchDocumentMetadata(docId, token);

    return {
      status: "completed",
      result: {
        ref: {
          type: "asset",
          id: docId,
          name: metadata.title,
          iconUrl: "https://example.com/icon.png",
          description: `Last modified: ${metadata.lastModified}`,
        },
      },
    };
  } catch (err) {
    console.error("Failed to resolve URL:", err);
    return { status: "not_found" };
  }
}
```

**Key points:**

* **URL parsing**: Extract identifiers from the URL to fetch content from your platform.
* **Metadata retrieval**: Fetch basic information about the content (title, description, icon).
* **Authentication**: Handle authentication if required to access the content.
* **Error handling**: Return `status: "not_found"` if the URL can't be expanded.

### Step 6: Implement content retrieval

The `getContent` method fetches the actual asset data that will be imported into the design. This method is called when the user chooses to import the content.

```typescript
import type { GetContentRequest, GetContentResponse } from "@canva/intents/asset";

async function getContent(request: GetContentRequest): Promise<GetContentResponse> {
  const { ref, requestConnection } = request;

  // Check if authentication is needed
  let { token } = await oauth.getAccessToken() ?? {};
  if (!token) {
    await requestConnection();
    const response = await oauth.requestAuthorization();
    if (response.status === "aborted") {
      throw new Error("Authentication was aborted.");
    }
    ({ token } = await oauth.getAccessToken() ?? {});
  }

  try {
    // Use the ref ID from expandUrl to identify the content
    const docId = ref.id;

    // Export the document from your platform
    const blob = await exportDocument(token, docId, "pdf");

    // Upload to a presigned URL or accessible location
    const presignedUrl = await uploadToAccessibleUrl(token, blob);

    return {
      type: "generic",
      name: ref.name,
      url: presignedUrl,
      mimeType: "application/pdf",
    };
  } catch (err) {
    console.error("Failed to get content:", err);
    throw err;
  }
}
```

**Key points:**

* **Content export**: Convert the content into a format Canva can import (image, video, PDF).
* **URL accessibility**: Provide a publicly accessible URL for Canva to download the content.
* **MIME type**: Specify the correct MIME type for the content.
* **Ref usage**: Use the `ref` object from `expandUrl` to identify the content.

### Step 7: Handle authentication

If your content requires authentication, handle the OAuth flow within both `expandUrl` and `getContent` methods.

**Authentication flow:**

1. Check if a valid access token exists.
2. If not, call `requestConnection()` to prompt the user to connect.
3. Call `oauth.requestAuthorization()` to complete the OAuth flow.
4. Store the token for subsequent requests.

```typescript
// Check for existing token
let { token } = await oauth.getAccessToken() ?? {};

if (!token) {
  // Request user to connect to the platform
  await requestConnection();

  // Perform OAuth authorization
  const response = await oauth.requestAuthorization();

  if (response.status === "aborted") {
    throw new Error("Authentication was aborted.");
  }

  // Get the new token
  ({ token } = await oauth.getAccessToken() ?? {});
}
```

**Note:** Currently, when the user doesn't have a valid auth token, you must invoke and wait for the completion of `await requestConnection()`. This ensures that users interact with the resource metadata (shown as a preview) before showing the authentication popup. In the future, this requirement will be removed, and you'll be able to call `await requestAuthorization()` directly.

## Testing the URL Expander intent

Testing the URL Expander intent works differently from other intents because users never discover and install your app from an explicit App Panel. Instead, the URL Expander activates when users paste URLs directly into Canva AI.

To test your draft app:

1. Navigate to your app through the [Your apps](https://www.canva.com/developers/apps) page.
2. Click **Preview** to open your app in a test environment.
3. To trigger your URL Expander:
   1. Click the search box and ensure Canva AI is selected.
   2. Paste a URL from your service that your app should recognize.
   3. Your app's `expandUrl` and `getContent` methods will be called automatically.
   4. If successful, the content will be imported into the design.

### Tips for testing

* Make sure you're testing with URLs that match the patterns your app registered.
* Check your browser's developer console for any errors during the expansion process.
* Test both authenticated and unauthenticated scenarios if your app requires user login.
* Verify that error messages display correctly when URLs can't be processed.

**Note:** Unlike traditional apps that appear in the apps panel, URL Expander apps work behind the scenes. Users won't see your app's interface directly—instead, they'll see the content from your service being imported seamlessly into their design.
