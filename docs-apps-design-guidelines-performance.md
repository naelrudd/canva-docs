Source: https://www.canva.dev/docs/apps/design-guidelines/performance/

# Performance

Guidelines for creating a fast-loading app.

## Reduce the bundle size

The source code for an app is loaded as a single JavaScript bundle. As a result, any increase in the bundle size affects the initial load time. To reduce the bundle size, we recommend:

* Being mindful of dependencies, which can add up quickly
* Using a tool, such as [Webpack Bundle Analyzer](https://www.npmjs.com/package/webpack-bundle-analyzer), to monitor the bundle size
* Loading assets via URLs instead of importing them as data URLs

## Offload tasks to a server

These days, you can run fairly intensive processes in the browser. Generally, though, we recommend offloading these processes to a server. This ensures that performance is consistent across devices and isn't affected by the amount of memory available to the app's frontend at that particular moment.

To learn how to interact with a server, see [HTTP request verification](https://www.canva.dev/docs/apps/verifying-http-requests/).

## Show loading spinners

Visual affordances, such as loading spinners, can improve the perception of performance. This may not be as satisfying as actually improving performance, but it's an important step.

To learn more about loading states, see [Loading](https://www.canva.dev/docs/apps/design-guidelines/loading/).

## Use thumbnails

When working with images (or using our image-related libraries), we recommend using [`thumbnailUrl`](https://www.canva.dev/docs/apps/api/latest/asset-upload/?parameter-list=Images#parameters) to define a smaller preview version of a full-size image. This lets you improve performance by loading a thumbnail instead of a full-size image, when required.

### Example

This example demonstrates how to define `thumbnailUrl` during an image upload process. To use this approach, you'll need to generate your own thumbnails and make them available in your storage backend.

You can then use the thumbnail in the object panel of the Canva editor, when the full-size image isn't required. The smaller size means that it'll load more quickly for the user, due to the reduced impact on network and compute resources.

```typescript
import { upload } from "@canva/asset";
await upload({
  type: "IMAGE",
  mimeType: "image/jpeg",
  // The full-size image:
  url: "https://www.canva.dev/example-assets/image-import/image.jpg",
  // The image thumbnail:
  thumbnailUrl:
    "https://www.canva.dev/example-assets/image-import/thumbnail.jpg",
  width: 540,
  height: 720,
  aiDisclosure: "none",
});
```

* `thumbnailUrl`: This thumbnail image can be rendered in the object panel of the Canva editor, and can also be used in the design canvas.
* `url`: The full-size image that gets added to the canvas.
* These URLs are fully-qualified paths that are subject to [CORS](https://www.canva.dev/docs/apps/cross-origin-resource-sharing/) controls.
