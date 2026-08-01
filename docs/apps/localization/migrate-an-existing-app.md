Source: https://www.canva.dev/docs/apps/localization/migrate-an-existing-app/

# Migrate an existing app

How to add localization support to an existing app.

## Phase 1: Configure your workspace

### Step 1: Install prerequisites

```shell
npm install @canva/app-i18n-kit react-intl @canva/app-ui-kit@latest && npm install --save-dev @formatjs/cli
```

### Step 2: Configure ESLint

```shell
npm install --save-dev eslint @canva/app-eslint-plugin
```

### Step 3: Configure webpack for FormatJS

```shell
npm install --save-dev @formatjs/ts-transformer
```

### Step 4: Configure webpack chunk limit

Use `optimize.LimitChunkCountPlugin({ maxChunks: 1 })` to ensure a single bundle.

## Phase 2: Updating your app

### Step 1: Add the dependency

Use `AppI18nProvider` instead of `IntlProvider` from `react-intl`.

### Step 2: Update UI strings

Use `FormattedMessage` or `useIntl()` hook.

## Phase 3: Testing and release

### Step 1: Testing localization

Use pseudolocalization in the Dev Toolkit.

### Step 2: Generate the JSON file

```shell
npm run build
```

### Step 3: Upload the JSON file

Upload in the Developer Portal.
