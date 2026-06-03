Source: https://www.canva.dev/docs/apps/examples/app-text-elements/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# App text elements

Create text elements inside app elements.

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
   npm run start app_text_elements
   ```

6. Click the **Preview URL** link shown in the terminal to open the example in the Canva editor.

## Example app source code

<Tabs>
  <Tab name="app.tsx">
    ```typescript
    // For usage information, see the README.md file.
    import {
      Button,
      ColorSelector,
      FormField,
      NumberInput,
      RadioGroup,
      Rows,
      Select,
      Text,
      TextInput,
      Title,
    } from "@canva/app-ui-kit";
    import type {
      AppElementOptions,
      FontWeight,
      TextAttributes,
    } from "@canva/design";
    import { initAppElement } from "@canva/design";
    import { useEffect, useState } from "react";
    import * as styles from "styles/components.css";

    type AppElementData = {
      text: string;
      color: string;
      fontWeight: FontWeight;
      fontStyle: TextAttributes["fontStyle"];
      decoration: TextAttributes["decoration"];
      textAlign: TextAttributes["textAlign"];
      width: number;
      rotation: number;
      useCustomWidth: boolean;
    };

    type AppElementChangeEvent = {
      data: AppElementData;
      update?: (opts: AppElementOptions<AppElementData>) => Promise<void>;
    };

    const initialState: AppElementChangeEvent = {
      data: {
        text: "Hello world",
        color: "#ff0099",
        fontWeight: "normal",
        fontStyle: "normal",
        decoration: "none",
        textAlign: "start",
        width: 250,
        rotation: 0,
        useCustomWidth: false,
      },
    };

    // Initialize the app element client - this handles communication between the app and Canva
    // The render function defines how the app element appears in the user's design
    const appElementClient = initAppElement<AppElementData>({
      render: (data) => {
        return [
          {
            type: "text", // Creates a text element within the app element
            top: 0,
            left: 0,
            ...data,
            width: data.useCustomWidth ? data.width : undefined,
            children: [data.text], // The actual text content to display
          },
        ];
      },
    });

    export const App = () => {
      const [state, setState] = useState<AppElementChangeEvent>(initialState);

      const {
        data: {
          text,
          color,
          fontWeight,
          fontStyle,
          decoration,
          textAlign,
          width,
          rotation,
          useCustomWidth,
        },
      } = state;

      const disabled = text.trim().length < 1 || color.trim().length < 1;

      useEffect(() => {
        // Register handler for app element changes - this allows editing existing elements
        // When a user selects an existing app element, we update the UI controls to match its properties
        appElementClient.registerOnElementChange((appElement) => {
          setState(
            appElement
              ? {
                  data: appElement.data,
                  update: appElement.update, // Function to update the existing element
                }
              : initialState, // Reset to initial state when no element is selected
          );
        });
      }, []);

      return (
        <div className={styles.scrollContainer}>
          <Rows spacing="2u">
            <Text>
              This example demonstrates how apps can create text elements inside app
              elements. Using an app element makes the text element re-editable and
              lets apps control additional properties, such as the width and height.
            </Text>
            <FormField
              label="Text"
              value={text}
              control={(props) => (
                <TextInput
                  {...props}
                  onChange={(value) => {
                    setState((prevState) => {
                      return {
                        ...prevState,
                        data: {
                          ...prevState.data,
                          text: value,
                        },
                      };
                    });
                  }}
                />
              )}
            />
            <Title size="small">Custom options</Title>
            <FormField
              label="Color"
              control={() => (
                <ColorSelector
                  color={color}
                  onChange={(value) => {
                    setState((prevState) => {
                      return {
                        ...prevState,
                        data: {
                          ...prevState.data,
                          color: value,
                        },
                      };
                    });
                  }}
                />
              )}
            />
            <FormField
              label="Font style"
              value={fontStyle}
              control={(props) => (
                <Select<TextAttributes["fontStyle"]>
                  {...props}
                  options={[
                    { value: "normal", label: "Normal" },
                    { value: "italic", label: "Italic" },
                  ]}
                  onChange={(value) => {
                    setState((prevState) => {
                      return {
                        ...prevState,
                        data: {
                          ...prevState.data,
                          fontStyle: value,
                        },
                      };
                    });
                  }}
                  stretch
                />
              )}
            />
            <FormField
              label="Font weight"
              value={fontWeight}
              control={(props) => (
                <Select<FontWeight>
                  {...props}
                  options={[
                    { value: "normal", label: "Normal" },
                    { value: "thin", label: "Thin" },
                    { value: "extralight", label: "Extra light" },
                    { value: "light", label: "Light" },
                    { value: "medium", label: "Medium" },
                    { value: "semibold", label: "Semibold" },
                    { value: "bold", label: "Bold" },
                    { value: "heavy", label: "Heavy" },
                  ]}
                  onChange={(value) => {
                    setState((prevState) => {
                      return {
                        ...prevState,
                        data: {
                          ...prevState.data,
                          fontWeight: value,
                        },
                      };
                    });
                  }}
                  stretch
                />
              )}
            />
            <FormField
              label="Decoration"
              value={decoration}
              control={(props) => (
                <Select<TextAttributes["decoration"]>
                  {...props}
                  options={[
                    { value: "none", label: "None" },
                    { value: "underline", label: "Underline" },
                  ]}
                  onChange={(value) => {
                    setState((prevState) => {
                      return {
                        ...prevState,
                        data: {
                          ...prevState.data,
                          decoration: value,
                        },
                      };
                    });
                  }}
                  stretch
                />
              )}
            />
            <FormField
              label="Text align"
              value={textAlign}
              control={(props) => (
                <Select<TextAttributes["textAlign"]>
                  {...props}
                  options={[
                    { value: "start", label: "Start" },
                    { value: "center", label: "Center" },
                    { value: "end", label: "End" },
                  ]}
                  onChange={(value) => {
                    setState((prevState) => {
                      return {
                        ...prevState,
                        data: {
                          ...prevState.data,
                          textAlign: value,
                        },
                      };
                    });
                  }}
                  stretch
                />
              )}
            />
            <FormField
              label="Width"
              value={useCustomWidth}
              control={(props) => (
                <RadioGroup
                  {...props}
                  options={[
                    {
                      label: "Fit to content",
                      value: false,
                    },
                    {
                      label: "Use custom width",
                      value: true,
                    },
                  ]}
                  onChange={(value) => {
                    setState((prevState) => {
                      return {
                        ...prevState,
                        data: {
                          ...prevState.data,
                          useCustomWidth: value,
                        },
                      };
                    });
                  }}
                />
              )}
            />
            {useCustomWidth ? (
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
                            width: Number(value || 1),
                          },
                        };
                      });
                    }}
                  />
                )}
              />
            ) : undefined}
            <FormField
              label="Rotation"
              value={rotation}
              control={(props) => (
                <NumberInput
                  {...props}
                  min={-180}
                  max={180}
                  onChange={(value) => {
                    setState((prevState) => {
                      return {
                        ...prevState,
                        data: {
                          ...prevState.data,
                          rotation: Number(value || 0),
                        },
                      };
                    });
                  }}
                />
              )}
            />
            <Button
              variant="primary"
              onClick={() => {
                if (state.update) {
                  // Update existing app element with new data
                  state.update({ data: state.data });
                } else {
                  // Create new app element and add it to the design
                  appElementClient.addElement({ data: state.data });
                }
              }}
              disabled={disabled}
              stretch
            >
              {`${state.update ? "Update" : "Add"} text`}
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
    # App text elements

    Demonstrates how to create text elements inside app elements with comprehensive styling controls including color, font weight, style, decoration, alignment, and dimensions. Shows text formatting within re-editable app elements.

    For API reference docs and instructions on running this example, see: https://www.canva.dev/docs/apps/examples/app-text-elements/.

    Related examples: See `design_elements/text_elements` for direct text insertion, or `assets_and_media/fonts` for advanced font selection patterns.

    NOTE: This example differs from what's expected for public apps to pass a Canva review:

    - Text content and styling options are hardcoded for demonstration purposes only. Production apps should provide user input interfaces or dynamic content loading and implement comprehensive text editing interfaces with proper font selection.
    - Internationalization isn't implemented. Production apps must support multiple languages using the `@canva/app-i18n-kit` package to pass Canva review requirements.
    - Accessibility features are simplified for demonstration. Production apps must meet WCAG 2.0 AA standards with proper keyboard navigation and ARIA labels.
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
