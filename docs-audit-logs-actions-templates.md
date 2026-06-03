Source: https://www.canva.dev/docs/audit-logs/actions/templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Templates

## Publish a template

An `actor` triggers this event when they publish a template

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `PUBLISH_TEMPLATE`

      **Available values:** The only valid value is `PUBLISH_TEMPLATE`.
    </Prop.Extras>
  </Prop>

  <Prop name="template_type" type="string" mode="output">
    The type of a template

    <Prop.Extras>
      **Available values:**

      * `DESIGN`: A design template
      * `ELEMENT`: An element template
    </Prop.Extras>
  </Prop>

  <Prop name="template_domain" type="string" mode="output">
    The domain of a template

    <Prop.Extras>
      **Available values:** The only valid value is `BRAND`: Brand domain.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Update a template's details

An `actor` triggers this event when they update a template

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_TEMPLATE`

      **Available values:** The only valid value is `UPDATE_TEMPLATE`.
    </Prop.Extras>
  </Prop>

  <Prop name="template_type" type="string" mode="output">
    The type of a template

    <Prop.Extras>
      **Available values:**

      * `DESIGN`: A design template
      * `ELEMENT`: An element template
    </Prop.Extras>
  </Prop>

  <Prop name="template_domain" type="string" mode="output">
    The domain of a template

    <Prop.Extras>
      **Available values:** The only valid value is `BRAND`: Brand domain.
    </Prop.Extras>
  </Prop>

  <Prop name="new_title" type="string" mode="output">
    The new title of the template
  </Prop>

  <Prop name="old_title" type="string" mode="output">
    The old title of the template.
  </Prop>

  <Prop name="new_description" type="string" mode="output">
    The new description of the template
  </Prop>

  <Prop name="old_description" type="string" mode="output">
    The old description of the template.
  </Prop>

  <Prop name="new_keywords" type="string[]" mode="output">
    The new keywords of the template
  </Prop>

  <Prop name="old_keywords" type="string[]" mode="output">
    The old keywords of the template
  </Prop>

  <Prop name="changed_fields" type="string[]" mode="output">
    Fields requested to be changed in this update.

    <Prop.Extras>
      **Available values:**

      * `TITLE`: The template's title
      * `DESCRIPTION`: The template's description
      * `KEYWORDS`: The template's keywords
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Delete a template

An `actor` triggers this event when they delete a template.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `DELETE_TEMPLATE`

      **Available values:** The only valid value is `DELETE_TEMPLATE`.
    </Prop.Extras>
  </Prop>

  <Prop name="template_type" type="string" mode="output">
    The type of a template

    <Prop.Extras>
      **Available values:**

      * `DESIGN`: A design template
      * `ELEMENT`: An element template
    </Prop.Extras>
  </Prop>

  <Prop name="template_domain" type="string" mode="output">
    The domain of a template

    <Prop.Extras>
      **Available values:** The only valid value is `BRAND`: Brand domain.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Restore a deleted template

An `actor` triggers this event when they restore a deleted template.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UNDELETE_TEMPLATE`

      **Available values:** The only valid value is `UNDELETE_TEMPLATE`.
    </Prop.Extras>
  </Prop>

  <Prop name="template_type" type="string" mode="output">
    The type of a template

    <Prop.Extras>
      **Available values:**

      * `DESIGN`: A design template
      * `ELEMENT`: An element template
    </Prop.Extras>
  </Prop>

  <Prop name="template_domain" type="string" mode="output">
    The domain of a template

    <Prop.Extras>
      **Available values:** The only valid value is `BRAND`: Brand domain.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Update a template's access controls

An `actor` triggers this event when they update the access control list of a template.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_TEMPLATE_ACCESS_CONTROLS`

      **Available values:** The only valid value is `UPDATE_TEMPLATE_ACCESS_CONTROLS`.
    </Prop.Extras>
  </Prop>

  <Prop name="changes" type="TemplateAccessControlChange[]" required mode="output">
    List of access control changes made to the template

    <Tabs>
      <Tab name="GRANT_USER_TEMPLATE_ACCESS">
        Grant template access to a user

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_USER_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `GRANT_USER_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="user" type="AuditLogUser" required mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>user</strong></>}>
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

          <Prop name="access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_USER_TEMPLATE_ACCESS">
        Revoke template access from a user

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_USER_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `REVOKE_USER_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="user" type="AuditLogUser" required mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>user</strong></>}>
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

          <Prop name="access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_USER_TEMPLATE_ACCESS">
        Update template access from a user

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_USER_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `UPDATE_USER_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="user" type="AuditLogUser" required mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>user</strong></>}>
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

          <Prop name="new_access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="old_access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="GRANT_TEAM_TEMPLATE_ACCESS">
        Grant template access to a team

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_TEAM_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `GRANT_TEAM_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="team" type="AuditLogTeam" required mode="output">
            A Canva team.

            <PillAccordion title={<>Properties of <strong>team</strong></>}>
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

          <Prop name="access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="role" type="string" mode="output">
            Identity context roles assignable to access control principals

            <Prop.Extras>
              **Available values:**

              * `ORGANIZATION_ADMIN`: The admin of the organization
              * `ORGANIZATION_TEAM_MANAGER`: The team manager of the organization
              * `TEAM_OWNER`: The owner of the team
              * `TEAM_ADMIN`: The admin of the team
              * `TEAM_DESIGNER`: The designer of the team
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_TEAM_TEMPLATE_ACCESS">
        Revoke template access from a team

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_TEAM_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `REVOKE_TEAM_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="team" type="AuditLogTeam" required mode="output">
            A Canva team.

            <PillAccordion title={<>Properties of <strong>team</strong></>}>
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

          <Prop name="access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="role" type="string" mode="output">
            Identity context roles assignable to access control principals

            <Prop.Extras>
              **Available values:**

              * `ORGANIZATION_ADMIN`: The admin of the organization
              * `ORGANIZATION_TEAM_MANAGER`: The team manager of the organization
              * `TEAM_OWNER`: The owner of the team
              * `TEAM_ADMIN`: The admin of the team
              * `TEAM_DESIGNER`: The designer of the team
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_TEAM_TEMPLATE_ACCESS">
        Update template access for a team

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_TEAM_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `UPDATE_TEAM_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="team" type="AuditLogTeam" required mode="output">
            A Canva team.

            <PillAccordion title={<>Properties of <strong>team</strong></>}>
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

          <Prop name="new_access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="old_access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="role" type="string" mode="output">
            Identity context roles assignable to access control principals

            <Prop.Extras>
              **Available values:**

              * `ORGANIZATION_ADMIN`: The admin of the organization
              * `ORGANIZATION_TEAM_MANAGER`: The team manager of the organization
              * `TEAM_OWNER`: The owner of the team
              * `TEAM_ADMIN`: The admin of the team
              * `TEAM_DESIGNER`: The designer of the team
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="GRANT_GROUP_TEMPLATE_ACCESS">
        Grant template access to a group

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_GROUP_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `GRANT_GROUP_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="group" type="AuditLogGroup" required mode="output">
            A Canva group.

            <PillAccordion title={<>Properties of <strong>group</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The group ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the group.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_GROUP_TEMPLATE_ACCESS">
        Revoke template access from a group

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_GROUP_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `REVOKE_GROUP_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="group" type="AuditLogGroup" required mode="output">
            A Canva group.

            <PillAccordion title={<>Properties of <strong>group</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The group ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the group.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_GROUP_TEMPLATE_ACCESS">
        Update template access from a group

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_GROUP_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `UPDATE_GROUP_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="group" type="AuditLogGroup" required mode="output">
            A Canva group.

            <PillAccordion title={<>Properties of <strong>group</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The group ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the group.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="old_access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="GRANT_ORGANIZATION_TEMPLATE_ACCESS">
        Grant template access to an organization

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_ORGANIZATION_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `GRANT_ORGANIZATION_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="organization" type="AuditLogOrganization" required mode="output">
            A Canva organization.

            <PillAccordion title={<>Properties of <strong>organization</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The organization ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the organization.

                  For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="role" type="string" mode="output">
            Identity context roles assignable to access control principals

            <Prop.Extras>
              **Available values:**

              * `ORGANIZATION_ADMIN`: The admin of the organization
              * `ORGANIZATION_TEAM_MANAGER`: The team manager of the organization
              * `TEAM_OWNER`: The owner of the team
              * `TEAM_ADMIN`: The admin of the team
              * `TEAM_DESIGNER`: The designer of the team
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_ORGANIZATION_TEMPLATE_ACCESS">
        Revoke template access from an organization

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_ORGANIZATION_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `REVOKE_ORGANIZATION_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="organization" type="AuditLogOrganization" required mode="output">
            A Canva organization.

            <PillAccordion title={<>Properties of <strong>organization</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The organization ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the organization.

                  For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="role" type="string" mode="output">
            Identity context roles assignable to access control principals

            <Prop.Extras>
              **Available values:**

              * `ORGANIZATION_ADMIN`: The admin of the organization
              * `ORGANIZATION_TEAM_MANAGER`: The team manager of the organization
              * `TEAM_OWNER`: The owner of the team
              * `TEAM_ADMIN`: The admin of the team
              * `TEAM_DESIGNER`: The designer of the team
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_ORGANIZATION_TEMPLATE_ACCESS">
        Update template access for an organization

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_ORGANIZATION_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `UPDATE_ORGANIZATION_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="organization" type="AuditLogOrganization" required mode="output">
            A Canva organization.

            <PillAccordion title={<>Properties of <strong>organization</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The organization ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the organization.

                  For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="old_access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="role" type="string" mode="output">
            Identity context roles assignable to access control principals

            <Prop.Extras>
              **Available values:**

              * `ORGANIZATION_ADMIN`: The admin of the organization
              * `ORGANIZATION_TEAM_MANAGER`: The team manager of the organization
              * `TEAM_OWNER`: The owner of the team
              * `TEAM_ADMIN`: The admin of the team
              * `TEAM_DESIGNER`: The designer of the team
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="GRANT_PUBLIC_LINK_TEMPLATE_ACCESS">
        Grant template access to a public share link

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_PUBLIC_LINK_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `GRANT_PUBLIC_LINK_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_PUBLIC_LINK_TEMPLATE_ACCESS">
        Revoke template access from a public share link

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_PUBLIC_LINK_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `REVOKE_PUBLIC_LINK_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="GRANT_TEAM_LINK_TEMPLATE_ACCESS">
        Grant template access to a team share link

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_TEAM_LINK_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `GRANT_TEAM_LINK_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="team" type="AuditLogTeam" required mode="output">
            A Canva team.

            <PillAccordion title={<>Properties of <strong>team</strong></>}>
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

          <Prop name="access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_TEAM_LINK_TEMPLATE_ACCESS">
        Revoke template access from a team share link

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_TEAM_LINK_TEMPLATE_ACCESS`

              **Available values:** The only valid value is `REVOKE_TEAM_LINK_TEMPLATE_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="team" type="AuditLogTeam" required mode="output">
            A Canva team.

            <PillAccordion title={<>Properties of <strong>team</strong></>}>
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

          <Prop name="access" type="TemplateAccessLevel" required mode="output">
            Template access level

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether the user can view the template.
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether the user can edit the template content.
                </Prop>

                <Prop name="share_view_access" type="boolean" required mode="output">
                  Whether the user can share the template with others to view.
                </Prop>

                <Prop name="share_edit_access" type="boolean" required mode="output">
                  Whether the user can share the template with others view and edit.
                </Prop>

                <Prop name="delete" type="boolean" required mode="output">
                  Whether the user can delete the template.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>
    </Tabs>
  </Prop>

  <Prop name="template_type" type="string" mode="output">
    The type of a template

    <Prop.Extras>
      **Available values:**

      * `DESIGN`: A design template
      * `ELEMENT`: An element template
    </Prop.Extras>
  </Prop>

  <Prop name="template_domain" type="string" mode="output">
    The domain of a template

    <Prop.Extras>
      **Available values:** The only valid value is `BRAND`: Brand domain.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

