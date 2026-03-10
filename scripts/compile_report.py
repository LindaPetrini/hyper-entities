#!/usr/bin/env python3
"""Compile report_v3.md to PDF (via Typst) and DOCX (via Pandoc)."""

import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
MD_PATH = BASE / "results" / "v3" / "report_v3.md"
TYP_PATH = BASE / "results" / "v3" / "report_v3.typ"
PDF_PATH = BASE / "results" / "v3" / "report_v3.pdf"
DOCX_PATH = BASE / "results" / "v3" / "report_v3.docx"


def md_to_typst(md: str) -> str:
    """Convert markdown text to Typst markup."""
    lines = md.split("\n")
    out = []
    in_table = False
    table_rows = []
    in_blockquote = False
    bq_lines = []

    def flush_blockquote():
        nonlocal in_blockquote, bq_lines
        if in_blockquote:
            text = " ".join(bq_lines)
            text = convert_inline(text)
            out.append(f'#block(fill: luma(245), inset: 12pt, radius: 4pt, width: 100%)[{text}]')
            out.append("")
            bq_lines = []
            in_blockquote = False

    def flush_table():
        nonlocal in_table, table_rows
        if not in_table:
            return
        # table_rows is list of lists of cell strings
        if len(table_rows) < 1:
            in_table = False
            table_rows = []
            return
        ncols = len(table_rows[0])
        col_spec = ", ".join(["auto"] * ncols)
        out.append(f"#table(columns: ({col_spec}),")
        out.append("  stroke: 0.5pt + luma(180),")
        out.append("  inset: 6pt,")
        # header row bold
        for i, row in enumerate(table_rows):
            for cell in row:
                cell_text = convert_inline(cell.strip())
                if i == 0:
                    out.append(f"  table.cell[*{cell_text}*],")
                else:
                    out.append(f"  table.cell[{cell_text}],")
        out.append(")")
        out.append("")
        in_table = False
        table_rows = []

    def convert_inline(text: str) -> str:
        """Convert inline markdown to typst."""
        # Links: [text](url) -> #link("url")[text]
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'#link("\2")[\1]', text)
        # Bold+italic ***text*** or ___text___
        text = re.sub(r'\*\*\*(.+?)\*\*\*', r'_*\1*_', text)
        # Bold: **text** -> *text*
        # But be careful not to double-convert
        text = re.sub(r'\*\*(.+?)\*\*', r'*\1*', text)
        # Italic: *text* -> _text_ (single asterisk not preceded/followed by asterisk)
        # Use negative lookbehind/ahead for *
        text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'_\1_', text)
        # Inline code
        text = re.sub(r'`([^`]+)`', r'`\1`', text)
        # Escape dollar signs (typst math mode)
        text = text.replace("$", "\\$")
        return text

    for line in lines:
        stripped = line.strip()

        # Horizontal rule
        if stripped == "---":
            flush_blockquote()
            flush_table()
            out.append("#line(length: 100%, stroke: 0.5pt + luma(180))")
            out.append("")
            continue

        # Table detection
        if "|" in stripped and stripped.startswith("|") and stripped.endswith("|"):
            flush_blockquote()
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            # Skip separator rows
            if all(re.match(r'^[-:]+$', c) for c in cells):
                continue
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(cells)
            continue
        else:
            flush_table()

        # Blockquote
        if stripped.startswith(">"):
            content = stripped.lstrip(">").strip()
            if not in_blockquote:
                in_blockquote = True
                bq_lines = []
            bq_lines.append(content)
            continue
        else:
            flush_blockquote()

        # Headers
        m = re.match(r'^(#{1,6})\s+(.*)', stripped)
        if m:
            level = len(m.group(1))
            title = convert_inline(m.group(2))
            heading = "=" * level
            out.append(f"{heading} {title}")
            out.append("")
            continue

        # Bullet lists
        m = re.match(r'^[-*]\s+(.*)', stripped)
        if m:
            out.append(f"- {convert_inline(m.group(1))}")
            continue

        # Numbered lists
        m = re.match(r'^\d+\.\s+(.*)', stripped)
        if m:
            out.append(f"+ {convert_inline(m.group(1))}")
            continue

        # Empty line
        if stripped == "":
            out.append("")
            continue

        # Regular paragraph
        out.append(convert_inline(stripped))

    flush_blockquote()
    flush_table()
    return "\n".join(out)


def build_typst_document(md: str) -> str:
    """Build complete typst document with preamble."""
    body = md_to_typst(md)

    preamble = r"""#set document(title: "Hyper-Entities V3: Spotlight Report", author: "Linda Petrini")
#set page(margin: 1in, numbering: "1")
#set text(font: "Helvetica", size: 11pt, lang: "en")
#set par(justify: true, leading: 0.65em)
#set heading(numbering: none)
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  text(size: 20pt, weight: "bold", it.body)
  v(0.5em)
}
#show heading.where(level: 2): it => {
  v(1em)
  text(size: 16pt, weight: "bold", it.body)
  v(0.3em)
}
#show heading.where(level: 3): it => {
  v(0.8em)
  text(size: 13pt, weight: "bold", it.body)
  v(0.2em)
}
#show link: it => {
  set text(fill: rgb("#1a5276"))
  underline(it)
}

// Title page
#align(center + horizon)[
  #text(size: 28pt, weight: "bold")[Hyper-Entities V3:\ Spotlight Report]
  #v(1.5em)
  #text(size: 14pt)[Linda Petrini]
  #v(0.5em)
  #text(size: 12pt)[Foresight Institute]
  #v(0.5em)
  #text(size: 12pt)[March 2026]
]
#pagebreak()

// Table of Contents
#outline(title: "Table of Contents", indent: 1.5em, depth: 2)
#pagebreak()

// Body
"""
    return preamble + body


def main():
    md = MD_PATH.read_text(encoding="utf-8")

    # 1. Typst -> PDF
    print("Converting markdown to Typst...")
    typ_content = build_typst_document(md)
    TYP_PATH.write_text(typ_content, encoding="utf-8")
    print(f"  Wrote {TYP_PATH}")

    print("Compiling Typst to PDF...")
    result = subprocess.run(
        ["typst", "compile", str(TYP_PATH), str(PDF_PATH)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  Typst errors:\n{result.stderr}")
        # Try to continue anyway
    if PDF_PATH.exists():
        size_mb = PDF_PATH.stat().st_size / (1024 * 1024)
        print(f"  PDF: {PDF_PATH} ({size_mb:.2f} MB)")
    else:
        print("  PDF compilation failed!")

    # 2. DOCX via Pandoc
    print("Converting markdown to DOCX via Pandoc...")
    result = subprocess.run(
        ["pandoc", str(MD_PATH), "-o", str(DOCX_PATH), "--toc",
         "-f", "markdown", "-t", "docx"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  Pandoc errors:\n{result.stderr}")
    if DOCX_PATH.exists():
        size_mb = DOCX_PATH.stat().st_size / (1024 * 1024)
        print(f"  DOCX: {DOCX_PATH} ({size_mb:.2f} MB)")
    else:
        print("  DOCX creation failed!")

    print("Done.")


if __name__ == "__main__":
    main()
