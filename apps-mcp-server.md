Source: https://www.canva.dev/docs/apps/mcp-server/

# Dev MCP server

How to configure the Canva Dev MCP server for an AI-assisted developer experience.

## Prerequisites

* git
* Node.js v24 (or later)
* npm
* A compatible MCP client (Cursor, Claude Desktop, etc.)

## Step 1: Configure your MCP client

### Cursor
Create `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "canva-dev": {
      "command": "npx",
      "args": ["-y", "@canva/cli@latest", "mcp"]
    }
  }
}
```

### Claude Desktop
Edit Claude Desktop config:
```json
{
  "mcpServers": {
    "canva-dev": {
      "command": "npx",
      "args": ["-y", "@canva/cli@latest", "mcp"]
    }
  }
}
```

### Claude Code
```shell
claude mcp add canva-dev -- npx -y @canva/cli@latest mcp
```

### VS Code
Create `.vscode/mcp.json`:
```json
{
  "servers": {
    "canva-dev": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@canva/cli@latest", "mcp"]
    }
  }
}
```

## Security and privacy

The MCP server operates locally on your device, fetching Canva documentation from canva.dev. It doesn't transmit your code or prompts to other sources.
