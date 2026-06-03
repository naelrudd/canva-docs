Source: https://www.canva.dev/docs/audit-logs/actions/audio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Audio

## Create an audio

An `actor` triggers this event when they create/upload an audio to their account or team.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `CREATE_AUDIO`

      **Available values:** The only valid value is `CREATE_AUDIO`.
    </Prop.Extras>
  </Prop>

  <Prop name="filename" type="string" mode="output">
    The name of the uploaded file.
  </Prop>
</Prop.List>

### Example

## Update an audio's details

An `actor` triggers this event when they update audios in their account or team.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_AUDIO`

      **Available values:** The only valid value is `UPDATE_AUDIO`.
    </Prop.Extras>
  </Prop>

  <Prop name="old_title" type="string" mode="output">
    The old title of the audio.
  </Prop>

  <Prop name="new_title" type="string" mode="output">
    The new title of the audio.
  </Prop>

  <Prop name="old_tags" type="string[]" mode="output">
    Original list of tags associated with the audio.
  </Prop>

  <Prop name="new_tags" type="string[]" mode="output">
    New list of tags associated with the audio.
  </Prop>

  <Prop name="changed_fields" type="string[]" mode="output">
    Fields requested to be changed in this update.

    <Prop.Extras>
      **Available values:**

      * `TITLE`: The audio's title.
      * `TAGS`: The audio's tags.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Delete an audio

An `actor` triggers this event when they permanently delete audios from their account or team.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `DELETE_AUDIO`

      **Available values:** The only valid value is `DELETE_AUDIO`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Trash an audio

An `actor` triggers this event when they move audios to the trash folder.
Audios in the trash folder aren't accessible to collaborators and will be deleted after a
period of time.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `TRASH_AUDIO`

      **Available values:** The only valid value is `TRASH_AUDIO`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Restore an audio from Trash

An `actor` triggers this event when they restore audios from the trash folder.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UNDELETE_AUDIO`

      **Available values:** The only valid value is `UNDELETE_AUDIO`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Copy an audio

An `actor` triggers this event when they copy an audio.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `COPY_AUDIO`

      **Available values:** The only valid value is `COPY_AUDIO`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Update an audio's access controls

An `actor` triggers this event when they change the rules that control access to an audio asset.
There can be multiple changes in a single update.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_AUDIO_ACCESS_CONTROLS`

      **Available values:** The only valid value is `UPDATE_AUDIO_ACCESS_CONTROLS`.
    </Prop.Extras>
  </Prop>

  <Prop name="changes" type="AudioAccessControlListChange[]" required mode="output">
    A change to the rules that control the access to the audio asset.

    <Tabs>
      <Tab name="GRANT_USER_AUDIO_ACCESS">
        A user granted another user access to the audio.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_USER_AUDIO_ACCESS`

              **Available values:** The only valid value is `GRANT_USER_AUDIO_ACCESS`.
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

          <Prop name="access" type="AudioAccessLevel" required mode="output">
            Access permissions for an audio asset.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_USER_AUDIO_ACCESS">
        A user revoked another user's access to the audio.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_USER_AUDIO_ACCESS`

              **Available values:** The only valid value is `REVOKE_USER_AUDIO_ACCESS`.
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
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_USER_AUDIO_ACCESS">
        A user changed another user's access to the audio.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_USER_AUDIO_ACCESS`

              **Available values:** The only valid value is `UPDATE_USER_AUDIO_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_access" type="AudioAccessLevel" required mode="output">
            Access permissions for an audio asset.

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="AudioAccessLevel" required mode="output">
            Access permissions for an audio asset.

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
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

      <Tab name="GRANT_GROUP_AUDIO_ACCESS">
        A user granted a [group](https://www.canva.com/help/groups/) access to the audio.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_GROUP_AUDIO_ACCESS`

              **Available values:** The only valid value is `GRANT_GROUP_AUDIO_ACCESS`.
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

          <Prop name="access" type="AudioAccessLevel" required mode="output">
            Access permissions for an audio asset.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_GROUP_AUDIO_ACCESS">
        A user revoked a [group's](https://www.canva.com/help/groups/) access to the audio.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_GROUP_AUDIO_ACCESS`

              **Available values:** The only valid value is `REVOKE_GROUP_AUDIO_ACCESS`.
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
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_GROUP_AUDIO_ACCESS">
        A user changed a [group's](https://www.canva.com/help/groups/) access to the audio.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_GROUP_AUDIO_ACCESS`

              **Available values:** The only valid value is `UPDATE_GROUP_AUDIO_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_access" type="AudioAccessLevel" required mode="output">
            Access permissions for an audio asset.

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="AudioAccessLevel" required mode="output">
            Access permissions for an audio asset.

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
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

      <Tab name="GRANT_TEAM_AUDIO_ACCESS">
        A user granted a [team](https://www.canva.com/help/create-teams/) access to the audio.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_TEAM_AUDIO_ACCESS`

              **Available values:** The only valid value is `GRANT_TEAM_AUDIO_ACCESS`.
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

          <Prop name="access" type="AudioAccessLevel" required mode="output">
            Access permissions for an audio asset.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_TEAM_AUDIO_ACCESS">
        A user revoked a [team's](https://www.canva.com/help/create-teams/) access to the audio.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_TEAM_AUDIO_ACCESS`

              **Available values:** The only valid value is `REVOKE_TEAM_AUDIO_ACCESS`.
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
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_TEAM_AUDIO_ACCESS">
        A user changed a [team's](https://www.canva.com/help/create-teams/) access to the audio.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_TEAM_AUDIO_ACCESS`

              **Available values:** The only valid value is `UPDATE_TEAM_AUDIO_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_access" type="AudioAccessLevel" required mode="output">
            Access permissions for an audio asset.

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="AudioAccessLevel" required mode="output">
            Access permissions for an audio asset.

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
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

      <Tab name="GRANT_ORGANIZATION_AUDIO_ACCESS">
        A user granted an organization access to the audio.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_ORGANIZATION_AUDIO_ACCESS`

              **Available values:** The only valid value is `GRANT_ORGANIZATION_AUDIO_ACCESS`.
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

          <Prop name="access" type="AudioAccessLevel" required mode="output">
            Access permissions for an audio asset.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_ORGANIZATION_AUDIO_ACCESS">
        A user revoked an organization's access to the audio.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_ORGANIZATION_AUDIO_ACCESS`

              **Available values:** The only valid value is `REVOKE_ORGANIZATION_AUDIO_ACCESS`.
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
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_ORGANIZATION_AUDIO_ACCESS">
        A user changed an organization's access to the audio.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_ORGANIZATION_AUDIO_ACCESS`

              **Available values:** The only valid value is `UPDATE_ORGANIZATION_AUDIO_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_access" type="AudioAccessLevel" required mode="output">
            Access permissions for an audio asset.

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="AudioAccessLevel" required mode="output">
            Access permissions for an audio asset.

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).

                  <Prop.Extras>
                    **Default value:** `false`
                  </Prop.Extras>
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

      <Tab name="UPDATE_AUDIO_OWNER">
        The owner of the audio asset was changed.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_AUDIO_OWNER`

              **Available values:** The only valid value is `UPDATE_AUDIO_OWNER`.
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
    </Tabs>
  </Prop>
</Prop.List>

### Example

