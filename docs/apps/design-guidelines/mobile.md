Source: https://www.canva.dev/docs/apps/design-guidelines/mobile/

# Mobile

Guidelines for designing apps for mobile devices.

One of Canva's goals is to empower the world to design on every device. This means, where practical, apps should be designed to work well on both desktop and mobile devices.

## Support the required operating systems

At a minimum, Canva expects apps to support the following versions of mobile operating systems:

* iOS 12
* Android 6.0

To confirm if these browsers support a feature, visit [caniuse.com](https://www.caniuse.com).

An example of a useful feature that is *not* available in iOS 12 is [`OffscreenCanvas`](https://developer.mozilla.org/en-US/docs/Web/API/OffscreenCanvas).

## Optimize interactions

It's easy to be precise with a desktop computer and a mouse, but many users interact with a touchscreen using their finger. Find a balance that works well across a range of hardware.

## Handle low-power mode

If a user's device enters low-power mode, it affects the capabilities of the app. For example, iOS throttles the [`requestAnimationFrame`](https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame) method.

To confirm how your app behaves in low-power mode, [enable the mode](https://support.apple.com/en-au/HT205234) and test the app.

## Test the app on real devices

You can use [Chrome DevTools](https://developer.chrome.com/docs/devtools/) to simulate different resolutions and devices, but ideally, you should test the app on actual hardware, as certain nuances aren't captured in simulations.

To test an app on a real device:

1. Set up, configure, and connect the app via the Developer Portal. This is most easily done on a desktop device, because the Developer Portal is not responsive on mobile.

   **Note:** To test your app on a real mobile device, you can't use a localhost development URL for the app's **Development URL**. You must upload the app's JavaScript bundle via the **App source** field. To learn more, see [Previewing apps](https://www.canva.dev/docs/apps/previewing-apps/) and [Bundling apps](https://www.canva.dev/docs/apps/bundling-apps/).

2. Open Canva on a mobile device, either via the browser or with the [iOS](https://www.canva.com/download/ios/) or [Android](https://www.canva.com/download/android/) app.

3. Open the draft version of the app via the **Apps** tab.

## Consider content "below the fold"

On mobile devices, apps have limited vertical space. As a result, some of the app's content may appear "below the fold" — that is, it might not be visible without scrolling.

This can be a problem when a user can make a choice — for example, checking a checkbox — that affects the content rendered by the app. If the affected content appears below the fold, the user may not see the change, and the app may appear unresponsive.

An alternative is to split multi-step processes across separate screens. Then, when a user makes a choice, update the entire screen to show the next step. This makes the impact of the user's action much more obvious.
