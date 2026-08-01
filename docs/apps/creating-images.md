Source: https://www.canva.dev/docs/apps/creating-images/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating images

How to add images to a user's design.

Apps can add images to a user's design, such as PNG or SVG files. The user can then arrange and manipulate those images with the Canva tooling they've come to know and love.

## The user experience

When an app adds an image to the user's design, the image file is uploaded to the user's media library.

The user's media library has a storage quota. If the user has a [Canva Pro](https://www.canva.com/pro/) account, their storage quota is 1TB. Otherwise, their storage quota is 5GB. If the user exceeds the storage quota, they'll see an error.

Once the image exists in the user's design, the image is indistinguishable from images added via Canva's built-in features. This means the user can manipulate the image in all the same ways, including:

* Adjusting the size, position, and rotation of the image
* Applying effects to the image
* Using the image as a background
* Animating the image — for example, having it fade in

## Supported image types

Apps can add the following types of images to a user's design:

| Name | MIME type     | Common file extensions |
| ---- | ------------- | ---------------------- |
| HEIC | image/heic    | .heic                  |
| JPEG | image/jpeg    | .jpg, .jpeg            |
| PNG  | image/png     | .png                   |
| SVG  | image/svg+xml | .svg                   |
| TIFF | image/tiff    | .tiff, .tif            |
| WebP | image/webp    | .webp                  |

The maximum file size for images is 50MB.

**Note:** GIFs are handled as videos, not images. To learn more, see [Creating videos](https://www.canva.dev/docs/apps/creating-videos/).

## Data URLs vs. external URLs

When creating images, the image data can be provided as an external URL or a base64-encoded data URL. The ideal format of the data depends on the behavior of the app:

* If the app generates images in the browser, such as by drawing on a `HTMLCanvasElement`, then a base64-encoded data URL will be the fastest and easiest way to provide the image data.
* If the app generates or serves images from a third-party server, as would be the case with generative AI apps, then an external URL would make the most sense.

## How to create images

### Step 1: Enable the required scopes

In the Developer Portal, enable the following scopes:

* `canva:design:content:write`
* `canva:asset:private:write`

In the future, the Apps SDK will throw an error if the required scopes aren't enabled.

To learn more, see [Configuring scopes](https://www.canva.dev/docs/apps/configuring-scopes/).

### Step 2: Upload an image

Import the `upload` method from the `@canva/asset` package:

```ts
import { upload } from "@canva/asset";
```

Call the method, passing in the options shown here:

```ts
const result = await upload({
  type: "image",
  mimeType: "image/jpeg",
  url: "https://www.canva.dev/example-assets/image-import/image.jpg",
  thumbnailUrl:
    "https://www.canva.dev/example-assets/image-import/thumbnail.jpg",
  aiDisclosure: "none",
});
```

When uploading images, the URLs must be exposed via the internet and available to Canva's backend, as Canva needs access to the URLs to download them. This means you can't use `localhost` URLs.

The `upload` method returns an object that contains a `ref` property:

```ts
console.log(result.ref);
```

This property contains a *reference*, which is a unique identifier that points to an image asset in Canva's backend. An app can use this reference to interact with the file — even while it's uploading.

### Step 3: Add the image to the design

Import the `addElementAtPoint` method (or `addElementAtCursor`, [depending on the current context](https://www.canva.dev/docs/apps/elements/#creating-elements)) from the `@canva/design` package:

```ts
import { addElementAtPoint } from "@canva/design";
```

Call the method, passing in the options shown here:

```ts
await addElementAtPoint({
  type: "image",
  ref: result.ref,
  altText: {
    text: "Example image",
    decorative: false
  },
});
```

## Additional considerations

* All images must comply with Canva's [Acceptable Use Policy](https://www.canva.com/policies/acceptable-use-policy).
* All images must comply with Canva's [Upload formats and requirements](https://www.canva.com/help/upload-formats-requirements/).

## API reference

* [`addElementAtPoint`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/)
* [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/)

## Code sample

```tsx
import React from "react";
import { upload } from "@canva/asset";
import { addElementAtPoint } from "@canva/design";

export function App() {
  async function handleClick() {
    // Upload an image
    const result = await upload({
      type: "image",
      mimeType: "image/jpeg",
      url: "https://www.canva.dev/example-assets/image-import/image.jpg",
      thumbnailUrl:
        "https://www.canva.dev/example-assets/image-import/thumbnail.jpg",
      aiDisclosure: "none",
    });

    // Add the image to the design
    await addElementAtPoint({
      type: "image",
      ref: result.ref,
      altText: {
        text: "Example image",
        decorative: false
      },
    });
  }

  return (
    <div>
      <button onClick={handleClick}>Add image from external URL</button>
    </div>
  );
}
```
