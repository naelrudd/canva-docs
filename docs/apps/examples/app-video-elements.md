Source: https://www.canva.dev/docs/apps/examples/app-video-elements/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# App video elements

Create video elements inside app elements.

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
   npm run start app_video_elements
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
      FormField,
      Grid,
      VideoCard,
      NumberInput,
      Rows,
      Text,
    } from "@canva/app-ui-kit";
    import {
      type AppElementOptions,
      initAppElement,
      type VideoRef,
    } from "@canva/design";
    import React from "react";
    import * as styles from "styles/components.css";
    import { upload } from "@canva/asset";

    // Type definition for the data stored within an app element
    type AppElementData = {
      title: string;
      videoId: string;
      width: number;
      height: number;
      rotation: number;
    };

    // Event handler type for app element changes (creation or editing)
    type AppElementChangeEvent = {
      data: AppElementData;
      update?: (opts: AppElementOptions<AppElementData>) => Promise<void>;
    };

    type ExampleStaticVideo = {
      title: string;
      url: string;
      thumbnailImageUrl: string;
      thumbnailVideoUrl: string;
      width: number;
      height: number;
      videoRef: VideoRef | undefined;
    };

    // Sample video data for demonstration - in production apps, use CDN hosting
    const STATIC_VIDEOS: Record<string, ExampleStaticVideo> = {
      building: {
        title: "Pinwheel on building",
        url: "https://www.canva.dev/example-assets/video-import/video.mp4",
        thumbnailImageUrl:
          "https://www.canva.dev/example-assets/video-import/thumbnail-image.jpg",
        thumbnailVideoUrl:
          "https://www.canva.dev/example-assets/video-import/thumbnail-video.mp4",
        width: 405,
        height: 720,
        videoRef: undefined,
      },
      beach: {
        title: "A beautiful beach scene",
        url: "https://www.canva.dev/example-assets/video-import/beach-video.mp4",
        thumbnailImageUrl:
          "https://www.canva.dev/example-assets/video-import/beach-thumbnail-image.jpg",
        thumbnailVideoUrl:
          "https://www.canva.dev/example-assets/video-import/beach-thumbnail-video.mp4",
        width: 320,
        height: 180,
        videoRef: undefined,
      },
    };

    const initialState: AppElementChangeEvent = {
      data: {
        title: "Pinwheel on building",
        videoId: "building",
        width: 405,
        height: 720,
        rotation: 0,
      },
    };

    // Initialize the app element client to handle video rendering in Canva designs
    const appElementClient = initAppElement<AppElementData>({
      render: (data) => {
        // In production, you would likely be fetching this from a database or API
        const video = STATIC_VIDEOS[data.videoId];

        if (!video) {
          throw new Error(`Unknown video ID: ${data.videoId}`);
        }

        if (!video.videoRef) {
          throw new Error(`Video ${data.videoId} has not been uploaded yet`);
        }

        return [
          {
            type: "video",
            top: 0,
            left: 0,
            altText: {
              text: `a video of ${data.title}`,
              decorative: undefined,
            },
            ref: video.videoRef,
            ...data,
          },
        ];
      },
    });

    export const App = () => {
      const [loading, setLoading] = React.useState(false);
      const [state, setState] = React.useState<AppElementChangeEvent>(initialState);
      const {
        data: { videoId, width, height, rotation },
      } = state;
      const disabled = loading || !videoId || videoId.trim().length < 1;

      const items = Object.entries(STATIC_VIDEOS).map(([key, value]) => {
        const { title, thumbnailImageUrl, thumbnailVideoUrl, width, height } =
          value;
        return {
          key,
          title,
          thumbnailImageUrl,
          thumbnailVideoUrl,
          active: videoId === key,
          onClick: () => {
            setState((prevState) => {
              return {
                ...prevState,
                data: {
                  ...prevState.data,
                  videoId: key,
                  width,
                  height,
                },
              };
            });
          },
        };
      });

      const addOrUpdateVideo = React.useCallback(async () => {
        setLoading(true);
        try {
          // In production, you would likely be fetching this from a database or API
          const video = STATIC_VIDEOS[state.data.videoId];

          if (!video) {
            throw new Error(`Unknown video ID: ${state.data.videoId}`);
          }

          // Upload video to Canva if not already uploaded
          if (!video.videoRef) {
            const { ref } = await upload({
              type: "video",
              mimeType: "video/mp4",
              url: video.url,
              thumbnailImageUrl: video.thumbnailImageUrl,
              thumbnailVideoUrl: video.thumbnailVideoUrl,
              aiDisclosure: "none",
            });

            // Update the mutable videoRef property
            video.videoRef = ref;
          }

          // Add new app element or update existing one based on current state
          if (state.update) {
            state.update({ data: state.data });
          } else {
            appElementClient.addElement({ data: state.data });
          }
        } finally {
          setLoading(false);
        }
      }, [state]);

      // Register listener for when user selects an existing app element to edit
      React.useEffect(() => {
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
              This example demonstrates how apps can create video elements inside
              app elements. Using an app element makes the video element re-editable
              and lets apps control additional properties, such as the width and
              height.
            </Text>
            <FormField
              label="Select a video"
              control={(props) => (
                <Box {...props} padding="1u">
                  <Grid columns={2} spacing="1.5u">
                    {items.map((item) => (
                      <VideoCard
                        ariaLabel={item.title}
                        mimeType="video/mp4"
                        key={item.key}
                        thumbnailUrl={item.thumbnailImageUrl}
                        videoPreviewUrl={item.thumbnailVideoUrl}
                        onClick={item.onClick}
                        selectable={true}
                        selected={item.active}
                        borderRadius="standard"
                        thumbnailHeight={150}
                      />
                    ))}
                  </Grid>
                </Box>
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
                          width: value || 0,
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
                          height: value || 0,
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
                          rotation: value || 0,
                        },
                      };
                    });
                  }}
                />
              )}
            />
            <Button
              variant="primary"
              onClick={addOrUpdateVideo}
              disabled={disabled}
              stretch
            >
              {`${state.update ? "Update" : "Add"} video`}
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
    # App video elements

    Demonstrates how to create video elements inside app elements, making them re-editable with controllable properties like dimensions and rotation. Users can select from predefined videos and customize their appearance.

    For API reference docs and instructions on running this example, see: https://www.canva.dev/docs/apps/examples/app-video-elements/.

    Related examples: See app_image_elements for images within app elements, or design_elements/video_elements for direct video insertion.

    NOTE: This example differs from what is expected for public apps to pass a Canva review:

    - Static video URLs are used for demonstration purposes only. Production apps should host videos on a CDN/hosting service and use the `upload` function from the `@canva/asset` package for user uploads
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
* [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/)

## Need help?

* Join our [Community Forum](https://community.canva.dev/)
* Report issues with this example on [GitHub](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/issues)
