# Cleanup Report

## Overview

This report tracks incremental cleanup batches. Each batch records scope, actions, and affected paths.

| Batch | Date | Scope | Files Added | Files Updated | Files Moved | Files Deleted | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-01-21 | Inventory + reports (no moves) | 4 | 1 | 0 | 0 | Initial documentation and plan |
| 2 | 2026-01-22 | Folders + entrypoints (no moves) | 12 | 3 | 0 | 0 | Added section entrypoints |

## Batch Log

### Batch 1 — Inventory + Reports (No Moves)

**Checklist**
- [x] Created baseline cleanup documentation.
- [x] Added target structure reference.
- [x] Documented migration plan and assumptions.
- [x] Updated root README with Structure (WIP) links.

**Changed paths**
- Added: `CLEANUP_REPORT.md`
- Added: `NEW_STRUCTURE.md`
- Added: `MIGRATION_PLAN.md`
- Added: `ASSUMPTIONS.md`
- Updated: `README.md`

### Batch 2 — Create Folders + Section Entry Points (No Moves)

**Checklist**
- [x] Created target directories.
- [x] Added section entrypoint READMEs.
- [x] Updated migration tracking files.

**Changed paths**
- ADD: `00_meta/README.md`
- ADD: `01_basics/README.md`
- ADD: `02_standards_marking/README.md`
- ADD: `03_types_components/README.md`
- ADD: `04_parameters_calculations/README.md`
- ADD: `05_operation_maintenance/README.md`
- ADD: `06_failures_diagnostics/README.md`
- ADD: `07_brands_manufacturers/README.md`
- ADD: `08_special_reference/README.md`
- ADD: `_tables/README.md`
- ADD: `_assets/README.md`
- ADD: `_trash_review/README.md`
- Updated: `README.md`
- Updated: `MIGRATION_PLAN.md`
- Updated: `CLEANUP_REPORT.md`

### Batch 3 — Standards & Marking Content Population

**Checklist**
- [x] Moved standards/marking content into `/02_standards_marking/`.
- [x] Updated section README index and coverage checklist.
- [x] Logged moves for standards/marking batch.

**Changed paths**
- MOVE: `wiki/2-standarty-i-markirovka/2-1-gost-standarty.md` → `02_standards_marking/02_01_gost_standards.md` (Section 02 — standards & marking)
- MOVE: `wiki/2-standarty-i-markirovka/2-2-iso-standarty.md` → `02_standards_marking/02_02_iso_standards.md` (Section 02 — standards & marking)
- MOVE: `wiki/1-osnovy-terminologiya-vybor/1-1-sistema-uslovnyh-oboznacheniy.md` → `02_standards_marking/02_03_designation_system.md` (Section 02 — standards & marking)
- MOVE: `wiki/1-osnovy-terminologiya-vybor/1-2-klass-tochnosti.md` → `02_standards_marking/02_04_accuracy_classes.md` (Section 02 — standards & marking)
- MOVE: `wiki/1-osnovy-terminologiya-vybor/1-3-zazory.md` → `02_standards_marking/02_05_clearance_groups.md` (Section 02 — standards & marking)
- MOVE: `wiki/1-osnovy-terminologiya-vybor/1-6-vnutrenniy-diametr.md` → `02_standards_marking/02_06_inner_diameter_rules.md` (Section 02 — standards & marking)
- MOVE: `wiki/1-osnovy-terminologiya-vybor/1-7-razmernye-serii.md` → `02_standards_marking/02_07_dimension_series.md` (Section 02 — standards & marking)
- MOVE: `wiki/2-standarty-i-markirovka/2-6-etu-oboznacheniya.md` → `02_standards_marking/02_08_etu_designations.md` (Section 02 — standards & marking)
- MOVE: `wiki/2-standarty-i-markirovka/2-3-analogi-gost-iso.md` → `02_standards_marking/02_09_gost_iso_analogues.md` (Section 02 — standards & marking)
- MOVE: `wiki/2-standarty-i-markirovka/2-4-analogi-iso-gost.md` → `02_standards_marking/02_10_iso_gost_analogues.md` (Section 02 — standards & marking)
- MOVE: `wiki/2-standarty-i-markirovka/2-5-analogi-dop-znakov.md` → `02_standards_marking/02_11_additional_sign_analogues.md` (Section 02 — standards & marking)
- MOVE: `wiki/2-standarty-i-markirovka/2-8-importnye-analogi.md` → `02_standards_marking/02_12_imported_analogues.md` (Section 02 — standards & marking)
