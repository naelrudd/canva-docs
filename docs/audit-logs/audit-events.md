Source: https://www.canva.dev/docs/audit-logs/audit-events/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Audit events

Audit events are exported as JSON and specify an `actor` that performed an `action` on a `target` at time `timestamp` with a specific `outcome` under a `context`.

The `actor` is the user who initiated the `action`. The `action` describes the activity. The `target` is the user, team, organization, or resource that the `action` targeted. The `outcome` includes the result of the `action`. The `context` contains additional information related to the event.

## AuditEvent schema

* `id` (string): The ID of the audit event.
* `timestamp` (integer): The time the event occurred, as a Unix timestamp (milliseconds since epoch).
* `actor` (Actor): The person who performed the action.
  * Types: `USER` (includes user, team, organization details), `CANVA_CUSTOMER_SUPPORT`, `ANONYMOUS`, `SYSTEM` (includes SCIM or CRM details).
* `target` (Target): The target resource of an action.
  * Types: `USER`, `TEAM`, `ORGANIZATION`, `RESOURCE` (includes resource_type, id, owner, name).
  * Resource types: `BRAND_KIT`, `DESIGN`, `FILE`, `FOLDER`, `GROUP`, `MEDIA`, `ADMIN_API_CLIENT`, `TEMPLATE`, `VIDEO`, `AUDIO`, `WEBSITE_DOMAIN`, `WEBSITE_SSO_CONNECTION`, `PROVISIONING_POLICY`, `3D`.
* `action` (Action): See individual action pages.
* `outcome` (Outcome): Result of the action.
  * Results: `UNKNOWN`, `PERMITTED`, `DENIED`, `RESOURCE_NOT_FOUND`, `FAILED`.
  * Details types: `RESOURCE_CREATED`, `USER_CREATED`, `INVESTIGATION_STARTED`.
* `context` (Context): Additional context.
  * `ip_address` (string), `session` (string), `request_id` (string), `device_id` (string), `integration_id` (string).
