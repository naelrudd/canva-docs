Source: https://www.canva.dev/docs/apps/using-color-selectors/

# Using color selectors

How to prompt users to select a color.

Sometimes, apps want to prompt users to select a color. For example, an app for creating patterns might want to prompt users to select the colors for a pattern. To ensure a consistent user experience, apps can use the Apps SDK to open a built-in color selector flyout and detect the selection of colors.

## Features

* A familiar user experience that's deeply integrated with Canva.
* Integrated with [Brand Kit](https://www.canva.com/help/brand-kit/), helping teams to remain on-brand.
* [Canva Pro](https://www.canva.com/pro/) users automatically get access to Pro-only features.

The color selector feature works within different [Canva design types](https://www.canva.dev/docs/apps/designs/), such as Presentations and Docs. See [Feature support](https://www.canva.dev/docs/apps/feature-support/) for more information.

## The user experience

Apps are responsible for determining how a color selector opens, but a common pattern is to open the selector when a user clicks a `Swatch` component.

The color selector itself appears in a flyout interface that's "pinned" to the element that opened it. The exact position of the flyout is calculated and controlled by Canva.

Users can select document colors, Brand Kit colors, or default colors. If non-breaking features are added to the color selector in the future, they will be automatically available to apps without requiring code changes.

While the color selector is open, an invisible overlay is rendered on top of the app. This overlay blocks interactions with the app, such as clicking or scrolling, until the color selector is closed.

## Color selection scopes

The color selector can be configured with one or more *scopes*. These scopes determine the user experience. At the moment, `"solid"` is the only supported scope. When enabled, this scope allows the user to select solid colors.

## How to open a color selector

### Step 1: Enable the required scopes

In the Developer Portal, enable the following scopes:

* `canva:brandkit:read`
* `canva:design:content:read`

### Step 2: Set up an anchor

```tsx
import { Rows, Swatch } from "@canva/app-ui-kit";
import * as React from "react";
import * as styles from "styles/components.css";

export function App() {
  return (
    <div className={styles.scrollContainer}>
      <Rows spacing="1u">
        <Swatch
          fill={["#ff0099"]}
          onClick={() => {
            // code goes here
          }}
        />
      </Rows>
    </div>
  );
}
```

### Step 3: Open the color selector

```tsx
import { openColorSelector } from "@canva/asset";

<Swatch
  fill={["#ff0099"]}
  onClick={async (event) => {
    const anchor = event.currentTarget.getBoundingClientRect();
    await openColorSelector(anchor, {
      scopes: ["solid"],
      onColorSelect: (event) => {
        console.log(event.selection);
      },
    });
  }}
/>
```

### Step 4: Handle the color selection

```tsx
const [color, setColor] = React.useState<string>("#ff0099");

<Swatch
  fill={[color]}
  onClick={async (event) => {
    const anchor = event.currentTarget.getBoundingClientRect();
    await openColorSelector(anchor, {
      scopes: ["solid"],
      onColorSelect: (event) => {
        if (event.selection.type === "solid") {
          setColor(event.selection.hexString);
        }
      },
    });
  }}
/>
```

### (Optional) Step 5: Handle multiple colors

```tsx
<Swatch
  fill={[color]}
  onClick={async (event) => {
    const anchor = event.currentTarget.getBoundingClientRect();
    await openColorSelector(anchor, {
      scopes: ["solid"],
      selectedColor: color
        ? {
            type: "solid",
            hexString: color,
          }
        : undefined,
      onColorSelect: (event) => {
        console.log(event.selection);
      },
    });
  }}
/>
```

### (Optional) Step 6: Close the color selector

```tsx
const closeColorSelector = await openColorSelector(anchor, {
  scopes: ["solid"],
  onColorSelect: (event) => {
    if (event.selection.type === "solid") {
      setColor(event.selection.hexString);
    }
  },
});

closeColorSelector();
```

## API reference

* [`openColorSelector`](https://www.canva.dev/docs/apps/api/latest/asset-open-color-selector/)
