Source: https://www.canva.dev/docs/apps/design-guidelines/forms/

# Forms

Guidelines for creating user-friendly forms.

## Use the pre-built form components

For user-friendly, consistent forms, your best bet is to use and combine our App UI Kit form components, which have a lot of common accessibility features built in. These include:

* Form controls:
  * `Select`
  * `Checkbox`
  * `RadioGroup`
  * `SegmentedControl`.
* `FormField` (can be combined with any form input or control to provide consistent layout and accessibility features).
* Inputs:
  * `TextInput`
  * `NumberInput`
  * `MultilineInput`.
* `FileInput` (form component supporting file upload).

## Don't rely on placeholders

Placeholders can be a useful way to indicate expected values, but:

* They aren't as prominent as labels.
* They aren't visible when inputs have focus.

Always use placeholders in addition to labels.

## Correctly assign labels to inputs

It's not enough to visually associate a label with an input. You must add an `id` to the input and the `for` (in HTML) or `htmlFor` (in JSX) attribute to the label:

```tsx
<label htmlFor="email">Email</label>
<input type="text" id="email" />
```

This ensures that:

* Clicking the label will focus the field.
* Screen readers can understand the form.

## Use checkboxes and radio buttons appropriately

Checkboxes and radio buttons appear similar, but they serve different purposes:

* Use checkboxes when the user should be able to select **any combination** of options.
* Use radio buttons when the user should only be able to select **one** option.

## Show error states

If the user enters or submits an invalid value, show the input in an error state.

If it's not obvious *why* an error is occurring, show an error message beneath the input. To learn how to write effective error messages, see [Errors & messaging](https://www.canva.dev/docs/apps/design-guidelines/errors/).
