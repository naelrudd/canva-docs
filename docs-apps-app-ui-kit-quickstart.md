Source: https://www.canva.dev/docs/apps/app-ui-kit/quickstart/

# Quickstart

Get up and running with the App UI Kit.

The App UI Kit is a React-based component library for Canva apps. If you're using the [starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/), the App UI Kit is already set up for you. If you're not using the starter kit, this guide will help you get started.

## Step 1: Install the App UI Kit

In the project's directory, run the following command:

```bash
npm install @canva/app-ui-kit
```

## Step 2: Set up the `AppUiProvider`

At the root of the application, such as in a project's `index.tsx` file:

1. Import the following stylesheet:

   ```tsx
   import "@canva/app-ui-kit/styles.css";
   ```

2. Import the `AppUiProvider` component:

   ```tsx
   import { AppUiProvider } from "@canva/app-ui-kit";
   ```

   This component provides theming and user preferences to App UI Kit components.

3. Wrap the app in the `AppUiProvider` component:

   ```tsx
   <AppUiProvider>
     <App />
   </AppUiProvider>
   ```

   **Note:** You should only use the `AppUiProvider` component once in an app's component tree.

## Step 3: Start using the components

1. Import components from the `@canva/app-ui-kit` package:

   ```tsx
   import { Button, Rows, Text, Title } from "@canva/app-ui-kit";
   ```

2. Use them as you would any other React component:

   ```tsx
   export function App() {
     return (
       <Rows spacing="2u">
         <Rows spacing="1u">
           <Title>Hello world</Title>
           <Text>This is a paragraph of text.</Text>
         </Rows>
         <Button variant="primary">Click me</Button>
       </Rows>
     );
   }
   ```

   **Warning:** For your app to be theme-responsive, App UI Kit components and any custom components must be wrapped in `AppUiProvider`.

## Next steps

Once you're up and running, either:

* Check out the [Storybook](https://www.canva.dev/docs/apps/app-ui-kit/storybook/) to explore the available components.
* Play around with the components in your app.
