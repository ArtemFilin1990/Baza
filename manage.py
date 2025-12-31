#!/usr/bin/env python3
"""
Unified CLI interface for Baza repository management tasks.

This script provides a convenient command-line interface for common tasks:
- Data validation
- Data extraction
- Data normalization
- Running tests
- Generating reports

Usage:
    python manage.py <command> [options]

Commands:
    validate    - Run CSV data validation
    extract     - Extract data from sources
    normalize   - Normalize and sort CSV data
    test        - Run test suite
    report      - Generate data update reports
    sources     - List all sources and their status
    help        - Show this help message

Examples:
    python manage.py validate
    python manage.py normalize
    python manage.py test
    python manage.py sources
"""

import sys
import os
import subprocess
from pathlib import Path

# Add repository root to path
REPO_ROOT = Path(__file__).parent
sys.path.insert(0, str(REPO_ROOT))


def run_command(cmd, description):
    """Run a shell command and handle errors."""
    print(f"\n{'=' * 60}")
    print(f"Running: {description}")
    print(f"{'=' * 60}\n")
    
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            cwd=REPO_ROOT,
            text=True
        )
        print(f"\n✅ {description} completed successfully")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"\n❌ {description} failed with exit code {e.returncode}")
        return e.returncode


def cmd_validate():
    """Run CSV data validation."""
    return run_command(
        "python scripts/validate/run_validations.py",
        "CSV Data Validation"
    )


def cmd_extract():
    """Extract data from sources."""
    return run_command(
        "python scripts/extract/raw_datasets.py",
        "Data Extraction from Sources"
    )


def cmd_normalize():
    """Normalize and sort CSV data."""
    return run_command(
        "python scripts/update_repo.py",
        "Data Normalization and Sorting"
    )


def cmd_test():
    """Run test suite."""
    # Try pytest first, fall back to unittest
    pytest_installed = subprocess.run(
        "python -m pytest --version",
        shell=True,
        capture_output=True
    ).returncode == 0
    
    if pytest_installed:
        return run_command(
            "python -m pytest tests/ -v",
            "Test Suite (pytest)"
        )
    else:
        return run_command(
            "python -m unittest discover tests/",
            "Test Suite (unittest)"
        )


def cmd_report():
    """Generate data update reports."""
    print("\n" + "=" * 60)
    print("Generating Data Update Report")
    print("=" * 60 + "\n")
    
    # This would generate a JSON report in data/reports/
    import json
    from datetime import datetime
    
    report_dir = REPO_ROOT / "data" / "reports"
    report_dir.mkdir(exist_ok=True)
    
    report_file = report_dir / f"{datetime.now().strftime('%Y-%m-%d')}_update.json"
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "type": "manual_update",
        "files_checked": [],
        "status": "generated"
    }
    
    # List all CSV files
    for csv_file in (REPO_ROOT / "data").rglob("*.csv"):
        report["files_checked"].append(str(csv_file.relative_to(REPO_ROOT)))
    
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Report generated: {report_file.relative_to(REPO_ROOT)}")
    return 0


def cmd_sources():
    """List all sources and their status."""
    print("\n" + "=" * 60)
    print("Sources Status")
    print("=" * 60 + "\n")
    
    import yaml
    
    sources_dir = REPO_ROOT / "sources"
    categories = ["gost", "iso", "analogs", "brands", "skf"]
    
    for category in categories:
        meta_file = sources_dir / category / "meta.yaml"
        if meta_file.exists():
            print(f"\n📁 {category.upper()}")
            print("-" * 60)
            
            try:
                with open(meta_file, 'r', encoding='utf-8') as f:
                    meta = yaml.safe_load(f)
                    
                if meta and 'sources' in meta:
                    for source in meta['sources']:
                        status = source.get('status', 'unknown')
                        file = source.get('file', 'unknown')
                        purpose = source.get('purpose', 'N/A')
                        
                        status_icon = "✅" if status == "verified" else "⏳"
                        print(f"{status_icon} {file}")
                        print(f"   Status: {status}")
                        print(f"   Purpose: {purpose}")
                        print()
            except Exception as e:
                print(f"   ⚠️  Error reading meta.yaml: {e}")
        else:
            print(f"\n📁 {category.upper()}")
            print("-" * 60)
            print(f"   ⚠️  No meta.yaml file found")
    
    return 0


def cmd_help():
    """Show help message."""
    print(__doc__)
    return 0


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        cmd_help()
        return 1
    
    command = sys.argv[1].lower()
    
    commands = {
        'validate': cmd_validate,
        'extract': cmd_extract,
        'normalize': cmd_normalize,
        'test': cmd_test,
        'report': cmd_report,
        'sources': cmd_sources,
        'help': cmd_help,
        '--help': cmd_help,
        '-h': cmd_help,
    }
    
    if command not in commands:
        print(f"❌ Unknown command: {command}")
        print("\nAvailable commands:")
        for cmd in sorted(set(commands.keys())):
            if not cmd.startswith('-'):
                print(f"  - {cmd}")
        return 1
    
    return commands[command]()


if __name__ == '__main__':
    sys.exit(main())
