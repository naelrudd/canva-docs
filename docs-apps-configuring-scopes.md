Source: https://www.canva.dev/docs/apps/configuring-scopes/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring scopes

How to manage an app's scopes.

At Canva, the privacy of our users is a top priority, but there are many valid reasons for apps to have access to their data. To balance these concerns, the Apps SDK has a scopes system that lets developers access user data while ensuring that users remain informed and in control of what data is accessed.

## How scopes work

In the Apps SDK, some methods have an associated *scope*. If an app uses one of these methods, the scope must be enabled with either the Developer Portal or the Canva CLI. If the scope isn't enabled, the app can't be approved for release.

By requiring apps to enable scopes, Canva can inform users of what data the app will have access to — and what the app can do with that data — before the user installs it.

## The user experience

Before a user installs an app, they're shown a screen that explains what the app is and what scopes are required to install it. If an app doesn't require any scopes, no requirements are listed.



If the user doesn't accept the app's scopes, the app can't be installed.

If a user uninstalls an app, all scopes are revoked.

## What scopes are required?

The scopes required by an app depend on the methods called by the app. For the complete list of scopes, along with the methods associated with those scopes, see [List of scopes](https://www.canva.dev/#list-of-scopes).

## How to configure scopes

You can configure scopes for your app with either the Developer Portal or the Canva CLI:

<Tabs storageKey="configuration">
  <Tab name="Developer Portal">
    1. Navigate to an app via the [Your apps](https://www.canva.com/developers/apps) page.
    2. On the **Scopes** page, enable the required scopes.


  </Tab>

  <Tab name="Canva CLI">
    1. Set up your app to use the Canva CLI to manage settings via the [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/#manage-configuration-using-the-canva-cli) file.
    2. Add the required scopes to the `runtime.scopes` property. For more information, see [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/#runtime-required).

       For example, the following adds the **Design read** and **Design write** scopes.

       ```json
       {
         "runtime": {
           "permissions": [
             {
               "name": "canva:design:content:read",
               "type": "mandatory"
             },
             {
               "name": "canva:design:content:write",
               "type": "mandatory"
             }
           ]
         }
       }
       ```
  </Tab>
</Tabs>

## List of scopes

This section lists the scopes that can be enabled for an app, including the methods that require the scope to be enabled. The required scopes are also listed on the API reference pages for each method.

### `canva:design:content:read`

The app may read the content of the user's design.

The following methods require this scope to be enabled:

* [`getCurrentPageContext`](https://www.canva.dev/docs/apps/api/latest/design-get-current-page-context/)
* [`initAppElement`](https://www.canva.dev/docs/apps/api/latest/design-init-app-element/), if the app calls the `registerOnElementChange` method
* [`selection.registerOnChange`](https://www.canva.dev/docs/apps/api/latest/design-selection-register-on-change/), if the app calls the `read` method

### `canva:design:content:write`

The app may modify the content of the user's design.

The following methods require this scope to be enabled:

* [`addAudioTrack`](https://www.canva.dev/docs/apps/api/latest/design-add-audio-track/)
* [`addElementAtCursor`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-cursor/)
* [`addElementAtPoint`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/)
* [`addNativeElement`](https://www.canva.dev/docs/apps/api/latest/design-add-native-element/)
* [`addPage`](https://www.canva.dev/docs/apps/api/latest/design-add-page/)
* [`initAppElement`](https://www.canva.dev/docs/apps/api/latest/design-init-app-element/), if the app calls the `addOrUpdateElement` method
* [`selection.registerOnChange`](https://www.canva.dev/docs/apps/api/latest/design-selection-register-on-change/), if the app calls the `save` method

### `canva:asset:private:read`

The app may download assets from the user's media library.

The following methods require this scope to be enabled:

* [`getTemporaryUrl`](https://www.canva.dev/docs/apps/api/latest/asset-get-temporary-url/)

### `canva:asset:private:write`

The app may upload assets to the user's media library.

The following methods require this scope to be enabled:

* [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/)

### `canva:brandkit:read`

The app may read data from brand kits that the user can access.

The following methods require this scope to be enabled:

* [`openColorSelector`](https://www.canva.dev/docs/apps/api/latest/asset-open-color-selector/)

### `canva:brandtemplate:read`

The app may read metadata and contents from brand templates that the user can access.

The following methods require this scope to be enabled:

* [`getDesignTemplateMetadata`](https://www.canva.dev/docs/apps/api/latest/design-get-design-template-metadata/)
