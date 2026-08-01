Source: https://www.canva.dev/docs/apps/setting-up-starter-kit/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting up the starter kit

How to set up Canva's app development starter kit.

By itself, [creating an app via the Developer Portal](https://www.canva.dev/docs/apps/quickstart/) doesn't do anything. You need to write the source code that defines the app's behavior and then share that code with Canva.

The source code must be provided as a standalone JavaScript bundle. To simplify the process of [generating this bundle](https://www.canva.dev/docs/apps/bundling-apps/), we've created a [starter kit](https://github.com/canva-sdks/canva-apps-sdk-starter-kit) — a GitHub repository that contains the boilerplate of an app and all the recommended tooling, including the [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/), [TypeScript](https://www.typescriptlang.org/), [React](https://react.dev/), and [webpack](https://webpack.js.org/).

While it's technically possible to create apps without the starter kit, the documentation assumes you're using it.

## TL;DR

```bash
git clone https://github.com/canva-sdks/canva-apps-sdk-starter-kit.git
cd canva-apps-sdk-starter-kit
npm install
```

## Prerequisites

To set up the starter kit, the following tools need to be installed:

* git
* Node.js `v24`
* npm `v11`

To learn more, see [Prerequisites](https://www.canva.dev/docs/apps/prerequisites/).

## Step 1: Clone the starter kit

The starter kit is available as a GitHub repo.

To clone the starter kit, run the following command:

```bash
git clone https://github.com/canva-sdks/canva-apps-sdk-starter-kit.git
```

By default, the repo is cloned into a directory named `canva-apps-sdk-starter-kit`. You can customize this name by passing a different name into the `git clone` command:

```bash
git clone https://github.com/canva-sdks/canva-apps-sdk-starter-kit.git my-custom-name
```

## Step 2: Install the dependencies

The `package.json` file contains a number of dependencies, such as React.

To install the dependencies:

1. Navigate into the starter kit:

   ```bash
   cd canva-apps-sdk-starter-kit
   ```

2. Run the following command:

   ```bash
   npm install
   ```

## Step 3: Explore the starter kit

Take a moment to explore the starter kit. If you have experience with modern JavaScript development, the structure and conventions should look familiar.

In particular, here are a few details worth highlighting:

* The entry point for the app is the `src/app.tsx` file.
* The app uses the [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/) to mimic the look and feel of Canva.
* The `examples` directory contains usage examples for the APIs.

## Next step

After setting up the starter kit, the next step is to preview your app in the Canva editor — and, ideally, preview it at regular intervals. To learn how to do this, see [Previewing apps](https://www.canva.dev/docs/apps/previewing-apps/).
