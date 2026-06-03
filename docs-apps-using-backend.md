Source: https://www.canva.dev/docs/apps/using-backend/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Using a backend

How to integrate an app with a backend.

At their most basic, apps are web pages embedded in the Canva editor. As a result, they have access to standard web technologies, such as the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API). This allows them to integrate with backend services and APIs.

## Why use a backend?

You can make great apps without a backend, but there are a number of reasons to use one, such as:

* Fetching content from a third-party server, such as images or videos.
* Running tasks that are difficult to run in the browser, such as generative AI tasks.
* Tracking a user's activities to better understand how they're using your app.

**Note:** An app requires a backend for certain features, such as [authentication](https://www.canva.dev/docs/apps/authenticating-users/).

## Setting up a backend

In [the starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/), we've provided [an example backend](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/tree/main/utils/backend), built with Express.js. Some of the example apps rely on this backend, but it's only intended to illustrate certain concepts — not as a production-ready solution.

Fortunately, Canva doesn't require backends to be built in any particular way. You can use any combination of language or framework, and if you already have a backend up and running, you can adapt it to work with your app.

## Sending requests

To send a request to an app's backend, use the Fetch API as you would on any other web page:

```ts
const response = await fetch("http://localhost:3000/hello-world");
console.log(response.status);
```

The backend can respond with whatever data the frontend needs. The requests don't pass through Canva's servers, so there's no particular format that Canva requires.

**Warning:** If the app's backend is not configured to receive requests from the app's frontend, the requests will fail. This is a security feature built into web browsers. To learn more, see [Cross-Origin Resource Sharing](https://www.canva.dev/docs/apps/cross-origin-resource-sharing/).

### Sending JSON

If you're sending JSON to the app's backend, include the `Content-Type` header and stringify the body:

```ts
const response = await fetch("http://localhost:3000/hello-world", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ message: "Hello world" }),
});

console.log(response.status);
```

This is standard usage of the Fetch API, but it's easy to forget.

## Developing locally

When developing an app, the backend does not always need to be available via the public internet. You can run the backend on your local machine and send requests directly to a `localhost` URL.

There are, however, some exceptions:

* When implementing [authentication](https://www.canva.dev/docs/apps/authenticating-users/), the backend must expose certain endpoints via the public internet.
* When [uploading assets](https://www.canva.dev/docs/apps/uploading-assets/), the assets themselves must be available via the public internet.

To make endpoints or resources available to the public internet, either:

* Deploy the endpoints to a testing or staging environment.
* Use an SSH tunneling tool, such as [ngrok](https://ngrok.com/) or [localtunnel](https://github.com/localtunnel/localtunnel).

**Warning:** There's an inherent risk in using SSH tunnels. Be mindful about what you're exposing to the public internet and shut down tunnels when they're not in use.

## Security requirements

For the sake of security, apps must verify HTTP requests. This ensures that the backend only accepts requests from known and trusted sources. This is also how apps can access user data, such as the ID of the user.

To learn more, see [HTTP request verification](https://www.canva.dev/docs/apps/verifying-http-requests/).
