Source: https://www.canva.dev/docs/apps/intents/design-editor/implementation-guide/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Design Editor intent implementation guide

Create specialized editing tools within Canva.

This guide helps you implement the [Design Editor intent](https://www.canva.dev/docs/apps/intents/design-editor/) to create specialized editing tools that appear alongside the Canva design surface.

## Creating a Design Editor

### Step 1: Enable the intent

Before an intent can be implemented, it must be enabled. Enabling an intent informs Canva of when and where the app should be invoked throughout the user experience.

You can configure intents for your app with either the Developer Portal or the Canva CLI:

<Tabs storageKey="configuration">
  <Tab name="Developer Portal">
    1. Navigate to an app via the [Your apps](https://www.canva.com/developers/apps) page.
    2. On the **Intents** page, find the "Available intents" section.
    3. For the "Design Editor" intent, click **Set up**.
    4. In the "Implement in your code" dialog that appears, click **Done**. The following sections in this guide will walk you through implementing the intent in your code.
  </Tab>

  <Tab name="Canva CLI">
    1. Set up your app to use the Canva CLI to manage settings via the [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/#manage-configuration-using-the-canva-cli) file.
    2. Set the `intent.design_editor` property to be enrolled. For more information, see [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/#intent-optional).

       For example, the following enables the Design Editor intent.

       ```json
       {
         "intent": {
           "design_editor": {
             "enrolled": true
           }
         }
       }
       ```
  </Tab>
</Tabs>

### Step 2: Register the intent

Before an intent can be implemented, it must be registered. Registering the Design Editor intent establishes how your app will render its UI within the Canva editor.

To register the intent, call the `prepareDesignEditor` method as soon as the app loads:

```ts
import { prepareDesignEditor } from "@canva/intents/design";

prepareDesignEditor({
  render: async () => {
    // TODO: Implement the logic to render your app's UI
  },
});
```

**Note:** Intents must only be registered once. To learn more, see [Technical requirements](https://www.canva.dev/docs/apps/intents/#technical-requirements).

### Step 3: Render the app's UI

When a user opens your app within the Canva editor, the intent will use the `render` method to display your app's interface. This method should set up your UI components and make them ready for user interaction.

```tsx
import { createRoot } from "react-dom/client";
import { AppUiProvider, Rows, Text } from "@canva/app-ui-kit";
import { prepareDesignEditor } from "@canva/intents/design";
import "@canva/app-ui-kit/styles.css";
import * as styles from "styles/components.css";

prepareDesignEditor({
  render: async () => {
    const rootElement = document.getElementById("root");
    const rootElementExists = rootElement instanceof Element;

    if (!rootElementExists) {
      throw new Error("Unable to find element with id of 'root'");
    }

    const root = createRoot(rootElement);

    root.render(
      <AppUiProvider>
        <DesignEditor />
      </AppUiProvider>
    );
  },
});

function DesignEditor() {
  return (
    <div className={styles.container}>
      <Rows spacing="2u">
        <Text>Hello world.</Text>
      </Rows>
    </div>
  );
}
```

## Initiating OAuth inside intents

If your app requires OAuth with a third-party identity provider, initiate the OAuth flow from inside the intent's render lifecycle so it runs within the app iframe.

For implementation guidance, see [Initiating OAuth inside intents](https://www.canva.dev/docs/apps/authenticating-users/oauth/#initiating-oauth-inside-intents).

## Next steps

After setting up the Design Editor intent, use the available APIs, such as the [Design Editing API](https://www.canva.dev/docs/apps/design-editing/), to interact with the user's design.
