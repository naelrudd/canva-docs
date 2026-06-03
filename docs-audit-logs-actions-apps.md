Source: https://www.canva.dev/docs/audit-logs/actions/apps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Apps

## Install an app

An `actor` triggers this event when they use a third-party app for the first time
(or following app uninstall). For example, when a user selects "open" on a new app
in the editor, or selects **Use in a new design** or **Use in existing design** from the
apps [marketplace](https://www.canva.com/your-apps/). The installation is for a user in a team.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `INSTALL_APP`

      **Available values:** The only valid value is `INSTALL_APP`.
    </Prop.Extras>
  </Prop>

  <Prop name="app" type="AuditLogApp" required mode="output">
    A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

    <PillAccordion title={<>Properties of <strong>app</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The app ID.
        </Prop>

        <Prop name="name" type="string" mode="output">
          The name of the app.
        </Prop>

        <Prop name="version" type="string" mode="output">
          The version of the app.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="permissions" type="string[]" mode="output">
    A set of permissions.

    <Prop.Extras>
      **Available values:**

      * `DESIGN_CONTENT_READ`: Permission to view [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
      * `DESIGN_CONTENT_WRITE`: Permission to modify [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
      * `ASSET_PRIVATE_READ`: Permission to view private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
      * `ASSET_PRIVATE_WRITE`: Permission to modify private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
      * `BRANDKIT_READ`: Permission to view [Brand Kits](https://www.canva.com/help/brand-kit/).
      * `BRAND_TEMPLATE_READ`: Permission to view [Brand Templates](https://www.canva.com/help/brand-templates/).
    </Prop.Extras>
  </Prop>

  <Prop name="settings" type="string[]" mode="output">
    A set of settings.

    <Prop.Extras>
      **Available values:** The only valid value is `ENABLED_FOR_CANVA_AI`: The app is available for Canva AI to use..
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Uninstall an app

An `actor` triggers this event when they remove a third-party app from their list of apps.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UNINSTALL_APP`

      **Available values:** The only valid value is `UNINSTALL_APP`.
    </Prop.Extras>
  </Prop>

  <Prop name="app" type="AuditLogApp" required mode="output">
    A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

    <PillAccordion title={<>Properties of <strong>app</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The app ID.
        </Prop>

        <Prop name="name" type="string" mode="output">
          The name of the app.
        </Prop>

        <Prop name="version" type="string" mode="output">
          The version of the app.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

### Example

## Update an app's permissions

An `actor` triggers this event when they accept updated permissions for an installed
third-party app. The app's developer may have updated the permissions required by the app.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_APP_PERMISSIONS`

      **Available values:** The only valid value is `UPDATE_APP_PERMISSIONS`.
    </Prop.Extras>
  </Prop>

  <Prop name="app" type="AuditLogApp" required mode="output">
    A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

    <PillAccordion title={<>Properties of <strong>app</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The app ID.
        </Prop>

        <Prop name="name" type="string" mode="output">
          The name of the app.
        </Prop>

        <Prop name="version" type="string" mode="output">
          The version of the app.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="old_permissions" type="string[]" mode="output">
    A set of permissions.

    <Prop.Extras>
      **Available values:**

      * `DESIGN_CONTENT_READ`: Permission to view [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
      * `DESIGN_CONTENT_WRITE`: Permission to modify [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
      * `ASSET_PRIVATE_READ`: Permission to view private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
      * `ASSET_PRIVATE_WRITE`: Permission to modify private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
      * `BRANDKIT_READ`: Permission to view [Brand Kits](https://www.canva.com/help/brand-kit/).
      * `BRAND_TEMPLATE_READ`: Permission to view [Brand Templates](https://www.canva.com/help/brand-templates/).
    </Prop.Extras>
  </Prop>

  <Prop name="new_permissions" type="string[]" mode="output">
    A set of permissions.

    <Prop.Extras>
      **Available values:**

      * `DESIGN_CONTENT_READ`: Permission to view [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
      * `DESIGN_CONTENT_WRITE`: Permission to modify [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
      * `ASSET_PRIVATE_READ`: Permission to view private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
      * `ASSET_PRIVATE_WRITE`: Permission to modify private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
      * `BRANDKIT_READ`: Permission to view [Brand Kits](https://www.canva.com/help/brand-kit/).
      * `BRAND_TEMPLATE_READ`: Permission to view [Brand Templates](https://www.canva.com/help/brand-templates/).
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Update a setting for an app

An `actor` triggers this event when they update a setting for an app.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_APP_SETTING`

      **Available values:** The only valid value is `UPDATE_APP_SETTING`.
    </Prop.Extras>
  </Prop>

  <Prop name="app" type="AuditLogApp" required mode="output">
    A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

    <PillAccordion title={<>Properties of <strong>app</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The app ID.
        </Prop>

        <Prop name="name" type="string" mode="output">
          The name of the app.
        </Prop>

        <Prop name="version" type="string" mode="output">
          The version of the app.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="setting" type="string" required mode="output">
    The setting for an app.

    <Prop.Extras>
      **Available values:** The only valid value is `ENABLED_FOR_CANVA_AI`: The app is available for Canva AI to use..
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Disconnect from a third-party service through an app

An `actor` triggers this event when they disconnect from a third-party service from within
a third-party [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps)
installed in Canva.
For example, a user disconnects from Google Drive in the [Google Drive App](https://www.canva.com/your-apps/googledrive/google-drive).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `DISCONNECT_FROM_THIRD_PARTY_APP`

      **Available values:** The only valid value is `DISCONNECT_FROM_THIRD_PARTY_APP`.
    </Prop.Extras>
  </Prop>

  <Prop name="app" type="AuditLogApp" required mode="output">
    A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

    <PillAccordion title={<>Properties of <strong>app</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The app ID.
        </Prop>

        <Prop name="name" type="string" mode="output">
          The name of the app.
        </Prop>

        <Prop name="version" type="string" mode="output">
          The version of the app.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

### Example

## Connect to a third-party service through an app

An `actor` triggers this event when they connect to a third-party service using a third-party
[app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps)
installed in Canva. For example, a user connects to Google Drive using the [Google Drive App](https://www.canva.com/your-apps/googledrive/google-drive).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `CONNECT_TO_THIRD_PARTY_APP`

      **Available values:** The only valid value is `CONNECT_TO_THIRD_PARTY_APP`.
    </Prop.Extras>
  </Prop>

  <Prop name="app" type="AuditLogApp" required mode="output">
    A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

    <PillAccordion title={<>Properties of <strong>app</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The app ID.
        </Prop>

        <Prop name="name" type="string" mode="output">
          The name of the app.
        </Prop>

        <Prop name="version" type="string" mode="output">
          The version of the app.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

### Example

