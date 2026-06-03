Source: https://www.canva.dev/docs/apps/examples/digital-asset-management/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Digital asset management

Digital asset management system using Canva app components.

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
   npm run start digital_asset_management
   ```

6. Click the **Preview URL** link shown in the terminal to open the example in the Canva editor.

## Example app source code

<Tabs>
  <Tab name="adapter.ts">
    ```typescript
    // For usage information, see the README.md file.
    import type {
      FindResourcesRequest,
      FindResourcesResponse,
    } from "@canva/app-components";
    import { auth } from "@canva/user";

    /**
     * Adapter function that handles communication with your digital asset management backend.
     * This function is called by SearchableListView to fetch resources based on user requests.
     */
    export async function findResources(
      request: FindResourcesRequest<"folder">,
    ): Promise<FindResourcesResponse> {
      // Get the Canva user token for authentication with your backend
      const userToken = await auth.getCanvaUserToken();

      // Replace this URL with your actual backend endpoint.
      // For production apps, ensure your backend validates the Canva user token and implements proper security measures.
      // If using the backend example, the URL should be updated to `${BACKEND_HOST}/api/resources/find` to ensure requests are authenticated in production
      const url = new URL(`${BACKEND_HOST}/resources/find`);

      try {
        const response = await fetch(url, {
          method: "POST",
          headers: {
            Authorization: `Bearer ${userToken}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(request),
        });
        const body = await response.json();

        // Return successful response with resources and continuation token for pagination
        if (body.resources) {
          return {
            type: "SUCCESS",
            resources: body.resources,
            continuation: body.continuation,
          };
        }
        return {
          type: "ERROR",
          errorCode: body.errorCode || "INTERNAL_ERROR",
        };
      } catch {
        // Handle network errors or other exceptions
        return {
          type: "ERROR",
          errorCode: "INTERNAL_ERROR",
        };
      }
    }
    ```
  </Tab>

  <Tab name="app.tsx">
    ```typescript
    // For usage information, see the README.md file.
    import { SearchableListView } from "@canva/app-components";
    import { Box } from "@canva/app-ui-kit";
    import "@canva/app-ui-kit/styles.css";
    import { useConfig } from "./config";
    import { findResources } from "./adapter";
    import * as styles from "./index.css";

    export function App() {
      const config = useConfig();
      return (
        <Box className={styles.rootWrapper} height="full">
          {/*
            SearchableListView is a Canva component that provides a complete digital asset management interface.
            It handles searching, filtering, browsing containers, and importing assets from external platforms.
          */}
          <SearchableListView
            config={config}
            findResources={findResources}
            /*
              Remove the saveExportedDesign prop and config.export settings if your app
              does not support exporting Canva designs to an external platform
            */
            saveExportedDesign={(
              exportedDesignUrl: string,
              containerId: string | undefined,
              designTitle: string | undefined,
            ) => {
              /*
                Replace this mock implementation with your platform's actual save logic.
                The function should save the exported design to your digital asset management system.
              */
              return new Promise((resolve) => {
                setTimeout(() => {
                  /* eslint-disable-next-line no-console */
                  console.info(
                    `Saving file "${designTitle}" from ${exportedDesignUrl} to ${config.serviceName} container id: ${containerId}`,
                  );
                  resolve({ success: true });
                }, 1000);
              });
            }}
          />
        </Box>
      );
    }
    ```
  </Tab>

  <Tab name="backend/routers/dam.ts">
    ```typescript
    // For usage information, see the README.md file.
    import express from "express";
    import crypto from "crypto";
    import type { Container, Resource } from "@canva/app-components";

    /**
     * Generates a unique hash for a URL.
     * Used for creating unique identifiers for digital assets from external URLs.
     */
    export async function generateHash(message: string) {
      const msgUint8 = new TextEncoder().encode(message);
      const hashBuffer = await crypto.subtle.digest("SHA-256", msgUint8);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      const hashHex = hashArray
        .map((b) => b.toString(16).padStart(2, "0"))
        .join("");
      return hashHex;
    }

    // Mock image URLs for demonstration purposes - replace with your actual digital asset sources
    const imageUrls = [
      "https://images.pexels.com/photos/1495580/pexels-photo-1495580.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
      "https://images.pexels.com/photos/3943197/pexels-photo-3943197.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
      "https://images.pexels.com/photos/7195267/pexels-photo-7195267.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
      "https://images.pexels.com/photos/2904142/pexels-photo-2904142.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
      "https://images.pexels.com/photos/5403478/pexels-photo-5403478.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    ];

    export const createDamRouter = () => {
      const router = express.Router();

      /*
        Main endpoint for finding digital assets and containers.
        This should be replaced with actual integration to your digital asset management system.
      */
      router.post("/resources/find", async (req, res) => {
        /*
          Extract relevant fields from the FindResourcesRequest.
          Replace this mock implementation with actual queries to your digital asset management system.
          Consider implementing proper filtering, sorting, and pagination based on these parameters.
        */
        const {
          types,
          continuation,
          locale,
          // Other available fields from the FindResourcesRequest:
          // containerTypes, limit, filters, query, sort, tab, containerId, parentContainerType
        } = req.body;

        let resources: Resource[] = [];

        // Handle image resource requests
        if (types.includes("IMAGE")) {
          resources = await Promise.all(
            Array.from({ length: 40 }, async (_, i) => {
              const imageUrl = imageUrls[i % imageUrls.length];

              if (!imageUrl) {
                throw new Error(`Image URL not found for index ${i}`);
              }

              return {
                id: await generateHash(i + ""),
                mimeType: "image/jpeg",
                name: `My new thing in ${locale}`, // Uses locale for demonstration - implement proper i18n
                type: "IMAGE",
                thumbnail: {
                  url: imageUrl,
                },
                url: imageUrl,
              };
            }),
          );
        }

        // Handle container (folder) resource requests
        if (types.includes("CONTAINER")) {
          const containers = await Promise.all(
            Array.from(
              { length: 10 },
              async (_, i) =>
                ({
                  id: await generateHash(i + ""),
                  containerType: "folder",
                  name: `My folder ${i}`,
                  type: "CONTAINER",
                }) satisfies Container,
            ),
          );

          resources = resources.concat(containers);
        }

        // Send response with resources and pagination token
        res.send({
          resources,
          continuation: +(continuation || 0) + 1,
        });
      });

      return router;
    };
    ```
  </Tab>

  <Tab name="backend/server.ts">
    ```typescript
    // For usage information, see the README.md file.
    import express from "express";
    import cors from "cors";
    import { createDamRouter } from "./routers/dam";
    import { createBaseServer } from "../../../../utils/backend/base_backend/create";
    import { user } from "@canva/app-middleware/express";

    async function main() {
      /*
        Set the CANVA_APP_ID environment variable in your project's .env file.
        This should match the app ID from your Canva Developer Portal.
      */
      const APP_ID = process.env.CANVA_APP_ID;

      if (!APP_ID) {
        throw new Error(
          `The CANVA_APP_ID environment variable is undefined. Set the variable in the project's .env file.`,
        );
      }

      const router = express.Router();

      /**
       * IMPORTANT: Configure your CORS Policy
       *
       * Cross-Origin Resource Sharing
       * ([CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS)) is an
       * [HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP)-header based
       * mechanism that allows a server to indicate any
       * [origins](https://developer.mozilla.org/en-US/docs/Glossary/Origin)
       * (domain, scheme, or port) other than its own from which a browser should
       * permit loading resources.
       *
       * A basic CORS configuration would include the origin of your app in the
       * following example:
       * const corsOptions = {
       *   origin: 'https://app-abcdefg.canva-apps.com',
       *   optionsSuccessStatus: 200
       * }
       *
       * The origin of your app is https://app-${APP_ID}.canva-apps.com, and note
       * that the APP_ID should to be converted to lowercase.
       *
       * https://www.npmjs.com/package/cors#configuring-cors
       *
       * You may need to include multiple permissible origins, or dynamic origins
       * based on the environment in which the server is running. Further
       * information can be found
       * [here](https://www.npmjs.com/package/cors#configuring-cors-w-dynamic-origin).
       */
      router.use(cors());

      /**
       * JWT middleware for authenticating requests from Canva apps.
       * This should be applied to all routes that require user authentication.
       */
      router.use(user.verifyToken({ appId: APP_ID }));

      /**
       * Add routes for digital asset management.
       */
      const damRouter = createDamRouter();
      router.use(damRouter);

      const server = createBaseServer(router);
      server.start(process.env.CANVA_BACKEND_PORT);
    }

    main();
    ```
  </Tab>

  <Tab name="config.ts">
    ```typescript
    // For usage information, see the README.md file.
    import type { Config } from "@canva/app-components";
    import { useIntl } from "react-intl";

    type ContainerTypes = "folder";

    /**
     * Configuration hook for the SearchableListView component.
     * Defines the digital asset management interface settings including search filters,
     * container types, sort options, and export capabilities.
     */
    export const useConfig = (): Config<ContainerTypes> => {
      const intl = useIntl();
      return {
        serviceName: intl.formatMessage({
          defaultMessage: "Example App",
          description:
            "Name of the service where the app will pull digital assets from",
        }),
        search: {
          enabled: true,
          filterFormConfig: {
            containerTypes: ["folder"],
            filters: [
              {
                filterType: "CHECKBOX",
                label: intl.formatMessage({
                  defaultMessage: "File Type",
                  description: "Label of filters for file type",
                }),
                key: "fileType",
                options: [
                  { value: "mp4", label: "MP4" },
                  { value: "png", label: "PNG" },
                  { value: "jpeg", label: "JPEG" },
                ],
                allowCustomValue: true,
              },
              {
                filterType: "RADIO",
                label: intl.formatMessage({
                  defaultMessage: "Size",
                  description: "Label of filters for asset size",
                }),
                key: "size",
                options: [
                  {
                    label: intl.formatMessage({
                      defaultMessage: "Large (800+ px)",
                      description: "One of the filter options for asset size",
                    }),
                    value: "large",
                  },
                  {
                    label: intl.formatMessage({
                      defaultMessage: "Medium (200-799px)",
                      description: "One of the filter options for asset size",
                    }),
                    value: "medium",
                  },
                ],
                allowCustomValue: true,
                customValueInputType: "SIZE_RANGE",
              },
              {
                filterType: "RADIO",
                label: intl.formatMessage({
                  defaultMessage: "Update Date",
                  description: "Label of the filters for asset's update date",
                }),
                key: "updateDate",
                options: [
                  {
                    value: ">now-30m",
                    label: intl.formatMessage({
                      defaultMessage: "Last 30 Minutes",
                      description:
                        "One of the filter options for asset update date",
                    }),
                  },
                  {
                    value: ">now-7d",
                    label: intl.formatMessage({
                      defaultMessage: "Last 7 days",
                      description:
                        "One of the filter options for asset update date",
                    }),
                  },
                ],
                allowCustomValue: true,
                customValueInputType: "DATE_RANGE",
              },
              {
                filterType: "RADIO",
                label: intl.formatMessage({
                  defaultMessage: "Design Status",
                  description: "Label of the filters for asset's design status",
                }),
                key: "designStatus",
                options: [
                  {
                    value: "approved",
                    label: intl.formatMessage({
                      defaultMessage: "Approved",
                      description:
                        "One of the filter options for asset design status",
                    }),
                  },
                  {
                    value: "rejected",
                    label: intl.formatMessage({
                      defaultMessage: "Rejected",
                      description:
                        "One of the filter options for asset design status",
                    }),
                  },
                  {
                    value: "draft",
                    label: intl.formatMessage({
                      defaultMessage: "Draft",
                      description:
                        "One of the filter options for asset design status",
                    }),
                  },
                ],
                allowCustomValue: true,
                customValueInputType: "PLAIN_TEXT",
              },
            ],
          },
        },
        containerTypes: [
          {
            value: "folder",
            label: intl.formatMessage({
              defaultMessage: "Folders",
              description: "Name of the asset container type",
            }),
            listingSurfaces: [
              { surface: "HOMEPAGE" },
              {
                surface: "CONTAINER",
                parentContainerTypes: ["folder"],
              },
              { surface: "SEARCH" },
            ],
            searchInsideContainer: {
              enabled: true,
              placeholder: intl.formatMessage({
                defaultMessage: "Search for media inside this folder",
                description: "Placeholder of a search input box",
              }),
            },
          },
        ],
        sortOptions: [
          {
            value: "created_at DESC",
            label: intl.formatMessage({
              defaultMessage: "Creation date (newest)",
              description: "One of the sort options",
            }),
          },
          {
            value: "created_at ASC",
            label: intl.formatMessage({
              defaultMessage: "Creation date (oldest)",
              description: "One of the sort options",
            }),
          },
          {
            value: "updated_at DESC",
            label: intl.formatMessage({
              defaultMessage: "Updated (newest)",
              description: "One of the sort options",
            }),
          },
          {
            value: "updated_at ASC",
            label: intl.formatMessage({
              defaultMessage: "Updated (oldest)",
              description: "One of the sort options",
            }),
          },
          {
            value: "name ASC",
            label: intl.formatMessage({
              defaultMessage: "Name (A-Z)",
              description: "One of the sort options",
            }),
          },
          {
            value: "name DESC",
            label: intl.formatMessage({
              defaultMessage: "Name (Z-A)",
              description: "One of the sort options",
            }),
          },
        ],
        layouts: ["MASONRY", "LIST"],
        resourceTypes: ["IMAGE", "VIDEO", "EMBED"],
        moreInfoMessage: intl.formatMessage({
          defaultMessage:
            "At the moment, we only support images and videos. Corrupted and unsupported files will not appear.",
          description: "Helper text to explain why some assets are not visible",
        }),
        /*
          Remove this export configuration if your app does not support 
          exporting Canva designs to your external platform
        */
        export: {
          enabled: true,
          /*
            Specify container types that users can choose when saving exported designs.
            Remove this field if users don't need to choose a specific container
          */
          containerTypes: ["folder"],
          /*
            List the file types your platform supports for exported designs.
            Remove any file types your platform cannot handle
          */
          acceptedFileTypes: [
            "png",
            "pdf_standard",
            "jpg",
            "gif",
            "svg",
            "video",
            "pptx",
          ],
        },
      };
    };
    ```
  </Tab>

  <Tab name="index.css">
    ```css
    .rootWrapper {
      overflow-y: hidden;
    }
    ```
  </Tab>

  <Tab name="index.tsx">
    ```typescript
    // For usage information, see the README.md file.
    import { AppUiProvider } from "@canva/app-ui-kit";
    import { createRoot } from "react-dom/client";
    import { App } from "./app";
    import "@canva/app-ui-kit/styles.css";
    import { AppI18nProvider } from "@canva/app-i18n-kit";
    import type { DesignEditorIntent } from "@canva/intents/design";
    import { prepareDesignEditor } from "@canva/intents/design";

    async function render() {
      const root = createRoot(document.getElementById("root") as Element);

      root.render(
        <AppI18nProvider>
          <AppUiProvider>
            <App />
          </AppUiProvider>
        </AppI18nProvider>,
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
    # Digital asset management

    Demonstrates how to integrate with external digital asset management systems using SearchableListView. Shows patterns for browsing, searching, and importing assets from third-party platforms while supporting design export.

    For API reference docs and instructions on running this example, see: <https://www.canva.dev/docs/apps/examples/digital-asset-management/>.

    This example requires a backend with a valid `CANVA_APP_ID` configured in the root `.env` file. See [Running an example's backend](../../../README.md#running-an-examples-backend) for setup instructions.

    Related examples: See asset_upload for direct asset upload patterns, or content_replacement examples for asset substitution workflows.

    NOTE: This example differs from what is expected for public apps to pass a Canva review:

    - **Static assets**: Mock image URLs from Pexels are used for demonstration. Production apps should use proper CDN/hosting services and implement the `upload` function from `@canva/asset` package for uploading assets to Canva
    - **Authentication and API integration**: Mock data and placeholder functions are used. Production apps must implement proper user authentication, secure API integration with external platforms, and comply with third-party service terms of service
    - **Error handling**: Simplified error handling is used for demonstration. Production apps must implement comprehensive error handling with clear user feedback, proper logging, and graceful failure modes
    - **CORS configuration**: The example uses permissive CORS settings (`cors()` with no restrictions). Production apps must implement proper CORS policies restricting origins to specific app domains
    - **Console logging**: ESLint rule `no-console` is disabled for debugging purposes. Production apps should replace console statements with proper logging solutions and avoid disabling linting rules without justification
    - **Localization**: While the example shows basic locale usage, production apps must implement complete internationalization using the `@canva/app-i18n-kit` package to support multiple languages as required for Canva review
    - **Code structure**: The code structure is simplified. Production apps using [intents](https://www.canva.dev/docs/apps/intents/) are recommended to call the prepareDesignEditor function from src/intents/design_editor/index.tsx
    ```
  </Tab>

  <Tab name="SETUP.md">
    ````markdown
    # Setup

    ## Step 1: Set the `APP_ID` environment variable

    1. Get the ID of your app.
       1. Log in to the [Developer Portal](https://www.canva.com/developers/).
       2. Navigate to the [Your apps](https://www.canva.com/developers/apps) page.
       3. Copy the ID from the **App ID** column in the apps table.
    2. Open the starter kit's [.env file](../../.env).
    3. Set the `APP_ID` environment variable to the ID of the app.

    ## Step 2: Run the development servers

    1. Navigate into the starter kit:

       ```bash
       cd canva-apps-sdk-starter-kit
       ```

    1. Run the following command:

       ```bash
       npm start digital_asset_management
       ```

       This will launch one development server for the frontend and backend.

    1. Navigate to your app at `https://www.canva.com/developers/apps`, and click **Preview** to preview the app.

    1. If your app requires authentication with a third party service, continue to Step 3.
       Otherwise, you can make requests to your service via [./backend/server.ts](./backend/server.ts) inside `"/resources/find"`.

    ## Step 3: (optional) Configure ngrok

    If your app requires authentication with a third party service,
    your server needs to be exposed via a publicly available URL, so that Canva can send requests to it. This step explains how to do this with [ngrok](https://ngrok.com/).

    **Note:** ngrok is a useful tool, but it has inherent security risks, such as someone figuring out the URL of your server and accessing proprietary information. Be mindful of the risks, and if you're working as part of an organization, talk to your IT department.
    You must replace ngrok urls with hosted API endpoints for production apps.

    To use ngrok, you'll need to do the following:

    1. Sign up for a ngrok account at <https://ngrok.com/>.
    2. Locate your ngrok [authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
    3. Set an environment variable for your authtoken, using the command line. Replace `<YOUR_AUTH_TOKEN>` with your actual ngrok authtoken:

       For macOS and Linux:

       ```bash
       export NGROK_AUTHTOKEN=<YOUR_AUTH_TOKEN>
       ```

       For Windows PowerShell:

       ```shell
       $Env:NGROK_AUTHTOKEN = "<YOUR_AUTH_TOKEN>"
       ```

    This environment variable is available for the current terminal session, so the command must be re-run for each new session. Alternatively, you can add the variable to your terminal's default parameters.

    ## Step 4: Run the development server with ngrok and add authentication to the app

    These steps demonstrate how to start the local development server with ngrok.

    From the `canva-apps-sdk-starter-kit` directory

    1. Stop any running scripts, and run the following command to launch the backend and frontend development servers. The `--ngrok` parameter exposes the backend server via a publicly accessible URL.

       ```bash
       npm start digital_asset_management --ngrok
       ```

    2. After ngrok is running, copy your ngrok URL
       (e.g. <https://0000-0000.ngrok-free.app>) to the clipboard.
       1. Go to your app in the [Developer Portal](https://www.canva.com/developers/apps).
       2. Navigate to the "Add authentication" section of your app.
       3. Check "This app requires authentication"
       4. In the "Redirect URL" text box, enter your ngrok URL followed by `/redirect-url` e.g.
          <https://0000-0000.ngrok-free.app/redirect-url>
       5. In the "Authentication base URL" text box, enter your ngrok URL followed by `/` e.g.
          <https://0000-0000.ngrok-free.app/>
          Note: Your ngrok URL changes each time you restart ngrok. Keep these fields up to
          date to ensure your example authentication step will run.

    3. Make sure the app is authenticating users by making the following changes:
       1. Replace

          `router.post("/resources/find", async (req, res) => {`

          with

          `router.post("/api/resources/find", async (req, res) => {`

          in [./backend/server.ts](./backend/server.ts). Adding `/api/` to the route ensures
          the JWT middleware authenticates requests.

       2. Replace

          ``const url = new URL(`${BACKEND_HOST}/resources/find`);``

          with

          ``const url = new URL(`${BACKEND_HOST}/api/resources/find`);``

          in [./adapter.ts](./adapter.ts)

       3. Comment out these lines in [./app.tsx](./app.tsx)

          ```typescript
          // Comment this next line out for production apps
          setAuthState("authenticated");
          ```

    4. Navigate to your app at `https://www.canva.com/developers/apps`, and click **Preview** to preview the app.
       1. A new screen will appear asking if you want to authenticate.
          Press **Connect** to start the authentication flow.
       2. A ngrok screen may appear. If it does, select **Visit Site**
       3. An authentication popup will appear. For the username, enter `username`, and
          for the password enter `password`.
       4. If successful, you will be redirected back to your app.

    5. You can now modify the `/redirect-url` function in `server.ts` to authenticate with your third-party
       asset manager, and `/api/resources/find` to pull assets from your third-party asset manager.

       See `https://www.canva.dev/docs/apps/authenticating-users/` for more details.
    ````
  </Tab>
</Tabs>

## API reference

* [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/)
* [`auth.getCanvaUserToken`](https://www.canva.dev/docs/apps/api/latest/user-auth-get-canva-user-token/)
* [`prepareDesignEditor`](https://www.canva.dev/docs/apps/api/latest/intents-design-prepare-design-editor/)
* [`user.verifyToken`](https://www.canva.dev/docs/apps/api/preview/app-middleware-express-user-verify-token/)

## Need help?

* Join our [Community Forum](https://community.canva.dev/)
* Report issues with this example on [GitHub](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/issues)
