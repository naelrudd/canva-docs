Source: https://www.canva.dev/docs/apps/design-guidelines/design-editing-api/

# Design Editing API

The best practices for using design editing on a page.

The [Design Editing API](https://www.canva.dev/docs/apps/design-editing/) allows users to see and edit all the elements on a page. Users can adjust an element's position, placement, orientation, and size.

Using design editing, you can create experiences such as a layout-builder app, or handle other common use cases for changing the document tree, which include, but aren't limited to:

* Making collages.
* Changing element arrangements.
* Scaling and resizing elements.
* Rearranging element layouts.

## Do

### Design as a whole

* **Do** make changes as a whole, and in one step, instead of multiple separate steps.
* **Do** introduce one undo action for when the user wants to revert any changes.

### Make the interaction intuitive

* **Do** show only options that users can apply to the number of elements on the page when building a layout app.
* **Do** apply changes instantly for quick actions that take less then 2 seconds.
* **Do** consider using a [spinner loader](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/story/components-progress-loading-indicator--simple-loading-indicator) on a button if an action is triggered by the button.
* **Do** use the [loading pattern](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/story/patterns-loading-loading-progress-bar--loading-progress-bar) when the process takes longer than 2 seconds.
* **Do** use progressive disclosure when building new design editing features.
* **Do** keep design editing simple, and use a preset or a one-click effect such as the effect shown in the previous Auto layout app example.
* **Do** offer more advanced controls progressively after users have applied the basic feature. For example, a rearrange button that changes the image order.

### Unsupported elements and error states

* **Do** show a [critical alert](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/docs/components-informational-alert--critical-alert) to inform users if design elements aren't supported.

### Successful edits

* **Do** consider using a [positive alert](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/docs/components-informational-alert--positive-alert) for providing feedback to the user when they successfully edit elements on the page. A positive alert is useful as feedback when changes are not obvious to the user.

### Failed edits

* **Do** show a [critical alert](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/docs/components-informational-alert--critical-alert) along with an error state explaining why an action resulted in an error.

### Preview

* **Do** display edits or changes.

## Don't

* **Don't** make changes that go against your user's expectation. For example, if the user has 3 elements on the design, don't allow changes that include only 2 elements, but delete 1 of those elements.
* **Don't** change elements into something different. For example, the design editor shouldn't change the entire design into an app element.
* **Don't** show templates that aren't providing value to your users.
