> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/print/llms.txt
> Use this file to discover all available pages before exploring further.

# Update order

Updates an order in the print partner's system.

* Changes to an order are restricted only to the delivery address and customer details of the order.
* Updates to an order aren't allowed if every item of the order has been canceled.
* The order update request can be denied if the update isn't possible. For example, if the order contains items that have already shipped.

## HTTP method and URL path

PATCH https\://\{yourPrintApiUrl}/v1/orders/\{orderReferenceId}

## Header parameters

<Prop.List>
  <Prop name="Content-Type" type="string" required>
    Indicates the media type of the information sent in the request. This must be set to `application/json`.

    For example: `Content-Type: application/json`
  </Prop>

  <Prop name="X-Canva-Public-Api-Version" type="string">
    The version of the Canva Print API used in the request. If not specified, the latest version is assumed.
  </Prop>

  <Prop name="X-Canva-Signature" type="string" required>
    The Canva request signature. This is used to verify the request is legitimate and was not tampered with in transit.
  </Prop>
</Prop.List>

## Path parameters

<Prop.List>
  <Prop name="orderReferenceId" type="string" required>
    Unique, case-sensitive string identifying the order in Canva's system.
  </Prop>
</Prop.List>

## Body parameters

<Prop.List>
  <Prop name="request_type" type="string" required>
    The type of request being made.

    <Prop.Extras>
      **Available values:** The only valid value is `update_order`.
    </Prop.Extras>
  </Prop>

  <Prop name="order_reference_id" type="string" required>
    A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

    <Prop.Extras>
      **Maximum length:** `255`
    </Prop.Extras>
  </Prop>

  <Prop name="updates" type="Updates" required>
    Updates to the order. The request must contain at least one of `customer_details` or `delivery_address`.

    <PillAccordion title={<>Properties of <strong>updates</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="customer_details" type="CustomerDetails">
          The customer.

          <PillAccordion title={<>Properties of <strong>customer_details</strong></>}>
            <Prop.List>
              <Prop name="name" type="string" required>
                The full name of the customer.

                <Prop.Extras>
                  **Maximum length:** `255`
                </Prop.Extras>
              </Prop>

              <Prop name="phone" type="string" required>
                The phone number of the customer.

                <Prop.Extras>
                  **Maximum length:** `255`
                </Prop.Extras>
              </Prop>

              <Prop name="email" type="string" required>
                The email address of the customer.

                <Prop.Extras>
                  **Maximum length:** `255`
                </Prop.Extras>
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="delivery_address" type="Address">
          An address.

          <PillAccordion title={<>Properties of <strong>delivery_address</strong></>}>
            <Prop.List>
              <Prop name="address_line1" type="string" required>
                The address line 1 portion of the address.

                <Prop.Extras>
                  **Maximum length:** `255`
                </Prop.Extras>
              </Prop>

              <Prop name="city" type="string" required>
                The city portion of the address.

                <Prop.Extras>
                  **Maximum length:** `255`
                </Prop.Extras>
              </Prop>

              <Prop name="country" type="string" required>
                ISO 3166-1 alpha-2 country code of the address. Includes the exceptionally reserved code IC for the autonomous Spanish region Canary Islands.

                <Prop.Extras>
                  **Maximum length:** `2`
                </Prop.Extras>
              </Prop>

              <Prop name="address_line2" type="string">
                The address line 2 portion of the address. Can contain additional address information such as unit number or house name.

                <Prop.Extras>
                  **Maximum length:** `255`
                </Prop.Extras>
              </Prop>

              <Prop name="subdivision" type="string">
                ISO 3166-2 subdivision code of the address.

                <Prop.Extras>
                  **Maximum length:** `6`
                </Prop.Extras>
              </Prop>

              <Prop name="postcode" type="string">
                The postcode/zipcode portion of the address.

                <Prop.Extras>
                  **Maximum length:** `12`
                </Prop.Extras>
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

## Example requests

### Update customer details and delivery address for a delivery order

```json
{
  "request_type": "update_order",
  "order_reference_id": "FB123456789",
  "updates": {
    "customer_details": {
      "name": "NotCharles Boyle",
      "phone": "(555) 555-0000",
      "email": "notcharlesboyle@email.com"
    },
    "delivery_address": {
      "address_line1": "374 Johnson Ave, Brooklyn",
      "address_line2": "Unit 2",
      "city": "New York",
      "subdivision": "US-NY",
      "postcode": "11206",
      "country": "US"
    }
  }
}
```

### Update customer details for a pickup order

```json
{
  "request_type": "update_order",
  "order_reference_id": "FB123456789",
  "updates": {
    "customer_details": {
      "name": "NotCharles Boyle",
      "phone": "(555) 555-0000",
      "email": "notcharlesboyle@email.com"
    }
  }
}
```

## Success response

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

<Prop.List>
  <Prop name="order" type="Order" required mode="output">
    An order.

    <Tabs>
      <Tab name="pickup">
        An order that will be picked up from a location by the customer.

        <Prop.List>
          <Prop name="order_type" type="string" required mode="output">
            The type of order.

            <Prop.Extras>
              **Available values:** The only valid value is `pickup`.
            </Prop.Extras>
          </Prop>

          <Prop name="order_reference_id" type="string" required mode="output">
            A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

            <Prop.Extras>
              **Maximum length:** `255`
            </Prop.Extras>
          </Prop>

          <Prop name="items" type="Item[]" required mode="output">
            The items in the order.

            <Prop.Extras>
              **Minimum length:** `1`
            </Prop.Extras>

            <PillAccordion title={<>Properties of <strong>items</strong></>}>
              <Prop.List>
                <Prop name="item_reference_id" type="string" required mode="output">
                  A unique, case-sensitive ID for an order item that the partner can use when communicating with Canva.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="status" type="string" required mode="output">
                  The updated production status of the item.

                  <Prop.Extras>
                    **Available values:**

                    * `received`: The order item was received and is pending further processing.
                    * `producing`: The order item production has started.
                    * `produced`: The order item production has completed.
                    * `packaging`: The order item packaging has started.
                    * `ready_for_pickup`: The order item was shipped to the receiver.
                    * `picked_up`: The order item is ready for pickup in store.
                    * `shipped`: The order item was picked up from the store.
                    * `canceled`: The order item was canceled.
                  </Prop.Extras>
                </Prop>

                <Prop name="sku_reference" type="string" required mode="output">
                  Partner-facing reference for an item's SKU. Describes a specific variant of a product to be produced.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="quantity" type="integer" required mode="output">
                  The number of copies of an item to produce.
                </Prop>

                <Prop name="add_on_sku_reference" type="string" mode="output">
                  Partner-facing reference for an item add on SKU. Sometimes referred to as a stock item. For example, envelopes with postcards.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="error_details" type="ErrorDetails" mode="output">
                  The error details of the item. Errors details should be cleared from an item after it has been resolved.

                  <PillAccordion title={<>Properties of <strong>error_details</strong></>}>
                    <Prop.List>
                      <Prop name="issue_origin" type="string" required mode="output">
                        The origin of the issue.

                        <Prop.Extras>
                          **Available values:**

                          * `production`
                          * `order_url`
                          * `user_details`
                          * `user_address`
                          * `delivery`
                          * `unknown`
                        </Prop.Extras>
                      </Prop>

                      <Prop name="description" type="string" required mode="output">
                        A human readable message that describes the cause of the error.

                        <Prop.Extras>
                          **Maximum length:** `255`
                        </Prop.Extras>
                      </Prop>
                    </Prop.List>
                  </PillAccordion>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="customer_details" type="CustomerDetails" required mode="output">
            The customer.

            <PillAccordion title={<>Properties of <strong>customer_details</strong></>}>
              <Prop.List>
                <Prop name="name" type="string" required mode="output">
                  The full name of the customer.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="phone" type="string" required mode="output">
                  The phone number of the customer.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="email" type="string" required mode="output">
                  The email address of the customer.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="production_location_reference" type="string" required mode="output">
            The reference ID for the production location of the order.

            <Prop.Extras>
              **Maximum length:** `255`
            </Prop.Extras>
          </Prop>

          <Prop name="pickup_location_reference" type="string" required mode="output">
            The reference ID for the pickup location of an order, as specified by the Canva user placing the order.

            <Prop.Extras>
              **Maximum length:** `255`
            </Prop.Extras>
          </Prop>

          <Prop name="created_at" type="integer" required mode="output">
            When the order was created, as a Unix timestamp (in seconds since the Unix Epoch).
          </Prop>

          <Prop name="updated_at" type="integer" required mode="output">
            When the order was last updated, as a Unix timestamp (in seconds since the Unix Epoch).
          </Prop>

          <Prop name="pickup_tier" type="string" mode="output">
            The pickup tier selected by the customer. Pickup tiers are Canva-defined values that describe different speeds and costs of pickup. Partners are expected to interpret this according to contractual agreements.
          </Prop>

          <Prop name="order_invoice_url" type="string" mode="output">
            A temporary URL for the print partner to download an order invoice. This can be a taxation requirement for some countries. This is only included for certain partners, and can be configured in the API settings.
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="delivery">
        An order that will be delivered to the customer.

        <Prop.List>
          <Prop name="order_type" type="string" required mode="output">
            The type of order.

            <Prop.Extras>
              **Available values:** The only valid value is `delivery`.
            </Prop.Extras>
          </Prop>

          <Prop name="order_reference_id" type="string" required mode="output">
            A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

            <Prop.Extras>
              **Maximum length:** `255`
            </Prop.Extras>
          </Prop>

          <Prop name="items" type="Item[]" required mode="output">
            The Items in the order.

            <Prop.Extras>
              **Minimum length:** `1`
            </Prop.Extras>

            <PillAccordion title={<>Properties of <strong>items</strong></>}>
              <Prop.List>
                <Prop name="item_reference_id" type="string" required mode="output">
                  A unique, case-sensitive ID for an order item that the partner can use when communicating with Canva.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="status" type="string" required mode="output">
                  The updated production status of the item.

                  <Prop.Extras>
                    **Available values:**

                    * `received`: The order item was received and is pending further processing.
                    * `producing`: The order item production has started.
                    * `produced`: The order item production has completed.
                    * `packaging`: The order item packaging has started.
                    * `ready_for_pickup`: The order item was shipped to the receiver.
                    * `picked_up`: The order item is ready for pickup in store.
                    * `shipped`: The order item was picked up from the store.
                    * `canceled`: The order item was canceled.
                  </Prop.Extras>
                </Prop>

                <Prop name="sku_reference" type="string" required mode="output">
                  Partner-facing reference for an item's SKU. Describes a specific variant of a product to be produced.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="quantity" type="integer" required mode="output">
                  The number of copies of an item to produce.
                </Prop>

                <Prop name="add_on_sku_reference" type="string" mode="output">
                  Partner-facing reference for an item add on SKU. Sometimes referred to as a stock item. For example, envelopes with postcards.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="error_details" type="ErrorDetails" mode="output">
                  The error details of the item. Errors details should be cleared from an item after it has been resolved.

                  <PillAccordion title={<>Properties of <strong>error_details</strong></>}>
                    <Prop.List>
                      <Prop name="issue_origin" type="string" required mode="output">
                        The origin of the issue.

                        <Prop.Extras>
                          **Available values:**

                          * `production`
                          * `order_url`
                          * `user_details`
                          * `user_address`
                          * `delivery`
                          * `unknown`
                        </Prop.Extras>
                      </Prop>

                      <Prop name="description" type="string" required mode="output">
                        A human readable message that describes the cause of the error.

                        <Prop.Extras>
                          **Maximum length:** `255`
                        </Prop.Extras>
                      </Prop>
                    </Prop.List>
                  </PillAccordion>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="customer_details" type="CustomerDetails" required mode="output">
            The customer.

            <PillAccordion title={<>Properties of <strong>customer_details</strong></>}>
              <Prop.List>
                <Prop name="name" type="string" required mode="output">
                  The full name of the customer.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="phone" type="string" required mode="output">
                  The phone number of the customer.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="email" type="string" required mode="output">
                  The email address of the customer.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="delivery_address" type="Address" required mode="output">
            An address.

            <PillAccordion title={<>Properties of <strong>delivery_address</strong></>}>
              <Prop.List>
                <Prop name="address_line1" type="string" required mode="output">
                  The address line 1 portion of the address.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="city" type="string" required mode="output">
                  The city portion of the address.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="country" type="string" required mode="output">
                  ISO 3166-1 alpha-2 country code of the address. Includes the exceptionally reserved code IC for the autonomous Spanish region Canary Islands.

                  <Prop.Extras>
                    **Maximum length:** `2`
                  </Prop.Extras>
                </Prop>

                <Prop name="address_line2" type="string" mode="output">
                  The address line 2 portion of the address. Can contain additional address information such as unit number or house name.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="subdivision" type="string" mode="output">
                  ISO 3166-2 subdivision code of the address.

                  <Prop.Extras>
                    **Maximum length:** `6`
                  </Prop.Extras>
                </Prop>

                <Prop name="postcode" type="string" mode="output">
                  The postcode/zipcode portion of the address.

                  <Prop.Extras>
                    **Maximum length:** `12`
                  </Prop.Extras>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="delivery_shipping_tier" type="string" required mode="output">
            The shipping tier selected by the customer. Shipping tiers are Canva-defined values that describe different speeds and costs of delivery. Partners are expected to interpret this according to contractual agreements. For example, `economy`, `standard` and `express`.
          </Prop>

          <Prop name="production_location_reference" type="string" required mode="output">
            The reference ID for the production location of the order.

            <Prop.Extras>
              **Maximum length:** `255`
            </Prop.Extras>
          </Prop>

          <Prop name="dispatch_location_reference" type="string" required mode="output">
            The reference ID for the dispatch location for the order.

            <Prop.Extras>
              **Maximum length:** `255`
            </Prop.Extras>
          </Prop>

          <Prop name="created_at" type="integer" required mode="output">
            When the order was created, as a Unix timestamp (in seconds since the Unix Epoch).
          </Prop>

          <Prop name="updated_at" type="integer" required mode="output">
            When the order was last updated, as a Unix timestamp (in seconds since the Unix Epoch).
          </Prop>

          <Prop name="shipments" type="Shipment[]" mode="output">
            A list of shipments for the order.

            <PillAccordion title={<>Properties of <strong>shipments</strong></>}>
              <Prop.List>
                <Prop name="items" type="ShipmentItem[]" required mode="output">
                  The items included in the shipment.

                  <Prop.Extras>
                    **Minimum length:** `1`
                  </Prop.Extras>

                  <PillAccordion title={<>Properties of <strong>items</strong></>}>
                    <Prop.List>
                      <Prop name="item_reference_id" type="string" required mode="output">
                        A unique, case-sensitive ID for an order item that the partner can use when communicating with Canva.

                        <Prop.Extras>
                          **Maximum length:** `255`
                        </Prop.Extras>
                      </Prop>

                      <Prop name="quantity" type="integer" required mode="output">
                        The number of copies of an item that were shipped.
                      </Prop>
                    </Prop.List>
                  </PillAccordion>
                </Prop>

                <Prop name="tracking_number" type="string" mode="output">
                  The tracking number provided by the carrier.

                  <Prop.Extras>
                    **Minimum length:** `1`

                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="carrier" type="string" mode="output">
                  The Canva-supported carrier delivering the shipment.

                  <Prop.Extras>
                    **Available values:**

                    * `allied_express`
                    * `allwayex`
                    * `amazon`
                    * `ams`
                    * `asendia`
                    * `aus_post`
                    * `b2c`
                    * `blue_dart`
                    * `bpost`
                    * `bring`
                    * `bring_no`
                    * `brt`
                    * `canada_post`
                    * `carriers`
                    * `chitchats`
                    * `chronopost`
                    * `colissimo`
                    * `correios`
                    * `correos`
                    * `correos_express`
                    * `couriers_please`
                    * `deutsche_post`
                    * `dhl`
                    * `dpd`
                    * `dpd_uk`
                    * `estafeta`
                    * `evri`
                    * `fastway`
                    * `fedex`
                    * `fleet_optics`
                    * `gls`
                    * `hunter_express`
                    * `ics`
                    * `icumulus`
                    * `india_post`
                    * `japan_post`
                    * `landmark_global`
                    * `laposte`
                    * `loomis_express`
                    * `lotte`
                    * `nacex`
                    * `new_zealand_post`
                    * `newzealand_couriers`
                    * `norsk_global`
                    * `paquetexpress`
                    * `parcel_force`
                    * `pitney_bowes`
                    * `planzer`
                    * `post_nl`
                    * `post_nord`
                    * `purolator`
                    * `qxpress`
                    * `royal_mail`
                    * `sagawa`
                    * `sda`
                    * `seur`
                    * `shiprocket`
                    * `spring_gds`
                    * `star_track`
                    * `swiss_post`
                    * `tnt`
                    * `toll`
                    * `uniuni`
                    * `ups`
                    * `usps`
                    * `yamato`
                  </Prop.Extras>
                </Prop>

                <Prop name="dispatched_at" type="integer" mode="output">
                  When the shipment was dispatched, as a Unix timestamp (in seconds since the Unix Epoch).
                </Prop>

                <Prop name="dispatch_location_reference" type="string" mode="output">
                  The location ID of where the shipment was dispatched.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="order_invoice_url" type="string" mode="output">
            A temporary URL for the print partner to download an order invoice. This can be a taxation requirement for some countries. This is only included for certain partners, and can be configured in the API settings.
          </Prop>
        </Prop.List>
      </Tab>
    </Tabs>
  </Prop>
</Prop.List>

## Example responses

### Update customer details and delivery address for a delivery order

```json
{
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "delivery",
    "customer_details": {
      "name": "NotCharles Boyle",
      "phone": "(555) 555-0000",
      "email": "notcharlesboyle@email.com"
    },
    "items": [
      {
        "item_reference_id": "FI123456789",
        "status": "received",
        "sku_reference": "IN00030",
        "quantity": 50
      }
    ],
    "delivery_address": {
      "address_line1": "374 Johnson Ave, Brooklyn",
      "address_line2": "Unit 2",
      "city": "New York",
      "subdivision": "US-NY",
      "postcode": "11206",
      "country": "US"
    },
    "delivery_shipping_tier": "economy",
    "production_location_reference": "partnerLocation1234",
    "dispatch_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice",
    "created_at": 1726448251,
    "updated_at": 1726449800
  }
}
```

### Update customer details for a pickup order

```json
{
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "pickup",
    "customer_details": {
      "name": "NotCharles Boyle",
      "phone": "(555) 555-0000",
      "email": "notcharlesboyle@email.com"
    },
    "items": [
      {
        "item_reference_id": "FI123456789",
        "status": "received",
        "sku_reference": "IN00030",
        "quantity": 50
      }
    ],
    "production_location_reference": "partnerLocation1234",
    "pickup_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice",
    "created_at": 1726448251,
    "updated_at": 1726449800
  }
}
```

## Error responses

### 400 Bad Request. For example, an invalid payload format.

### 401 Unauthorized. For example, an invalid signature.

### 403 Forbidden. For example, an idempotent order issue, or the order doesn't exist.

### 405 Not Allowed. For example, the request isn't allowed because of the order state, or it isn't supported or implemented.
