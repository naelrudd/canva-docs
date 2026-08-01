Source: https://www.canva.dev/docs/apps/verifying-http-requests/

# HTTP request verification

How to verify the authenticity of HTTP requests.

## Step 1: Get a JWT from Canva

```ts
import { auth } from "@canva/user";
const token = await auth.getCanvaUserToken();
```

## Step 2: Send a request

```ts
const response = await fetch("http://localhost:3001/my/api/endpoint", {
  headers: {
    Authorization: `Bearer ${token}`,
  },
});
```

## Step 3: Verify the request

### Using @canva/app-middleware (recommended)

```typescript
import express from "express";
import { user } from "@canva/app-middleware/express";

const app = express();
app.use("/my/api", user.verifyToken({ appId: process.env.CANVA_APP_ID }));
```

### Manual verification

Extract the JWT from the `Authorization` header, verify it, and check the claims (`aud`, `brandId`, `userId`). Reject with `401` if invalid.
