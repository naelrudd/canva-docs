Source: https://www.canva.dev/docs/apps/positioning-elements/

# Positioning elements

How to arrange elements in a user's design.

By default, adding an element to the user's design positions the element in the center of the page and scales it to a size that's determined by Canva.

Likewise, elements inside [groups](https://www.canva.dev/docs/apps/grouping-elements/) and [app elements](https://www.canva.dev/docs/apps/creating-app-elements/) have default positions and scaling.

Apps can, however, override these values to set the position of elements in either context.

## Feature support considerations

Apps can position elements in responsive and fixed [Canva design types](https://www.canva.dev/docs/apps/designs/#design-types) depending on the method:

* `addElementAtPoint` only works in fixed design types, such as Presentations.
* `addElementAtCursor` only works in responsive design types, such as Canva docs.
* `getCurrentPageContext` only works in fixed design types.

See [Feature support](https://www.canva.dev/docs/apps/feature-support/) for more information.

## How to position elements on a page

The syntax for positioning an element depends on the method that renders the element.

When calling the [`addElementAtPoint`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/) method (or [`addElementAtCursor`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-cursor/), [depending on the current context](https://www.canva.dev/docs/apps/elements/#creating-elements)), pass the position in with the first argument:

```ts
await addElementAtPoint({
  type: "embed",
  url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",

  // Position
  width: 640,
  height: 360,
  top: 0,
  left: 0,
  rotation: 0,
});
```

When calling the [`addOrUpdateElement`](https://www.canva.dev/docs/apps/api/latest/design-init-app-element/) method, pass the position in as the second argument:

```ts
appElement.addOrUpdateElement(
  {
    // app element data goes here
  },
  {
    // Position
    width: 640,
    height: 360,
    top: 0,
    left: 0,
    rotation: 0,
  }
);
```

In both cases, the following properties must be used together:

* `width`
* `height`
* `top`
* `left`

The `rotation` property is always optional, but only has an effect if the positional properties are set.

### Using the dimensions of the current page

1. In the Developer Portal, enable the `canva:design:content:read` scope. In the future, the Apps SDK will throw an error if the required scopes aren't enabled. To learn more, see [Configuring scopes](https://www.canva.dev/docs/apps/configuring-scopes/).
2. Call the [`getCurrentPageContext`](https://www.canva.dev/docs/apps/api/latest/design-get-current-page-context/) method:

   ```ts
   import { getCurrentPageContext } from "@canva/design";
   const context = await getCurrentPageContext();
   console.log(context.dimensions); // => { width: 1280, height: 720 }
   ```

   The method returns a `dimensions` property that you can use to:

   * Position elements within the bounds of the current page.
   * Position elements in relative terms — for example, in the bottom-right corner.

**Warning:** Some types of designs, such as [whiteboards](https://www.canva.com/online-whiteboard/), don't have dimensions. In these cases, the `dimensions` property will be `undefined`.

## How to position elements in groups and app elements

You can set the position of elements inside groups and app elements, and since app elements are essentially groups with extra features, the approach to positioning elements is the same.

### Box model

You can think of an app element and a group as a box.

By default, the box doesn't have a width or height. Instead, the size of the box is based on the size and spacing between the elements it contains.

### Dimensions

The elements inside a box must have a width and a height. (The one exception is [text elements](https://www.canva.dev/docs/apps/creating-text/), which can't have a predefined height.)

When the width is defined as a number, the height can be set to `"auto"` (and vice versa). At runtime, Canva replaces `"auto"` with a value that maintains the aspect ratio of the element.

**Warning:** You can't set *both* the width and height to `"auto"`. At least one value must be a number.

### Coordinates

Within a box, elements can be positioned with `top` and `left` coordinates. These coordinates are relative to the box's *origin* — that is, the top-left corner of the box.

The origin is determined by the box's topmost and leftmost elements. For example, if the topmost element has a `top` position of `50` and the leftmost element has a `left` position of `100`, then:

* The top and left coordinates of the box start from `50` and `100`
* The top and left coordinates of all other elements are relative to `50` and `100`

This can be confusing — especially if you're using negative values for positions — so we recommend treating the `top` and `left` coordinates as `0` and `0`, even though this isn't strictly required.

### Spacing

Elements can be positioned to overlap or to have spacing between them. The size of the box grows or shrinks to accommodate for the combined size of the elements.

When elements overlap, the ordering of the elements is determined by the order in which the elements are rendered. The elements later in an array are rendered in front of elements earlier in the array.

### Padding

Boxes do not have padding. There's always one element positioned against each edge of the box.

### Units of measurement

Within a box, dimensions and coordinates are defined with relative units, not absolute units. This means `200` is always twice as large as `100`, but these numbers don't correspond to pixel values.

The end result is that, if a design is 1920 pixels × 1280 pixels, setting the dimensions of a box's elements to a combined size of 1920 pixels × 1280 pixels will not necessarily result in the box extending to the edges of the design. Instead, the box will be scaled to a size that's calculated by Canva.

*How* Canva determines the absolute size of elements depends on a variety of factors that may change over time and is beyond the scope of this documentation.

The key takeaway is to **never treat dimensions or coordinates within a box as absolute values**.

## API reference

* [`addElementAtPoint`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/)
* [`getCurrentPageContext`](https://www.canva.dev/docs/apps/api/latest/design-get-current-page-context/)
* [`initAppElement`](https://www.canva.dev/docs/apps/api/latest/design-init-app-element/)

## Code samples

### Positioning app elements

```tsx
import { Button, Rows } from "@canva/app-ui-kit";
import { getCurrentPageContext, initAppElement } from "@canva/design";
import * as styles from "styles/components.css";
import { useFeatureSupport } from "@canva/app-hooks";

const appElement = initAppElement({
  render: () => {
    return [
      {
        type: "embed",
        url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        width: 640,
        height: 360,
        top: 0,
        left: 0,
      },
    ];
  },
});

export function App() {

  const isSupported = useFeatureSupport();

  async function handleClick() {
    if (!isSupported(getCurrentPageContext)) {
     const context = await getCurrentPageContext();

     if (!context.dimensions) {
       console.warn("The current design does not have dimensions");
       return;
     }

     const width = 640;
     const height = 360;
     const top = context.dimensions.height - height;
     const left = context.dimensions.width - width;

     await appElement.addOrUpdateElement(
       {
         // app element data goes here
       },
       {
         width,
         height,
         top,
         left,
       }
     );
   }
  }

  return (
    <div className={styles.scrollContainer}>
      <Rows spacing="2u">
        <Button
          variant="primary"
          onClick={handleClick}
          disabled={!isSupported(getCurrentPageContext)}
          >
          Create positioned app element
        </Button>
      </Rows>
    </div>
  );
}
```

### Positioning native elements

```tsx
import { Button, Rows } from "@canva/app-ui-kit";
import { addElementAtPoint, addElementAtCursor, getCurrentPageContext } from "@canva/design";
import { useFeatureSupport } from "@canva/app-hooks";
import * as styles from "styles/components.css";

export function App() {

  const isSupported = useFeatureSupport();

  async function handleClick() {
    if (!isSupported(getCurrentPageContext)) {
     const context = await getCurrentPageContext();

     if (!context.dimension) {
       console.warn("The current design does not have dimensions");
       return;
     }

     const width = 640;
     const height = 360;
     const top = context.dimensions.height - height;
     const left = context.dimensions.width - width;

     if (isSupported(addElementAtPoint)) {
       await addElementAtPoint({
         type: "embed",
         url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
         width,
         height,
         top,
         left,
       });
     }
   }
  }

   async function handleAddElementAtCursor() {
    if (!isSupported(addElementAtPoint)) { // Check the design type and use addElementAtCursor if addElementAtPoint isn't supported
      await addElementAtCursor({
        type: "text",
        children: ["Adding content at Cursor."]
      })
    }
  }

  return (
    <div className={styles.scrollContainer}>
      <Rows spacing="2u">
        <Button
          variant="primary"
          onClick={handleClick}
          disabled={!isSupported(addElementAtPoint)}
          >
          Create positioned native element
        </Button>
        <Button
          variant="secondary"
          onClick={handleAddElementAtCursor}
          disabled={!isSupported(addElementAtCursor)}
          >
          Create native element at cursor
        </Button>
      </Rows>
    </div>
  );
}
```

### Positioning elements in groups and app elements

```tsx
import { addElementAtPoint } from "@canva/design";
import { useFeatureSupport } from "@canva/app-hooks";
import { Button, Rows } from "@canva/app-ui-kit";
import * as styles from "styles/components.css";

export function App() {
  const isSupported = useFeatureSupport();
  async function handleClick() {
    if (isSupported(addElementAtPoint)) {
      await addElementAtPoint({
        type: "group",
        children: [
          {
            type: "embed",
            url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            width: 100,
            height: 100,
            top: 0,
            left: 0,
          },
          {
            type: "embed",
            url: "https://www.youtube.com/watch?v=o-YBDTqX_ZU",
            width: 100,
            height: 100,
            top: 0,
            left: 100,
          },
        ],
      });
    }
  }

  return (
    <div className={styles.scrollContainer}>
      <Rows spacing="2u">
        <Button
          variant="primary"
          onClick={handleClick}
          disabled={!isSupported(addElementAtPoint)}
          >
          Add group element
        </Button>
      </Rows>
    </div>
  );
}
```
