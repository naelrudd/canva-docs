Source: https://www.canva.dev/docs/apps/security-guidelines/

# Security guidelines

How to keep your app (and its users) secure.

## Use reasonable security measures

Ensure your app is not vulnerable to the [OWASP Top 10](https://owasp.org/www-project-top-ten/).

## Respect Canva's Content Security Policy

See [Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/).

## Configure Cross-Origin Resource Sharing

Set the most restrictive policy possible. See [CORS](https://www.canva.dev/docs/apps/cross-origin-resource-sharing/).

## Verify HTTP requests

For Node.js backends, use the [`@canva/app-middleware`](https://www.npmjs.com/package/@canva/app-middleware) package.

## Store secrets securely

* Always verify JWTs.
* Use tokens with least privilege.
* Use JavaScript closures instead of WebStorage APIs for sensitive values.
* Keep secrets masked.
* Use rate-limiting.
* Transmit tokens securely using POST requests.
* Always associate access tokens with user AND team IDs.
* Delete tokens when no longer needed.
* Use TLS to encrypt traffic.

## Maintain ownership of subdomains

Regularly verify DNS configurations and ensure subdomains can't be taken over.

## Don't require users to download files

Never ask users to download external files, especially executables.
