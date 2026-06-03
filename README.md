# Canva Developers Documentation — LLM-Ready Markdown Dump

**377 markdown files** covering every page from the [Canva Developers documentation](https://www.canva.dev/docs/).

This repo is designed for **LLM ingestion, RAG pipelines, and knowledge graph exploration** — so AI assistants can answer questions about Canva's developer platform without hitting API rate limits or crawling docs on the fly.

## Contents

| Section | Files | Source |
|---------|-------|--------|
| **Apps SDK** | 200+ pages | [/docs/apps/](https://www.canva.dev/docs/apps/) |
| **Connect APIs** | 80+ pages | [/docs/connect/](https://www.canva.dev/docs/connect/) |
| **MCP** | 6 pages | [/docs/mcp/](https://www.canva.dev/docs/mcp/) |
| **SCIM API** | 13 pages | [/docs/scim/](https://www.canva.dev/docs/scim/) |
| **Audit Logs** | 22 pages | [/docs/audit-logs/](https://www.canva.dev/docs/audit-logs/) |

## Quick Start

```bash
# Clone
git clone https://github.com/naelrudd/canva-docs.git
cd canva-docs

# Feed the markdown files directly to your LLM
cat *.md | your-llm-prompt

# Or use with a RAG tool like graphify (see graphify/ folder)
```

## Using with LangChain / LlamaIndex / Custom RAG

All files are flat markdown with no frontmatter. Each file has a `Source:` header linking back to the original URL.

```python
from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader("path/to/canva-docs", glob="**/*.md")
docs = loader.load()
```

## Using as Context for Claude / ChatGPT / Gemini

```bash
# Concatenate everything
cat *.md > canva-docs-complete.txt

# Or select a section
cat docs-apps-*.md > apps-sdk.txt
```

## Knowledge Graph

This repo includes [graphify](https://github.com/safishamsi/graphify) (forked) — turn the entire docset into a queryable knowledge graph.

### Quick Start

```bash
# Set at least one API key (see .env.example)
# Supports: GOOGLE_API_KEY, OPENAI_API_KEY, ANTHROPIC_API_KEY, DEEPSEEK_API_KEY, etc.
# For Google Gemini: multiple keys can be space/comma-separated for automatic rotation on quota limits
$env:GOOGLE_API_KEY = "key1 key2 key3"

# Run the full pipeline (extraction → clustering → report)
python _run_graphify.py
```

The script auto-detects available backends, installs graphify if missing, and retries with the next API key if rate-limited (429).

### Output

Output lands in `graphify-out/`:
- **graph.json** — raw GraphRAG-ready JSON (5094 nodes, 9622 edges)
- **GRAPH_REPORT.md** — audit report with god nodes and community analysis
- **manifest.json** — incremental extraction cache (re-run is free for unchanged files)

## License

The markdown files are sourced from [Canva Developers](https://www.canva.dev/docs/) and are subject to Canva's terms.

The wrapper scripts and configuration in this repo (`_run_graphify.py`, `.env.example`, etc.) are MIT-licensed — see [LICENSE](LICENSE).

The [graphify](https://github.com/safishamsi/graphify) tool is MIT-licensed.
