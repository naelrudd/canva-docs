Source: https://www.canva.dev/docs/scim/list-users/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/scim/llms.txt
> Use this file to discover all available pages before exploring further.

# List users

Gets a paginated list of all users in a Canva team, including inactive users.

You can use the `startIndex` and `count` parameters to control the pagination of the response.

You can also provide a `filter` parameter to narrow down the users returned to only include those matching the filter.

## HTTP method and URL path

GET https://www.canva.com/_scim/v2/Users

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

    * Return the user matching the SCIM `userName` value: `userName eq "{saml_name_id}"`.

      For example: `GET /_scim/v2/Users?filter=userName%20eq%20"aliddell"`
    * Return the user matching the SCIM `externalId` value: `externalId eq "{idp_provided_external_id}"`.

      For example: `GET /_scim/v2/Users?filter=externalId%20eq%20"abcdefgh12345678"`
  </Prop>
</Prop.List>

## Example request

Examples for using the `/_scim/v2/Users` endpoint:

<Tabs storageKey="example.language" disableContentTransition>
  <Tab name="cURL">
    ```sh
    curl --request GET 'https://www.canva.com/_scim/v2/Users' \
    --header 'Authorization: Bearer {token}'
    ```
  </Tab>

  <Tab name="Node.js">
    ```js
    const fetch = require("node-fetch");

    fetch("https://www.canva.com/_scim/v2/Users", {
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
                .uri(URI.create("https://www.canva.com/_scim/v2/Users"))
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

    response = requests.get("https://www.canva.com/_scim/v2/Users",
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
      RequestUri = new Uri("https://www.canva.com/_scim/v2/Users"),
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
    	url := "https://www.canva.com/_scim/v2/Users"
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
      CURLOPT_URL => "https://www.canva.com/_scim/v2/Users",
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

    url = URI('https://www.canva.com/_scim/v2/Users')
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

  <Prop name="resources" type="ScimUserResponse[]" required mode="output">
    An array of the users returned in the current page of results.

    <PillAccordion title={<>Properties of <strong>resources</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="schemas" type="string[]" required mode="output">
          The URIs of the SCIM schemas.

          <Prop.Extras>
            **Available values:** The only valid value is `urn:ietf:params:scim:schemas:core:2.0:User`.
          </Prop.Extras>
        </Prop>

        <Prop name="id" type="string" required mode="output">
          The Canva-generated SCIM ID for the user.
        </Prop>

        <Prop name="meta" type="object" required mode="output">
          Meta properties for the user.

          <PillAccordion title={<>Properties of <strong>meta</strong></>}>
            <Prop.List>
              <Prop name="resourceType" type="string" required mode="output">
                The SCIM resource type of the object.

                <Prop.Extras>
                  **Available values:** The only valid value is `User`.
                </Prop.Extras>
              </Prop>

              <Prop name="created" type="string" required mode="output">
                The timestamp when the object was created.
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="userName" type="string" required mode="output">
          A unique identifier for the user.
        </Prop>

        <Prop name="displayName" type="string" required mode="output">
          The name of the user, suitable for display to end-users.
        </Prop>

        <Prop name="emails" type="object[]" required mode="output">
          The email address for the user.

          NOTE: The Canva SCIM API only supports one email address for each user.

          <PillAccordion title={<>Properties of <strong>emails</strong></>}>
            <Prop.List>
              <Prop name="primary" type="boolean" required mode="output">
                Whether the email is the primary address. Only one email address for a user can be the primary one.
              </Prop>

              <Prop name="value" type="string" required mode="output">
                The email address.
              </Prop>

              <Prop name="type" type="string" required mode="output">
                The type of email address for the user. The Canva SCIM API only supports `work` as the type of the email address.

                <Prop.Extras>
                  **Available values:** The only valid value is `work`.
                </Prop.Extras>
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="active" type="boolean" required mode="output">
          Whether the user account is active. Setting this to `false` deprovisions the user in Canva.
        </Prop>

        <Prop name="role" type="string" required mode="output">
          The role of the user.

          If an invalid value is provided, the role defaults to `Member`.

          NOTE: Except for `Member`, all other role values map to the Canva "Brand Designer" role. For more information on Canva roles, see [Team roles and permissions](https://www.canva.com/help/roles-and-permissions/).

          <Prop.Extras>
            **Default value:** `Member`

            **Available values:**

            * `Member`
            * `Teacher`
            * `Staff`
            * `Admin`
            * `Template-designer`
            * `Aide`
            * `Administrator`
            * `School administrator`
            * `School`
            * `Tenant`
            * `Faculty`
          </Prop.Extras>
        </Prop>

        <Prop name="externalId" type="string" mode="output">
          A string that is an identifier for the resource as defined by the provisioning client.
        </Prop>

        <Prop name="name" type="name" mode="output">
          The components of the user's name.

          <PillAccordion title={<>Properties of <strong>name</strong></>}>
            <Prop.List>
              <Prop name="givenName" type="string" mode="output">
                The first or 'given' name for the user.
              </Prop>

              <Prop name="familyName" type="string" mode="output">
                The last or 'family' name for the user.
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="locale" type="string" mode="output">
          The user's default location, for example `en_AU`.
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
        "urn:ietf:params:scim:schemas:core:2.0:User"
      ],
      "id": "UAFdxab1abC",
      "externalId": "abcd1234",
      "meta": {
        "resourceType": "User",
        "created": "2023-09-18T06:08:35Z"
      },
      "userName": "aliddell",
      "displayName": "Alice Liddell",
      "name": {
        "givenName": "Alice",
        "familyName": "Liddell"
      },
      "emails": [
        {
          "primary": true,
          "value": "alice@acme.com",
          "type": "work"
        }
      ],
      "active": true,
      "locale": "en_US",
      "role": "Member"
    }
  ]
}
```

## Error responses

### 400 Bad request

<Prop.List>
  <Prop name="schemas" type="string[]" required mode="output">
    <Prop.Extras>
      **Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:Error`.
    </Prop.Extras>
  </Prop>

  <Prop name="detail" type="string" required mode="output">
    <Prop.Extras>
      **Available values:** The only valid value is `No SSO configurations found, please check the settings page`.
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
  "detail": "No SSO configurations found, please check the settings page",
  "status": "400"
}
```

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
