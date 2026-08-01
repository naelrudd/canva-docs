Source: https://www.canva.dev/docs/apps/intents/content-publisher/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Content Publisher intent

Integrate Canva with third-party content publishing platforms.

Content Publisher is a type of [intent](https://www.canva.dev/docs/apps/intents/) that enables users to publish Canva designs directly to external platforms.

When users want to publish their designs to an external platform, they can configure their publish settings and preview the content before publishing.

<Availability>
  Social scheduling apps using the Content Publisher intent are only available to users on the following Canva plans with premium features: Canva Pro, Canva Business, Canva Enterprise, Canva for Education, and Canva for Nonprofits. When the Content Publisher intent is added to an existing app, users on the Canva Free plan with existing installations will be grandfathered. These users will retain full access after the restriction is applied to new installs, unless otherwise advised by Canva.

  A social scheduling app is a third-party app (not owned by a social platform) that can create, publish, or schedule posts from inside Canva to a social network. This includes immediate posting, queues, recurring schedules, cross posting, and any background or timed publishing.
</Availability>

Implementing this intent requires you to integrate Canva with your third-party platform authentication and content publishing APIs.

Building with the Content Publisher intent offers significant advantages:

* **Easy setup**: Canva handles the complex parts—export processing, page selection, media delivery, and output type selection.
* **App discovery**: Your app is discoverable by users contextually within Canva, increasing engagement and usage with your platform.
* **Built for scale**: Integrate across Canva surfaces. Whether users access Canva from desktop, mobile, or future surfaces, your app will have a seamless user experience.
* **Focus on what matters**: Spend your time building platform-specific features and optimizations, not wrestling with Canva integration mechanics.

<Grid columns={2} spacing="2u">
  <div>
    ## App requirements

    * [ ] You must use [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/) components.
    * [ ] This intent requires you to implement third-party platform authentication and content publishing APIs.
    * [ ] Your app might need a backend to handle authentication for some third-party content platforms.
  </div>

  <div>
    ## APIs this intent uses

    * [`prepareContentPublisher`](https://www.canva.dev/docs/apps/api/latest/intents-content-prepare-content-publisher/)

    ## Required scopes

    * Design read ([`canva:design:content:read`](https://www.canva.dev/docs/apps/configuring-scopes/#canvadesigncontentread))
  </div>
</Grid>

## Next steps

* Have a look at the Content Publisher intent [example app](https://www.canva.dev/docs/apps/examples/content-publisher-intent/) for inspiration.
* For instructions on implementing this intent, follow the Content Publisher intent [implementation guide](https://www.canva.dev/docs/apps/intents/content-publisher/implementation-guide/).
* Make sure that you adhere to the Content Publisher intent [design guidelines](https://www.canva.dev/docs/apps/design-guidelines/content-publisher/) when using this intent.
