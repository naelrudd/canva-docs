Source: https://www.canva.dev/docs/apps/examples/app-embed-elements/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# App embed elements

Create embed elements inside app elements.

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
   npm run start app_embed_elements
   ```

6. Click the **Preview URL** link shown in the terminal to open the example in the Canva editor.

## Example app source code

<Tabs>
  <Tab name="app.tsx">
    ```typescript
    // For usage information, see the README.md file.
    import { type AppElementOptions, initAppElement } from "@canva/design";
    import {
      Button,
      FormField,
      NumberInput,
      Rows,
      Text,
      TextInput,
    } from "@canva/app-ui-kit";
    import * as styles from "styles/components.css";
    import { useEffect, useState } from "react";

    // Data structure that defines the properties of our app element
    // This will be persisted when the user saves their design
    type AppElementData = {
      url: string;
      width: number;
      height: number;
    };

    // The state of the user interface. In this example,
    // we have data representing AppElementData, but it could be different.
    // We also store an update function that can be used to update the app element.
    type AppElementChangeEvent = {
      data: AppElementData;
      update?: (opts: AppElementOptions<AppElementData>) => Promise<void>;
    };

    const initialState: AppElementChangeEvent = {
      data: {
        url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        width: 640,
        height: 360,
      },
    };

    // Initialize the app element client - this handles communication with Canva's design APIs
    // The render function defines how our data becomes design elements when added to the canvas
    const appElementClient = initAppElement<AppElementData>({
      render: (data) => {
        // Return an embed element with our app element data
        // The top/left positioning is handled by Canva when the user places the element
        return [{ type: "embed", ...data, top: 0, left: 0 }];
      },
    });

    export const App = () => {
      const [state, setState] = useState<AppElementChangeEvent>(initialState);
      const {
        data: { url, width, height },
      } = state;
      const disabled = url?.trim().length < 1 || !width || !height;

      useEffect(() => {
        // Register to listen for app element changes - this occurs when the user
        // selects an existing app element in the design to edit it
        appElementClient.registerOnElementChange((appElement) => {
          setState(
            appElement
              ? {
                  data: appElement.data,
                  update: appElement.update,
                }
              : initialState,
          );
        });
      }, []);

      return (
        <div className={styles.scrollContainer}>
          <Rows spacing="2u">
            <Text>
              This example demonstrates how apps can create embed elements inside
              app elements. This makes the element re-editable and lets apps control
              additional properties, such as the width and height.
            </Text>
            <FormField
              label="URL"
              value={url}
              control={(props) => (
                <TextInput
                  {...props}
                  onChange={(value) => {
                    setState((prevState) => {
                      return {
                        ...prevState,
                        data: {
                          ...prevState.data,
                          url: value,
                        },
                      };
                    });
                  }}
                />
              )}
            />
            <FormField
              label="Width"
              value={width}
              control={(props) => (
                <NumberInput
                  {...props}
                  min={1}
                  onChange={(value) => {
                    setState((prevState) => {
                      return {
                        ...prevState,
                        data: {
                          ...prevState.data,
                          width: Number(value || 0),
                        },
                      };
                    });
                  }}
                />
              )}
            />
            <FormField
              label="Height"
              value={height}
              control={(props) => (
                <NumberInput
                  {...props}
                  min={1}
                  onChange={(value) => {
                    setState((prevState) => {
                      return {
                        ...prevState,
                        data: {
                          ...prevState.data,
                          height: Number(value || 0),
                        },
                      };
                    });
                  }}
                />
              )}
            />
            <Button
              variant="primary"
              stretch
              onClick={() => {
                if (state.update) {
                  // Update existing app element when editing
                  state.update({ data: state.data });
                } else {
                  // Add new app element to the design
                  appElementClient.addElement({ data: state.data });
                }
              }}
              disabled={disabled}
            >
              {`${state.update ? "Update" : "Add"} element`}
            </Button>
          </Rows>
        </div>
      );
    };
    ```
  </Tab>

  <Tab name="index.tsx">
    ```typescript
    // For usage information, see the README.md file.
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

    // Hot Module Replacement for development (automatically reloads the app when changes are made)
    if (module.hot) {
      module.hot.accept("./app", render);
    }
    ```
  </Tab>

  <Tab name="README.md">
    ```markdown
    # App embed elements

    Demonstrates how to create embed elements inside app elements, making embeds re-editable with customizable properties like URL, width, and height. Shows how to wrap embed functionality in an app element for enhanced control.

    For API reference docs and instructions on running this example, see: https://www.canva.dev/docs/apps/examples/app-embed-elements/.

    Related examples: See design_elements/embed_elements for direct embed insertion, or app_video_elements for video-specific app elements.

    NOTE: This example differs from what is expected for public apps to pass a Canva review:

    - Content is hardcoded for demonstration purposes only. Production apps should provide user input interfaces for URL entry and dynamic content loading
    - Input validation and sanitization is simplified for demonstration. Production apps must implement comprehensive URL validation and error handling for invalid embed URLs
    - Error handling is simplified for demonstration. Production apps must implement comprehensive error handling with clear user feedback and graceful failure modes
    - Internationalization is not implemented. Production apps must support multiple languages using the `@canva/app-i18n-kit` package to pass Canva review requirements
    - The code structure is simplified: Production apps using [intents](https://www.canva.dev/docs/apps/intents/) are recommended to call the prepareDesignEditor function from src/intents/design_editor/index.tsx
    ```
  </Tab>
</Tabs>

## API reference

* [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/)
* [`initAppElement`](https://www.canva.dev/docs/apps/api/latest/design-init-app-element/)
* [`prepareDesignEditor`](https://www.canva.dev/docs/apps/api/latest/intents-design-prepare-design-editor/)

## Need help?

* Join our [Community Forum](https://community.canva.dev/)
* Report issues with this example on [GitHub](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/issues)
