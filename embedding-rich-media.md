Source: https://www.canva.dev/docs/apps/embedding-rich-media/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Embedding rich media

How to embed rich media in a user's design.

Across the internet, all sorts of media is designed to be embedded, from YouTube videos to Instagram photos to GitHub gists. Users can easily embed this media in their Canva designs, and so can apps.

## The user experience

When a user adds an embed to their design, the media is embedded in an iframe. The user can then manipulate the position, rotation, and size of the embed.

Some embeds are interactive. For example, users can watch embedded YouTube videos.

Unlike images, videos, and text, users can't apply effects to embeds. This is because Canva doesn't have access to the underlying media in the embed's iframe.

## Supported media sources

Behind the scenes, Canva uses [Iframely](https://iframely.com/) to embed media from thousands of different platforms. This means apps can embed any media that's supported by the Iframely API.

To check if a URL is supported by Iframely, see [What URLs to send to Iframely](https://iframely.com/docs/providers).

## How to embed rich media

### Step 1: Enable the required scopes

Enable the `canva:design:content:write` scope.

### Step 2: Add the embed to the design

```ts
import { addElementAtPoint } from "@canva/design";

await addElementAtPoint({
  type: "embed",
  url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
});
```

The `url` property must contain an Iframely-supported URL.

## Known limitations

* Iframely can't embed arbitrary HTML files. It can only embed media supported by its API.
* If the original media is deleted, an error is displayed in place of the media.
* If the original media changes, the changes are not immediately reflected in the user's design.

## API reference

* [`addElementAtPoint`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/)

## Code sample

```tsx
import React from "react";
import { addElementAtPoint } from "@canva/design";

export function App() {
  async function handleClick() {
    await addElementAtPoint({
      type: "embed",
      url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    });
  }

  return (
    <div>
      <button onClick={handleClick}>Add embed to design</button>
    </div>
  );
}
```
