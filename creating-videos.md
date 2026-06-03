Source: https://www.canva.dev/docs/apps/creating-videos/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating videos

How to add videos to a user's design.

Apps can add videos to a user's design, such as MP4 and MOV files. The user can arrange these videos in a Canva design or splice them together in Canva's video editor.

**Note:** To add videos from third-party sources, such as YouTube, see [Embedding rich media](https://www.canva.dev/docs/apps/embedding-rich-media/).

## The user experience

When an app adds a video to the user's design, the video file is uploaded to the user's media library. While the video is uploading, a lower-resolution version of the video is shown to the user.

The user's media library has a storage quota. If the user has a [Canva Pro](https://www.canva.com/pro/) account, their storage quota is 1TB. Otherwise, their storage quota is 5GB.

## Supported video types

| Name      | MIME types                 | Common file extensions |
| --------- | -------------------------- | ---------------------- |
| AVI       | video/avi, video/x-msvideo | .avi                   |
| GIF       | image/gif                  | .gif                   |
| Lottie    | application/json           | .json                  |
| M4V       | video/x-m4v                | .m4v                   |
| Matroska  | video/x-matroska           | .mkv                   |
| QuickTime | video/quicktime            | .mov                   |
| MP4       | video/mp4                  | .mp4                   |
| MPEG      | video/mpeg                 | .mpg, .mpeg            |
| WebM      | video/webm                 | .webm                  |

The maximum allowed video file size is 100MB (0.5MB for Lottie files).

### Lottie file limitations

* Max size: 0.5MB (500KB)
* Must not exceed 10 seconds or 2048 x 2048 pixels
* Must not contain 3D layers, font references, media assets, or property expressions
* Compositions must not contain 3D layers, audio, gradient stroke shapes, images, solids, star shapes, text, time remapping, or time stretching

## How to create videos

### Step 1: Enable the required scopes

Enable `canva:design:content:write` and `canva:asset:private:write`.

### Step 2: Upload a video file

```ts
import { upload } from "@canva/asset";

const result = await upload({
  type: "video",
  mimeType: "video/mp4",
  url: "https://www.canva.dev/example-assets/video-import/video.mp4",
  thumbnailImageUrl: "https://www.canva.dev/example-assets/video-import/thumbnail-image.jpg",
  thumbnailVideoUrl: "https://www.canva.dev/example-assets/video-import/thumbnail-video.mp4",
  aiDisclosure: "none",
});
```

### Step 3: Add the video to the design

```ts
import { addElementAtPoint } from "@canva/design";

await addElementAtPoint({
  type: "video",
  ref: result.ref,
  altText: {
    text: "Video description for accessibility",
    decorative: false
  },
});
```

## API reference

* [`addElementAtPoint`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/)
* [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/)

## Code sample

```tsx
import React from "react";
import { addElementAtPoint } from "@canva/design";
import { upload } from "@canva/asset";

export function App() {
  async function handleClick() {
    const result = await upload({
      type: "video",
      mimeType: "video/mp4",
      url: "https://www.canva.dev/example-assets/video-import/video.mp4",
      thumbnailImageUrl: "https://www.canva.dev/example-assets/video-import/thumbnail-image.jpg",
      thumbnailVideoUrl: "https://www.canva.dev/example-assets/video-import/thumbnail-video.mp4",
      aiDisclosure: "none",
    });

    await addElementAtPoint({
      type: "video",
      ref: result.ref,
      altText: {
        text: "Video description for accessibility",
        decorative: false
      },
    });
  }

  return (
    <div>
      <button onClick={handleClick}>Add video to design</button>
    </div>
  );
}
```
