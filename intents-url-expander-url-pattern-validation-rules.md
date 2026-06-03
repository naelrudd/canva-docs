Source: https://www.canva.dev/docs/apps/intents/url-expander/url-pattern-validation-rules/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# URL Expander URL pattern validation rules

Rules for defining URL patterns that your app can expand.

When registering URL patterns for the [URL Expander intent](https://www.canva.dev/docs/apps/intents/url-expander/), your patterns must follow specific validation rules to ensure they're secure and functional.

**Warning:** The URL Expander intent is provided as a preview. Validation rules may change before general availability.

URL patterns define which URLs your app can recognize and expand. These patterns use wildcards to match multiple URLs from your platform while maintaining security and specificity.

**Note:** In the Developer Portal, URL patterns are configured in the "Supported URLs" field. This documentation refers to them as "URL patterns" to align with the API terminology.

## Validation rules

URLs used with the URL Expander intent must follow these rules:

* Use the `https://` protocol.
* Include a valid domain.
* The TLD must not contain a wildcard.
* Contain no more than 3 wildcards.
* Not include query parameters or fragments.

### Valid examples

```
https://example.com/*
https://*.example.com/*
https://example.co.uk/*
```

### Invalid examples

```
http://example.com/*  (Must use HTTPS)
https://example.*  (Wildcard in TLD)
https://example/* (Invalid domain)
```

**Note:** URLs without a trailing wildcard (for example, `https://example.com`) aren't recommended unless you intend to match an exact URL.

## Protocol

URLs must use the HTTPS protocol.

### Valid

```
https://example.com/*
```

### Invalid

```
example.com/*
http://example.com/*
```

All URLs must explicitly use the `https://` protocol. HTTP URLs and protocol-relative URLs aren't supported for security reasons.

## Domain

The domain must be a valid domain name that follows DNS naming conventions.

### Invalid

```
https://example/*
https://example.comm/*
https://com/*
https://co.uk/*
```

The domain must include:

* A valid top-level domain (TLD) such as `.com`, `.org`, `.co.uk`.
* A valid second-level domain (the part before the TLD).
* Proper formatting with no typos or malformed parts.

## Wildcards

You can use up to 3 wildcards (`*`) per URL pattern. Wildcards match any string of characters in that position.

### Wildcard placement

Wildcards are allowed in:

* **Subdomains**: Match different subdomains (for example, `https://*.example.com/*`).
* **Path segments**: Match different paths (for example, `https://example.com/*/docs/*`).

Wildcards aren't allowed in:

* **Top-level domains (TLD)**: The TLD must be explicit (for example, `https://example.*` is invalid).
* **Registrable domain (eTLD+1)**: The core domain must be explicit (for example, `https://*.com` is invalid).

### Valid wildcard examples

```
https://*.example.com/*
https://example.com/*/docs/*
https://subdomain.example.com/*/*
```

### Invalid wildcard examples

```
https://example.*/*  (Wildcard in TLD)
https://*.*.*.*.example.com/*  (Exceeds 3 wildcards)
https://*.com  (Wildcard at registrable domain level)
```

### Wildcard limits

Each URL pattern can contain a maximum of 3 wildcards. This limit ensures that patterns remain specific enough to identify URLs from your platform.

**Valid (3 wildcards):**

```
https://*.example.com/*/*
```

**Invalid (4 wildcards):**

```
https://*.*.example.com/*/*
```

## Query parameters and fragments

URL patterns can't include query parameters (`?`) or fragments (`#`). Patterns should match the base URL structure only.

### Invalid

```
https://example.com?param=value
https://example.com#section
https://example.com/path?query=string
https://example.com/path#fragment
```

### Valid

```
https://example.com/*
https://example.com/path/*
```

When a user pastes a URL with query parameters or fragments, your app's `expandUrl` method receives the full URL including those parts. However, the pattern you register should only match the base URL structure.

**Example:**

* **Registered pattern:** `https://docs.example.com/document/*`
* **User pastes:** `https://docs.example.com/document/abc123?view=edit#page2`
* **Pattern matches:** Yes (query parameters and fragments are ignored for pattern matching)
* **Your app receives:** The full URL including `?view=edit#page2`

## Pattern specificity

### Exact URLs

You can register exact URLs without wildcards if you want to match only specific URLs:

```
https://example.com/specific-page
```

However, this is rarely useful since most apps need to match multiple URLs. Exact URLs are only recommended for testing or very specific use cases.

### Subdomain wildcards

Use subdomain wildcards to match all subdomains of your platform:

```
https://*.example.com/*
```

This matches:

* `https://docs.example.com/page`
* `https://app.example.com/resource`
* `https://cdn.example.com/asset`

### Path wildcards

Use path wildcards to match different resources within your platform:

```
https://example.com/docs/*/view
```

This matches:

* `https://example.com/docs/page1/view`
* `https://example.com/docs/page2/view`
* `https://example.com/docs/section/subsection/view`

Note that a single wildcard matches one or more path segments.

## Best practices

### Be specific

Use patterns that are specific to your platform to avoid conflicts with other apps:

**Good:**

```
https://docs.myplatform.com/document/*
https://myplatform.com/resources/*
```

**Avoid:**

```
https://*.com/*  (Too broad)
https://*/*  (Too broad)
```

### Use multiple patterns

If your platform has different URL structures for different content types, register multiple patterns:

```typescript
const urlPatterns = [
  "https://docs.myplatform.com/document/*",
  "https://docs.myplatform.com/presentation/*",
  "https://myplatform.com/media/*",
];
```

### Consider future URLs

Design patterns that can accommodate future URL structures on your platform. Use wildcards strategically to allow for growth while maintaining specificity.

### Test your patterns

Before deploying, test your patterns with various URLs from your platform to ensure they match correctly:

* URLs with different path lengths.
* URLs with different subdomains (if applicable).
* URLs with query parameters and fragments.
* Edge cases specific to your platform.

## Examples by platform type

### Document platform

```typescript
const urlPatterns = [
  "https://docs.platform.com/doc/*",
  "https://docs.platform.com/sheet/*",
  "https://docs.platform.com/presentation/*",
];
```

### Media platform

```typescript
const urlPatterns = [
  "https://platform.com/image/*",
  "https://platform.com/video/*",
  "https://cdn.platform.com/assets/*",
];
```

### Multi-region platform

```typescript
const urlPatterns = [
  "https://*.platform.com/content/*",  // Matches any regional subdomain
];
```

### Versioned API URLs

```typescript
const urlPatterns = [
  "https://api.platform.com/*/resources/*",  // Matches any version
];
```

## Related resources

* [URL Expander intent overview](https://www.canva.dev/docs/apps/intents/url-expander/)
* [URL Expander implementation guide](https://www.canva.dev/docs/apps/intents/url-expander/implementation-guide/)
