# Automated Bearings Catalog Processing System

[Русская версия / Russian version](automation_ru.md)

## Quick Start

### Install
```bash
pip install -r requirements.txt
```

### Run
```bash
# Watch mode (continuous)
python -m src.cli watch

# Process once and exit  
python -m src.cli once

# Rebuild catalog from processed files
python -m src.cli rebuild
```

### Usage
1. Drop files into `inbox/` directory
2. System automatically processes them
3. Results appear in `out/catalog_target.csv`
4. Processed files move to `processed/`

## Supported Formats

- **CSV** - Various encodings, flexible column names
- **XLSX** - Excel files  
- **JSON** - Array of objects
- **TXT/MD** - Tab-separated or dimension patterns

## Features

✅ **Fully Automated** - No manual intervention  
✅ **Idempotent** - Safe to reprocess same files  
✅ **Multi-format** - CSV, XLSX, JSON, TXT  
✅ **Smart Deduplication** - Handles dimension conflicts  
✅ **Atomic Updates** - Never corrupts catalog  
✅ **Full Audit Trail** - Comprehensive logging

## Output Files

- `out/catalog_target.csv` - Unified catalog (CSV)
- `out/catalog_target.json` - Unified catalog (JSON)  
- `out/run_report.ndjson` - Processing reports
- `out/processed_registry.json` - File tracking (SHA256)
- `logs/app.log` - Application logs

## Data Schema

| Column | Description | Required |
|--------|-------------|----------|
| Наименование | Product name | Optional |
| Артикул | Part number | ✓ |
| Аналог | Equivalent | Optional |
| Бренд | Brand | Optional |
| D | Outer diameter (mm) | Optional |
| d | Inner diameter (mm) | Optional |
| H | Width (mm) | Optional |
| m | Mass (kg) | Optional |

## Examples

See `examples/` directory for sample files:
- `sample_data.csv` - CSV example
- `sample_data.json` - JSON example

## Testing

```bash
pytest tests/test_automation_pipeline.py -v
```

## Full Documentation

Complete documentation with all details available in:
- **Russian (detailed):** [automation_ru.md](automation_ru.md)

## Architecture

```
inbox/ → Parser → Normalizer → Catalog → processed/
                                    ↓
                        out/catalog_target.csv
                        out/run_report.ndjson
```

## Configuration

Configure in `config/`:
- `app.yaml` - Main settings
- `brand_aliases.json` - Brand name mapping
- `parsing_rules.json` - Column mappings

---

**Status:** ✅ Production Ready  
**Version:** 1.0
