Source: https://www.canva.dev/docs/apps/intents/design-editor/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Design Editor intent

Create apps that add design tools to Canva.

Design Editor is a type of [intent](https://www.canva.dev/docs/apps/intents/) that enables users to interact with the Canva design editor and create specialized editing tools that appear alongside the Canva design surface.

The Design Editor intent is the default intent for Canva apps, and the APIs and functionality provided by this intent include those available before the introduction of intents. The Design Editor intent provides a standardized way to render apps within the Canva editor and ensures better compatibility with future Canva features.

NOTE: For apps that were created before the introduction of intents, we recommend migrating to explicitly use the Design Editor intent. For more information, see the [Design Editor intent migration guide](https://www.canva.dev/docs/apps/upgrades-and-migrations/design-editor-migration-guide/).



<Grid columns={2} spacing="2u">
  <div>
    ## App requirements

    There are no specific requirements for apps using the Design Editor intent, but APIs you implement within the intent may have specific requirements or design guidelines.
  </div>

  <div>
    ## APIs this intent uses

    * [`prepareDesignEditor`](https://www.canva.dev/docs/apps/api/latest/intents-design-prepare-design-editor/)
    * Other APIs that work with design content.

    ## Required scopes

    The Design Editor intent doesn't require any scopes, but APIs you implement within the intent may require additional scopes to work properly.
  </div>
</Grid>

## Next steps

* For instructions on implementing this intent, follow the Design Editor intent [implementation guide](https://www.canva.dev/docs/apps/intents/design-editor/implementation-guide/).
* If you have an existing app using the legacy direct render pattern, follow the [Design Editor intent migration guide](https://www.canva.dev/docs/apps/upgrades-and-migrations/design-editor-migration-guide/) to upgrade your app to use the Design Editor intent.
* After setting up the Design Editor intent, use the available APIs, such as the [Design Editing API](https://www.canva.dev/docs/apps/design-editing/), to interact with the user's design.
