Source: https://www.canva.dev/docs/apps/integrating-canva/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating with Canva

How to create an app that hooks into the Canva editor.

At its most basic, an app is a JavaScript file that runs inside an iframe. Canva embeds this iframe in the side panel of the Canva editor. The app can then render content inside the iframe and interact with the editor via APIs.

## Using the APIs

Canva injects APIs into the app's iframe. The app can then access these APIs via a number of methods. The TypeScript declarations for these methods are organized into a handful of npm packages.

The available packages include:

* [`@canva/asset`](https://www.npmjs.com/package/@canva/asset)
* [`@canva/design`](https://www.npmjs.com/package/@canva/design)
* [`@canva/error`](https://www.npmjs.com/package/@canva/error)
* [`@canva/platform`](https://www.npmjs.com/package/@canva/platform)
* [`@canva/user`](https://www.npmjs.com/package/@canva/user)

Apps can use any combination of these packages and their methods to implement the app's behavior.

To use a method, import it from a package and call it with the required parameters. For example, the following code sample demonstrates how to use the `requestExport` method from the `@canva/design` package:

```ts
import { requestExport } from "@canva/design";

const response = await requestExport({
  acceptedFileTypes: ["png", "jpg"],
});

console.log(response); // { exportBlobs: [{ url: "https://example.com/image.png" }] }
```

You can find the complete list of methods and their parameters in the **API reference** section of the documentation.

<Warning>
  **Gotcha: The side-effect of injection**

  By injecting APIs into the iframe, we can push fixes to the APIs without requiring apps to be updated. The unfortunate side-effect of this is that we can also inadvertently push bugs to the APIs.

  In these cases, rolling packages back to earlier versions won't fix the issue because the packages contain TypeScript declarations, not the underlying methods. The only solution is to wait for us to push the fix.

  This isn't a common occurrence. It's just potentially confusing if you're not aware of it ahead of time.
</Warning>

## Preview APIs

To ensure we're developing the best possible APIs, we want to get them in the hands of developers sooner rather than later. We do this by releasing preview versions of the APIs that anyone can play around with.

Canva provides a preview of the APIs through [the npm package registry](https://www.npmjs.com/). You can install an available preview API package by using npm with the `beta` dist-tag. The following npm command demonstrates how to install the preview `@canva/design` package:

```bash
npm install @canva/design@beta
```

After installing the preview package, you can then import the preview methods you'd like to try:

```ts
import { addElementAtPoint } from "@canva/design";
```

If a preview method reaches a stable release, you can then install the latest package version, and continue using the method without changing the import declaration. Confirm your package version by running `npm list`, and checking for the `beta` tag:

```bash
npm list -a @canva/design@beta

├── @canva/design@1.11.0-beta.1
├─┬ digital_asset_management@ -> ./examples/digital_asset_management
  └─┬ @canva/app-components@1.0.0-beta.22
    └── @canva/design@1.10.0
```

A preview accessed through the `beta` dist-tag exposes new methods and modified versions of existing methods. They're documented alongside the stable APIs, but we make sure to highlight anything that's only available as a preview.

If you're planning on using a preview package, be aware that:

* Anything imported with the `beta` dist-tag package may experience breaking changes at short notice. You should not rely on the methods remaining available or continuing to behave in the same way.
* If an app depends on the preview package, it won't be approved for release during Canva's [app review process](https://www.canva.dev/docs/apps/app-review-process/). You'll have to wait for the API to be moved into one of the stable packages.

## Technical limitations

Apps have a lot of freedom within their iframes, but not total freedom.

In particular, these are the technical limitations that developers struggle with:

* The iframe has a Content Security Policy (CSP) that prevents certain resources, such as third-party scripts, from being loaded. To learn more, see [Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/).
* The iframe has a [Permission Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Permissions_Policy) that prevents apps from accessing certain browser features. The only feature allowed by this policy is writing data to the user's clipboard.
* If the app sends HTTP requests to a backend, the requests will fail unless the backend is configured to support Cross-Origin Resource Sharing (CORS). To learn more, see [Using a backend](https://www.canva.dev/docs/apps/using-backend/) and [Cross-Origin Resource Sharing](https://www.canva.dev/docs/apps/cross-origin-resource-sharing/).
* The app doesn't have free-for-all access to the underlying document model. This means it can't freely read and write changes to the design. It can only use Canva's APIs, which expose a limited subset of controls.
