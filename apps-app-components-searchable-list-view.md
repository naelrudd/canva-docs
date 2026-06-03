Source: https://www.canva.dev/docs/apps/app-components/searchable-list-view/

# SearchableListView

How to use the SearchableListView component.

`SearchableListView` is a UI component that helps users find your images, videos, embeds, and audio.

### Filter options

```ts
{
  filterType: "CHECKBOX",
  label: "File Type",
  key: "fileType",
  options: [
    { value: "mp4", label: "MP4" },
    { value: "png", label: "PNG" },
  ],
  allowCustomValue: true,
},
```

### Sort options

```typescript
sortOptions: [
  { value: "created_at DESC", label: "Creation date (newest)" },
  { value: "created_at ASC", label: "Creation date (oldest)" },
];
```

### Layout

Three layout options: `LIST`, `MASONRY`, `FULL_WIDTH`.

## Example: Infinite scrolling

```typescript
findResources={async (request) => {
  const response = await fetch("http://localhost:3000/content/resources/find", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(request),
  });
}}
```

The `continuation` property enables pagination:

```typescript
const nextPage = (parseInt(currentPage, 10) + 1).toString();
const findResourcesResponse: FindResourcesResponse = {
  type: "SUCCESS",
  resources: images,
  continuation: nextPage,
};
```

## Localization

Strings in `SearchableListView` will be automatically localized for all supported locales.

## Export

Use the `saveExportedDesign` callback to export a Canva design:

```tsx
<SearchableListView
  config={config}
  findResources={findResources}
  saveExportedDesign={(exportedDesignUrl, containerId, designTitle) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve({ success: true });
      }, 1000);
    });
  }}
/>
```
