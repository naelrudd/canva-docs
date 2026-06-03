Source: https://www.canva.dev/docs/apps/localization/bad-practices/

# Bad practices

Common localization mistakes to avoid and how to fix them.

## Not setting up i18n linting
**Don't** skip setting up i18n linting. **Do** set up the recommended i18n linting.

## Unformatted strings
**Don't** render strings without localizing them:
```jsx
<Text>Welcome to My App</Text>
```
**Do** use `intl.formatMessage` or `<FormattedMessage>`:
```jsx
<Text><FormattedMessage defaultMessage="Welcome to My App" /></Text>
```

## Use dynamic id or defaultMessage values
**Don't** use dynamic id/defaultMessage values — `@formatjs/cli` won't extract them.

## Render strings returned from the backend
**Don't** render untranslated strings from the backend. **Do** map backend responses to predefined messages.

## Define placeholder-only messages
**Don't** define messages that only contain variable placeholders like `{selectedOption}`.
