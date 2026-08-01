Source: https://www.canva.dev/docs/apps/app-templates/digital-asset-management/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Digital Asset Management app

Retrieve content from a backend and make it available to a Canva app.



You can build a digital asset management (DAM) app that retrieves content from a [backend](https://www.canva.dev/docs/apps/using-backend/#why-use-a-backend) and makes it available to a Canva app.

To help you get started, Canva has created a template DAM app that implements the [design editor intent](https://www.canva.dev/docs/apps/intents/design-editor/), which you can install and customize.

This article shows you how to install the DAM app template, run it locally on your machine, and start adding customizations.

## Step 1: Create a new app using the DAM app template

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

4. Use the following command to create a new app using the DAM template:

   ```shell
   canva apps create --template "dam"
   ```

5. The setup process guides you through the remaining settings:
   1. Choose the [audience](https://www.canva.dev/docs/apps/quickstart/#public-vs-team-apps) for your app.
   2. Enter a name for your app.
   3. Choose whether to initialize a git repository for your project.
   4. Choose whether your project should use npm to install its dependencies.

After the setup process has completed, the output lists the steps for running the new app. For example:

```shell
cd example-dam-app
npm start
```

* Replace `example-dam-app` with your app's name.

## Step 2: Preview your app

Run the app locally to see a preview.

1. Navigate to your app's directory and start the app. The `example-dam-app` directory name will vary based on your app's name.

   ```shell
   cd example-dam-app
   npm start
   ```

   After the app starts, the `Development URL (Frontend)` and `Base URL (Backend)` local addresses are shown in the output.

2. In [Your apps](https://www.canva.com/developers/apps), select your app, then **Code upload > App source > Development URL**.

3. Under **Code upload > App source > Development URL** confirm that the `the Development URL (Frontend)` address matches the address shown in the *Development URL* field.

4. Locate the **Preview** button in the top right of the page, and click it to open a new tab that loads the Canva editor, with a preview of your app in the sidebar.

5. Click **Open** if prompted. This message only appears when using an app for the first time.

## Step 3: Customize the DAM app

The DAM app template should now be running locally. In the preview, you can see tabs called *All*, *Collection*, and *Assets*. This procedure demonstrates how to rename a tab.

<Note>
  To customize the view, container type, layout, search, and more, see the [SearchableListView](https://www.canva.dev/docs/apps/app-templates/storybook/?path=/docs/app-components-searchable-list-view-searchablelistview--docs) component.
</Note>

1. In your IDE, open the `src/config.ts` file and change `label: "Folders",` to `label: "My Folders",`

   ```tsx
   containerTypes: [
      {
         value: "folder",
         label: "Folders",
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
         placeholder: "Search for resources inside this folder",
         },
      },
   ],
   ```

2. Save the changes to `config.ts`.

3. Click **↻** to reload the app. The renamed tab should now be visible in the preview.



## Step 4: Connect to a backend

To retrieve digital assets, connect the app to your backend. For more information, see [Using a backend](https://www.canva.dev/docs/apps/using-backend/).

## Step 5: Add user authentication

Update your app to add [user authentication](https://www.canva.dev/docs/apps/authenticating-users/). You can use frictionless or OAuth authentication:

* **Frictionless**: To implement frictionless authentication, add App ID and JWT verification middleware to your app. This approach uses the `auth.getCanvaUserToken()` method to receive a JWT. For more information, see [JSON Web Tokens](https://www.canva.dev/docs/apps/verifying-jwts/). For an example, see the [authentication example](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/tree/main/examples/fundamentals/authentication) in the `canva-apps-sdk-starter-kit` repository.
* **OAuth**: Alternatively, you can configure your app to use [OAuth authentication](https://www.canva.dev/docs/apps/authenticating-users/oauth/) through a third-party service.

## Localization

To localize this template for all [supported locales](https://www.canva.dev/docs/apps/localization/#supported-locales):

1. Ensure that the app has otherwise been localized in accordance with the [recommended localization workflow](https://www.canva.dev/docs/apps/localization/recommended-workflow/).
2. Use the latest version of the `@canva/app-components` package.

The literal strings in the `SearchableListView` component will be localized automatically as long as your app follows the localization workflow and uses the latest version of `@canva/app-components`.

## Next steps

* To dive deeper into building and customizing design editor apps, explore the [design editor intent](https://www.canva.dev/docs/apps/intents/design-editor/) documentation.
* When your app is ready, you can submit it for review through the Developer Portal. For more information, see [Submitting apps](https://www.canva.dev/docs/apps/submitting-apps/).
