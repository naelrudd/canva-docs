Source: https://www.canva.dev/docs/apps/upgrades-and-migrations/v2-migration-guide/

# Apps SDK v2 Upgrade guide

How to upgrade to Apps SDK v2.

## Automated migration tool

```shell
canva apps migrate apps-sdk-v1-v2
```

## Manual migration steps

### Packages

```shell
npm install @canva/asset@latest @canva/design@latest @canva/error@latest @canva/platform@latest @canva/user@latest
```

### AI disclosure

```tsx
await upload({
  type: "audio",
  title: "Example audio",
  url: "https://...",
  mimeType: "audio/mp3",
  aiDisclosure: "none", // => Or "app_generated"
});
```

### Alternative text

```tsx
await addElementAtPoint({
  type: "image",
  ref: result.ref,
  altText: {
    text: "Example image",
    decorative: false,
  },
});
```

### Authentication

Manual authentication has been removed in v2. Use [Frictionless auth](https://www.canva.dev/docs/apps/authenticating-users/frictionless/) or [OAuth](https://www.canva.dev/docs/apps/authenticating-users/oauth/).

### Feature support

```tsx
const isSupported = useFeatureSupport();
const addElement = [addElementAtPoint, addElementAtCursor].find((fn) =>
  isSupported(fn),
);
```

### Adding elements

`addNativeElement` deprecated in v2. Superseded by:
* `addElementAtPoint`
* `addElementAtCursor`

### Asset IDs

The `id` property has been removed from the `upload` method.

### Discriminators

All discriminator values are now lowercase (e.g., `"EMBED"` → `"embed"`).

### Drag and drop

`startDrag` deprecated, `makeDraggable` removed. Use:
* `startDragToPoint`
* `startDragToCursor`

### Uploading assets

`queueMediaUpload` and `whenUploaded` have been removed. Use only `upload`.
