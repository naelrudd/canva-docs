Source: https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Permissions & Settings

## Update a Team's Permissions

An `actor` triggers this event when they update a team permission for a feature.
For example, when a user sets `MAGIC WRITE` to `TEAM_ADMINS`, users with the `TEAM ADMIN` team role can access `MAGIC WRITE`.
If an a user adds a group to a feature's team permission, all members of this group will get access to the
feature regardless of the members team role.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_TEAM_PERMISSION`

      **Available values:** The only valid value is `UPDATE_TEAM_PERMISSION`.
    </Prop.Extras>
  </Prop>

  <Prop name="team_permission" type="string" required mode="output">
    The feature which the permission controls access too.

    <Prop.Extras>
      **Available values:**

      * `DREAM_STUDIO`: Use Dream studio.
      * `OFFLINE_DESIGNS`: Use Offline Designs.
      * `CANVA_AI`: Use Canva AI (conversational AI) to brainstorm, write, and create designs.
      * `MAGIC_DESIGN`: Use Magic Design.
      * `MAGIC_EDIT`: Use Magic Edit.
      * `MAGIC_MEDIA`: Use Magic Media.
      * `TRANSFORM_INTO_DOC`: Use Transform into Doc.
      * `MAGIC_WRITE`: Use Magic Write.
      * `TEMPLATE_LIBRARY`: Access the templates library.
      * `ASK_CANVA`: Ask Canva for AI-generated design advice.
      * `NON_INDEMNIFIED_CONTENT`: Access elements and fonts not covered by Canva’s IP indemnity.
      * `MAGIC_INSIGHTS`: Use Magic Insights.
      * `CANVA_CODE`: Use Canva Code.
      * `ACCEPT_COPIED_CONTENT_FROM_ANOTHER_TEAM`: Accept copied content from another team.
      * `SHARE_DESIGNS_EXTERNALLY_VIA_LINKS`: Share designs via [public view links](https://www.canva.com/help/sharing-your-design-as-a-public-view-link/), [public embeds](https://www.canva.com/help/embed-designs/), [websites](https://www.canva.com/help/canva-websites/), and [collaboration links](https://www.canva.com/help/share-via-link-or-email/) that can be shared externally.
      * `SHARE_DESIGNS_TO_EXTERNAL_EMAILS`: Share designs to external emails by design access invitation or directly granting access.
      * `SCHEDULE_POSTS_WITH_CONTENT_PLANNER`: Schedule posts with the Content Planner.
      * `CANVA_PRINT`: Use Canva Print.
      * `DOWNLOAD_DESIGNS`: Download designs or selected elements.
      * `COPY_CONTENT_TO_ANOTHER_TEAM`: Send copies of their content outside the team.
      * `PHOTO_ELEMENTS`: Use photo elements.
      * `AUDIO_ELEMENTS`: Use audio elements.
      * `VIDEO_ELEMENTS`: Use video elements.
      * `GRAPHIC_ELEMENTS`: Use graphic elements.
      * `STICKER_ELEMENTS`: Use sticker elements.
      * `CHART_ELEMENTS`: Use chart elements.
      * `TABLE_ELEMENTS`: Use table elements.
      * `FRAME_ELEMENTS`: Use frame elements.
      * `GRID_ELEMENTS`: Use grid elements.
      * `SHAPE_ELEMENTS`: Use shape elements.
      * `OTHER_ELEMENTS`: Use any other elements.
      * `VIEW_EMAILS`: See other members email addresses.
      * `CREATE_GROUPS`: Create [groups](https://www.canva.com/help/groups/).
      * `LEAVE_TEAM`: Leave a team.
      * `REFERENCE_TEAM_CONTENT_FOR_AI_GENERATED_RESPONSES`: Reference team documents when using AI to generate content.
      * `MAGIC_ACTIVITIES`: Use Magic Activities.
      * `GROW_CREATE`: Use Canva Grow Create
      * `GROW_INSIGHTS`: Use Canva Grow Insights
      * `GROW_INSPIRE`: Use Canva Grow Inspire
      * `CONNECT_AD_ACCOUNTS`: Connect Ad Accounts to Canva Grow
      * `MAGIC_BACKGROUND`: Use Magic Background.
      * `AI_CHART_GENERATION`: Use AI to generate charts.
      * `PUBLISH_TO_WEBSITE_DOMAIN`: Publish to a website domain.
      * `AI_AUDIO_GENERATION`: Use AI to generate audio.
      * `AI_3D_ELEMENT_GENERATION`: Use AI to generate 3D elements.
      * `MAGIC_DECORATIONS`: Use Magic Decorations.
      * `BEAUTIFY`: Use Beautify.
      * `MAGIC_LAYERS`: Use Magic Layers.
      * `BULK_CREATE_AUTO_MATCH_FIELDS`: Use auto-match fields in bulk create.
      * `IMAGE_TO_VIDEO`: Use Image to Video.
    </Prop.Extras>
  </Prop>

  <Prop name="old_team_permission_role" type="string" mode="output">
    The team role for a feature. Users who are assigned this team role will access to the feature controlled by the Permission.

    <Prop.Extras>
      **Available values:**

      * `NO_ONE`: No team members can use the feature.
      * `TEAM_ADMINS`: Team admins can use the feature.
      * `TEAM_BRAND_DESIGNERS_AND_TEAM_ADMINS`: Team designers and admins can use the feature.
      * `EVERYONE`: All team members can use the feature.
    </Prop.Extras>
  </Prop>

  <Prop name="new_team_permission_role" type="string" mode="output">
    The team role for a feature. Users who are assigned this team role will access to the feature controlled by the Permission.

    <Prop.Extras>
      **Available values:**

      * `NO_ONE`: No team members can use the feature.
      * `TEAM_ADMINS`: Team admins can use the feature.
      * `TEAM_BRAND_DESIGNERS_AND_TEAM_ADMINS`: Team designers and admins can use the feature.
      * `EVERYONE`: All team members can use the feature.
    </Prop.Extras>
  </Prop>

  <Prop name="old_groups" type="AuditLogGroup[]" mode="output">
    The [Groups](https://www.canva.dev/docs/audit-logs/how-are-teams-structured) associated with this Permission Setting. Members of a Group included will have access to the feature regardless of the Team Role.

    <PillAccordion title={<>Properties of <strong>old_groups</strong></>} defaultExpanded={true}>
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

  <Prop name="new_groups" type="AuditLogGroup[]" mode="output">
    The [Groups](https://www.canva.dev/docs/audit-logs/how-are-teams-structured) associated with this Permission Setting. Members of a Group included will have access to the feature regardless of the Team Role.

    <PillAccordion title={<>Properties of <strong>new_groups</strong></>} defaultExpanded={true}>
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

### Example

## Update an Organization's Permissions

An `actor` triggers this event when they update an organization's default permission for a feature.
For example, when an organization admin sets `MAGIC WRITE` to `TEAM_ADMINS`, all users in the organization with the `TEAM ADMIN` team role can access `MAGIC WRITE`.
An organization admin is able to specify whether this default permission value is overrideable by team level admins.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_ORGANIZATION_PERMISSION`

      **Available values:** The only valid value is `UPDATE_ORGANIZATION_PERMISSION`.
    </Prop.Extras>
  </Prop>

  <Prop name="team_permission" type="string" required mode="output">
    The feature which the permission controls access too.

    <Prop.Extras>
      **Available values:**

      * `DREAM_STUDIO`: Use Dream studio.
      * `OFFLINE_DESIGNS`: Use Offline Designs.
      * `CANVA_AI`: Use Canva AI (conversational AI) to brainstorm, write, and create designs.
      * `MAGIC_DESIGN`: Use Magic Design.
      * `MAGIC_EDIT`: Use Magic Edit.
      * `MAGIC_MEDIA`: Use Magic Media.
      * `TRANSFORM_INTO_DOC`: Use Transform into Doc.
      * `MAGIC_WRITE`: Use Magic Write.
      * `TEMPLATE_LIBRARY`: Access the templates library.
      * `ASK_CANVA`: Ask Canva for AI-generated design advice.
      * `NON_INDEMNIFIED_CONTENT`: Access elements and fonts not covered by Canva’s IP indemnity.
      * `MAGIC_INSIGHTS`: Use Magic Insights.
      * `CANVA_CODE`: Use Canva Code.
      * `ACCEPT_COPIED_CONTENT_FROM_ANOTHER_TEAM`: Accept copied content from another team.
      * `SHARE_DESIGNS_EXTERNALLY_VIA_LINKS`: Share designs via [public view links](https://www.canva.com/help/sharing-your-design-as-a-public-view-link/), [public embeds](https://www.canva.com/help/embed-designs/), [websites](https://www.canva.com/help/canva-websites/), and [collaboration links](https://www.canva.com/help/share-via-link-or-email/) that can be shared externally.
      * `SHARE_DESIGNS_TO_EXTERNAL_EMAILS`: Share designs to external emails by design access invitation or directly granting access.
      * `SCHEDULE_POSTS_WITH_CONTENT_PLANNER`: Schedule posts with the Content Planner.
      * `CANVA_PRINT`: Use Canva Print.
      * `DOWNLOAD_DESIGNS`: Download designs or selected elements.
      * `COPY_CONTENT_TO_ANOTHER_TEAM`: Send copies of their content outside the team.
      * `PHOTO_ELEMENTS`: Use photo elements.
      * `AUDIO_ELEMENTS`: Use audio elements.
      * `VIDEO_ELEMENTS`: Use video elements.
      * `GRAPHIC_ELEMENTS`: Use graphic elements.
      * `STICKER_ELEMENTS`: Use sticker elements.
      * `CHART_ELEMENTS`: Use chart elements.
      * `TABLE_ELEMENTS`: Use table elements.
      * `FRAME_ELEMENTS`: Use frame elements.
      * `GRID_ELEMENTS`: Use grid elements.
      * `SHAPE_ELEMENTS`: Use shape elements.
      * `OTHER_ELEMENTS`: Use any other elements.
      * `VIEW_EMAILS`: See other members email addresses.
      * `CREATE_GROUPS`: Create [groups](https://www.canva.com/help/groups/).
      * `LEAVE_TEAM`: Leave a team.
      * `REFERENCE_TEAM_CONTENT_FOR_AI_GENERATED_RESPONSES`: Reference team documents when using AI to generate content.
      * `MAGIC_ACTIVITIES`: Use Magic Activities.
      * `GROW_CREATE`: Use Canva Grow Create
      * `GROW_INSIGHTS`: Use Canva Grow Insights
      * `GROW_INSPIRE`: Use Canva Grow Inspire
      * `CONNECT_AD_ACCOUNTS`: Connect Ad Accounts to Canva Grow
      * `MAGIC_BACKGROUND`: Use Magic Background.
      * `AI_CHART_GENERATION`: Use AI to generate charts.
      * `PUBLISH_TO_WEBSITE_DOMAIN`: Publish to a website domain.
      * `AI_AUDIO_GENERATION`: Use AI to generate audio.
      * `AI_3D_ELEMENT_GENERATION`: Use AI to generate 3D elements.
      * `MAGIC_DECORATIONS`: Use Magic Decorations.
      * `BEAUTIFY`: Use Beautify.
      * `MAGIC_LAYERS`: Use Magic Layers.
      * `BULK_CREATE_AUTO_MATCH_FIELDS`: Use auto-match fields in bulk create.
      * `IMAGE_TO_VIDEO`: Use Image to Video.
    </Prop.Extras>
  </Prop>

  <Prop name="old_team_overrides_enabled" type="boolean" mode="output">
    Whether or not the team permission was overrideable by team admins previously.
  </Prop>

  <Prop name="new_team_overrides_enabled" type="boolean" mode="output">
    Whether or not the team permission is overrideable by team admins currently.
  </Prop>

  <Prop name="old_team_permission_role_default" type="string" mode="output">
    The team role for a feature. Users who are assigned this team role will access to the feature controlled by the Permission.

    <Prop.Extras>
      **Available values:**

      * `NO_ONE`: No team members can use the feature.
      * `TEAM_ADMINS`: Team admins can use the feature.
      * `TEAM_BRAND_DESIGNERS_AND_TEAM_ADMINS`: Team designers and admins can use the feature.
      * `EVERYONE`: All team members can use the feature.
    </Prop.Extras>
  </Prop>

  <Prop name="new_team_permission_role_default" type="string" mode="output">
    The team role for a feature. Users who are assigned this team role will access to the feature controlled by the Permission.

    <Prop.Extras>
      **Available values:**

      * `NO_ONE`: No team members can use the feature.
      * `TEAM_ADMINS`: Team admins can use the feature.
      * `TEAM_BRAND_DESIGNERS_AND_TEAM_ADMINS`: Team designers and admins can use the feature.
      * `EVERYONE`: All team members can use the feature.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Update an Organization's settings

An `actor` triggers this event when they update an organization setting.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_ORGANIZATION_SETTING`

      **Available values:** The only valid value is `UPDATE_ORGANIZATION_SETTING`.
    </Prop.Extras>
  </Prop>

  <Prop name="setting" type="string" required mode="output">
    The name of the setting that was updated.

    <Prop.Extras>
      **Available values:**

      * `PERSONAL_TEAM_ARCHIVING_ENABLED`: Automatically [archive any personal teams](https://www.canva.com/help/enable-content-consolidation-enterprise/) that your managed members may have.
      * `SHARE_DESIGNS_WITH_CANVA_SUPPORT_ENABLED`: Allows or prevents members of a [Canva organization](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/) from temporarily sharing affected designs with Canva Support during support requests.
      * `INVESTIGATIONS_ENABLED`: Allows organisation admins to access private content that hasn’t been shared with them. This access is for security and compliance investigations only and is always audit logged.
      * `DESIGN_ACTIVITY_REPORT_ENABLED`: When turned on, admins can access the design activity report which shows insights about team designs.
      * `TEAM_ARCHIVAL_ENABLED`: When turned on, affiliated users will have brands they own archived. See [Archive personal teams in Canva](https://www.canva.com/help/enable-content-consolidation-enterprise/) for more details.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Update data residency region

An `actor` triggers this event when they update the data residency region.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_DATA_RESIDENCY_REGION_SETTING`

      **Available values:** The only valid value is `UPDATE_DATA_RESIDENCY_REGION_SETTING`.
    </Prop.Extras>
  </Prop>

  <Prop name="new_region" type="string" required mode="output">
    The data residency region.

    <Prop.Extras>
      **Available values:**

      * `US`: United States
      * `EU`: Europe
      * `AU`: Australia
      * `JP`: Japan
      * `ANY`: No preference
    </Prop.Extras>
  </Prop>

  <Prop name="old_region" type="string" mode="output">
    The data residency region.

    <Prop.Extras>
      **Available values:**

      * `US`: United States
      * `EU`: Europe
      * `AU`: Australia
      * `JP`: Japan
      * `ANY`: No preference
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

