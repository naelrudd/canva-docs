Source: https://www.canva.dev/docs/apps/app-configuration/canva-app-json/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# canva-app.json

Configuration file for Canva apps.

The `canva-app.json` file is the configuration file for Canva apps. It defines the app's scopes, supported devices, API versions, and other runtime settings.

When you create a new app using the [Canva CLI](https://www.canva.dev/docs/apps/canva-cli/), a `canva-app.json` file is automatically created in your project root directory with a default configuration.

## File location

The `canva-app.json` file is located in the root directory of your app project.

```
my-canva-app/
├── canva-app.json
├── package.json
└── src/
```

## Validation

The `canva-app.json` file is validated against the [JSON Schema](https://canva.dev/schemas/app/v1/manifest-schema.json). Most code editors with JSON Schema support provide validation and auto-completion when you include the `$schema` property.

## Properties

## Example configuration

The following is a complete example of a `canva-app.json` file for a Data Connector app:

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
