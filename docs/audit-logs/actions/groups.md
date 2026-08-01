Source: https://www.canva.dev/docs/audit-logs/actions/groups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Groups

## Create a group

An `actor` triggers this event when they create a new
[Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).
For details on creating Canva groups, see
[Canva Help: Creating groups](https://www.canva.com/help/groups/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `CREATE_GROUP`

      **Available values:** The only valid value is `CREATE_GROUP`.
    </Prop.Extras>
  </Prop>

  <Prop name="display_name" type="string" required mode="output">
    The display name for the group.
  </Prop>

  <Prop name="description" type="string" mode="output">
    A description for the group.
  </Prop>
</Prop.List>

### Example

## Update a group's details

An `actor` triggers this event when they update the details of a
[Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/),
such as the group's display name.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_GROUP`

      **Available values:** The only valid value is `UPDATE_GROUP`.
    </Prop.Extras>
  </Prop>

  <Prop name="old_display_name" type="string" mode="output">
    The old display name of the group.
  </Prop>

  <Prop name="new_display_name" type="string" mode="output">
    The new display name for the group.
  </Prop>
</Prop.List>

### Example

## Delete a group

An `actor` triggers this event when they delete a
[Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `DELETE_GROUP`

      **Available values:** The only valid value is `DELETE_GROUP`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Add a user to a group

An `actor` triggers this event when they add a Canva user to a
[Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).
For details on adding users to a Canva group, see
[Canva Help: Creating groups — Adding people to a group](https://www.canva.com/help/groups/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `ADD_USER_TO_GROUP`

      **Available values:** The only valid value is `ADD_USER_TO_GROUP`.
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

  <Prop name="role" type="string" mode="output">
    The user's role within a group.

    <Prop.Extras>
      **Available values:**

      * `MEMBER`: Group member.
      * `ADMIN`: Group administrator.
    </Prop.Extras>
  </Prop>

  <Prop name="reason" type="GroupMembershipChangeReason" mode="output">
    The reason for the change.

    <Tabs>
      <Tab name="PROVISIONING_POLICY">
        This change was triggered by an provisioning policy.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `PROVISIONING_POLICY`

              **Available values:** The only valid value is `PROVISIONING_POLICY`.
            </Prop.Extras>
          </Prop>

          <Prop name="provisioning_policy" type="AuditLogProvisioningPolicy" mode="output">
            A Canva provisioning policy.

            <PillAccordion title={<>Properties of <strong>provisioning_policy</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The provisioning policy ID.
                </Prop>

                <Prop name="name" type="string" mode="output">
                  The provisioning policy name.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>
    </Tabs>
  </Prop>
</Prop.List>

### Example

## Update a user in a group

An `actor` triggers this event when they update a Canva user's membership within a
[Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/),
such as changing the user's role from `ADMIN` to `MEMBER`.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_USER_IN_GROUP`

      **Available values:** The only valid value is `UPDATE_USER_IN_GROUP`.
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

  <Prop name="new_role" type="string" mode="output">
    The user's role within a group.

    <Prop.Extras>
      **Available values:**

      * `MEMBER`: Group member.
      * `ADMIN`: Group administrator.
    </Prop.Extras>
  </Prop>

  <Prop name="old_role" type="string" mode="output">
    The user's role within a group.

    <Prop.Extras>
      **Available values:**

      * `MEMBER`: Group member.
      * `ADMIN`: Group administrator.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Remove a user from a group

An `actor` triggers this event when they remove a Canva user from a
[Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).
This includes users removing themselves from a group.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `REMOVE_USER_FROM_GROUP`

      **Available values:** The only valid value is `REMOVE_USER_FROM_GROUP`.
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

  <Prop name="role" type="string" mode="output">
    The user's role within a group.

    <Prop.Extras>
      **Available values:**

      * `MEMBER`: Group member.
      * `ADMIN`: Group administrator.
    </Prop.Extras>
  </Prop>

  <Prop name="reason" type="GroupMembershipChangeReason" mode="output">
    The reason for the change.

    <Tabs>
      <Tab name="PROVISIONING_POLICY">
        This change was triggered by an provisioning policy.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `PROVISIONING_POLICY`

              **Available values:** The only valid value is `PROVISIONING_POLICY`.
            </Prop.Extras>
          </Prop>

          <Prop name="provisioning_policy" type="AuditLogProvisioningPolicy" mode="output">
            A Canva provisioning policy.

            <PillAccordion title={<>Properties of <strong>provisioning_policy</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The provisioning policy ID.
                </Prop>

                <Prop name="name" type="string" mode="output">
                  The provisioning policy name.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>
    </Tabs>
  </Prop>
</Prop.List>

### Example

