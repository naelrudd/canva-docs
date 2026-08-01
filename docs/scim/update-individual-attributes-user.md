Source: https://www.canva.dev/docs/scim/update-individual-attributes-user/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/scim/llms.txt
> Use this file to discover all available pages before exploring further.

# Update individual attributes for a user

Updates individual attributes for a user. To update a user's attributes, you must use the correct [syntax for the operation, as defined in the SCIM specification](https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.2).

For example, to update a user's `work` email and `familyName` values, use the following for the request body:

```json
{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
  "Operations": [
    {
      "op": "replace",
      "path": "emails[type eq \"work\"].value",
      "value": "my.new.email@example.com"
    },
    {
      "op": "replace",
      "path": "name.familyName",
      "value": "New-Family-Name"
    }
  ]
}
```

To deprovision a SCIM user, you can use an operation to set the `active` attribute to `false`. For example:

```json
{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
  "Operations": [
    {
      "op": "replace",
      "path": "active",
      "value": false
    }
  ]
}
```

Alternatively, you can provide an operation's `value` object as a list of paths and values to modify. For example:

```json
{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
  "Operations": [
    {
      "op": "add",
      "value": {
        "name.givenName": "New-Given-Name",
        "name.familyName": "New-Family-Name",
        "externalId": "abcd1234"
      }
    }
  ]
}
```

## HTTP method and URL path

PATCH https://www.canva.com/_scim/v2/Users/{canva_scim_id}

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

## Path parameters

<Prop.List>
  <Prop name="canva_scim_id" type="string" required>
    The Canva-generated SCIM ID for the user.
  </Prop>
</Prop.List>

## Body parameters

<Prop.List>
  <Prop name="schemas" type="string[]" required>
    The URIs of the SCIM schemas.

    <Prop.Extras>
      **Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:PatchOp`.
    </Prop.Extras>
  </Prop>

  <Prop name="Operations" type="object[]" required>
    List of patch operations

    <PillAccordion title={<>Properties of <strong>Operations</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="op" type="string" required>
          The SCIM patch operation to perform.

          <Prop.Extras>
            **Available values:**

            * `add`
            * `remove`
            * `replace`
          </Prop.Extras>
        </Prop>

        <Prop name="path" type="string">
          An attribute path describing the target of the operation. For more information, see the [SCIM specification](https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.2).
        </Prop>

        <Prop name="value" type="object">
          The value to add, remove, or replace.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

## Example request

Examples for using the `/_scim/v2/Users/{canva_scim_id}` endpoint:

<Tabs storageKey="example.language" disableContentTransition>
  <Tab name="cURL">
    ```sh
    curl --request PATCH 'https://www.canva.com/_scim/v2/Users/{canva_scim_id}' \
    --header 'Authorization: Bearer {token}' \
    --header 'Content-Type: application/scim+json' \
    --data '{
      "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
      ],
      "Operations": [
        {
          "op": "replace",
          "path": "name.familyName",
          "value": "Liddell"
        }
      ]
    }'
    ```
  </Tab>

  <Tab name="Node.js">
    ```js
    const fetch = require("node-fetch");

    fetch("https://www.canva.com/_scim/v2/Users/{canva_scim_id}", {
      method: "PATCH",
      headers: {
        "Authorization": "Bearer {token}",
        "Content-Type": "application/scim+json",
      },
      body: JSON.stringify({
        "schemas": [
          "urn:ietf:params:scim:api:messages:2.0:PatchOp"
        ],
        "Operations": [
          {
            "op": "replace",
            "path": "name.familyName",
            "value": "Liddell"
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
                .uri(URI.create("https://www.canva.com/_scim/v2/Users/{canva_scim_id}"))
                .header("Authorization", "Bearer {token}")
                .header("Content-Type", "application/scim+json")
                .method("PATCH", HttpRequest.BodyPublishers.ofString("{\"schemas\": [\"urn:ietf:params:scim:api:messages:2.0:PatchOp\"], \"Operations\": [{\"op\": \"replace\", \"path\": \"name.familyName\", \"value\": \"Liddell\"}]}"))
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
        "schemas": [
            "urn:ietf:params:scim:api:messages:2.0:PatchOp"
        ],
        "Operations": [
            {
                "op": "replace",
                "path": "name.familyName",
                "value": "Liddell"
            }
        ]
    }

    response = requests.patch("https://www.canva.com/_scim/v2/Users/{canva_scim_id}",
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
      Method = HttpMethod.Patch,
      RequestUri = new Uri("https://www.canva.com/_scim/v2/Users/{canva_scim_id}"),
      Headers =
      {
        { "Authorization", "Bearer {token}" },
      },
      Content = new StringContent(
        "{\"schemas\": [\"urn:ietf:params:scim:api:messages:2.0:PatchOp\"], \"Operations\": [{\"op\": \"replace\", \"path\": \"name.familyName\", \"value\": \"Liddell\"}]}",
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
    	  "schemas": [
    	    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    	  ],
    	  "Operations": [
    	    {
    	      "op": "replace",
    	      "path": "name.familyName",
    	      "value": "Liddell"
    	    }
    	  ]
    	}`)

    	url := "https://www.canva.com/_scim/v2/Users/{canva_scim_id}"
    	req, _ := http.NewRequest("PATCH", url, payload)
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
      CURLOPT_URL => "https://www.canva.com/_scim/v2/Users/{canva_scim_id}",
      CURLOPT_CUSTOMREQUEST => "PATCH",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => array(
        'Authorization: Bearer {token}',
        'Content-Type: application/scim+json',
      ),
      CURLOPT_POSTFIELDS => json_encode([
        "schemas" => [
          "urn:ietf:params:scim:api:messages:2.0:PatchOp"
        ],
        "Operations" => [
          [
            "op" => "replace",
            "path" => "name.familyName",
            "value" => "Liddell"
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

    url = URI('https://www.canva.com/_scim/v2/Users/{canva_scim_id}')
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true

    request = Net::HTTP::Patch.new(url)
    request['Authorization'] = 'Bearer {token}'
    request['Content-Type'] = 'application/scim+json'
    request.body = <<REQUEST_BODY
    {
      "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
      ],
      "Operations": [
        {
          "op": "replace",
          "path": "name.familyName",
          "value": "Liddell"
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

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

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

    <PillAccordion title={<>Properties of <strong>meta</strong></>} defaultExpanded={true}>
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

    <PillAccordion title={<>Properties of <strong>emails</strong></>} defaultExpanded={true}>
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

    <PillAccordion title={<>Properties of <strong>name</strong></>} defaultExpanded={true}>
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

## Example response

```json
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
      **Available values:** The only valid value is `Email domain not authorized for SCIM.`.
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
  "detail": "Email domain not authorized for SCIM.",
  "status": "403"
}
```

### 404 Not found

<Prop.List>
  <Prop name="schemas" type="string[]" required mode="output">
    <Prop.Extras>
      **Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:Error`.
    </Prop.Extras>
  </Prop>

  <Prop name="detail" type="string" required mode="output">
    <Prop.Extras>
      **Available values:** The only valid value is `No user found for id {canva_scim_id}`.
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
  "detail": "No user found for id {canva_scim_id}",
  "status": "404"
}
```

### 409 Conflict

<Prop.List>
  <Prop name="schemas" type="string[]" required mode="output">
    <Prop.Extras>
      **Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:Error`.
    </Prop.Extras>
  </Prop>

  <Prop name="detail" type="string" required mode="output">
    <Prop.Extras>
      **Available values:**

      * `userName not available`
      * `Account with email can not be updated. User needs to accept SSO linking`
      * `Account with email already exists. User must first log in with SAML to confirm account ownership`
      * `Account with email is soft deleted. The user must first log in to reactivate their account`
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
  "detail": "userName not available",
  "status": "409"
}
```
