Source: https://www.canva.dev/docs/apps/selection/

# Selection API

Read, transform, and write the user's current selection.

The Selection API allows apps to read and replace the [content](https://www.canva.dev/docs/apps/content/) of the user's current selection.

## Supported content types

* Images (not including SVGs)
* Plaintext
* Richtext
* Videos

## Scopes

* If your app only reads content, enable `canva:design:content:read`.
* If your app replaces plaintext or richtext content, enable `canva:design:content:read` and `canva:design:content:write`.
* If your app replaces image or video content, enable `canva:design:content:read`, `canva:design:content:write`, `canva:asset:private:read`, and `canva:asset:private:write`.

## Listening for selection events

```ts
import { useSelection } from "@canva/app-hooks";

const selectedContent = useSelection("plaintext");
```

Supported values: `"image"`, `"plaintext"`, `"richtext"`, `"video"`.

## Checking if content is selected

```ts
const isContentSelected = selectedContent.count > 0;
```

## Reading selected content

```ts
const draft = await selectedContent.read();

for (const content of draft.contents) {
  console.log(content.ref);  // for images/videos
  console.log(content.text); // for plaintext
}
```

### Richtext

```tsx
const draft = await selectedContent.read();

for (const content of draft.contents) {
  const regions = content.readTextRegions();
  for (const region of regions) {
    console.log(region.text);
    console.log(region.formatting);
  }
}
```

## Replacing selected content

The basic workflow:
1. Read the current selection: `const draft = await selectedContent.read();`
2. Loop through contents and transform them.
3. Save: `await draft.save();`

### Images

```ts
for (const content of draft.contents) {
  const { url } = await getTemporaryUrl({ type: "image", ref: content.ref });
  const transformedImage = await transformImage(url);
  const asset = await upload({
    type: "image", url: transformedImage.url, mimeType: transformedImage.mimeType,
    thumbnailUrl: transformedImage.thumbnailUrl, parentRef: content.ref, aiDisclosure: "none",
  });
  content.ref = asset.ref;
}
await draft.save();
```

### Plaintext

```ts
for (const content of draft.contents) {
  content.text = `${content.text} was modified!`;
}
await draft.save();
```

### Videos

Similar to images — download, transform, upload, replace ref.

## Known limitations

* Apps can only read and replace raster images — not vector images.
* You can't replace one type of content with a different type of content.
* The ordering of multiple selected content items is not stable.
