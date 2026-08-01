Source: https://www.canva.dev/docs/connect/api-reference/autofills/

# Autofill

The Canva Connect APIs for working with autofillable brand templates.

Brand templates were migrated to use a new ID format in September 2025.

AVAILABILITY: To use the Autofill APIs, your integration must act on behalf of a user who is a member of a Canva Enterprise organization.

The Autofill APIs let you create personalized designs using a brand template and input data. You can generate personalized invites, letters, training materials, pitch decks, marketing content, and more.

To autofill a brand template:
1. Use the Get brand template dataset API to check which fields you can fill.
2. Use the Create design autofill job API to start generating the design.
3. Use the Get design autofill job API to check the status and retrieve the design.

## Autofill APIs

* [Get brand template dataset](https://www.canva.dev/docs/connect/api-reference/brand-templates/get-brand-template-dataset/): Check if a brand template has autofillable fields.
* [Create design autofill job](https://www.canva.dev/docs/connect/api-reference/autofills/create-design-autofill-job/): Create an asynchronous job to generate a design from a brand template.
* [Get design autofill job](https://www.canva.dev/docs/connect/api-reference/autofills/get-design-autofill-job/): Get the status and results of the autofill job.
