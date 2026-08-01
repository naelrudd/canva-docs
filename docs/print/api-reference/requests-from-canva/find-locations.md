> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/print/llms.txt
> Use this file to discover all available pages before exploring further.

# Find locations

Gets up-to-date information on the print partner's locations that support in-store pickup.

Canva is interested in:

* The address of each pickup location.
* Production and transfer locations that supply to each pickup location.
* The opening hours of each pickup location.

## HTTP method and URL path

GET https\://\{yourPrintApiUrl}/locations

## Header parameters

<Prop.List>
  <Prop name="X-Canva-Public-Api-Version" type="string">
    The version of the Canva Print API used in the request. If not specified, the latest version is assumed.
  </Prop>

  <Prop name="X-Canva-Signature" type="string" required>
    The Canva request signature. This is used to verify the request is legitimate and was not tampered with in transit.
  </Prop>
</Prop.List>

## Query parameters

<Prop.List>
  <Prop name="country" type="string">
    The ISO 3166-1 alpha-2 country code to filter the returned partner locations.
  </Prop>

  <Prop name="continuation" type="string">
    If the success response contains a continuation token, the list contains more items you can list. You can use this token as a query parameter and retrieve more items from the list.

    To retrieve all items, you might need to make multiple requests.
  </Prop>

  <Prop name="limit" type="integer" required>
    The limit for the number of results to return. If the available items are more than the limit, then the response will include a continuation token.
  </Prop>
</Prop.List>

## Success response

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

<Prop.List>
  <Prop name="locations" type="PickupLocation[]" required mode="output">
    List of pickup locations currently available for the partner.

    <PillAccordion title={<>Properties of <strong>locations</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The internal reference of the location on the partners system.

          <Prop.Extras>
            **Maximum length:** `255`
          </Prop.Extras>
        </Prop>

        <Prop name="display_name" type="string" required mode="output">
          The display name of the location. This is what Canva customers can expect the location to be called.

          <Prop.Extras>
            **Maximum length:** `255`
          </Prop.Extras>
        </Prop>

        <Prop name="phone" type="string" required mode="output">
          The contact phone number of the location.

          <Prop.Extras>
            **Maximum length:** `255`
          </Prop.Extras>
        </Prop>

        <Prop name="timezone" type="string" required mode="output">
          The timezone of the location in tz format.

          <Prop.Extras>
            **Maximum length:** `255`
          </Prop.Extras>
        </Prop>

        <Prop name="address" type="Address" required mode="output">
          An address.

          <PillAccordion title={<>Properties of <strong>address</strong></>}>
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

        <Prop name="geolocation" type="Geolocation" required mode="output">
          Longitude and latitude of a location.

          <PillAccordion title={<>Properties of <strong>geolocation</strong></>}>
            <Prop.List>
              <Prop name="latitude" type="number" required mode="output">
                The latitude of the geolocation.

                <Prop.Extras>
                  **Minimum:** `-90`

                  **Maximum:** `90`
                </Prop.Extras>
              </Prop>

              <Prop name="longitude" type="number" required mode="output">
                The longitude of the geolocation.

                <Prop.Extras>
                  **Minimum:** `-180`

                  **Maximum:** `180`
                </Prop.Extras>
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="pickup_hours" type="PickupHours" required mode="output">
          Pickup hours for a pickup location. If hours do not exist for a day, the store is considered closed.

          <PillAccordion title={<>Properties of <strong>pickup_hours</strong></>}>
            <Prop.List>
              <Prop name="monday_hours" type="Hours" mode="output">
                Details on the opening and closing time for a pickup location.

                The open time must be before close time. Hours must be open for at least a minute.

                <PillAccordion title={<>Properties of <strong>monday_hours</strong></>}>
                  <Prop.List>
                    <Prop name="open_time_hour" type="integer" required mode="output">
                      The hour part of the time the store opens in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="open_time_minute" type="integer" required mode="output">
                      The minute part of the time the store opens.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_hour" type="integer" required mode="output">
                      The hour part of the time the store closes in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_minute" type="integer" required mode="output">
                      The minute part of the time the store closes.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>
                  </Prop.List>
                </PillAccordion>
              </Prop>

              <Prop name="tuesday_hours" type="Hours" mode="output">
                Details on the opening and closing time for a pickup location.

                The open time must be before close time. Hours must be open for at least a minute.

                <PillAccordion title={<>Properties of <strong>tuesday_hours</strong></>}>
                  <Prop.List>
                    <Prop name="open_time_hour" type="integer" required mode="output">
                      The hour part of the time the store opens in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="open_time_minute" type="integer" required mode="output">
                      The minute part of the time the store opens.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_hour" type="integer" required mode="output">
                      The hour part of the time the store closes in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_minute" type="integer" required mode="output">
                      The minute part of the time the store closes.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>
                  </Prop.List>
                </PillAccordion>
              </Prop>

              <Prop name="wednesday_hours" type="Hours" mode="output">
                Details on the opening and closing time for a pickup location.

                The open time must be before close time. Hours must be open for at least a minute.

                <PillAccordion title={<>Properties of <strong>wednesday_hours</strong></>}>
                  <Prop.List>
                    <Prop name="open_time_hour" type="integer" required mode="output">
                      The hour part of the time the store opens in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="open_time_minute" type="integer" required mode="output">
                      The minute part of the time the store opens.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_hour" type="integer" required mode="output">
                      The hour part of the time the store closes in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_minute" type="integer" required mode="output">
                      The minute part of the time the store closes.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>
                  </Prop.List>
                </PillAccordion>
              </Prop>

              <Prop name="thursday_hours" type="Hours" mode="output">
                Details on the opening and closing time for a pickup location.

                The open time must be before close time. Hours must be open for at least a minute.

                <PillAccordion title={<>Properties of <strong>thursday_hours</strong></>}>
                  <Prop.List>
                    <Prop name="open_time_hour" type="integer" required mode="output">
                      The hour part of the time the store opens in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="open_time_minute" type="integer" required mode="output">
                      The minute part of the time the store opens.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_hour" type="integer" required mode="output">
                      The hour part of the time the store closes in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_minute" type="integer" required mode="output">
                      The minute part of the time the store closes.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>
                  </Prop.List>
                </PillAccordion>
              </Prop>

              <Prop name="friday_hours" type="Hours" mode="output">
                Details on the opening and closing time for a pickup location.

                The open time must be before close time. Hours must be open for at least a minute.

                <PillAccordion title={<>Properties of <strong>friday_hours</strong></>}>
                  <Prop.List>
                    <Prop name="open_time_hour" type="integer" required mode="output">
                      The hour part of the time the store opens in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="open_time_minute" type="integer" required mode="output">
                      The minute part of the time the store opens.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_hour" type="integer" required mode="output">
                      The hour part of the time the store closes in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_minute" type="integer" required mode="output">
                      The minute part of the time the store closes.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>
                  </Prop.List>
                </PillAccordion>
              </Prop>

              <Prop name="saturday_hours" type="Hours" mode="output">
                Details on the opening and closing time for a pickup location.

                The open time must be before close time. Hours must be open for at least a minute.

                <PillAccordion title={<>Properties of <strong>saturday_hours</strong></>}>
                  <Prop.List>
                    <Prop name="open_time_hour" type="integer" required mode="output">
                      The hour part of the time the store opens in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="open_time_minute" type="integer" required mode="output">
                      The minute part of the time the store opens.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_hour" type="integer" required mode="output">
                      The hour part of the time the store closes in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_minute" type="integer" required mode="output">
                      The minute part of the time the store closes.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>
                  </Prop.List>
                </PillAccordion>
              </Prop>

              <Prop name="sunday_hours" type="Hours" mode="output">
                Details on the opening and closing time for a pickup location.

                The open time must be before close time. Hours must be open for at least a minute.

                <PillAccordion title={<>Properties of <strong>sunday_hours</strong></>}>
                  <Prop.List>
                    <Prop name="open_time_hour" type="integer" required mode="output">
                      The hour part of the time the store opens in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="open_time_minute" type="integer" required mode="output">
                      The minute part of the time the store opens.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_hour" type="integer" required mode="output">
                      The hour part of the time the store closes in 24-hour format.

                      <Prop.Extras>
                        **Maximum:** `23`
                      </Prop.Extras>
                    </Prop>

                    <Prop name="close_time_minute" type="integer" required mode="output">
                      The minute part of the time the store closes.

                      <Prop.Extras>
                        **Maximum:** `59`
                      </Prop.Extras>
                    </Prop>
                  </Prop.List>
                </PillAccordion>
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="receiving_from_locations" type="string[]" mode="output">
          A list of locations that are allowed to produce or transfer items to this pickup location.

          <Prop.Extras>
            **Minimum length:** `1`
          </Prop.Extras>
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="continuation" type="string" mode="output">
    A continuation token. If the success response contains a continuation token, the list contains more items you can list. You can use this token as a query parameter and retrieve more items from the list. This value should be NULL if no more results are available.

    <Prop.Extras>
      **Maximum length:** `255`
    </Prop.Extras>
  </Prop>
</Prop.List>

## Example response

```json
{
  "locations": [
    {
      "id": "partnerLocation1234",
      "display_name": "Partner Fake Location",
      "phone": "(555) 555-1234",
      "timezone": "Australia/Melbourne",
      "address": {
        "address_line1": "374 Johnson Ave, Brooklyn",
        "address_line2": "Unit 1",
        "city": "New York",
        "subdivision": "US-NY",
        "postcode": "11206",
        "country": "US"
      },
      "geolocation": {
        "latitude": -33.8853,
        "longitude": 151.2088
      },
      "receiving_from_locations": [
        "partnerLocation1234_production",
        "partnerLocation1234_transfer"
      ],
      "pickup_hours": {
        "monday_hours": {
          "open_time_hour": 10,
          "open_time_minute": 0,
          "close_time_hour": 17,
          "close_time_minute": 30
        },
        "tuesday_hours": {
          "open_time_hour": 10,
          "open_time_minute": 0,
          "close_time_hour": 17,
          "close_time_minute": 30
        },
        "wednesday_hours": {
          "open_time_hour": 10,
          "open_time_minute": 0,
          "close_time_hour": 17,
          "close_time_minute": 30
        },
        "thursday_hours": {
          "open_time_hour": 10,
          "open_time_minute": 0,
          "close_time_hour": 17,
          "close_time_minute": 30
        },
        "friday_hours": {
          "open_time_hour": 10,
          "open_time_minute": 0,
          "close_time_hour": 17,
          "close_time_minute": 30
        },
        "saturday_hours": {
          "open_time_hour": 9,
          "open_time_minute": 0,
          "close_time_hour": 17,
          "close_time_minute": 30
        },
        "sunday_hours": {
          "open_time_hour": 9,
          "open_time_minute": 0,
          "close_time_hour": 12,
          "close_time_minute": 0
        }
      }
    }
  ],
  "continuation": "edf3"
}
```

## Error responses

### 400 Bad Request. For example, an invalid payload format.

### 401 Unauthorized. For example, an invalid signature.
