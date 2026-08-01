Source: https://www.canva.dev/docs/apps/app-templates/hello-world/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Hello World app

Create a minimal Canva app as a first example.

The Hello World template is a minimal example app that demonstrates using the [design editor intent](https://www.canva.dev/docs/apps/intents/design-editor/) to implement components and design tokens from the Canva App UI Kit, as well as an Apps SDK API method. You can use it as a base to build your own Canva app.

This article shows you how to install the Hello World template, run it locally, and start building your own app.

## Step 1: Create a new app using the Hello World template

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

4. Use the following command to create a new app using the Hello World template:

   ```shell
   canva apps create --template "hello_world"
   ```

5. The setup process guides you through the remaining settings:
   1. Choose the [audience](https://www.canva.dev/docs/apps/quickstart/#public-vs-team-apps) for your app.
   2. Enter a name for your app.
   3. Choose whether to initialize a git repository for your project.
   4. Choose whether your project should use npm to install its dependencies.

After the setup process has completed, the output lists the steps for running the new app. For example:

```shell
cd example-hello-world-app
npm start
```

* Replace `example-hello-world-app` with your app's name.

## Step 2: Preview your app

Run the app locally to see a preview.

1. In your app's root directory, start the app. The `example-hello-world-app` directory name will vary based on your app's name.

   ```shell
   cd example-hello-world-app
   npm start
   ```

   After the app starts, the `Development URL (Frontend)` and `Base URL (Backend)` local addresses are shown in the output.

2. In [Your apps](https://www.canva.com/developers/apps), select your app, then **Code upload > App source > Development URL**.

3. Under **Code upload > App source > Development URL** confirm that the `Development URL (Frontend)` address matches the address shown in the *Development URL* field.

4. Locate the **Preview** button at the top right of the page, and click it to open a new tab that loads the Canva editor. A preview of your app loads in the sidebar.

5. Click **Open** if prompted. This message only appears when using an app for the first time.

You can now try adding more components, tokens, and methods in the following step, or go to [Step 4](https://www.canva.dev/#step-4-connect-to-a-backend) to set up your app back end.

## Step 3. Customize your app

The app should now be running locally. In the preview, you can see the minimal Canva app. Clicking the **Do something cool** button creates a new text element in the design.

You can customize the app using more UI Kit components, design tokens, and API methods.

The following example customizes the Hello World template by adding the ability to change text color and size in the design. It uses the following:

* A `PaintRollerIcon` from the App UI Kit icon set.
* The `secondary` color design token.
* The `editContent` API method.

1. In your IDE, open the `src/app.tsx` file.

2. Add `PaintRollerIcon` to the `@canva/app-ui-kit` import.

   ```tsx
   import { Button, Rows, Text, PaintRollerIcon } from "@canva/app-ui-kit";
   ```

3. Import the `editContent` method:

   ```tsx
   import { editContent } from "@canva/design";
   ```

4. Add the `editContent` method, and create the following:

   1. A callback with the required `contentType` and `target` properties.
   2. The `session` object, and a `sync` method for managing content change.
   3. A loop to search through the content items in the design using the `readPlaintext` and `formatParagraph` methods:

   ```tsx
   export const App = () => {
     const isSupported = useFeatureSupport();
     const addElement = [addElementAtPoint, addElementAtCursor].find((fn) =>
       isSupported(fn),
     );

     const onClick = () => {
       if (!addElement) {
         return;
       }

       addElement({
         type: "text",
         children: ["Hello world!"],
       });
     };

     async function editOnClick() {
       await editContent(
         {
           contentType: "richtext",
           target: "current_page"
         },
         async (session) => {
           for (const content of session.contents) {
             const plaintext = content.readPlaintext();

             content.formatParagraph(
               { index: 0,
                 length: plaintext.length
               },
               { fontWeight: "bold",
                 fontSize: 30,
                 color: "#008008"
                }
             );
           }
           await session.sync();
         }
       );
     }
   ```

5. Create a new button component after the existing **Do something cool** button, using the `secondary` design variant and adding the `PaintRollerIcon`:

   ```tsx
   <Button variant="secondary" onClick={editOnClick} icon={(() => <PaintRollerIcon />)} stretch>
     {intl.formatMessage({
       defaultMessage: "Change the content",
       description: "Change the color and size of text content in the design when pressed.",
     })}
   </Button>
   ```

When you click on the new button, the text content in the design changes color and size.

## Step 4. Connect to a backend

To add more capabilities to your new app, connect the app to your backend. For more information, see [Using a backend](https://www.canva.dev/docs/apps/using-backend/).

## Step 5. Add user authentication

Update your app to add [user authentication](https://www.canva.dev/docs/apps/authenticating-users/). You can use frictionless or OAuth authentication:

* **Frictionless**: To implement frictionless authentication, add App ID and JWT verification middleware to your app. This approach uses the `auth.getCanvaUserToken()` method to receive a JWT. For more information, see [JSON Web Tokens](https://www.canva.dev/docs/apps/verifying-jwts/). For an example, see the [authentication example](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/tree/main/examples/fundamentals/authentication) in the `canva-apps-sdk-starter-kit` repository.
* **OAuth**: Alternatively, you can configure your app to use [OAuth authentication](https://www.canva.dev/docs/apps/authenticating-users/oauth/) through a third-party service.

## Localization

To localize this template for all [supported locales](https://www.canva.dev/docs/apps/localization/#supported-locales):

1. Ensure that the app has otherwise been localized in accordance with the [recommended localization workflow](https://www.canva.dev/docs/apps/localization/recommended-workflow/).
2. Use the latest version of the `@canva/app-components` package.

Literal strings added to a `SearchableListView` component will be localized automatically as long as your app follows the localization workflow and uses the latest version of `@canva/app-components`.

## Next steps

* To dive deeper into building and customizing design editor apps, explore the [design editor intent](https://www.canva.dev/docs/apps/intents/design-editor/) documentation.
* When your app is ready, you can submit it for review through the Developer Portal. For more information, see [Submitting apps](https://www.canva.dev/docs/apps/submitting-apps/).
