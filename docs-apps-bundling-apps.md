Source: https://www.canva.dev/docs/apps/bundling-apps/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Bundling apps

How to generate a JavaScript bundle for an app.

When you're ready to [submit an app for review](https://www.canva.dev/docs/apps/submitting-apps/), you need to upload the app to the [Developer Portal](https://www.canva.com/developers/) as a standalone JavaScript bundle. The [starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/) includes a build script that handles this for you.

## How to generate a bundle

1. Navigate into the starter kit:

   ```bash
   cd canva-apps-sdk-starter-kit
   ```

2. Run the following command:

   ```bash
   npm run build
   ```

   An `app.js` file will appear in the `dist` directory.

## How to upload a bundle

1. Log in to the Developer Portal.
2. Navigate to an app via the [Your apps](https://www.canva.com/developers/apps) page.
3. Upload the `app.js` file to the **App source > JavaScript file** field.

## Known limitations

* Canva doesn't support code-splitting, so all code and dependencies must be bundled in a single file. (You can still organize your code into separate files. The webpack configuration in the starter kit takes care of the bundling.)
* The size of the app bundle must not exceed 5MB.
