Source: https://www.canva.dev/docs/apps/creating-shapes/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating shapes

How to add shapes to a user's design.

Shapes are fundamental elements that users can add to their Canva designs. There are a number of shapes built into Canva, such as circles and rectangles, and apps can create their own shapes.

## Why create shapes?

* Shapes can be resized without becoming blurry.
* Shapes are faster to create than equivalent images.
* Shapes don't count against a user's upload quota.

## The user experience

After an app adds a shape to a user's design, the shape is indistinguishable from Canva's built-in shapes. This means the user can manipulate the shape in all the same ways, including:

* Moving, resizing, and rotating the shape
* Adjusting the color(s) of the shapes

## The anatomy of shapes

Shapes are comparable to Scalable Vector Graphics (SVGs), in that they're made up of paths, fills, strokes, and a view box. There are, however, some nuances that distinguish them from SVGs.

### Paths

A *path* is a combination of one or more lines that forms a shape. For example, a path could be a single line that forms a circle or a combination of lines that forms a hexagon.

By themselves, paths are not visible. They define the boundaries of a shape but not the contents of a shape. For a path to be made visible, it requires a fill or a stroke.

#### Using path commands

A *path command* defines the position, length, and curvature of a path.

Path commands are made up of two ingredients:

* A letter that defines what the path command does
* A list of numeric parameters

For example, the following path commands draw a square:

```
M 0 0
H 100
V 100
H 0
L 0 0
```

#### Supported path commands

When creating shapes, the following path commands are available:

* **MoveTo**: M, m
* **LineTo**: L, l, H, h, V, v
* **Cubic Bezier Curve**: C, c, S, s
* **Elliptical Arc Curve**: A, a
* **ClosePath**: Z, z

A command that is available to SVGs but is *not* available to shapes is the `Q` command, which is used to create quadratic Bezier curves.

#### Path limitations

* A shape must have between 1 and 30 paths.
* The maximum combined size of all paths must not exceed 2kb.
* Paths must start with an `M` command.
* Paths must not have more than one `M` command.
* Paths must not use the `Q` command.
* Paths must be closed in either of the following ways:
  * With a `Z` command at the end
  * By having the last coordinate match the first coordinate

### Fills

A *fill* defines the interior of a path. It can be a color, an image, or a video. The maximum number of unique fill colors across a shape's paths must not exceed 6.

### Strokes

A *stroke* is an outline that can be applied to a path. This outline is rendered along the edges of a path and can be configured with a custom weight (width) and color.

### View box

The *view box* is a rectangular area that defines the coordinates of the shape. It determines how the shape should be scaled, rotated, or positioned.

## How to create shapes

### Step 1: Enable the required scopes

Enable the `canva:design:content:write` scope.

### Step 2: Add to the shape to the design

```ts
import { addElementAtPoint } from "@canva/design";

await addElementAtPoint({
  type: "shape",
  paths: [
    {
      d: "M 0 0 H 100 V 100 H 0 L 0 0",
      fill: {
        color: "#ff0099",
      },
    },
  ],
  viewBox: {
    height: 100,
    width: 100,
    left: 0,
    top: 0,
  },
});
```

## How to create drop targets

Set the `dropTarget` property to `true` on a fill to allow users to drag and drop images or videos onto it.

## How to use image and video fills

Upload an image or video and pass the `ref` property into the fill:

```ts
await addElementAtPoint({
  type: "shape",
  paths: [
    {
      d: "M 0 0 H 100 V 100 H 0 L 0 0",
      fill: {
        dropTarget: false,
        asset: {
          type: "image",
          ref: image.ref,
        },
      },
    },
  ],
  viewBox: {
    height: 100,
    width: 100,
    left: 0,
    top: 0,
  },
});
```

## API reference

* [`addElementAtPoint`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/)

## Code sample

```tsx
import React from "react";
import { addElementAtPoint } from "@canva/design";

export function App() {
  async function handleClick() {
    await addElementAtPoint({
      type: "shape",
      paths: [
        {
          d: "M 0 0 H 100 V 100 H 0 L 0 0",
          fill: {
            color: "#ff0099",
          },
        },
      ],
      viewBox: {
        height: 100,
        width: 100,
        left: 0,
        top: 0,
      },
    });
  }

  return (
    <div>
      <button onClick={handleClick}>Add shape to design</button>
    </div>
  );
}
```
