Source: https://www.canva.dev/docs/apps/cross-origin-resource-sharing/

# Cross-Origin Resource Sharing

How to troubleshoot and fix CORS errors.

## What is CORS?

Cross-Origin Resource Sharing (CORS) is a security feature of web browsers that blocks client-side HTTP requests between different *origins*.

The app's frontend is hosted on:
```
https://app-CANVA_APP_ID.canva-apps.com
```

## Fixing CORS errors

The backend must set `Access-Control-Allow-Origin` header.

### Express.js example

```ts
import express from "express";
import cors from "cors";

const CANVA_APP_ID = process.env.CANVA_APP_ID?.toLowerCase();

const app = express();
app.use(cors({
  origin: `https://app-${CANVA_APP_ID}.canva-apps.com`,
  optionsSuccessStatus: 200,
}));
```

### Handling preflight requests

Browsers send `OPTIONS` requests before the actual request. The backend must handle these.

### Handling multiple origins

Create an allowlist of supported origins and dynamically set the header.
