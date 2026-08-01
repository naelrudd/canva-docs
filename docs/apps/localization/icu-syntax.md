Source: https://www.canva.dev/docs/apps/localization/icu-syntax/

# ICU syntax

Canva supports a subset of International Components for Unicode (ICU).

## Supported syntax

### Basic messages
```tsx
<FormattedMessage
  defaultMessage="My internationalized app"
  description="The title the user sees when opening the app."
/>
```

### Interpolation
```tsx
<FormattedMessage
  defaultMessage="Welcome {firstName}!"
  values={{ firstName: name }}
/>
```

### Plurals
```tsx
<FormattedMessage
  defaultMessage={`Use {creditsCost, number} of {remainingCredits, plural,
    one {# credit}
    other {# credits}
  }`}
  values={{ creditsCost, remainingCredits }}
/>
```

### Numbers
```tsx
<FormattedMessage
  defaultMessage="Image generation is {progress, number, ::percent} complete."
  values={{ progress: 0.75 }}
/>
```

### Dates
```tsx
<FormattedMessage
  defaultMessage="Credits refresh on: {refreshDate, date, short}"
  values={{ refreshDate: new Date() }}
/>
```

### Select
```tsx
<FormattedMessage
  defaultMessage="Hello, {role, select, admin {Administrator} other {User}}!"
  values={{ role }}
/>
```

### Rich text
```tsx
<FormattedMessage
  defaultMessage="Discover <link>gallery</link>"
  values={{
    link: (chunks) => <Link href={url}>{chunks}</Link>,
  }}
/>
```

## Unsupported syntax

* Multiple `plural` arguments in one string
* `plural` with `offset` property
* `selectordinal` argument
* `choice` argument
* Strings with over 20 combinations
* Nested selects/plurals (except when the nested argument is a simple placeholder)
