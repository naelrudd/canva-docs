Source: https://www.canva.dev/docs/apps/querying/

# Querying content

Reading and updating content in a user's design.

Apps can query the [content](https://www.canva.dev/docs/apps/content/) in a user's design, similar to how the HTML DOM can be queried. They can then read and update the queried content, which unlocks a range of powerful use-cases.

Content is not the same as an element in a design. However, they are related because elements contain content. An app can operate on content through content querying, but needs [design editing](https://www.canva.dev/docs/apps/design-editing/) to position elements and set element dimensions.

## Content types

There are different types of content that may appear in a design, including:

* [Images](https://www.canva.dev/docs/apps/creating-images/)
* [Text](https://www.canva.dev/docs/apps/creating-text/), including plaintext and richtext
* [Videos](https://www.canva.dev/docs/apps/creating-videos/)

For the time being, **richtext is the only content type that's compatible with querying**.

## Targets

When an app queries a design, it must specify a target. This determines what part of the design to query. For the time being, **the only supported target is the current page**.

## Reading content

```tsx
import { editContent } from "@canva/design";

await editContent(
  {
    contentType: "richtext",
    target: "current_page",
  },
  async (session) => {
    console.log(session.contents);
  }
);
```

## Updating content

```tsx
import { editContent } from "@canva/design";

await editContent(
  {
    contentType: "richtext",
    target: "current_page",
  },
  async (session) => {
    for (const content of session.contents) {
      const plaintext = content.readPlaintext();
      content.formatParagraph(
        { index: 0, length: plaintext.length },
        { fontWeight: "bold" }
      );
    }
    await session.sync();
  }
);
```

### Handling conflicts

If queried content is changed after the `editContent` method is called but before the session is synced, it can lead to conflicts between the state of the content and the true state of the design. Canva will attempt to resolve conflicts.

### Handling deleted content

```tsx
for (const content of session.contents) {
  if (content.deleted) {
    continue;
  }
  const plaintext = content.readPlaintext();
  content.formatParagraph(
    { index: 0, length: plaintext.length },
    { fontWeight: "bold" }
  );
}
```

## Gotchas

* You can't use querying to read or update the position of elements on a page.
* In content arrays, the order of the content items is not guaranteed.
* You can't call the `editContent` method from within the callback of another `editContent` method.
