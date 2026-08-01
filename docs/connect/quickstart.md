Source: https://www.canva.dev/docs/connect/quickstart/

# Quickstart

How to integrate an app with Canva, using the Connect APIs.

To help you get started with the Connect APIs, Canva has created an [example app in a GitHub repository](https://github.com/canva-sdks/canva-connect-api-starter-kit) that demonstrates some of the main features.

This guide shows you how to clone the repository, configure the app, and run it locally on your machine. You can then review the source code to understand how its features work.

## Prerequisites

To follow this guide, you'll need to:

* Sign up for a [Canva](https://www.canva.com/) account.
* Set up [Multi-Factor Authentication (MFA)](https://www.canva.com/help/login-verification/) on your Canva account.
* Install git, Node.js `v24`, and npm `v11`.

To make sure you're running the correct version of Node.js, we recommend using a version manager like [nvm](https://github.com/nvm-sh/nvm#intro). The [.nvmrc](https://github.com/canva-sdks/canva-connect-api-starter-kit/blob/main/.nvmrc) file in the repository's root directory will ensure the correct version is used when you run `nvm install`.

## Step 1: Create a Canva integration

Create a new integration:

1. Log in to the [Developer Portal](https://www.canva.com/developers/).
2. Navigate to the [Your integrations](https://www.canva.com/developers/integrations) page.
3. Click **Create an integration**.
4. Select the type of integration you want to create:
   * **Public**: Public integrations are available to all Canva users, but the integration must first be reviewed by Canva and meet the [integration requirements](https://www.canva.dev/docs/connect/submission-checklist/).
   * **Private**: Private integrations can only be used by your team on a [Canva Enterprise](https://www.canva.com/enterprise/) plan.
5. Select the checkbox to agree to the [Canva Developer Terms](https://www.canva.com/policies/canva-developer-terms/).
6. Click **Create integration**.

## Step 2: Configure your Canva integration

Configure the integration's scope, secret, and authentication settings:

1. Under **Configuration** → **Configure your integration**, set the following values:
   * **Integration name**: Add a name.
   * **Client ID**: Make a note of this value; you'll need it in a later step.
   * **Generate secret**. Click this and save the secret in a secure location, because you'll need it for a later step and won't be able to retrieve it then.

2. Under **Scopes** → **Set the scopes**, check the following boxes:
   * **design:content**: Read and Write.
   * **design:meta**: Read.
   * **asset**: Read and Write.
   * **brandtemplate:meta**: Read.
   * **brandtemplate:content**: Read.
   * **profile**: Read.

3. Under **Authentication** → **Add Authentication**, locate **URL 1** and enter the following value:

   ```
   http://127.0.0.1:3001/oauth/redirect
   ```

4. In **Return navigation**, enable the **Enable return navigation** switch, and enter the following value for **Return URL**:

   ```
   http://127.0.0.1:3001/return-nav
   ```

## Step 3: Clone the repository

Clone the example repository to your local machine:

```bash
git clone https://github.com/canva-sdks/canva-connect-api-starter-kit.git
```

## Step 4: Install dependencies

Install the dependencies in the repository root:

```bash
cd canva-connect-api-starter-kit
npm install
```

## Step 5: Configure the env file

Add your integration settings to the `demos/ecommerce_shop/.env` file. For example, you can use `code` from the command line to open the file in Visual Studio Code:

```bash
cd demos/ecommerce_shop
code .env
```

Update the following values:

* `CANVA_CLIENT_ID`: This is the client ID from Step 2.
* `CANVA_CLIENT_SECRET`: This is the client secret you generated in Step 2. You can generate a new one if you no longer have it.

For China:
  - `BASE_CANVA_CONNECT_API_URL`: Use `https://api.canva.cn/rest`.
  - `BASE_CANVA_CONNECT_AUTH_URL`: Use `https://www.canva.cn/api`.

## Step 6: Run the app

In the `demos/ecommerce_shop` directory, run the following command to start the app locally on your machine:

```bash
npm start
```

## Step 7: View the app

With the app running locally on your machine, you can now authorize the app to access your Canva account using OAuth:

1. Use your browser to access the app at [http://127.0.0.1:3000](http://127.0.0.1:3000). Don't use `localhost:3000`, as you might get CORS errors.
2. Click the **Connect to Canva** button and follow the prompts in the popup window.
3. Navigate through the app to view your Canva resources.

## Step 8 (Optional): Setup the Canva Dev MCP Server

If you're using AI coding tools, such as Cursor or Claude Code, you can connect to the Canva Dev MCP Server to supercharge your development workflow. See this [setup guide](https://www.canva.dev/docs/connect/mcp-server/) to get started.

## Optional: Generate a client SDK

The Connect API's OpenAPI description is publicly available at [https://www.canva.dev/sources/connect/api/latest/api.yml](https://www.canva.dev/sources/connect/api/latest/api.yml).

You can use this description to generate a client SDK in your preferred language, using a code generation library like [openapi-generator](https://github.com/OpenAPITools/openapi-generator).

### TypeScript SDK

This example uses [openapi-ts](https://www.npmjs.com/package/@hey-api/openapi-ts) to generate the TypeScript SDK in [client/ts](https://github.com/canva-sdks/canva-connect-api-starter-kit/tree/main/client/ts).

To regenerate the types, run the following command from the repository root:

```bash
npm run generate
```

## Next steps

* Learn how to [generate dynamic designs](https://www.canva.dev/docs/connect/autofill-guide/), using Brand template and the Autofill APIs.
* Learn about [security practices](https://www.canva.dev/docs/connect/guidelines/security/) for the Connect APIs.
