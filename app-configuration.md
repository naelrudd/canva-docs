Source: https://www.canva.dev/docs/apps/app-configuration/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# App configuration

Manage the settings for your Canva app.

You can manage configuration for your app using the following methods:

* Canva CLI
* Canva Developer Portal

The configuration for an app includes settings such as [intents](https://www.canva.dev/docs/apps/intents/), [scopes](https://www.canva.dev/docs/apps/configuring-scopes/) and [authentication](https://www.canva.dev/docs/apps/authenticating-users/).

## Manage configuration using the Canva CLI

The Canva CLI can be used to manage your app's intents and scopes.

To check everything is set up for your app to manage configuration, run the [Canva Apps Doctor](https://www.canva.dev/docs/apps/canva-cli/#step-4-run-a-health-check-on-your-app). This creates or updates your [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/) file. At any time you can run the Apps Doctor to check the health of your app configuration.

Using the Canva CLI, you can pull the configuration from the Developer Portal, push your local configuration to update the Developer Portal, or check the status of your configuration with the [apps config commands](https://www.canva.dev/docs/apps/canva-cli/#commands).

### Example workflow: enabling the Data Connector intent

1. Run `canva apps config pull` to fetch the app configuration from the Developer Portal.
2. Edit the `canva-app.json` file to add the intent and required scopes (`permissions`):
   ```json
   {
     "$schema": "https://www.canva.dev/schemas/app/v1/manifest-schema.json",
     "manifest_schema_version": 1,
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
       ],
     },
     "intent": {
       "data_connector": {
         "enrolled": true
       }
     }
   }
   ```
3. Run `canva apps config push` to submit the local changes to the Developer Portal, and when prompted, confirm that the changes should be applied.

## Manage configuration using the Developer Portal

To manage app settings using the Developer Portal:

1. Navigate to an app via the [Your apps](https://www.canva.com/developers/apps) page on the Developer Portal.
2. Change the settings on the relevant tabs.
