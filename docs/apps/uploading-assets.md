Source: https://www.canva.dev/docs/apps/uploading-assets/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Assets

How apps can upload, download, and interact with assets.

An *asset* is a file that exists in Canva's backend, such as an image, video, or audio file. Apps can upload, download, and otherwise interact with assets in a variety of ways.

## Asset types

Apps can interact with the following types of assets:

* [Audio](https://www.canva.dev/docs/apps/creating-audio-tracks/)
* [Fonts](https://www.canva.dev/docs/apps/fonts/)
* [Images](https://www.canva.dev/docs/apps/creating-images/)
* [Videos](https://www.canva.dev/docs/apps/creating-videos/)

The type of asset affects how an app can interact with it. For example, apps can upload and download image assets, but can only use font assets when [creating text](https://www.canva.dev/docs/apps/creating-text/) — they can't upload or download font assets.

The following table indicates how apps can interact with each type of asset:

|            | Upload | Download | Use |
| ---------- | ------ | -------- | --- |
| **Audio**  |        |          |     |
| **Fonts**  |        |          |     |
| **Images** |        |          |     |
| **Videos** |        |          |     |

## Asset ownership

There are two kinds of assets:

* Public assets
* Private assets

There are some differences in how apps can interact with each kind of asset.

### Public assets

A *public asset* is one that's owned by Canva — that is, it was uploaded by Canva and is available to most users (with some restrictions, depending on how the asset was licensed). These assets appear in the **Elements** tab.

In certain contexts, apps can download public assets, but they can never upload them.

### Private assets

A *private asset* is one that was uploaded by a user and exists within their media library. The user owns the asset and no one else has access to it unless they choose to share it. These assets appear in the **Uploads** tab.

In certain contexts, apps can upload and/or download private assets.

## Asset references

All assets have an *asset reference*, also known as a *ref*.

A ref is a unique identifier that points to an asset in Canva's backend.

Refs are used throughout the Apps SDK in a variety of contexts. For example, when an asset is uploaded, a ref for that asset is returned and can be used to then interact with that asset:

```tsx
import { type ImageRef, upload } from "@canva/asset";

// If you are uploading an image that is derived from another image, pass its imageRef, otherwise set it as undefined
const parentRef = "PLACEHOLDER_IMAGE_REF" as ImageRef;

// Upload an image asset
const asset = await upload({
  type: "image",
  parentRef,
  mimeType: "image/jpeg",
  url: "https://example.com/image.jpg",
  thumbnailUrl: "https://example.com/thumbnail.jpg",
  aiDisclosure: "none",
});

// Use the ref of the asset
console.log(asset.ref);
```

Similarly, refs can sometimes be retrieved for existing assets, such as when selecting a font from a [font picker](https://www.canva.dev/docs/apps/fonts/).

The various ways that refs can be used are explained throughout the documentation.

### Important: Refs are opaque strings

**Refs are opaque strings and apps shouldn't rely on them remaining the same**. In practice, this means that apps should only use refs soon after they're created or retrieved and should not store them for later use.

Apps can upload private assets to a user's media library. When the upload succeeds or fails, a toast notification is shown to the user. (The notification itself is not customizable.)

<Tabs>
  <Tab name="Audio">
    ```tsx
    import { upload } from "@canva/asset";

    await upload({
      type: "audio",
      title: "Example audio",
      mimeType: "audio/mp3",
      durationMs: 86047,
      url: "https://example.com/audio.mp3",
      aiDisclosure: "none",
    });
    ```
  </Tab>

  <Tab name="Images">
    ```tsx
    import { type ImageRef, upload } from "@canva/asset";

    // If you are uploading an image that is derived from another image, pass its imageRef, otherwise set it as undefined
    const parentRef = "PLACEHOLDER_IMAGE_REF" as ImageRef;

    await upload({
      type: "image",
      parentRef,
      mimeType: "image/jpeg",
      url: "https://example.com/image.jpg",
      thumbnailUrl: "https://example.com/thumbnail.jpg",
      aiDisclosure: "none",
    });
    ```
  </Tab>

  <Tab name="Videos">
    ```tsx
    import { type VideoRef, upload } from "@canva/asset";

    // If you are uploading a video that is derived from another video, pass its videoRef, otherwise set it as undefined
    const parentRef = "PLACEHOLDER_VIDEO_REF" as VideoRef;

    await upload({
      type: "video",
      parentRef,
      mimeType: "video/mp4",
      url: "https://example.com/video.mp4",
      thumbnailImageUrl: "https://example.com/thumbnail-image.jpg",
      thumbnailVideoUrl: "https://example.com/thumbnail-video.mp4",
      aiDisclosure: "none",
    });
    ```
  </Tab>
</Tabs>

**Note:** All assets must comply with Canva's [Acceptable Use Policy](https://www.canva.com/policies/acceptable-use-policy/).

### Supported file formats

When uploading assets, the following file formats are supported:

<Tabs>
  <Tab name="Audio">
    | Name      | MIME type       | Common file extensions        |
    | --------- | --------------- | ----------------------------- |
    | MPEG      | `"audio/mpeg"`  | .mpg, .mpeg, .mp1, .mp2, .mp3 |
    | MP4 Audio | `"audio/mp4"`   | .mp4, .m4a                    |
    | M4A       | `"audio/x-m4a"` | .m4a                          |
    | MP3       | `"audio/mp3"`   | .mp3                          |
    | OGG       | `"audio/ogg"`   | .ogg, .oga                    |
    | WAV       | `"audio/wav"`   | .wav                          |
    | X-WAV     | `"audio/x-wav"` | .wav                          |
    | WEBM      | `"audio/webm"`  | .webm                         |
  </Tab>

  <Tab name="Images">
    | Name | MIME type         | Common file extensions |
    | ---- | ----------------- | ---------------------- |
    | HEIC | `"image/heic"`    | .heic                  |
    | JPEG | `"image/jpeg"`    | .jpg, .jpeg            |
    | PNG  | `"image/png"`     | .png                   |
    | SVG  | `"image/svg+xml"` | .svg                   |
    | TIFF | `"image/tiff"`    | .tiff, .tif            |
    | WebP | `"image/webp"`    | .webp                  |

    **Note:** In the Apps SDK, GIFs are considered to be videos, not images.
  </Tab>

  <Tab name="Videos">
    | Name      | MIME types                         | Common file extensions |
    | --------- | ---------------------------------- | ---------------------- |
    | AVI       | `"video/avi"`, `"video/x-msvideo"` | .avi                   |
    | GIF       | `"image/gif"`                      | .gif                   |
    | M4V       | `"video/x-m4v"`                    | .m4v                   |
    | Matroska  | `"video/x-matroska"`               | .mkv                   |
    | QuickTime | `"video/quicktime"`                | .mov                   |
    | MP4       | `"video/mp4"`                      | .mp4                   |
    | MPEG      | `"video/mpeg"`                     | .mpg, .mpeg            |
    | WebM      | `"video/webm"`                     | .webm                  |

    **Note:** In video files, transparent or translucent pixels are converted to black pixels.
  </Tab>
</Tabs>

### File size limits

When uploading assets, the following file size limits apply:

| Asset type      | Maximum file size |
| --------------- | ----------------- |
| Audio           | 250 MB            |
| Images (Raster) | 50 MB             |
| Images (SVG)    | 3 MB              |
| Videos          | 1000 MB           |

### Asset URLs

When uploading an asset, the asset is downloaded via Canva's backend. For this reason, asset URLs must be available via the public internet — that is, they can't be uploaded from `localhost` URLs.

### Thumbnail URLs

When uploading image and video assets, a thumbnail must be provided. In the case of videos, a preview video can also be provided. These thumbnails and previews are shown to the user:

* in the **Uploads** tab
* in the editor, while the asset is uploading

For security reasons, the URLs of these thumbnails and previews must support [Cross-Origin Resource Sharing](https://www.canva.dev/docs/apps/cross-origin-resource-sharing/) (CORS). If CORS is not supported, the URLs won't load and an error will appear in the JavaScript Console.

### AI disclosure

When uploading assets, apps must disclose if the asset was created or significantly altered with AI. This helps users make informed decisions about the content they interact with.

These are some examples of when AI usage must be disclosed:

* Generating a new image from scratch
* Changing the style of an image
* Removing an object and replacing it with new content
* Changing facial expressions of people
* Compositing multiple images together
* Expanding images by generating content at the edges
* Replacing backgrounds with generated content

These are some examples of when AI usage does not require disclosure:

* Using existing assets from an asset library
* Correcting red eyes
* Removing backgrounds without replacement
* Changing object colors
* Detecting image defects and suggesting fixes
* Adjusting brightness and contrast
* Upscaling images

If the app used AI to create or alter an asset, set `aiDisclosure` to `"app_generated"`:

```tsx
import { type ImageRef, upload } from "@canva/asset";

// If you are uploading an image that is derived from another image, pass its imageRef, otherwise set it as undefined
const parentRef = "PLACEHOLDER_IMAGE_REF" as ImageRef;

const asset = await upload({
  type: "image",
  parentRef,
  mimeType: "image/jpeg",
  url: "https://example.com/ai-generated-image.jpg",
  thumbnailUrl: "https://example.com/ai-generated-thumbnail.jpg",
  aiDisclosure: "app_generated",
});
```

Otherwise, set `aiDisclosure` to `"none"`:

```tsx
import { type ImageRef, upload } from "@canva/asset";

// If you are uploading an image that is derived from another image, pass its imageRef, otherwise set it as undefined
const parentRef = "PLACEHOLDER_IMAGE_REF" as ImageRef;

const asset = await upload({
  type: "image",
  parentRef,
  mimeType: "image/jpeg",
  url: "https://example.com/ai-generated-image.jpg",
  thumbnailUrl: "https://example.com/ai-generated-thumbnail.jpg",
  aiDisclosure: "none",
});
```

### Checking upload progress

Apps can detect when an asset has finished uploading. An example of how an app might use this behavior is to render a loading state while the upload is in progress.

<Tabs>
  <Tab name="Audio">
    ```tsx
    import { upload } from "@canva/asset";
    import { addAudioTrack } from "@canva/design";

    // Upload an audio asset
    const asset = await upload({
      type: "audio",
      title: "Example audio",
      mimeType: "audio/mp3",
      durationMs: 86047,
      url: "https://example.com/audio.mp3",
      aiDisclosure: "none",
    });

    // Wait for the upload to complete
    await asset.whenUploaded();
    ```
  </Tab>

  <Tab name="Images">
    ```tsx
    import { type ImageRef, upload } from "@canva/asset";

    // If you are uploading an image that is derived from another image, pass its imageRef, otherwise set it as undefined
    const parentRef = "PLACEHOLDER_IMAGE_REF" as ImageRef;

    // Upload an image asset
    const asset = await upload({
      type: "image",
      parentRef,
      mimeType: "image/jpeg",
      url: "https://example.com/image.jpg",
      thumbnailUrl: "https://example.com/thumbnail.jpg",
      aiDisclosure: "none",
    });

    // Wait for the upload to complete
    await asset.whenUploaded();
    ```
  </Tab>

  <Tab name="Videos">
    ```tsx
    import { type VideoRef, upload } from "@canva/asset";

    // If you are uploading a video that is derived from another video, pass its videoRef, otherwise set it as undefined
    const parentRef = "PLACEHOLDER_VIDEO_REF" as VideoRef;

    // Upload a video asset
    const asset = await upload({
      type: "video",
      parentRef,
      mimeType: "video/mp4",
      url: "https://example.com/video.mp4",
      thumbnailImageUrl: "https://example.com/thumbnail-image.jpg",
      thumbnailVideoUrl: "https://example.com/thumbnail-video.mp4",
      aiDisclosure: "none",
    });

    // Wait for the upload to complete
    await asset.whenUploaded();
    ```
  </Tab>
</Tabs>

What's possibly surprising though is that apps don't have to wait for the upload to complete before the asset reference is available. Apps can use the asset reference as soon as the upload starts.

<Tabs>
  <Tab name="Audio">
    ```tsx
    import { upload } from "@canva/asset";
    import { addAudioTrack } from "@canva/design";

    // Upload an audio asset
    const asset = await upload({
      type: "audio",
      title: "Example audio",
      mimeType: "audio/mp3",
      durationMs: 86047,
      url: "https://example.com/audio.mp3",
      aiDisclosure: "none",
    });

    // You can use the asset reference immediately
    console.log(asset.ref);

    // Use the asset reference to add an audio track
    await addAudioTrack({
      ref: asset.ref,
    });
    ```
  </Tab>

  <Tab name="Images">
    ```tsx
    import { type ImageRef, upload } from "@canva/asset";
    import { addElementAtPoint } from "@canva/design";

    // If you are uploading an image that is derived from another image, pass its imageRef, otherwise set it as undefined
    const parentRef = "PLACEHOLDER_IMAGE_REF" as ImageRef;

    // Upload an image asset
    const asset = await upload({
      type: "image",
      parentRef,
      mimeType: "image/jpeg",
      url: "https://example.com/image.jpg",
      thumbnailUrl: "https://example.com/thumbnail.jpg",
      aiDisclosure: "none",
    });

    // You can use the asset reference immediately
    console.log(asset.ref);

    // Use the asset reference to add an image element
    await addElementAtPoint({
      type: "image",
      ref: asset.ref,
    });
    ```
  </Tab>

  <Tab name="Videos">
    ```tsx
    import { type VideoRef, upload } from "@canva/asset";
    import { addElementAtPoint } from "@canva/design";

    // If you are uploading a video that is derived from another video, pass its videoRef, otherwise set it as undefined
    const parentRef = "PLACEHOLDER_VIDEO_REF" as VideoRef;

    // Upload a video asset
    const asset = await upload({
      type: "video",
      parentRef,
      mimeType: "video/mp4",
      url: "https://example.com/video.mp4",
      thumbnailImageUrl: "https://example.com/thumbnail-image.jpg",
      thumbnailVideoUrl: "https://example.com/thumbnail-video.mp4",
      aiDisclosure: "none",
    });

    // You can use the asset reference immediately
    console.log(asset.ref);

    // Use the asset reference to add a video element
    await addElementAtPoint({
      type: "video",
      ref: asset.ref,
    });
    ```
  </Tab>
</Tabs>

### Handling errors

A range of errors may occur when uploading assets. For example, if the user doesn't have enough storage space in their media library, a `"quota_exceeded"` error will be thrown:

```ts
import { type ImageRef, upload } from "@canva/asset";
import { CanvaError } from "@canva/error";

// If you are uploading an image that is derived from another image, pass its imageRef, otherwise set it as undefined
const parentRef = "PLACEHOLDER_IMAGE_REF" as ImageRef;

try {
  const asset = await upload({
    type: "image",
    parentRef,
    mimeType: "image/jpeg",
    url: "https://example.com/image.jpg",
    thumbnailUrl: "https://example.com/thumbnail.jpg",
    aiDisclosure: "none",
  });

  await asset.whenUploaded();
} catch (error) {
  if (error instanceof CanvaError) {
    if (error.code === "quota_exceeded") {
      console.error("The user is out of storage space.");
    } else {
      console.error("An error occurred:", error.code);
    }
  }
}
```

Some errors propagate from `whenUploaded`, so we recommend wrapping both methods in a try/catch block.

To learn more about handling errors in general, see [Handling errors](https://www.canva.dev/docs/apps/handling-errors/).

## Downloading assets

In some contexts, apps can download assets. For example, when a user [selects image or video content](https://www.canva.dev/docs/apps/selection/), an app can detect the selection of that content and download the underlying media.

### Getting asset URLs

Apps can use an asset's ref to generate a temporary URL for an asset. The app can then use this URL to download the underlying media. For security reasons, asset URLs expire after a short period of time.

Apps should use asset URLs as soon as possible, rather than storing them for later use.

<Tabs>
  <Tab name="Images">
    ```tsx
    import { getTemporaryUrl } from "@canva/asset";

    const imageRef = "..." as any; // Placeholder for the ref of the image

    const { url } = await getTemporaryUrl({
      type: "image",
      ref: imageRef,
    });

    console.log(url);
    ```
  </Tab>

  <Tab name="Videos">
    ```tsx
    import { getTemporaryUrl } from "@canva/asset";

    const videoRef = "..." as any; // Placeholder for the ref of the video

    const { url } = await getTemporaryUrl({
      type: "video",
      ref: videoRef,
    });

    console.log(url);
    ```
  </Tab>
</Tabs>

### Downloading assets via the frontend

The simplest way to download assets is via the frontend. The main downside of this approach is that it's impractical to process large files via the frontend, such as videos. It also consumes more of the user's bandwidth.

<Tabs>
  <Tab name="Images">
    ```tsx
    import { getTemporaryUrl } from "@canva/asset";

    const imageRef = "..." as any; // Placeholder for the ref of the image

    const { url } = await getTemporaryUrl({
      type: "image",
      ref: imageRef,
    });

    // Download the image using the Fetch API
    const response = await fetch(url);
    const blob = await response.blob();
    ```
  </Tab>

  <Tab name="Videos">
    ```tsx
    import { getTemporaryUrl } from "@canva/asset";

    const videoRef = "..." as any; // Placeholder for the ref of the video

    const { url } = await getTemporaryUrl({
      type: "video",
      ref: videoRef,
    });

    // Download the video using the Fetch API
    const response = await fetch(url);
    const blob = await response.blob();
    ```
  </Tab>
</Tabs>

### Downloading assets via the backend

The most versatile option is to pass the URL of the asset to the app's backend and download it there. This allows the app to process larger files in more complex ways, but it does require more code and infrastructure.

<Tabs>
  <Tab name="Images">
    ```tsx
    import { getTemporaryUrl } from "@canva/asset";

    const imageRef = "..." as any; // Placeholder for the ref of the image

    // Get a temporary URL for the image
    const { url } = await getTemporaryUrl({
      type: "image",
      ref: imageRef,
    });

    // Send the URL to your backend
    await fetch("https://your-backend.com/process-image", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ imageUrl: url }),
    });
    ```
  </Tab>

  <Tab name="Videos">
    ```tsx
    import { getTemporaryUrl } from "@canva/asset";

    // Get a temporary URL for the video
    const { url } = await getTemporaryUrl({
      type: "video",
      ref: videoRef,
    });

    // Send the URL to your backend
    await fetch("https://your-backend.com/process-video", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ videoUrl: url }),
    });
    ```
  </Tab>
</Tabs>

## Deriving assets

A common pattern for apps is to download an asset, modify it in some way, and then upload a new asset. For example, an app might download and apply an effect to an image.

When a new asset is created from an existing asset, it's known as a *derived asset*, and when an app uploads a derived asset, it must provide the ref of the asset it was derived from. We verify this during the [app review process](https://www.canva.dev/docs/apps/app-review-process/).

The following code sample demonstrates the basic flow of deriving an asset:

```tsx
import { upload, getTemporaryUrl } from "@canva/asset";

const originalImageRef = "..." as any; // Placeholder for the ref of the original image

// Get the original image
const { url } = await getTemporaryUrl({
  type: "image",
  ref: originalImageRef,
});

// Process the image in some way
const response = await fetch("https://your-backend.com/process-image", {
  method: "POST",
  body: JSON.stringify({ imageUrl: url }),
});
const { processedImageUrl } = await response.json();

// Upload the processed image as a derived asset
const derivedAsset = await upload({
  type: "image",
  mimeType: "image/jpeg",
  url: processedImageUrl,
  thumbnailUrl: processedImageUrl,
  aiDisclosure: "none",
  parentRef: originalImageRef,
});
```

This is required because Canva licenses assets from a number of creators and it's only by providing the ref of existing assets that Canva can ensure these licensing requirements are met.

A side-effect of this requirement is that apps are not allowed to combine multiple assets into a single asset, as the mechanism we use to track asset licensing only supports individual derived assets.

## API reference

* [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/)
