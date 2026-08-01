Source: https://www.canva.dev/docs/scim/create-group/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/scim/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a group with SCIM

Creates a user group in a Canva team.

The `displayName` of the group can't already be in use by an existing group within the same Canva Team.

NOTE: You can't provide a list of group members when creating a group. To add users to a group, you can use either the [`PUT`](/docs/scim/update-all-information-group) or [`PATCH`](/docs/scim/update-individual-attributes-group) operations after the group is created.

## HTTP method and URL path

POST https://www.canva.com/_scim/v2/Groups

## Header parameters

<Prop.List>
  <Prop name="Authorization" type="string" required>
    Provides credentials to authenticate the request, in the form of a `Bearer` token.

    For example: `Authorization: Bearer {token}`
  </Prop>

  <Prop name="Content-Type" type="string" required>
    Indicates the media type of the information sent in the request. This must be set to `application/scim+json`.

    For example: `Content-Type: application/scim+json`
  </Prop>
</Prop.List>

## Body parameters

<Prop.List>
  <Prop name="schemas" type="string[]" required>
    <Prop.Extras>
      **Available values:** The only valid value is `urn:ietf:params:scim:schemas:core:2.0:Group`.
    </Prop.Extras>
  </Prop>

  <Prop name="displayName" type="string" required>
    The name of the group, suitable for display to end-users.
  </Prop>
</Prop.List>

## Example request

Examples for using the `/_scim/v2/Groups` endpoint:

<Tabs storageKey="example.language" disableContentTransition>
  <Tab name="cURL">
    ```sh
    curl --request POST 'https://www.canva.com/_scim/v2/Groups' \
    --header 'Authorization: Bearer {token}' \
    --header 'Content-Type: application/scim+json' \
    --data '{
      "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
      "displayName": "White rabbits"
    }'
    ```
  </Tab>

  <Tab name="Node.js">
    ```js
    const fetch = require("node-fetch");

    fetch("https://www.canva.com/_scim/v2/Groups", {
      method: "POST",
      headers: {
        "Authorization": "Bearer {token}",
        "Content-Type": "application/scim+json",
      },
      body: JSON.stringify({
        "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
        "displayName": "White rabbits"
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
                .uri(URI.create("https://www.canva.com/_scim/v2/Groups"))
                .header("Authorization", "Bearer {token}")
                .header("Content-Type", "application/scim+json")
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"schemas\": \"urn:ietf:params:scim:schemas:core:2.0:Group\", \"displayName\": \"White rabbits\"}"))
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
        "Content-Type": "application/scim+json"
    }

    data = {
        "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
        "displayName": "White rabbits"
    }

    response = requests.post("https://www.canva.com/_scim/v2/Groups",
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
      RequestUri = new Uri("https://www.canva.com/_scim/v2/Groups"),
      Headers =
      {
        { "Authorization", "Bearer {token}" },
      },
      Content = new StringContent(
        "{\"schemas\": \"urn:ietf:params:scim:schemas:core:2.0:Group\", \"displayName\": \"White rabbits\"}",
        Encoding.UTF8,
        "application/scim+json"
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
    	  "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
    	  "displayName": "White rabbits"
    	}`)

    	url := "https://www.canva.com/_scim/v2/Groups"
    	req, _ := http.NewRequest("POST", url, payload)
    	req.Header.Add("Authorization", "Bearer {token}")
    	req.Header.Add("Content-Type", "application/scim+json")

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
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => array(
        'Authorization: Bearer {token}',
        'Content-Type: application/scim+json',
      ),
      CURLOPT_POSTFIELDS => json_encode([
        "schemas" => "urn:ietf:params:scim:schemas:core:2.0:Group",
        "displayName" => "White rabbits"
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

    url = URI('https://www.canva.com/_scim/v2/Groups')
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true

    request = Net::HTTP::Post.new(url)
    request['Authorization'] = 'Bearer {token}'
    request['Content-Type'] = 'application/scim+json'
    request.body = <<REQUEST_BODY
    {
      "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
      "displayName": "White rabbits"
    }
    REQUEST_BODY

    response = http.request(request)
    puts response.read_body
    ```
  </Tab>
</Tabs>

## Success response

If successful, the endpoint returns a `201` response with a JSON body with the following parameters:

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

    <PillAccordion title={<>Properties of <strong>meta</strong></>} defaultExpanded={true}>
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

## Example response

```json
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
```

## Error responses

### 409 Conflict

<Prop.List>
  <Prop name="schemas" type="string[]" required mode="output">
    <Prop.Extras>
      **Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:Error`.
    </Prop.Extras>
  </Prop>

  <Prop name="detail" type="string" required mode="output">
    <Prop.Extras>
      **Available values:** The only valid value is `Group with name {group_name} already exists.`.
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
  "detail": "Group with name White rabbits already exists.",
  "status": "409"
}
```
