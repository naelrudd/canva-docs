Source: https://www.canva.dev/docs/apps/canva-cli/

# Canva CLI

CLI for creating and managing Canva Apps.

## Requirements

* Node.js `v24`
* npm `v11`
* A [Canva account](https://www.canva.com/developers)

## Quickstart

```shell
npm install -g @canva/cli@latest
canva login
canva apps create "My New App" --template="hello_world" --distribution="public" --git --installDependencies
cd my-new-app
npm start
```

## CLI Reference

### Commands

* `canva welcome` - Show welcome page
* `canva tip` - Print random development tip
* `canva bug` - Raise an issue on GitHub
* `canva login` - Log in to the CLI
* `canva logout` - Log out and revoke access
* `canva mcp` - Start the MCP server
* `canva apps` - Manage apps
  * `canva apps create` - Create a new app
  * `canva apps list` - List all apps
  * `canva apps preview` - Preview your app
  * `canva apps doctor` - Run diagnostics
  * `canva apps migrate <name>` - Run code migrations
  * `canva apps config` - Manage app configuration
  * `canva apps link` - Link to an existing app
