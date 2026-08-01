Source: https://www.canva.dev/docs/apps/design-guidelines/premium-apps/

# Premium apps

Guidelines for designing apps within the Premium Apps Program.

This guide helps you design apps that are part of the [Premium Apps Program](https://www.canva.dev/docs/apps/premium-apps/). It covers best practices for designing premium features, as well as specific design guidelines for gated and non-gated premium apps.

## Best practices

### Feels like home

Premium apps feel like home in every corner of Canva – working seamlessly across platforms, document types, and workflows to help users design anything, anywhere they need.

* **Work across document types:** Support presentations, whiteboards, docs, emails and other Canva formats.
* **Skip the sign-in:** Let users try premium features without creating or linking accounts.
* **Speak every language:** Provide all features and content in every language Canva supports from day one.
* **Provide flexible input options:** Let users work with at least 2 input methods, such as uploading files or selecting from their design.

### Confidence in creativity

Premium apps empower users at every skill level, surfacing the right capabilities at the right time to build confidence without overwhelming.

* **Suggest smart presets:** Offer templates and prompts that help users begin confidently.
* **Meet users where they are:** Offer guided experiences for beginners alongside powerful tools for experienced users.
* **Show changes instantly:** Display live previews so users can see their edits take effect in real-time.
* **Guide users naturally:** Place important controls where users expect them, with layouts that intuitively lead to key features.

### Responsive and clear

Premium apps honor users' time with responsive performance and transparent feedback, keeping users in control of their workflow even during complex operations.

* **Keep it snappy:** Deliver results fast enough that users stay in their creative flow.
* **Set time expectations:** Tell users how long things will take and update them if that changes.
* **Provide control:** Give users the ability to cancel processes, undo changes, and redo actions.

### Meets every expectation

Premium apps deliver on their promise from first impression to final output.

* **Show real examples:** Use marketplace images that demonstrate actual use cases.
* **Delight with quality:** Produce results as polished as Canva's own features.
* **Preview before committing:** Show before/after views and multiple options before users add to their design.

## Gated premium apps

For completely gated Premium Apps, remove any paywalls that currently exist in the apps, as well as any off-platform login requirements or credit systems. All features in the app should be accessible to Canva users on paid plans.

## Visualizing premium features in freemium or credit-based apps

Non-gated Premium apps should follow Canva's native design pattern to distinguish premium features. We use the premium crown icon and pro badge components, sometimes supplemented with a tooltip, as the indication for what the user gets as part of their current Canva plan.

Free users are prompted with the account upgrade dialog immediately after clicking on a premium feature. Therefore, the app's design should focus on the user's task, and let the upgrade dialog handle the upgrade and conversion experience.

## Provide a clear freemium app experience

Non-gated premium apps should offer a valuable freemium experience. Create a thoughtful balance between free and premium features: enough free content to keep users engaged, while clearly showcasing the added value of upgrading.

Free features available to users should remain free and not be retracted, and premium features should be an add-on. UI should remain the same for Free and Pro users. Users should only experience differences when they see locked features.

## UI requirements

The [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/) includes the following types of icons for freemium or credit-based apps:

* `PremiumCrownIcon`
* `ProBadge`

These icons visually indicate the user's access with color variants. Free users will see yellow, and users on paid Canva plans will see grey.

### Premium crown icon

**Warning:** This icon must only be used to highlight premium features that are part of the Premium App Program.

The premium crown icon is used in a few different UI patterns:

* **In a label:** include the icon immediately after the label text
* **In a button:** include the icon immediately before the text

#### Include the icon immediately after the label text

When all input components under a label provide premium features, the premium crown icon are added after the label text. Free users are prompted with an upgrade dialog when they interact with the related input components under them.

#### Added to the end of each option item

Premium crown icons are used to signify one or more premium options for checkboxes, segmented controls, and select.

#### In upgrade buttons

Premium crown icons may also feature as the beginning decoration in upgrade buttons. Use **Upgrade to Canva Pro** as button text.

#### In a menu list

Premium crown icons may also be featured in a list style within a drop down menu. The Pro crown should be positioned at the right end of the premium menu item.

#### In font pickers

Canva's built-in font picker features the premium crown icon to signify premium fonts, with the upgrade flow already configured.

#### Custom font picker

When displaying premium fonts, it should follow the same pattern as the built-in font picker.

#### In pills

Place the premium crown icon as an end decorator to highlight premium selections.

### Pro badges

Pro badges are often overlaid on cards, and reveal pro text when hovered. Always position the pro badge in the lower right corner of cards.

#### Disassociate the crown icon from off-platform logins

**The crown icon must only be used for premium features enabled by a paid Canva plan.** When a user logs in to use features enabled by your off-platform subscription, you must use a different UI.

#### Upgrade button as a secondary action for free users

Free users should see an upgrade button, in the secondary variant, immediately beneath the primary action.
