#!/usr/bin/env python3
"""
V3: Extract hyper-entities using rigorous scoring framework.
Includes definition check and 9-axis qualification scoring (≥18/27 to qualify).
"""

import os
import json
import re
import sys
import time
from pathlib import Path
from datetime import datetime
from anthropic import Anthropic

# Unbuffer output for real-time progress
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

# Configuration
CONFIG = {
    "api_key_env": "ANTHROPIC_API_KEY",
    "model": "claude-3-5-haiku-20241022",  # Using Haiku until Sonnet/Opus recover
    "max_tokens": 8192,
    "temperature": 0.3,
    "chunk_size": 30000,  # Reduced for more thorough extraction per chunk
    "chunk_overlap": 3000,  # Increased overlap to catch entities spanning chunks
    "request_timeout": 120,
    "retry_attempts": 3,
    "retry_delay": 10,  # seconds between retries
    "sources_dir": "sources",
    "prompt_file": "extraction_prompt_v3.txt",
    "output_file": "results/hyperentities_extracted_v3.md",
    "progress_file": "results/progress_v3.json",
}


def load_extraction_prompt():
    """Load the v3 extraction prompt from file."""
    prompt_path = Path(CONFIG["prompt_file"])
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
    return prompt_path.read_text()


def get_all_markdown_files(sources_dir):
    """Recursively find all markdown files in the sources directory."""
    sources_path = Path(sources_dir)
    if not sources_path.exists():
        raise FileNotFoundError(f"Sources directory not found: {sources_path}")
    md_files = list(sources_path.rglob("*.md"))
    return sorted(md_files)


def smart_chunk_text(text, chunk_size, overlap):
    """Split text into chunks at paragraph boundaries with overlap."""
    if len(text) <= chunk_size:
        return [text]

    paragraphs = re.split(r'\n\n+', text)
    chunks = []
    current_chunk = []
    current_size = 0

    for para in paragraphs:
        para_size = len(para)

        if para_size > chunk_size:
            sentences = re.split(r'(?<=[.!?])\s+', para)
            for sentence in sentences:
                if current_size + len(sentence) > chunk_size and current_chunk:
                    chunks.append('\n\n'.join(current_chunk))
                    overlap_text = '\n\n'.join(current_chunk[-2:]) if len(current_chunk) >= 2 else current_chunk[-1] if current_chunk else ''
                    current_chunk = [overlap_text, sentence] if overlap_text else [sentence]
                    current_size = len(overlap_text) + len(sentence)
                else:
                    current_chunk.append(sentence)
                    current_size += len(sentence)
        else:
            if current_size + para_size > chunk_size and current_chunk:
                chunks.append('\n\n'.join(current_chunk))
                overlap_paras = current_chunk[-2:] if len(current_chunk) >= 2 else current_chunk[-1:] if current_chunk else []
                current_chunk = overlap_paras + [para]
                current_size = sum(len(p) for p in current_chunk)
            else:
                current_chunk.append(para)
                current_size += para_size

    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))

    return chunks


def extract_from_chunk(client, text_chunk, source_file, chunk_num, total_chunks, extraction_prompt):
    """Extract hyper-entities from a single chunk with retry logic."""
    chunk_context = ""
    if total_chunks > 1:
        chunk_context = f"\n\nNOTE: This is chunk {chunk_num} of {total_chunks} from this document.\n"

    full_prompt = f"{extraction_prompt}{chunk_context}\n\n---\n\nSOURCE FILE: {source_file}\n\nTEXT TO ANALYZE:\n\n{text_chunk}"

    # Retry logic for handling temporary API issues
    for attempt in range(CONFIG["retry_attempts"]):
        try:
            message = client.messages.create(
                model=CONFIG["model"],
                max_tokens=CONFIG["max_tokens"],
                temperature=CONFIG["temperature"],
                timeout=CONFIG["request_timeout"],
                messages=[{"role": "user", "content": full_prompt}]
            )

            return {
                "status": "success",
                "extraction": message.content[0].text,
                "tokens_used": {
                    "input": message.usage.input_tokens,
                    "output": message.usage.output_tokens,
                }
            }

        except Exception as e:
            error_str = str(e)

            # Check if it's a retryable error (overload, timeout, rate limit)
            is_retryable = any(x in error_str.lower() for x in ['overload', 'timeout', 'rate_limit', '529'])

            if is_retryable and attempt < CONFIG["retry_attempts"] - 1:
                wait_time = CONFIG["retry_delay"] * (attempt + 1)
                print(f"      ⚠ Attempt {attempt + 1} failed: {error_str[:100]}")
                print(f"      Retrying in {wait_time}s...")
                time.sleep(wait_time)
                continue
            else:
                return {
                    "status": "error",
                    "error": error_str,
                    "extraction": None,
                }

    return {
        "status": "error",
        "error": "Max retries exceeded",
        "extraction": None,
    }


def extract_hyperentities(client, text, source_file, extraction_prompt):
    """Extract hyper-entities with chunking if needed."""
    chunks = smart_chunk_text(text, CONFIG["chunk_size"], CONFIG["chunk_overlap"])
    num_chunks = len(chunks)

    if num_chunks > 1:
        print(f"    Split into {num_chunks} chunks")

    all_extractions = []
    total_input_tokens = 0
    total_output_tokens = 0

    for i, chunk in enumerate(chunks, 1):
        if num_chunks > 1:
            print(f"    Processing chunk {i}/{num_chunks}...", end=" ", flush=True)

        result = extract_from_chunk(client, chunk, source_file, i, num_chunks, extraction_prompt)

        if result["status"] == "success":
            all_extractions.append(result["extraction"])
            total_input_tokens += result["tokens_used"]["input"]
            total_output_tokens += result["tokens_used"]["output"]
            if num_chunks > 1:
                print(f"✓ ({result['tokens_used']['input']} in / {result['tokens_used']['output']} out)")
        else:
            print(f"✗ Error: {result.get('error', 'Unknown')}")
            return {
                "source_file": str(source_file),
                "status": "error",
                "error": f"Chunk {i} failed: {result.get('error', 'Unknown')}",
                "extraction": None,
            }

    if num_chunks > 1:
        combined_extraction = f"# Combined extraction from {num_chunks} chunks\n\n"
        for i, extraction in enumerate(all_extractions, 1):
            combined_extraction += f"## Chunk {i}/{num_chunks}\n\n{extraction}\n\n---\n\n"
    else:
        combined_extraction = all_extractions[0]

    return {
        "source_file": str(source_file),
        "status": "success",
        "extraction": combined_extraction,
        "num_chunks": num_chunks,
        "tokens_used": {
            "input": total_input_tokens,
            "output": total_output_tokens,
        },
        "doc_stats": {
            "characters": len(text),
            "lines": len(text.splitlines()),
        }
    }


def save_progress(results, completed_files):
    """Save progress to a JSON file."""
    output_path = Path(CONFIG["progress_file"])
    output_path.parent.mkdir(parents=True, exist_ok=True)

    progress_data = {
        "last_updated": datetime.now().isoformat(),
        "completed_files": completed_files,
        "total_results": len(results),
        "results": results,
    }

    with output_path.open("w") as f:
        json.dump(progress_data, f, indent=2)


def save_results_incrementally(result):
    """Append result to output file as we go."""
    output_path = Path(CONFIG["output_file"])
    output_path.parent.mkdir(parents=True, exist_ok=True)

    mode = "a" if output_path.exists() else "w"

    with output_path.open(mode) as f:
        if mode == "w":
            f.write("# Hyper-Entities Extraction Results (v3 - Rigorous Scoring)\n\n")
            f.write(f"**Extraction Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Methodology:** See METHODOLOGY.md for scoring framework\n")
            f.write(f"**Qualification Threshold:** ≥18/27 on Stage 1 scoring\n\n")
            f.write("---\n\n")

        if result["status"] == "success":
            f.write(f"## Source: {result['source_file']}\n\n")
            f.write(f"**Size:** {result['doc_stats']['characters']:,} chars, {result['doc_stats']['lines']} lines")
            if result.get('num_chunks', 1) > 1:
                f.write(f" | **Chunks:** {result['num_chunks']}")
            f.write(f" | **Tokens:** {result['tokens_used']['input']:,} in / {result['tokens_used']['output']:,} out")
            f.write("\n\n")
            f.write(result["extraction"])
            f.write("\n\n---\n\n")
        else:
            f.write(f"## Source: {result['source_file']}\n\n")
            f.write(f"**ERROR:** {result.get('error', 'Unknown error')}\n\n")
            f.write("---\n\n")

    # Flush to disk
    output_path.touch()


def main():
    """Main execution."""
    print("=" * 80)
    print("HYPER-ENTITIES EXTRACTION (v3 - RIGOROUS SCORING FRAMEWORK)")
    print("=" * 80)
    print()

    # Check for API key
    api_key = os.environ.get(CONFIG["api_key_env"])
    if not api_key:
        print(f"ERROR: {CONFIG['api_key_env']} environment variable not set.")
        print("\nTo set your API key:")
        print("  export ANTHROPIC_API_KEY='your-key'")
        print("\nOr source from .env file:")
        print("  export $(cat .env | grep -v '^#' | xargs)")
        return

    print("✓ API key found")

    # Initialize client
    client = Anthropic(api_key=api_key)

    # Load extraction prompt
    print("✓ Loading v3 extraction prompt...")
    extraction_prompt = load_extraction_prompt()
    print(f"✓ Loaded rigorous scoring framework ({len(extraction_prompt)} chars)")

    # Get all files
    print("✓ Finding markdown files...")
    md_files = get_all_markdown_files(CONFIG["sources_dir"])
    print(f"✓ Found {len(md_files)} files to process")
    print()

    # Process files
    results = []
    total_input = 0
    total_output = 0
    completed = 0

    print("Processing files:")
    print("-" * 80)

    for i, md_file in enumerate(md_files, 1):
        print(f"\n[{i}/{len(md_files)}] {md_file}")

        try:
            content = md_file.read_text(encoding="utf-8")
            print(f"  Size: {len(content):,} chars, {len(content.splitlines())} lines")
        except Exception as e:
            print(f"  ✗ Error reading file: {e}")
            result = {
                "source_file": str(md_file),
                "status": "error",
                "error": f"Failed to read: {str(e)}",
                "extraction": None,
            }
            results.append(result)
            save_results_incrementally(result)
            continue

        # Extract
        result = extract_hyperentities(client, content, md_file, extraction_prompt)
        results.append(result)

        if result["status"] == "success":
            total_input += result["tokens_used"]["input"]
            total_output += result["tokens_used"]["output"]
            completed += 1
            print(f"  ✓ Complete! Total: {result['tokens_used']['input']:,} in / {result['tokens_used']['output']:,} out")
        else:
            print(f"  ✗ Failed: {result.get('error', 'Unknown')}")

        # Save incrementally
        save_results_incrementally(result)
        save_progress(results, completed)

        # Show running totals
        cost = (total_input / 1_000_000) * 3 + (total_output / 1_000_000) * 15
        print(f"  Running total: {completed}/{len(md_files)} files | {total_input:,} in / {total_output:,} out | ${cost:.2f}")

    print("-" * 80)
    print()
    print("=" * 80)
    print("EXTRACTION COMPLETE!")
    print("=" * 80)
    print(f"Files processed: {len(md_files)}")
    print(f"Successful: {completed}")
    print(f"Failed: {len(md_files) - completed}")
    print(f"Total tokens: {total_input:,} in / {total_output:,} out")

    cost = (total_input / 1_000_000) * 3 + (total_output / 1_000_000) * 15
    print(f"Final cost: ${cost:.2f}")
    print()
    print(f"Results saved to: {CONFIG['output_file']}")
    print(f"Progress saved to: {CONFIG['progress_file']}")
    print()
    print("Next steps:")
    print("  1. Review extraction results")
    print("  2. Run synthesis: python3 synthesize_smart.py")
    print("  3. Create visualization: python3 create_visualization_v2.py")
    print()


if __name__ == "__main__":
    main()
