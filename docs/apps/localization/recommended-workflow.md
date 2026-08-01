Source: https://www.canva.dev/docs/apps/localization/recommended-workflow/

# Recommended workflow

Canva can translate your app into other languages.

## Step 1: Using FormattedMessage

```ts
import { FormattedMessage, useIntl } from "react-intl";
```

```ts
<Text>
  <FormattedMessage
    description="Message that welcomes the user to the app"
    defaultMessage="Welcome to {appName}."
    values={{ appName: 'My Cool App' }}
  />
</Text>
```

## Step 2: Testing localization

Use the `@canva/app-i18n-kit` package to test with pseudolocalization.

## Step 3: Generate the JSON file

```shell
npm run build
```

The file `messages_en.json` is generated.

## Step 4: Upload the JSON file

Upload it as part of the app submission process in the Developer Portal.
