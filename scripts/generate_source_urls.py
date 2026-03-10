#!/usr/bin/env python3
"""Generate sources/source_urls.json mapping source files to their public URLs."""

import json
import os
import re
from pathlib import Path

BASE = Path("/Users/lindapetrini/Documents/AI/Foresight/hyper-entities/sources")

def slugify(name: str) -> str:
    """Convert a filename (without .md) to a URL slug."""
    slug = name.lower()
    # Remove special characters except alphanumeric, spaces, and hyphens
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    # Replace spaces with hyphens
    slug = slug.replace(" ", "-")
    # Collapse multiple hyphens
    slug = re.sub(r"-{2,}", "-", slug)
    # Remove leading/trailing hyphens
    slug = slug.strip("-")
    return slug

result = {}

# Podcasts
podcast_dir = BASE / "podcast"
for f in sorted(podcast_dir.glob("*.md")):
    key = f"podcast/{f.name}"
    slug = slugify(f.stem)
    url = f"https://www.existentialhope.com/podcasts/{slug}"
    result[key] = {"url": url, "type": "podcast"}

# World gallery
wg_dir = BASE / "world-gallery"
for f in sorted(wg_dir.glob("*.md")):
    key = f"world-gallery/{f.name}"
    slug = slugify(f.stem.strip())  # strip leading/trailing whitespace in filename
    url = f"https://worlds.existentialhope.com/world/{slug}/"
    result[key] = {"url": url, "type": "world-gallery"}

# Reports
for subdir in ["ai-pathways", "x-hope"]:
    d = BASE / subdir
    if d.exists():
        for f in sorted(d.glob("*.md")):
            key = f"{subdir}/{f.name}"
            result[key] = {"url": None, "type": "report"}

out_path = BASE / "source_urls.json"
with open(out_path, "w") as fp:
    json.dump(result, fp, indent=2, ensure_ascii=False)

print(f"Written {len(result)} entries to {out_path}")
