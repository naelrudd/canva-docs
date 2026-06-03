Source: https://www.canva.dev/docs/apps/using-design-ids/

# Using design IDs

How to store and retrieve data against a user's design.

Sometimes, apps need to associate data with a user's design. For example, an app could present the user with settings that persist on a per-design basis.

## Step 1: Get a design and user token

```tsx
import { auth } from "@canva/user";
const userToken = await auth.getCanvaUserToken();

import { getDesignToken } from "@canva/design";
const designToken = await getDesignToken();
```

## Step 2: Send the tokens to the app's backend

```tsx
const response = await fetch(
  `http://localhost:3001/my/api/endpoint?designToken=${designToken}`,
  {
    method: "POST",
    headers: {
      Authorization: `Bearer ${userToken}`,
    },
  }
);
```

## Step 3: Verify the tokens

For Node.js backends, use the [`@canva/app-middleware`](https://www.npmjs.com/package/@canva/app-middleware) package.

```typescript
import express from "express";
import { design, tokenExtractors } from "@canva/app-middleware/express";

const app = express();

app.post(
  "/my/api/design",
  design.verifyToken({
    appId: process.env.CANVA_APP_ID,
    tokenExtractor: tokenExtractors.fromQuery("designToken"),
  }),
  (req, res) => {
    const { designId, appId } = req.canva.design;
    res.sendStatus(200);
  }
);
```

### Manually verifying JWTs

```ts
const verifiedUserToken = jwt.verify("USER_JWT_GOES_HERE", publicKey, {
  audience: "YOUR_APP_ID",
});

const verifiedDesignToken = jwt.verify("DESIGN_JWT_GOES_HERE", publicKey, {
  audience: "YOUR_APP_ID",
});
```

User token contains: `aud`, `brandId`, `userId`.
Design token contains: `aud`, `designId`.

## Step 4: Store data against the design

Data should be linked with the combination of the design ID, the user ID, and the team ID.

## Security guidelines

* Decode and verify tokens through the backend — never through the frontend.
* Get fresh tokens from Canva before sending to the backend.
* Send tokens and relevant data in the same request.
