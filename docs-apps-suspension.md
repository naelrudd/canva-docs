Source: https://www.canva.dev/docs/apps/suspension/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Suspension

An introduction to suspension in the Apps SDK.

When a user navigates away from an app, Canva attempts to suspend the app rather than closing it entirely. When the user returns to the app, they can then can continue from where they left off.

This mimics the user experience of Canva's native features.

## How suspension works

When an app is suspended:

* The app's iframe is hidden from view.
* The process injected into the iframe remains active but is placed in a `"suspended"` state.

To see this in action:

1. Open an app.
2. Interact with the app in some way, such as by entering a value into a text field.
3. Switch to a different tab in the editor, such as the **Elements** tab.
4. Switch back to the app.

You should see that the app has remained open and maintained its state.

## Resource limits

While an app is suspended, it continues to consume some resources. Because of this, there are limits to the number of apps that can be running at any point in time. The exact limit depends on the device and may change over time.

The important thing to understand is that suspension is not guaranteed. It's done on a "best effort" basis. If too many resources are consumed, the app's process will be terminated to avoid performance issues.

## Restricted APIs

While an app is suspended, some features of the Apps SDK are not available, including but not limited to:

* APIs that attempt to access design data.
* APIs that attempt to access user data.
* APIs that require user interaction.

In addition, the following restrictions apply to standard web APIs:

* Audio playback is paused.
* Video playback is paused.

If an app attempts to call an unavailable API, the SDK throws an `CanvaError` with an error code of `"not_allowed"`:

```ts
import { addElementAtPoint } from "@canva/design";
import { CanvaError } from "@canva/error";

try {
  await addElementAtPoint({
    type: "embed",
    url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  });
} catch (error) {
  if (error instanceof CanvaError) {
    // If a restricted API is called while the app is
    // suspended, the error code is `"not_allowed"`
    console.log(error.code);
  }
}
```

## Gotchas

* Apps don't remain suspended across page loads. If the user reloads the page, all app processes will be terminated.
