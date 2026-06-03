Source: https://www.canva.dev/docs/apps/examples/image-editing-overlay/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Image editing overlay

Create custom image editing overlays and filters.

## Running this example

To run this example locally:

1. If you haven't already, create a new app in the [Developer Portal](https://www.canva.com/developers/apps). For more information, refer to our [Quickstart guide](https://www.canva.dev/docs/apps/quickstart/).

2. In your app's configuration on the [Developer Portal](https://www.canva.com/developers/apps), ensure the "Development URL" is set to `http://localhost:8080`.

3. Clone the starter kit:
   ```shell
   git clone https://github.com/canva-sdks/canva-apps-sdk-starter-kit.git
   cd canva-apps-sdk-starter-kit
   ```

4. Install dependencies:
   ```shell
   npm install
   ```

5. Run the example:
   ```shell
   npm run start image_editing_overlay
   ```

6. Click the **Preview URL** link shown in the terminal to open the example in the Canva editor.

## Example app source code

<Tabs>
  <Tab name="app.tsx">
    ```typescript
    import { appProcess } from "@canva/platform";
    import { ObjectPanel } from "./object_panel";
    import { SelectedImageOverlay } from "./overlay";

    export const App = () => {
      const context = appProcess.current.getInfo();
      if (context.surface === "object_panel") return <ObjectPanel />;
      if (context.surface === "selected_image_overlay") return <SelectedImageOverlay />;
      throw new Error(`Invalid surface: ${context.surface}`);
    };
    ```
  </Tab>

  <Tab name="index.tsx">
    ```typescript
    import { AppUiProvider } from "@canva/app-ui-kit";
    import { createRoot } from "react-dom/client";
    import "@canva/app-ui-kit/styles.css";
    import { App } from "./app";
    import type { DesignEditorIntent } from "@canva/intents/design";
    import { prepareDesignEditor } from "@canva/intents/design";

    async function render() {
      const root = createRoot(document.getElementById("root") as Element);
      root.render(<AppUiProvider><App /></AppUiProvider>);
    }
    const designEditor: DesignEditorIntent = { render };
    prepareDesignEditor(designEditor);
    if (module.hot) module.hot.accept("./app", render);
    ```
  </Tab>

  <Tab name="object_panel.tsx">
    ```typescript
    import { Alert, Button, Rows, Text, Title } from "@canva/app-ui-kit";
    import { appProcess } from "@canva/platform";
    import * as React from "react";
    import * as styles from "styles/components.css";
    import { useFeatureSupport, useOverlay } from "@canva/app-hooks";

    export const ObjectPanel = () => {
      const overlay = useOverlay("image_selection");
      const isSupported = useFeatureSupport();
      const [isImageReady, setIsImageReady] = React.useState(false);

      React.useEffect(() => {
        appProcess.registerOnMessage(async (sender, message) => {
          if (typeof message === "object" && message != null && "isImageReady" in message) {
            setIsImageReady(Boolean(message.isImageReady));
          }
        });
      }, []);

      if (!isSupported(overlay.open)) {
        return <div className={styles.scrollContainer}><Alert tone="warn">Image editing overlay functionality is not supported in the current design type.</Alert></div>;
      }

      if (overlay.isOpen) {
        return (
          <div className={styles.scrollContainer}>
            <Rows spacing="3u">
              <Title size="small">Image editing</Title>
              <Text>Apply effects to your image with real-time preview.</Text>
              <Rows spacing="1.5u">
                <Button variant="secondary" disabled={!isImageReady} onClick={() => appProcess.broadcastMessage({ action: "invert" })} stretch>Invert colors</Button>
                <Button variant="secondary" disabled={!isImageReady} onClick={() => appProcess.broadcastMessage({ action: "blur" })} stretch>Add blur</Button>
                <Button variant="secondary" disabled={!isImageReady} onClick={() => appProcess.broadcastMessage({ action: "reset" })} stretch>Reset changes</Button>
              </Rows>
              <Rows spacing="1.5u">
                <Button variant="primary" disabled={!isImageReady} onClick={() => overlay.close({ reason: "completed" })} stretch>Save and close</Button>
                <Button variant="secondary" disabled={!isImageReady} onClick={() => overlay.close({ reason: "aborted" })} stretch>Close without saving</Button>
              </Rows>
            </Rows>
          </div>
        );
      }

      return (
        <div className={styles.scrollContainer}>
          <Rows spacing="3u">
            <Title size="small">Image editing overlay</Title>
            <Text>Select a raster image in your design to start editing with real-time preview.</Text>
            <Button variant="primary" disabled={!overlay.canOpen} onClick={() => overlay.open()} stretch>Edit image</Button>
            {!overlay.canOpen && <Alert tone="info">Select a single raster image in your design to enable image editing. Vector images and multiple selections are not supported.</Alert>}
          </Rows>
        </div>
      );
    };
    ```
  </Tab>
</Tabs>

## API reference

* [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/)
* [`appProcess.broadcastMessage`](https://www.canva.dev/docs/apps/api/latest/platform-app-process-broadcast-message/)
* [`prepareDesignEditor`](https://www.canva.dev/docs/apps/api/latest/intents-design-prepare-design-editor/)
* [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/)

## Need help?

* Join our [Community Forum](https://community.canva.dev/)
* Report issues with this example on [GitHub](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/issues)
