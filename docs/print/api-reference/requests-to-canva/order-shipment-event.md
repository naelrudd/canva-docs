> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/print/llms.txt
> Use this file to discover all available pages before exploring further.

# Create order shipment event

Creates an event to notify Canva about a shipment for an order in the print partner's system.

## HTTP method and URL path

POST https\://api.canva.com/print/v1/events/order-shipment

## Header parameters

<Prop.List>
  <Prop name="Authorization" type="string" required>
    Provides credentials to authenticate the request, in the form of a `Bearer` token.

    For example: `Authorization: Bearer {token}`
  </Prop>

  <Prop name="Content-Type" type="string" required>
    Indicates the media type of the information sent in the request. This must be set to `application/json`.

    For example: `Content-Type: application/json`
  </Prop>

  <Prop name="X-Canva-Print-Client-Id" type="string" required>
    Unique ID of the print partner making the request.
  </Prop>
</Prop.List>

## Body parameters

<Prop.List>
  <Prop name="request_type" type="string" required>
    <Prop.Extras>
      **Available values:** The only valid value is `shipment_event`.
    </Prop.Extras>
  </Prop>

  <Prop name="order_reference_id" type="string" required>
    A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

    <Prop.Extras>
      **Maximum length:** `255`
    </Prop.Extras>
  </Prop>

  <Prop name="shipments" type="ShipmentEvent[]" required>
    A list of shipments for the order.

    <Prop.Extras>
      **Minimum items:** `1`
    </Prop.Extras>

    <PillAccordion title={<>Properties of <strong>shipments</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="tracking_number" type="string" required>
          The tracking number provided by the carrier.

          <Prop.Extras>
            **Minimum length:** `1`

            **Maximum length:** `255`
          </Prop.Extras>
        </Prop>

        <Prop name="carrier" type="string" required>
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

        <Prop name="items" type="ShipmentItem[]" required>
          The items included in the shipment.

          <Prop.Extras>
            **Minimum items:** `1`
          </Prop.Extras>

          <PillAccordion title={<>Properties of <strong>items</strong></>}>
            <Prop.List>
              <Prop name="item_reference_id" type="string" required>
                A unique, case-sensitive ID for an order item that the partner can use when communicating with Canva.

                <Prop.Extras>
                  **Maximum length:** `255`
                </Prop.Extras>
              </Prop>

              <Prop name="quantity" type="integer" required>
                The number of copies of an item that were shipped.
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="dispatch_location_reference" type="string" required>
          The location reference ID of where the shipment was dispatched.

          <Prop.Extras>
            **Maximum length:** `255`
          </Prop.Extras>
        </Prop>

        <Prop name="dispatched_at" type="integer" required>
          When the shipment was dispatched, as a Unix timestamp (in seconds since the Unix Epoch).
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

## Example requests

### Single item, single shipment

<Tabs storageKey="example.language" disableContentTransition>
  <Tab name="cURL">
    ```sh
    curl --request POST 'https://api.canva.com/print/v1/events/order-shipment' \
    --header 'Authorization: Bearer {token}' \
    --header 'Content-Type: application/json' \
    --header 'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=' \
    --data '{
      "request_type": "shipment_event",
      "order_reference_id": "FO123456789",
      "shipments": [
        {
          "tracking_number": "123456789",
          "carrier": "fedex",
          "items": [
            {
              "item_reference_id": "FI123456789",
              "quantity": 50
            }
          ],
          "dispatched_at": 1726448251,
          "dispatch_location_reference": "partnerLocation1234"
        }
      ]
    }'
    ```
  </Tab>

  <Tab name="Node.js">
    ```js
    const fetch = require("node-fetch");

    fetch("https://api.canva.com/print/v1/events/order-shipment", {
      method: "POST",
      headers: {
        "Authorization": "Bearer {token}",
        "Content-Type": "application/json",
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28=",
      },
      body: JSON.stringify({
        "request_type": "shipment_event",
        "order_reference_id": "FO123456789",
        "shipments": [
          {
            "tracking_number": "123456789",
            "carrier": "fedex",
            "items": [
              {
                "item_reference_id": "FI123456789",
                "quantity": 50
              }
            ],
            "dispatched_at": 1726448251,
            "dispatch_location_reference": "partnerLocation1234"
          }
        ]
      }),
    })
      .then(async (response) => {
        const data = await response.json();
        console.log(data);
      })
      .catch(err => console.error(err));
    ```
  </Tab>

  <Tab name="Java">
    ```java
    import java.io.IOException;
    import java.net.URI;
    import java.net.http.*;

    public class ApiExample {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://api.canva.com/print/v1/events/order-shipment"))
                .header("Authorization", "Bearer {token}")
                .header("Content-Type", "application/json")
                .header("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"request_type\": \"shipment_event\", \"order_reference_id\": \"FO123456789\", \"shipments\": [{\"tracking_number\": \"123456789\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 50}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}]}"))
                .build();

            HttpResponse<String> response = HttpClient.newHttpClient().send(
                request,
                HttpResponse.BodyHandlers.ofString()
            );
            System.out.println(response.body());
        }
    }
    ```
  </Tab>

  <Tab name="Python">
    ```py
    import requests

    headers = {
        "Authorization": "Bearer {token}",
        "Content-Type": "application/json",
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28="
    }

    data = {
        "request_type": "shipment_event",
        "order_reference_id": "FO123456789",
        "shipments": [
            {
                "tracking_number": "123456789",
                "carrier": "fedex",
                "items": [
                    {
                        "item_reference_id": "FI123456789",
                        "quantity": 50
                    }
                ],
                "dispatched_at": 1726448251,
                "dispatch_location_reference": "partnerLocation1234"
            }
        ]
    }

    response = requests.post("https://api.canva.com/print/v1/events/order-shipment",
        headers=headers,
        json=data
    )
    print(response.json())
    ```
  </Tab>

  <Tab name="C#">
    ```csharp
    using System.Net.Http;

    var client = new HttpClient();
    var request = new HttpRequestMessage
    {
      Method = HttpMethod.Post,
      RequestUri = new Uri("https://api.canva.com/print/v1/events/order-shipment"),
      Headers =
      {
        { "Authorization", "Bearer {token}" },
        { "X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=" },
      },
      Content = new StringContent(
        "{\"request_type\": \"shipment_event\", \"order_reference_id\": \"FO123456789\", \"shipments\": [{\"tracking_number\": \"123456789\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 50}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}]}",
        Encoding.UTF8,
        "application/json"
      ),
    };

    using (var response = await client.SendAsync(request))
    {
      response.EnsureSuccessStatusCode();
      var body = await response.Content.ReadAsStringAsync();
      Console.WriteLine(body);
    };
    ```
  </Tab>

  <Tab name="Go">
    ```go
    package main

    import (
    	"fmt"
    	"io"
    	"net/http"
    	"strings"
    )

    func main() {
    	payload := strings.NewReader(`{
    	  "request_type": "shipment_event",
    	  "order_reference_id": "FO123456789",
    	  "shipments": [
    	    {
    	      "tracking_number": "123456789",
    	      "carrier": "fedex",
    	      "items": [
    	        {
    	          "item_reference_id": "FI123456789",
    	          "quantity": 50
    	        }
    	      ],
    	      "dispatched_at": 1726448251,
    	      "dispatch_location_reference": "partnerLocation1234"
    	    }
    	  ]
    	}`)

    	url := "https://api.canva.com/print/v1/events/order-shipment"
    	req, _ := http.NewRequest("POST", url, payload)
    	req.Header.Add("Authorization", "Bearer {token}")
    	req.Header.Add("Content-Type", "application/json")
    	req.Header.Add("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")

    	res, _ := http.DefaultClient.Do(req)
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    	fmt.Println(string(body))
    }
    ```
  </Tab>

  <Tab name="PHP">
    ```php
    $curl = curl_init();
    curl_setopt_array($curl, array(
      CURLOPT_URL => "https://api.canva.com/print/v1/events/order-shipment",
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => array(
        'Authorization: Bearer {token}',
        'Content-Type: application/json',
        'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=',
      ),
      CURLOPT_POSTFIELDS => json_encode([
        "request_type" => "shipment_event",
        "order_reference_id" => "FO123456789",
        "shipments" => [
          [
            "tracking_number" => "123456789",
            "carrier" => "fedex",
            "items" => [
              [
                "item_reference_id" => "FI123456789",
                "quantity" => 50
              ]
            ],
            "dispatched_at" => 1726448251,
            "dispatch_location_reference" => "partnerLocation1234"
          ]
        ]
      ])
    ));

    $response = curl_exec($curl);
    $err = curl_error($curl);
    curl_close($curl);

    if (empty($err)) {
      echo $response;
    } else {
      echo "Error: " . $err;
    }
    ```
  </Tab>

  <Tab name="Ruby">
    ```ruby
    require 'net/http'
    require 'uri'

    url = URI('https://api.canva.com/print/v1/events/order-shipment')
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true

    request = Net::HTTP::Post.new(url)
    request['Authorization'] = 'Bearer {token}'
    request['Content-Type'] = 'application/json'
    request['X-Canva-Print-Client-Id'] = 'Ym9zY236Ym9zY28='
    request.body = <<REQUEST_BODY
    {
      "request_type": "shipment_event",
      "order_reference_id": "FO123456789",
      "shipments": [
        {
          "tracking_number": "123456789",
          "carrier": "fedex",
          "items": [
            {
              "item_reference_id": "FI123456789",
              "quantity": 50
            }
          ],
          "dispatched_at": 1726448251,
          "dispatch_location_reference": "partnerLocation1234"
        }
      ]
    }
    REQUEST_BODY

    response = http.request(request)
    puts response.read_body
    ```
  </Tab>
</Tabs>

### Multiple items, single shipment

<Tabs storageKey="example.language" disableContentTransition>
  <Tab name="cURL">
    ```sh
    curl --request POST 'https://api.canva.com/print/v1/events/order-shipment' \
    --header 'Authorization: Bearer {token}' \
    --header 'Content-Type: application/json' \
    --header 'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=' \
    --data '{
      "request_type": "shipment_event",
      "order_reference_id": "FO123456789",
      "shipments": [
        {
          "tracking_number": "123456789",
          "carrier": "fedex",
          "items": [
            {
              "item_reference_id": "FI123456789",
              "quantity": 50
            },
            {
              "item_reference_id": "FI987654321",
              "quantity": 10
            }
          ],
          "dispatched_at": 1726448251,
          "dispatch_location_reference": "partnerLocation1234"
        }
      ]
    }'
    ```
  </Tab>

  <Tab name="Node.js">
    ```js
    const fetch = require("node-fetch");

    fetch("https://api.canva.com/print/v1/events/order-shipment", {
      method: "POST",
      headers: {
        "Authorization": "Bearer {token}",
        "Content-Type": "application/json",
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28=",
      },
      body: JSON.stringify({
        "request_type": "shipment_event",
        "order_reference_id": "FO123456789",
        "shipments": [
          {
            "tracking_number": "123456789",
            "carrier": "fedex",
            "items": [
              {
                "item_reference_id": "FI123456789",
                "quantity": 50
              },
              {
                "item_reference_id": "FI987654321",
                "quantity": 10
              }
            ],
            "dispatched_at": 1726448251,
            "dispatch_location_reference": "partnerLocation1234"
          }
        ]
      }),
    })
      .then(async (response) => {
        const data = await response.json();
        console.log(data);
      })
      .catch(err => console.error(err));
    ```
  </Tab>

  <Tab name="Java">
    ```java
    import java.io.IOException;
    import java.net.URI;
    import java.net.http.*;

    public class ApiExample {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://api.canva.com/print/v1/events/order-shipment"))
                .header("Authorization", "Bearer {token}")
                .header("Content-Type", "application/json")
                .header("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"request_type\": \"shipment_event\", \"order_reference_id\": \"FO123456789\", \"shipments\": [{\"tracking_number\": \"123456789\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 50}, {\"item_reference_id\": \"FI987654321\", \"quantity\": 10}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}]}"))
                .build();

            HttpResponse<String> response = HttpClient.newHttpClient().send(
                request,
                HttpResponse.BodyHandlers.ofString()
            );
            System.out.println(response.body());
        }
    }
    ```
  </Tab>

  <Tab name="Python">
    ```py
    import requests

    headers = {
        "Authorization": "Bearer {token}",
        "Content-Type": "application/json",
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28="
    }

    data = {
        "request_type": "shipment_event",
        "order_reference_id": "FO123456789",
        "shipments": [
            {
                "tracking_number": "123456789",
                "carrier": "fedex",
                "items": [
                    {
                        "item_reference_id": "FI123456789",
                        "quantity": 50
                    },
                    {
                        "item_reference_id": "FI987654321",
                        "quantity": 10
                    }
                ],
                "dispatched_at": 1726448251,
                "dispatch_location_reference": "partnerLocation1234"
            }
        ]
    }

    response = requests.post("https://api.canva.com/print/v1/events/order-shipment",
        headers=headers,
        json=data
    )
    print(response.json())
    ```
  </Tab>

  <Tab name="C#">
    ```csharp
    using System.Net.Http;

    var client = new HttpClient();
    var request = new HttpRequestMessage
    {
      Method = HttpMethod.Post,
      RequestUri = new Uri("https://api.canva.com/print/v1/events/order-shipment"),
      Headers =
      {
        { "Authorization", "Bearer {token}" },
        { "X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=" },
      },
      Content = new StringContent(
        "{\"request_type\": \"shipment_event\", \"order_reference_id\": \"FO123456789\", \"shipments\": [{\"tracking_number\": \"123456789\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 50}, {\"item_reference_id\": \"FI987654321\", \"quantity\": 10}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}]}",
        Encoding.UTF8,
        "application/json"
      ),
    };

    using (var response = await client.SendAsync(request))
    {
      response.EnsureSuccessStatusCode();
      var body = await response.Content.ReadAsStringAsync();
      Console.WriteLine(body);
    };
    ```
  </Tab>

  <Tab name="Go">
    ```go
    package main

    import (
    	"fmt"
    	"io"
    	"net/http"
    	"strings"
    )

    func main() {
    	payload := strings.NewReader(`{
    	  "request_type": "shipment_event",
    	  "order_reference_id": "FO123456789",
    	  "shipments": [
    	    {
    	      "tracking_number": "123456789",
    	      "carrier": "fedex",
    	      "items": [
    	        {
    	          "item_reference_id": "FI123456789",
    	          "quantity": 50
    	        },
    	        {
    	          "item_reference_id": "FI987654321",
    	          "quantity": 10
    	        }
    	      ],
    	      "dispatched_at": 1726448251,
    	      "dispatch_location_reference": "partnerLocation1234"
    	    }
    	  ]
    	}`)

    	url := "https://api.canva.com/print/v1/events/order-shipment"
    	req, _ := http.NewRequest("POST", url, payload)
    	req.Header.Add("Authorization", "Bearer {token}")
    	req.Header.Add("Content-Type", "application/json")
    	req.Header.Add("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")

    	res, _ := http.DefaultClient.Do(req)
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    	fmt.Println(string(body))
    }
    ```
  </Tab>

  <Tab name="PHP">
    ```php
    $curl = curl_init();
    curl_setopt_array($curl, array(
      CURLOPT_URL => "https://api.canva.com/print/v1/events/order-shipment",
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => array(
        'Authorization: Bearer {token}',
        'Content-Type: application/json',
        'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=',
      ),
      CURLOPT_POSTFIELDS => json_encode([
        "request_type" => "shipment_event",
        "order_reference_id" => "FO123456789",
        "shipments" => [
          [
            "tracking_number" => "123456789",
            "carrier" => "fedex",
            "items" => [
              [
                "item_reference_id" => "FI123456789",
                "quantity" => 50
              ],
              [
                "item_reference_id" => "FI987654321",
                "quantity" => 10
              ]
            ],
            "dispatched_at" => 1726448251,
            "dispatch_location_reference" => "partnerLocation1234"
          ]
        ]
      ])
    ));

    $response = curl_exec($curl);
    $err = curl_error($curl);
    curl_close($curl);

    if (empty($err)) {
      echo $response;
    } else {
      echo "Error: " . $err;
    }
    ```
  </Tab>

  <Tab name="Ruby">
    ```ruby
    require 'net/http'
    require 'uri'

    url = URI('https://api.canva.com/print/v1/events/order-shipment')
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true

    request = Net::HTTP::Post.new(url)
    request['Authorization'] = 'Bearer {token}'
    request['Content-Type'] = 'application/json'
    request['X-Canva-Print-Client-Id'] = 'Ym9zY236Ym9zY28='
    request.body = <<REQUEST_BODY
    {
      "request_type": "shipment_event",
      "order_reference_id": "FO123456789",
      "shipments": [
        {
          "tracking_number": "123456789",
          "carrier": "fedex",
          "items": [
            {
              "item_reference_id": "FI123456789",
              "quantity": 50
            },
            {
              "item_reference_id": "FI987654321",
              "quantity": 10
            }
          ],
          "dispatched_at": 1726448251,
          "dispatch_location_reference": "partnerLocation1234"
        }
      ]
    }
    REQUEST_BODY

    response = http.request(request)
    puts response.read_body
    ```
  </Tab>
</Tabs>

### Single item, multi shipment

<Tabs storageKey="example.language" disableContentTransition>
  <Tab name="cURL">
    ```sh
    curl --request POST 'https://api.canva.com/print/v1/events/order-shipment' \
    --header 'Authorization: Bearer {token}' \
    --header 'Content-Type: application/json' \
    --header 'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=' \
    --data '{
      "request_type": "shipment_event",
      "order_reference_id": "FO123456789",
      "shipments": [
        {
          "tracking_number": "123456789",
          "carrier": "fedex",
          "items": [
            {
              "item_reference_id": "FI123456789",
              "quantity": 25
            }
          ],
          "dispatched_at": 1726448251,
          "dispatch_location_reference": "partnerLocation1234"
        },
        {
          "tracking_number": "987654321",
          "carrier": "fedex",
          "items": [
            {
              "item_reference_id": "FI123456789",
              "quantity": 25
            }
          ],
          "dispatched_at": 1726448251,
          "dispatch_location_reference": "partnerLocation1234"
        }
      ]
    }'
    ```
  </Tab>

  <Tab name="Node.js">
    ```js
    const fetch = require("node-fetch");

    fetch("https://api.canva.com/print/v1/events/order-shipment", {
      method: "POST",
      headers: {
        "Authorization": "Bearer {token}",
        "Content-Type": "application/json",
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28=",
      },
      body: JSON.stringify({
        "request_type": "shipment_event",
        "order_reference_id": "FO123456789",
        "shipments": [
          {
            "tracking_number": "123456789",
            "carrier": "fedex",
            "items": [
              {
                "item_reference_id": "FI123456789",
                "quantity": 25
              }
            ],
            "dispatched_at": 1726448251,
            "dispatch_location_reference": "partnerLocation1234"
          },
          {
            "tracking_number": "987654321",
            "carrier": "fedex",
            "items": [
              {
                "item_reference_id": "FI123456789",
                "quantity": 25
              }
            ],
            "dispatched_at": 1726448251,
            "dispatch_location_reference": "partnerLocation1234"
          }
        ]
      }),
    })
      .then(async (response) => {
        const data = await response.json();
        console.log(data);
      })
      .catch(err => console.error(err));
    ```
  </Tab>

  <Tab name="Java">
    ```java
    import java.io.IOException;
    import java.net.URI;
    import java.net.http.*;

    public class ApiExample {
        public static void main(String[] args) throws IOException, InterruptedException {
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://api.canva.com/print/v1/events/order-shipment"))
                .header("Authorization", "Bearer {token}")
                .header("Content-Type", "application/json")
                .header("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"request_type\": \"shipment_event\", \"order_reference_id\": \"FO123456789\", \"shipments\": [{\"tracking_number\": \"123456789\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 25}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}, {\"tracking_number\": \"987654321\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 25}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}]}"))
                .build();

            HttpResponse<String> response = HttpClient.newHttpClient().send(
                request,
                HttpResponse.BodyHandlers.ofString()
            );
            System.out.println(response.body());
        }
    }
    ```
  </Tab>

  <Tab name="Python">
    ```py
    import requests

    headers = {
        "Authorization": "Bearer {token}",
        "Content-Type": "application/json",
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28="
    }

    data = {
        "request_type": "shipment_event",
        "order_reference_id": "FO123456789",
        "shipments": [
            {
                "tracking_number": "123456789",
                "carrier": "fedex",
                "items": [
                    {
                        "item_reference_id": "FI123456789",
                        "quantity": 25
                    }
                ],
                "dispatched_at": 1726448251,
                "dispatch_location_reference": "partnerLocation1234"
            },
            {
                "tracking_number": "987654321",
                "carrier": "fedex",
                "items": [
                    {
                        "item_reference_id": "FI123456789",
                        "quantity": 25
                    }
                ],
                "dispatched_at": 1726448251,
                "dispatch_location_reference": "partnerLocation1234"
            }
        ]
    }

    response = requests.post("https://api.canva.com/print/v1/events/order-shipment",
        headers=headers,
        json=data
    )
    print(response.json())
    ```
  </Tab>

  <Tab name="C#">
    ```csharp
    using System.Net.Http;

    var client = new HttpClient();
    var request = new HttpRequestMessage
    {
      Method = HttpMethod.Post,
      RequestUri = new Uri("https://api.canva.com/print/v1/events/order-shipment"),
      Headers =
      {
        { "Authorization", "Bearer {token}" },
        { "X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=" },
      },
      Content = new StringContent(
        "{\"request_type\": \"shipment_event\", \"order_reference_id\": \"FO123456789\", \"shipments\": [{\"tracking_number\": \"123456789\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 25}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}, {\"tracking_number\": \"987654321\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 25}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}]}",
        Encoding.UTF8,
        "application/json"
      ),
    };

    using (var response = await client.SendAsync(request))
    {
      response.EnsureSuccessStatusCode();
      var body = await response.Content.ReadAsStringAsync();
      Console.WriteLine(body);
    };
    ```
  </Tab>

  <Tab name="Go">
    ```go
    package main

    import (
    	"fmt"
    	"io"
    	"net/http"
    	"strings"
    )

    func main() {
    	payload := strings.NewReader(`{
    	  "request_type": "shipment_event",
    	  "order_reference_id": "FO123456789",
    	  "shipments": [
    	    {
    	      "tracking_number": "123456789",
    	      "carrier": "fedex",
    	      "items": [
    	        {
    	          "item_reference_id": "FI123456789",
    	          "quantity": 25
    	        }
    	      ],
    	      "dispatched_at": 1726448251,
    	      "dispatch_location_reference": "partnerLocation1234"
    	    },
    	    {
    	      "tracking_number": "987654321",
    	      "carrier": "fedex",
    	      "items": [
    	        {
    	          "item_reference_id": "FI123456789",
    	          "quantity": 25
    	        }
    	      ],
    	      "dispatched_at": 1726448251,
    	      "dispatch_location_reference": "partnerLocation1234"
    	    }
    	  ]
    	}`)

    	url := "https://api.canva.com/print/v1/events/order-shipment"
    	req, _ := http.NewRequest("POST", url, payload)
    	req.Header.Add("Authorization", "Bearer {token}")
    	req.Header.Add("Content-Type", "application/json")
    	req.Header.Add("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")

    	res, _ := http.DefaultClient.Do(req)
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    	fmt.Println(string(body))
    }
    ```
  </Tab>

  <Tab name="PHP">
    ```php
    $curl = curl_init();
    curl_setopt_array($curl, array(
      CURLOPT_URL => "https://api.canva.com/print/v1/events/order-shipment",
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => array(
        'Authorization: Bearer {token}',
        'Content-Type: application/json',
        'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=',
      ),
      CURLOPT_POSTFIELDS => json_encode([
        "request_type" => "shipment_event",
        "order_reference_id" => "FO123456789",
        "shipments" => [
          [
            "tracking_number" => "123456789",
            "carrier" => "fedex",
            "items" => [
              [
                "item_reference_id" => "FI123456789",
                "quantity" => 25
              ]
            ],
            "dispatched_at" => 1726448251,
            "dispatch_location_reference" => "partnerLocation1234"
          ],
          [
            "tracking_number" => "987654321",
            "carrier" => "fedex",
            "items" => [
              [
                "item_reference_id" => "FI123456789",
                "quantity" => 25
              ]
            ],
            "dispatched_at" => 1726448251,
            "dispatch_location_reference" => "partnerLocation1234"
          ]
        ]
      ])
    ));

    $response = curl_exec($curl);
    $err = curl_error($curl);
    curl_close($curl);

    if (empty($err)) {
      echo $response;
    } else {
      echo "Error: " . $err;
    }
    ```
  </Tab>

  <Tab name="Ruby">
    ```ruby
    require 'net/http'
    require 'uri'

    url = URI('https://api.canva.com/print/v1/events/order-shipment')
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true

    request = Net::HTTP::Post.new(url)
    request['Authorization'] = 'Bearer {token}'
    request['Content-Type'] = 'application/json'
    request['X-Canva-Print-Client-Id'] = 'Ym9zY236Ym9zY28='
    request.body = <<REQUEST_BODY
    {
      "request_type": "shipment_event",
      "order_reference_id": "FO123456789",
      "shipments": [
        {
          "tracking_number": "123456789",
          "carrier": "fedex",
          "items": [
            {
              "item_reference_id": "FI123456789",
              "quantity": 25
            }
          ],
          "dispatched_at": 1726448251,
          "dispatch_location_reference": "partnerLocation1234"
        },
        {
          "tracking_number": "987654321",
          "carrier": "fedex",
          "items": [
            {
              "item_reference_id": "FI123456789",
              "quantity": 25
            }
          ],
          "dispatched_at": 1726448251,
          "dispatch_location_reference": "partnerLocation1234"
        }
      ]
    }
    REQUEST_BODY

    response = http.request(request)
    puts response.read_body
    ```
  </Tab>
</Tabs>

## Success response

If successful, the endpoint returns the status code `204 No content` without a response body.

## Error responses

### 400 Invalid request. For example, an invalid data format.

<Prop.List>
  <Prop name="code" type="string" required mode="output">
    A short string indicating what failed. This field can be used to handle errors programmatically.

    <Prop.Extras>
      **Available values:**

      * `invalid_field`
      * `invalid_header_value`
      * `invalid_request`
      * `permission_denied`
      * `too_many_requests`
      * `not_found`
      * `bad_request_body`
      * `bad_http_method`
      * `bad_request_params`
      * `bad_query_params`
      * `endpoint_not_found`
      * `unsupported_version`
      * `invalid_access_token`
      * `revoked_access_token`
      * `invalid_client`
      * `unauthorized_client`
      * `invalid_basic_header`
    </Prop.Extras>
  </Prop>

  <Prop name="message" type="string" required mode="output">
    A human-readable description of what went wrong.
  </Prop>
</Prop.List>

#### Example error response

##### Bad request

```json
{
  "code": "invalid_request",
  "message": "The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed."
}
```

### 401 Invalid or unauthorized client ID or secret.

<Prop.List>
  <Prop name="code" type="string" required mode="output">
    A short string indicating what failed. This field can be used to handle errors programmatically.

    <Prop.Extras>
      **Available values:**

      * `invalid_field`
      * `invalid_header_value`
      * `invalid_request`
      * `permission_denied`
      * `too_many_requests`
      * `not_found`
      * `bad_request_body`
      * `bad_http_method`
      * `bad_request_params`
      * `bad_query_params`
      * `endpoint_not_found`
      * `unsupported_version`
      * `invalid_access_token`
      * `revoked_access_token`
      * `invalid_client`
      * `unauthorized_client`
      * `invalid_basic_header`
    </Prop.Extras>
  </Prop>

  <Prop name="message" type="string" required mode="output">
    A human-readable description of what went wrong.
  </Prop>
</Prop.List>

#### Example error response

##### Unauthorized

```json
{
  "code": "unauthorized_client",
  "message": "The client is not authorized for action."
}
```

### 403 Partner has no access to the order.

<Prop.List>
  <Prop name="code" type="string" required mode="output">
    A short string indicating what failed. This field can be used to handle errors programmatically.

    <Prop.Extras>
      **Available values:**

      * `invalid_field`
      * `invalid_header_value`
      * `invalid_request`
      * `permission_denied`
      * `too_many_requests`
      * `not_found`
      * `bad_request_body`
      * `bad_http_method`
      * `bad_request_params`
      * `bad_query_params`
      * `endpoint_not_found`
      * `unsupported_version`
      * `invalid_access_token`
      * `revoked_access_token`
      * `invalid_client`
      * `unauthorized_client`
      * `invalid_basic_header`
    </Prop.Extras>
  </Prop>

  <Prop name="message" type="string" required mode="output">
    A human-readable description of what went wrong.
  </Prop>
</Prop.List>

#### Example error response

##### Forbidden

```json
{
  "code": "permission_denied",
  "message": "The resource owner or authorization server denied the request."
}
```
