Source: https://www.canva.dev/docs/apps/app-ui-kit/design-tokens/

# Design tokens

What are design tokens? Why use them?

A *design token* is a variable used to store design-related values, such as colors. They act as a single source of truth for design properties, simplifying the maintenance of interface elements and enabling features, such as theming.

The App UI Kit exposes design tokens as JavaScript variables, CSS variables, and React component props. Apps can use these tokens to customize components or create components that match the look and feel of Canva.

Your app [must be wrapped in `AppUiProvider`](https://www.canva.dev/docs/apps/app-ui-kit/quickstart/#step-2-set-up-the-appuiprovider) for design tokens to work, even if you're using custom components.

## Using design tokens

### CSS variables

You can use the CSS variables in global stylesheets, CSS modules, or your app's source code:

```css
.button {
  background-color: var(--ui-kit-color-content-fg);
}
```

The variables are written in kebab case and prefixed with `--ui-kit-`.

### JavaScript variables

You can use the JavaScript variables in your app's source code:

```tsx
import { AppUiProvider, tokens } from "@canva/app-ui-kit";
import "@canva/app-ui-kit/styles.css";

function App() {
  return (
    <AppUiProvider>
      <div style={{ backgroundColor: tokens.colorContentFg }}>Hello world.</div>
    </AppUiProvider>
  );
}
```

The variables are written in camel case, without a prefix.

**Note:** The values of the JavaScript variables are CSS variables. For example, the value of the `colorContentFg` token is `var(--ui-kit-color-content-fg)`, not the underlying CSS value that the variable resolves to.

### React component props

The props of some components only accept certain tokens. This prevents you from using components in a way that would be unfamiliar to Canva's users. For example, the `Button` component only has three color variants:

```tsx
<Button variant="primary">Click me</Button>
<Button variant="secondary">Click me</Button>
<Button variant="tertiary">Click me</Button>
```

These props are documented in [Storybook](https://www.canva.dev/docs/apps/app-ui-kit/storybook/) and available as autocomplete options via IntelliSense.

## List of design tokens

You can find the reference documentation for the tokens on the following pages:

* [Colors](https://www.canva.dev/docs/apps/app-ui-kit/colors/)
* [Shadows](https://www.canva.dev/docs/apps/app-ui-kit/shadows/)
* [Spacing](https://www.canva.dev/docs/apps/app-ui-kit/spacing/)
* [Transitions](https://www.canva.dev/docs/apps/app-ui-kit/transitions/)
