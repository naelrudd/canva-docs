Source: https://www.canva.dev/docs/scim/list-groups/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/scim/llms.txt
> Use this file to discover all available pages before exploring further.

# List groups

Gets a paginated list of all user groups in a Canva team.

You can use the `startIndex` and `count` parameters to control the pagination of the response.

You can also provide a `filter` parameter to narrow down the groups returned to only include those matching the filter.

NOTE: The `members` array returned in a group's API response is always empty, even if there are members in the group. To see members of a group, you must [use the Canva web interface](https://www.canva.com/help/groups/).

## HTTP method and URL path

GET https://www.canva.com/_scim/v2/Groups

## Header parameters

<Prop.List>
  <Prop name="Authorization" type="string" required>
    Provides credentials to authenticate the request, in the form of a `Bearer` token.

    For example: `Authorization: Bearer {token}`
  </Prop>
</Prop.List>

## Query parameters

<Prop.List>
  <Prop name="startIndex" type="integer">
    Used to paginate the response: the index of the first result to return.
  </Prop>

  <Prop name="count" type="integer">
    Used to paginate the response: the number of results to return. Must be between `1` and `10`.
  </Prop>

  <Prop name="filter" type="string">
    A filter to narrow down the results returned, using the  equals (`eq`) query parameter. The following filters are supported:

    * Return the group matching the SCIM `displayName` value: `displayName eq "{display_name}"`.

      For example: `GET /_scim/v2/Groups?filter=displayName%20eq%20"White rabbits"`
  </Prop>
</Prop.List>

## Example request

Examples for using the `/_scim/v2/Groups` endpoint:

<Tabs storageKey="example.language" disableContentTransition>
  <Tab name="cURL">
    ```sh
    curl --request GET 'https://www.canva.com/_scim/v2/Groups' \
    --header 'Authorization: Bearer {token}'
    ```
  </Tab>

  <Tab name="Node.js">
    ```js
    const fetch = require("node-fetch");

    fetch("https://www.canva.com/_scim/v2/Groups", {
      method: "GET",
      headers: {
        "Authorization": "Bearer {token}",
      },
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
                .uri(URI.create("https://www.canva.com/_scim/v2/Groups"))
                .header("Authorization", "Bearer {token}")
                .method("GET", HttpRequest.BodyPublishers.noBody())
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
        "Authorization": "Bearer {token}"
    }

    response = requests.get("https://www.canva.com/_scim/v2/Groups",
        headers=headers
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
      Method = HttpMethod.Get,
      RequestUri = new Uri("https://www.canva.com/_scim/v2/Groups"),
      Headers =
      {
        { "Authorization", "Bearer {token}" },
      },
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
    )

    func main() {
    	url := "https://www.canva.com/_scim/v2/Groups"
    	req, _ := http.NewRequest("GET", url, nil)
    	req.Header.Add("Authorization", "Bearer {token}")

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
      CURLOPT_URL => "https://www.canva.com/_scim/v2/Groups",
      CURLOPT_CUSTOMREQUEST => "GET",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => array(
        'Authorization: Bearer {token}',
      ),
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

    url = URI('https://www.canva.com/_scim/v2/Groups')
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true

    request = Net::HTTP::Get.new(url)
    request['Authorization'] = 'Bearer {token}'

    response = http.request(request)
    puts response.read_body
    ```
  </Tab>
</Tabs>

## Success response

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

<Prop.List>
  <Prop name="schemas" type="string[]" required mode="output">
    <Prop.Extras>
      **Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:ListResponse`.
    </Prop.Extras>
  </Prop>

  <Prop name="totalResults" type="integer" required mode="output">
    The total number of results matching the query.
  </Prop>

  <Prop name="startIndex" type="integer" required mode="output">
    The index of the first result.
  </Prop>

  <Prop name="itemsPerPage" type="integer" required mode="output">
    The number of results returned in the current page.
  </Prop>

  <Prop name="resources" type="ScimGroupResponse[]" required mode="output">
    An array of the groups returned in the current page of results.

    <PillAccordion title={<>Properties of <strong>resources</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="schemas" type="string[]" required mode="output">
          <Prop.Extras>
            **Available values:** The only valid value is `urn:ietf:params:scim:schemas:core:2.0:Group`.
          </Prop.Extras>
        </Prop>

        <Prop name="id" type="string" required mode="output">
          The Canva-generated SCIM ID for the group.
        </Prop>

        <Prop name="meta" type="object" required mode="output">
          Meta properties for the group.

          <PillAccordion title={<>Properties of <strong>meta</strong></>}>
            <Prop.List>
              <Prop name="resourceType" type="string" required mode="output">
                The SCIM resource type of the object.

                <Prop.Extras>
                  **Available values:** The only valid value is `Group`.
                </Prop.Extras>
              </Prop>

              <Prop name="created" type="string" required mode="output">
                The timestamp when the object was created.
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="displayName" type="string" required mode="output">
          The name of the group, suitable for display to end-users.
        </Prop>

        <Prop name="members" type="object[]" required mode="output">
          NOTE: The `members` array returned in a group's API response is always empty, even if there are members in the group. To see members of a group, you must [use the Canva web interface](https://www.canva.com/help/groups/).
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

## Example response

```json
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "totalResults": 1,
  "startIndex": 1,
  "itemsPerPage": 10,
  "resources": [
    {
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group"
      ],
      "id": "GAFgrpb1abC",
      "meta": {
        "resourceType": "Group",
        "created": "2023-09-18T06:08:35Z"
      },
      "displayName": "White rabbits",
      "members": []
    }
  ]
}
```

## Error responses

### 403 Forbidden

<Prop.List>
  <Prop name="schemas" type="string[]" required mode="output">
    <Prop.Extras>
      **Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:Error`.
    </Prop.Extras>
  </Prop>

  <Prop name="detail" type="string" required mode="output">
    <Prop.Extras>
      **Available values:** The only valid value is `Unsupported filter field`.
    </Prop.Extras>
  </Prop>

  <Prop name="status" type="string" required mode="output">
    The HTTP status code of the error.
  </Prop>
</Prop.List>

#### Example error response

```json
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:Error"
  ],
  "detail": "Unsupported filter field",
  "status": "403"
}
```
