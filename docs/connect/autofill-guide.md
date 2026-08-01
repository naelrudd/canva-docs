Source: https://www.canva.dev/docs/connect/autofill-guide/

# Autofill guide

How to generate dynamic designs using Brand templates and the Autofill APIs.

This guide demonstrates how you can generate dynamic designs in Canva using brand templates, autofill, and the Connect APIs.

AVAILABILITY: To use the Brand template and Autofill APIs, your integration must act on behalf of a user that's a member of a Canva Enterprise organization.

## Prerequisites

### Create a Canva account
Your account must have MFA enabled and be a member of a Canva Enterprise organization.

### Create an integration
Make sure to set the following scopes:
* design:content: Read and Write
* design:meta: Read
* brandtemplate:meta: Read
* brandtemplate:content: Read
* asset: Read and Write

### Understanding autofill permissions
Integration developers must be members of a Canva Enterprise organization. Integration users must also be members of a Canva Enterprise organization.

## Create an autofillable template

1. Open the pre-built template containing three data fields: CITY (text), TEMPERATURE (text), BACKGROUND (image).
2. Publish your design as a brand template and note the brand template ID from the URL.

## Authenticate with OAuth

Follow the Authentication guide to get an authorization code, then generate an access token.

## Preparing assets for autofill

### Step 1. Upload your asset
Use the Create asset upload job API:

```shell
curl --request POST 'https://api.canva.com/rest/v1/asset-uploads' \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Content-Type: application/octet-stream' \
  --header 'Asset-Upload-Metadata: { "name_base64": "YmFja2dyb3VuZC5qcGc=" }' \
  --data-binary '@/path/to/your/image.jpg'
```

### Step 2. Get your asset upload job
Poll with GET /asset-uploads/{JOB-ID} until status is `success`.

### Limitations
* Only image assets can be used for autofill. Video assets are currently not supported.
* External image URLs are currently not supported for autofill.

## Generate an autofilled design

### Step 1. Query your brand template
Use Get brand template dataset API: `GET /brand-templates/{TEMPLATE-ID}/dataset`

### Step 2. Create a design autofill job
Use Create design autofill job API: `POST /autofills`

```shell
curl --request POST \
  --url https://api.canva.com/rest/v1/autofills \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "brand_template_id": "{TEMPLATE-ID}",
    "data": {
      "CITY": { "type": "text", "text": "Sydney" },
      "TEMPERATURE": { "type": "text", "text": "25C" },
      "BACKGROUND": { "type": "image", "asset_id": "{ASSET-ID}" }
    }
  }'
```

### Step 3. Get your design autofill job
Poll with `GET /autofills/{JOB-ID}` until status is `success`.

## Next steps

* Export the design using Create design export job.
* Move the design to a designated folder using Move folder item.
