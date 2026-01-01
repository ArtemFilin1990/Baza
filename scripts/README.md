# Scripts Directory

This directory contains utility scripts for data processing, validation, and repository maintenance.

## Directory Structure

```
scripts/
├── extract/              # Data extraction scripts
├── normalize/            # Data normalization scripts
├── parse/                # Data parsing scripts
├── validate/             # Data validation scripts
├── update_repo.py        # Main normalization script
├── update_changelog.py   # Automated CHANGELOG.md updater
└── validate_articles_structure.py  # Article structure validator
```

## Main Scripts

### Data Processing

#### `update_repo.py`
Main script for normalizing and sorting CSV data.

**Usage:**
```bash
python scripts/update_repo.py
```

**What it does:**
- Normalizes CSV file formatting (UTF-8, consistent delimiters)
- Sorts data according to schemas
- Validates data integrity
- Removes duplicates

#### `extract/raw_datasets.py`
Extract raw data from various sources and convert to CSV.

**Usage:**
```bash
python scripts/extract/raw_datasets.py
```

### Validation

#### `validate/run_validations.py`
Run all validation checks on CSV data.

**Usage:**
```bash
python scripts/validate/run_validations.py
```

**Checks:**
- CSV format validation
- Schema compliance
- Required fields presence
- Data type validation
- Uniqueness constraints
- Sorting order

#### `validate/csv_validator.py`
Core CSV validation logic.

**Usage:**
```bash
python scripts/validate/csv_validator.py <csv_file> <schema_file>
```

**Example:**
```bash
python scripts/validate/csv_validator.py data/gost/bearings.csv schemas/gost.yaml
```

#### `validate_articles_structure.py`
Validate article directory structure and file naming.

**Usage:**
```bash
python scripts/validate_articles_structure.py
```

### Repository Maintenance

#### `update_changelog.py`
Automatically update CHANGELOG.md from git commits.

**Usage:**
```bash
# Update with all commits since last tag
python scripts/update_changelog.py --version 1.0.2

# Update with commits since specific date
python scripts/update_changelog.py --version 1.0.2 --since 2025-12-01

# Dry run (preview without modifying file)
python scripts/update_changelog.py --version 1.0.2 --since 2025-12-01 --dry-run
```

**Parameters:**
- `--version`: Version number for the release (required)
- `--since`: Start date for commits (YYYY-MM-DD)
- `--since-tag`: Start from a specific git tag
- `--date`: Release date (defaults to today)
- `--dry-run`: Preview without modifying CHANGELOG.md

## Unified CLI Interface

For convenience, use the unified CLI interface in the repository root:

```bash
# Run validation
python manage.py validate

# Normalize data
python manage.py normalize

# Run tests
python manage.py test

# Generate report
python manage.py report

# List sources
python manage.py sources

# Show help
python manage.py help
```

See [`manage.py`](../manage.py) documentation for more details.

## Adding New Scripts

When adding new scripts:

1. **Choose the right directory:**
   - `extract/` - for data extraction from sources
   - `normalize/` - for data formatting and normalization
   - `parse/` - for parsing specific file formats
   - `validate/` - for validation and checking

2. **Follow naming conventions:**
   - Use descriptive names: `extract_pdf_tables.py`, not `script1.py`
   - Use snake_case for filenames

3. **Add documentation:**
   - Include docstring at the top of the file
   - Add usage examples in comments
   - Update this README

4. **Make executable (optional):**
   ```bash
   chmod +x scripts/your_script.py
   ```

5. **Add shebang for direct execution:**
   ```python
   #!/usr/bin/env python3
   ```

## Script Development Guidelines

### Error Handling
Always handle errors gracefully:

```python
try:
    # Your code
    pass
except FileNotFoundError as e:
    print(f"Error: File not found - {e}")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
```

### Logging
Use descriptive output:

```python
print(f"✅ Success: Processed {count} records")
print(f"⚠️  Warning: Skipped {skip_count} invalid entries")
print(f"❌ Error: Failed to read file")
```

### Return Codes
Use standard exit codes:
- `0` - Success
- `1` - General error
- `2` - Invalid arguments

### Dependencies
- Prefer standard library when possible
- Document external dependencies in `requirements.txt`
- Keep scripts simple and focused

## Common Tasks

### Add New Data Source
```bash
# 1. Add PDF to sources/
cp new_catalog.pdf sources/brands/

# 2. Update meta.yaml
# Edit sources/brands/meta.yaml

# 3. Extract data (if needed)
python scripts/extract/raw_datasets.py

# 4. Normalize
python manage.py normalize

# 5. Validate
python manage.py validate
```

### Fix CSV Formatting Issues
```bash
# Run normalization
python manage.py normalize

# Check for errors
python manage.py validate
```

### Update After Data Changes
```bash
# Complete update workflow
python manage.py normalize
python manage.py validate
python manage.py test

# Generate report
python manage.py report
```

## Testing Scripts

All scripts should be tested before committing:

```bash
# Run script tests
python -m pytest tests/test_*.py -v

# Or with unittest
python -m unittest discover tests/
```

## Continuous Integration

Scripts are automatically run by GitHub Actions on:
- Every push to main branch
- Every pull request
- Scheduled daily runs

See [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) for CI configuration.

## Troubleshooting

### "Module not found" errors
Install dependencies:
```bash
pip install -r requirements.txt
```

### "Permission denied" errors
Make script executable:
```bash
chmod +x scripts/your_script.py
```

### CSV validation failures
Check:
1. UTF-8 encoding
2. Consistent delimiters (commas)
3. No missing required fields
4. Proper sorting order

## Questions and Support

For help with scripts:
- Check script docstrings and comments
- Review examples in this README
- Open an issue with tag `scripts`
- See [CONTRIBUTING.md](../CONTRIBUTING.md)
