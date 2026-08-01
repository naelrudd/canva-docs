Source: https://www.canva.dev/docs/connect/creating-integrations/

# Creating integrations

How to create and configure an integration.

To get started integrating into Canva, you must create and configure an integration on the Canva [Developer Portal](https://www.canva.com/developers/).

Your Canva account must have [Multi-factor Authentication (MFA)](https://www.canva.com/help/login-verification/) enabled before you can create an integration.

## Step 1: Create an integration

1. Log in to the [Developer Portal](https://www.canva.com/developers/).
2. Navigate to the [Your integrations](https://www.canva.com/developers/integrations) page.
3. Click **Create an integration**.
4. Select the type of integration you want to create:
   * **Public**: Public integrations are available to all Canva users, but the integration must first be reviewed by Canva and meet the [integration requirements](https://www.canva.dev/docs/connect/submission-checklist/).
   * **Private**: Private integrations can only be used by your team on a [Canva Enterprise](https://www.canva.com/enterprise/) plan.
5. Select the checkbox to agree to the [Canva Developer Terms](https://www.canva.com/policies/canva-developer-terms/).
6. Click **Create integration**.

## Step 2: Set a name and get credentials

1. On the **Configure your integration** page, set a name for your integration.
   This name is how users identify your integration, for example when going through the authorization process.
2. Under **Credentials**, copy and save the value for your **Client ID**.
3. Click the **Generate secret** button, and save the generated **Client secret** value in a secure location.
   NOTE: Make sure you save the client secret, as you won't be able to view it again.

## Step 3: Set scopes

Scopes define the access permissions that your integration needs for a user's account.

1. In the left menu, navigate to **Scopes**.
2. Under **Reading and writing**, select the scopes that your integration needs when acting on a user's behalf.
3. If you want your integration to receive webhook notifications from Canva, under **Notifications** enable **Enable collaboration:event**.
   1. In the **Webhook URL** field, enter the URL that will receive the webhook notifications.

## Step 4: Set a redirect URL

The Canva Connect APIs use the OAuth 2.0 Authorization Code flow with Proof Key for Code Exchange (PKCE) for user authorization.

1. In the left menu, navigate to **Authentication**.
2. Under **Authorized redirects**, add at least one redirect URL. If required, you can add up to 10 redirect URLs.
   For local development, you can add `http://127.0.0.1:<port>` as a redirect URL (`localhost` isn't allowed).

## Next steps

Learn fundamentals for the Connect APIs, including:
* Handling [authorization and authentication](https://www.canva.dev/docs/connect/authentication/).
* How [API versions](https://www.canva.dev/docs/connect/versions/) work.
* [Security recommendations](https://www.canva.dev/docs/connect/guidelines/security/).
* Key [Canva-specific concepts](https://www.canva.dev/docs/connect/canva-concepts/).
