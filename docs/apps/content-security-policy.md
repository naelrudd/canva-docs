Source: https://www.canva.dev/docs/apps/content-security-policy/

# Content Security Policy

What is a Content Security Policy? How does it affect app development?

## What is (and isn't) allowed

Apps can:
* Load audio, fonts, images, and videos from data URLs and HTTPS URLs.
* Use inline CSS.

Apps can't:
* Use frames, web workers, or other nested browsing contexts.
* Load JavaScript from third-party sources.
* Load CSS stylesheets.
* Use the `base` element.
* Use the `form` element's `action` attribute.

## What directives does Canva use?

```
base-uri 'none';
child-src 'none';
connect-src https: data: wss: https://o13855.ingest.sentry.io https://telemetry.canva.com/v1/traces;
default-src 'none';
font-src  data: https: https://static.canva.com;
form-action 'none';
frame-ancestors https://*.canva.com http://localhost:*;
frame-src 'none';
img-src data: https: blob: https://static.canva.com;
media-src  data: https: blob: https://static.canva.com;
object-src 'none';
script-src 'wasm-unsafe-eval' ...;
style-src 'unsafe-inline' https://static.canva.com;
worker-src 'none';
```

## How to troubleshoot violations

When an app violates the CSP, an error is logged to the JavaScript Console.
