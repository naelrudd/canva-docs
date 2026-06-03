Source: https://www.canva.dev/docs/audit-logs/actions/teams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Teams

## Update a team's details

An `actor` triggers this event when they update the details of a
[Canva Team](https://www.canva.com/help/manage-teams/), such as the team's display name.

We only log the team properties that the actor requested changes for.
The changed fields are listed in the `changed_fields` array.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_TEAM`

      **Available values:** The only valid value is `UPDATE_TEAM`.
    </Prop.Extras>
  </Prop>

  <Prop name="changed_fields" type="string[]" mode="output">
    Fields requested to be changed in this update.

    <Prop.Extras>
      **Available values:**

      * `TEAM_NAME`: The team name.
      * `DISPLAY_NAME`: The team's display name as shown in the Canva UI.
      * `THIRD_PARTY`: Whether this team represents a third party integration.
      * `BILLING_INFO`: Billing information for the team.
      * `WEBSITE_URL`: The website URL for the team.
      * `ADDRESS`: The team's address.
      * `EXTERNAL_LINKS`: Links to teams or other entities within external identity providers.
      * `BRAND_COLORS_ONLY`: Whether the team is restricted to brand colors.
      * `BRAND_FONTS_ONLY`: Whether the team is restricted to brand fonts.
    </Prop.Extras>
  </Prop>

  <Prop name="team_name" type="string" mode="output">
    The team name.
  </Prop>

  <Prop name="display_name" type="string" mode="output">
    The team's display name. This is used to represent the team with text in a UI.
  </Prop>

  <Prop name="third_party_integrated" type="boolean" mode="output">
    Whether this team represents a third-party integrated application.
  </Prop>

  <Prop name="billing_info" type="object" mode="output">
    Billing information for the team.

    <PillAccordion title={<>Properties of <strong>billing_info</strong></>} defaultExpanded={true}>
      <Prop.List />
    </PillAccordion>
  </Prop>

  <Prop name="team_address" type="object" mode="output">
    Address for the team.

    <PillAccordion title={<>Properties of <strong>team_address</strong></>} defaultExpanded={true}>
      <Prop.List />
    </PillAccordion>
  </Prop>

  <Prop name="external_links" type="TeamExternalLink[]" mode="output">
    Represents a link to teams or other entities within external identity providers.

    <PillAccordion title={<>Properties of <strong>external_links</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="source" type="string" mode="output">
          The source of the external link.

          <Prop.Extras>
            **Available values:**

            * `ONE_ROSTER`: A OneRoster system.
            * `MANUAL`: Manual imports, such as Canva customer support performing the import.
          </Prop.Extras>
        </Prop>

        <Prop name="managing_team" type="object" mode="output">
          Represents the managing team with the associated external configuration.
          When `source` is `MANUAL`, users managed by the managing team are
          provisioned into this team as a fallback.

          <PillAccordion title={<>Properties of <strong>managing_team</strong></>}>
            <Prop.List>
              <Prop name="id" type="string" required mode="output">
                The managing team ID.
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="external_id" type="string" mode="output">
          Included when `source` is not `MANUAL`.
          Otherwise, this is the SSO identity provider or OneRoster external ID associated with the team.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="website_url" type="string" mode="output">
    The website URL for the team.
  </Prop>

  <Prop name="brand_fonts_only" type="boolean" mode="output">
    Whether the team is restricted to brand fonts.
  </Prop>

  <Prop name="brand_colors_only" type="boolean" mode="output">
    Whether the team is restricted to brand colors.
  </Prop>
</Prop.List>

### Example

## Delete a team

An `actor` triggers this event when they delete a
[Canva Team](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).
For details on deleting a Canva team, see
[Canva Help: Managing and deleting teams — Deleting a team](https://www.canva.com/help/manage-teams/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `DELETE_TEAM`

      **Available values:** The only valid value is `DELETE_TEAM`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Cancel the deletion of a team

An `actor` triggers this event when they cancel or undo the deletion of a
[Canva Team](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).
For details on deleting a Canva team, see
[Canva Help: Managing and deleting teams —
Canceling or undoing team deletion](https://www.canva.com/help/manage-teams/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UNDELETE_TEAM`

      **Available values:** The only valid value is `UNDELETE_TEAM`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Add a user to a team

An `actor` triggers this event when they add a Canva user to a
[Canva team](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).
For details on adding users to a Canva team, see
[Canva Help: Adding or removing people in a team or class —
Inviting users to join your team](https://www.canva.com/help/manage-members/).

The `reason` field contains the reason the user was added to the team. For example, they
accepted a team invitation or they were provisioned by a SCIM provider.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `ADD_USER_TO_TEAM`

      **Available values:** The only valid value is `ADD_USER_TO_TEAM`.
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
    The user's role within a team.

    <Prop.Extras>
      **Available values:**

      * `MEMBER`: Team member.
      * `DESIGNER`: Team designer.
      * `ADMIN`: Team administrator.
      * `OWNER`: Team owner.
    </Prop.Extras>
  </Prop>

  <Prop name="reason" type="TeamMembershipChangeReason" mode="output">
    The reason for the change.

    <Tabs>
      <Tab name="INVITATION_ACCEPTED">
        An invitation to join team was accepted

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `INVITATION_ACCEPTED`

              **Available values:** The only valid value is `INVITATION_ACCEPTED`.
            </Prop.Extras>
          </Prop>

          <Prop name="inviter" type="AuditLogUser" mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>inviter</strong></>}>
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
        </Prop.List>
      </Tab>

      <Tab name="JOIN_POLICY_ALLOWED">
        The change was permitted by your [Team discovery and settings](https://www.canva.com/help/team-discovery/).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `JOIN_POLICY_ALLOWED`

              **Available values:** The only valid value is `JOIN_POLICY_ALLOWED`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REQUEST_TO_JOIN_APPROVED">
        A user request to join your team was approved.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REQUEST_TO_JOIN_APPROVED`

              **Available values:** The only valid value is `REQUEST_TO_JOIN_APPROVED`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="SCIM">
        The change was made through your team's configured [SCIM Identity Provider](https://www.canva.com/help/scim-provisioning-and-deprovisioning/).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `SCIM`

              **Available values:** The only valid value is `SCIM`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="SAML_JIT_PROVISIONING">
        SAML Just-In-Time provisioning. This event can be triggered by events like a user
        [linking their Canva account with your SSO provider](https://www.canva.com/help/sso-linking/)
        or when you [set up Single Sign-On (SSO)](https://www.canva.com/help/set-up-sso/) for your
        team.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `SAML_JIT_PROVISIONING`

              **Available values:** The only valid value is `SAML_JIT_PROVISIONING`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

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

## Update a user in a team

An `actor` triggers this event when they update a Canva user's membership within a
[Canva team](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/),
such as changing the user's role from `ADMIN` to `MEMBER`.
For details on the different team roles, see
[Canva Help: Team roles and permissions](https://www.canva.com/help/roles-and-permissions/).

The `reason` field contains the reason the user was updated in the team. For example, their
details were updated by a SCIM provider.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_USER_IN_TEAM`

      **Available values:** The only valid value is `UPDATE_USER_IN_TEAM`.
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
    The user's role within a team.

    <Prop.Extras>
      **Available values:**

      * `MEMBER`: Team member.
      * `DESIGNER`: Team designer.
      * `ADMIN`: Team administrator.
      * `OWNER`: Team owner.
    </Prop.Extras>
  </Prop>

  <Prop name="old_role" type="string" mode="output">
    The user's role within a team.

    <Prop.Extras>
      **Available values:**

      * `MEMBER`: Team member.
      * `DESIGNER`: Team designer.
      * `ADMIN`: Team administrator.
      * `OWNER`: Team owner.
    </Prop.Extras>
  </Prop>

  <Prop name="reason" type="TeamMembershipChangeReason" mode="output">
    The reason for the change.

    <Tabs>
      <Tab name="INVITATION_ACCEPTED">
        An invitation to join team was accepted

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `INVITATION_ACCEPTED`

              **Available values:** The only valid value is `INVITATION_ACCEPTED`.
            </Prop.Extras>
          </Prop>

          <Prop name="inviter" type="AuditLogUser" mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>inviter</strong></>}>
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
        </Prop.List>
      </Tab>

      <Tab name="JOIN_POLICY_ALLOWED">
        The change was permitted by your [Team discovery and settings](https://www.canva.com/help/team-discovery/).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `JOIN_POLICY_ALLOWED`

              **Available values:** The only valid value is `JOIN_POLICY_ALLOWED`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REQUEST_TO_JOIN_APPROVED">
        A user request to join your team was approved.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REQUEST_TO_JOIN_APPROVED`

              **Available values:** The only valid value is `REQUEST_TO_JOIN_APPROVED`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="SCIM">
        The change was made through your team's configured [SCIM Identity Provider](https://www.canva.com/help/scim-provisioning-and-deprovisioning/).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `SCIM`

              **Available values:** The only valid value is `SCIM`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="SAML_JIT_PROVISIONING">
        SAML Just-In-Time provisioning. This event can be triggered by events like a user
        [linking their Canva account with your SSO provider](https://www.canva.com/help/sso-linking/)
        or when you [set up Single Sign-On (SSO)](https://www.canva.com/help/set-up-sso/) for your
        team.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `SAML_JIT_PROVISIONING`

              **Available values:** The only valid value is `SAML_JIT_PROVISIONING`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

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

## Remove a user from a team

An `actor` triggers this event when they remove a Canva user from a
[Canva team](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).
This includes users [removing themselves from a team](https://www.canva.com/help/leave-teams/).

The `reason` field contains the reason the user was removed from the team. For example, they
were removed by a SCIM provider.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `REMOVE_USER_FROM_TEAM`

      **Available values:** The only valid value is `REMOVE_USER_FROM_TEAM`.
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
    The user's role within a team.

    <Prop.Extras>
      **Available values:**

      * `MEMBER`: Team member.
      * `DESIGNER`: Team designer.
      * `ADMIN`: Team administrator.
      * `OWNER`: Team owner.
    </Prop.Extras>
  </Prop>

  <Prop name="reason" type="TeamMembershipChangeReason" mode="output">
    The reason for the change.

    <Tabs>
      <Tab name="INVITATION_ACCEPTED">
        An invitation to join team was accepted

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `INVITATION_ACCEPTED`

              **Available values:** The only valid value is `INVITATION_ACCEPTED`.
            </Prop.Extras>
          </Prop>

          <Prop name="inviter" type="AuditLogUser" mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>inviter</strong></>}>
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
        </Prop.List>
      </Tab>

      <Tab name="JOIN_POLICY_ALLOWED">
        The change was permitted by your [Team discovery and settings](https://www.canva.com/help/team-discovery/).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `JOIN_POLICY_ALLOWED`

              **Available values:** The only valid value is `JOIN_POLICY_ALLOWED`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REQUEST_TO_JOIN_APPROVED">
        A user request to join your team was approved.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REQUEST_TO_JOIN_APPROVED`

              **Available values:** The only valid value is `REQUEST_TO_JOIN_APPROVED`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="SCIM">
        The change was made through your team's configured [SCIM Identity Provider](https://www.canva.com/help/scim-provisioning-and-deprovisioning/).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `SCIM`

              **Available values:** The only valid value is `SCIM`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="SAML_JIT_PROVISIONING">
        SAML Just-In-Time provisioning. This event can be triggered by events like a user
        [linking their Canva account with your SSO provider](https://www.canva.com/help/sso-linking/)
        or when you [set up Single Sign-On (SSO)](https://www.canva.com/help/set-up-sso/) for your
        team.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `SAML_JIT_PROVISIONING`

              **Available values:** The only valid value is `SAML_JIT_PROVISIONING`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

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

## Request to join a team

An `actor` triggers this event when they request to join a team and the team's settings require an administrator to
approve before they can join. For information on users joining teams, see [Canva Help: Joining teams](https://www.canva.com/help/join-teams/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `CREATE_TEAM_JOIN_REQUEST`

      **Available values:** The only valid value is `CREATE_TEAM_JOIN_REQUEST`.
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
</Prop.List>

### Example

## Update a user's request to join a team

An `actor` triggers this event when they update a user's request to join a team. For example, an administrator
approved another user's request to join a team.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_TEAM_JOIN_REQUEST`

      **Available values:** The only valid value is `UPDATE_TEAM_JOIN_REQUEST`.
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

  <Prop name="approval_status" type="string" required mode="output">
    The status of a request or invite to join a team.

    <Prop.Extras>
      **Available values:**

      * `PENDING`: The request is pending.
      * `APPROVED`: An administrator approved the request.
      * `REJECTED`: An administrator rejected the request.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Request to invite a user into a team

A non-administrator `actor` triggers this event when they create a request to invite user to join a team.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `CREATE_TEAM_INVITATION_REQUEST`

      **Available values:** The only valid value is `CREATE_TEAM_INVITATION_REQUEST`.
    </Prop.Extras>
  </Prop>

  <Prop name="emails" type="string[]" required mode="output">
    A list of emails invited to join the team. These emails might not be linked to
    existing Canva accounts.
  </Prop>
</Prop.List>

### Example

## Update a request to invite a user into a team

An `actor` triggers this event when they update a non-administrator's request to invite a user to join a team. For
example, an administrator approved a user's request to invite another user to join a team.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_TEAM_INVITATION_REQUEST`

      **Available values:** The only valid value is `UPDATE_TEAM_INVITATION_REQUEST`.
    </Prop.Extras>
  </Prop>

  <Prop name="email" type="string" required mode="output">
    The email invited to join the team.
  </Prop>

  <Prop name="approval_status" type="string" required mode="output">
    The status of a request or invite to join a team.

    <Prop.Extras>
      **Available values:**

      * `PENDING`: The request is pending.
      * `APPROVED`: An administrator approved the request.
      * `REJECTED`: An administrator rejected the request.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Export a team report

An `actor` triggers this event when they export a team report.
For details on these reports, see
[Canva Help: Checking team analytics and reports](https://www.canva.com/help/team-reports/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `EXPORT_TEAM_REPORT`

      **Available values:** The only valid value is `EXPORT_TEAM_REPORT`.
    </Prop.Extras>
  </Prop>

  <Prop name="report_type" type="string" mode="output">
    The type of team activity report.

    <Prop.Extras>
      **Available values:**

      * `TEAM_MEMBER_ACTIVITY`: Team member activity. This includes the team member role, when they were last active, and the number of designs that they have created, published, shared, and viewed.
      * `BRAND_TEMPLATE_ACTIVITY`: Brand template activity. This includes the number of times a brand template was used, published, or shared.
      * `BRAND_KIT_ACTIVITY`: Brand Kit activity. This includes the number of times a Brand Kit was applied.
      * `BRAND_KIT_DESIGN_ACTIVITY`: Brand Kit design activity. This includes either the designs using a specific Brand Kit, or designs not using any Brand Kits.
    </Prop.Extras>
  </Prop>

  <Prop name="start_timestamp" type="integer" mode="output">
    The start of the report's time window, as a Unix timestamp (in milliseconds since the Unix Epoch).
  </Prop>

  <Prop name="end_timestamp" type="integer" mode="output">
    The end of the report's time window, as a Unix timestamp (in milliseconds since the Unix Epoch).
  </Prop>
</Prop.List>

### Example

## Export a design approval activity report

An `actor` triggers this event when they export a design approval activity report from the design approvals page.
The report contains the team's design approval activity for up to the past 12 months.
For details on design approvals, see
[Canva Help: Setting up design approval](https://www.canva.com/help/setting-up-design-approval/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `EXPORT_DESIGN_APPROVAL_ACTIVITY_REPORT`

      **Available values:** The only valid value is `EXPORT_DESIGN_APPROVAL_ACTIVITY_REPORT`.
    </Prop.Extras>
  </Prop>

  <Prop name="start_timestamp" type="integer" mode="output">
    The start of the report's time window, as a Unix timestamp (in milliseconds since the Unix Epoch).
  </Prop>
</Prop.List>

### Example

