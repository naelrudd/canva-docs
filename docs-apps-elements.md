Source: https://www.canva.dev/docs/apps/elements/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Elements

An introduction to elements in the Apps SDK.

In Canva, users can add *elements* to their designs.

An element is a container that holds some kind of [content](https://www.canva.dev/docs/apps/content/), such as image content, and can be arranged in a user's design, such as by setting its dimensions and position.

Apps can create and otherwise interact with elements in a variety of ways.

## Elements vs. content

Content is the underlying media or text that exists within an element. Elements are a container with a specific set of dimensions that holds content. For example, a user uploads their image content into the image element on their design.

**Content, however, doesn't always align with an element.**

For example, a page background may contain image content, but the page background isn't an image element. Similarly, a table cell may contain text content, but table cells aren't text elements.

If your app needs to operate on the elements of a design, see the following sections and code samples, as well as the [Design Editing](https://www.canva.dev/docs/apps/design-guidelines/design-editing-api/) guidelines for more information. If instead your app needs to edit the text, image, or video content found within the elements of a design, see the [Content](https://www.canva.dev/docs/apps/content/) guide, and the [Content Querying](https://www.canva.dev/docs/apps/design-guidelines/content-querying-api/) guidelines for more information.

## Element types

Apps can interact with wide variety of element types, including:

* [Embeds](https://www.canva.dev/docs/apps/embedding-rich-media/)
* [Images](https://www.canva.dev/docs/apps/creating-images/)
* [Groups](https://www.canva.dev/docs/apps/grouping-elements/)
* [Shapes](https://www.canva.dev/docs/apps/creating-shapes/)
* [Tables](https://www.canva.dev/docs/apps/creating-tables/)
* [Text](https://www.canva.dev/docs/apps/creating-text/)
* [Richtext](https://www.canva.dev/docs/apps/creating-text/)
* [Videos](https://www.canva.dev/docs/apps/creating-videos/)

To learn more about each element type, see the linked pages.

Additional types will be supported in the future.

## App elements

There's a special type of element called an *app element*. An app element is essentially a group element with metadata attached to it. This metadata allows the app to create custom, re-editable elements.

Although app elements share characteristics with elements in general, they're unique enough that they're documented separately. To learn more, see [App elements](https://www.canva.dev/docs/apps/creating-app-elements/).

## Creating elements

Apps can create elements by calling either of the following methods:

* `addElementAtPoint`
* `addElementAtCursor`

Both methods add an element to the user's design, but:

* `addElementAtPoint` accepts an (optional) position and is only compatible with design types that support absolute positions, which is all design types except for documents.
* `addElementAtCursor` doesn't accept a position and is only compatible with design types that contain streams of text, which is only the document design type.

The supported elements also depend on the method being called:

| Element type | addElementAtPoint | addElementAtCursor |
| ------------ | ----------------- | ------------------ |
| Embeds       | ✅                 | ✅                  |
| Images       | ✅                 | ✅                  |
| Groups       | ✅                 | ❌                  |
| Shapes       | ✅                 | ❌                  |
| Tables       | ✅                 | ✅                  |
| Text         | ✅                 | ✅                  |
| Richtext     | ✅                 | ✅                  |
| Videos       | ✅                 | ✅                  |

Where possible, apps should determine the context in which the app is running and either call the compatible method or make it obvious when functionality isn't available:

```tsx
import { Button, Rows } from "@canva/app-ui-kit";
import { addElementAtCursor, addElementAtPoint } from "@canva/design";
import { useFeatureSupport } from "@canva/app-hooks";
import * as styles from "styles/components.css";

export const App = () => {
  const isSupported = useFeatureSupport();
  const addElement = [addElementAtPoint, addElementAtCursor].find((fn) =>
    isSupported(fn),
  );

  function handleClick() {
    addElement?.({
      type: "text",
      children: ["Hello world"],
    });
  }

  return (
    <div className={styles.scrollContainer}>
      <Rows spacing="1u">
        <Button
          variant="primary"
          onClick={handleClick}
          disabled={!addElement}
          tooltipLabel={!addElement ? "This feature is not supported in the current page" : undefined}
        >
          Add element
        </Button>
      </Rows>
    </div>
  );
};
```

To learn more, see [Feature support](https://www.canva.dev/docs/apps/feature-support/).

## Positioning elements

The `addElementAtPoint` method accepts an optional set of dimensions and position:

```tsx
import { addElementAtPoint } from "@canva/design";

// Upload an image asset
const asset = await upload({
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
  ref: asset.ref,
  top: 50,
  left: 50,
  width: 1280,
  height: 720,
});
```

These properties must be used together or not at all. If a position isn't provided, the element is added to the center of the design.

### Auto-calculating dimensions

You can set either the `width` or `height` properties to `"auto"`:

```tsx
import { addElementAtPoint } from "@canva/design";

// Upload an image asset
const asset = await upload({
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
  ref: asset.ref,
  top: 0,
  left: 0,
  width: 1280,
  height: "auto",
});
```

This maintains the aspect ratio of the element without having to specify a pixel value.

### Rotating elements

The `addElementAtPoint` method accepts a rotation:

```tsx
import { addElementAtPoint } from "@canva/design";

// Upload an image asset
const asset = await upload({
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
  ref: asset.ref,
  top: 0,
  left: 0,
  width: 1280,
  height: "auto",
  rotation: 90,
});
```

This rotation only has an effect if the element has dimensions and a position.

### Feature support for positioned elements

When positioning elements, you should check for feature support to make sure `addElementAtPoint` is supported in the current design type.

The positioning properties (`top`, `left`, `width`, `height`, and `rotation`) are only available when using the `addElementAtPoint` method. These properties aren't available with `addElementAtCursor`, which is designed for responsive documents that use a text-based flow.

Some element types, such as groups and shapes, require these positioning properties. For example, when creating a group, each child element must have `top`, `left`, `width`, and `height` properties to define their position within the group.

```tsx
import { Button, Rows } from "@canva/app-ui-kit";
import { addElementAtPoint } from "@canva/design";
import { useFeatureSupport } from "@canva/app-hooks";
import * as styles from "styles/components.css";

export const App = () => {
  const isSupported = useFeatureSupport();
  const isAddElementAtPointSupported = isSupported(addElementAtPoint);

  function handleClick() {
    addElementAtPoint({
      type: "group",
      children: [
        {
          type: "shape",
          paths: [
            {
              d: "M 0 0 H 100 V 100 H 0 L 0 0",
              fill: { color: "#ff0099" },
            },
          ],
          viewBox: { width: 100, height: 100, top: 0, left: 0 },
          top: 0,
          left: 0,
          width: 100,
          height: 100,
        },
        {
          type: "shape",
          paths: [
            {
              d: "M 50 0 L 100 100 L 0 100 Z",
              fill: { color: "#00ff99" },
            },
          ],
          viewBox: { width: 100, height: 100, top: 0, left: 0 },
          top: 0,
          left: 110,
          width: 100,
          height: 100,
        },
      ],
    });
  }

  return (
    <div className={styles.scrollContainer}>
      <Rows spacing="1u">
        <Button
          variant="primary"
          onClick={handleClick}
          disabled={!isAddElementAtPointSupported}
          tooltipLabel={
            !isAddElementAtPointSupported
              ? "Positioned elements are not supported in this design type"
              : undefined
          }
        >
          Add positioned group
        </Button>
      </Rows>
    </div>
  );
};
```

To learn more about feature support, see [Feature support](https://www.canva.dev/docs/apps/feature-support/). For more information about groups and shapes, see [Grouping elements](https://www.canva.dev/docs/apps/grouping-elements/) and [Creating shapes](https://www.canva.dev/docs/apps/creating-shapes/).

## Element traversal

Apps can traverse the elements in a user's design. This allows the app to read and update the structure of the design and the content of its elements. To learn more, see [Design Editing API](https://www.canva.dev/docs/apps/design-editing/).
