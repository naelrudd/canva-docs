Source: https://www.canva.dev/docs/apps/design-guidelines/selection/

# Selection

The best practices for reading and replacing selected content.

An overlay is an interactive editing surface placed on top of a selected image. It enables users to edit images, and preview their adjustments on the design.

## Update the interface based on the selection

It often makes sense to update the user interface based on whether something is selected. For example, if nothing is selected, an app should disable any elements that are only relevant when something is selected.

## Preview updated content and only replace content with permission and intent

When updating or replacing content, the recommended approach is to show a preview to the user before publishing content updates to a design. The better approach is for apps to only replace content when there is clear intent, such as when the user clicks a button. Show users a preview of the enhanced content, and then check if the user wants to add it to the canvas.

## Show loading states

Replacing content can be a time-consuming process, such as when uploading a replacement image. In these cases, show the appropriate loading states, such as loading spinners or progress bars. To learn more, see [Loading](https://www.canva.dev/docs/apps/design-guidelines/loading/).

## Decide whether to handle multiple selections

The `selection.registerOnChange` method assumes the app wants to handle multiple elements at once. If this is not the case, show an alert and disable any relevant buttons when more than one element is selected.

## Handle derived assets

If an app replaces an image, it must pass the `ref` of the original image into the `upload` method via the `parentRef` property. This ensures that Canva can keep track of the original asset and adhere to any licensing requirements.

## Don't run a process on content without user confirmation

Ask the user for confirmation to run a process. For example, when the user selects an image, enhance it only when the user clicks to confirm.

This avoids running costly processes each time the user selects a different object, and introduces fewer distractions.
