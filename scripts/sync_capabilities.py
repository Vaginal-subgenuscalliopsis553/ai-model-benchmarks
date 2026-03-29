#!/usr/bin/env python3
"""
Syncs model capabilities from OpenRouter API into data/models.json.

Pulls: modalities, supported parameters, context limits, max output tokens.
Maps them into a structured `capabilities` object per model.

Usage:
    python scripts/sync_capabilities.py
    python scripts/sync_capabilities.py --dry-run
"""

import json
import sys
import argparse
from datetime import date
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent
MODELS_FILE = REPO_ROOT / "data" / "models.json"
OPENROUTER_API = "https://openrouter.ai/api/v1/models"

# Map OpenRouter supported_parameters to our capability flags
PARAM_TO_CAPABILITY = {
    "tools": "tool_calling",
    "structured_outputs": "structured_output",
    "reasoning": "reasoning",
    "logprobs": "logprobs",
    "web_search_options": "web_search",
    "response_format": "json_mode",
    "seed": "deterministic_seed",
}


def fetch_openrouter_models() -> list[dict]:
    """Fetch all models from OpenRouter API."""
    try:
        resp = requests.get(OPENROUTER_API, timeout=30)
        resp.raise_for_status()
        return resp.json().get("data", [])
    except requests.RequestException as e:
        print(f"ERROR: Failed to fetch OpenRouter models: {e}")
        sys.exit(1)


def load_json(path: Path) -> list:
    with open(path) as f:
        return json.load(f)


def save_json(path: Path, data: list):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {path}")


def extract_capabilities(or_model: dict) -> dict:
    """Extract structured capabilities from an OpenRouter model object."""
    arch = or_model.get("architecture", {})
    input_mods = set(arch.get("input_modalities", []))
    output_mods = set(arch.get("output_modalities", []))
    params = set(or_model.get("supported_parameters", []))
    top = or_model.get("top_provider", {})

    caps = {
        # Modalities
        "vision": "image" in input_mods,
        "audio_input": "audio" in input_mods,
        "audio_output": "audio" in output_mods,
        "video_input": "video" in input_mods,
        "file_input": "file" in input_mods,
        "image_output": "image" in output_mods,
        # Parameters → flags
        "tool_calling": "tools" in params,
        "structured_output": "structured_outputs" in params,
        "json_mode": "response_format" in params,
        "reasoning": "reasoning" in params,
        "web_search": "web_search_options" in params,
        "logprobs": "logprobs" in params,
        "deterministic_seed": "seed" in params,
        # Limits
        "context_length": top.get("context_length") or or_model.get("context_length"),
        "max_output_tokens": top.get("max_completion_tokens"),
        "is_moderated": top.get("is_moderated", False),
    }

    # Remove None limits (keep False booleans)
    return {k: v for k, v in caps.items() if v is not None}


def build_or_capability_map(or_models: list[dict]) -> dict[str, dict]:
    """Build map of openrouter_id -> capabilities."""
    cap_map = {}
    for m in or_models:
        model_id = m.get("id")
        if not model_id:
            continue
        cap_map[model_id] = extract_capabilities(m)
    return cap_map


def sync_capabilities(
    our_models: list[dict], cap_map: dict[str, dict], today: str
) -> tuple[list[dict], int, int]:
    """
    Merge capabilities into our models.
    Returns (updated_models, updated_count, skipped_count).
    """
    updated = 0
    skipped = 0

    for model in our_models:
        or_id = model.get("openrouter_id")
        if not or_id:
            skipped += 1
            continue

        caps = cap_map.get(or_id)
        if not caps:
            skipped += 1
            continue

        old_caps = model.get("capabilities", {})

        # Also sync context_length and max_output at top level
        if caps.get("context_length"):
            model["context_length"] = caps["context_length"]
        if caps.get("max_output_tokens"):
            model["max_output_tokens"] = caps["max_output_tokens"]

        # Build capabilities object (without limits — those are top-level)
        new_caps = {
            k: v
            for k, v in caps.items()
            if k not in ("context_length", "max_output_tokens")
        }
        new_caps["source"] = "openrouter"
        new_caps["updated"] = today

        if new_caps != old_caps:
            model["capabilities"] = new_caps
            updated += 1

    return our_models, updated, skipped


def print_summary(our_models: list[dict]):
    """Print capability coverage summary."""
    total = len(our_models)
    with_caps = sum(1 for m in our_models if m.get("capabilities"))
    with_vision = sum(1 for m in our_models if m.get("capabilities", {}).get("vision"))
    with_tools = sum(
        1 for m in our_models if m.get("capabilities", {}).get("tool_calling")
    )
    with_reasoning = sum(
        1 for m in our_models if m.get("capabilities", {}).get("reasoning")
    )
    with_structured = sum(
        1 for m in our_models if m.get("capabilities", {}).get("structured_output")
    )
    with_web = sum(1 for m in our_models if m.get("capabilities", {}).get("web_search"))
    with_max_out = sum(1 for m in our_models if m.get("max_output_tokens"))

    print(f"\n--- CAPABILITY COVERAGE ({with_caps}/{total} models) ---")
    print(f"  vision:            {with_vision}")
    print(f"  tool_calling:      {with_tools}")
    print(f"  reasoning:         {with_reasoning}")
    print(f"  structured_output: {with_structured}")
    print(f"  web_search:        {with_web}")
    print(f"  max_output_tokens: {with_max_out}")


def main():
    parser = argparse.ArgumentParser(
        description="Sync model capabilities from OpenRouter API"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Report changes without writing files"
    )
    args = parser.parse_args()

    today = date.today().isoformat()

    print("Fetching models from OpenRouter API...")
    or_models = fetch_openrouter_models()
    print(f"Fetched {len(or_models)} models from OpenRouter")

    cap_map = build_or_capability_map(or_models)
    our_models = load_json(MODELS_FILE)

    updated_models, updated_count, skipped_count = sync_capabilities(
        our_models, cap_map, today
    )

    print(
        f"\nUpdated: {updated_count} | Skipped (no openrouter_id match): {skipped_count}"
    )
    print_summary(updated_models)

    if args.dry_run:
        # Show sample
        for m in updated_models[:2]:
            if m.get("capabilities"):
                print(f"\nSample — {m['name']}:")
                print(json.dumps(m.get("capabilities", {}), indent=2))
        print("\nDry run — no files written.")
        return

    save_json(MODELS_FILE, updated_models)
    print(f"\nDone. Capabilities synced: {today}")


if __name__ == "__main__":
    main()
