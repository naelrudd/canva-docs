Source: https://www.canva.dev/docs/apps/localization/outside-react-components/

# Localize outside React components

Use Canva-provided translations outside React components with the initIntl function.

## Using initIntl

```typescript
import { initIntl } from "@canva/app-i18n-kit";

const intl = initIntl();

async function getPublishConfiguration() {
  return {
    status: "completed",
    outputTypes: [
      {
        id: "post",
        displayName: intl.formatMessage({
          defaultMessage: "Feed Post",
          description: "Label shown in the output type dropdown",
        }),
      },
    ],
  };
}
```

NOTE: Call `initIntl()` once at module level.
