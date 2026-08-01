Source: https://www.canva.dev/docs/apps/localization/backend-responses/

# Localize backend responses

Handle translations when your app's content depends on API responses.

## Preferred: Frontend localization

The backend should return status codes or identifiers. The frontend maps these to `FormattedMessage`.

```typescript
const getErrorMessage = (errorCode: ErrorCode) => {
  switch (errorCode) {
    case "INAPPROPRIATE_CONTENT":
      return Messages.inappropriateContent;
    case "RATE_LIMIT_EXCEEDED":
      return Messages.rateLimitExceeded;
    default:
      return Messages.unknownError;
  }
};
```

## Backend response depends on user locale

Send locale as a query parameter:

```jsx
const params = new URLSearchParams({ query, locale });
const url = `${BACKEND_HOST}/videos/find?${params.toString()}`;
```
