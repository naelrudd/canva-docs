# Canva Developers Documentation — LLM-Ready Markdown

An unofficial, machine-readable mirror of the official [Canva Developers documentation](https://www.canva.dev/docs/) — **392 pages** mirrored as plain Markdown, organized 1:1 by URL path, for **LLM ingestion, RAG pipelines, and knowledge graph exploration**.

AI assistants can answer questions about Canva's developer platform without hitting API rate limits or crawling docs on the fly.

## Contents

| Section | Pages | Source |
|---------|-------|--------|
| **Apps SDK** | 209 | [`docs/apps/`](docs/apps.md) |
| **Connect APIs** | 120 | [`docs/connect/`](docs/connect.md) |
| **MCP** | 7 | [`docs/mcp/`](docs/mcp.md) |
| **SCIM API** | 15 | [`docs/scim/`](docs/scim.md) |
| **Audit Logs** | 24 | [`docs/audit-logs/`](docs/audit-logs.md) |
| **Print API** | 16 | [`docs/print/`](docs/print.md) |
| **Docs home** | — | [`docs.md`](docs.md) |

Each page is a Markdown file with a `Source:` header linking back to the original URL. The folder tree mirrors `www.canva.dev/docs/...` exactly, so `docs/apps/quickstart.md` ↔ `https://www.canva.dev/docs/apps/quickstart/`.

## Quick Start

```bash
git clone https://github.com/naelrudd/canva-docs.git
cd canva-docs

# Feed the markdown files directly to your LLM
cat docs/apps/*.md | your-llm-prompt

# Or explore a section
ls docs/connect/api-reference/
```

## Using as Context for Claude / ChatGPT / Gemini

```bash
# Concatenate everything
cat docs/**/*.md docs.md > canva-docs-complete.txt

# Or select a section
cat docs/apps/**/*.md > apps-sdk.txt
```

## Using with LangChain / LlamaIndex / Custom RAG

```python
from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader("path/to/canva-docs/docs", glob="**/*.md")
docs = loader.load()
```

For discovery, start from [`llms.txt`](llms.txt) (official index) or the curated [`INDEX.md`](INDEX.md). For the entire corpus in a single file, use [`llms-full.txt`](llms-full.txt).

## RAG Starter Kit

Local semantic search over the docs:

```bash
pip install chromadb
python rag.py build                    # index Markdown pages into ./rag_chroma
python rag.py query "your question"    # retrieve top-k relevant chunks
python rag.py info                     # corpus stats
```

Re-running `build` is idempotent and incremental.

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

## Updating

Re-mirror from the official index:

```bash
curl -sL -o llms.txt https://www.canva.dev/docs/llms.txt
# each section has its own llms.txt, e.g.
#   https://www.canva.dev/docs/apps/llms.txt
#   https://www.canva.dev/docs/connect/llms.txt
#   https://www.canva.dev/docs/print/llms.txt
# parse each https://www.canva.dev/docs/*.md link and download, preserving the URL path
```

## License & attribution

- This repository is **not affiliated with, endorsed by, or sponsored by Canva Pty Ltd.**
- All documentation content is © Canva Pty Ltd. and belongs to its respective owners. See [NOTICE.md](NOTICE.md).
- The wrapper scripts and configuration (`_run_graphify.py`, `.env.example`, etc.) are MIT-licensed — see [LICENSE](LICENSE).
- The [graphify](https://github.com/safishamsi/graphify) tool is MIT-licensed.
