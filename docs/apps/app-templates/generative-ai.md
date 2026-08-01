Source: https://www.canva.dev/docs/apps/app-templates/generative-ai/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Generative AI app

Create a generative AI app on Canva with a focus on user experience



You can build a generative AI app quickly using Canva's Generative AI template, which is available through the [@canva/cli](https://www.npmjs.com/package/@canva/cli) command-line interface (CLI).

The Generative AI template is a starting point for implementing the [design editor intent](https://www.canva.dev/docs/apps/intents/design-editor/) to build an AI app, and helps you get started with setting up a user interface (UI). The template doesn't connect to an AI service, but provides an image generation mock-up UI, which lets you explore the UI without a potentially lengthy AI integration step.

This article shows you how to install the Generative AI template, run it locally, and customize it.

## Step 1: Create a new app using the Generative AI template

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

4. Use the following command to create a new app using the Generative AI template:

   ```shell
   canva apps create --template "gen_ai"
   ```

5. The setup process guides you through the remaining settings:
   1. Choose the [audience](https://www.canva.dev/docs/apps/quickstart/#public-vs-team-apps) for your app.
   2. Enter a name for your app.
   3. Choose whether to initialize a git repository for your project.
   4. Choose whether your project should use npm to install its dependencies.

After the setup process has completed, the output lists the steps for running the new app. For example:

```shell
cd example-gen-ai-app
npm start
```

* Replace `example-gen-ai-app` with your app's name.

## Step 2: Preview your app

You can now start the app preview to explore the UI.

1. In the root directory for your app, start the app preview with the following command:

   ```shell
   npm start
   ```

   After the app has started, the `Development URL (Frontend)` and `Base URL (Backend)` local addresses are shown in the output.

2. In [Your apps](https://www.canva.com/developers/apps), select your app, then **Code upload > App source > Development URL**.

3. Under **Code upload > App source > Development URL** confirm that the `the Development URL (Frontend)` address matches the address shown in the *Development URL* field.

4. Locate the **Preview** button in the top right of the page, and click it to open a new tab that loads the Canva editor with a preview of your app.

5. Click **Open** if prompted. This message only appears when using an app for the first time.

## Step 3: Understand the AI user experience

With the Generative AI app running locally, you can explore the overall user experience. The following list explains some of the essential user experience features and components that you can build on:

* **Word filtering**: An obscenity filter provides basic restrictions against potentially offensive or harmful inputs.
* **Loading states**: Since generating AI assets and media can take some time to load, providing placeholders, waiting time messages, and a progress bar communicates the request status to users.
* **Thumbnails previews**: Providing thumbnails means your app gives faster visual feedback, and contributes to reducing load time.
* **A credit system**: The demo credit system allows for users to make some free requests before they need to log in and purchase more credits to continue generating assets.
* **State management**: React Context manages state changes for the example app user experience. For apps that need more complex state management, a more comprehensive library is recommended.
* **Routing**: React Router provides routing and navigation for the example app.

Test out the Generative AI app by entering a prompt, pressing the **Generate image** button, and observing how the user experience essentials work together.

## Step 4: Customize your app

### Change the displayed text

This procedure explains how to change the text displayed in the app's [`FormField`](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/docs/components-form-form-field--docs) component:

1. Open the `src/app.messages.ts` file.

2. Change the contents of `AppMessages`, adjusting the text strings:

   ```typescript
   export const AppMessages = {
     .../* Some lines omitted */
     /** Messages related to prompts and user input validation. */
     promptInspireMe: () => "Try some image inspiration prompts",
     promptTryAnother: () => "Try another",
     promptLabel: () => "Describe the image you want to create",
     promptPlaceholder: () => "Enter at least five words to describe your image.",
     promptMissingErrorMessage: () => "Please describe what you want to create",
     promptNoCreditsRemaining: () => "No credits remaining .",
     promptObscenityErrorMessage: () =>
       "Something you typed may result in content that doesn't meet our policies.",
   ```

3. At the top of the app panel, click **↻** to reload the app.

### Modify the loading state time

This procedure explains how to adjust the timing and loading state set with the app [`Progress Bar`](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/docs/components-progress-progress-bar--docs) component.

1. Open the `src/components/loading_results.tsx` file.

2. Modify the interval duration values:

   ```typescript
   const INTERVAL_DURATION_IN_MS = 500;
   const TOTAL_PROGRESS_PERCENTAGE = 100;
   const LOADING_THRESHOLD_IN_SECONDS = 1;
   ```

3. At the top of the app panel, click **↻** to reload the app.

### Adjust the default inspiration prompts

This procedure explains how to adjust the default set of inspiration prompts:

1. Open the `src/components/prompt_input.tsx` file.

2. Adjust the `examplePrompts` strings:

   ```typescript
   /* Some lines omitted */
   const examplePrompts: string[] = [
     "Cats ruling a parallel universe",
     "Futuristic city with friendly robots",
     "Magical forest with unicorns and dragons",
     "Underwater kingdom with colorful fish and mermaids",
   ```

### Modify the image generation mock-up

The image generation mock-up works by returning the same image set in response to each prompt. This procedure explains how to modify the app's image set. Note that to set up an AI integration and connect to an API, you can modify `backend/routers/image.ts` as a starting point.

1. Open the `backend/routers/image.ts` file.

2. Modify the `imageUrls` list values:

   ```typescript
   /* Some lines omitted */
   // In a real-world scenario, these URLs would point to dynamically generated images.
   const imageUrls: ImageResponse[] = [
     {
       fullsize: {
         width: 1280,
         height: 853,
         url: "https://cdn.pixabay.com/photo/2023/02/03/05/11/youtube-background-7764170_1280.jpg",
       },
       thumbnail: {
         width: 640,
         height: 427,
         url: "https://cdn.pixabay.com/photo/2023/02/03/05/11/youtube-background-7764170_640.jpg",
       },
     },
   ```

## Step 5: Connect to a backend

Since the Generative AI app uses an Express server as a sample backend, when moving to production, it's recommended to change the Express server to a higher capacity production backend. See [Using a backend](https://www.canva.dev/docs/apps/using-backend/) for more information.

## Step 6: Add user authentication

To add [user authentication](https://www.canva.dev/docs/apps/authenticating-users/), you can use frictionless or OAuth authentication methods:

* **Frictionless**: Add App ID and JWT verification middleware to your app. This approach uses the `auth.getCanvaUserToken()` method to receive a JWT. For more information, see [JSON Web Tokens](https://www.canva.dev/docs/apps/verifying-jwts/). For an example, see the [authentication example](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/tree/main/examples/fundamentals/authentication) in the [`canva-apps-sdk-starter-kit`](https://github.com/canva-sdks/canva-apps-sdk-starter-kit) repository.
* **OAuth**: Alternatively, you can configure your app to use [OAuth authentication](https://www.canva.dev/docs/apps/authenticating-users/oauth/) through a third-party service.

## Next steps

* To dive deeper into building and customizing design editor apps, explore the [design editor intent](https://www.canva.dev/docs/apps/intents/design-editor/) documentation.
* When your app is ready, you can submit it for review through the Developer Portal. For more information, see [Submitting apps](https://www.canva.dev/docs/apps/submitting-apps/).
