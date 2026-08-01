Source: https://www.canva.dev/docs/apps/grouping-elements/

# Grouping elements

How to organize elements into groups.

In Canva, a design's elements can be organized into groups. The elements in these groups can then be manipulated as a single unit, which is more convenient when working on complex designs.

## The user experience

A group can be moved, resized, rotated, and animated as a single unit.

For fine-grained control, users can select and edit any of the individual elements in a group — for example, to apply effects to a specific image.

Users have the option of *locking* a group. When a group is locked, it can't be ungrouped, and its elements can't be edited. If a group is not locked, it can be ungrouped into its individual elements.

## What can be grouped?

The following types of elements can be organized into groups:

* [Embeds](https://www.canva.dev/docs/apps/embedding-rich-media/)
* [Images](https://www.canva.dev/docs/apps/creating-images/)
* [Shapes](https://www.canva.dev/docs/apps/creating-shapes/)
* [Text](https://www.canva.dev/docs/apps/creating-text/)
* [Videos](https://www.canva.dev/docs/apps/creating-videos/)

The following types of elements *cannot* be organized into groups:

* [App elements](https://www.canva.dev/docs/apps/creating-app-elements/)
* Groups
* [Tables](https://www.canva.dev/docs/apps/creating-tables/)

## How to create groups

### Step 1: Enable the required scopes

Enable the `canva:design:content:write` scope with either the Developer Portal or the Canva CLI. In the future, the Apps SDK will throw an error if the required scopes aren't enabled. To learn more, see [Configuring scopes](https://www.canva.dev/docs/apps/configuring-scopes/).

### Step 2: Add the group to the design

Import the `addElementAtPoint` method (or `addElementAtCursor`, [depending on the current context](https://www.canva.dev/docs/apps/elements/#creating-elements)) from the `@canva/design` package:

```ts
import { addElementAtPoint } from "@canva/design";
```

Call the method, passing in the options shown here:

```ts
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
```

The `children` property should contain the elements to include in the group. The elements will render in the order they appear — that is, later elements will render in front of earlier elements.

Each object in the `children` array:

* Must have a `width` and a `height`
* Must have `top` and `left` coordinates
* Can have a `rotation`, in degrees

The one exception is [text elements](https://www.canva.dev/docs/apps/creating-text/), which don't require a `width` and can't have a `height`.

To learn more about how to position elements within a group, see [Positioning elements](https://www.canva.dev/docs/apps/positioning-elements/).

## Known limitations

* Groups must contain at least two elements.
* Apps can't create locked groups.

## API reference

* [`addElementAtPoint`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/)

## Code sample

```tsx
import React from "react";
import { addElementAtPoint } from "@canva/design";
import { Button, Rows } from "@canva/app-ui-kit";
import * as styles from "styles/components.css";

export function App() {
  async function handleClick() {
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

  return (
    <div className={styles.scrollContainer}>
      <Rows spacing="2u">
        <Button variant="primary" onClick={handleClick}>
          Add group to design
        </Button>
      </Rows>
    </div>
  );
}
```
