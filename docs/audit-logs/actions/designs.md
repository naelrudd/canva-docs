Source: https://www.canva.dev/docs/audit-logs/actions/designs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Designs

## Copy a design

An `actor` triggers this event when they make a copy of an existing design.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `COPY_DESIGN`

      **Available values:** The only valid value is `COPY_DESIGN`.
    </Prop.Extras>
  </Prop>

  <Prop name="original_design_id" type="string" required mode="output">
    The ID of the original design.
  </Prop>

  <Prop name="title" type="string" mode="output">
    Title of the new design.
  </Prop>
</Prop.List>

### Example

## View a design

An `actor` triggers this event when they view a design. Actors viewing a publicly shared
design without logging in are recorded as `ANONYMOUS`.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `VIEW_DESIGN`

      **Available values:** The only valid value is `VIEW_DESIGN`.
    </Prop.Extras>
  </Prop>

  <Prop name="view_type" type="string" mode="output">
    The activity type for viewing a design.

    <Prop.Extras>
      **Available values:**

      * `VIEW_IN_EDITOR`: Viewed in the editor.
      * `VIEW_IN_VIEWER`: Viewed in the viewer.
    </Prop.Extras>
  </Prop>

  <Prop name="design_type" type="string" mode="output">
    The type of design, such as "Presentation (16:9)", "Document", or "Instagram Post (Square)".
  </Prop>
</Prop.List>

### Example

## View a design from a share link

An `actor` triggers this event when they open a design from a share link, and gain access to that design.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `ACCEPT_DESIGN_SHARE`

      **Available values:** The only valid value is `ACCEPT_DESIGN_SHARE`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Import a file to create a new design

An `actor` triggers this event when they import a file into Canva to create a new
design. This includes uploaded presentations and PDFs, and doesn't include Canva design
[assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets),
such as images and videos.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `IMPORT_DESIGN`

      **Available values:** The only valid value is `IMPORT_DESIGN`.
    </Prop.Extras>
  </Prop>

  <Prop name="title" type="string" mode="output">
    The title of the imported design.
  </Prop>

  <Prop name="file_type" type="string" mode="output">
    The file type of the imported file, such as:

    * `PPTX` for a Microsoft PowerPoint presentations.
    * `PDF` for Portable Document Format files.
  </Prop>
</Prop.List>

### Example

## Create a design

An `actor` triggers this event when they create a new
[design in Canva](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs).
This includes when a user creates a design from a template, or using a [Canva App or
Canva Integration](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `CREATE_DESIGN`

      **Available values:** The only valid value is `CREATE_DESIGN`.
    </Prop.Extras>
  </Prop>

  <Prop name="title" type="string" mode="output">
    Title of the new design.
  </Prop>

  <Prop name="design_type" type="string" mode="output">
    The type of design, such as "Presentation (16:9)", "Document", or "Instagram Post (Square)".
  </Prop>
</Prop.List>

### Example

## Trash a design

An `actor` triggers this event when they move a design to the trash folder.
Designs in the trash folder aren't accessible to collaborators and will be deleted after a
period of time.
For details, see: [Deleting designs](https://www.canva.com/help/delete-designs/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `TRASH_DESIGN`

      **Available values:** The only valid value is `TRASH_DESIGN`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Restore a design from Trash

An `actor` triggers this event when they restore a design from the trash folder.
For details, see:
[Restoring or deleting designs or files from your Trash](https://www.canva.com/help/deleted-designs/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UNTRASH_DESIGN`

      **Available values:** The only valid value is `UNTRASH_DESIGN`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Delete a design from Trash

An `actor` triggers this event when they permanently delete a design from the trash folder.
Deleting a user's account will also delete all the designs in their trash folder.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `DELETE_DESIGN`

      **Available values:** The only valid value is `DELETE_DESIGN`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Restore a deleted design

An `actor` triggers this event when they restore a recently deleted design.
For example, when restoring a deleted user or
[team account](https://www.canva.com/help/recover-designs-deleted-team/), the designs deleted with
the account will also be restored.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UNDELETE_DESIGN`

      **Available values:** The only valid value is `UNDELETE_DESIGN`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Update a design's access controls

An `actor` triggers this event when they change the rules that control access to a design. There can be multiple changes in a single update.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_DESIGN_ACCESS_CONTROLS`

      **Available values:** The only valid value is `UPDATE_DESIGN_ACCESS_CONTROLS`.
    </Prop.Extras>
  </Prop>

  <Prop name="changes" type="UpdateDesignAccessControlChange[]" required mode="output">
    A change to the rules that control the access to the design.

    <Tabs>
      <Tab name="CREATE_DESIGN_ACCESS_TOKEN">
        A user created an access token that allows the design to be publicly accessible.
        Examples include creating:

        * [A Public view link](https://www.canva.com/help/sharing-your-design-as-a-public-view-link/).
        * [An embed of a design](https://www.canva.com/help/embed-designs/).
        * [A Canva Website](https://www.canva.com/help/canva-websites/).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `CREATE_DESIGN_ACCESS_TOKEN`

              **Available values:** The only valid value is `CREATE_DESIGN_ACCESS_TOKEN`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="token_prefix" type="string" mode="output">
            The prefix of the access token for the design.
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="DELETE_DESIGN_ACCESS_TOKEN">
        A user removed an access token that allows the design to be publicly accessible,
        such as deleting a [Public view link](https://www.canva.com/en_au/help/sharing-your-design-as-a-public-view-link/).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `DELETE_DESIGN_ACCESS_TOKEN`

              **Available values:** The only valid value is `DELETE_DESIGN_ACCESS_TOKEN`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="token_prefix" type="string" mode="output">
            The prefix of the access token for the design.
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="CREATE_DESIGN_ACCESS_INVITE">
        A user sent an invitation to access the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `CREATE_DESIGN_ACCESS_INVITE`

              **Available values:** The only valid value is `CREATE_DESIGN_ACCESS_INVITE`.
            </Prop.Extras>
          </Prop>

          <Prop name="recipient" type="string" required mode="output">
            The recipient of the invitation. This property contains the address used to share the design, such as the recipient's email address, Slack ID, or mobile number.
          </Prop>

          <Prop name="access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="token_prefix" type="string" mode="output">
            The prefix of the single-use invite token for the design.
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REDEEM_DESIGN_ACCESS_INVITE">
        A user exchanged the invitation to access the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REDEEM_DESIGN_ACCESS_INVITE`

              **Available values:** The only valid value is `REDEEM_DESIGN_ACCESS_INVITE`.
            </Prop.Extras>
          </Prop>

          <Prop name="recipient" type="string" required mode="output">
            The recipient of the invitation. This property contains the address used to share the design, such as the recipient's email address, Slack ID, or mobile number.
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

          <Prop name="token_prefix" type="string" mode="output">
            The prefix of the single-use invite token for the design.
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="DELETE_DESIGN_ACCESS_INVITE">
        A user removed the invitation to access the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `DELETE_DESIGN_ACCESS_INVITE`

              **Available values:** The only valid value is `DELETE_DESIGN_ACCESS_INVITE`.
            </Prop.Extras>
          </Prop>

          <Prop name="recipient" type="string" required mode="output">
            The recipient of the invitation. This property contains the address used to share the design, such as the recipient's email address, Slack ID, or mobile number.
          </Prop>

          <Prop name="token_prefix" type="string" mode="output">
            The prefix of the single-use invite token for the design.
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_DESIGN_OWNER">
        The owner of the design changed when a user left the team.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_DESIGN_OWNER`

              **Available values:** The only valid value is `UPDATE_DESIGN_OWNER`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_owner" type="DesignOwner" required mode="output">
            <Tabs>
              <Tab name="USER">
                <Prop.List>
                  <Prop name="type" type="string" required mode="output">
                    <Prop.Extras>
                      **Default value:** `USER`

                      **Available values:** The only valid value is `USER`.
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

              <Tab name="TEAM_LIBRARY">
                <Prop.List>
                  <Prop name="type" type="string" required mode="output">
                    <Prop.Extras>
                      **Default value:** `TEAM_LIBRARY`

                      **Available values:** The only valid value is `TEAM_LIBRARY`.
                    </Prop.Extras>
                  </Prop>

                  <Prop name="team_library" type="AuditLogTeamLibrary" required mode="output">
                    A Canva Team Library.

                    <PillAccordion title={<>Properties of <strong>team_library</strong></>}>
                      <Prop.List>
                        <Prop name="id" type="string" required mode="output">
                          The Team Library ID.
                        </Prop>

                        <Prop name="name" type="string" mode="output">
                          The name of the Team Library.
                        </Prop>
                      </Prop.List>
                    </PillAccordion>
                  </Prop>
                </Prop.List>
              </Tab>
            </Tabs>
          </Prop>

          <Prop name="new_owner" type="DesignOwner" required mode="output">
            <Tabs>
              <Tab name="USER">
                <Prop.List>
                  <Prop name="type" type="string" required mode="output">
                    <Prop.Extras>
                      **Default value:** `USER`

                      **Available values:** The only valid value is `USER`.
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

              <Tab name="TEAM_LIBRARY">
                <Prop.List>
                  <Prop name="type" type="string" required mode="output">
                    <Prop.Extras>
                      **Default value:** `TEAM_LIBRARY`

                      **Available values:** The only valid value is `TEAM_LIBRARY`.
                    </Prop.Extras>
                  </Prop>

                  <Prop name="team_library" type="AuditLogTeamLibrary" required mode="output">
                    A Canva Team Library.

                    <PillAccordion title={<>Properties of <strong>team_library</strong></>}>
                      <Prop.List>
                        <Prop name="id" type="string" required mode="output">
                          The Team Library ID.
                        </Prop>

                        <Prop name="name" type="string" mode="output">
                          The name of the Team Library.
                        </Prop>
                      </Prop.List>
                    </PillAccordion>
                  </Prop>
                </Prop.List>
              </Tab>
            </Tabs>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="CREATE_DESIGN_ACCESS_RESTRICTION">
        A user restricted access to the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `CREATE_DESIGN_ACCESS_RESTRICTION`

              **Available values:** The only valid value is `CREATE_DESIGN_ACCESS_RESTRICTION`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="DELETE_DESIGN_ACCESS_RESTRICTION">
        A user removed an access restriction on the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `DELETE_DESIGN_ACCESS_RESTRICTION`

              **Available values:** The only valid value is `DELETE_DESIGN_ACCESS_RESTRICTION`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="GRANT_USER_DESIGN_ACCESS">
        A user granted another user access to the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_USER_DESIGN_ACCESS`

              **Available values:** The only valid value is `GRANT_USER_DESIGN_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
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

      <Tab name="REVOKE_USER_DESIGN_ACCESS">
        A user revoked another user's access to the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_USER_DESIGN_ACCESS`

              **Available values:** The only valid value is `REVOKE_USER_DESIGN_ACCESS`.
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

          <Prop name="access" type="DesignAccessLevel" mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_USER_DESIGN_ACCESS">
        A user changed another user's access to the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_USER_DESIGN_ACCESS`

              **Available values:** The only valid value is `UPDATE_USER_DESIGN_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
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

      <Tab name="GRANT_GROUP_DESIGN_ACCESS">
        A user granted a [group](https://www.canva.com/help/groups/) access to the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_GROUP_DESIGN_ACCESS`

              **Available values:** The only valid value is `GRANT_GROUP_DESIGN_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
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

      <Tab name="REVOKE_GROUP_DESIGN_ACCESS">
        A user removed a [group's](https://www.canva.com/help/groups/) access to the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_GROUP_DESIGN_ACCESS`

              **Available values:** The only valid value is `REVOKE_GROUP_DESIGN_ACCESS`.
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

          <Prop name="access" type="DesignAccessLevel" mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_GROUP_DESIGN_ACCESS">
        A user changed a [group's](https://www.canva.com/help/groups/) access to the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_GROUP_DESIGN_ACCESS`

              **Available values:** The only valid value is `UPDATE_GROUP_DESIGN_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
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

      <Tab name="GRANT_TEAM_DESIGN_ACCESS">
        A user granted a [team](https://www.canva.com/help/create-teams/) access to the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_TEAM_DESIGN_ACCESS`

              **Available values:** The only valid value is `GRANT_TEAM_DESIGN_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
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

      <Tab name="REVOKE_TEAM_DESIGN_ACCESS">
        A user removed a [team's](https://www.canva.com/help/create-teams/) access to the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_TEAM_DESIGN_ACCESS`

              **Available values:** The only valid value is `REVOKE_TEAM_DESIGN_ACCESS`.
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

          <Prop name="access" type="DesignAccessLevel" mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_TEAM_DESIGN_ACCESS">
        A user changed a [team's](https://www.canva.com/help/create-teams/) access to the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_TEAM_DESIGN_ACCESS`

              **Available values:** The only valid value is `UPDATE_TEAM_DESIGN_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
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

      <Tab name="GRANT_ORGANIZATION_DESIGN_ACCESS">
        A user granted an organization access to the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_ORGANIZATION_DESIGN_ACCESS`

              **Available values:** The only valid value is `GRANT_ORGANIZATION_DESIGN_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
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

      <Tab name="REVOKE_ORGANIZATION_DESIGN_ACCESS">
        A user revoked an organization's access to the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_ORGANIZATION_DESIGN_ACCESS`

              **Available values:** The only valid value is `REVOKE_ORGANIZATION_DESIGN_ACCESS`.
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

          <Prop name="access" type="DesignAccessLevel" mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_ORGANIZATION_DESIGN_ACCESS">
        A user changed an organization's access to the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_ORGANIZATION_DESIGN_ACCESS`

              **Available values:** The only valid value is `UPDATE_ORGANIZATION_DESIGN_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>old_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>new_access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
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

      <Tab name="GRANT_DESIGN_LINK_ACCESS">
        A user created a [collaboration link](https://www.canva.com/help/share-via-link-or-email/) for the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GRANT_DESIGN_LINK_ACCESS`

              **Available values:** The only valid value is `GRANT_DESIGN_LINK_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="owning_team_only" type="boolean" mode="output">
            Only users in the same team as the design's owner can access the design.

            If `owning_team_only` is `false`, anyone with the link can access the design.
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REVOKE_DESIGN_LINK_ACCESS">
        A user revoked a [collaboration link](https://www.canva.com/help/share-via-link-or-email/) for the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REVOKE_DESIGN_LINK_ACCESS`

              **Available values:** The only valid value is `REVOKE_DESIGN_LINK_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="access" type="DesignAccessLevel" required mode="output">
            Whether the design's content can be viewed or edited.

            <PillAccordion title={<>Properties of <strong>access</strong></>}>
              <Prop.List>
                <Prop name="read" type="boolean" required mode="output">
                  Whether read access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="write" type="boolean" required mode="output">
                  Whether write access has been provided (`true`) or denied (`false`).
                </Prop>

                <Prop name="comment" type="boolean" mode="output">
                  Whether comment access has been provided (`true`) or denied (`false`).
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="owning_team_only" type="boolean" mode="output">
            Only users in the same team as the design's owner can access the design.

            If `owning_team_only` is `false`, anyone with the link can access the design.
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="UPDATE_DESIGN_LINK_ACCESS">
        A user changed a [collaboration link](https://www.canva.com/help/share-via-link-or-email/) for the design.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `UPDATE_DESIGN_LINK_ACCESS`

              **Available values:** The only valid value is `UPDATE_DESIGN_LINK_ACCESS`.
            </Prop.Extras>
          </Prop>

          <Prop name="old_link_role" type="DesignLinkRole" required mode="output">
            How the design may be accessed using a [collaboration link](https://www.canva.com/help/share-via-link-or-email/).

            <PillAccordion title={<>Properties of <strong>old_link_role</strong></>}>
              <Prop.List>
                <Prop name="access" type="DesignAccessLevel" required mode="output">
                  Whether the design's content can be viewed or edited.

                  <PillAccordion title={<>Properties of <strong>access</strong></>}>
                    <Prop.List>
                      <Prop name="read" type="boolean" required mode="output">
                        Whether read access has been provided (`true`) or denied (`false`).
                      </Prop>

                      <Prop name="write" type="boolean" required mode="output">
                        Whether write access has been provided (`true`) or denied (`false`).
                      </Prop>

                      <Prop name="comment" type="boolean" mode="output">
                        Whether comment access has been provided (`true`) or denied (`false`).
                      </Prop>
                    </Prop.List>
                  </PillAccordion>
                </Prop>

                <Prop name="owning_team_only" type="boolean" mode="output">
                  Only users in the same team as the design's owner can access the design.

                  If `owning_team_only` is `false`, anyone with the link can access the design.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="new_link_role" type="DesignLinkRole" required mode="output">
            How the design may be accessed using a [collaboration link](https://www.canva.com/help/share-via-link-or-email/).

            <PillAccordion title={<>Properties of <strong>new_link_role</strong></>}>
              <Prop.List>
                <Prop name="access" type="DesignAccessLevel" required mode="output">
                  Whether the design's content can be viewed or edited.

                  <PillAccordion title={<>Properties of <strong>access</strong></>}>
                    <Prop.List>
                      <Prop name="read" type="boolean" required mode="output">
                        Whether read access has been provided (`true`) or denied (`false`).
                      </Prop>

                      <Prop name="write" type="boolean" required mode="output">
                        Whether write access has been provided (`true`) or denied (`false`).
                      </Prop>

                      <Prop name="comment" type="boolean" mode="output">
                        Whether comment access has been provided (`true`) or denied (`false`).
                      </Prop>
                    </Prop.List>
                  </PillAccordion>
                </Prop>

                <Prop name="owning_team_only" type="boolean" mode="output">
                  Only users in the same team as the design's owner can access the design.

                  If `owning_team_only` is `false`, anyone with the link can access the design.
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

## Send a design share notification

An `actor` triggers this event when they share a design.
Canva will attempt to send an email and an in-app notification to the user the design is shared with (`recipient`).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `SEND_DESIGN_SHARE_NOTIFICATION`

      **Available values:** The only valid value is `SEND_DESIGN_SHARE_NOTIFICATION`.
    </Prop.Extras>
  </Prop>

  <Prop name="recipient" type="ShareNotificationRecipient" required mode="output">
    The recipient of the share notification.

    The recipient can be a user, a group, an organization, or an email address.

    <Tabs>
      <Tab name="USER_RECIPIENT">
        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `USER_RECIPIENT`

              **Available values:** The only valid value is `USER_RECIPIENT`.
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

      <Tab name="GROUP_RECIPIENT">
        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GROUP_RECIPIENT`

              **Available values:** The only valid value is `GROUP_RECIPIENT`.
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

      <Tab name="ORGANIZATION_RECIPIENT">
        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `ORGANIZATION_RECIPIENT`

              **Available values:** The only valid value is `ORGANIZATION_RECIPIENT`.
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

      <Tab name="EMAIL_RECIPIENT">
        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `EMAIL_RECIPIENT`

              **Available values:** The only valid value is `EMAIL_RECIPIENT`.
            </Prop.Extras>
          </Prop>

          <Prop name="email" type="string" required mode="output">
            The email address the design invite was sent to.
          </Prop>
        </Prop.List>
      </Tab>
    </Tabs>
  </Prop>

  <Prop name="message" type="string" mode="output">
    An optional message from the `actor` to the `recipient`.
  </Prop>

  <Prop name="invite_to_team" type="boolean" mode="output">
    Whether the `recipient` was invited to the team containing the shared design.
  </Prop>
</Prop.List>

### Example

## Request access to a design

An `actor` triggers this event when they request access to a design.
This request is sent to the owner of the design.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `REQUEST_DESIGN_ACCESS`

      **Available values:** The only valid value is `REQUEST_DESIGN_ACCESS`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Grant access to a design

An `actor` (typically the design `owner`) triggers this event when they grant the `requester` access to their design.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `GRANT_DESIGN_ACCESS`

      **Available values:** The only valid value is `GRANT_DESIGN_ACCESS`.
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
    A user's access level for a design.

    <Prop.Extras>
      **Available values:**

      * `VIEW`: The user can view the design.
      * `COMMENT`: The user can view and comment on the design.
      * `EDIT`: The user can view, comment, edit, and modify access to the design.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

