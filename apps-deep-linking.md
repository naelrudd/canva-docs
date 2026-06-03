Source: https://www.canva.dev/docs/apps/deep-linking/

# Deep linking

How to link directly to apps in the Canva editor.

## Find your app's unique identifier (ui)

1. Navigate to the [Your apps](https://www.canva.com/developers/apps) page.
2. Click the app.
3. Click **Preview** to open the app in a new tab.
4. In the address bar, the URL ends with something like `/edit?ui=abCDEfg1HiJ_...`. Copy the `ui` value.

## Create a link to your app for a design type

```
https://www.canva.com/login/?redirect=%2Fdesign%3Fcreate%26type%3D<TYPE-ID>%26ui%3D<APP-UI>
```

## Create a link to your app for a template

```
https://www.canva.com/login/?redirect=%2Fdesign%3Fcreate%26template%3D<TEMPLATE-ID>%26ui%3D<APP-UI>
```
