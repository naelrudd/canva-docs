Source: https://www.canva.dev/docs/apps/examples/app-shape-elements/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# App shape elements

Create shape elements inside app elements.

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
   npm run start app_shape_elements
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
      Column,
      Columns,
      FormField,
      MultilineInput,
      NumberInput,
      PlusIcon,
      Rows,
      Text,
      Title,
    } from "@canva/app-ui-kit";
    import { type AppElementOptions, initAppElement } from "@canva/design";
    import { useEffect, useState } from "react";
    import * as styles from "styles/components.css";

    // Data structure for shape elements within app elements
    type AppElementData = {
      // Array of SVG path objects that define the shape geometry
      paths: {
        d: string; // SVG path data using standard path commands (M, L, H, V, C, etc.)
        fill: {
          dropTarget: boolean; // Whether this path accepts dropped content from Canva
          color: string; // Hex color value for the shape fill
        };
      }[];
      // SVG viewBox defines the coordinate system and visible area
      viewBox: {
        width: number;
        height: number;
        top: number;
        left: number;
      };
      // Physical dimensions and rotation of the app element in Canva
      width: number;
      height: number;
      rotation: number;
    };

    // Event object received when an app element is selected or modified in Canva
    type AppElementChangeEvent = {
      data: AppElementData;
      update?: (opts: AppElementOptions<AppElementData>) => Promise<void>; // Function to update existing app element
    };

    // Default state when no app element is selected - creates a simple square path
    const initialState: AppElementChangeEvent = {
      data: {
        paths: [
          {
            d: "M 0 0 H 100 V 100 H 0 L 0 0", // SVG path for a 100x100 square
            fill: {
              dropTarget: false,
              color: "#ff0099",
            },
          },
        ],
        viewBox: {
          width: 100,
          height: 100,
          top: 0,
          left: 0,
        },
        width: 100,
        height: 100,
        rotation: 0,
      },
    };

    // Initialize the app element client to handle shape rendering in Canva
    const appElementClient = initAppElement<AppElementData>({
      // Define how the app element data should be rendered as design elements
      render: (data) => {
        return [{ type: "shape", top: 0, left: 0, ...data }];
      },
    });

    export const App = () => {
      const [state, setState] = useState<AppElementChangeEvent>(initialState);
      const {
        data: { paths, viewBox, width, height, rotation },
      } = state;
      const disabled = paths.length < 1;

      useEffect(() => {
        // Register listener for when user selects an app element in Canva
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
          <Rows spacing="3u">
            <Text>
              This example demonstrates how apps can create shape elements inside
              app elements. Using an app element makes the shape element re-editable
              and lets apps control additional properties, such as the width and
              height.
            </Text>
            <Rows spacing="1u">
              <Columns spacing="0" alignY="center">
                <Column>
                  <Title size="small">Paths</Title>
                </Column>
                <Column width="content">
                  {paths.length < 7 && (
                    <Button
                      variant="tertiary"
                      icon={PlusIcon}
                      ariaLabel="Add a new path"
                      onClick={() => {
                        setState((prevState) => {
                          return {
                            ...prevState,
                            data: {
                              ...prevState.data,
                              paths: [
                                ...prevState.data.paths,
                                {
                                  d: "",
                                  fill: {
                                    dropTarget: false,
                                    color: "#000000",
                                  },
                                },
                              ],
                            },
                          };
                        });
                      }}
                    />
                  )}
                </Column>
              </Columns>
              {paths.map((path, outerIndex) => {
                return (
                  <Rows spacing="2u" key={outerIndex}>
                    <FormField
                      label="Line commands"
                      value={path.d}
                      control={(props) => (
                        <MultilineInput
                          {...props}
                          onChange={(value) => {
                            setState((prevState) => {
                              return {
                                ...prevState,
                                data: {
                                  ...prevState.data,
                                  paths: prevState.data.paths.map(
                                    (path, innerIndex) => {
                                      if (outerIndex === innerIndex) {
                                        return {
                                          ...path,
                                          d: value,
                                        };
                                      }
                                      return path;
                                    },
                                  ),
                                },
                              };
                            });
                          }}
                        />
                      )}
                    />
                    <FormField
                      label="Color"
                      control={() => (
                        <ColorSelector
                          color={path.fill.color}
                          onChange={(value) => {
                            setState((prevState) => {
                              return {
                                ...prevState,
                                data: {
                                  ...prevState.data,
                                  paths: prevState.data.paths.map(
                                    (path, innerIndex) => {
                                      if (outerIndex === innerIndex) {
                                        return {
                                          ...path,
                                          fill: {
                                            ...path.fill,
                                            color: value,
                                          },
                                        };
                                      }
                                      return path;
                                    },
                                  ),
                                },
                              };
                            });
                          }}
                        />
                      )}
                    />
                  </Rows>
                );
              })}
            </Rows>
            <Rows spacing="2u">
              <Title size="small">Viewbox</Title>
              <FormField
                label="Width"
                value={viewBox.width}
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
                            viewBox: {
                              ...prevState.data.viewBox,
                              width: Number(value || 0),
                            },
                          },
                        };
                      });
                    }}
                  />
                )}
              />
              <FormField
                label="Height"
                value={viewBox.height}
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
                            viewBox: {
                              ...prevState.data.viewBox,
                              height: Number(value || 0),
                            },
                          },
                        };
                      });
                    }}
                  />
                )}
              />
              <FormField
                label="Top"
                value={viewBox.top}
                control={(props) => (
                  <NumberInput
                    {...props}
                    min={0}
                    onChange={(value) => {
                      setState((prevState) => {
                        return {
                          ...prevState,
                          data: {
                            ...prevState.data,
                            viewBox: {
                              ...prevState.data.viewBox,
                              top: Number(value || 0),
                            },
                          },
                        };
                      });
                    }}
                  />
                )}
              />
              <FormField
                label="Left"
                value={viewBox.left}
                control={(props) => (
                  <NumberInput
                    {...props}
                    min={0}
                    onChange={(value) => {
                      setState((prevState) => {
                        return {
                          ...prevState,
                          data: {
                            ...prevState.data,
                            viewBox: {
                              ...prevState.data.viewBox,
                              left: Number(value || 0),
                            },
                          },
                        };
                      });
                    }}
                  />
                )}
              />
            </Rows>
            <Rows spacing="2u">
              <Title size="small">Position</Title>
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
            </Rows>
            <Rows spacing="1u">
              <Button
                variant="secondary"
                onClick={() => {
                  setState(initialState);
                }}
                stretch
              >
                Reset
              </Button>
              <Button
                variant="primary"
                onClick={() => {
                  if (state.update) {
                    // Update existing app element in Canva
                    state.update({ data: state.data });
                  } else {
                    // Add new app element to Canva design
                    appElementClient.addElement({ data: state.data });
                  }
                }}
                disabled={disabled}
                stretch
              >
                {`${state.update ? "Update" : "Add"} shape`}
              </Button>
            </Rows>
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
    # App shape elements

    This example demonstrates how to create custom vector shape elements inside app elements using SVG path data. It shows shape creation, color customization, and path manipulation for building reusable custom shapes.

    For API reference docs and instructions on running this example, see: https://www.canva.dev/docs/apps/examples/app-shape-elements/.

    Related examples: See `design_elements/shape_elements` for direct shape insertion, or `app_element_children` for multiple shapes within app elements.

    NOTE: This example differs from what is expected for public apps to pass a Canva review:

    - Content is hardcoded for demonstration purposes only. Production apps should provide user input interfaces or dynamic content loading and user-friendly shape creation and editing interfaces
    - Path validation and error handling is simplified for demonstration. Production apps must validate SVG paths and handle malformed path data gracefully
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
