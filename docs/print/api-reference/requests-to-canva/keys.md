> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/print/llms.txt
> Use this file to discover all available pages before exploring further.

# Get signing keys

Gets a JSON Web Key Set (JWKS) containing public keys that are used to verify the authenticity of requests from the Canva Print API. The JWKS format follows [RFC-7517](https://www.rfc-editor.org/rfc/rfc7517#section-2) specifications.

You must use these keys to decrypt request signatures and verify that requests originated from Canva. This helps protect against [replay attacks](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/).

Canva might occasionally rotate these keys. We recommend you cache the keys returned from this API, and only access this API when you receive a request signed with an unrecognized key. This lets you verify requests quicker than fetching keys every time you receive a request from Canva.

## HTTP method and URL path

GET https\://api.canva.com/print/v1/keys

## Example request

Examples for using the `/v1/keys` endpoint:

<Tabs storageKey="example.language" disableContentTransition>
  <Tab name="cURL">
    ```sh
    curl --request GET 'https://api.canva.com/print/v1/keys'
    ```
  </Tab>

  <Tab name="Node.js">
    ```js
    const fetch = require("node-fetch");

    fetch("https://api.canva.com/print/v1/keys", {
      method: "GET",
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
                .uri(URI.create("https://api.canva.com/print/v1/keys"))
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

    response = requests.get("https://api.canva.com/print/v1/keys");
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
      RequestUri = new Uri("https://api.canva.com/print/v1/keys"),
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
    	url := "https://api.canva.com/print/v1/keys"
    	req, _ := http.NewRequest("GET", url, nil)

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
      CURLOPT_URL => "https://api.canva.com/print/v1/keys",
      CURLOPT_CUSTOMREQUEST => "GET",
      CURLOPT_RETURNTRANSFER => true,
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

    url = URI('https://api.canva.com/print/v1/keys')
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true

    request = Net::HTTP::Get.new(url)

    response = http.request(request)
    puts response.read_body
    ```
  </Tab>
</Tabs>

## Success response

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

<Prop.List>
  <Prop name="keys" type="EdDsaJwk[]" required mode="output">
    A JSON Web Key Set (JWKS) with public keys used for signing requests. You can use this JWKS to verify that a request was sent from Canva.

    <PillAccordion title={<>Properties of <strong>keys</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="kid" type="string" required mode="output">
          The key ID, a unique identifier for the public key. When the keys used to sign requests are rotated, you can use this ID to select the correct key within a JWKS during the key rollover. This value is case-sensitive.
        </Prop>

        <Prop name="kty" type="string" required mode="output">
          The key type, which identifies the cryptographic algorithm family used with the key, such as `RSA` or `EC`. Only Octet Key Pairs (OKPs) are supported.
          This value is case-sensitive. For more information, see [RFC-8037](https://www.rfc-editor.org/rfc/rfc8037.html#section-2).
        </Prop>

        <Prop name="crv" type="string" required mode="output">
          The curve property, which identifies the curve used for elliptical curve encryptions. Only `Ed25519` is supported. For more information, see [RFC-8037](https://www.rfc-editor.org/rfc/rfc8037.html#section-2).
        </Prop>

        <Prop name="x" type="string" required mode="output">
          The public key of an elliptical curve encryption. The key
          is encoded with `Base64urlUInt`. For more information, see [RFC-8037](https://www.rfc-editor.org/rfc/rfc8037#section-2).
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

## Example response

```json
{
  "keys": [
    {
      "kid": "a418dc7d-ecc5-5c4b-85ce-e1104a8addbe",
      "kty": "OKP",
      "crv": "Ed25519",
      "x": "aIQtqd0nDfB-ug0DrzZbwTum-1ITdXvKxGFak_1VB2j"
    },
    {
      "kid": "c8de5bec1-1b88-4ddaae04acc-ce415-5d7",
      "kty": "OKP",
      "crv": "Ed25519",
      "x": "m2d1FT-gfBXxIzKwdQVTra0D-aBq_ubZ1jI0GuvkDtn"
    }
  ]
}
```
