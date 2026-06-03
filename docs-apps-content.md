Source: https://www.canva.dev/docs/apps/content/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Content

An introduction to content in the Apps SDK.

In the Apps SDK, users can add different types of *content* to their designs.

Content is text or media content, such as [image content](https://www.canva.dev/docs/apps/creating-images/) or [richtext content](https://www.canva.dev/docs/apps/creating-text/).

Content is not the same as an [element](https://www.canva.dev/docs/apps/elements/). For example, in a Canva design, an image element contains image content that the user added. The "content" and "element" distinction matters because there are differences in how apps can operate on content versus how apps can operate on elements.

If you're not aware of these differences, the behavior of the Apps SDK may be confusing.

## Content vs. elements

An [element](https://www.canva.dev/docs/apps/elements/) is a container with a set of position and dimensions, while content is the underlying media or text that exists within that container. For example, image elements contain image content and video elements contain video content.

**Content, however, does not always align with an element.**

For example, a page background may contain image content, but a page background is not an image element. Similarly, table cells may have text content, but table cells are not text elements.

If your app needs to operate on the text, image, or video content found within the elements of a design, see the following sections on [querying](https://www.canva.dev/#content-querying), [selection](https://www.canva.dev/#content-selection), and [traversal](https://www.canva.dev/#element-traversal), as well as the [Content Querying](https://www.canva.dev/docs/apps/design-guidelines/content-querying-api/) guidelines for more information. If instead your app needs to traverse only the elements of a design, see the [Elements](https://www.canva.dev/docs/apps/elements/) guide, and the [Design Editing](https://www.canva.dev/docs/apps/design-guidelines/design-editing-api/) guidelines for more information.

## Content types

Apps can interact with the following types of content:

* [Image content](https://www.canva.dev/docs/apps/creating-images/)
* [Text content](https://www.canva.dev/docs/apps/creating-text/), as plaintext or richtext
* [Video content](https://www.canva.dev/docs/apps/creating-videos/)

The way in which an app can interact with content depends on the type of content. The exact details are explained on the linked pages.

## Content querying

Apps can query the content in a user's design. This allows the app to read and update the content of a design without needing to understand or traverse the structure of the design. To learn more, see [Querying content](https://www.canva.dev/docs/apps/querying/).

## Content selection

Apps can listen for the selection of content in a user's design. This allows the app to read and update the selected content, which is appropriate for more targeted operations. To learn more, see [Selection API](https://www.canva.dev/docs/apps/selection/).

## Element traversal

Apps can traverse the elements in a user's design. This allows the app to read and update the content of the elements, which means the app can understand the context in which the content is rendered. To learn more, see [Design Editing API](https://www.canva.dev/docs/apps/design-editing/).
