Source: https://www.canva.dev/docs/audit-logs/actions/organizations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Organizations

## Update an organization's details

An `actor` triggers this event when they update the details of a
[Canva organization](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/),
such as the organization's display name.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_ORGANIZATION`

      **Available values:** The only valid value is `UPDATE_ORGANIZATION`.
    </Prop.Extras>
  </Prop>

  <Prop name="changed_fields" type="string[]" mode="output">
    Fields requested to be changed in this update.

    <Prop.Extras>
      **Available values:**

      * `ORGANIZATION_NAME`: The name of the organization.
      * `DEFAULT_TEAM`: The team to provision users into by default.
      * `DEFAULT_TEAM_POLICY`: The policy for determining if a user can be provisioned into a default team.
    </Prop.Extras>
  </Prop>

  <Prop name="old_name" type="string" mode="output">
    The previous name of the organization.
  </Prop>

  <Prop name="new_name" type="string" mode="output">
    The new name of the organization.
  </Prop>

  <Prop name="default_team" type="AuditLogTeam" mode="output">
    A Canva team.

    <PillAccordion title={<>Properties of <strong>default_team</strong></>} defaultExpanded={true}>
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

  <Prop name="default_team_policy" type="string" mode="output">
    The policy for determining if a user can be provisioned into a default team.

    <Prop.Extras>
      **Available values:**

      * `ADMIN_AND_UP`: Users with the `ADMIN` organization role or higher are added to the team.
      * `DESIGNER_AND_UP`: Users with the `DESIGNER` organization role or higher are added to the team.
      * `MEMBER_AND_UP`: Users with the `MEMBER` organization role or higher are added to the team.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Update a user in an organization

An `actor` triggers this event when they update a Canva user's membership within a
[Canva organization](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).
This includes promoting a `MEMBER` to `BRAND_DESIGNER` or `ADMIN`, changing roles between
`BRAND_DESIGNER` and `ADMIN`, or removing a user's `ADMIN` or `BRAND_DESIGNER` role.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_USER_IN_ORGANIZATION`

      **Available values:** The only valid value is `UPDATE_USER_IN_ORGANIZATION`.
    </Prop.Extras>
  </Prop>

  <Prop name="user" type="AuditLogUser" required mode="output">
    A Canva user.

    <PillAccordion title={<>Properties of <strong>user</strong></>} defaultExpanded={true}>
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

  <Prop name="old_role" type="string" mode="output">
    The user's role in the organization.

    <Prop.Extras>
      **Available values:**

      * `ADMIN`: Organization admin.
      * `BRAND_DESIGNER`: Organization brand designer.
      * `MEMBER`: Organization member.
    </Prop.Extras>
  </Prop>

  <Prop name="new_role" type="string" mode="output">
    The user's role in the organization.

    <Prop.Extras>
      **Available values:**

      * `ADMIN`: Organization admin.
      * `BRAND_DESIGNER`: Organization brand designer.
      * `MEMBER`: Organization member.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Add a team to the organization

An `actor` triggers this event when they add a Canva Team to their
[Canva organization](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `ADD_TEAM_TO_ORGANIZATION`

      **Available values:** The only valid value is `ADD_TEAM_TO_ORGANIZATION`.
    </Prop.Extras>
  </Prop>

  <Prop name="team" type="AuditLogTeam" required mode="output">
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

## Remove a team from the organization

An `actor` triggers this event when they remove a Canva Team from their
[Canva organization](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `REMOVE_TEAM_FROM_ORGANIZATION`

      **Available values:** The only valid value is `REMOVE_TEAM_FROM_ORGANIZATION`.
    </Prop.Extras>
  </Prop>

  <Prop name="team" type="AuditLogTeam" required mode="output">
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

