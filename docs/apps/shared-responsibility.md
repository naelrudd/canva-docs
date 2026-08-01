Source: https://www.canva.dev/docs/apps/shared-responsibility/

# Shared responsibility model for Canva Apps

Shared security responsibilities for developing Canva Apps.

## Security operations

| Area | Your responsibilities | Canva's responsibilities |
|------|----------------------|--------------------------|
| Vulnerability management | Regular security reviews, mitigate vulnerabilities | Suspend apps with unmitigated vulnerabilities |
| Monitoring and alerting | Monitor backend functionality | Monitor App SDK platform health |
| Logging | Don't log sensitive data | Maintain robust logging |
| Incident response | Develop and test incident response plan | Maintain incident response plan |
| Network security | Use secure protocols | Support modern, secure protocols |
| Infrastructure security | Harden app backend | Harden platform infrastructure |
| Disaster recovery | Establish business continuity plan | Back up data, maintain DR plans |
| Subdomain ownership | Maintain ownership of subdomains | Monitor for takeover indicators |

## Trust and safety

| Area | Your responsibilities | Canva's responsibilities |
|------|----------------------|--------------------------|
| User identity | Verify user/team access | Authenticate user and team |
| DoS prevention | Detect/mitigate DoS against backends | Detect/mitigate DoS through frontends |
| Abuse prevention | Comply with developer terms | Enforce platform limits |

## App

| Area | Your responsibilities | Canva's responsibilities |
|------|----------------------|--------------------------|
| Authenticating requests | Authenticate users before serving content | Provide secure authentication mechanism |
| Authorizing requests from app | Verify HTTP request authenticity | Obtain user consent |
| App framework | Keep third-party libraries up-to-date | Apply secure development practices |
| Input validation | Treat all input as unsafe | Encode HTML output for UI Components |
| Business logic | Identify/remediate business logic flaws | - |
| Tenant security | - | Ensure isolation between apps |
| Data storage | Minimize data collection, don't hard-code secrets | Maintain web storage separation |
