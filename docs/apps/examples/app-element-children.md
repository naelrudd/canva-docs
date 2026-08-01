Source: https://www.canva.dev/docs/apps/examples/app-element-children/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# App element children

Build composite app elements from multiple child elements.

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
   npm run start app_element_children
   ```

6. Click the **Preview URL** link shown in the terminal to open the example in the Canva editor.

## Example app source code

<Tabs>
  <Tab name="app.tsx">
    ```typescript
    // For usage information, see the README.md file.
    import {
      Button,
      FormField,
      NumberInput,
      Rows,
      Text,
      Title,
    } from "@canva/app-ui-kit";
    import type {
      AppElementRendererOutput,
      ShapeElementAtPoint,
      AppElementOptions,
    } from "@canva/design";
    import { initAppElement } from "@canva/design";
    import { useEffect, useState } from "react";
    import * as styles from "styles/components.css";

    // The data that will be attached to the app element
    type AppElementData = {
      rows: number;
      columns: number;
      width: number;
      height: number;
      spacing: number;
      rotation: number;
    };

    // The state of the user interface. In this example,
    // we have data representing AppElementData, but it *could* be different.
    // We also store an update function that can be used to update the app element.
    type AppElementChangeEvent = {
      data: AppElementData;
      update?: (opts: AppElementOptions<AppElementData>) => Promise<void>;
    };

    // The default values for the UI components.
    const initialState: AppElementChangeEvent = {
      data: {
        rows: 3,
        columns: 3,
        width: 100,
        height: 100,
        spacing: 25,
        rotation: 0,
      },
    };

    // Initialize the app element client with custom render logic
    // App elements are Canva design objects that can contain multiple child elements
    const appElementClient = initAppElement<AppElementData>({
      // This render callback executes when Canva needs to display the app element
      // It transforms our app data into actual design elements positioned on the canvas
      render: (data) => {
        const elements: AppElementRendererOutput = [];

        // Generate a grid of shape elements based on rows and columns
        // Each shape is positioned using absolute coordinates relative to the app element
        for (let row = 0; row < data.rows; row++) {
          for (let column = 0; column < data.columns; column++) {
            const { width, height, spacing, rotation } = data;
            // Calculate position offsets to create a non-overlapping grid layout
            const top = row * (height + spacing);
            const left = column * (width + spacing);
            const element = createSquareShapeElement({
              width,
              height,
              top,
              left,
              rotation,
            });
            elements.push(element);
          }
        }
        return elements;
      },
    });

    export const App = () => {
      const [state, setState] = useState<AppElementChangeEvent>(initialState);
      const {
        data: { width, height, rows, columns, spacing, rotation },
      } = state;
      const disabled = width < 1 || height < 1 || rows < 1 || columns < 1;

      // Register a change listener to sync UI state with selected app elements
      // This is called when the user selects an app element in Canva or when element data changes
      useEffect(() => {
        appElementClient.registerOnElementChange((appElement) => {
          // Update local state to reflect the current app element's data
          // If no element is selected, reset to default values
          setState(
            appElement
              ? { data: appElement.data, update: appElement.update }
              : initialState,
          );
        });
      }, []);

      return (
        <div className={styles.scrollContainer}>
          <Rows spacing="2u">
            <Text>
              This example demonstrates how app elements can be made up of one or
              more elements, and how those elements can be positioned relatively to
              one another.
            </Text>
            <Title size="small">Grid</Title>
            <FormField
              label="Rows"
              value={rows}
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
                          rows: Number(value || 0),
                        },
                      };
                    });
                  }}
                />
              )}
            />
            <FormField
              label="Columns"
              value={columns}
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
                          columns: Number(value || 0),
                        },
                      };
                    });
                  }}
                />
              )}
            />
            <FormField
              label="Spacing"
              value={spacing}
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
                          spacing: Number(value || 0),
                        },
                      };
                    });
                  }}
                />
              )}
            />
            <Title size="small">Squares</Title>
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
              stretch
              onClick={() => {
                // Add new app element or update existing one with current data
                // This triggers the render callback to create the visual elements on canvas
                if (state.update) {
                  // Update existing app element with new data
                  state.update({ data: state.data });
                } else {
                  // Create new app element and add it to the design
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

    // Creates a square shape element using SVG path data
    // Shape elements are one of the core design element types in Canva
    const createSquareShapeElement = ({
      width,
      height,
      top,
      left,
      rotation,
    }: {
      width: number;
      height: number;
      top: number;
      left: number;
      rotation: number;
    }): ShapeElementAtPoint => {
      return {
        type: "shape",
        // SVG path defining a rectangle shape (Move to origin, Horizontal line, Vertical line, etc.)
        paths: [
          {
            d: `M 0 0 H ${width} V ${height} H 0 L 0 0`,
            fill: {
              dropTarget: false,
              color: "#ff0099", // Bright pink fill color
            },
          },
        ],
        // ViewBox defines the coordinate system for the shape
        viewBox: {
          width,
          height,
          top: 0,
          left: 0,
        },
        // Physical dimensions and positioning on the canvas
        width,
        height,
        rotation,
        top,
        left,
      };
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
    # App element children

    Demonstrates how app elements can contain multiple child elements positioned relative to each other. Creates a customizable grid of square shapes where users can control rows, columns, spacing, and individual element properties. This example showcases the core app element renderer API and how to create complex multi-element designs programmatically.

    For API reference docs and instructions on running this example, see: <https://www.canva.dev/docs/apps/examples/app-element-children/>.

    Related example: See app_image_elements for working with single elements within app elements.

    NOTE: This example differs from what's expected for public apps to pass a Canva review:

    - Error handling is simplified for demonstration. Production apps must implement comprehensive error handling with clear user feedback and graceful failure modes
    - Accessibility features aren't fully implemented. Production apps must meet WCAG 2.0 AA standards with proper keyboard navigation and ARIA labels
    - Input validation is minimal for demonstration. Production apps must validate all user inputs and provide clear error messaging
    - Internationalization isn't implemented. Production apps must support multiple languages using the `@canva/app-i18n-kit` package to pass Canva review requirements
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
