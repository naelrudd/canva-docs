Source: https://www.canva.dev/docs/apps/design-guidelines/localization/

# Localization

Design guidelines for localizing your app.

When designing an app for a global audience, it's essential to consider how localization affects user experience. The following guidelines will help you create a user-friendly interface that adapts seamlessly to different languages and cultures.

## Use the App UI kit

The [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/) was designed for a global audience. Using its components, patterns, colors, typography, and icons will help ensure effective communication across different languages and cultures.

## Allow for text expansion

As text length can change with translation, keep calls to action and labels short and concise to ensure your interface adapts well.

NOTE: To ensure your app displays properly in different languages, use the left-to-right and right-to-left pseudolocalization options in the Dev Toolkit. This simulates foreign languages by adding different characters and longer strings. After translation, preview your app in various languages using the Dev Toolkit.

## Keep the language simple

Avoid using acronyms, abbreviations, slang, jargon, idioms, and jokes in your interface. These may not translate well into other languages, even if they're common in one culture.

## Avoid multi-line clauses

Breaking a single clause into multiple lines can lead to grammatically incorrect translations. Instead, let the line wrap naturally or divide the clause so that each part is grammatically independent.

## Don't link entire sentences

When adding links to text, only link the action or destination, keeping it as a single term or short phrase. Use the external link component for linking.

## Review all images

If your app uses images for context, consider cultural sensitivities and ensure they're suitable and easily understood by a global audience. Consider these risks when using images:

* **Flags**: Different countries may recognize flags differently.
* **Maps**: Boundaries can be interpreted differently across countries.
* **People**: Pay attention to gestures, hands, and racial representations.
* **Symbols**: Be mindful of national, political, religious, or spiritual symbols.
* **Cultural associations**: Colors, numbers, names, and events can have varying meanings.

## Keep text out of images

As text in images can't be translated, using such images in your interface can undermine your app's localization efforts.

## Localize numbers, currencies, and dates

### Numbers

* Use numeric digits (for example, 12345) instead of words for numbers.
* Use the recommended i18n tooling when displaying numbers. The tooling automatically adds the correct digit group separator for large numbers, depending on the locale (for example, 3,500 in English).
* Spell out single-digit numbers if they start a sentence. e.g. Seven.
* Write number sequences or ranges consistently.

For more information and examples, see [Numbers](https://www.canva.dev/docs/apps/localization/icu-syntax/#numbers).

### Credit usage

If your app requires users to spend credits to generate a design or perform an action, make sure to specify the number of credits that will be used for the action, and the total or remaining credits they have available. We recommend the format: "Use X of Y \[App name] credits" to clearly communicate how many credits will be spent from the total available.

For example ICU syntax, see [Pluralization](https://www.canva.dev/docs/apps/localization/icu-syntax/#plurals).

### Decimals and fractions

As a general rule, use rounded numbers. If rounding isn't possible, use the fewest decimals or spell it out as a fraction.

### Percentages

Use the % symbol instead of spelling out 'percent'.

### Phone numbers

If you need to reference a phone number:

* Use country codes for clarity
* Use spaces between sets of numbers

### Ranges and spans

Use 'to' between a range of numbers. If space is limited, use an en dash with no spaces on either side.

### Measurement

If your app displays measurements, we recommend using the metric system for a global audience. If you choose to use the imperial system, ensure it's applied consistently throughout and avoid mixing metric and imperial units.

### Temperatures

* Use numerals and the word 'degrees' for temperatures.
* Specify Celsius or Fahrenheit the first time you mention a temperature.
* Don't repeat the word 'degrees' if it's already implied or if you've included the degree symbol.
* If space is limited, use the degree symbol and abbreviate the temperature scale.

### Currencies

When displaying prices, either specify the currency of the item's origin or ensure your audience sees a localized price.
For your app's pricing, use the [Link](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/docs/components-link-link--docs) component to link to your website, where the price can be shown in the user's local currency format.

### Dates

If you're just displaying a date with no other message content, you can just use `<FormattedDate/>` or `intl.formatDate`, so that users can see dates that reflect their localization settings.

Use the [DateInput](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/docs/components-form-date-input--docs) component so that users can see dates that reflect their localization settings.

In cases where a date is displayed rather than selected, there are 4 standard time formats you can use:

| Format   | Description                                         | Example               |
| -------- | --------------------------------------------------- | --------------------- |
| `short`  | A numerical format                                  | 1/3/24                |
| `medium` | Includes the month's name with abbreviation         | Mar 1, 2024           |
| `long`   | Includes the month's name without abbreviation      | March 1, 2024         |
| `full`   | Includes the name for the month and day of the week | Friday, March 1, 2024 |

For more information and examples, see [Dates](https://www.canva.dev/docs/apps/localization/icu-syntax/#dates).

## Localize times

Use the following format for times, letting your audience see times that reflect their locale.

There are 4 standard time formats you can use:

| Format   | Description                                     | Example             |
| -------- | ----------------------------------------------- | ------------------- |
| `short`  | Includes hours and minutes                      | 10:40 AM            |
| `medium` | Includes hours, minutes, seconds                | 10:40:29 AM         |
| `long`   | Includes hours, minutes, seconds, and time zone | 10:40:29 AM GMT +10 |
| `full`   | Includes hours, minutes, seconds, and time zone | 10:40:29 AM GMT +10 |

To indicate a time range, use the word 'to' instead of a hyphen. Avoid using words like 'last' and 'next' when you write about time. For example, the phrase 'during the last month' could mean during the previous month or during the final month.

### Time zones

Use the Coordinated Universal Time (UTC) offset to ensure dates and times are correctly adjusted for the user's location.

## More information

* Overview of the localization process: [Localization overview](https://www.canva.dev/docs/apps/localization/)
* Learn how to use the recommended workflow: [Recommended workflow](https://www.canva.dev/docs/apps/localization/recommended-workflow/)
* Learn how to localize an existing app: [Migrate an existing app](https://www.canva.dev/docs/apps/localization/migrate-an-existing-app/)
* Review the supported syntax and exceptions: [ICU syntax](https://www.canva.dev/docs/apps/localization/icu-syntax/)
