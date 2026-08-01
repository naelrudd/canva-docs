Source: https://www.canva.dev/docs/apps/authenticating-users/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Authenticating users

How to authenticate Canva users.

Authentication in Canva is about creating a seamless experience by ensuring that your app remembers your users. How you create this experience in your app can depend on the type of app and how you want to store user data.

## Types of authentication

Apps can handle users with two forms of authentication: frictionless, or manual.

### Frictionless authentication (preferred)

Users confronted with a login prompt could consider it a hurdle. Any hurdles in the onboarding process come with a chance for them to drop out of your funnel, maybe to never return again. Because of this, we encourage you to consider *frictionless authentication*. This ensures that user data or credentials are automatically remembered to help users retain data, even without them passing through a login screen.

For more information on adding frictionless authentication to your app, see [Frictionless authentication](https://www.canva.dev/docs/apps/authenticating-users/frictionless/).

### OAuth integration

If your app requires access to resources on a third-party platform (e.g. Google Drive), you can use OAuth to simplify the authorization process for your users. This method allows users to securely grant your app the necessary permissions with a third party service without exposing user credentials.

For more information, see [OAuth integration](https://www.canva.dev/docs/apps/authenticating-users/oauth/).

### Manual authentication

This requires your users to authenticate with a third-party platform to access certain content or features within an app, including their own data. Your app can use manual authentication, but the way you handle users and user data can affect your apps inclusion in the user adoption program and your app's positioning in the Apps Marketplace. Consider using frictionless authentication, and make sure to follow our [authentication guidelines](https://www.canva.dev/docs/apps/design-guidelines/authentication/).

For more information on adding manual authentication to your app, see [Manual authentication](https://www.canva.dev/docs/apps/authenticating-users/manual/).

## Authentication workflows

How you create an app and create ways for users to authenticate can shape the user experience. The following are workflows you can consider to create a delightful authentication flow.

### Handle existing or returning users

If a Canva user has an account with your app (for example, if they have previously accessed your app with Canva) fetching the user token should be enough for you to identify if they do. Then you can either:

* Continue allowing them access to the content associated with that user token.
* Prompt them to log in to their account using manual authentication.

A user might have an account with your app, but have never accessed your app through Canva, so you don't have a user token associated to them.

In this case we recommend adding non-blocking text such as 'Already have an account? Click here to sign in.' at the bottom of your app to provide them the opportunity to initiate the authentication process.

### Support a free trial without authentication

If the trial is time-based, you can save the date of initial account creation and then check if that date + \[trial time period] is before today's date. If it is, then allow the user to continue accessing the app. If it is not, you can restrict the UI in the app until the user authenticates and subscribes to an appropriate plan.

If the trial is usage-based, track usage as above and then restrict usage of the app when the tracked usage is the same as your defined usage limit.

### Free and freemium

If your app is free, you can use tracking usage for your analytics to understand how users are using your app. Free apps typically see higher usage, which count towards your app usage award tier - so you can make money without ever needing to set up subscriptions or authenticating users!

If you implement a freemium model for your app, which allows a certain amount of free usage per month (same as free trial), get them to upgrade, but reset at the end of the month.

If they can only use certain features, consider:

* Allowing access to those features within the free tier
* When they want to try a paid feature, give them some access to trial it (and track as you would any other usage and then require users authenticate and then subscribe to continue using that feature).

### Alternative authentication experiences

Most apps should use one of the standard authentication patterns described above.
However, in rare cases where your app's requirements can't be met using frictionless authentication, OAuth, or manual authentication, you may need to consider an alternative approach.

For guidance on how to handle these exceptional scenarios securely, see [Alternative authentication experiences](https://www.canva.dev/docs/apps/authenticating-users/alternative-auth-experiences/).

## API reference

* [`auth.getCanvaUserToken`](https://www.canva.dev/docs/apps/api/latest/user-auth-get-canva-user-token/)
* [`auth.requestAuthentication`](https://www.canva.dev/docs/apps/api/v1/user-auth-request-authentication/)
