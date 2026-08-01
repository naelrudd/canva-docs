> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/print/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

<Changelog>
  <ChangelogEntry date="2026-07-15">
    * The list of available carriers has been updated.

      These values have been added: `planzer`.
  </ChangelogEntry>

  <ChangelogEntry date="2026-07-13">
    * The list of available carriers has been updated.

      These values have been added: `bring`, `brt`, `colissimo`, `nacex`, `shiprocket`.
  </ChangelogEntry>

  <ChangelogEntry date="2026-06-15">
    * The list of available carriers has been updated.

      These values have been added: `new_zealand_post`.
  </ChangelogEntry>

  <ChangelogEntry date="2026-05-08">
    * The description of the `delivery_shipping_tier` field has been updated to remove the list of available values.

      This is to allow for additional shipping tiers based on contractual agreements to be sent in the future.
      There should be no changes for existing integrations.

    * A `pickup_tier` field has been introduced as an optional field on `CreateOrder` and `Order` for pickup orders.

      This is to allow for additional pickup tiers based on contractual agreements to be sent in the future.
      There should be no changes for existing integrations.

    * The example URLs for item `mockup_url` and artworks have been updated with realistic Canva URLs.
  </ChangelogEntry>

  <ChangelogEntry date="2026-04-07">
    * The list of available carriers has been updated.

      These values have been added: `japan_post`.
  </ChangelogEntry>

  <ChangelogEntry date="2026-02-11">
    * The title for the 'Get Locations' operation has been renamed to 'Find Locations'. The `operationId` in the OpenAPI description has also been renamed.
  </ChangelogEntry>

  <ChangelogEntry date="2026-01-16">
    * The list of available carriers has been updated.

      These values have been added: `norsk_global`.
  </ChangelogEntry>

  <ChangelogEntry date="2025-12-29">
    * The example requests for the [Create order API](https://www.canva.dev/docs/print/api-reference/requests-from-canva/create-order/) have been updated to remove the properties in the `attributes` object.

      This is to reduce confusion because the attribute values may differ per integration.
  </ChangelogEntry>

  <ChangelogEntry date="2025-10-16">
    * The description of the `country` field has been updated to include the exceptionally reserved ISO 3166-2 alpha-2 code IC for the autonomous Spanish region Canary Islands.
  </ChangelogEntry>

  <ChangelogEntry date="2025-10-02">
    * The list of available carriers has been updated.

      These values have been added: `fleet_optics`, `newzealand_couriers`.
  </ChangelogEntry>

  <ChangelogEntry date="2025-09-29">
    * The list of available carriers has been updated.

      These values have been added: `uniuni`.
  </ChangelogEntry>

  <ChangelogEntry date="2025-09-19">
    * Description updated to mention the valid order type for `ready_for_pickup` and `picked_up` item status updates.

    * The list of available carriers has been updated.

      These values have been added: `amazon`.
  </ChangelogEntry>

  <ChangelogEntry date="2025-09-10">
    * Single item and Multi item example requests for order production events have been updated.

      The new examples remove an incorrect `example` object from the request body.
  </ChangelogEntry>

  <ChangelogEntry date="2025-09-04">
    * The list of available carriers has been updated.

      These values have been added: `chronopost`.
  </ChangelogEntry>

  <ChangelogEntry date="2025-08-12">
    * The maximum length of the continuation field in a response has been updated from 10 characters to 255.
  </ChangelogEntry>

  <ChangelogEntry date="2025-07-18">
    * Additional examples for order error, shipment and production events have been added.

      The new examples show multiple items in the request body.
  </ChangelogEntry>

  <ChangelogEntry date="2025-06-18">
    * The order examples have been updated.

      Some properties were incorrectly shown as numbers instead of strings. For example, postcode shown as `2017` instead of `"2017"`.

      These examples have been fixed to now show as strings.

    * The example cost summary events have been updated.

      The previous monetary values were incorrectly shown as numbers instead of strings, and one cost summary example had `total_major_unit` instead of `total_major_units`.

      All cost summary event examples now have the correct monetary values and the correct labels.
  </ChangelogEntry>

  <ChangelogEntry date="2025-04-29">
    * The example cost summary events have been updated.

      The previous values incorrectly showed that the `request_type` was `cost_summary` instead of `cost_summary_event`.

      All cost summary event examples now have the correct `request_type` value `cost_summary_event`.
  </ChangelogEntry>

  <ChangelogEntry date="2025-04-16">
    * The list of available carriers has been updated.

      These values have been removed: `dhl_express`, `dhl_us`, `quorier`, `major_express`.

      These values have been added: `correos`, `correos_express`, `gls`, `landmark_global`, `evri`, `spring_gds`, `chitchats`.
  </ChangelogEntry>

  <ChangelogEntry date="2025-04-14">
    **New API version: <Badge size="large" tone="feedbackWarnSubtle">2025-04-14</Badge>**

    * Initial release of the Print API.
  </ChangelogEntry>
</Changelog>
