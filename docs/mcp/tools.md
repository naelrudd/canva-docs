Source: https://www.canva.dev/docs/mcp/tools/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/mcp/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP tools and rate limits

See all the available tools, their rate limits, and plan availability for the Canva MCP server.

The Canva MCP implements rate limits for each tool to ensure service stability. Rate limits are measured in requests per minute (req/min).

## Assets

| MCP tool                | Rate limit  | Plan availability |
| ----------------------- | ----------- | ----------------- |
| `upload-asset-from-url` | 30 req/min  | All plans         |
| `get-assets`            | 100 req/min | All plans         |

## Autofill

| MCP tool                     | Rate limit  | Plan availability |
| ---------------------------- | ----------- | ----------------- |
| `autofill-design`            | 10 req/min  |  Enterprise only  |
| `get-brand-template-dataset` | 100 req/min |  Enterprise only  |

## Brand templates

| MCP tool                 | Rate limit  | Plan availability |
| ------------------------ | ----------- | ----------------- |
| `search-brand-templates` | 100 req/min |  Enterprise only  |
| `list-brand-kits`        | 100 req/min |  Enterprise only  |

## Comments

| MCP tool            | Rate limit  | Plan availability |
| ------------------- | ----------- | ----------------- |
| `comment-on-design` | 100 req/min | All plans         |
| `reply-to-comment`  | 20 req/min  | All plans         |
| `list-comments`     | 100 req/min | All plans         |
| `list-replies`      | 100 req/min | All plans         |

## Designs

| MCP tool                       | Rate limit  | Plan availability |
| ------------------------------ | ----------- | ----------------- |
| `search-designs`               | 100 req/min | All plans         |
| `get-design`                   | 100 req/min | All plans         |
| `get-design-pages`             | 100 req/min | All plans         |
| `get-design-content`           | 100 req/min | All plans         |
| `get-presenter-notes`          | 100 req/min | All plans         |
| `get-design-export-formats`    | 100 req/min | All plans         |
| `generate-design`              | 20 req/min  | All plans         |
| `create-design-from-candidate` | 20 req/min  | All plans         |
| `request-outline-review`       | 20 req/min  | All plans         |
| `generate-design-structured`   | 20 req/min  | All plans         |

## Design imports

| MCP tool                 | Rate limit | Plan availability |
| ------------------------ | ---------- | ----------------- |
| `import-design-from-url` | 20 req/min | All plans         |

## Exports

| MCP tool        | Rate limit | Plan availability |
| --------------- | ---------- | ----------------- |
| `export-design` | 20 req/min | All plans\*       |

<Note>
  The `export-design` tool is available on all plans, but the plan affects output quality:

  * **Free plans:** Standard quality export
  * **Canva Pro and above:** Pro quality with lossless PNG, transparent backgrounds, and premium element export
  * **All plans:** If a design contains premium elements, export may fail with `license_required`
</Note>

## Folders

| MCP tool              | Rate limit  | Plan availability |
| --------------------- | ----------- | ----------------- |
| `create-folder`       | 20 req/min  | All plans         |
| `list-folder-items`   | 100 req/min | All plans         |
| `search-folders`      | 100 req/min | All plans         |
| `move-item-to-folder` | 100 req/min | All plans         |

## Resizes

| MCP tool        | Rate limit | Plan availability |
| --------------- | ---------- | ----------------- |
| `resize-design` | 20 req/min |  Pro and above    |

## Editing transactions

| MCP tool                     | Rate limit  | Plan availability |
| ---------------------------- | ----------- | ----------------- |
| `start-editing-transaction`  | 20 req/min  | All plans         |
| `perform-editing-operations` | 50 req/min  | All plans         |
| `commit-editing-transaction` | 20 req/min  | All plans         |
| `cancel-editing-transaction` | 20 req/min  | All plans         |
| `get-design-thumbnail`       | 100 req/min | All plans         |

## Plan availability legend

* &#x20;**Enterprise only:** Feature is only available to Canva Enterprise customers
* &#x20;**Pro and above:** Feature is available to Canva Pro, Business, and Enterprise plans
* **All plans:** Feature is available to all Canva users
