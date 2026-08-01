Source: https://www.canva.dev/docs/apps/design-guidelines/icons/

# Icons

Learn how to use icons throughout your app.

Icons in an app should aim to represent the intended symbolism while maintaining a distinct Canva personality. To ensure consistency, Canva provides guidelines to help design and prepare icon assets for use in the product.

**Tip:** Where possible, we recommend using icons from the [App UI Kit](https://www.npmjs.com/package/@canva/app-ui-kit). To view all of the available icons, see [Storybook](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/story/components-icons-icons--all-icons). If a required icon isn't available, [raise a feature request](https://community.canva.dev/c/apps-sdk/apps-sdk-requests/7).

## Accessibility

Icons are not accessible without additional markup. Markup depends on how the icon is used, though generally, it can be broken down into three categories: decorative, interactive, and indicative icons.

### Decorative icons

Decorative icons are purely cosmetic and convey no real semantic meaning — if they were removed, no context would be lost — and are typically used for visual reinforcement or branding. Decorative icons are paired with text, such as in lists or inputs, which provide the context for sighted and screen reader users.

Icons have the `aria-hidden="true"` attribute by default, meaning that they're invisible to screen readers and support this use case by default.

### Interactive icons

Interactive icons do convey meaning to users. The most common example is buttons or links, which are icon-only.

### Indicative icons

Indicative icons aren't interactive, though the icon does convey meaning. This is useful for statuses or when icons are used in place of text inside a longer message.

Either way, it must be communicated by using [invisible content available to screen readers](https://webaim.org/techniques/css/invisiblecontent/) or the surrounding content.
