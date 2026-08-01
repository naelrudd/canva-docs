Source: https://www.canva.dev/docs/connect/return-navigation-guide/

# Return navigation guide

Let users move seamlessly between your integration and the Canva editor.

You can use the Connect APIs to let your users move seamlessly between your integration and the Canva editor.

## Workflow

1. Authenticate and authorize the user with Canva's OAuth flow.
2. Query the Connect APIs to get a list of their designs.
3. Display the designs with an *Edit in Canva* button.
4. Redirect the user to the Canva editor.
5. Decode Canva's return URL when the user is ready to return to your integration.
6. Refresh the displayed designs when the user returns.

## Prerequisites

You need an account on https://www.canva.com/developers.

## Configure your integration

### Step 1. Create an integration
Create an integration with at least one redirect url, and at least the `design:read` and `design:meta:read` scopes. Enable return navigation and add a valid return URL.

### Step 2. Authenticate with OAuth
Follow the Authentication guide to get an authorization code, then generate an access token.

## Build your workflow

### Step 1. Get designs
Call the List designs API: `GET /v1/designs`

Each design item contains a `urls` object with `edit_url` and `view_url` properties.

### Step 2. Build your UI
For each design, create a unique `correlation_state` string and append it to the design's `edit_url` as a query parameter.

Requirements for `correlation_state`:
* Must be 50 characters or less.
* Must be URL safe.
* Can contain stringified JSON.

Add an *Edit in Canva* button using the design's edit URL.

### Step 3. Parse the return URL
When the user finishes editing, Canva generates a URL:
```
https://{YOUR_RETURN_URL}?correlation_jwt={CORRELATION_JWT}
```

The `correlation_jwt` is a URL-safe, Base64-encoded JWT containing:
* `aud`: Your integration's Client ID.
* `exp`: Token expiry (1 day).
* `sub`: The User ID.
* `team_id`: The Team ID.
* `type`: Set as `rti`.
* `jti`: Unique identifier.
* `design_id`: The design's ID.
* `correlation_state`: Your original correlation_state string.

Validate the JWT signature against the public keys provided by the keys API.
