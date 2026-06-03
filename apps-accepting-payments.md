Source: https://www.canva.dev/docs/apps/accepting-payments/

# External payment links

How to monetize apps by accepting payments from users.

## How to accept payments

### Step 1: Authenticate the user

Create a link between the user in Canva and the user in the app's backend.

See [Authenticating users](https://www.canva.dev/docs/apps/authenticating-users/).

### Step 2: Check if the app can link to a payment flow

```ts
import { getPlatformInfo } from "@canva/platform";

const info = getPlatformInfo();
console.log(info.canAcceptPayments);
```

### Step 3: Show a call-to-action

```tsx
import { Alert, Link } from "@canva/app-ui-kit";
import { getPlatformInfo, requestOpenExternalUrl } from "@canva/platform";

const UPGRADE_URL = "https://www.example.com/upgrade";

export function App() {
  return (
    <div>
      <UpgradeLink />
    </div>
  );
}

function UpgradeLink() {
  const info = getPlatformInfo();

  if (info.canAcceptPayments) {
    async function handleClick() {
      await requestOpenExternalUrl({ url: UPGRADE_URL });
    }
    return (
      <Link href={UPGRADE_URL} requestOpenExternalUrl={handleClick}>
        Upgrade
      </Link>
    );
  }

  return (
    <Alert tone="info">
      Open this app in a web browser to learn how to upgrade.
    </Alert>
  );
}
```

## API reference

* [`auth.getCanvaUserToken`](https://www.canva.dev/docs/apps/api/latest/user-auth-get-canva-user-token/)
* [`auth.requestAuthentication`](https://www.canva.dev/docs/apps/api/v1/user-auth-request-authentication/)
* [`getPlatformInfo`](https://www.canva.dev/docs/apps/api/latest/platform-get-platform-info/)
* [`requestOpenExternalUrl`](https://www.canva.dev/docs/apps/api/latest/platform-request-open-external-url/)
