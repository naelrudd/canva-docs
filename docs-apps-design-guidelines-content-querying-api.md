Source: https://www.canva.dev/docs/apps/design-guidelines/content-querying-api/

# Content Querying API

Guidelines for the text querying API

Content querying allows apps to retrieve and edit all text content on the design, and then make edits. It's a simplified API that enables useful capabilities such as improving your user's design typography. Common use cases for content querying include, but aren't limited to:

* Translation apps.
* Design assistants.
* Spell checker services.
* SEO keyword checkers.

## For apps that replace part of the text

For spell checker services and translation apps, it's advisable to consider the following:

* **Do** highlight the text to replace in the object panel, and clearly show the suggested text.
* **Do** use a checkbox if there are multiple suggestions.
* **Do** use a call-to-action (CTA) that explains the action. For example, to fix spelling or typography.

* **Don't** use a generic CTA that's unclear, or omits an explanation of the action.
* **Don't** make edits to the design without giving context of what's being changed and why.

## Translation apps

* **Do** replace the source text automatically once the user interacts with the CTA button or element.

## Rich text

* **Do** preserve rich text formatting until the user changes the formatting option.

## General guidelines

### What content querying can do

* Query all text in the current page plus the entire design.
* Carry out transformation operations on the text such as:
  * Replace the whole text.
  * Replace part of the text.
  * Make part of the text bold, or edit any rich text.
  * Update the text color.

### What content querying can't do

* It can't provide any information about which element contains a given piece of text, such as text located in a table, shape, or native text element.
* It can't provide the ability to position elements on pages (See [Design Editing API](https://www.canva.dev/docs/apps/design-guidelines/design-editing-api/) for information on positioning elements). When using content querying, the app does not read the text in a linear way, and instead reads the text randomly.
* Text highlighting on the design is not possible. Future updates may include text highlighting.
* It's not currently available in Canva Docs.
