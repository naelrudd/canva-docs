Source: https://www.canva.dev/docs/connect/guidelines/shared-responsibility/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/connect/llms.txt
> Use this file to discover all available pages before exploring further.

# Shared responsibility model for the Connect APIs

Shared security responsibilities for Canva API integrations.

Shared responsibility models clarify security responsibility between a platform provider and developers building integrations that use that platform.

Building an integration that connects to Canva means that developers share the same users as Canva. As a result, developers must take some responsibility to protect Canva user data and privacy, which can differ from other Software as a Service (SaaS) product expectations. Canva, as a provider, takes some responsibility, but not all of the security responsibility.

Read through the following sections to understand what are your security responsibilities, and what are Canva's responsibilities.

We reserve the right to amend this page from time to time in our sole discretion.

<Note>
  Make sure that you read, and are complying with, the [Canva API and App Developer Terms](https://www.canva.com/policies/canva-developer-terms).

  Noncompliance may result in Canva:

  * Suspending your integration.
  * Disabling access to your integration in the Canva Apps Marketplace.
  * Discontinuing your access to Canva APIs.
</Note>

<Note>
  For specific security advice on recommended security practices or how to handle access management, see the [Connect APIs security recommendations](https://www.canva.dev/docs/connect/guidelines/security/), and the [Authentication guide](https://www.canva.dev/docs/connect/authentication/).
</Note>

## Integration concepts

**Integrations and data flow**
Integrations allow third-party app developers to extend key Canva capabilities off-platform. As a result, integrations allow Canva to share data with third parties. This data sharing happens even when a user isn't actively designing in Canva. The flow of data from Canva through to third parties is controlled by integration architecture. The essential component for this data flow is the Canva Connect APIs.

**Connect APIs**

The Connect APIs use resource-oriented URLs. They accept requests with parameters, and return JSON responses with standard HTTP response codes. For more information, see [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/).

**Integration architecture**
Some examples of integration architectures built with the Connect APIs can include, but aren't limited to:

* Keeping Canva in sync with cloud storage and content management apps.
* Enabling collaboration and communication with different platforms.
* Embedding Canva into project management workflows.

## Security responsibilities

### Vulnerability management & disclosure

| Your responsibilities | Canva's responsibilities |
|---|---|
| Conduct regular security reviews of infrastructure and source code using vulnerability scanning tools, vulnerability disclosure programs, or penetration testing by external parties. | Suspend integrations that haven't mitigated security vulnerabilities. |
| Mitigate or remediate integration security vulnerabilities within the timelines expected in the Developer Terms. | Communicate with developers about vulnerabilities in the platform or integrations. |
| Notify Canva of critical or high security vulnerabilities in your integration. | |

### Monitoring and alerting

| Your responsibilities | Canva's responsibilities |
|---|---|
| Implement adequate monitoring and alerting for backend functionality. | Ongoing monitoring of integration platform health, and raising alerts in response to degraded performance, security, or abuse events. |

### Logging

| Your responsibilities | Canva's responsibilities |
|---|---|
| Ensure your integration doesn't log sensitive security data, personally identifiable information, authentication tokens, and user-generated content. | Maintain robust logging that includes an audit trail of actions performed by an integration. |
| Implement adequate logging for backend functionality. | Restrict access to logs based on organization permissions. |

### Incident response

| Your responsibilities | Canva's responsibilities |
|---|---|
| Notify Canva of any incidents involving Canva integration data. | Maintain a detailed plan of action for responding to security incidents. |
| Develop a detailed plan of action for responding to security incidents. | Regularly test the incident response plan. |
| Regularly test your incident response plan. | |

### Network security

| Your responsibilities | Canva's responsibilities |
|---|---|
| Use secure protocols and configurations to encrypt traffic. | Ensure that contemporary, secure protocols are supported. |
| Handle data according to your data classification policy. | |

### Infrastructure security

| Your responsibilities | Canva's responsibilities |
|---|---|
| Harden any associated services in the integration backend. | Ensure the platform infrastructure is hardened. |
| Scan for security misconfigurations and vulnerabilities. | Scan for security misconfigurations and vulnerabilities. |
| Provide a secure runtime for integrations. | |

### Disaster recovery

| Your responsibilities | Canva's responsibilities |
|---|---|
| | Establish a business continuity and disaster recovery plan. |
| | Ensure that data stored by Canva is backed up. |
| | Maintain business continuity and disaster recovery plans. |

## Trust and safety

### User identity and access management

| Your responsibilities | Canva's responsibilities |
|---|---|
| Use mechanisms to verify user and team access. | Provide APIs for authentication. |

### Denial of service prevention

| Your responsibilities | Canva's responsibilities |
|---|---|
| Detect denial of service attacks against integration backends. | Detect denial of service attacks. |
| Mitigate denial of service attacks against integration backends. | Mitigate denial of service attacks. |
| | Suspend integrations that may be misbehaving. |

### Abuse prevention

| Your responsibilities | Canva's responsibilities |
|---|---|
| Ensure your integration complies with the Developer Terms. | Detect and mitigate integrations that disrupt normal operations. |
| Ensure your integration does not exceed API quotas and limits. | Enforce platform limits. |

## Integration

### Authentication of requests to the integration

| Your responsibilities | Canva's responsibilities |
|---|---|
| Ensure secure storage and handling of client credentials. | Provide support for secure and recommended client authentication methods. |
| Securely handle access tokens, refresh tokens, and ID tokens. | |

### Authorization of requests

| Your responsibilities | Canva's responsibilities |
|---|---|
| Verify the authenticity of incoming webhook messages. | Ensure that users with access to Canva can use your integration. |
| Verify that organizations, teams, and users are authorized to access content. | For private integrations, ensure only authorized users can access it. |

### Input validation and output encoding

| Your responsibilities | Canva's responsibilities |
|---|---|
| Implement input validation in your integration. | Ensure all data received from your integration undergoes stringent validation. |
| Apply appropriate encoding mechanisms. | |
| Carefully inspect and validate authorization responses. | |

### Business logic

| Your responsibilities | Canva's responsibilities |
|---|---|
| Ensure correct OAuth implementation with PKCE. | |
| Properly validate redirect URLs. | |
| Implement secure error handling. | |
| Request only necessary scopes. | |
| Securely manage the state parameter. | |

### Integration framework

| Your responsibilities | Canva's responsibilities |
|---|---|
| Choose robust and well-maintained frameworks and libraries. | Offer detailed documentation, SDKs, and libraries. |
| Configure the integration framework securely. | Ensure backward compatibility for API changes. |
| Conduct thorough testing of OAuth flow. | Communicate known security considerations. |

### Tenant security

| Your responsibilities | Canva's responsibilities |
|---|---|
| Implement authentication that identifies users based on tenant context. | Provide robust support for multi-tenancy. |
| Ensure application logic and data storage segregate data per tenant. | Issue access tokens scoped to the appropriate team. |
| Safely configure tenant-specific settings. | Offer access controls for tailored configurations. |

### Data storage

| Your responsibilities | Canva's responsibilities |
|---|---|
| Limit data collection to what is required. | Maintain web storage separation and cleanup between user sessions. |
| Ensure API keys and secrets are not hard-coded in source code. | |
| Have processes for revocation and rotation of sensitive data. | |
| Handle personal information in accordance with the Developer Terms and applicable legislation. | |

### Secure development activities

| Your responsibilities | Canva's responsibilities |
|---|---|
| Adopt secure development activities. | |
| Perform regular threat modeling on integrations. | |
