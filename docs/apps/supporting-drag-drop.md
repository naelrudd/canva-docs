Source: https://www.canva.dev/docs/apps/supporting-drag-drop/

# Drag and drop

How apps can support drag and drop.

Something that Canva users love is the ability to drag and drop [content](https://www.canva.dev/docs/apps/content/) straight into their designs. Apps can use the Apps SDK to support this behavior, ensuring that the user experience is delightfully consistent.

## Content types

Apps can enable drag and drop for various types of content, including:

* [Audio tracks](https://www.canva.dev/docs/apps/creating-audio-tracks/)
* [Embeds](https://www.canva.dev/docs/apps/embedding-rich-media/)
* [Images](https://www.canva.dev/docs/apps/creating-images/)
* [Text](https://www.canva.dev/docs/apps/creating-text/)
* [Videos](https://www.canva.dev/docs/apps/creating-videos/)

Additional content types may be supported in the future.

## Feature support considerations

Drag and drop methods are supported in responsive and fixed [Canva design types](https://www.canva.dev/docs/apps/designs/#design-types) depending on the method:

* `startDragToCursor` only works in fixed design types, such as Presentations.
* `startDragToPoint` only works in responsive design types, such as Docs.

To learn more, see [Feature support](https://www.canva.dev/docs/apps/feature-support/).

## Rendering the UI

Apps need to render something in their UI that can be dragged.

This can be as simple as an `HTMLDivElement` with a `draggable` attribute:

```tsx
<div draggable>This text can be dragged.</div>
```

In the [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/) though, we've also provided a number of card components that are designed to work seamlessly with drag and drop. The components include:

* `AudioCard`
* `EmbedCard`
* `ImageCard`
* `TypographyCard`
* `VideoCard`

To see how to use these components, see [Code samples](https://www.canva.dev/#code-samples).

## Handling drag events

Apps can handle drag events by registering an `onDragStart` callback and passing the drag event into either of the following methods:

* `startDragToPoint`
* `startDragToCursor`

Both methods add content to the user's design, but:

* `startDragToPoint` is only compatible with design types that support absolute positions, which is all design types except for documents.
* `startDragToCursor` is only compatible with design types that contain streams of text, which is only the document design type.

The supported content types also depend on the method being called:

| Content Type | startDragToPoint | startDragToCursor |
| ------------ | ---------------- | ----------------- |
| Audio tracks | ✅                | ❌                 |
| Embeds       | ✅                | ✅                 |
| Images       | ✅                | ✅                 |
| Text         | ✅                | ❌                 |
| Videos       | ✅                | ✅                 |

Where possible, apps should determine the context in which the app is running and either call the compatible method or make it obvious when functionality isn't available. To learn more, see [Feature support](https://www.canva.dev/docs/apps/feature-support/).

## Handling clicks

For accessibility reasons, drag and drop should not be the only way that users can add content to a design. Apps should also support click events. This behavior is built into the App UI Kit components and demonstrated below.

## Code samples

(Full code samples for Audio, Embeds, Images, Text, and Videos are available in the original documentation.)
