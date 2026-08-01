Source: https://www.canva.dev/docs/apps/designs/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Designs

An introduction to designs in the Apps SDK.

In Canva, users can create *designs*. These designs are made out of pages, and those pages contain various ingredients, such as [image](https://www.canva.dev/docs/apps/creating-images/) elements and [text](https://www.canva.dev/docs/apps/creating-text/) content.

## Design types

Canva supports a range of *design types*, each of which is intended for specific use-cases. For example, there's a design type for Instagram posts and a design type for postcards.

The design types themselves fall into the following categories:

* *Fixed design types*, which refer to design types that have fixed dimensions — that is, the dimensions are set to a specific width and height. This is the most common category of design type.
* *Responsive design types*, which refer to design types that have responsive dimensions — that is, the dimensions adjust to the content of the design. The only example of a responsive design type is a document.

Apps are compatible with all design types, but some methods are only available for certain categories.

Where possible, apps should determine the context in which an app is running and either call the compatible method or make it obvious when a certain feature isn't available. To learn more, see [Feature support](https://www.canva.dev/docs/apps/feature-support/).

## Design IDs

All designs have a unique ID. Apps can access this ID and use it to store information that's associated with the design — for example, to save the user's settings on a per-design basis. To learn more, see [Using design IDs](https://www.canva.dev/docs/apps/using-design-ids/).

## Interacting with designs

Apps can interact with designs in a variety of ways, such as by:

* [Adding elements to designs](https://www.canva.dev/docs/apps/elements/)
* [Adding pages to a design](https://www.canva.dev/docs/apps/api/latest/design-add-page/)
* [Querying content in designs](https://www.canva.dev/docs/apps/querying/)
* [Listening for content selection](https://www.canva.dev/docs/apps/selection/)
* [Traversing elements in designs](https://www.canva.dev/docs/apps/design-editing/)
