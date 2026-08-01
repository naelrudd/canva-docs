> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/print/llms.txt
> Use this file to discover all available pages before exploring further.

# Create order

Creates an order on the print partner's system. This operation lets Canva request a partner to commence production on an order.

As part of the request, Canva sends an `orderReferenceId` and a list of `items` to print.

Requests to this endpoint should be idempotent. If a provided `orderReferenceId` already exists in the partner system, and:

* The item `item_reference_id`s match and are not canceled: A success response should be returned.
* The item `item_reference_id`s match but items requested in the request are canceled: An error response should be returned.
* The item `item_reference_id`s don't match: An error response should be returned.

## HTTP method and URL path

POST https\://\{yourPrintApiUrl}/v1/orders

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

## Body parameters

<Prop.List>
  <Prop name="request_type" type="string" required>
    The type of request being made.

    <Prop.Extras>
      **Available values:** The only valid value is `create_order`.
    </Prop.Extras>
  </Prop>

  <Prop name="order" type="CreateOrder" required>
    Describes an order to create.

    <Tabs>
      <Tab name="pickup">
        Pickup order to create.

        <Prop.List>
          <Prop name="order_type" type="string" required>
            The type of order.

            <Prop.Extras>
              **Available values:** The only valid value is `pickup`.
            </Prop.Extras>
          </Prop>

          <Prop name="order_reference_id" type="string" required>
            A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

            <Prop.Extras>
              **Maximum length:** `255`
            </Prop.Extras>
          </Prop>

          <Prop name="items" type="CreateItem[]" required>
            Items to create.

            <Prop.Extras>
              **Minimum length:** `1`
            </Prop.Extras>

            <PillAccordion title={<>Properties of <strong>items</strong></>}>
              <Prop.List>
                <Prop name="item_reference_id" type="string" required>
                  A unique, case-sensitive ID for an order item that the partner can use when communicating with Canva.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="sku_reference" type="string" required>
                  Partner-facing reference for an item's SKU. Describes a specific variant of a product to be produced.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="artworks" type="Artwork[]" required>
                  The artworks of the item.

                  <Prop.Extras>
                    **Minimum length:** `1`
                  </Prop.Extras>

                  <PillAccordion title={<>Properties of <strong>artworks</strong></>}>
                    <Prop.List>
                      <Prop name="url" type="string" required>
                        A temporary URL for the partner to download a production-quality print file for an item.
                      </Prop>

                      <Prop name="print_area" type="string" required>
                        Where on a product an artwork file is expected to appear.

                        * `cover`
                        * `front`
                        * `back`
                        * `sheets`
                        * `none`

                        <Prop.Extras>
                          **Maximum length:** `255`
                        </Prop.Extras>
                      </Prop>

                      <Prop name="orientation" type="string" required>
                        The physical orientation of the file.

                        <Prop.Extras>
                          **Maximum length:** `255`

                          **Available values:**

                          * `portrait`
                          * `landscape`
                          * `square`
                        </Prop.Extras>
                      </Prop>

                      <Prop name="pages" type="integer">
                        The number of the pages in the file. Only provided for PDF.
                      </Prop>
                    </Prop.List>
                  </PillAccordion>
                </Prop>

                <Prop name="quantity" type="integer" required>
                  The number of copies of an item to produce.
                </Prop>

                <Prop name="attributes" type="object" required>
                  A key-value pair of attributes describing an item. These pairs complement the SKU by enumerating the unique attributes it describes. If used by the print partner, the expected values must be confirmed with Canva.

                  <PillAccordion title={<>Properties of <strong>attributes</strong></>}>
                    <Prop.List>
                      <Prop name="<KEY>" type="object of strings" required>
                        A key-value pair of attributes describing an item. These pairs complement the SKU by enumerating the unique attributes it describes. If used by the print partner, the expected values must be confirmed with Canva.

                        ```json
                        {
                          "paperFinish": "matte",
                          "paperType": "premium",
                          "productSize": "portrait"
                        }
                        ```
                      </Prop>
                    </Prop.List>
                  </PillAccordion>
                </Prop>

                <Prop name="add_on_sku_reference" type="string">
                  Partner-facing reference for an item add on SKU. Sometimes referred to as a stock item. For example, envelopes with postcards.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="mockup_url" type="string">
                  A temporary URL for the partner to download a mockup file displaying artwork imposed on a product for an item. This is included for certain products, generally apparel. This is controlled by Canva's internal product definition and not an API configuration.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="customer_details" type="CustomerDetails" required>
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

          <Prop name="preferred_production_location_reference" type="string" required>
            The reference ID for the preferred production location for the order. Partners can override this if the selected location is unsuitable, but partners must notify Canva through a production update if this occurs.

            <Prop.Extras>
              **Maximum length:** `255`
            </Prop.Extras>
          </Prop>

          <Prop name="pickup_location_reference" type="string" required>
            The reference ID for the pickup location of an order, as specified by the Canva user placing the order. Partners can't override this selection.

            <Prop.Extras>
              **Maximum length:** `255`
            </Prop.Extras>
          </Prop>

          <Prop name="pickup_tier" type="string">
            The pickup tier selected by the customer. Pickup tiers are Canva-defined values that describe different speeds and costs of pickup. Partners are expected to interpret this according to contractual agreements.
          </Prop>

          <Prop name="order_invoice_url" type="string">
            A temporary URL for the print partner to download an order invoice. This can be a taxation requirement for some countries. This is only included for certain partners, and can be configured in the API settings.
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="delivery">
        Delivery order to create.

        <Prop.List>
          <Prop name="order_type" type="string" required>
            The type of order.

            <Prop.Extras>
              **Available values:** The only valid value is `delivery`.
            </Prop.Extras>
          </Prop>

          <Prop name="order_reference_id" type="string" required>
            A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

            <Prop.Extras>
              **Maximum length:** `255`
            </Prop.Extras>
          </Prop>

          <Prop name="items" type="CreateItem[]" required>
            Items to create.

            <Prop.Extras>
              **Minimum length:** `1`
            </Prop.Extras>

            <PillAccordion title={<>Properties of <strong>items</strong></>}>
              <Prop.List>
                <Prop name="item_reference_id" type="string" required>
                  A unique, case-sensitive ID for an order item that the partner can use when communicating with Canva.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="sku_reference" type="string" required>
                  Partner-facing reference for an item's SKU. Describes a specific variant of a product to be produced.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="artworks" type="Artwork[]" required>
                  The artworks of the item.

                  <Prop.Extras>
                    **Minimum length:** `1`
                  </Prop.Extras>

                  <PillAccordion title={<>Properties of <strong>artworks</strong></>}>
                    <Prop.List>
                      <Prop name="url" type="string" required>
                        A temporary URL for the partner to download a production-quality print file for an item.
                      </Prop>

                      <Prop name="print_area" type="string" required>
                        Where on a product an artwork file is expected to appear.

                        * `cover`
                        * `front`
                        * `back`
                        * `sheets`
                        * `none`

                        <Prop.Extras>
                          **Maximum length:** `255`
                        </Prop.Extras>
                      </Prop>

                      <Prop name="orientation" type="string" required>
                        The physical orientation of the file.

                        <Prop.Extras>
                          **Maximum length:** `255`

                          **Available values:**

                          * `portrait`
                          * `landscape`
                          * `square`
                        </Prop.Extras>
                      </Prop>

                      <Prop name="pages" type="integer">
                        The number of the pages in the file. Only provided for PDF.
                      </Prop>
                    </Prop.List>
                  </PillAccordion>
                </Prop>

                <Prop name="quantity" type="integer" required>
                  The number of copies of an item to produce.
                </Prop>

                <Prop name="attributes" type="object" required>
                  A key-value pair of attributes describing an item. These pairs complement the SKU by enumerating the unique attributes it describes. If used by the print partner, the expected values must be confirmed with Canva.

                  <PillAccordion title={<>Properties of <strong>attributes</strong></>}>
                    <Prop.List>
                      <Prop name="<KEY>" type="object of strings" required>
                        A key-value pair of attributes describing an item. These pairs complement the SKU by enumerating the unique attributes it describes. If used by the print partner, the expected values must be confirmed with Canva.

                        ```json
                        {
                          "paperFinish": "matte",
                          "paperType": "premium",
                          "productSize": "portrait"
                        }
                        ```
                      </Prop>
                    </Prop.List>
                  </PillAccordion>
                </Prop>

                <Prop name="add_on_sku_reference" type="string">
                  Partner-facing reference for an item add on SKU. Sometimes referred to as a stock item. For example, envelopes with postcards.

                  <Prop.Extras>
                    **Maximum length:** `255`
                  </Prop.Extras>
                </Prop>

                <Prop name="mockup_url" type="string">
                  A temporary URL for the partner to download a mockup file displaying artwork imposed on a product for an item. This is included for certain products, generally apparel. This is controlled by Canva's internal product definition and not an API configuration.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>

          <Prop name="customer_details" type="CustomerDetails" required>
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

          <Prop name="delivery_address" type="Address" required>
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

          <Prop name="delivery_shipping_tier" type="string" required>
            The shipping tier selected by the customer. Shipping tiers are Canva-defined values that describe different speeds and costs of delivery. Partners are expected to interpret this according to contractual agreements. For example, `economy`, `standard` and `express`.
          </Prop>

          <Prop name="preferred_production_location_reference" type="string" required>
            The reference ID for the preferred production location for the order. Partners can override this if the selected location is unsuitable, but partners must notify Canva through a production update if this occurs.

            <Prop.Extras>
              **Maximum length:** `255`
            </Prop.Extras>
          </Prop>

          <Prop name="preferred_dispatch_location_reference" type="string" required>
            The reference ID for the preferred dispatch location for an order, as determined by Canva's internal routing. Partners can override this if the selected location is unsuitable, but partners must notify Canva through a production update if this occurs. Generally, this is the same as the preferred production location, but they are separated for future flexibility.

            <Prop.Extras>
              **Maximum length:** `255`
            </Prop.Extras>
          </Prop>

          <Prop name="order_invoice_url" type="string">
            A temporary URL for the print partner to download an order invoice. This can be a taxation requirement for some countries. This is only included for certain partners, and can be configured in the API settings.
          </Prop>
        </Prop.List>
      </Tab>
    </Tabs>
  </Prop>
</Prop.List>

## Example requests

### Create order: delivery, single item (invitation)

```json
{
  "request_type": "create_order",
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "delivery",
    "items": [
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "IN00030",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait",
            "pages": 2
          }
        ],
        "quantity": 50,
        "attributes": {}
      }
    ],
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "delivery_address": {
      "address_line1": "374 Johnson Ave, Brooklyn",
      "address_line2": "Unit 1",
      "city": "New York",
      "subdivision": "US-NY",
      "postcode": "11206",
      "country": "US"
    },
    "delivery_shipping_tier": "economy",
    "preferred_production_location_reference": "partnerLocation1234",
    "preferred_dispatch_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
  }
}
```

### Create order: delivery, single item (T-shirt)

```json
{
  "request_type": "create_order",
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "delivery",
    "items": [
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "TSHIRT_DELUXE_WHITE_MENS_M",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/JIB6bESKbphJ/9hi0gly7f7e016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "front",
            "orientation": "portrait"
          },
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "back",
            "orientation": "portrait"
          }
        ],
        "mockup_url": "https://print-prepress-file.canva.com/KIB6bRTYbphJ/325135e5c95c0161e2d3770dad48bba05db8c6ef2ef43e0d34c3612954f3f555.png?X-Amz-Algorithm=AWS4-HMAC-SHA256",
        "quantity": 1,
        "attributes": {}
      }
    ],
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "delivery_address": {
      "address_line1": "374 Johnson Ave, Brooklyn",
      "address_line2": "Unit 1",
      "city": "New York",
      "subdivision": "US-NY",
      "postcode": "11206",
      "country": "US"
    },
    "delivery_shipping_tier": "economy",
    "preferred_production_location_reference": "partnerLocation1234",
    "preferred_dispatch_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
  }
}
```

### Create order: delivery, single item (photobook)

```json
{
  "request_type": "create_order",
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "delivery",
    "items": [
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "PHBOOK_11X8.5IN_HARD-COVER_SOFT-TOUCH",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/JIB6bESKbphJ/9hi0gly7f7e016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "cover",
            "orientation": "portrait",
            "pages": 1
          },
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait",
            "pages": 20
          }
        ],
        "quantity": 1,
        "attributes": {}
      }
    ],
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "delivery_address": {
      "address_line1": "374 Johnson Ave, Brooklyn",
      "address_line2": "Unit 1",
      "city": "New York",
      "subdivision": "US-NY",
      "postcode": "11206",
      "country": "US"
    },
    "delivery_shipping_tier": "economy",
    "preferred_production_location_reference": "partnerLocation1234",
    "preferred_dispatch_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
  }
}
```

### Create order: delivery, single item (canvas)

```json
{
  "request_type": "create_order",
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "delivery",
    "items": [
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "CANVAS_PREMIUM_11X14IN_WOODGRAIN-FRAME",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait"
          }
        ],
        "quantity": 1,
        "attributes": {}
      }
    ],
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "delivery_address": {
      "address_line1": "374 Johnson Ave, Brooklyn",
      "address_line2": "Unit 1",
      "city": "New York",
      "subdivision": "US-NY",
      "postcode": "11206",
      "country": "US"
    },
    "delivery_shipping_tier": "economy",
    "preferred_production_location_reference": "partnerLocation1234",
    "preferred_dispatch_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
  }
}
```

### Create order: delivery, single item (invitations) with add ons (envelopes)

```json
{
  "request_type": "create_order",
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "delivery",
    "items": [
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "IN00030",
        "add_on_sku_reference": "EN00006",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait",
            "pages": 2
          }
        ],
        "quantity": 50,
        "attributes": {}
      }
    ],
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "delivery_address": {
      "address_line1": "374 Johnson Ave, Brooklyn",
      "address_line2": "Unit 1",
      "city": "New York",
      "subdivision": "US-NY",
      "postcode": "11206",
      "country": "US"
    },
    "delivery_shipping_tier": "economy",
    "preferred_production_location_reference": "partnerLocation1234",
    "preferred_dispatch_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
  }
}
```

### Create Order: delivery, multiple items (canvas and invitations)

```json
{
  "request_type": "create_order",
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "delivery",
    "items": [
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "CANVAS_PREMIUM_11X14IN_WOODGRAIN-FRAME",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait"
          }
        ],
        "quantity": 1,
        "attributes": {}
      },
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "IN00030",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait",
            "pages": 2
          }
        ],
        "quantity": 50,
        "attributes": {}
      }
    ],
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "delivery_address": {
      "address_line1": "374 Johnson Ave, Brooklyn",
      "address_line2": "Unit 1",
      "city": "New York",
      "subdivision": "US-NY",
      "postcode": "11206",
      "country": "US"
    },
    "delivery_shipping_tier": "economy",
    "preferred_production_location_reference": "partnerLocation1234",
    "preferred_dispatch_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
  }
}
```

### Create Order: delivery, multiple items (canvas and invitations) with add ons (envelopes)

```json
{
  "request_type": "create_order",
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "delivery",
    "items": [
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "CANVAS_PREMIUM_11X14IN_WOODGRAIN-FRAME",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait"
          }
        ],
        "quantity": 1,
        "attributes": {}
      },
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "IN00030",
        "add_on_sku_reference": "EN00006",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait",
            "pages": 2
          }
        ],
        "quantity": 50,
        "attributes": {}
      }
    ],
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "delivery_address": {
      "address_line1": "374 Johnson Ave, Brooklyn",
      "address_line2": "Unit 1",
      "city": "New York",
      "subdivision": "US-NY",
      "postcode": "11206",
      "country": "US"
    },
    "delivery_shipping_tier": "economy",
    "preferred_production_location_reference": "partnerLocation1234",
    "preferred_dispatch_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
  }
}
```

### Create order: pickup, single item (invitations)

```json
{
  "request_type": "create_order",
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "pickup",
    "items": [
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "IN00030",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait",
            "pages": 2
          }
        ],
        "quantity": 50,
        "attributes": {}
      }
    ],
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "preferred_production_location_reference": "partnerLocation1234",
    "pickup_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice"
  }
}
```

### Create order: pickup, single item (invitations) with add ons (envelopes)

```json
{
  "request_type": "create_order",
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "pickup",
    "items": [
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "IN00030",
        "add_on_sku_reference": "EN00006",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait",
            "pages": 2
          }
        ],
        "quantity": 50,
        "attributes": {}
      }
    ],
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "preferred_production_location_reference": "partnerLocation1234",
    "pickup_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice"
  }
}
```

### Create order: pickup, multiple items (invitations and canvas)

```json
{
  "request_type": "create_order",
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "pickup",
    "items": [
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "IN00030",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait",
            "pages": 2
          }
        ],
        "quantity": 50,
        "attributes": {}
      },
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "CANVAS_PREMIUM_11X14IN_WOODGRAIN-FRAME",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait"
          }
        ],
        "quantity": 1,
        "attributes": {}
      }
    ],
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "preferred_production_location_reference": "partnerLocation1234",
    "pickup_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice"
  }
}
```

### Create order: pickup, multiple items (invitations) with add ons (envelopes)

```json
{
  "request_type": "create_order",
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "pickup",
    "items": [
      {
        "item_reference_id": "FI123456789",
        "sku_reference": "IN00030",
        "add_on_sku_reference": "EN00006",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait",
            "pages": 2
          }
        ],
        "quantity": 50,
        "attributes": {}
      },
      {
        "item_reference_id": "FI987654321",
        "sku_reference": "IN00030",
        "artworks": [
          {
            "url": "https://print-prepress-file.canva.com/Sy55hyF6YuT_/16e9b4c0b2b7555552a0155555a5ac4d48bba05dbe053c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
            "print_area": "sheets",
            "orientation": "portrait",
            "pages": 2
          }
        ],
        "quantity": 50,
        "attributes": {}
      }
    ],
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "preferred_production_location_reference": "partnerLocation1234",
    "pickup_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice"
  }
}
```

## Success response

If successful, the endpoint returns a `201` response with a JSON body with the following parameters:

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

### Delivery order, single item (invitation)

```json
{
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "delivery",
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
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
      "address_line2": "Unit 1",
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
    "updated_at": 1726448251
  }
}
```

### Delivery order, single item (invitation) with add ons (envelopes)

```json
{
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "delivery",
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "items": [
      {
        "item_reference_id": "FI123456789",
        "status": "received",
        "sku_reference": "IN00030",
        "add_on_sku_reference": "EN00006",
        "quantity": 50
      }
    ],
    "delivery_address": {
      "address_line1": "374 Johnson Ave, Brooklyn",
      "address_line2": "Unit 1",
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
    "updated_at": 1726448251
  }
}
```

### Delivery order, multiple items (invitation and canvas) with add ons (envelopes)

```json
{
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "delivery",
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "items": [
      {
        "item_reference_id": "FI123456789",
        "status": "received",
        "sku_reference": "IN00030",
        "add_on_sku_reference": "EN00006",
        "quantity": 50
      },
      {
        "item_reference_id": "FI987654321",
        "status": "received",
        "sku_reference": "CANVAS_PREMIUM_16X20_STRETCHED",
        "quantity": 5
      }
    ],
    "delivery_address": {
      "address_line1": "374 Johnson Ave, Brooklyn",
      "address_line2": "Unit 1",
      "city": "New York",
      "subdivision": "US-NY",
      "postcode": "11206",
      "country": "US"
    },
    "delivery_shipping_tier": "economy",
    "production_location_reference": "partnerLocation1234",
    "dispatch_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf",
    "created_at": 1726448251,
    "updated_at": 1726448251
  }
}
```

### Pickup order, single item (invitation)

```json
{
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "pickup",
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
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
    "updated_at": 1726448251
  }
}
```

### Pickup order, single item (invitation) with add ons (envelopes)

```json
{
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "pickup",
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "items": [
      {
        "item_reference_id": "FI123456789",
        "status": "received",
        "sku_reference": "IN00030",
        "add_on_sku_reference": "EN00006",
        "quantity": 50
      }
    ],
    "production_location_reference": "partnerLocation1234",
    "pickup_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice",
    "created_at": 1726448251,
    "updated_at": 1726448251
  }
}
```

### Pickup order, multiple items (invitation and canvas) with add ons (envelopes)

```json
{
  "order": {
    "order_reference_id": "FB123456789",
    "order_type": "pickup",
    "customer_details": {
      "name": "Charles Boyle",
      "phone": "(555) 555-1234",
      "email": "charlesboyle@email.com"
    },
    "items": [
      {
        "item_reference_id": "FI123456789",
        "status": "received",
        "sku_reference": "IN00030",
        "add_on_sku_reference": "EN00006",
        "quantity": 50
      },
      {
        "item_reference_id": "FI987654321",
        "status": "received",
        "sku_reference": "CANVAS_PREMIUM_16X20_STRETCHED",
        "quantity": 5
      }
    ],
    "production_location_reference": "partnerLocation1234",
    "pickup_location_reference": "partnerLocation1234",
    "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice",
    "created_at": 1726448251,
    "updated_at": 1726448251
  }
}
```

## Error responses

### 400 Bad Request. For example, an invalid payload format.

### 401 Unauthorized. For example, an invalid signature.
