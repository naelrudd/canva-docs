Source: https://www.canva.dev/docs/apps/app-templates/data-connector/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Connector app

Create a data connector app on Canva that imports data from external sources.

You can build a Data Connector app quickly using Canva's Data Connector template, available through the [@canva/cli](https://www.npmjs.com/package/@canva/cli) command-line interface (CLI).

The Data Connector template is a starting point for building an app that lets users import data from external sources into Canva. The template provides a working example that demonstrates how to implement the [Data Connector intent](https://www.canva.dev/docs/apps/intents/data-connector/) to authenticate, select a data source, configure queries, and return data in a table format for use in Canva designs.

This article shows you how to install the Data Connector template, run it locally, and customize it for your own data sources.

## Step 1: Create a new app using the Data Connector template

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

4. Use the following command to create a new app using the Data Connector template:

   ```shell
   canva apps create --template "data_connector"
   ```

5. The setup process guides you through the remaining settings:
   1. Choose the [audience](https://www.canva.dev/docs/apps/quickstart/#public-vs-team-apps) for your app.
   2. Enter a name for your app.
   3. Choose whether to initialize a git repository for your project.
   4. Choose whether your project should use npm to install its dependencies.

After the setup process has completed, the output lists the steps for running the new app. For example:

```shell
cd example-data-connector-app
npm start
```

* Replace `example-data-connector-app` with your app's name.

## Step 2: Set up authentication

Set up the Canva Connect API authentication as described in the generated README. This ensures your app data source can connect to Canva and function correctly during preview.

## Step 3: Preview your app

You can now start the app preview to explore the UI.

1. In the root directory for your app, start the app preview with the following command:

   ```shell
   npm start
   ```

   After the app has started, the `Development URL (Frontend)` and `Base URL (Backend)` local addresses are shown in the output.

2. In [Your apps](https://www.canva.com/developers/apps), select your app, then **Code upload > App source > Development URL**.

3. Under **Code upload > App source > Development URL** confirm that the `Development URL (Frontend)` address matches the address shown in the *Development URL* field.

4. Locate the **Preview** button in the top right of the page, and click it to open a new tab that loads the Canva editor with a preview of your app.

5. Click **Open** if prompted. This message only appears when using an app for the first time.

## Step 4: Understand the Data Connector user experience

With the Data Connector app running locally, you can explore the overall user experience. The template demonstrates:

* **Data source selection**: Users can browse and select from available data sources (for example, designs, brand templates, or your own API).
* **Configurable queries**: Users can apply filters, search criteria, or sort options to refine the data they want to import.
* **Tabular data import**: The app fetches data from the external source and returns it as a table, ready to be used in Canva.
* **State management**: The template uses React Context for state management. For more complex apps, you may consider libraries like Redux or MobX.
* **Routing**: React Router is integrated to manage multiple views or pages, such as list/detail flows for data sources.
* **App UI Kit**: The template uses the [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/) for a consistent Canva look and feel. This helps you comply with [design guidelines](https://www.canva.dev/docs/apps/design-guidelines/).

Test out the Data Connector app by selecting a data source, configuring your query, and importing data. Observe how the UI guides the user through each step.

## Step 5: Customize your app

### Change data source labels and configuration

To change the labels, filters, or configuration options for your data sources:

1. Open the `src/api/data_sources/` directory.
2. Edit or add data source files to define new sources, filters, or display columns.
3. Update the UI components to reflect your data source options.

### Edit data table columns and formatting

To customize the columns and formatting of the imported data table:

1. Open the relevant data source handler (see `src/api/data_source.ts`).
2. Adjust the logic for mapping API responses to data table columns and cell types (string, number, date, boolean, media, and so on).
3. Use column configs to set column names and types for the table returned to Canva.

### Modify authentication and API integration

The template demonstrates OAuth authentication with the Canva Connect API, but you can adapt it for your own API:

1. Update `src/api/oauth.ts` to set the correct OAuth scopes and endpoints for your API.
2. Adjust API calls in your data source handlers to fetch data from your chosen external system.

### Handle data size limits and errors

* Use the `limit` parameter in the selection UI and data fetching logic to respect Canva's [data size constraints](https://www.canva.dev/docs/apps/intents/data-connector/implementation-guide/#step-8-handle-data-size-limits).
* Implement error handling for authentication, network, and data issues, returning the appropriate status (`completed`, `app_error`, `remote_request_failed`, or `outdated_source_ref`).

### UI and state management

* Update UI components in `src/components/` to change the look and feel, add new fields, or improve the user experience.
* Use React Context or your preferred state management solution for complex flows.
* Add or modify routes using React Router for multi-step or multi-source flows.

## Next steps

* To dive deeper into building and customizing Data Connector apps, explore the [Data Connector intent](https://www.canva.dev/docs/apps/intents/data-connector/) documentation.
* When your app is ready, you can submit it for review through the Developer Portal. For more information, see the [guide on submitting apps](https://www.canva.dev/docs/apps/submitting-apps/).
