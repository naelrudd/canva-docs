Source: https://www.canva.dev/docs/apps/localization/

# Localization overview

Canva can translate your app into other languages.

## Supported locales

Arabic: `ar-EG`, Dutch: `nl-NL`, French: `fr-FR`, German: `de-DE`, Indonesian: `id-ID`, Italian: `it-IT`, Japanese: `ja-JP`, Korean: `ko-KR`, Malay: `ms-MY`, Polish: `pl-PL`, Portuguese: `pt-BR`, Romanian: `ro-RO`, Spanish: `es-ES` and `es-419`, Swedish: `sv-SE`, Thai: `th-TH`, Turkish: `tr-TR`, Vietnamese: `vi-VN`.

## How localization works

Uses `react-intl` library with `FormattedMessage` components.

1. Extract UI strings into a JSON file and upload as part of the review process.
2. Canva performs the translation.
3. Test your app with new locales.
4. Users see the app in their language automatically.

## MessageFormat syntax

Supports a subset of ICU `MessageFormat` syntax.

## Add notes for translators

Include `description` property in each `FormattedMessage`.

## Excluding text

Use ESLint directive to ignore the rule:
```typescript
// eslint-disable-next-line no-literal-string-in-jsx
<Text>Text that must not be translated</Text>
```

## Locale fallback

Falls back to English `en` if no translations are available.
