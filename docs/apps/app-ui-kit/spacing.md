Source: https://www.canva.dev/docs/apps/app-ui-kit/spacing/

# Spacing

An overview of spacing in the App UI Kit.

The App UI Kit exposes a spacing scale. This scale is made up of a limited range of numeric [design tokens](https://www.canva.dev/docs/apps/app-ui-kit/design-tokens/) that are multiples of the [base unit](https://www.canva.dev/docs/apps/app-ui-kit/units/). By using these tokens, the size of and spacing between components remains consistent, which results in a more polished and visually harmonious experience.

## Using spacing tokens

The tokens that make up the spacing scale are exposed as:

* CSS variables
* JavaScript variables
* React component props (with exceptions)

You can use the CSS and JavaScript variables as you would any other design token.

In the case of React component props, some props only accept values from the spacing scale. For example, the `Rows` component has a `spacing` prop that sets the vertical margin between its children:

```tsx
<Rows spacing="2u">
  <Box>This is a box.</Box>
  <Box>This is a box.</Box>
  <Box>This is a box.</Box>
</Rows>
```

This code will render three rows of boxes with 2 units (16 pixels) between each row.

When passing values from the scale as props, the value takes the form of "𝑥u," where "𝑥" is a number on the scale, and "u" is an abbreviation of "unit." An exception to this rule is when the value is "0," because this value doesn't have a suffix.

## List of spacing tokens

### Spacing scale

### Other spacing tokens
