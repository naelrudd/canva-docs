Source: https://www.canva.dev/docs/audit-logs/actions/investigations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Investigations

## Start an investigation

An `actor` triggers this event when they start an investigation.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `START_INVESTIGATION`

      **Available values:** The only valid value is `START_INVESTIGATION`.
    </Prop.Extras>
  </Prop>

  <Prop name="owners" type="AuditLogUser[]" required mode="output">
    The list of owners that are being audited in the investigation.

    <PillAccordion title={<>Properties of <strong>owners</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The user ID.
        </Prop>

        <Prop name="display_name" type="string" mode="output">
          The display name of the user.

          For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.
        </Prop>

        <Prop name="email" type="string" mode="output">
          The email address of the user.

          For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="investigation_reason" type="string" mode="output">
    <Prop.Extras>
      **Available values:**

      * `SECURITY_INVESTIGATION`: Security investigation.
      * `COMPLIANCE_INVESTIGATION`: Compliance investigation.
      * `OTHER`: Other.
    </Prop.Extras>
  </Prop>

  <Prop name="context" type="string" mode="output">
    The context provided as a rationale for starting the investigation.
  </Prop>
</Prop.List>

### Example

## Investigate a design

An `actor` triggers this event when they view a specific design during an investigation.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `INVESTIGATE_DESIGN`

      **Available values:** The only valid value is `INVESTIGATE_DESIGN`.
    </Prop.Extras>
  </Prop>

  <Prop name="investigation_id" type="string" mode="output">
    The ID for the investigation. This is a UUID that represents the investigation.
  </Prop>
</Prop.List>

### Example

