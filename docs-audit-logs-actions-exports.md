Source: https://www.canva.dev/docs/audit-logs/actions/exports.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exports

## Export a design

An `actor` triggers this event when they export a design.
Internal Canva systems may export the design for tasks including:

* Creating template previews.
* Creating design and template thumbnails.
* Sending a design for [print](https://www.canva.com/print/).

[Canva Apps and Canva Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)
can also trigger the export event.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `EXPORT_DESIGN`

      **Available values:** The only valid value is `EXPORT_DESIGN`.
    </Prop.Extras>
  </Prop>

  <Prop name="reason" type="ExportReason" mode="output">
    The reason the design was exported. If not specified, a user, a Canva App, or a Canva
    integration exported the design.

    <Tabs>
      <Tab name="APP">
        The design was exported by an app.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `APP`

              **Available values:** The only valid value is `APP`.
            </Prop.Extras>
          </Prop>

          <Prop name="app" type="AuditLogApp" required mode="output">
            A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

            <PillAccordion title={<>Properties of <strong>app</strong></>}>
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
      </Tab>

      <Tab name="INTERNAL">
        Canva internally exported the design for tasks including creating template previews,
        creating design and template thumbnails, or sending a design for
        [print](https://www.canva.com/print/).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `INTERNAL`

              **Available values:** The only valid value is `INTERNAL`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>
    </Tabs>
  </Prop>

  <Prop name="output_type" type="string" mode="output">
    The type of export.

    <Prop.Extras>
      **Available values:**

      * `PDF`
      * `JPG`
      * `PNG`
      * `PPTX`
      * `MP4`
      * `WEB`
      * `GIF`
      * `SVG`
      * `EMAIL`
      * `HTML`
      * `WEBSITE`
      * `DOCX`
      * `CSV`
      * `XLSX`
      * `WEBP`
    </Prop.Extras>
  </Prop>

  <Prop name="bulk_export_id" type="string" mode="output">
    The unique identifier for a bulk export operation. This ID will be shared across all exported resources that are part of the same bulk export operation.
  </Prop>
</Prop.List>

### Example

## Export a user's data and content in bulk

Note: This isn't a Data Subject Access Request (DSAR).

An `actor` triggers this event when they export personal data, uploads, and designs
from the **Login & Security** settings page.
A [team owner](https://www.canva.com/help/roles-and-permissions/) can also download their team's content.
For details, see [Canva Help: Downloading your personal data, uploads, and designs in bulk](https://www.canva.com/help/bulk-download-data-uploads-designs/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `EXPORT_BULK_DOWNLOAD`

      **Available values:** The only valid value is `EXPORT_BULK_DOWNLOAD`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Download a user's data and content in bulk

An `actor` triggers this event when they visit the page showing the download URL for their
bulk download request. This event doesn't record whether the user downloaded the content.

These download URLs are valid for 14 days after the user made the request.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `VIEW_BULK_DOWNLOAD_LINKS`

      **Available values:** The only valid value is `VIEW_BULK_DOWNLOAD_LINKS`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

