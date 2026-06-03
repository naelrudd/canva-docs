Source: https://www.canva.dev/docs/apps/examples/feature-support/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Feature support

Feature detection and conditional functionality based on platform support.

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
   npm run start feature_support
   \\\

6. Click the **Preview URL** link shown in the terminal to open the example in the Canva editor.

## Example app source code

<Tabs>
  <Tab name="app.tsx">
    \\\	ypescript
    import { addElementAtPoint, addPage } from "@canva/design";
    import { useState } from "react";
    import * as styles from "styles/components.css";
    import { useFeatureSupport } from "@canva/app-hooks";
    import { HomePage } from "./home";
    import { InteractionPage } from "./interaction";

    type AppPage = "home" | "interaction";

    export const App = () => {
      const [appPage, setAppPage] = useState<AppPage>("home");
      const isSupported = useFeatureSupport();
      const isInteractionSupported = isSupported(addElementAtPoint, addPage);

      const renderPage = (page: AppPage) => {
        switch (page) {
          case "home":
            return <HomePage enterInteractionPage={() => setAppPage("interaction")} />;
          case "interaction":
            return <InteractionPage goBack={() => setAppPage("home")} isInteractionSupported={isInteractionSupported} />;
          default:
            return;
        }
      };

      return <div className={styles.scrollContainer}>{renderPage(appPage)}</div>;
    };
    \\\
  </Tab>

  <Tab name="home.tsx">
    \\\	ypescript
    import { Button, Rows, Text, Title } from "@canva/app-ui-kit";

    type HomePageProps = { enterInteractionPage: () => void };

    export const HomePage = (props: HomePageProps) => {
      return (
        <Rows spacing="1.5u">
          <Title>Home page</Title>
          <Text>This example app demonstrates how to toggle interactive UI based on the currently available features.</Text>
          <Button variant="primary" onClick={props.enterInteractionPage}>Enter interactions page</Button>
        </Rows>
      );
    };
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
      root.render(<AppUiProvider><App /></AppUiProvider>);
    }

    const designEditor: DesignEditorIntent = { render };
    prepareDesignEditor(designEditor);

    if (module.hot) {
      module.hot.accept("./app", render);
    }
    \\\
  </Tab>

  <Tab name="interaction.tsx">
    \\\	ypescript
    import { Alert, Button, Rows } from "@canva/app-ui-kit";
    import { addElementAtPoint, addPage } from "@canva/design";

    type InteractionPageProps = { goBack: () => void; isInteractionSupported: boolean };

    export const InteractionPage = (props: InteractionPageProps) => {
      return (
        <Rows spacing="1.5u">
          {!props.isInteractionSupported && <UnsupportedAlert />}
          <Button variant="primary" onClick={props.goBack}>Back</Button>
          <Button disabled={!props.isInteractionSupported} variant="secondary" onClick={() => addElementAtPoint({ type: "shape", ...shape })}>Add a shape at a point</Button>
          <Button disabled={!props.isInteractionSupported} variant="secondary" onClick={() => addElementAtPoint({ type: "group", children: [{ type: "shape", ...shape, left: 0, top: 0, width: 200, height: "auto" }, { type: "embed", url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ", left: 300, top: 100, width: 200, height: "auto" }] })}>Add a group at a point</Button>
          <Button disabled={!props.isInteractionSupported} variant="secondary" onClick={() => addPage()}>Add a new page</Button>
        </Rows>
      );
    };

    const shape = {
      paths: [{ d: "M 0 0 H 100 V 100 H 0 L 0 0", fill: { dropTarget: false, color: "#ff0099" } }],
      viewBox: { width: 100, height: 100, top: 0, left: 0 },
    };

    const UnsupportedAlert = () => (
      <Alert tone="warn" title="Shapes, Groups and Pages can't be added to Docs.">Try using this app in a different design type.</Alert>
    );
    \\\
  </Tab>

  <Tab name="README.md">
    \\\markdown
    # Feature support

    Demonstrates how to detect and handle feature availability across different design types and contexts. Shows dynamic feature detection, graceful degradation, and context-aware UI rendering using the Canva Apps SDK's feature support system.

    For API reference docs and instructions on running this example, see: <https://www.canva.dev/docs/apps/examples/feature-support/>.

    Related examples: This pattern should be used across all apps to ensure proper functionality across different design contexts.

    NOTE: This example differs from what is expected for public apps to pass a Canva review:
    - Feature detection patterns are simplified for demonstration purposes only. Production apps must implement feature detection for all functionality that depends on design context or user permissions
    - Error handling is simplified for demonstration. Production apps must implement comprehensive error handling with clear user feedback and graceful failure modes
    - Internationalization is not implemented. Production apps must support multiple languages using the \@canva/app-i18n-kit\ package to pass Canva review requirements
    - The code structure is simplified: Production apps using [intents](https://www.canva.dev/docs/apps/intents/) are recommended to call the prepareDesignEditor function from src/intents/design_editor/index.tsx
    \\\
  </Tab>
</Tabs>

## API reference

* [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/)
* [\ddElementAtPoint\](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/)
* [\ddPage\](https://www.canva.dev/docs/apps/api/latest/design-add-page/)
* [\prepareDesignEditor\](https://www.canva.dev/docs/apps/api/latest/intents-design-prepare-design-editor/)

## Need help?

* Join our [Community Forum](https://community.canva.dev/)
* Report issues with this example on [GitHub](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/issues)

