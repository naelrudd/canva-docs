Source: https://www.canva.dev/docs/audit-logs/actions/audit-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Audit Logs

## Export audit logs

An `actor` triggers this event when they click the **Export** button on the **Audit logs** settings page, then click **Download**, as described in [Canva Help: About Canva audit logs](https://www.canva.com/help/view-audit-logs/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `EXPORT_AUDIT_LOGS`

      **Available values:** The only valid value is `EXPORT_AUDIT_LOGS`.
    </Prop.Extras>
  </Prop>

  <Prop name="start_timestamp" type="integer" mode="output">
    The start of the time period queried by the `actor`, as a Unix timestamp (in milliseconds since the Unix Epoch).
  </Prop>

  <Prop name="end_timestamp" type="integer" mode="output">
    The end of the time period queried by the `actor`, as a Unix timestamp (in milliseconds since the Unix Epoch).
  </Prop>

  <Prop name="team" type="AuditLogTeam" mode="output">
    A Canva team.

    <PillAccordion title={<>Properties of <strong>team</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The team ID.
        </Prop>

        <Prop name="display_name" type="string" mode="output">
          The display name of the team.

          For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

### Example

## View audit logs

An `actor` triggers this event when they view the audit logs, as described in [Canva Help: About Canva audit logs](https://www.canva.com/help/view-audit-logs/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `VIEW_AUDIT_LOGS`

      **Available values:** The only valid value is `VIEW_AUDIT_LOGS`.
    </Prop.Extras>
  </Prop>

  <Prop name="start_timestamp" type="integer" mode="output">
    The start of the time period viewed by the `actor`, as a Unix timestamp (in milliseconds since the Unix Epoch).
  </Prop>

  <Prop name="end_timestamp" type="integer" mode="output">
    The end of the time period viewed by the `actor`, as a Unix timestamp (in milliseconds since the Unix Epoch).
  </Prop>

  <Prop name="team" type="AuditLogTeam" mode="output">
    A Canva team.

    <PillAccordion title={<>Properties of <strong>team</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The team ID.
        </Prop>

        <Prop name="display_name" type="string" mode="output">
          The display name of the team.

          For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

### Example

## Update audit log settings

An `actor` triggers this event when they update the audit log settings. If the change
updated the S3 Bucket name, this event will appear in the new S3 bucket (the configured S3
Bucket after the change).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_AUDIT_LOGS_SETTINGS`

      **Available values:** The only valid value is `UPDATE_AUDIT_LOGS_SETTINGS`.
    </Prop.Extras>
  </Prop>

  <Prop name="changed_fields" type="string[]" mode="output">
    The configuration settings the `actor` requested changes for.

    <Prop.Extras>
      **Available values:**

      * `REGION`: The region of the AWS S3 bucket.
      * `S3_BUCKET_NAME`: The name of your Canva audit logs S3 bucket.
      * `S3_KEY_PREFIX`: An optional S3 key prefix.
      * `ROLE_ARN`: The Amazon Resource Name (ARN) of the AWS Role that Canva uses to access the S3 bucket.
    </Prop.Extras>
  </Prop>

  <Prop name="old_region" type="string" mode="output">
    The old region of the AWS S3 bucket.
  </Prop>

  <Prop name="new_region" type="string" mode="output">
    The new region of the AWS S3 bucket.
  </Prop>

  <Prop name="old_s3_bucket_name" type="string" mode="output">
    The old name of your Canva audit logs S3 bucket.
  </Prop>

  <Prop name="new_s3_bucket_name" type="string" mode="output">
    The new name of your Canva audit logs S3 bucket.
  </Prop>

  <Prop name="old_s3_key_prefix" type="string" mode="output">
    The old S3 key prefix.
  </Prop>

  <Prop name="new_s3_key_prefix" type="string" mode="output">
    The new S3 key prefix.
  </Prop>

  <Prop name="old_role_arn" type="string" mode="output">
    The old Amazon Resource Name (ARN) of the AWS Role that Canva uses to access the S3
    bucket.
  </Prop>

  <Prop name="new_role_arn" type="string" mode="output">
    The new Amazon Resource Name (ARN) of the AWS Role that Canva uses to access the S3
    bucket.
  </Prop>
</Prop.List>

### Example

