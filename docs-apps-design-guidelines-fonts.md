Source: https://www.canva.dev/docs/apps/design-guidelines/fonts/

# Fonts

Guidelines for prompting users to select a font.

There are two ways that apps can prompt users to select a font:

* Open Canva's built-in font picker with the `requestFontSelection` method.
* Get a list of fonts with the `findFonts` method and render a custom user interface.

Each option has its own set of design considerations.

**Note:** To learn more about creating text and using fonts, see [Creating text](https://www.canva.dev/docs/apps/creating-text/).

## Built-in font picker

Apps can use Canva's own built-in font picker. This is a dialog that offers the most consistent and familiar user experience, with support for search, filtering, font previews, and more.

* **Do** use the built-in font picker unless a custom user interface is absolutely necessary.
* **Do** use a secondary `Button` component to open the font picker.
* **Do** use the `selectedFontRef` property to remember the state of the user's selection.

## Custom user interface

Sometimes, the built-in font picker isn't the right option. In these cases, apps can provide their own custom user interface for selecting a font.

* **Do** render long lists of fonts in an appropriate component, such as a `Select` dropdown.
* **Do** show the user a preview of each font (or at least the selected font).
* **Do** allow the user to select from a list of supported font weights.
* **Do** allow the user to select from a list of supported font styles.
* **Don't** allow the user to select unsupported font weights or styles.
* **Don't** enable font weight or style selection if only one option is available.
