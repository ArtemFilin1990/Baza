# Target Structure (WIP)

## Goal
Define a stable, readable structure for the knowledge base. Migration will proceed in batches with minimal changes per PR.

## Target Tree
```
/
├── README.md
├── 00_meta/
├── 01_basics/
├── 02_standards_marking/
├── 03_types_components/
├── 04_parameters_calculations/
├── 05_operation_maintenance/
├── 06_failures_diagnostics/
├── 07_brands_manufacturers/
├── 08_special_reference/
├── _tables/
├── _assets/
└── _trash_review/
```

## Conventions
- **00_meta/**: project-level indexes, reports, migration plans, structure docs.
- **01_basics/**: terms, theory, introductory materials.
- **02_standards_marking/**: GOST/ISO standards, marking, suffixes, designation rules.
- **03_types_components/**: bearing types, assemblies, components.
- **04_parameters_calculations/**: sizes, load ratings, formulas, calculations.
- **05_operation_maintenance/**: lubrication, mounting, handling, maintenance.
- **06_failures_diagnostics/**: failure modes, troubleshooting, diagnostics.
- **07_brands_manufacturers/**: catalogs, brands, manufacturer references.
- **08_special_reference/**: applications (auto, linear systems), special domains.
- **_tables/**: structured tables, datasets, reference sheets (non-binary).
- **_assets/**: images/diagrams (binary moves only in dedicated micro-batches).
- **_trash_review/**: quarantined duplicates or uncertain material.

## Link Policy
- Update links only inside files touched by the current batch.
- Preserve existing navigation while migrating.
- Add redirects or notes when renames are unavoidable.

