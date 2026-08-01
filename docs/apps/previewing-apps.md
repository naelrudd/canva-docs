Source: https://www.canva.dev/docs/apps/previewing-apps/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Previewing apps

How to preview apps.

When you have set up your app, for example after [setting up the starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/), you can preview how it looks and behaves in the Canva editor.

There are two ways to preview your app:

* Generate a JavaScript bundle and upload it using the Developer Portal.
* Load the app from a local development server.

It'd be tedious to generate and upload a bundle after every change, so the first option is intended for when you're ready to [submit the app for review](https://www.canva.dev/docs/apps/submitting-apps/). To learn more, see [Bundling apps](https://www.canva.dev/docs/apps/bundling-apps/).

The second option is ideal during development because it offers the fastest development loop.

## Step 1: Start the local development server

Apps created with the starter kit or with a template through the Canva CLI both contain the necessary tools and webpack configuration required for starting a local server. The local server exposes the app's source code through a URL that can be shared with Canva.

To start the local development server:

1. Change into the app's folder:

   ```shell
   cd my-new-app
   ```

2. Run the `npm` command to start your app:

   ```shell
   npm start
   ```

The local server is available at [http://localhost:8080](http://localhost:8080) by default. If you navigate to this URL, you should see the app's (minified) source code.

### Using HTTPS

By default, the development server doesn't use the HTTPS protocol. This is convenient because there's no need for a security certificate, but it prevents you from previewing an app in Safari.

If you're using Safari (or otherwise need to use HTTPS):

1. Start the development server with the `--use-https` flag:

   ```shell
   npm run start --use-https
   ```

2. Navigate to [https://localhost:8080](https://localhost:8080).

3. Bypass the invalid security certificate warning:
   1. Click **Show details**.
   2. Click **Visit website**.

You'll need to bypass the invalid security certificate warning every time you start the server.

## Step 2: Configure the Development URL

In the Developer Portal, set the **App source > Development URL** field to the URL of the local development server. This field tells Canva to load the app's source code from the specified URL.



The URL must point directly to a standalone JavaScript file.

**Warning:** The **Development URL** field only exists as a convenient feature during development. You can't submit an app for review while the field contains a value.

## Step 3: Preview the app

In the Developer Portal, click the **Preview** button.

This will open the app in a new tab.

By default, apps use the [Design Editor](https://www.canva.dev/docs/apps/intents/design-editor/) intent. If your app implements multiple intents, you can use the dropdown next to the **Preview** button to choose which intent to preview. For more information, see [Intents](https://www.canva.dev/docs/apps/intents/).

The first time you open an app, it must be connected (installed). To do this, click the **Open** button. The app will then load within the iframe.

If you're using Google Chrome, click **Allow** when prompted by your browser to [allow local network access](https://www.canva.dev/#local-network-access-permission-required).

**Note:** You only have to install the app once, when using it for the first time.

### Reloading the app

If you make a change to the app — for example, by editing the `src/app.tsx` file — that change isn't immediately reflected in the app's iframe. You need to reload the app to preview the changes.

You can reload an app manually or automatically as the code changes.

#### Manual

To manually reload the app, do any of the following:

* Click the **Reload** button in the app's header.



  **Warning:** The **Reload** button is only visible if the app is under active development, in the **Draft** state. It's not visible once the app has been submitted for review or released.

* Return to the Developer Portal and click the **Preview** button.

* Right-click in the app's iframe and select **Reload frame**.

* Close and re-open the app in the Canva editor.

#### Automatic

The most efficient way to preview changes is with [Hot Module Replacement](https://webpack.js.org/concepts/hot-module-replacement/) (HMR). This is a feature of webpack that will automatically reload the app whenever the source code changes.

To enable HMR:

1. Navigate to an app using the [Your apps](https://www.canva.com/developers/apps) page.

2. Select **Security** -> **Credentials** -> **.env file**.

3. Copy the `.env` file contents.

4. Paste the contents into your app's `.env` file. For example:

   ```bash
   CANVA_APP_ID=AABBccddeeff
   CANVA_APP_ORIGIN=https://app-aabbccddeeff.canva-apps.com
   CANVA_HMR_ENABLED=TRUE
   ```

5. Restart the local development server.

6. Reload the app manually to ensure that HMR takes effect.

All changes to the source code will automatically be reflected in the app's iframe.

### Previewing apps using the desktop app

Although Canva has [a desktop app](https://www.canva.com/download/mac/), we recommend previewing apps using the web browser. Previewing apps using the desktop app requires a self-signed SSL certificate, which requires extra work without any meaningful benefit and isn't something we actively support.

### Previewing apps on mobile devices

Canva is extremely popular on mobile devices, so it's important to preview and test your app on them. The local development server on your computer won't be accessible from a mobile device though. The workaround is to upload the app's JavaScript bundle using the **App source** field so that the code can be loaded from Canva's servers.

## Known limitations

* You can't preview an app outside of the Canva editor. This is because the Apps SDK must be able to send and receive messages to and from the editor.

## Troubleshooting

### Local network access permission required

Chrome and other Chromium-based browsers require explicit permission to access local development servers for security reasons.



When you first preview your app, Chrome will display a permission prompt in the address bar. To grant access, click **Allow**.



If you have previously denied access to localhost in Chrome, you will see a crossed out network icon. If this is the case, you can still grant it:

1. Click the permission prompt icon in the address bar.
2. Toggle local network access to "on" to grant permission.

The permission is remembered for the current site during your session.

### App not loading or connection issues

If your app isn't loading in the Canva editor:

* **Verify the development server is running:** Check that `npm start` is running without errors.
* **Check the Development URL:** Ensure the URL in the Developer Portal matches your local server (for example, `http://localhost:8080`).
* **Check browser console:** Look for error messages that might indicate the issue.
* **Clear browser cache:** Sometimes cached content can cause loading issues.

### Hot module replacement not working

If changes aren't automatically reflected:

* Verify `CANVA_HMR_ENABLED=TRUE` is set in your `.env` file.
* Restart the development server after updating the `.env` file.
* Manually reload the app once after enabling HMR.
* Check that the `.env` file contains the correct `CANVA_APP_ID` and `CANVA_APP_ORIGIN`.

### Changes not appearing after manual reload

If changes aren't visible after reloading:

* Verify you're editing the correct file in your source code.
* Check that the development server detected the file change (watch for console output).
* Try a hard refresh in the browser (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows).
* Restart the development server.

### HTTPS certificate warnings

If you see security warnings when using HTTPS:

* This is expected behavior with self-signed certificates.
* You must bypass the warning each time you start the server.
* Consider using HTTP for development (use HTTPS only if required for Safari).

## Next step

Once you have an app up and running in the Canva editor, you can start writing code that hooks into the Canva editor by calling APIs exposed by the Apps SDK. To learn how, see [Integrating with Canva](https://www.canva.dev/docs/apps/integrating-canva/).
