Source: https://www.canva.dev/docs/scim/delete-user/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/scim/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a user

The Canva SCIM API doesn't implement a REST `DELETE` operation for a SCIM user.

To deprovision a SCIM user, you can use the `PATCH` operation to set the user's `active` attribute to `false`. For more information, see [Update individual attributes for a user](https://www.canva.dev/docs/scim/update-individual-attributes-user/).
