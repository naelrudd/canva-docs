Source: https://www.canva.dev/docs/apps/design-editing/

# Design Editing API

How to programmatically read and edit designs.

**Warning:** We're actively developing the Design Editing API.

The Design Editing API enables apps to read and edit the "ingredients" of a design, such as pages and elements.

## Core concepts

The Design Editing API centers around a single `openDesign` method:

```tsx
import { openDesign } from "@canva/design";
```

### Design contexts

```tsx
// Edit the current page only
await openDesign({ type: "current_page" }, async (session) => {
  console.log(session);
});

// Edit all pages in the design
await openDesign({ type: "all_pages" }, async (session) => {
  console.log(session);
});
```

### Sessions

Sessions have a **1-minute expiry**. The callback-based design encourages you to complete editing operations efficiently.

#### Current page sessions

```tsx
await openDesign({ type: "current_page" }, async (session) => {
  console.log(session.page);
  console.log(session.helpers);
  console.log(session.sync);
});
```

#### Multi-page sessions

```tsx
await openDesign({ type: "all_pages" }, async (session) => {
  for (const pageRef of session.pageRefs.toArray()) {
    await session.helpers.openPage(pageRef, async (pageResult) => {
      console.log(pageResult.page);
      console.log(pageResult.helpers);
    });
  }
});
```

### Syncing

```ts
await openDesign({ type: "current_page" }, async (session) => {
  if (session.page.type !== "absolute") return;

  const initialCount = session.page.elements.count();
  await session.sync();
  const updatedCount = session.page.elements.count();
});
```

### Lists

The Design Editing API uses special "list" data structures. Lists are used for `page.elements`, `group.contents`, `shape.paths`, etc.

**List methods:**
* **Reading**: `count`, `toArray`, `forEach`, `filter`
* **Mutating**: `insertBefore`, `insertAfter`, `moveBefore`, `moveAfter`, `delete`

## Pages

### Page types

```ts
await openDesign({ type: "current_page" }, async (session) => {
  console.log(session.page.type); // => "absolute" or "unsupported"
});
```

#### Absolute pages

```ts
await openDesign({ type: "current_page" }, async (session) => {
  if (session.page.type === "absolute") {
    if (session.page.dimensions) {
      console.log("The current page has fixed dimensions.");
    } else {
      console.log("The current page has unbounded dimensions.");
    }
  }
});
```

### Locked pages

```ts
await openDesign({ type: "current_page" }, async (session) => {
  if (session.page.locked) {
    console.log("The current page is locked, so no edits are allowed.");
    return;
  }
});
```

## Multi-page editing

**Warning:** The `all_pages` design context is currently in preview.

```ts
await openDesign({ type: "all_pages" }, async (session) => {
  for (const pageRef of session.pageRefs.toArray()) {
    if (pageRef.type !== "absolute" || pageRef.locked) continue;

    await session.helpers.openPage(pageRef, async (pageResult) => {
      console.log(`Editing page with ${pageResult.page.elements.count()} elements`);
    });
  }
  await session.sync();
});
```

## Backgrounds

```ts
await openDesign({ type: "current_page" }, async (session) => {
  if (session.page.type !== "absolute") return;

  if (!session.page.background) {
    console.log("The page doesn't have a background.");
    return;
  }

  console.log(session.page.background); // => Fill
});
```

## Elements

Supported element operations: Creating, Reading, Updating, Deleting.

### Locked elements

```ts
const textElement = session.page.elements
  .toArray()
  .find(
    (element): element is DesignEditing.TextElement => element.type === "text"
  );

if (textElement.locked) {
  console.log("The element is locked and can't be modified.");
}
```

### Creating elements

```ts
const circleState = session.helpers.elementStateBuilder.createShapeElement({
  top: 100,
  left: 350,
  width: 100,
  height: 100,
  viewBox: { top: 0, left: 0, width: 100, height: 100 },
  paths: [{
    d: "M 50 0 A 50 50 0 1 1 50 100 A 50 50 0 1 1 50 0 Z",
    fill: { colorContainer: { type: "solid", color: "#0099ff" } }
  }]
});

session.page.elements.insertAfter(undefined, circleState);
await session.sync();
```

### Reading elements

```ts
session.page.elements.forEach((element, index) => {
  console.log(`Element ${index}: ${element.type}`);
  console.log(`Position: ${element.top}, ${element.left}`);
});

const textElements = session.page.elements.filter(
  (element): element is DesignEditing.TextElement => element.type === "text"
);
```

### Updating elements

```ts
session.page.elements.forEach((element) => {
  if (element.type === "unsupported" || element.locked) return;
  element.top += 50;
  element.left += 50;
  element.rotation += 15;
  element.transparency = 0.8;
});

await session.sync();
```

### Deleting elements

```ts
const elements = session.page.elements.toArray();
if (elements.length > 0) {
  session.page.elements.delete(elements[0]);
}
await session.sync();
```

## Element types

Supported: Embeds, Groups, Rects, Shapes, Text.

### Embed elements

```ts
const embedElementState = session.helpers.elementStateBuilder.createEmbedElement({
  top: 50, left: 50, width: 560, height: 315,
  url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
});
```

### Group elements

```ts
const groupElement = await session.helpers.group({
  elements: [addedRect, addedText],
});

const ungroupedElements = await session.helpers.ungroup({
  element: groupElement,
});
```

### Rect elements

```ts
const rectElementState = session.helpers.elementStateBuilder.createRectElement({
  top: 50, left: 50, width: 200, height: 150,
  fill: { colorContainer: { type: "solid", color: "#ff6b6b" } },
});
```

### Shape elements

```ts
const shapeElementState = session.helpers.elementStateBuilder.createShapeElement({
  top: 100, left: 100, width: 100, height: 100,
  viewBox: { top: 0, left: 0, width: 100, height: 100 },
  paths: [{ d: "M 50 0 A 50 50 0 1 1 50 100 A 50 50 0 1 1 50 0 Z", fill: { colorContainer: { type: "solid", color: "#3498db" } } }],
});
```

### Text elements

```ts
const textElementState = session.helpers.elementStateBuilder.createTextElement({
  top: 50, left: 50, width: 300,
  text: { regions: [{ text: "Hello, Canva!", formatting: { fontSize: 32, color: "#2c3e50", fontWeight: "bold", textAlign: "center" } }] },
});
```

## Fills

Supported fill types: Colors, Images, Videos.

(Full documentation includes detailed reading, setting, and clearing fills for backgrounds, rects, and shapes.)
