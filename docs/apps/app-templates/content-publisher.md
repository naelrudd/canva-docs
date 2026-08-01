Source: https://www.canva.dev/docs/apps/app-templates/content-publisher/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Content Publisher app

Create a content publishing app that integrates with external platforms.

You can build a content publishing app quickly using Canva's Content Publisher template, which is available through the [@canva/cli](https://www.npmjs.com/package/@canva/cli) command-line interface (CLI).

The Content Publisher template is a starting point for implementing the [Content Publisher intent](https://www.canva.dev/docs/apps/intents/content-publisher/), which enables users to publish Canva designs directly to external platforms like social media, blogs, or newsletters. The template provides a mock publishing flow with settings and preview UIs, allowing you to explore the user experience before integrating with your platform's APIs.

This article shows you how to install the Content Publisher template, run it locally, and customize it.

## Step 1: Create a new app using the Content Publisher template

1. Install the [Canva CLI](https://www.npmjs.com/package/@canva/cli) globally:

   ```shell
   npm install -g @canva/cli@latest
   ```

2. Log in to the Canva CLI. This command opens an access request page in your browser:

   <GlobalContent>
     ```shell
     canva login
     ```
   </GlobalContent>

   <ChinaContent>
     ```shell
     canva login --cn
     ```
   </ChinaContent>

3. Click **Allow** to grant the Canva CLI permission to manage your Canva apps.

4. Use the following command to create a new app using the Content Publisher template:

   ```shell
   canva apps create --template "content_publisher"
   ```

5. The setup process guides you through the remaining settings:
   1. Choose the [audience](https://www.canva.dev/docs/apps/quickstart/#public-vs-team-apps) for your app.
   2. Enter a name for your app.
   3. Choose whether to initialize a git repository for your project.
   4. Choose whether your project should use npm to install its dependencies.

After the setup process has completed, the output lists the steps for running the new app. For example:

```shell
cd example-content-publisher-app
npm start
```

* Replace `example-content-publisher-app` with your app's name.

## Step 2: Preview your app

You can now start the app preview to explore the UI.

1. In the root directory for your app, start the app preview with the following command:

   ```shell
   npm start
   ```

   After the app starts, the `Development URL (Frontend)` local address is shown in the output.

2. In [Your apps](https://www.canva.com/developers/apps), select your app, then **Code upload > App source > Development URL**.

3. Under **Code upload > App source > Development URL** confirm that the `Development URL (Frontend)` address matches the address shown in the *Development URL* field.

4. Locate the **Preview** button at the top right of the page, and click it to open a new tab that loads the Canva editor.

5. Click **Open** if prompted. This message only appears when using an app for the first time.

## Step 3: Understand the Content Publisher user experience

With the Content Publisher app running locally, you can explore the publishing flow. The template implements all 4 required functions of the Content Publisher intent:

* **Settings UI**: A form where users configure publishing options, such as entering a caption. The settings UI validates required fields and enables or disables the publish button accordingly.
* **Preview UI**: A mock social media post preview showing how the content will appear after publishing. This helps users visualize their post before committing.
* **Output type configuration**: Defines the "Feed Post" output type with image specifications, including aspect ratio constraints and file format requirements.
* **Publish handler**: A placeholder function that returns a mock success response. In production, this connects to your platform's APIs.

Test the Content Publisher app by entering a caption in the settings panel, observing the preview update, and clicking the publish button to see the mock response.

## Step 4: Customize your app

### Add additional settings fields

To add more configuration options to the settings UI:

1. Open the `src/intents/content_publisher/types.ts` file.

2. Add new fields to the `PublishSettings` interface:

   ```typescript
   export interface PublishSettings {
     caption: string;
     visibility: "public" | "private";
   }
   ```

3. Open the `src/intents/content_publisher/settings_ui.tsx` file.

4. Update the initial state and add new form controls for the additional fields.

5. Update the `validatePublishRef` function to validate the new fields.

### Customize the preview appearance

To modify the preview to match your platform's design:

1. Open the `src/intents/content_publisher/post_preview.tsx` file.

2. Modify the `PostPreview` component to match your platform's visual style, including colors, layout, and branding elements.

3. Update the `styles/preview_ui.css` file to apply custom styles.

### Configure output types

To modify the supported publishing formats:

1. Open the `src/intents/content_publisher/index.tsx` file.

2. Modify the `getPublishConfiguration` function to define your platform's supported formats:

   ```tsx
   return {
     status: "completed",
     outputTypes: [
       {
         id: "story",
         displayName: intl.formatMessage({
           defaultMessage: "Story",
           description: "Label for story format",
         }),
         mediaSlots: [
           {
             id: "media",
             displayName: "Media",
             fileCount: { exact: 1 },
             accepts: {
               image: {
                 format: "png",
                 aspectRatio: { min: 9 / 16, max: 9 / 16 },
               },
             },
           },
         ],
       },
     ],
   };
   ```

## Step 5: Add user authentication

Most publishing platforms require user authentication to post content. You can use [OAuth authentication](https://www.canva.dev/docs/apps/authenticating-users/oauth/) to connect user accounts:

1. Configure OAuth settings in the [Developer Portal](https://www.canva.com/developers/apps) for your app.
2. Implement the OAuth flow to obtain access tokens for your platform.
3. Store tokens securely and use them when making API calls in the `publishContent` function.

For more information, see [Authenticating users](https://www.canva.dev/docs/apps/authenticating-users/).

## Step 6: Implement platform integration

To complete your content publishing app, replace the placeholder implementation with actual API calls:

1. Open the `src/intents/content_publisher/index.tsx` file.

2. In the `publishContent` function, add your platform's API integration:

   ```tsx
   async function publishContent(
     request: PublishContentRequest,
   ): Promise<PublishContentResponse> {
     // Parse the settings from publishRef
     const settings = JSON.parse(request.publishRef);

     // Upload media to your platform
     // const uploadedMedia = await uploadToYourPlatform(request.outputMedia);

     // Create the post on your platform
     // const post = await createPost({
     //   media: uploadedMedia,
     //   caption: settings.caption,
     // });

     return {
       status: "completed",
       externalId: "your-platform-post-id",
       externalUrl: "https://your-platform.com/post/123",
     };
   }
   ```

3. Update the preview UI in `src/intents/content_publisher/preview_ui.tsx` to fetch and display the authenticated user's profile information.

## Next steps

* To dive deeper into building content publishing apps, explore the [Content Publisher intent](https://www.canva.dev/docs/apps/intents/content-publisher/) documentation.
* Review the [Content Publisher design guidelines](https://www.canva.dev/docs/apps/design-guidelines/content-publisher/) to ensure your app provides a great user experience.
* When your app is ready, you can submit it for review through the Developer Portal. For more information, see the [guide on submitting apps](https://www.canva.dev/docs/apps/submitting-apps/).
