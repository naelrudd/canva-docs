Source: https://www.canva.dev/docs/apps/examples/fonts/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Fonts

Use the fonts picker to apply custom fonts to text elements in designs.

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
   npm run start fonts
   ```

6. Click the **Preview URL** link shown in the terminal to open the example in the Canva editor.

## Example app source code

<Tabs>
  <Tab name="app.tsx">
    ```typescript
    // For usage information, see the README.md file.
    import {
      Box,
      Button,
      ChevronDownIcon,
      FormField,
      Rows,
      Select,
      Text,
      TextInput,
      Title,
      SegmentedControl,
      ImageCard,
    } from "@canva/app-ui-kit";
    import type { Font, FontStyle, FontWeightName } from "@canva/asset";
    // Canva's Font APIs for discovering available fonts and opening the font picker
    import { findFonts, requestFontSelection } from "@canva/asset";
    import { addElementAtCursor, addElementAtPoint } from "@canva/design";
    import { useState, useEffect, useCallback } from "react";
    import * as styles from "styles/components.css";
    import { useFeatureSupport } from "@canva/app-hooks";

    type TextConfig = {
      text: string;
      color: string;
      fontWeight: FontWeightName;
      fontStyle: FontStyle;
    };

    const initialConfig: TextConfig = {
      text: "Hello world",
      color: "#8B3DFF",
      fontWeight: "normal",
      fontStyle: "normal",
    };

    const fontStyleOptions: {
      value: FontStyle;
      label: FontStyle;
      disabled?: boolean;
    }[] = [
      { value: "normal", label: "normal", disabled: false },
      { value: "italic", label: "italic", disabled: false },
    ];

    export const App = () => {
      const isSupported = useFeatureSupport();
      const addElement = [addElementAtPoint, addElementAtCursor].find((fn) =>
        isSupported(fn),
      );
      const [textConfig, setTextConfig] = useState<TextConfig>(initialConfig);
      const [selectedFont, setSelectedFont] = useState<Font | undefined>(undefined);
      const [availableFonts, setAvailableFonts] = useState<readonly Font[]>([]);

      // Fetch all fonts available in Canva using the findFonts API
      const fetchFonts = useCallback(async () => {
        const response = await findFonts();
        setAvailableFonts(response.fonts);
      }, [setAvailableFonts]);

      useEffect(() => {
        fetchFonts();
      }, [fetchFonts]);

      const { text, fontWeight, fontStyle } = textConfig;
      const disabled = text.trim().length === 0;
      const availableFontWeights = getFontWeights(selectedFont);

      const availableFontStyles = getFontStyles(fontWeight, selectedFont);
      const availableStyleValues = new Set(
        availableFontStyles.map((style) => style.value),
      ); // Create a Set for lookup
      const availableFontStyleOptions = fontStyleOptions.map((styleOption) => {
        // Check if the current style option is NOT present in the available styles.
        if (!availableStyleValues.has(styleOption.value)) {
          // If so, return a new object with `disabled` set to true, keeping the rest of the object the same.
          return { ...styleOption, disabled: true };
        }
        // If the style is available, return it as is. Also ensures disabled is set to false explicitly if not already defined.
        return { ...styleOption, disabled: false };
      });

      const resetSelectedFontStyleAndWeight = (selectedFont?: Font) => {
        setTextConfig((prevState) => {
          return {
            ...prevState,
            fontStyle:
              getFontStyles(fontWeight, selectedFont)[0]?.value || "normal",
            fontWeight: getFontWeights(selectedFont)[0]?.value || "normal",
          };
        });
      };

      return (
        <div className={styles.scrollContainer}>
          <Rows spacing="2u">
            <Text>
              This example demonstrates how apps can apply fonts to text elements
              and add to design.
            </Text>
            <FormField
              label="Text"
              value={text}
              control={(props) => (
                <TextInput
                  {...props}
                  onChange={(value) => {
                    setTextConfig((prevState) => {
                      return {
                        ...prevState,
                        text: value,
                      };
                    });
                  }}
                />
              )}
            />
            <Title size="small">Font selection</Title>
            {availableFonts.length > 0 && (
              <FormField
                label="Font family"
                value={selectedFont?.ref}
                control={(props) => (
                  <Select
                    {...props}
                    stretch
                    onChange={(ref) => {
                      const selected = availableFonts.find((f) => f.ref === ref);
                      setSelectedFont(selected);
                      resetSelectedFontStyleAndWeight(selected);
                    }}
                    options={availableFonts.map((f) => ({
                      value: f.ref,
                      label: f.name,
                    }))}
                  />
                )}
              />
            )}
            <Button
              variant="secondary"
              icon={ChevronDownIcon}
              iconPosition="end"
              alignment="start"
              stretch={true}
              onClick={async () => {
                // Open Canva's built-in font picker dialog
                const response = await requestFontSelection({
                  selectedFontRef: selectedFont?.ref,
                });
                if (response.type === "completed") {
                  setSelectedFont(response.font);
                  resetSelectedFontStyleAndWeight(response.font);
                }
              }}
              disabled={disabled}
            >
              {selectedFont?.name || "Select a font"}
            </Button>
            {selectedFont?.previewUrl && (
              <Box background="neutralLow" padding="2u" width="full">
                <Rows spacing="0" align="center">
                  <Box>
                    <ImageCard
                      thumbnailUrl={selectedFont.previewUrl}
                      alt={selectedFont.name}
                    />
                  </Box>
                </Rows>
              </Box>
            )}
            <Title size="small">Font options</Title>
            <FormField
              label="Font weight"
              value={fontWeight}
              control={(props) => (
                <Select
                  {...props}
                  stretch
                  onChange={(fontWeight) => {
                    setTextConfig((prevState) => {
                      return {
                        ...prevState,
                        fontWeight,
                      };
                    });
                  }}
                  disabled={!selectedFont || availableFontWeights.length === 0}
                  options={availableFontWeights}
                />
              )}
            />
            <FormField
              label="Font style"
              value={fontStyle}
              control={(props) => (
                <SegmentedControl
                  {...props}
                  options={availableFontStyleOptions}
                  value={fontStyle}
                  onChange={(style) => {
                    setTextConfig((prevState) => {
                      return {
                        ...prevState,
                        fontStyle: style,
                      };
                    });
                  }}
                />
              )}
            />
            <Button
              variant="primary"
              onClick={() => {
                if (!addElement) {
                  return;
                }

                // Create a text element with the selected font and add it to the Canva design
                addElement({
                  type: "text",
                  ...textConfig,
                  fontRef: selectedFont?.ref,
                  children: [textConfig.text],
                });
              }}
              disabled={disabled || !addElement}
              tooltipLabel={
                !addElement
                  ? "This feature is not supported in the current page"
                  : undefined
              }
              stretch
            >
              Add text element
            </Button>
          </Rows>
        </div>
      );
    };

    // Extract available font weights from a Canva Font object for display in UI components
    const getFontWeights = (
      font?: Font,
    ): {
      value: FontWeightName;
      label: FontWeightName;
    }[] => {
      return font
        ? font.weights.map((w) => ({
            value: w.weight,
            label: w.weight,
          }))
        : [];
    };

    // Extract available font styles for a specific weight from a Canva Font object
    const getFontStyles = (
      fontWeight: FontWeightName,
      font?: Font,
    ): {
      value: FontStyle;
      label: FontStyle;
    }[] => {
      return font
        ? (font.weights
            .find((w) => w.weight === fontWeight)
            ?.styles.map((s) => ({ value: s, label: s })) ?? [])
        : [];
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
    # Fonts

    Demonstrates how to find, select, and apply fonts to text elements. Shows font discovery, weight and style selection, and font picker integration for creating styled text with custom typography.

    For API reference docs and instructions on running this example, see: <https://www.canva.dev/docs/apps/examples/fonts/>.

    Related examples: See design_elements/text_elements for basic text insertion, or app_text_elements for text within app elements.

    NOTE: This example differs from what is expected for public apps to pass a Canva review:

    - Error handling for font loading and unavailable fonts is simplified for demonstration. Production apps must implement comprehensive error handling with retry logic and user feedback for API failures
    - Font fallback handling is not implemented. Production apps should provide fallback fonts and handle font loading failures gracefully
    - Text content is hardcoded for demonstration purposes only. Production apps should provide user input interfaces or dynamic content loading
    - Internationalization is not implemented. Production apps must support multiple languages using the `@canva/app-i18n-kit` package to pass Canva review requirements
    - The code structure is simplified: Production apps using [intents](https://www.canva.dev/docs/apps/intents/) are recommended to call the prepareDesignEditor function from src/intents/design_editor/index.tsx
    ```
  </Tab>
</Tabs>

## API reference

* [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/)
* [`addElementAtCursor`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-cursor/)
* [`addElementAtPoint`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/)
* [`findFonts`](https://www.canva.dev/docs/apps/api/latest/asset-find-fonts/)
* [`prepareDesignEditor`](https://www.canva.dev/docs/apps/api/latest/intents-design-prepare-design-editor/)
* [`requestFontSelection`](https://www.canva.dev/docs/apps/api/latest/asset-request-font-selection/)

## Need help?

* Join our [Community Forum](https://community.canva.dev/)
* Report issues with this example on [GitHub](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/issues)
