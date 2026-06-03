Source: https://www.canva.dev/docs/connect/reference-apps/realty-commercial/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/connect/llms.txt
> Use this file to discover all available pages before exploring further.

# Automate real estate marketing with Canva

Learn how to connect your real estate platform to Canva and automate property marketing workflows

Real estate teams spend hours creating property brochures, social posts, and listing materials. By integrating Canva into your platform using the [Connect API](https://www.canva.dev/docs/connect/), you can automate this process, letting agents generate on-brand marketing materials directly from your application.

AVAILABILITY: This integration uses Brand Templates and Autofill, which require a [Canva Enterprise](https://www.canva.com/enterprise/) subscription. See the [Autofill guide](https://www.canva.dev/docs/connect/autofill-guide/) for details on requesting development access.

This guide walks you through a reference demo that shows these integration patterns in action. You'll see how to connect your platform to Canva, autofill templates with property data, and streamline your marketing workflows.

NOTE: The Realty demo is a reference implementation for learning purposes. Use it to understand the integration patterns you can apply to your own application.

## What you can automate

With the Connect API, your real estate platform can:

* **OAuth authentication:** Securely connect a user's Canva account to your application.
* **Brand templates:** Fetch and display templates from a user's Canva Brand Kit.
* **Autofill:** Automatically populate templates with property data, agent information, and images.
* **Design creation:** Generate Canva designs programmatically from your application.
* **Return navigation:** Allow users to return to your app after editing in Canva.

## Prerequisites

Before starting, ensure you have:

* Node.js v24 or later
* npm v11
* A Canva account (preferably with access to [Canva Enterprise](https://www.canva.com/enterprise/) for Brand Templates and Autofill)

## Step 1: Create an integration

1. Open the [Developer Portal](https://www.canva.com/developers/integrations/connect-api) and click **Create an integration**.

2. Under **Configuration** → **Configure your integration**:

   * Enter a name for your integration.
   * Note the **Client ID** for later.
   * Click **Generate secret** and save the secret securely.

3. Under **Scopes** → **Set the scopes**, enable the following permissions:

   * `asset`: Read and Write
   * `brandtemplate:content`: Read
   * `brandtemplate:meta`: Read
   * `design:content`: Read and Write
   * `design:meta`: Read
   * `profile`: Read

4. Under **Authentication** → **Add Authentication**, set **URL 1** to:

   ```text
   http://127.0.0.1:3001/oauth/redirect
   ```

5. Under **Return navigation**, toggle on **Enable return navigation** and set the **Return Url** to:

   ```text
   http://127.0.0.1:3001/return-nav
   ```

## Step 2: Clone and configure the demo

1. Clone the [Connect API Starter Kit](https://github.com/canva-sdks/canva-connect-api-starter-kit):

   ```shell
   git clone https://github.com/canva-sdks/canva-connect-api-starter-kit.git
   cd canva-connect-api-starter-kit
   ```

2. Install dependencies:

   ```shell
   npm install
   cd demos/realty
   ```

3. Configure your environment variables in the `demos/realty/.env` file:

   * `DATABASE_ENCRYPTION_KEY`: Automatically generated during installation. If missing, run `npm run generate:db-key`.
   * `CANVA_CLIENT_ID`: Your Client ID from Step 1.
   * `CANVA_CLIENT_SECRET`: Your client secret from Step 1.

## Step 3: Set up brand templates

To use the autofill functionality, you need Brand Templates in your Canva account:

1. Open the [sample Brand Template deck](https://www.canva.com/design/DAGGkcb61HQ/OJhMIQrmz2daIoxo8u3T2g/view).
2. Click **Use template** to add the templates to your Canva account.
3. Ensure the templates are saved to your Brand Kit.

## Step 4: Run the demo

1. Start the application:

   ```shell
   npm start
   ```

2. Open [http://127.0.0.1:3000](http://127.0.0.1:3000) in your browser.

WARNING: Access the app using `127.0.0.1:3000`, not `localhost:3000`, to avoid CORS errors.

## Using the demo

1. Click **Connect to Canva** to authenticate with your Canva account.
2. Browse property listings on the **Listings** page.
3. Select a property to create marketing materials.
4. On the **Configure design** page:
   1. Choose a Brand Template.
   2. Select one or more agents (depending on the template).
   3. Select a property.
   4. Click **Generate with Canva**.
5. The app validates the template fields, generates the design using autofill, and displays a preview.
6. Click **Edit in Canva** to open the design in Canva's editor.

## Integration patterns to apply

Use these patterns from the demo as a reference when integrating Canva into your own application.

### Authentication

The demo uses OAuth 2.0 with PKCE for secure authentication. Your backend should handle:

* Generating authorization URLs with code challenges
* Exchanging authorization codes for access tokens
* Securely storing and refreshing tokens

For more information, see [Authentication](https://www.canva.dev/docs/connect/authentication/).

### Autofill

Autofill lets you programmatically populate Brand Template fields with your data. In your application, you would map your own data (such as product details, customer information, or content from your database) to template placeholders.

For more information, see [Autofill guide](https://www.canva.dev/docs/connect/autofill-guide/).

### Return navigation

Return navigation allows users to return to your application after editing a design in Canva. You can use this to update your UI with the edited design or trigger follow-up actions in your workflow.

For more information, see [Return navigation guide](https://www.canva.dev/docs/connect/return-navigation-guide/).

## Next steps

* Explore the [Connect API documentation](https://www.canva.dev/docs/connect/) to learn about additional capabilities.
* Review the [Autofill guide](https://www.canva.dev/docs/connect/autofill-guide/) for detailed information on populating templates.
* Check the [API reference](https://www.canva.dev/docs/connect/api-reference/authentication/generate-access-token/) for endpoint details.
* Submit your integration for review using the [Submission checklist](https://www.canva.dev/docs/connect/submission-checklist/).
