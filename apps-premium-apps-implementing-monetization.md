Source: https://www.canva.dev/docs/apps/premium-apps/implementing-monetization/

# Implementing monetization

Learn how to add premium features to your app.

## Step 1: Decide what Premium apps features to implement

Billable actions: `generate_image`, `generate_video`, `generate_audio`, `generate_text`, `modify_image`, `modify_video`, `modify_audio`, `modify_text`, `import_image`, `import_video`, `import_audio`, `import_text`.

## Step 2: Install the User SDK

```json
{
  "dependencies": {
    "@canva/user": "^2.2.0"
  }
}
```

## Step 3: Check whether a user can perform a billable action

```typescript
import { monetization } from "@canva/user";

const checkBillableAction = async (action: BillableAction) => {
  const canPerformAction = await monetization.isEnabled(action);
  if (canPerformAction) {
    // The user is enabled
  } else {
    // The user is not enabled
  }
};
```

## Step 4: Display your UI

```typescript
const [isActionEnabled, setIsActionEnabled] = useState<boolean>(false);

useEffect(() => {
  const checkIsActionEnabled = async () => {
    setIsActionEnabled(await monetization.isEnabled("generate_image"))
  };
  checkIsActionEnabled().catch(e => {});
}, []);

// <PremiumBadge enabled={isActionEnabled} />
```

## Step 5: Handle not-enabled users

```typescript
const performBillableAction = async (action: BillableAction) => {
  const canPerformAction = await monetization.isEnabled(action);
  if (canPerformAction) {
    // Do the billable action
  } else {
    const res = await monetization.requestEnableBillableAction(action);
    if (res.status !== "granted") {
      return;
    }
    // Do the billable action
  }
};
```

## Step 6: Execute premium features

### Run your code in a tracking session

```typescript
const importPremiumAsset = async () => {
  const session = await monetization.openTrackingSession({
    action: "import_image",
  });
  const image = await upload({ type: "image", mimeType: "image/jpeg", url: "...", thumbnailUrl: "...", aiDisclosure: "none" });
  await addElementAtPoint({ type: "image", ref: image.ref });
  session.closeTrackingSession();
};
```

### HTTP requests with tracking sessions

```typescript
async function generateImage(): Promise<TrackingId> {
  const token = await auth.getCanvaUserToken();
  const generationSession = monetization.openTrackingSession({ action: "generate_image" });
  try {
    const response = await fetch("https://example.com/generate", {
      headers: {
        Authorization: `Bearer ${token}`,
        "Canva-Premium-Usage-Id": generationSession.id,
      },
    });
    await generationSession.closeTrackingSession();
    return generationSession.id;
  } catch (error) {}
}
```

### Configure your backend

```typescript
if (!verified.aud || !verified.brandId || !verified.userId || !verified.billableActions) {
  return response.sendStatus(401);
}

if (!verified.billableActions.includes("generate_image")) {
  return response.sendStatus(403);
}
```

## Security considerations

Apps without a backend are vulnerable to users tampering with the JavaScript bundle. Consider implementing high-value parts of a billable action in a backend.
