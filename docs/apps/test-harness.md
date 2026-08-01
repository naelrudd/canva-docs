Source: https://www.canva.dev/docs/apps/test-harness/

# Test harness

A step by step guide setting up the Apps SDK test harness.

The Canva Apps SDK test harness lets you run and test your Canva app outside of the Canva environment.

NOTE: The Canva Apps SDK harness is provided as an experimental resource to support development.

## Step 1: Create required directories

```bash
mkdir -p harness public
```

## Step 2: Create the harness HTML file

Create `public/harness.html` with:
```html
<!doctype html>
<html dir="ltr" lang="en" class="cc24 theme dark">
  <head>
    <title>Canva Apps SDK Test Harness</title>
    <script src="/init.js" defer></script>
    <script src="/harness.js" defer></script>
  </head>
  <body style="width: 360px; height: 770px; padding: 10px; border: 1px solid red; overflow-y: auto; overflow-x: hidden;">
    <div id="root" style="width: 100%; height: 100%"></div>
  </body>
</html>
```

## Step 3: Create `harness/init.ts`

```typescript
import * as design from "@canva/design/test";
import * as asset from "@canva/asset/test";
import * as user from "@canva/user/test";
import * as error from "@canva/error/test";
import * as intents from "@canva/intents/test";
import * as platform from "@canva/platform/test";

design.initTestEnvironment();
asset.initTestEnvironment();
error.initTestEnvironment();
user.initTestEnvironment();
intents.initTestEnvironment();
platform.initTestEnvironment();
```

## Step 4: Create `harness/harness.tsx`

```typescript
import React from "react";
import { TestAppUiProvider } from "@canva/app-ui-kit";
import { createRoot } from "react-dom/client";
import { App } from "../src/app";
import "@canva/app-ui-kit/styles.css";
import { TestAppI18nProvider } from "@canva/app-i18n-kit";

const root = createRoot(document.getElementById("root") as Element);

function render() {
  root.render(
    <TestAppI18nProvider>
      <TestAppUiProvider>
        <App />
      </TestAppUiProvider>
    </TestAppI18nProvider>,
  );
}

render();
```

## Step 5: Update webpack configuration

Modify `webpack.config.ts` to support the harness environment.

## Step 6: Run the test harness

```bash
IN_HARNESS=true npx webpack serve --config webpack.config.ts --mode development
```

## Step 7: View your app

Open [http://localhost:8080/harness.html](http://localhost:8080/harness.html)
