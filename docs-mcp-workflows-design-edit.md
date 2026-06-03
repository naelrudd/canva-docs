Source: https://www.canva.dev/docs/mcp/workflows/design-edit/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/mcp/llms.txt
> Use this file to discover all available pages before exploring further.

# Design edit handoff

After your agent generates, modifies, or lists a design, always give users a way to open and edit it in Canva.

When an agent creates or edits a design on someone's behalf, the work isn't done. The user still needs to review it, tweak it, and make it their own. If your integration doesn't surface a way back into Canva, users are stuck — they've got a result they can't act on.

This pattern is called design edit handoff: after any design-touching operation, your agent should return a direct link to the design so the user can immediately open it in Canva.

## When to apply it

Apply the handoff pattern whenever your agent calls one of these tools:

| Tool                                                       | Why a handoff is needed                                                                  |
| :--------------------------------------------------------- | :--------------------------------------------------------------------------------------- |
| `generate-design` + `create-design-from-candidate`         | User may need to refine the generated result such as adjusting layout, copy, or visuals. |
| `autofill-design`                                          | Autofilled content may need a final human check.                                         |
| `search-designs` / `get-design`                            | User may want to open a listed design directly.                                          |
| `start-editing-transaction` + `commit-editing-transaction` | User should verify and continue edits after programmatic changes.                        |
| `resize-design`                                            | User may want to fine-tune the resized output.                                           |
| `import-design-from-url`                                   | User may want to edit the imported design.                                               |

If your agent touches a design in any way, include a handoff link.

## What to include in the response

Every design-touching tool response should surface two things:

1. The design's edit URL — a direct link that opens the design in the Canva editor.
2. A clear call to action — a short prompt that tells the user they can open and edit it.

### Edit URL format

Most design-touching tools return an edit URL directly in their response:

* `edit_url` — returned by tools such as `search-designs` and `get-design`, as a top-level field
* `design_summary.urls.edit_url` — returned by `create-design-from-candidate`, nested under `design_summary.urls`
* `edit_design_url` — returned by `start-editing-transaction`, as a top-level field

Use whichever field the tool returns. If you need to construct an edit URL from a `design_id`, use this format:

```text
https://www.canva.com/design/{design_id}/edit
```

The `design_id` is returned in the response of all design-creating and design-fetching tools. In `create-design-from-candidate` responses, it's available as `design_summary.id`.

For example, the response from `create-design-from-candidate` looks like this:

```json
{
  "design_summary": {
    "id": "DAHFr228rsU",
    "title": "Cobalt Blue Instagram Post with 'Hello World'",
    "urls": {
      "edit_url": "https://www.canva.com/d/...",
      "view_url": "https://www.canva.com/d/..."
    },
    ...
  }
}
```

Your agent should present this to the user like:

```text
Your design is ready. Open in Canva to edit ↗
```

## How to implement it

1. Get the edit URL from the tool response.

   The edit URL field location varies by tool. Use whichever is present, or construct it from the `design_id` as a fallback:

   ```typescript
    const editUrl =
     toolResponse.edit_url ??
     toolResponse.edit_design_url ??
     toolResponse.design_summary?.urls?.edit_url ??
     `https://www.canva.com/design/${toolResponse.design_id ?? toolResponse.design_summary?.id}/edit`;
   ```

2. Include the edit URL in your agent's final response.

   Pass the edit URL into your LLM's context so it can surface the link to the user. Add it to your system prompt or tool result handling:

   ```typescript
    const systemPrompt = `
      After any tool call that creates, modifies, or retrieves a design, always include a direct link for the user to open and edit the design in Canva. Use the format: https://www.canva.com/design/{design_id}/edit

      Present it clearly as a call to action, e.g.: "Your design is ready. Open it in Canva to review and edit."
    `;
   ```

3. Handle listing tools.

   When returning a list of designs (e.g., from `search-designs`), include an edit URL for each item in the list — not just the first result.

   ```typescript
    const designs = toolResponse.items.map((design) => ({
      ...design,
      edit_url:
        design.edit_url ??
        `https://www.canva.com/design/${design.design_id}/edit`,
    }));
   ```

## What not to do

* Don't end the workflow at export. `export-design` gives users a static file. It's a delivery mechanism, not a handoff. Always offer the edit URL alongside or before an export.
* Don't skip the handoff for "read-only" operations. Even when listing or retrieving designs, users often want to jump straight into editing. Include the link.
* Don't bury the link. The edit URL should be one of the first things a user sees after an operation completes, not an afterthought at the bottom of a long response.

## Learn more

* [MCP tools and rate limits](https://www.canva.dev/docs/mcp/tools/)
* [Usage policy](https://www.canva.dev/docs/mcp/usage-policy/)
