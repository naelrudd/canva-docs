Source: https://www.canva.dev/docs/apps/app-ui-kit/colors/

# Colors

An overview of colors in the App UI Kit.

Canva has a distinct and vibrant color palette. The App UI Kit exposes a subset of this palette as [design tokens](https://www.canva.dev/docs/apps/app-ui-kit/design-tokens/). You can use these colors to create a user interface that matches Canva's aesthetic.

## Using colors

The colors are exposed in the following formats:

* CSS variables
* JavaScript variables
* React component props (with exceptions)

You can use the CSS and JavaScript variables as you would any other design token.

In the case of React component props, some props only accept specific colors. For example, the `Alert` component only accepts the following colors for the `tone` prop:

```tsx
<Alert tone="info">This is an alert.</Alert>
<Alert tone="warn">This is an alert.</Alert>
<Alert tone="positive">This is an alert.</Alert>
<Alert tone="critical">This is an alert.</Alert>
```

These props are documented in [Storybook](https://www.canva.dev/docs/apps/app-ui-kit/storybook/) and available as autocomplete options via IntelliSense.

## List of color tokens

### Actions

These colors are used to perform actions, in such components as buttons, menu items or pills.

#### Primary

Key actions that represent the main purpose of the interface.

#### Secondary

Supporting actions such as secondary buttons and pills.

#### Tertiary

Subdued actions such as menu items and teritary buttons.

#### Overlay

Actions that appear over busy and vibrant backgrounds.

#### Selected

Actions that indicate a user selection or the origin of an effect.

#### General

Universal color states that apply across multiple components.

### Feedback

#### Positive

Successes and other positive information.

#### Info

General information.

#### Warn

Cautionary information.

#### Critical

Errors and problems.

#### Hint

Hints and assistive information.

#### Overlay

Info over busy backgrounds.

### UI

Neutral grays, focus and overlay colors for use within UI components, such as alert or thumbnail backgrounds.

### Content

General text and icons.

### Control

Form elements such as text inputs, selects, pickers, sliders and switches.

#### General

Default states for interactive form elements.

#### Critical

Error states and validation problems in form controls.

#### Selected

Active or chosen states in form controls.

### Link

Navigational link elements.

### Handle

Tactile handles and grabbers.

### Surface backgrounds

Elevation backgrounds of various surface containers.
