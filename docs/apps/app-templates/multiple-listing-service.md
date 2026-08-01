Source: https://www.canva.dev/docs/apps/app-templates/multiple-listing-service/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Multiple Listing Service app

Learn how to build an app that integrates MLS data into Canva



The MLS reference app is a starting point for building an app that lets users browse real estate listings and add the listing information and assets to their designs. It demonstrates how to display a searchable list of properties and handle drag-and-drop interactions.

This article shows you how to set up the MLS reference app, run it locally, and start building your own app.

## Step 1: Create the app

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

4. Use the following command to create a new app using the MLS reference app:

   ```shell
   canva apps create --template="mls"
   ```

5. The setup process guides you through the remaining settings:
   1. Choose any optional configs you want to add to your project.
   2. Choose the [audience](https://www.canva.dev/docs/apps/quickstart/#public-vs-team-apps) for your app.
   3. Enter a name for your app.
   4. Choose whether to initialize a git repository for your project.
   5. Choose whether your project should use npm to install its dependencies.

After the setup process has completed, the output lists the steps for running the new app. For example:

```shell
cd mls-app-solution
npm start
```

* Replace `mls-app-solution` with your app's name.

## Step 2: Preview your app

Run the app locally to see a preview.

1. In your app's root directory, start the app.

   ```shell
   cd mls-app-solution
   npm start
   ```

   After the app starts, the output shows a direct link to preview the app.

2. Click the link in the terminal to open the app in the Canva editor.

3. Click **Open** if prompted. This message only appears when using an app for the first time.

The app should now be running locally. In the preview, choose a property listing and drag the images or text to your design.

## Step 3: Connect to real MLS data

The reference app uses dummy data by default. To build a production app, you need to connect to your MLS provider's data.

Most MLS providers require authentication and shouldn't be accessed directly from the frontend to avoid exposing your API keys. You should set up a backend to proxy requests to the MLS provider.

1. **Set up a backend**: Use the [backend guide](https://www.canva.dev/docs/apps/using-backend/) or your own backend infrastructure.
2. **Fetch data**: Open `src/adapter.ts`. This file contains the logic for fetching listings and agents.
3. Replace the mock data implementation in `fetchListings` with a call to your backend.

   ```ts
   // src/adapter.ts

   export const fetchListings = async (
     office?: Office | null,
     query?: string,
     propertyType?: string | null,
     sortBy?: string | null,
     continuation?: string,
   ): Promise<{ listings: Property[]; continuation?: string }> => {
     const params = new URLSearchParams({ query: query ?? "" });
     // Replace with your backend endpoint
     const response = await fetch(
       `https://api.example.com/listings?${params}`
     );
     return await response.json();
   };
   ```

For more information on backend integration, see [Using a backend](https://www.canva.dev/docs/apps/using-backend/).

## Next steps

* Explore the [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/) to add more components to your app.
* Learn about [Drag and Drop](https://www.canva.dev/docs/apps/supporting-drag-drop/) to improve how users interact with listings.
* Submit your app to the [Canva Apps Marketplace](https://www.canva.dev/docs/apps/submitting-apps/).
