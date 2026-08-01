Source: https://www.canva.dev/docs/apps/examples/asset-upload/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Asset upload

Upload and manage assets directly into Canva.

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
   npm run start asset_upload
   ```

6. Click the **Preview URL** link shown in the terminal to open the example in the Canva editor.

## Example app source code

<Tabs>
  <Tab name="app.tsx">
    ```typescript
    // For usage information, see the README.md file.
    /* eslint-disable no-console */
    import { Alert, Button, Rows, Text } from "@canva/app-ui-kit";
    import { upload } from "@canva/asset";
    import {
      addAudioTrack,
      addElementAtCursor,
      addElementAtPoint,
    } from "@canva/design";
    import * as styles from "styles/components.css";
    import { useFeatureSupport } from "@canva/app-hooks";

    export const App = () => {
      const isSupported = useFeatureSupport();
      const addElement = [addElementAtPoint, addElementAtCursor].find((fn) =>
        isSupported(fn),
      );

      const importAndAddImage = async () => {
        if (!addElement) {
          return;
        }

        // Start uploading the image using Canva's upload API
        // This creates an asset reference that can be used immediately while the upload continues in the background
        const image = await upload({
          type: "image",
          mimeType: "image/jpeg",
          url: "https://www.canva.dev/example-assets/image-import/image.jpg",
          thumbnailUrl:
            "https://www.canva.dev/example-assets/image-import/thumbnail.jpg",
          width: 540,
          height: 720,
          aiDisclosure: "none",
        });

        // Add the image element to the current design using the asset reference
        // Canva will display the thumbnail initially and replace it with the full image once upload completes
        await addElement({
          type: "image",
          ref: image.ref,
          altText: {
            text: "a photo of buildings by the water",
            decorative: undefined,
          },
        });

        // Wait for the upload to complete to handle any upload errors
        // In production apps, this should include proper error handling and user feedback
        await image.whenUploaded();

        // Upload completed successfully
        console.log("Upload complete!");
      };

      const importAndAddVideo = async () => {
        if (!addElement) {
          return;
        }

        // Start uploading the video using Canva's upload API
        // Videos support both image and video thumbnails for better preview experience
        const queuedVideo = await upload({
          type: "video",
          mimeType: "video/mp4",
          url: "https://www.canva.dev/example-assets/video-import/video.mp4",
          thumbnailImageUrl:
            "https://www.canva.dev/example-assets/video-import/thumbnail-image.jpg",
          thumbnailVideoUrl:
            "https://www.canva.dev/example-assets/video-import/thumbnail-video.mp4",
          width: 405,
          height: 720,
          aiDisclosure: "none",
        });

        // Add the video element to the current design using the asset reference
        // The video thumbnail will be shown initially, replaced with the full video once upload completes
        await addElement({
          type: "video",
          ref: queuedVideo.ref,
          altText: {
            text: "a video of building with yellow spinning wheel",
            decorative: undefined,
          },
        });

        // Wait for the upload to complete to handle any upload errors
        // In production apps, this should include proper error handling and user feedback
        await queuedVideo.whenUploaded();

        // Upload completed successfully
        console.log("Upload complete!");
      };

      const importAndAddAudio = async () => {
        // Start uploading the audio file using Canva's upload API
        // Audio uploads require duration metadata and optionally a title
        const queuedAudio = await upload({
          type: "audio",
          mimeType: "audio/mp3",
          url: "https://www.canva.dev/example-assets/audio-import/audio.mp3",
          durationMs: 86047,
          title: "Example audio",
          aiDisclosure: "none",
        });

        // Add the audio to the design as a new audio track (not supported in all design types)
        // Audio tracks are added to the timeline and play in the background of the design
        await addAudioTrack({
          ref: queuedAudio.ref,
        });

        // Wait for the upload to complete to handle any upload errors
        // In production apps, this should include proper error handling and user feedback
        await queuedAudio.whenUploaded();

        // Upload completed successfully
        console.log("Upload complete!");
      };

      return (
        <div className={styles.scrollContainer}>
          <Rows spacing="3u">
            <Text>
              This example demonstrates how apps can import video, audio and image
              assets into Canva.
            </Text>
            <Rows spacing="1.5u">
              <Button
                onClick={importAndAddImage}
                variant="secondary"
                disabled={!addElement}
                tooltipLabel={
                  !addElement
                    ? "This feature is not supported in the current page"
                    : undefined
                }
                stretch
              >
                Import image
              </Button>
              <Button
                onClick={importAndAddVideo}
                variant="secondary"
                disabled={!addElement}
                tooltipLabel={
                  !addElement
                    ? "This feature is not supported in the current page"
                    : undefined
                }
                stretch
              >
                Import video
              </Button>
              <Button
                onClick={importAndAddAudio}
                variant="secondary"
                // addAudioTrack is not supported in certain design types such as docs
                disabled={!isSupported(addAudioTrack)}
                tooltipLabel={
                  !isSupported(addAudioTrack)
                    ? "This feature is not supported in the current page"
                    : undefined
                }
                stretch
              >
                Import audio
              </Button>
            </Rows>
            {!isSupported(addAudioTrack) && <UnsupportedAlert />}
          </Rows>
        </div>
      );
    };

    const UnsupportedAlert = () => (
      <Alert tone="warn">
        Sorry, the required feature (addAudioTrack) is not supported in the current
        design.
      </Alert>
    );
    ```
  </Tab>

  <Tab name="index.tsx">
    ```typescript
    // For usage information, see the README.md file.
    import { AppUiProvider } from "@canva/app-ui-kit";
    import { createRoot } from "react-dom/client";
    import "@canva/app-ui-kit/styles.css";

    import { App } from "./app";
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
    # Asset upload

    Demonstrates how to upload and import various media types (images, videos, audio) into Canva designs using the upload function. Shows asynchronous upload handling, thumbnail support, and design type compatibility checks.

    For API reference docs and instructions on running this example, see: https://www.canva.dev/docs/apps/examples/asset-upload/.

    Related examples: See digital_asset_management for external asset browsing, or drag_and_drop examples for alternative asset insertion patterns.

    NOTE: This example differs from what is expected for public apps to pass a Canva review:

    - Static assets are used for demonstration purposes only. Production apps should host assets on a CDN/hosting service and use the `upload` function from the `@canva/asset` package
    - Console.log statements are used for debugging purposes but should be replaced with proper error handling and logging in production apps
    - ESLint rule `no-console` is disabled for example purposes only. Production apps should not disable linting rules without proper justification
    - Error handling is simplified for demonstration. Production apps must implement comprehensive error handling with clear user feedback and graceful failure modes
    - Internationalization is not implemented. Production apps must support multiple languages using the `@canva/app-i18n-kit` package to pass Canva review requirements
    - The code structure is simplified: Production apps using [intents](https://www.canva.dev/docs/apps/intents/) are recommended to call the prepareDesignEditor function from src/intents/design_editor/index.tsx
    ```
  </Tab>
</Tabs>

## API reference

* [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/)
* [`addAudioTrack`](https://www.canva.dev/docs/apps/api/latest/design-add-audio-track/)
* [`addElementAtCursor`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-cursor/)
* [`addElementAtPoint`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/)
* [`prepareDesignEditor`](https://www.canva.dev/docs/apps/api/latest/intents-design-prepare-design-editor/)
* [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/)

## Need help?

* Join our [Community Forum](https://community.canva.dev/)
* Report issues with this example on [GitHub](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/issues)
