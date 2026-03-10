# De-AI Find/Replace List for Google Docs

Use Ctrl+H (Cmd+H on Mac) in Google Docs. Work through Category 1 first (global replace all), then Category 2 (replace one-by-one with review).

---

## Category 1: Safe Global Replacements

Replace all instances without checking context. Order matters for some -- do multi-word phrases before single words.

| # | Find | Replace | Notes |
|---|------|---------|-------|
| 1 | `fundamentally reshape` | `reshape` | Delete intensifier |
| 2 | `fundamentally transform` | `transform` | Delete intensifier |
| 3 | `fundamentally different` | `very different` | Or just "different" |
| 4 | `fundamentally resist` | `actively resist` | |
| 5 | `fundamental challenge` | `core challenge` | |
| 6 | `fundamental barrier` | `core barrier` | |
| 7 | `fundamental barriers` | `core barriers` | |
| 8 | `fundamental mismatch` | `mismatch` | |
| 9 | `The fundamental challenge` | `The core challenge` | |
| 10 | `fundamentally` | *(delete)* | Catch remaining instances |
| 11 | `fundamental ` | `core ` | Catch remaining instances (note trailing space) |
| 12 | `genuinely transformative` | `transformative` | |
| 13 | `genuinely ` | *(delete)* | Catch remaining instances (note trailing space) |
| 14 | `truly understand` | `understand` | |
| 15 | `truly distributed` | `distributed` | |
| 16 | `truly decentralized` | `decentralized` | |
| 17 | `truly aligned` | `aligned` | |
| 18 | `truly ` | *(delete)* | Catch remaining instances (note trailing space) |
| 19 | `radically different` | `very different` | |
| 20 | `radically ` | *(delete)* | Catch remaining (note trailing space) |
| 21 | `dramatically ` | *(delete)* | Note trailing space |
| 22 | `unprecedented ` | *(delete)* | Note trailing space |
| 23 | `staggering amounts` | `enormous amounts` | |
| 24 | `staggering` | `enormous` | Catch remaining |
| 25 | `genuine ` | `real ` | "genuine energy independence" -> "real energy independence" |
| 26 | `specifically designed` | `designed` | |
| 27 | `it's worth noting` | *(delete)* | Filler phrase |
| 28 | `It's worth noting that ` | *(delete)* | Filler with "that" |
| 29 | `the reality is` | *(delete)* | Filler phrase |
| 30 | `The reality is that ` | *(delete)* | Filler with "that" (capitalize next word manually) |
| 31 | `And crucially, ` | *(delete)* | Filler opener |
| 32 | `Crucially, ` | *(delete)* | Filler opener |
| 33 | `crucially` | *(delete)* | Inline filler |
| 34 | `simply doesn't` | `doesn't` | |
| 35 | `simply don't` | `don't` | |
| 36 | `simply ` | *(delete)* | Catch remaining (note trailing space) |
| 37 | `profound ` | *(delete)* | Note trailing space |
| 38 | `profoundly ` | *(delete)* | Note trailing space |
| 39 | `leading the charge` | *(delete or rephrase)* | Cliche |
| 40 | `set out to` | *(use active present tense)* | "set out to identify" -> "identifies" |
| 41 | `represent critical infrastructure` | `are critical infrastructure` | |
| 42 | `measure fundamentally different things` | `measure different things` | |
| 43 | ` — ` (space-em-dash-space before list item like "**X**") | `, ` | In bullet lists: "**Entity** -- d/acc: 65%" -> "**Entity**, d/acc: 65%" |

---

## Category 2: Replace with Review

Check each instance individually. The replacement depends on what's around it.

### Em Dashes (the big one: ~195 instances)

Find: `—` (em dash, U+2014)

Most common replacements (check each one):

| Context pattern | Replace with | Example |
|----------------|--------------|---------|
| Parenthetical aside: `X — Y — Z` | Commas: `X, Y, Z` | "drawn from ExHope — Foresight's initiative — that" -> "drawn from ExHope, Foresight's initiative, that" |
| Introducing explanation: `X — Y` | Colon: `X: Y` | "flips this model — AI coordinates" -> "inverts this model. AI coordinates" |
| Contrast or elaboration: `X — Y` | Period + new sentence | "brittle by design — a single storm" -> "brittle by design. A single storm" |
| Short parenthetical: `X—Y` | Comma: `X, Y` | "legal infrastructure — a vision" -> "legal infrastructure, a vision" |
| Before a list: `including — X, Y, Z` | Colon | |
| Separating clauses of equal weight | Semicolon | "they personalize outputs — not frameworks" -> "they personalize outputs; not frameworks" |
| **Keep** ~10 em dashes | No change | Mid-sentence parenthetical asides where commas would be confusing |

### "not just X, but Y" construction (~15 instances)

Find: `not just`

| Context | Replace with | Example |
|---------|--------------|---------|
| "not just X, but Y" (formulaic contrast) | Direct statement of Y | "not just happen through evolution, but could be designed" -> "could be deliberately designed" |
| "not just X but Y" in genuine contrast | Keep (1 instance kept in Key Findings) | "chosen not just because they scored highly, but because..." |

### "Perhaps most importantly" and similar openers

| Find | Replace | Notes |
|------|---------|-------|
| `Perhaps most importantly, ` | `They also ` or *(delete)* | Check if "They also" fits; otherwise just delete and start with the substance |
| `the deeper question` | *(delete or rephrase)* | Usually can just state the question directly |
| `the question of` | *(rephrase)* | Often removable; "the question of whether" -> "whether" |

### "from X to Y" rhetorical ranges

Find: `from` (then check if it's a false range)

| Context | Replace with | Notes |
|---------|--------------|-------|
| Rhetorical: "from climate change to pandemic prep" | Parenthetical list: "(climate change, pandemic prep)" | Only replace when the range is rhetorical, not literal |
| Literal: "from 90% to near-zero" | Keep | Actual numeric ranges stay |
| "from waiting for X to creating Y" | Direct statement | "Rather than waiting for X, they create Y" |

### Trailing -ing clauses

Find: `, ensuring` / `, highlighting` / `, creating` / `, enabling`

| Find | Replace | Notes |
|------|---------|-------|
| `, ensuring...` | `. This ensures...` or rephrase as direct statement | Give the clause its own sentence with a subject |
| `, highlighting...` | `. This highlights...` or "a reminder of..." | |
| `, creating...` | `. This creates...` | |

### "This isn't X; it's Y" / "This isn't about X"

Find: `This isn't`

| Context | Replace | Notes |
|---------|---------|-------|
| "This isn't about X; it's about Y" | Direct statement of Y | "The goal is Y" |
| "This isn't inherently wrong" | Just cut the hedge and state the point | |

### Contractions to formal English (optional, ~5 instances)

| Find | Replace | Notes |
|------|---------|-------|
| `we'll` | `we will` | Only in formal/concluding passages |
| `we're` | `we are` | Selective; keep in conversational sections |
| `don't` | `do not` | Only where formality matters |

---

## Cleanup Pass (do last)

After all replacements:

1. **Double spaces**: Find two spaces, replace with one space. Repeat until none found.
2. **Orphaned commas**: Search `, ,` and fix.
3. **Capitalization**: After deleting sentence-opening fillers ("The reality is that X"), make sure the next word is capitalized.
4. **Empty lines**: Search for double blank lines and reduce to single.
5. **Trailing whitespace before punctuation**: Search for ` ,` and ` .` patterns.
