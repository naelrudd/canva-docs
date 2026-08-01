Source: https://www.canva.dev/docs/apps/design-guidelines/rich-text/

# Richtext

Read and replace selected text while preserving its styling.

In Canva, the term *richtext* refers to text that has formatting (style) attributes. Using the Apps SDK, apps can read and replace richtext while preserving or manipulating these attributes.

The supported attributes include:

* Font size
* Text color
* Font weight
* Italics
* Underline
* Strikethrough
* Hyperlinks

This page contains various design considerations when working with richtext. To learn more about working with richtext in general, see [Creating text](https://www.canva.dev/docs/apps/creating-text/).

## Selecting text

Users must select richtext content before an app can read or otherwise interact with it. This means that, in addition to the [selection guidelines](https://www.canva.dev/docs/apps/design-guidelines/selection/), it's important to keep the following things in mind:

* **Do** disable UI components if text content is not selected.
* **Consider** showing an [informational alert](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/story/canva-app-ui-kit-informational-alert--informational-alert) that prompts users to select text content.
* **Do** show a [warning alert](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/story/canva-app-ui-kit-informational-alert--warning-alert) to inform users if the selected content is not supported by the app.
* **Do** ensure the app has reasonable behavior in the following scenarios:
  * When a user selects a whole text element.
  * When a user select multiple text elements.
  * When a user selects a group with multiple content types such as text, images, and videos.
  * When a user selects a portion of text content, such as a single word or paragraph.
  * When a user selects multiple words or paragraphs while holding the `Shift` key.

## Styling text

* **Do** preserve the styling of the selected text, unless this contradicts the intended behavior of the app.
* **Consider** allowing users to customize the text's style.
* **Do** use [formatting icons](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/story/canva-app-ui-kit-icons-icons--all-icons) from the App UI Kit to display styling options.
* **Do** show a preview of style adjustments before applying them.
* **Do** use the [color selector flyout](https://www.canva.dev/docs/apps/using-color-selectors/) if your app allows users to modify the text's color.

## Confirmation

* **Do** show a [positive alert](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/story/canva-app-ui-kit-informational-alert--positive-alert) once the app has succesfully replaced the user's text.
