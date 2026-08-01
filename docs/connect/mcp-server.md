Source: https://www.canva.dev/docs/connect/mcp-server/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/connect/llms.txt
> Use this file to discover all available pages before exploring further.

# Dev MCP server

How to configure the Canva Dev MCP server for an AI-assisted developer experience.

NOTE: Looking for an MCP server to help with your Canva designs? Check out the [Canva MCP server](/docs/connect/canva-mcp-server-setup/).

The Canva Dev Model Context Protocol (MCP) server provides AI-powered development assistance for Canva apps and integrations. By connecting your preferred MCP client (such as Cursor, Claude Desktop, or other compatible tools) to canva.dev, you can access specialized tools and documentation to enhance your development workflow.

## Before you begin

To follow this guide, you'll need to install the following prerequisites:

* git
* Node.js v24 (or later)
* npm
* A compatible MCP client. For example, Cursor, Claude Desktop.

If you need help with any of these prerequisites, including how to set up the required tooling, see the Canva Apps documentation.

## Step 1: Configure your MCP client

Each MCP client requires specific configuration to communicate with the Canva Dev MCP server. Follow the instructions below for your client.

<Tabs>
  <Tab name="Cursor">
    NOTE: MCP tools are currently only available in Agent mode.

    You can automatically set up the MCP server using this [Cursor configuration link](cursor://anysphere.cursor-deeplink/mcp/install?name=canva-dev). Alternatively, you can manually create the configuration with the following steps:

    1. In your project directory, create the configuration directory and file:

       ```shell
       mkdir -p .cursor
       touch .cursor/mcp.json
       ```

    2. Add the following configuration to `.cursor/mcp.json`:
       ```json
       {
         "mcpServers": {
           "canva-dev": {
             "command": "npx",
             "args": [
               "-y",
               "@canva/cli@latest",
               "mcp"
             ]
           }
         }
       }
       ```

    For more information, see the [Cursor MCP documentation](https://docs.cursor.com/context/model-context-protocol#configuring-mcp-servers).
  </Tab>

  <Tab name="Claude Desktop">
    1. Open Claude Desktop Settings:
       * On Windows, use the keyboard shortcut `Ctrl + ,`.
       * On macOS, use the keyboard shortcut `Command + ,`.
    2. Navigate to the **Developer** tab.
    3. Click **Edit Config** and add the following configuration to the config file:

       ```json
       {
         "mcpServers": {
           "canva-dev": {
             "command": "npx",
             "args": [
               "-y",
               "@canva/cli@latest",
               "mcp"
             ]
           }
         }
       }
       ```

    For more information, see the [MCP quickstart guide](https://modelcontextprotocol.io/quickstart/user).
  </Tab>

  <Tab name="Claude Code">
    Run the following command in your terminal:

    ```shell
    claude mcp add canva-dev -- npx -y @canva/cli@latest mcp
    ```

    For more information, see the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/mcp)
  </Tab>

  <Tab name="VS Code">
    NOTE: MCP tools are only available in Agent mode.

    1. In your workspace, create the VS Code configuration directory and file:

       ```shell
       mkdir -p .vscode
       touch .vscode/mcp.json
       ```

    2. Add the following to `.vscode/mcp.json`:

       ```json
       {
         "servers": {
           "canva-dev": {
             "type": "stdio",
             "command": "npx",
             "args": [
               "-y",
               "@canva/cli@latest",
               "mcp"
             ]
           }
         }
       }
       ```

    For more information, see the [VS Code MCP documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).
  </Tab>
</Tabs>

## Step 2: Restart your MCP client

1. Save all configuration changes.
2. Restart your MCP client (for example, Cursor, Claude Desktop, or VS Code) to apply the new settings.

## Step 3: Verify the connection

To confirm the MCP server is working:

* Look for visual indicators in your client.

  For example, in Claude Desktop, click the **+** button at the bottom of the chat box, and select **Connectors** > **Manage connectors** to see the connected local "Desktop" MCP servers and their available tools.

* Ask a simple question to test the connection. For example:

  > How many components are in the App UI Kit?

  If your connection is successful, your client should display a tool invocation prompt for you to accept.

## Troubleshooting

* If your MCP client can't find enabled tools:

  1. Make sure the MCP server is configured correctly (see [Step 1](#step-1-configure-your-mcp-client)).
  2. Restart the application to refresh your client.
* If you receive incorrect or inconsistent responses:
  * Try starting a new chat session to reset the conversation context.
  * Be specific in your queries and include relevant keywords such as "App UI Kit" or "Apps SDK".
  * Request explicit references to Canva documentation.

## Security and privacy

The MCP server operates locally on your device, fetching Canva documentation from canva.dev and other sources. Your AI agent receives context and information regarding your Canva app or integration, and uses it to enhance its output and recommendations. The MCP server doesn't transmit your code or prompts to any other sources other than to your AI agent or LLM tool.
