Source: https://www.canva.dev/docs/apps/design-guidelines/feature-support/

# Feature support

Guidelines for handling unsupported features.

Apps built for Canva run in various contexts, and it's essential to consider how your app functions across varied contexts such as the design type and surface. For example, consider the context of these design types and surfaces:

* Design types:
  * Fixed design types like [Presentations](https://www.canva.com/presentations/).
  * Responsive design types like [Docs](https://www.canva.com/docs/).
* Surfaces:
  * The object panel.
  * Selected image overlay.
* Preview or future contexts that impact API availability.

Make sure you're checking if a feature is available and supported, partially supported, or unavailable for your app's use case. It's an important part of developing your app's overall UI. There are steps you can take when feature availability changes to make sure your app's overall user experience is consistent, even across different contexts.

## Check feature availability

As an example of how to check feature availability, the following pattern generator app adds patterns as an image, or sets patterns as page backgrounds.

## Identify level of feature support

When designing your app, make sure you check if a feature is available and supported, partially supported, on unavailable, and asses the impact. You can check for supported APIs by referring to the API compatibility matrix, or checking in developer mode when you [preview your app](https://www.canva.dev/docs/apps/previewing-apps/).

There are 3 levels of feature support to look for when assessing feature support impact on your app:

### Fully supported

* Your app only uses supported APIs.
* All the features work across all design types and surfaces.
* **Adaptation isn't a requirement**.

### Partially supported

* Your app uses APIs unsupported in some design types or surfaces.
* Users are not prevented from carrying out the app's primary functionality.
* **Some adaptation is a requirement**:
  * Implement the design pattern to [handle unsupported features](https://www.canva.dev/#manage-unsupported-features).
  * [Contact us](https://canva-external.atlassian.net/servicedesk/customer/portal/2/group/2) for support on reviewing your app and feature availability.

### Not supported

* Your app uses unsupported APIs that block primary functionality in some design types.
* Your app isn't available for the incompatible design types, but users can still install the app if they choose to.
* **Adaptation might be extensive**:
  * Adapt your app's UI for partial feature support.
  * Choose to maintain your app as unsupported for certain design types.

Currently, we have whitelisted all the apps to be available in their supported contexts. In the future, we'll provide a way for you to specify the contexts for you app. Follow the [Developers Community](https://community.canva.dev) for updates.

## Manage unsupported features

Make sure that the overall user experience stays consistent when adapting your app by following these recommended approaches:

1. It's preferable to [adapt the experience with minimal changes](https://www.canva.dev/#adapt-the-experience). When a feature is not supported on a given design type, you can prioritize using alternative methods, or select an API that provides similar functionality.
2. [Handle dead-ends with a workaround](https://www.canva.dev/#handle-dead-ends-with-a-workaround). If there's no alternative method, provide a workaround that users can follow for a path forward.

## Adapt the experience

When certain features are not supported for a specific design type, the preferred approach is using an alternative API, or a solution that provides similar functionality, without significantly altering the user experience. This makes sure users can interact with the app while reducing confusion or frustration.

### Do

* **Do** keep a consistent experience across different design types so it remains intuitive, especially for users already familiar with your app.
* **Do** consider hiding unsupported features to keep the experience simple.
* **Do** ensure the primary action remains enabled and visible.

### Don't

* **Don't** use critical alerts at the beginning of the flow to highlight unavailable features. This may give users the impression that there's an app error.
* **Don't** allow users to interact with unsupported features. This could lead to disabling the primary action, errors, or broken flows.

## Handle dead-ends with a workaround

When there are no alternative APIs to achieve a task, provide users with a clear workaround. Options for workarounds could include, but aren't limited to:

* Guiding users through manual steps.
* Offering alternate methods to achieve their goals with the app's primary functionality.

For example, if recording and adding audio files isn't supported in certain design types, the app can upload these to the user's library instead.

* **Do** inform users upfront about any unavailable features.
* **Do** provide users with a workaround, and make sure it's achievable with the least amount of effort.
* **Do** specify if a certain design type is not supported.
* **Don't** wait until users have invested significant time or effort before informing them of unavailable features.
* **Don't** leave users without any guidance or feedback when a feature is unsupported.
* **Don't** use vague language and instead specify the exact issue or design type.

## Highlight the app's use case in the app listing

When writing your app listing, highlight the use cases that your app is designed to work within. The app listing displayed in Canva and the Apps Marketplace contributes to a consistent user experience by establishing expectations.

Select written content and featured images with consideration of available features and design types. Make sure the content is meaningful. This makes it easier for users to understand where and how your app works. Read the [App listing guidelines](https://www.canva.dev/docs/apps/app-listing-guidelines/) to learn more about what makes an effective app listing.
