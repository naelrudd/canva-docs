Source: https://www.canva.dev/docs/apps/handling-errors/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Handling errors

How to handle errors thrown by the Apps SDK.

In the Apps SDK, all methods have the potential to throw an error if something goes wrong, such as a request timing out or the user being disconnected from the internet.

While developing an app, it's important to:

* Be mindful of errors that may occur.
* Handle errors as gracefully as possible.

## How to handle errors

1. Import `CanvaError` from the `@canva/error` package:

   ```ts
   import { CanvaError } from "@canva/error";
   ```

2. When calling a method from the Apps SDK, wrap it in a try/catch block:

   ```ts
   import { addElementAtPoint } from "@canva/design";
   import { CanvaError } from "@canva/error";

   try {
     await addElementAtPoint({
       type: "embed",
       url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
     });
   } catch (error) {
     console.log(error);
   }
   ```

3. In the `catch` block, check if the error is an instance of a `CanvaError`:

   ```ts
   if (error instanceof CanvaError) {
     console.log("CanvaError:", error.code);
   }
   ```

   The `CanvaError` object contains two properties:

   * `code` - A string that identifies the reason for the error.
   * `message` - Additional information about the error.

4. Use the `code` property to handle the possible error cases:

   ```ts
   if (error instanceof CanvaError) {
     switch (error.code) {
       case "permission_denied":
         console.log("You don't have the required scopes.");
         break;
       case "user_offline":
         console.log("You're offline.");
         break;
       case "timeout":
         console.log("The request timed out.");
         break;
     }
   }
   ```

**Note:** You don't have to handle all error codes for all methods — most methods only have the potential to throw a subset of the available errors.

### Using the Promise syntax

The try/catch syntax is the modern way to catch errors, and it's the approach that's used throughout the documentation, but it's not a strict requirement. You can also use the Promise syntax:

```ts
import { addElementAtPoint } from "@canva/design";
import { CanvaError } from "@canva/error";

addElementAtPoint({
  type: "embed",
  url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
}).catch((error) => {
  if (error instanceof CanvaError) {
    console.log("CanvaError:", error.code);
  }

  console.log(error);
});
```

### Handling other errors

Be mindful of the fact that other errors may occur throughout the lifecycle of an app, such as errors from native browser APIs or third-party libraries — that is, handling errors from the Apps SDK doesn't mean that all possible errors are handled.

## List of error codes

When a method in the Apps SDK throws an error, there's a limited range of possible error codes. This section lists all of the possible error codes that may appear in a `CanvaError` object.

### `bad_external_service_response`

A response from an external service is invalid or malformed.

**Example:** When redirecting back to Canva at the end of an authentication flow, the URL is malformed.

### `bad_request`

The app has made a request that's invalid or malformed.

**Example:** The app calls a function without a required parameter.

### `failed_precondition`

The app hasn't met a precondition.

### `internal_error`

There's an error in the App SDK's internal implementation.

**Example:** There's an underlying issue in Canva's backend.

### `not_allowed`

The app is not allowed to perform the specified operation.

**Example:** The app tries to call the `navigator.clipboard.write` method, which has been disabled due to it not being cross-browser compatible.

### `not_found`

The app can't retrieve the specified resource.

**Example:** The app tries to operate on an asset reference that doesn't exist.

### `quota_exceeded`

The app or user has exceeded their allocated quota for a resource or service.

**Example:** The app can't upload a file because the user is out of storage space.

### `permission_denied`

The app doesn't have sufficient scopes.

**Example:** The app tries to create an element without having sufficient scopes.

### `rate_limited`

The app has made too many requests within a certain time period. The reference page for each API method includes a description of any rate limits. For example, the [rate limit for `requestExport`](https://www.canva.dev/docs/apps/api/v1/design-request-export/#rate-limit).

**Example:** The app tries to create too many elements in a short period of time.

### `timeout`

The operation exceeded the maximum allowed time to complete.

### `unsupported_surface`

An API is called from an incompatible surface. A surface may be incompatible with an API for technical reasons or to avoid a confusing user experience.

**Example:** An app tries to [open a font picker](https://www.canva.dev/docs/apps/creating-text/) from an [image overlay](https://www.canva.dev/docs/apps/creating-image-overlays/).

### `user_offline`

The user is offline.

**Example:** The user tries to authenticate without being connected to the internet.
