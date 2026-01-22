# Migration Plan (Batch-Based)

## Objectives
- Incrementally reorganize the repository into the target structure.
- Keep each batch small and reviewable.
- Avoid broken links and preserve readability at all times.

## Batch Sequence

### Batch 1 — Inventory + Reports (No Moves)
- Add: `CLEANUP_REPORT.md`, `NEW_STRUCTURE.md`, `MIGRATION_PLAN.md`, `ASSUMPTIONS.md`.
- Update: root `README.md` with Structure (WIP) section linking to `NEW_STRUCTURE.md`.
- No file moves/renames/deletes.

### Batch 2 — Create Folders + Section Entry Points (No Moves) ✅ Completed
- [x] Create target directories.
- [x] Add placeholder `README.md` in each section.
- [x] No content migration yet.

### Batch 3 — Content Migration by Topic (Standards & Marking) ✅ Completed
- Section: `/02_standards_marking/`
- Files moved: 12
- Notes: Limited to standards/marking scope; no deep rewrites.

### Batch 4+ — Content Migration by Topic (Small Batches)
- Move 10–15 markdown/text files into **one** target section per batch.
- Minimal renames (only for clarity or collisions).
- Update links only inside touched files.
- Record every change in `CLEANUP_REPORT.md`.
- Duplicates: place into `/_trash_review/` with a note (no merging yet).

### Dedicated Micro-Batches
- Binary relocation: max 5 files per batch.
- Duplicate merge: max 3 files per batch with manual review.

## Validation Checklist (Each Batch)
- README navigation still works.
- `CLEANUP_REPORT.md` updated with batch summary.
- No bulk moves or large diffs.
