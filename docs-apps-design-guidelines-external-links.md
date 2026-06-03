Source: https://www.canva.dev/docs/apps/design-guidelines/external-links/

# External links

The best practices for linking to external web pages.

## Use the App UI Kit components

The [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/) has two components that are suitable for linking to external web pages:

* `Button`
* `Link`

We recommend using these components instead of creating custom components.

## Use the most appropriate component

The most appropriate component for a link depends on how it's used:

* If the external link is the main call-to-action (CTA), use the `Button` component with the `variant` prop set to `"primary"` or `"secondary"`. Otherwise, use the `Link` component.
* If there are more than 2-3 CTAs on the page, use the `Link` component.

## Only open links with permission and intent

That is, only open links in response to a relevant action, such as clicking a button. Don't open links in a way or at a time that might be surprising, such as immediately after the user opens the app.

## Only open links with `requestOpenExternalUrl`

When an app calls the [`requestOpenExternalUrl`](https://www.canva.dev/docs/apps/api/latest/platform-request-open-external-url/) method, the user is informed that they are navigating away from Canva. Trying to open a link through alternative means, such as via the `window.open` method, triggers an error.

## Only show payment links on supported platforms

You can monetize your app by linking to external web pages that prompt users for payment, but only on certain platforms. To learn more, see [External payment links](https://www.canva.dev/docs/apps/accepting-payments/).

## Don't overload users with CTAs

The more CTAs an app has, the less focused the user experience becomes, and the more overwhelmed the user becomes. Providing fewer options results in a simpler, friendlier app.

## Don't include redundant links

Some links, such as links to the app's terms and conditions, can be configured via the Developer Portal. Don't include links to these pages in the app itself, because this creates a redundant and inconsistent user experience.
