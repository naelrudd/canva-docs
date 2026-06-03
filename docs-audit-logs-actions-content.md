Source: https://www.canva.dev/docs/audit-logs/actions/content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Content

## Transfer ownership of user content within a team

An `actor` triggers this event when they change the owner of a user's content (such as [designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)) to another user on their Team. For details transferring content ownership, see [Canva Help: Transfer Designs](https://www.canva.com/help/transfer-designs/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `INITIATE_OWNERSHIP_TRANSFER`

      **Available values:** The only valid value is `INITIATE_OWNERSHIP_TRANSFER`.
    </Prop.Extras>
  </Prop>

  <Prop name="new_owner" type="AuditLogUser" required mode="output">
    A Canva user.

    <PillAccordion title={<>Properties of <strong>new_owner</strong></>} defaultExpanded={true}>
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

## Copy assets, folders, or designs

An `actor` triggers this event when they make a copy of:

* One or more [folders](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#folders) either within a team, or to another team.
* One or more [designs](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) or [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets) to another team.
  This event is sent to the `actor`'s team, not the destination team. For details on copying content between teams or accounts, see [Canva Help: Copy designs or files to another team or account](https://www.canva.com/help/transfer-designs-to-personal-account/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `INITIATE_CONTENT_COPY`

      **Available values:** The only valid value is `INITIATE_CONTENT_COPY`.
    </Prop.Extras>
  </Prop>

  <Prop name="destination_team" type="AuditLogTeam" required mode="output">
    A Canva team.

    <PillAccordion title={<>Properties of <strong>destination_team</strong></>} defaultExpanded={true}>
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

  <Prop name="reason" type="ContentCopyReason" mode="output">
    The reason for the content copy operation.

    <Tabs>
      <Tab name="CROSS_ACCOUNT_COPY">
        Content copied from one user account to another.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `CROSS_ACCOUNT_COPY`

              **Available values:** The only valid value is `CROSS_ACCOUNT_COPY`.
            </Prop.Extras>
          </Prop>

          <Prop name="source_user" type="AuditLogUser" mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>source_user</strong></>}>
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

          <Prop name="destination_user" type="AuditLogUser" mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>destination_user</strong></>}>
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

  <Prop name="content_copy_id" type="string" mode="output">
    A unique identifier for a content copy event. This ID matches the `content_copy_id` for the corresponding `RECEIVE_CONTENT_COPY` event.
  </Prop>
</Prop.List>

### Example

## Receive a copy of assets, folders, or designs

A team receives this event when they receive content from another team, or content is copied within the team, as the result of a `INITIATE_CONTENT_COPY` event. This event is sent to the team receiving the content, not the `actor`'s team. For details on copying content between teams or accounts, see [Canva Help: Copy designs or files to another team or account](https://www.canva.com/help/transfer-designs-to-personal-account/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `RECEIVE_CONTENT_COPY`

      **Available values:** The only valid value is `RECEIVE_CONTENT_COPY`.
    </Prop.Extras>
  </Prop>

  <Prop name="source_team" type="AuditLogTeam" required mode="output">
    A Canva team.

    <PillAccordion title={<>Properties of <strong>source_team</strong></>} defaultExpanded={true}>
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

  <Prop name="reason" type="ContentCopyReason" mode="output">
    The reason for the content copy operation.

    <Tabs>
      <Tab name="CROSS_ACCOUNT_COPY">
        Content copied from one user account to another.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `CROSS_ACCOUNT_COPY`

              **Available values:** The only valid value is `CROSS_ACCOUNT_COPY`.
            </Prop.Extras>
          </Prop>

          <Prop name="source_user" type="AuditLogUser" mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>source_user</strong></>}>
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

          <Prop name="destination_user" type="AuditLogUser" mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>destination_user</strong></>}>
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

  <Prop name="content_copy_id" type="string" mode="output">
    A unique identifier for a content copy event. This ID matches the `content_copy_id` for the corresponding `INITIATE_CONTENT_COPY` event. If a user retries a failed copy event, multiple `RECEIVE_CONTENT_COPY` events with the same `content_copy_id` will exist.
  </Prop>
</Prop.List>

### Example

