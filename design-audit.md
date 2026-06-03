Source: https://www.canva.dev/docs/apps/examples/design-audit/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Design audit

Audit design elements for positioning issues and automatically fix elements that are too close to page edges.

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
   npm run start design_audit
   ```

6. Click the **Preview URL** link shown in the terminal to open the example in the Canva editor.

## Example app source code

<Tabs>
  <Tab name="app.tsx">
    ```typescript
    // For usage information, see the README.md file.
    import { Alert, Button, Rows, Text } from "@canva/app-ui-kit";
    import { openDesign, type DesignEditing } from "@canva/design";
    import { useState } from "react";
    import * as styles from "styles/components.css";

    type FixResult = {
      totalElementsFixed: number; // Total number of elements that were repositioned
      totalPagesModified: number; // Total number of pages that had at least one element modified
    };

    type AppState = {
      isLoading: boolean; // Whether we're currently processing the design
      lastFixResult?: FixResult; // Results from the last fix operation, undefined if never run
      errorMessage?: string; // Error message from the last operation, undefined if no error
    };

    const SAFE_DISTANCE = 100; // Minimum safe distance from page edges in pixels

    const initialState: AppState = {
      isLoading: false,
    };

    export const App = () => {
      const [state, setState] = useState<AppState>(initialState);
      const checkAndFixElement = (element: DesignEditing.AbsoluteElement, pageDimensions: { width: number; height: number } | undefined): boolean => {
        if (element.type === "unsupported") return false;
        if (!pageDimensions) return false;
        const distanceFromRight = pageDimensions.width - (element.left + element.width);
        const distanceFromBottom = pageDimensions.height - (element.top + element.height);
        let wasFixed = false;
        if (element.top < SAFE_DISTANCE) { element.top = SAFE_DISTANCE; wasFixed = true; }
        else if (distanceFromBottom < SAFE_DISTANCE) { element.top = pageDimensions.height - element.height - SAFE_DISTANCE; wasFixed = true; }
        if (element.left < SAFE_DISTANCE) { element.left = SAFE_DISTANCE; wasFixed = true; }
        else if (distanceFromRight < SAFE_DISTANCE) { element.left = pageDimensions.width - element.width - SAFE_DISTANCE; wasFixed = true; }
        return wasFixed;
      };

      const fixPositioningIssues = async () => {
        setState((prev) => ({ ...prev, isLoading: true, errorMessage: undefined }));
        try {
          let totalElementsFixed = 0;
          let totalPagesModified = 0;
          await openDesign({ type: "all_pages" }, async (session) => {
            for (const pageRef of session.pageRefs.toArray()) {
              if (pageRef.type !== "absolute" || pageRef.locked) continue;
              await session.helpers.openPage(pageRef, async (pageResult) => {
                let elementsFixedOnPage = 0;
                pageResult.page.elements.forEach((element) => {
                  if (element.locked) return;
                  if (checkAndFixElement(element, pageResult.page.dimensions)) elementsFixedOnPage++;
                });
                totalElementsFixed += elementsFixedOnPage;
                if (elementsFixedOnPage > 0) totalPagesModified++;
              });
            }
            await session.sync();
          });
          setState((prev) => ({ ...prev, isLoading: false, lastFixResult: { totalElementsFixed, totalPagesModified } }));
        } catch (error) {
          const errorMessage = error instanceof Error ? error.message : "An unexpected error occurred";
          setState((prev) => ({ ...prev, isLoading: false, errorMessage }));
        }
      };

      return (
        <div className={styles.scrollContainer}>
          <Rows spacing="2u">
            <Text>This app automatically fixes elements that are positioned too close to the edges of pages.</Text>
            <Button variant="primary" onClick={fixPositioningIssues} disabled={state.isLoading}>Fix element positioning</Button>
            {state.lastFixResult && (<Alert tone="positive">Fixed {state.lastFixResult.totalElementsFixed} element(s) across {state.lastFixResult.totalPagesModified} pages.</Alert>)}
            {state.errorMessage && (<Alert tone="critical">{state.errorMessage}</Alert>)}
          </Rows>
        </div>
      );
    };
    ```
  </Tab>

  <Tab name="index.tsx">
    ```typescript
    import { AppUiProvider } from "@canva/app-ui-kit";
    import { createRoot } from "react-dom/client";
    import { App } from "./app";
    import "@canva/app-ui-kit/styles.css";

    function render() {
      const root = createRoot(document.getElementById("root") as Element);
      root.render(<AppUiProvider><App /></AppUiProvider>);
    }
    render();
    if (module.hot) { module.hot.accept("./app", render); }
    ```
  </Tab>

  <Tab name="README.md">
    ```markdown
    # Design audit
    Demonstrates how to audit design elements for positioning issues and automatically fix elements that are positioned too close to page edges. Shows how to use the Design Editing API to iterate over every element on all pages of the design.
    For API reference docs and instructions on running this example, see: https://www.canva.dev/docs/apps/examples/design-audit/.
    Related examples: See design_interaction/design_editing for other complex design editing workflows using the Design Editing API.
    NOTE: This example differs from what is expected for public apps to pass a Canva review:
    - Uses the preview Design Editing API "all_pages" design context. Production apps must not use preview APIs
    - Element positioning logic is simplified for demonstration. Production apps should implement comprehensive positioning validation with support for different design types and element constraints
    - Error handling is simplified for demonstration. Production apps must implement comprehensive error handling with clear user feedback and graceful failure modes
    - Internationalization is not implemented. Production apps must support multiple languages using the `@canva/app-i18n-kit` package to pass Canva review requirements
    - The code structure is simplified: Production apps using [intents](https://www.canva.dev/docs/apps/intents/) are recommended to call the prepareDesignEditor function from src/intents/design_editor/index.tsx
    ```
  </Tab>
</Tabs>

## API reference

* [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/)
* [`openDesign`](https://www.canva.dev/docs/apps/api/preview/design-open-design/)

## Need help?

* Join our [Community Forum](https://community.canva.dev/)
* Report issues with this example on [GitHub](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/issues)
