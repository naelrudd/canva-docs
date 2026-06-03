Source: https://www.canva.dev/docs/apps/quickstart/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

Get an app up and running in a matter of minutes.

Canva's app development platform allows anyone to create apps that enhance Canva. This guide explains how to get an app up and running in a matter of minutes.

## Before you begin

To follow this guide, you'll need to:

* Sign up for a [Canva](https://www.canva.com/) account.
* Install git, Node.js `v24`, and npm `v11`.
* Learn the fundamentals of TypeScript, React, and webpack.

If you need help with any of these prerequisites, including how to set up the required tooling, see [Prerequisites](https://www.canva.dev/docs/apps/prerequisites/). If you need help with the Canva CLI, use the `--help` flag for more information.

### Public vs. team apps

Before creating an app, you must decide who your app is for.

* Public apps are created for release to the general public. After they're [reviewed by Canva](https://www.canva.dev/docs/apps/app-review-process/) and released, they can be discovered in the Apps Marketplace.
* Team apps are created solely for a team using Canva, such as an app created to integrate into a specific system. These apps aren't available to the general public. Your team administrators review and approve team apps.

AVAILABILITY: Team apps are only available to [teams](https://www.canva.com/for-teams/) on an [Enterprise plan](https://www.canva.com/enterprise/).

## Step 1: Create an app

<Tabs storageKey="apps-quickstart">
  <Tab name="CLI">
    1. Install the [Canva CLI](https://www.npmjs.com/package/@canva/cli) globally:

       ```shell
       npm install -g @canva/cli@latest
       ```

    2. Log in to the Canva CLI. This command opens an access request page in your browser:

       <GlobalContent>
         ```shell
         canva login
         ```
       </GlobalContent>

       <ChinaContent>
         ```shell
         canva login --cn
         ```
       </ChinaContent>

    3. Click **Allow** to grant the Canva CLI permission to manage your Canva apps.

    4. Copy the confirmation code shown, and paste it into the Canva CLI input.

    5. Run the `canva apps create` command to start the app creation process, or run the command with the following optional command flags. If they aren't set, the Canva CLI prompts you for a decision during the app creation process:

       * **App name**: Add your app's name after the `canva apps create` command as an argument. For example: `canva apps create "A New App"`.
       * **App template**: Select a template using the `--template` flag. Templates are pre-built starter projects that demonstrate common use cases and best practices. Available templates include `hello_world` (a minimal example), `data_connector` (for importing external data), `content_publisher` (for publishing to external platforms), and more. For a complete list, see [App templates](https://www.canva.dev/docs/apps/app-templates/).
       * **Audience**: Set the target audience using the `--distribution` flag. This flag is important because it restricts the target audience for your app:
         * `public`: You can make your app available to all of Canva's users, but the app will need to be reviewed by Canva and meet the requirements outlined in [the submission checklist](https://www.canva.dev/docs/apps/submission-checklist/).
         * `private`: The app can only be made available to members of the current [team](https://www.canva.com/for-teams/) on an [Enterprise plan](https://www.canva.com/enterprise/), and the team's administrators are responsible for reviewing it.
       * **Git**: Include a Git repository using the `--git` flag.
       * **Dependencies**: Install dependencies during the app creation process using the `--installDependencies` flag.

    This example creates an app named "My New App" that uses the `hello_world` template with `public` distribution, includes a Git repository, and installs the dependencies during the app creation process:

    ```shell
    canva apps create "My New App" --template="hello_world" --distribution="public" --git --installDependencies
    ```

    When the build process is complete, the Canva CLI automatically opens the [Developer Portal](https://www.canva.com/developers/) to your new app's configuration page.
  </Tab>

  <Tab name="Manual">
    1. Log in to the [Developer Portal](https://www.canva.com/developers/).

    2. Navigate to the [Your apps](https://www.canva.com/developers/apps) page.

    3. Click **Create an app**.

    4. Select a target audience for the app:

       * **Public**: You can make your app available to all of Canva's users, but the app will need to be reviewed by Canva and meet the requirements outlined in [the submission checklist](https://www.canva.dev/docs/apps/submission-checklist/).
       * **Restrict to your team**: The app can only be made available to members of the current [team](https://www.canva.com/for-teams/) on an [Enterprise plan](https://www.canva.com/enterprise/), and the team's administrators are responsible for reviewing it.

    5. Agree to the [terms and conditions](https://www.canva.com/policies/canva-developer-terms/).

    6. Click **Create**.
  </Tab>
</Tabs>

## Step 2: Set up and run the app

<Tabs storageKey="apps-quickstart">
  <Tab name="CLI">
    1. Change into the app's folder:

       ```shell
       cd my-new-app
       ```

    2. If you didn't use the `--installDependencies` flag when running the `canva apps create` command, or install the dependencies when prompted, manually install the dependencies:

       ```shell
       npm install
       ```

    3. Run the `npm` command to start your app:

       ```shell
       npm start
       ```

       The local development server starts running at [http://localhost:8080](http://localhost:8080), but you can't use this URL to view the local preview, see the next step instead.
  </Tab>

  <Tab name="Manual">
    1. Clone the following repo:

       ```shell
       git clone https://github.com/canva-sdks/canva-apps-sdk-starter-kit.git
       ```

       This repo contains the *starter kit* for the Apps SDK. The starter kit is a boilerplate for an app and all of the tooling we recommend. To learn more about the starter kit, see [Setting up the starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/).

    2. Navigate into the cloned directory for the starter kit:

       ```shell
       cd canva-apps-sdk-starter-kit
       ```

    3. Install the dependencies:

       ```shell
       npm install
       ```

    4. Start the local development server:

       ```shell
       npm run start
       ```

       The local development server starts running at [http://localhost:8080](http://localhost:8080), but you can't use this URL to view the local preview, see the next step instead.
  </Tab>
</Tabs>

## Step 3: Preview the app

This step explains how to use Canva to view the app running locally at [http://localhost:8080](http://localhost:8080).

1. In the [Developer Portal](https://www.canva.com/developers/apps), navigate to the app's **Code upload** page.
2. Select **App source > Development URL**.
3. In the **Development URL** field, enter the URL of the development server.
4. Click **Preview** to open the app in a preview Canva editor.
5. Click **Open** If this is the first time previewing your app.
6. If you're using Google Chrome, click **Allow** when prompted by your browser to allow local network access. For more information on this, see [Previewing apps](https://www.canva.dev/docs/apps/previewing-apps/#local-network-access-permission-required).

The example app includes a button that responds with "Hello world!" when clicked:



To learn more about how to preview apps, including how to set up live reloading, see [Previewing apps](https://www.canva.dev/docs/apps/previewing-apps/).

## Step 4: Start editing code

Use a code editor to open `src/intents/design_editor/app.tsx`. This file contains placeholder code that you can edit to start building your app.

In the following example, a button click triggers a wrapper method for [addElementAtPoint](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/), adding a new text layer to the Canva design with the words "Hello world!".

```tsx
import { Button, Rows, Text } from "@canva/app-ui-kit";
import { FormattedMessage, useIntl } from "react-intl";
import * as styles from "styles/components.css";
import { useFeatureSupport } from "@canva/app-hooks";

export const App = () => {
  const isSupported = useFeatureSupport();
  const addElement = [addElementAtPoint, addElementAtCursor].find((fn) =>
    isSupported(fn),
  );
  const onClick = () => {
    if (!addElement) {
      return;
    }

    addElement({
      type: "text",
      children: ["Hello world!"],
    });
  };

  const intl = useIntl();

  return (
    <div className={styles.scrollContainer}>
      <Rows spacing="2u">
        <Text>
          <FormattedMessage
            defaultMessage="
              To make changes to this app, edit the <code>src/app.tsx</code> file,
              then close and reopen the app in the editor to preview the changes.
            "
            description="
            Instructions for how to make changes to the app. Do not translate
            <code>src/app.tsx</code>.
            "
            values={{
              code: (chunks) => <code>{chunks}</code>,
            }}
          />
        </Text>
        <Button
          variant="primary"
          onClick={onClick}
          disabled={!addElement}
          tooltipLabel={!addElement ? intl.formatMessage({
              defaultMessage: "This feature is not supported in the current design",
              description: "Tooltip label for when a feature is not supported in the current design",
            }) : undefined}
            stretch
          >
          {intl.formatMessage({
            defaultMessage: "Do something cool",
            description:
              "Button text to do something cool. Creates a new text element when pressed.",
          })}
        </Button>
      </Rows>
    </div>
  );
};
```

## Step 5 (Optional): Setup the Canva Dev MCP Server

If you're using AI coding tools, such as Cursor or Claude Code, you can connect to the Canva Dev MCP Server to supercharge your development workflow. See this [setup guide](https://www.canva.dev/docs/connect/mcp-server/) to get started.

## Optional: Log out of the Canva CLI

When you log in to the Canva CLI using the `canva login` command, the Canva CLI generates an authentication token. The token prevents you from having to repeat an authentication step for every CLI request. The token is encrypted and stored in `~/.canva-cli/credentials` or `%USERPROFILE%\.canva-cli\credentials`, depending on your operating system.

You can use the `canva logout` command to revoke the token's access to your account as well as deleting the token file. Manually deleting the token file removes Canva CLI access, but doesn't revoke the token, so a copy of the token could reconnect the Canva CLI to your account.

Use the `canva logout` command to revoke access and delete the stored token.

```shell
canva logout
```

## Next steps

* You can use various Canva APIs to add functionality to your app. For more information, see [Integrating with Canva](https://www.canva.dev/docs/apps/integrating-canva/).
* If you plan to submit your app to the [Apps Marketplace](https://www.canva.com/your-apps/), you can prepare by reading the following:
  * [Design guidelines](https://www.canva.dev/docs/apps/design-guidelines/)
  * [App listing guidelines](https://www.canva.dev/docs/apps/app-listing-guidelines/)
  * [App review process](https://www.canva.dev/docs/apps/app-review-process/)
  * [Submission checklist](https://www.canva.dev/docs/apps/submission-checklist/)
  * [Submitting apps](https://www.canva.dev/docs/apps/submitting-apps/)
