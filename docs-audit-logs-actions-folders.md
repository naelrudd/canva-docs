Source: https://www.canva.dev/docs/audit-logs/actions/folders.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Folders

## Update a folder's access controls

An `actor` triggers this event when they change the rules that control access to a folder. There can be multiple changes in a single update.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_FOLDER_ACCESS_CONTROLS`

      **Available values:** The only valid value is `UPDATE_FOLDER_ACCESS_CONTROLS`.
    </Prop.Extras>
  </Prop>

  <Prop name="access_control_changes" type="UpdateFolderAccessControlChange[]" required mode="output">
    A change to the rules that control the access to the folder.

    <Tabs>
      <Tab name="UPDATE_FOLDER_OWNER">
        The owner of the folder changed when a user left the team.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_FOLDER_OWNER`

              **Available values:** The only valid value is `UPDATE_FOLDER_OWNER`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_owner" type="AuditLogUser" mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>old_owner</strong></>}>
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

          <Prop name="new_owner" type="AuditLogUser" mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>new_owner</strong></>}>
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

      <Tab name="GRANT_USER_FOLDER_ACCESS">
        A user granted another user access to the folder.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_USER_FOLDER_ACCESS`

              **Available values:** The only valid value is `GRANT_USER_FOLDER_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="FolderAccessLevel" required mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
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
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_USER_FOLDER_ACCESS">
        A user revoked another user's access to the folder.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_USER_FOLDER_ACCESS`

              **Available values:** The only valid value is `REVOKE_USER_FOLDER_ACCESS`.
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

          <Prop name="access" type="FolderAccessLevel" mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_USER_FOLDER_ACCESS">
        A user changed another user's access to the folder.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_USER_FOLDER_ACCESS`

              **Available values:** The only valid value is `UPDATE_USER_FOLDER_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_access" type="FolderAccessLevel" required mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="FolderAccessLevel" required mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
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
        </Prop.List>
      </Tab>

      <Tab name="GRANT_GROUP_FOLDER_ACCESS">
        A user granted a [group](https://www.canva.com/help/groups/) access to the folder.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_GROUP_FOLDER_ACCESS`

              **Available values:** The only valid value is `GRANT_GROUP_FOLDER_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="FolderAccessLevel" required mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
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
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_GROUP_FOLDER_ACCESS">
        A user revoked a [group's](https://www.canva.com/help/groups/) access to the folder.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_GROUP_FOLDER_ACCESS`

              **Available values:** The only valid value is `REVOKE_GROUP_FOLDER_ACCESS`.
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

          <Prop name="access" type="FolderAccessLevel" mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_GROUP_FOLDER_ACCESS">
        A user changed a [group's](https://www.canva.com/help/groups/) access to the folder.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_GROUP_FOLDER_ACCESS`

              **Available values:** The only valid value is `UPDATE_GROUP_FOLDER_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_access" type="FolderAccessLevel" required mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="FolderAccessLevel" required mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
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
        </Prop.List>
      </Tab>

      <Tab name="GRANT_TEAM_FOLDER_ACCESS">
        A user granted a [team](https://www.canva.com/help/create-teams/) access to the folder.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_TEAM_FOLDER_ACCESS`

              **Available values:** The only valid value is `GRANT_TEAM_FOLDER_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="FolderAccessLevel" required mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
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
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_TEAM_FOLDER_ACCESS">
        A user revoked a [team's](https://www.canva.com/help/create-teams/) access to the folder.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_TEAM_FOLDER_ACCESS`

              **Available values:** The only valid value is `REVOKE_TEAM_FOLDER_ACCESS`.
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

          <Prop name="access" type="FolderAccessLevel" mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_TEAM_FOLDER_ACCESS">
        A user changed a [team's](https://www.canva.com/help/create-teams/) access to the folder.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_TEAM_FOLDER_ACCESS`

              **Available values:** The only valid value is `UPDATE_TEAM_FOLDER_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_access" type="FolderAccessLevel" required mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="FolderAccessLevel" required mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
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
        </Prop.List>
      </Tab>

      <Tab name="GRANT_ORGANIZATION_FOLDER_ACCESS">
        A user granted an organization access to the folder.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_ORGANIZATION_FOLDER_ACCESS`

              **Available values:** The only valid value is `GRANT_ORGANIZATION_FOLDER_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="FolderAccessLevel" required mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
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
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_ORGANIZATION_FOLDER_ACCESS">
        A user revoked an organization's access to the folder.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_ORGANIZATION_FOLDER_ACCESS`

              **Available values:** The only valid value is `REVOKE_ORGANIZATION_FOLDER_ACCESS`.
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

          <Prop name="access" type="FolderAccessLevel" mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_ORGANIZATION_FOLDER_ACCESS">
        A user changed an organization's access to the folder.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_ORGANIZATION_FOLDER_ACCESS`

              **Available values:** The only valid value is `UPDATE_ORGANIZATION_FOLDER_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_access" type="FolderAccessLevel" required mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="FolderAccessLevel" required mode="output">
            Whether the folder's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
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
        </Prop.List>
      </Tab>
    </Tabs>
  </Prop>
</Prop.List>

### Example

## Add an item to a folder

An `actor` triggers this event when they add an item to a folder.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `ADD_ITEM_TO_FOLDER`

      **Available values:** The only valid value is `ADD_ITEM_TO_FOLDER`.
    </Prop.Extras>
  </Prop>

  <Prop name="item" type="FolderItem" required mode="output">
    An item in a folder, such as a [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs).

    <PillAccordion title={<>Properties of <strong>item</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="item_type" type="string" required mode="output">
          The type of item.

          <Prop.Extras>
            **Available values:**

            * `FOLDER`: A folder.
            * `DESIGN`: A design.
            * `IMAGE`: An image.
            * `VIDEO`: A video.
            * `TEMPLATE`: A template.
          </Prop.Extras>
        </Prop>

        <Prop name="id" type="string" required mode="output">
          The item ID.
        </Prop>

        <Prop name="team" type="AuditLogTeam" mode="output">
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

        <Prop name="owner" type="AuditLogUser" mode="output">
          A Canva user.

          <PillAccordion title={<>Properties of <strong>owner</strong></>}>
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

        <Prop name="display_name" type="string" mode="output">
          The display name of the item.
          Rarely, it may be omitted for technical reasons.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

### Example

## Remove an item from a folder

An `actor` triggers this event when they remove an item from a folder.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `REMOVE_ITEM_FROM_FOLDER`

      **Available values:** The only valid value is `REMOVE_ITEM_FROM_FOLDER`.
    </Prop.Extras>
  </Prop>

  <Prop name="item" type="FolderItem" required mode="output">
    An item in a folder, such as a [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs).

    <PillAccordion title={<>Properties of <strong>item</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="item_type" type="string" required mode="output">
          The type of item.

          <Prop.Extras>
            **Available values:**

            * `FOLDER`: A folder.
            * `DESIGN`: A design.
            * `IMAGE`: An image.
            * `VIDEO`: A video.
            * `TEMPLATE`: A template.
          </Prop.Extras>
        </Prop>

        <Prop name="id" type="string" required mode="output">
          The item ID.
        </Prop>

        <Prop name="team" type="AuditLogTeam" mode="output">
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

        <Prop name="owner" type="AuditLogUser" mode="output">
          A Canva user.

          <PillAccordion title={<>Properties of <strong>owner</strong></>}>
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

        <Prop name="display_name" type="string" mode="output">
          The display name of the item.
          Rarely, it may be omitted for technical reasons.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

### Example

## Request access to a folder

An `actor` triggers this event when they request access to a folder.
This request is sent to the owner of the folder.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `REQUEST_FOLDER_ACCESS`

      **Available values:** The only valid value is `REQUEST_FOLDER_ACCESS`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Grant access to a folder

An `actor` (typically the folder `owner`) triggers this event when they grant the `requester` access to their folder.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `GRANT_FOLDER_ACCESS`

      **Available values:** The only valid value is `GRANT_FOLDER_ACCESS`.
    </Prop.Extras>
  </Prop>

  <Prop name="requester" type="AuditLogUser" required mode="output">
    A Canva user.

    <PillAccordion title={<>Properties of <strong>requester</strong></>} defaultExpanded={true}>
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

  <Prop name="access" type="string" mode="output">
    A user's access level for a folder.

    <Prop.Extras>
      **Available values:**

      * `VIEW`: The user can view the folder and its contents.
      * `EDIT`: The user can view and edit the folder and its contents.
      * `ADMIN`: The user can view, edit, and modify access to the folder and its contents.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

