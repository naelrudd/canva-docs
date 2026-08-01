Source: https://www.canva.dev/docs/scim/authentication/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/scim/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

To authenticate to the Canva SCIM API, your client requests must provide a `Bearer` token in the `Authorization` header.

## Generate an access token

Generate the access token from your team's settings in your Canva account. Only team administrators and owners of Canva for Teams or Canva for Education have access to generate a SCIM access token.

1. Log in to your Canva account.

2. Click the gear icon to go to your [Account settings](https://www.canva.com/settings/your-account).

3. In the side menu, under your team's settings, click **SSO & provisioning**.

4. Under **SCIM**, select **Enable SCIM user provisioning**.

   NOTE: Each time the slider is toggled, the current access token is revoked and a new token is created.

5. Copy the access token.

The SCIM access token is unique to your Canva team, and there's only a single access token active at any one time. It is a long-lived token, so make sure it's stored securely.
