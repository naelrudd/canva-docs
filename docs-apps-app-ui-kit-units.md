Source: https://www.canva.dev/docs/apps/app-ui-kit/units/

# Units

An overview of units in the App UI Kit.

Canva's user interface is laid out on a grid, which consists of square cells, each measuring 8 pixels in width and height. This 8-pixel measurement is referred to as the *base unit*.

By aligning interface elements to this grid, apps can maintain a level of visual consistency that is aesthetically pleasing. It's not enough for apps to only conform to the grid, but it is a fundamental building block.

To help apps conform to the grid, most sizing and spacing values in the App UI Kit (widths, heights, margins, etc.) are multiples of the base unit. This ensures that interface elements align correctly.

## What are units?

A value that is a multiple of the base unit is referred to as a *unit*, abbreviated as *u*. As a result, the following values are synonymous:

* 8 pixels
* 1 unit
* 1u

Using units instead of hard-coded pixel values ensures that, should the size of the base unit change, apps would still conform to the grid. It also simplifies reasoning about relative sizing, as "2u" is twice "1u," thereby reducing the need for mental calculations when arranging components.

## Using the base unit

Generally, apps don't need to directly use the base unit. This number is used to compute the values of tokens in the [spacing scale](https://www.canva.dev/docs/apps/app-ui-kit/spacing/), and apps should typically employ these tokens for setting sizes and spaces.

However, if you want to adhere to the grid using a value not available in the spacing scale, you can access the base unit as a CSS or JavaScript variable and calculate the value yourself.

### CSS

```css
.container {
  padding: calc(var(--ui-kit-base-unit) * 10);
}
```

### JavaScript

```ts
import { tokens } from "@canva/app-ui-kit";

const style = {
  padding: `calc(${tokens.baseUnit} * 10)`,
};
```

## Exceptions

There are instances where conforming to the grid is impractical, such as when displaying a raster image with a fixed width and height. In these cases, disregard the grid. It is intended as a tool, not a constraint.
