Source: https://www.canva.dev/docs/apps/fonts/

# Using fonts

How to use fonts when creating or updating text.

Canva has an expansive library of fonts. Apps can access and use a limited subset of these fonts when [creating or updating text](https://www.canva.dev/docs/apps/creating-text/) in a user's design.

## Feature and surface support considerations

The font picker works within different [Canva design types](https://www.canva.dev/docs/apps/designs/#design-types), such Presentations and Docs.

## Open font picker

Apps can open a font picker that lets users choose a font from Canva's library. This offers a familiar and consistent user experience, and it's how we recommend most apps implement a font selection interface.

```tsx
import { Button, Rows } from "@canva/app-ui-kit";
import { requestFontSelection } from "@canva/asset";
import * as React from "react";
import * as styles from "styles/components.css";
import { useFeatureSupport } from "@canva/app-hooks";

export function App() {

  const isSupported = useFeatureSupport();

  async function handleClick() {
    const fontResponse = await requestFontSelection();
    if (isSupported(requestFontSelection)) {
    console.log(fontResponse);
    return;
   }
  }

  return (
    <div className={styles.scrollContainer}>
      <Rows spacing="1u">
        <Button
          variant="primary"
          onClick={handleClick}
          disabled={!isSupported(requestFontSelection)}
          >
          Open font picker
        </Button>
      </Rows>
    </div>
  );
}
```

## Remember font selection

When a user selects a font, we recommend storing that font in a state object.

```tsx
import { Button, Rows, Text } from "@canva/app-ui-kit";
import { Font, requestFontSelection } from "@canva/asset";
import * as React from "react";
import * as styles from "styles/components.css";
import { useFeatureSupport } from "@canva/app-hooks";

export function App() {
  const [selectedFont, setSelectedFont] = React.useState<Font | undefined>();

  const message = selectedFont
    ? `The selected font is ${selectedFont.name}.`
    : `There is no font selected.`;

  const isSupported = useFeatureSupport();

  async function handleClick() {
    if (isSupported(requestFontSelection)) {
    const fontResponse = await requestFontSelection({
      selectedFontRef: selectedFont?.ref,
    });

    if (fontResponse.type !== "completed") {
      return;
    }
  }

    setSelectedFont(fontResponse.font);
  }

  return (
    <div className={styles.scrollContainer}>
      <Rows spacing="1u">
        <Text>{message}</Text>
        <Button
          variant="primary"
          onClick={handleClick}
          disabled={!isSupported(requestFontSelection)}
          >
          Select a font
        </Button>
      </Rows>
    </div>
  );
}
```

## Use selected font

```tsx
import { addElementAtPoint } from "@canva/design";

await addElementAtPoint({
  type: "text",
  children: ["Hello world"],
  fontRef: selectedFont?.ref,
});
```

## Render font preview

All fonts have an associate image that contains a preview of the font.

```tsx
<div>{selectedFont && <img src={selectedFont.previewUrl} />}</div>
```

## Get list of recommended fonts

```tsx
import { findFonts } from "@canva/asset";
const { fonts } = await findFonts();
console.log(fonts); // => [ { name: "Arial", ... }]
```

## Get specific font details

```tsx
import { findFonts } from "@canva/asset";
const { fonts } = await findFonts({ fontRefs: ["font_ref_goes_here"] });
console.log(fonts); // => [ { name: "Arial", ... }]
```

## Gotchas

* Apps can't access [Canva Pro](https://www.canva.com/pro/) fonts.
* Apps can't upload or otherwise define custom fonts.
* Apps can't download the underlying font files.
* Apps can only set the font of paragraphs, not of inline text.

## API reference

* [`findFonts`](https://www.canva.dev/docs/apps/api/latest/asset-find-fonts/)
* [`requestFontSelection`](https://www.canva.dev/docs/apps/api/latest/asset-request-font-selection/)
