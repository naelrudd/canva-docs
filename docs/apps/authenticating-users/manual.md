Source: https://www.canva.dev/docs/apps/authenticating-users/manual/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Manual authentication

How to set up authentication with a third-party platform.

**Warning:** Manual authentication was removed in Apps SDK v2. You should use one of the other authentication strategies, such as [frictionless authentication](https://www.canva.dev/docs/apps/authenticating-users/frictionless/) or [OAuth](https://www.canva.dev/docs/apps/authenticating-users/oauth/).

## Overview

Manual authentication is the more traditional approach when a user logs in via a third-party so they can access certain content or features within the app.

By doing this, you can:

* Give users access to their personal content, such as photos or videos
* Give users access to certain features based on their specific privileges
* Monetize apps by offering features or content to paying customers.

Some examples of apps that support authentication include:

* [D-ID Ai Presenters](https://www.canva.com/your-apps/AAFapKzFFus-d-id-ai-presenters)
* [Soundraw](https://www.canva.com/your-apps/AAFlCL1cRsE-soundraw?q=Soundraw)

For more examples, see the [Apps Marketplace](https://www.canva.com/your-apps).

## Lifecycle

The diagram below illustrates the lifecycle of an authentication flow that integrates with a third-party platform. Refer to the instructions below to understand how to implement each of the steps.



## Prerequisites

Before you begin, review the [Authentication design guidelines](https://www.canva.dev/docs/apps/design-guidelines/authentication/).

## Step 1: Enable authentication

By default, authentication is disabled.

To enable authentication:

1. Log in to the [Developer Portal](https://www.canva.com/developers).
2. Navigate to an app via the [Your apps](https://www.canva.com/developers/apps) page.
3. Click **Add authentication**.
4. Enable **This app requires authentication**.

When authentication is enabled, the following fields become active:

* Redirect URL
* Authentication base URL

Both of these fields must contain a URL and, in the coming steps, we'll set up those URLs.



## Step 2: Start an authentication flow

Apps are responsible for triggering the start of an authentication flow. *When* an app triggers the start of an authentication flow depends on the desired user experience. For example, you might want to start an authentication flow when a user tries to access restricted content.

To trigger the start of an authentication flow:

1. Import the `auth` namespace from the `@canva/user` package:

   ```ts
   import { auth } from "@canva/user";
   ```

2. Call the [`requestAuthentication`](https://www.canva.dev/docs/apps/api/v1/user-auth-request-authentication/) method:

   ```ts
   const result = await auth.requestAuthentication();
   ```

The `requestAuthentication` method opens a popup window and, within this window, redirects the user to the following URL:

```
<authentication_base_url>/configuration/start
```

`<authentication_base_url>` is a placeholder that will be replaced with the app's **Authentication base URL**. You can configure this URL in the Developer Portal, via the **Add authentication** page.



For example, if the **Authentication base URL** is:

```
https://www.example.com
```

Then the complete URL would be:

```
https://www.example.com/configuration/start
```

This URL doesn't exist yet though, so we'll set it up in the next step.

### Exposing the backend

The **Authentication base URL** must be available to Canva's backend. This means it must be exposed via the public internet. If it's not, Canva won't be able to send requests to it.

To do this, we recommend either of the following options:

* Deploy the app's backend to a non-production environment.
* Use an SSH tunneling service, such as [ngrok](https://www.ngrok.com), to expose a local server.

**Warning:** There are inherent risks in using tools such as ngrok. Be careful about what you expose to the public internet and shut-down the ngrok tunnel as soon as you're done using it.

## Step 3: Set up the `/configuration/start` endpoint

In the app's backend, set up an endpoint that handle `GET` requests sent to `/configuration/start`:

```ts
import * as express from "express";
import * as crypto from "crypto";

const app = express();

app.get("/configuration/start", (req, res) => {
  // TODO: Handle the request
});

// Start the server
const port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

This endpoint must:

* Extract the `state` parameter from the request's query parameters
* Generate a unique nonce for each request
* Store the nonce and an expiry time in a cookie
* Sign the cookie to avoid cookie tampering
* Redirect the user back to Canva

**Warning:** Don't attempt to [verify the HTTP request](https://www.canva.dev/docs/apps/verifying-http-requests/) that's sent to this endpoint. It does not have access to the necessary parameters that make verification possible.

### Extracting the `state` parameter

Canva appends a `state` query parameter to the `/configuration/start` endpoint. This parameter contains a random string of characters that must be returned to Canva for security reasons.

For the time being, extract the parameter from the request object:

```ts
const { state } = req.query;
```

### Generating a nonce

In the `/configuration/start` endpoint, generate a unique *nonce* for each request.

A nonce is a random, single-use value that's impossible to guess or enumerate. We recommended using a Version 4 UUID that is cryptographically secure, such as one generated with [`randomUUID`](https://nodejs.org/api/crypto.html#cryptorandomuuidoptions):

```ts
import * as crypto from "crypto";
const nonce = crypto.randomUUID();
```

**Warning:** Not all UUIDs are cryptographically secure, such as ones generated with the [`uuid`](https://www.npmjs.com/package/uuid) package.

### Setting a cookie

After generating a nonce, set a cookie that contains the nonce and an expiry time.

The cookie should be:

* [Secure](https://owasp.org/www-community/controls/SecureCookieAttribute)
* [HTTP-only](https://owasp.org/www-community/HttpOnly)
* Signed

It should also have an expiry time **in addition to** the expiry time being included in the cookie itself.

By *signing* a cookie, the app's backend can verify that the user hasn't modified the cookie. This prevents bad actors from tampering with the cookie in the browser.

The steps for setting and signing cookies depend on the framework. Some frameworks automatically sign cookies, while some don't have built-in support for cookie signing and require custom code.

It's beyond the scope of this documentation to explain all of the possible approaches, but refer to the following links to learn more about cookie signing in some popular frameworks:

* Go
  * [Fiber](https://docs.gofiber.io/api/middleware/encryptcookie/)
* Node.js
  * [Express.js](https://expressjs.com/en/resources/middleware/cookie-parser.html)
  * [Remix](https://remix.run/docs/en/main/utils/cookies#signing-cookies)
* PHP
  * [Laravel](https://laravel.com/docs/10.x/requests#cookies)
* Python
  * [Django](https://docs.djangoproject.com/en/4.2/topics/signing/)
  * [Flask](https://flask.palletsprojects.com/en/2.0.x/api/#sessions)
* Ruby
  * [Ruby on Rails](https://api.rubyonrails.org/v5.1/classes/ActionDispatch/Cookies.html)

The following code sample demonstrates how to set cookies with Express.js and [`cookieParser`](https://www.npmjs.com/package/cookie-parser):

```ts
import * as express from "express";
import * as crypto from "crypto";
import * as cookieParser from "cookie-parser";

const app = express();

// TODO: Load a cryptographically secure secret from an environment variable
app.use(cookieParser("SECRET GOES HERE"));

// The expiry time for the nonce, in milliseconds
const NONCE_EXPIRY_MS = 5 * 60 * 1000; // 5 minutes

app.get("/configuration/start", (req, res) => {
  // Generate a nonce
  const nonce = crypto.randomUUID();

  // Create an expiry time for the nonce
  const nonceExpiry = Date.now() + NONCE_EXPIRY_MS;

  // Store the nonce and expiry time in a stringified JSON array
  const nonceWithExpiry = JSON.stringify([nonce, nonceExpiry]);

  // Store the nonce and expiry time in a cookie
  res.cookie("nonceWithExpiry", nonceWithExpiry, {
    httpOnly: true,
    secure: true,
    signed: true,
    maxAge: NONCE_EXPIRY_MS,
  });
});
```

It's worth nothing that:

* To sign a cookie, you need a cryptographically secure secret, such as one generated by the `randomUUID` method. This secret should:
  * be loaded via an environment variable
  * not change between server restarts
  * not be committed to source control
* To store the nonce and an expiry time in a cookie, the above code sample stringifies a JSON array that contains both of the values, but there are other ways to accomplish the same outcome.
* You should be mindful of framework-specific nuances. For example, in Express.js, the `maxAge` property is set in milliseconds, but the [`Max-Age`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age) attribute value must be set in seconds.

### Redirecting back to Canva

After setting the cookie, redirect the user to the following URL with a `302` redirect:

```
https://www.canva.com/apps/configure/link?state=<state>&nonce=<nonce>
```

You'll need to:

* Replace `<state>` with the `state` query parameter that Canva included with the request.
* Replace `<nonce>` with the nonce that was stored in the cookie.

For example:

```ts
// Extract state from query parameters
const { state } = req.query;

// Create query parameters
const params = new URLSearchParams({
  state,
  nonce,
});

// Redirect the user
res.redirect(
  302,
  `https://www.canva.com/apps/configure/link?${params.toString()}`
);
```

When the redirect completes, Canva redirects the user to the app's **Redirect URL**. We'll see how to set up the **Redirect URL** in the next step.

## Step 4: Set up a Redirect URL

To authenticate users, apps need a **Redirect URL** — a page, hosted on the app's infrastructure, that allows a user to authenticate with the app's platform.

You can configure the app's **Redirect URL** in the Developer Portal, via the **Add authentication** page.

How a user authenticates isn't strictly important. The **Redirect URL** could point to a login form with a username and password, an OAuth 2.0 authorization flow, or something else altogether. The key is that the platform can identify the user and then link that identity to the user's Canva account.

When Canva redirects to the **Redirect URL**, it appends the following query parameters to the URL:

* `canva_user_token`
* `nonce`
* `state`

Your app's backend can use these parameters to securely authenticate a user.

**Note:** You may notice some other parameters appended to the **Redirect URL**. These parameters are deprecated and should be ignored.

### Validating the nonce

When a user arrives at the **Redirect URL**, the app needs to validate the nonce that was generated in the `/configuration/start` endpoint. This ensures that the user who started the authentication flow is the same one who is continuing it (and not some attacker trying to impersonate the user).

To validate the nonce:

1. Get the `nonce` query parameter:

   ```ts
   const nonceQuery = req.query.nonce;
   ```

2. Get the cookie that contains the nonce and its expiry time:

   ```ts
   const nonceWithExpiryCookie = req.signedCookies.nonceWithExpiry;
   ```

3. Clear the cookie:

   ```ts
   res.clearCookie("nonceWithExpiry");
   ```

4. Parse the value of the cookie:

   ```ts
   try {
     const [nonceCookie, nonceExpiry] = JSON.parse(nonceWithExpiryCookie);
   } catch (e) {
     // TODO: Handle errors
   }
   ```

   (This code uses a try/catch block to account for the possibility of JSON parsing exceptions.)

5. Verify that:

   * The nonce from the cookie has not expired.
   * The nonces are not nullish.
   * The nonces are not empty strings.
   * The nonces are equal to one another.

   For example:

   ```ts
   if (
     Date.now() > nonceExpiry || // The nonce has expired
     typeof nonceCookie !== "string" || // The nonce in the cookie is not a string
     typeof nonceQuery !== "string" || // The nonce in the query parameter is not a string
     nonceCookie.length < 1 || // The nonce in the cookie is an empty string
     nonceQuery.length < 1 || // The nonce in the query parameter is an empty string
     nonceCookie !== nonceQuery // The nonce in the cookie does not match the nonce in the query parameter
   ) {
     // The nonce is NOT valid
   }
   ```

### Handling invalid nonces

If the nonce validation fails, redirect the user to the following URL with a `302` redirect:

```
https://www.canva.com/apps/configured?success=false&state=<state>&errors=<errors>
```

You'll need to:

* Replace `<state>` with the `state` query parameter that Canva included with the request.
* Replace `<errors>` with a comma-separated list of one or more error codes. You can define the error codes yourself. They will be passed as-is to the app's frontend.

For example:

```ts
// Get the nonce from the query parameter
const nonceQuery = req.query.nonce;

// Get the nonce with expiry time from the cookie
const nonceWithExpiryCookie = req.signedCookies.nonceWithExpiry;

try {
  // Parse the JSON that contains the nonce and expiry time
  const nonceWithExpiry = JSON.parse(nonceWithExpiryCookie);

  // Extract the nonce and expiry time
  const [nonceCookie, nonceExpiry] = nonceWithExpiry;

  // Clear the cookie
  res.clearCookie("nonceWithExpiry");

  // If the nonces are invalid, terminate the authentication flow
  if (
    Date.now() > nonceExpiry || // The nonce has expired
    typeof nonceCookie !== "string" || // The nonce in the cookie is not a string
    typeof nonceQuery !== "string" || // The nonce in the query parameter is not a string
    nonceCookie.length < 1 || // The nonce in the cookie is an empty string
    nonceQuery.length < 1 || // The nonce in the query parameter is an empty string
    nonceCookie !== nonceQuery // The nonce in the cookie does not match the nonce in the query parameter
  ) {
    const params = new URLSearchParams({
      success: "false",
      state: req.query.state,
      errors: "invalid_nonce",
    });

    return res.redirect(
      302,
      `https://www.canva.com/apps/configured?${params.toString()}`
    );
  }
} catch (e) {
  // An unexpected error has occurred (e.g. JSON parsing error)
  const params = new URLSearchParams({
    success: "false",
    state: req.query.state,
    errors: "invalid_nonce",
  });

  return res.redirect(
    302,
    `https://www.canva.com/apps/configured?${params.toString()}`
  );
}
```

We also recommend logging a security alert, as invalid nonces suggest a potential threat.

### Authenticating the user

If the nonce validation succeeds, allow the user to authenticate. This is the part of the process that is highly dependent on the third-party platform, as there are many authentication strategies available.

After the user authenticates — for example, by entering a username and password — the next step is to create a link between the user's account on the platform and the user's account with Canva.

To link a user's accounts:

1. Grab the `canva_user_token` query parameter that Canva includes with the request. This parameter is a JSON Web Token (JWT) that is unique to the user.
2. [Verify the JWT](https://www.canva.dev/docs/apps/verifying-jwts/) to get the ID of the user and their team.
3. Use the IDs to create a mapping between the user in Canva and the user in the app's backend.

There are many ways to create a mapping, so it's not practical to document all of the possible options, but we can provide an example:

If your app's backend has a `users` table in its database, you could add an `canvaId` column to the table. This column could contain a composite key made up of the IDs. For example, if the user's ID is `123` and the ID of their team is `456`, the composite key would be something like `123:456`.

When a user authenticates via the **Redirect URL**, the app could save the composite key to the database. The app could then check for the existence of this key to determine if the user is authenticated.

## Step 5: End the authentication flow

At the end of an authentication flow, the app needs to:

* Know that the authentication flow has ended.
* Know the outcome of the authentication flow.
* Close the popup window.

If the user is able to successfully authenticate with the third-party platform, redirect them to the following URL from within the popup window:

```
https://www.canva.com/apps/configured?success=true&state=<state>
```

Replace `<state>` with the value of the `state` token from the start of the authentication flow.

If the user is *not* able to authenticate — for example, they have too many failed login attempts — redirect them to the following URL:

```
https://www.canva.com/apps/configured?success=false&state=<state>&errors=<errors>
```

Be sure to:

* Replace `<state>` with the value of the `state` token from the start of the authentication flow.
* Replace `<errors>` with a comma-separated list of one or more error codes. You can define the error codes yourself. They will be passed as-is to the app's frontend.

If you're performing the redirect via the app's backend, use a `302` redirect:

```ts
const params = new URLSearchParams({
  success: "true",
  state: req.query.state,
});

response.redirect(
  302,
  `https://www.canva.com/apps/configured?${params.toString()}`
);
```

If you're performing the redirect via the app's frontend, use the `window.location.replace` method:

```ts
const params = new URLSearchParams({
  success: "true",
  state: req.query.state,
});

window.location.replace(
  `https://www.canva.com/apps/configured?${params.toString()}`
);
```

## Step 6: Handle the authentication result

When the authentication flow ends, successfully or otherwise, the `requestAuthentication` method returns an object with a `status` property that describes the outcome of the flow:

```ts
const result = await auth.requestAuthentication();
console.log(result.status);
```

You can use the `status` property to render an appropriate user interface based on the result of the flow — for example, rendering an error when the authentication fails, or rendering certain content or features when authentication succeeds.

The possible values of the `status` property are:

* `"COMPLETED"` - The user was able to authenticate.
* `"DENIED"` - The user was not able to authenticate.
* `"ABORTED"` - The user closed the popup window.

When the `status` property is `"DENIED"`, the object has a `details` property that contains an array of error codes. These are the error codes provided by the app (if any) when it redirected back to Canva.

## Step 7: Send authenticated requests

When a user opens or interacts with an app, the app will need to check if the user is authenticated and, in some cases, render privileged content or features for that user.

To accomplish this, generate a JWT for the current user in the app's frontend:

```ts
const token = await auth.getCanvaUserToken();
```

Then send an HTTP request to the app's backend with the JWT in the `Authorization` header:

```ts
const response = await fetch("https://localhost:3001/authenticated-endpoint", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${token}`,
  },
});
```

When the backend receives the request:

1. Extract the JWT from the `Authorization` header.
2. [Verify the JWT](https://www.canva.dev/docs/apps/verifying-jwts/) to get the ID of the user and their team.
3. Use the IDs to check if the user is authenticated. How the app does this depends on how the app created a mapping between the user in their backend and the user on Canva.

If the user is authenticated, respond with whatever the frontend needs to render the authenticated content or features — for example, the user's photos or specific privileges.

If the user is not authenticated, respond to the request with an error. The frontend can use this error to restrict what the user has access to and to prompt them to authenticate.

## Step 8: Handle disconnections

**Tip:** Review Canva's design guidelines for [handling app disconnections and reconnections](https://www.canva.dev/docs/apps/design-guidelines/authentication/#handle-disconnections).

After a user connects (installs) an app, they have the option of disconnecting (uninstalling) it.

If a user has authenticated with a third-party platform, disconnecting the app in Canva won't automatically remove the connection between Canva and the platform — as far as the platform is concerned, the user will still be authenticated.

This is a subpar user experience for a couple of reasons:

* Disconnecting an app signals that the user's intent is to no longer be associated with the app and the app should respect that intent.
* If the user reconnects the app at a later time, they'll already be authenticated. This is a confusing user experience that's inconsistent with how the the rest of Canva works.

To address this issue, Canva sends a `POST` to the following endpoint when a user disconnects an app:

```
<authentication_base_url>/configuration/delete
```

`<authentication_base_url>` is a placeholder that will be replaced with the app's **Authentication base URL**. You can configure this URL in the Developer Portal, via the **Add authentication** page.

**Warning:** The `/configuration/delete` endpoint must not redirect to a different endpoint. Even a redirect that just appends a `/` to the end of the endpoint will cause the request to fail.

In the request's headers, Canva includes an `Authorization` header that contains a JWT for the current user. When the app receives this request, it should:

1. Extract the JWT from the `Authorization` header.
2. [Verify the JWT](https://www.canva.dev/docs/apps/verifying-jwts/) to get the ID of the user and their team.
3. Use the IDs to find the user in the app's backend.
4. Remove any connection between the user and Canva.

When the disconnection is complete, respond with a `200` status code and the following object:

```json
{
  "type": "SUCCESS"
}
```

To confirm that the disconnection flow is working:

1. Navigate through the authentication flow.
2. Disconnect (uninstall) the app.
3. Reconnect (install) the app.

You should have to re-authenticate to access any privileged content or features. If you don't have to re-authenticate, double-check the disconnection logic.

## API reference

* [`auth.getCanvaUserToken`](https://www.canva.dev/docs/apps/api/latest/user-auth-get-canva-user-token/)
* [`auth.requestAuthentication`](https://www.canva.dev/docs/apps/api/v1/user-auth-request-authentication/)
