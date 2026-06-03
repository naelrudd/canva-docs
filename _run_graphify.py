"""
Run graphify full extraction pipeline on the Canva docs corpus.

Supports automatic API key rotation when rate-limited (429).

Usage:
    python _run_graphify.py

Environment variables:
    GOOGLE_API_KEY       — single key, or comma/space-separated list for rotation
    GEMINI_API_KEY       — alias for GOOGLE_API_KEY (lower priority)
    GRAPHIFY_BACKEND     — force a specific backend (default: auto-detect)
    GRAPHIFY_MODEL       — force a specific model (default: backend default)
"""

import os
import subprocess
import sys
import time

# ── Ensure graphify is installed ────────────────────────────────────────────
try:
    import graphify.llm as _glm
except ImportError:
    print("[run_graphify] graphify not found — installing...")
    ret = subprocess.run(
        [sys.executable, "-m", "pip", "install", "graphifyy"],
        capture_output=True, text=True,
    )
    if ret.returncode != 0:
        print(f"[run_graphify] install failed:\n{ret.stderr}", file=sys.stderr)
        sys.exit(1)
    print("[run_graphify] graphify installed")
    import graphify.llm as _glm


def _parse_keys(raw: str | None) -> list[str]:
    """Parse comma/space-separated keys into a list."""
    if not raw:
        return []
    return [k.strip() for k in raw.replace(",", " ").split() if k.strip()]


ALL_GOOGLE_KEYS = _parse_keys(os.environ.get("GOOGLE_API_KEY")) or _parse_keys(os.environ.get("GEMINI_API_KEY"))
ALL_OPENAI_KEYS = _parse_keys(os.environ.get("OPENAI_API_KEY"))

def _key_rotation_context(keys: list[str], *, env_var: str):
    """Cycle through API keys when 429 is detected. Yields each key, then None."""
    for idx, key in enumerate(keys):
        os.environ[env_var] = key
        print(f"[run_graphify] using API key {idx + 1}/{len(keys)}: ...{key[-8:]}")
        yield key
    yield None  # signal exhaustion


# ── Patch OpenAI-compatible base URL before graphify loads ──────────────────
custom_openai_url = (
    os.environ.get("OPENAI_BASE_URL")
    or os.environ.get("OPENAI_COMPATIBLE_BASE_URL")
)
if custom_openai_url:
    _glm.BACKENDS["openai"]["base_url"] = custom_openai_url

# ── Import graphify CLI entry point ─────────────────────────────────────────
from graphify.__main__ import main as _graphify_main


def _run_graphify(args: list[str]) -> None:
    """Run graphify main() and return; catches SystemExit."""
    sys.argv = ["graphify", *args]
    try:
        _graphify_main()
    except SystemExit as e:
        if e.code not in (None, 0):
            raise RuntimeError(f"graphify exited with code {e.code}")


def _run_with_retry(args: list[str], keys: list[str], *, env_var: str = "GOOGLE_API_KEY") -> None:
    """Run graphify extraction, retrying with next API key on 429."""
    if not keys:
        _run_graphify(args)
        return

    for key in _key_rotation_context(keys, env_var=env_var):
        if key is None:
            raise RuntimeError("All API keys exhausted. Extraction incomplete.")
        try:
            _run_graphify(args)
            return
        except Exception as exc:
            err_str = str(exc).lower()
            if "429" in err_str or "rate limit" in err_str or "quota" in err_str:
                print(f"[run_graphify] rate limited, rotating key...")
                time.sleep(5)
                continue
            raise


if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))

    # ── Detect backend ─────────────────────────────────────────────────────
    backend_override = os.environ.get("GRAPHIFY_BACKEND")
    model_override = os.environ.get("GRAPHIFY_MODEL")

    if backend_override:
        backend = backend_override
    else:
        backend = _glm.detect_backend()
        if backend is None:
            print(
                "error: no API key found. "
                "Set one of: GEMINI_API_KEY, GOOGLE_API_KEY, OPENAI_API_KEY, "
                "MOONSHOT_API_KEY, ANTHROPIC_API_KEY, DEEPSEEK_API_KEY. "
                "See .env.example for all options.",
                file=sys.stderr,
            )
            sys.exit(1)

    print(f"[run_graphify] using backend: {backend}")
    if model_override:
        print(f"[run_graphify] using model:  {model_override}")

    # ── Determine keys for rotation ────────────────────────────────────────
    rotation_keys: list[str] = []
    rotation_env: str = "GOOGLE_API_KEY"
    if backend == "gemini":
        rotation_keys = ALL_GOOGLE_KEYS
        if rotation_keys:
            print(f"[run_graphify] {len(rotation_keys)} Gemini API key(s) available for rotation")
    elif backend in ("openai", "kimi", "deepseek"):
        rotation_keys = ALL_OPENAI_KEYS
        rotation_env = "OPENAI_API_KEY"
        if rotation_keys:
            print(f"[run_graphify] {len(rotation_keys)} OpenAI API key(s) available for rotation")

    extract_args = [
        "extract", project_root,
        "--out", project_root,
        "--backend", backend,
        "--max-concurrency", "1",
    ]
    if model_override:
        extract_args.extend(["--model", model_override])

    # Step 1: Full extraction (incremental if graph.json exists)
    print("\n=== Step 1: Extraction ===\n")
    _run_with_retry(extract_args, rotation_keys, env_var=rotation_env)

    # Step 2: Regenerate report + clusters (graph.html skipped if >5000 nodes)
    print("\n=== Step 2: Report + Clustering ===\n")
    _run_graphify(["cluster-only", project_root])

    print("\n=== Done ===")
