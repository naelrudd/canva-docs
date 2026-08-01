Source: https://www.canva.dev/docs/apps/authenticating-users/frictionless/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Frictionless authentication

Seamlessly authenticate users.

Frictionless authentication is when you use the [`auth.getCanvaUserToken` method](https://www.canva.dev/docs/apps/api/latest/user-auth-get-canva-user-token/) to retain a user's data without them having to sign-in through a login screen. With this, you can do away with traditional, manual authentication entirely or delay it until a user tests your app to see the value it provides.

## User tokens

Using the [`auth.getCanvaUserToken` method](https://www.canva.dev/docs/apps/api/latest/user-auth-get-canva-user-token/) you can:

* Retrieve a token that uniquely identifies the Canva user and their associated brand
* Store the user ID on your end
* Learn about how your users use your app.

We've seen that if a user experiences most of an app's features, they're less likely to abandon the flow than if they're required to authenticate up front.

## High-level workflow

The workflow looks like the following:

1. The user interacts with your app. Canva assigns a unique user ID to the user.
2. You track how the user uses your app. This interaction, as well as the associated user and app ID, is stored in the app backend.
3. Your app backend stores the user ID in a database.

As well as the above, you, as the app developer exploring metrics, can use the stored data to know more about your users, such as:

* Track usage: You can monitor how much a user has used your services in Canva, regardless of whether they have interacted with the design. This is especially useful for AI apps where there's a real cost to serve for running the model. Here, you do all the tracking using the data in your app's backend.
* Track time in app: You can save the date the user initially created their account (When the user token was created), then compare that date to today's date to see how long they've been using your app.

## Prerequisites

Before you begin, review the [Authentication design guidelines](https://www.canva.dev/docs/apps/design-guidelines/authentication/).

## Step 1: Get a JWT for the current user

To implement frictionless authentication, an app needs the ID of the user and their team, which you can get using a JSON Web Token (JWT).

To get a JWT for the current user:

1. Import the `auth` namespace from the `@canva/user` package:

   ```ts
   import { auth } from "@canva/user";
   ```

2. Call the `getCanvaUserToken` method:

   ```ts
   const token = await auth.getCanvaUserToken();
   ```

   This method returns a JWT as a string.

## Step 2: Verify the JWT in your backend

By itself, the JWT is a meaningless string of characters. To get the ID of the user and their team from the JWT, an app must send the JWT to the app's backend then verify that JWT.

To send the JWT to the app's backend, use the Fetch API, or a library such as [axios](https://github.com/axios/axios):

```ts
const response = await fetch("http://localhost:3001/my/api/endpoint", {
  headers: {
    Authorization: `Bearer ${token}`,
  },
});
```

When sending the request, include an `Authorization` header that contains the word `Bearer` and the JWT, separated by a space.

To verify the JWT, you can either use the `@canva/app-middleware` package (recommended), or manually implement your own verification.

### Recommended: Using @canva/app-middleware

For Node.js backends, we recommend using the [`@canva/app-middleware`](https://www.npmjs.com/package/@canva/app-middleware) package to automatically verify JWTs:

#### Express.js middleware

```typescript
import express from "express";
import { user } from "@canva/app-middleware/express";

const app = express();

// Apply middleware to verify all requests
app.use("/my/api", user.verifyToken({ appId: process.env.CANVA_APP_ID }));

app.post("/my/api/endpoint", (req, res) => {
  // Access verified user information
  const { userId, brandId } = req.canva.user;

  // Your application logic here

  res.sendStatus(200);
});

app.listen(process.env.PORT || 3000);
```

For more information, see [`user.verifyToken`](/docs/apps/api/preview/app-middleware-express-user-verify-token/).

#### Framework-agnostic approach

For other Node.js environments:

### Alternative: Manual verification

For non-Node.js backends, follow the steps in [JSON Web Tokens](https://www.canva.dev/docs/apps/verifying-jwts/) to manually verify the JWT. If the JWT is valid, you will have an object that contains the ID of the user and their team.

## Step 3: Associate data with the user

When the user opens the app for the first time, use the ID of the user and their team to create a user record in the backend's database. This is essentially a registration process, except that it's invisible to the user — an account is created for them in the app's backend when all they've done is access the app.

As the user interacts with the app, or when they return to the app at a later time, send additional HTTP requests to create, read, or update data associated with their account. With each request, the app will need to send and verify a JWT to get the ID of the user and their team.

## Step 4: Handle disconnections

**Tip:** Review Canva's design guidelines for [handling app disconnections and reconnections](https://www.canva.dev/docs/apps/design-guidelines/authentication/#handle-disconnections).

After a user disconnects (uninstalls) an app, you should remove any persisted data associated with their account. This ensures that if they reinstall the app later, they'll start with a fresh state.

To handle disconnections, you must configure a webhook URL in the Developer Portal. This URL will receive a `POST` request from Canva when a user disconnects your app.

### Configure the user uninstall webhook URL

1. Log in to the [Developer Portal](https://www.canva.com/developers).
2. Navigate to your app's settings.
3. Go to the **Webhooks** section.
4. Add a new webhook URL for **User uninstalls**.

### Handle the webhook and remove data

When a user disconnects your app, Canva sends a `POST` request to your webhook URL. The request includes an `Authorization` header containing a JWT that identifies the user:

```
Authorization: Bearer <jwt>
```

When your backend receives the webhook:

1. Extract the JWT from the `Authorization` header.
2. [Verify the JWT](https://www.canva.dev/docs/apps/verifying-jwts/) to get the ID of the user and their team.
3. Use the user and team IDs to find and remove any persisted data associated with the user, such as:
   * Usage history
   * Saved preferences
   * Generated content
   * Any other user-specific data

Respond to the webhook with a `200` status code and the following object to acknowledge receipt:

```json
{
  "type": "SUCCESS"
}
```

#### Example webhook implementation

For Node.js backends using Express.js:

```typescript
import express from "express";
import { user } from "@canva/app-middleware/express";

const app = express();

// Apply middleware to verify the webhook JWT
app.use("/webhooks", user.verifyToken({ appId: process.env.CANVA_APP_ID }));

app.post("/webhooks/user-uninstall", async (req, res) => {
  // Get verified user information from the JWT
  const { userId, brandId } = req.canva.user;

  // Remove all data associated with this user
  await removeUserData(userId, brandId);

  // Acknowledge receipt
  res.json({ type: "SUCCESS" });
});

app.listen(3000);
```

For more information, see [`user.verifyToken`](https://www.canva.dev/docs/apps/api/preview/app-middleware-express-user-verify-token/).

### Confirm the disconnection flow works

To confirm that the disconnection flow is working:

1. Navigate through the app and create some data.
2. Disconnect (uninstall) the app.
3. Reconnect (install) the app.

You should see that all previously created data is gone, and the user starts with a fresh state. If the data persists, double-check your disconnection logic.

## API reference

* [`auth.getCanvaUserToken`](https://www.canva.dev/docs/apps/api/latest/user-auth-get-canva-user-token/)
* [`auth.requestAuthentication`](https://www.canva.dev/docs/apps/api/v1/user-auth-request-authentication/)
