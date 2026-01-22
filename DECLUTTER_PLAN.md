# Decluttering Plan: Fusing Similar Hyper-Entities

## Goal
Reduce 345 entities → ~100-150 distinct concepts by merging similar/overlapping entities.

## Approach Options

### Option A: Embedding-Based Clustering (Recommended)
1. Generate embeddings for each entity (name + description + core_technologies)
2. Compute pairwise cosine similarity
3. Identify clusters of similar entities (similarity > 0.85)
4. For each cluster, either:
   - Merge into single "canonical" entity (best scores)
   - Create parent concept with variants as children

**Pros:** Catches semantic similarity even with different wording
**Cons:** Needs embedding API calls (~$0.10 for 345 entities)

### Option B: Technology-Based Deduplication
1. Group entities by overlapping `core_technologies`
2. Entities sharing 3+ technologies → candidates for merge
3. Manual review of merge candidates

**Pros:** Simple, no API needed
**Cons:** Misses semantically similar entities with different tech labels

### Option C: Name/Description Fuzzy Matching
1. Fuzzy string matching on names (Levenshtein distance)
2. TF-IDF similarity on descriptions
3. Flag pairs above threshold for merge

**Pros:** Fast, no API
**Cons:** Less accurate than embeddings

## Recommended Pipeline

```
Step 1: Generate embeddings (Claude or OpenAI)
        └── ~345 entities × embedding cost

Step 2: Build similarity matrix
        └── Find all pairs with similarity > 0.80

Step 3: Create merge groups
        └── Connected components of similar entities

Step 4: Auto-merge or review
        └── For each group:
            - If 2-3 entities: auto-merge (keep highest scores)
            - If 4+ entities: flag for manual review

Step 5: Create canonical entities
        └── Merged entity gets:
            - Best name (or synthesized)
            - Combined description
            - Union of core_technologies
            - Max of each score
            - List of "also known as" variants

Step 6: Update dashboard
        └── New version (v3.5) with deduplicated entities
        └── Option to show/hide variants
```

## Expected Outcome
- 345 entities → ~120-180 canonical entities
- Each canonical entity may have 1-5 "variants" or "related concepts"
- Cleaner browsing experience
- Easier to identify truly unique hyper-entities

## Files to Create
- `deduplicate_entities.py` - Main deduplication script
- `results/stage4_deduplicated/entities.json` - Deduplicated data
- `results/stage4_deduplicated/merge_log.json` - Record of what was merged

## Questions to Decide
1. **Merge strategy:** Keep best? Average scores? Union of technologies?
2. **Threshold:** 0.80? 0.85? 0.90 similarity?
3. **Manual review:** All merges? Only large groups? None?
4. **Variants display:** Show in dashboard? Separate tab? Hidden?

## Quick Start Tomorrow
```bash
# Option A (embeddings - recommended)
python deduplicate_entities.py --method embeddings --threshold 0.85

# Option B (tech overlap - simpler)
python deduplicate_entities.py --method technology --min-overlap 3

# Preview only (no changes)
python deduplicate_entities.py --preview
```
