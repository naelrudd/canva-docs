Source: https://www.canva.dev/docs/apps/intents/data-connector/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Connector intent

Create apps that import data from external sources.

<Availability>
  Apps using the Data Connector intent are only available to users on the following Canva plans: Canva Business, Canva Enterprise, Canva for Education, and Canva for Nonprofits.

  When the Data Connector intent is added to an existing app, users on the Canva Free plan with existing installations will be grandfathered. These users will retain full access after the restriction is applied to new installs, unless otherwise advised by Canva.
</Availability>

Data Connector is a type of [intent](https://www.canva.dev/docs/apps/intents/) that enables users to import data from external sources into Canva.

When users want to include data in their designs, they can browse available data sources, choose what specific data they need (like applying filters or selecting date ranges), and then import it. The data remains linked to its source, so users can refresh it later to get updated information without having to manually re-import everything.

Implementing this intent requires you to integrate Canva with your external data sources and their APIs.

Building with the Data Connector intent offers significant advantages:

* **Easy setup**: Canva handles the complex parts, such as data table rendering, refresh mechanisms, size limit enforcement, and error handling workflows.
* **App discovery**: Your app is discoverable by users contextually within Canva, increasing engagement and usage with your platform.
* **Built for scale**: Integrate across Canva surfaces. Whether users access Canva from desktop, mobile, or future surfaces, your app will have a seamless user experience.
* **Focus on what matters**: Spend your time building data source integrations and filtering capabilities, not wrestling with Canva integration mechanics.



<Grid columns={2} spacing="2u">
  <div>
    ## App requirements

    * [ ] You must use [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/) components.
    * [ ] This intent requires you to implement external data source APIs and data fetching logic.
    * [ ] Your app might need a backend to handle authentication for third-party platforms.
  </div>

  <div>
    ## APIs this intent uses

    * [`prepareDataConnector`](https://www.canva.dev/docs/apps/api/latest/intents-data-prepare-data-connector/)

    ## Required scopes

    * Design read ([`canva:design:content:read`](https://www.canva.dev/docs/apps/configuring-scopes/#canvadesigncontentread))
    * Design write ([`canva:design:content:write`](https://www.canva.dev/docs/apps/configuring-scopes/#canvadesigncontentwrite))
  </div>
</Grid>

## Next steps

* Have a look at the Data Connector intent [example app](https://www.canva.dev/docs/apps/examples/data-connector-intent/) for inspiration.
* For instructions on implementing this intent, follow the Data Connector intent [implementation guide](https://www.canva.dev/docs/apps/intents/data-connector/implementation-guide/).
* Make sure that you adhere to the Data Connector intent [design guidelines](https://www.canva.dev/docs/apps/design-guidelines/data-connector/) when using this intent.
