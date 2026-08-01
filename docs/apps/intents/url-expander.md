Source: https://www.canva.dev/docs/apps/intents/url-expander/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# URL Expander intent

Automatically import content from external URLs into Canva AI.

URL Expander is a type of [intent](https://www.canva.dev/docs/apps/intents/) that enables users to seamlessly import content from external URLs directly into Canva when using Canva AI.

When users paste URLs into Canva AI, your app can recognize supported URLs, fetch the associated content, and add it as context. This creates a frictionless experience where users can simply paste a link and immediately work with the content in their design.

Implementing this intent requires you to integrate Canva with your platform's content APIs to retrieve and deliver assets referenced by URLs.

Building with the URL Expander intent offers significant advantages:

* **Easy setup**: Canva handles the complex parts—URL recognition, content preview, and asset import flow.
* **App discovery**: Your app is discoverable by users contextually within Canva, increasing engagement and usage with your platform.
* **Built for scale**: Integrate across Canva surfaces. Whether users access Canva from desktop, mobile, or future surfaces, your app will have a seamless user experience.
* **Focus on what matters**: Spend your time building URL pattern matching and content retrieval logic, not wrestling with Canva integration mechanics.

**Warning:** The URL Expander intent is provided as a preview. Preview intents are unstable and may change without warning. You can't release public apps using a preview intent until it's stable.

<Grid columns={2} spacing="2u">
  <div>
    ## App requirements

    * [ ] Your app must have a backend to fetch content from URLs.
    * [ ] Your app must register URL patterns that identify expandable URLs.
    * [ ] This intent requires you to implement content retrieval APIs to fetch assets from your platform.
  </div>

  <div>
    ## APIs this intent uses

    * [`prepareUrlExpander`](https://www.canva.dev/docs/apps/api/preview/intents-asset-prepare-url-expander/)

    ## Required scopes

    * Asset write ([`canva:asset:private:write`](https://www.canva.dev/docs/apps/configuring-scopes/#canvaassetprivatewrite))
  </div>
</Grid>

## Next steps

* Have a look at the URL Expander intent [example app](https://www.canva.dev/docs/apps/examples/url-expander-intent/) for inspiration.
* For instructions on implementing this intent, follow the URL Expander intent [implementation guide](https://www.canva.dev/docs/apps/intents/url-expander/implementation-guide/).
