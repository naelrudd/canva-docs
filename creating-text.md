Source: https://www.canva.dev/docs/apps/creating-text/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating text

How to add text to a user's design.

Text is an essential ingredient in a designer's toolkit, and apps can create and otherwise interact with text in a variety of ways. This page explains everything you need to know about working with text.

## Text formats

While using the Apps SDK, text can be represented in either of the following formats:

* Plaintext
* Richtext

Apps can choose which format to work with, but the choice affects what features are available.

### Plaintext

* When creating plaintext, formatting can only be applied to the whole text.
* When reading plaintext, apps can't access the existing formatting information.
* When updating plaintext, apps can't maintain the styling of the text.

### Richtext

* When creating richtext, different parts of the text can have different formatting.
* When reading richtext, apps can access the existing formatting information.
* When updating richtext, apps can maintain the styling of the text.

## Text elements

Apps can create *text elements*:

**Richtext:**
```tsx
import { addElementAtPoint, createRichtextRange } from "@canva/design";

const range = createRichtextRange();
range.appendText("Hello world");

await addElementAtPoint({
  type: "richtext",
  range,
});
```

**Plaintext:**
```tsx
import { addElementAtPoint } from "@canva/design";

await addElementAtPoint({
  type: "text",
  children: ["Hello world"],
});
```

## Text content

When text exists in a design, it's known as *text content*. This content can exist in table cells, text elements, and other containers.

## Text formatting

Apps can apply a variety of formatting options to text, including [fonts](https://www.canva.dev/docs/apps/fonts/).

## Paragraphs

Use the `\n` character to denote the end of a paragraph.

## Text selection

Apps can listen for the selection of text content and read or update the selected content using the Selection API.

## Richtext ranges

A richtext range represents a portion of formatted text:

```tsx
import { createRichtextRange } from "@canva/design";
const range = createRichtextRange();
range.appendText("Hello world.");
range.appendText("This is bold.", { fontWeight: "bold" });
```

### Formatting richtext

**Inline formatting:**
```tsx
range.formatText({ start: 0, length: 4 }, { fontWeight: "bold" });
```

**Paragraph formatting:**
```tsx
range.formatParagraph({ start: 0, length: 1 }, { textAlign: "center" });
```

### Reading richtext as plaintext

```tsx
const plaintext = range.readPlaintext();
```

### Reading richtext as text regions

```tsx
const regions = range.readTextRegions();
```

## Gotchas

* Apps can't set the line-height of text.
* Apps can't create text with a vertical writing mode.
* Text elements can't have a predefined height.
* Font sizes are defined with pixels (px) in the API but displayed as points (pt) in the UI.

## API reference

* [`addElementAtPoint`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/)
* [`createRichtextRange`](https://www.canva.dev/docs/apps/api/latest/design-create-richtext-range/)
