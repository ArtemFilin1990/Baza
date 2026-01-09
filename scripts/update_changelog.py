#!/usr/bin/env python3
"""
Automated CHANGELOG.md updater.

This script helps maintain CHANGELOG.md by:
1. Reading git commit history
2. Categorizing changes
3. Generating formatted changelog entries
4. Updating CHANGELOG.md

Usage:
    python scripts/update_changelog.py [--since DATE] [--version VERSION]

Examples:
    python scripts/update_changelog.py --since 2025-12-01
    python scripts/update_changelog.py --version 1.0.2
"""

import argparse
import re
import subprocess
from datetime import datetime
from pathlib import Path


def get_commits_since(since_date=None, since_tag=None):
    """Get git commits since a date or tag."""
    cmd = ["git", "log", "--pretty=format:%h|%s|%ad", "--date=short"]

    if since_tag:
        cmd.append(f"{since_tag}..HEAD")
    elif since_date:
        cmd.append(f"--since={since_date}")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        commits = []
        for line in result.stdout.strip().split("\n"):
            if line:
                parts = line.split("|")
                if len(parts) >= 3:
                    commits.append({"hash": parts[0], "message": parts[1], "date": parts[2]})
        return commits
    except subprocess.CalledProcessError:
        return []


def categorize_commit(message):
    """Categorize a commit message."""
    message_lower = message.lower()

    # Category keywords
    categories = {
        "Added": ["add", "create", "new", "implement"],
        "Changed": ["change", "update", "modify", "refactor", "improve", "enhance"],
        "Fixed": ["fix", "correct", "resolve", "patch"],
        "Removed": ["remove", "delete"],
        "Documentation": ["doc", "readme", "comment"],
        "Data": ["data", "csv", "schema"],
        "Tests": ["test", "spec"],
    }

    for category, keywords in categories.items():
        if any(keyword in message_lower for keyword in keywords):
            return category

    return "Changed"  # Default category


def format_changelog_entry(commits, version, date=None):
    """Format commits into a changelog entry."""
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    # Group by category
    categorized = {}
    for commit in commits:
        category = categorize_commit(commit["message"])
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(commit)

    # Build changelog text
    lines = [f"## [{version}] - {date}\n"]

    for category in ["Added", "Changed", "Fixed", "Removed", "Documentation", "Data", "Tests"]:
        if category in categorized:
            lines.append(f"\n### {category}\n")
            for commit in categorized[category]:
                # Clean up commit message
                msg = commit["message"].strip()
                # Remove conventional commit prefixes
                msg = re.sub(r"^(feat|fix|docs|style|refactor|test|chore):\s*", "", msg, flags=re.IGNORECASE)
                lines.append(f"- {msg} ({commit['hash']})\n")

    return "".join(lines)


def update_changelog(new_entry, changelog_path):
    """Update CHANGELOG.md with new entry."""
    if not changelog_path.exists():
        # Create new changelog
        content = f"""# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

{new_entry}
"""
    else:
        # Read existing changelog
        with open(changelog_path, encoding="utf-8") as f:
            content = f.read()

        # Find insertion point (after header, before first version)
        match = re.search(r"(# Changelog.*?\n\n.*?\n\n)", content, re.DOTALL)
        if match:
            header = match.group(1)
            rest = content[len(header) :]
            content = f"{header}{new_entry}\n{rest}"
        else:
            # Just append at the end
            content += f"\n{new_entry}"

    # Write back
    with open(changelog_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Update CHANGELOG.md")
    parser.add_argument("--since", help="Get commits since this date (YYYY-MM-DD)")
    parser.add_argument("--since-tag", help="Get commits since this tag")
    parser.add_argument("--version", required=True, help="Version number for this release")
    parser.add_argument("--date", help="Release date (YYYY-MM-DD), defaults to today")
    parser.add_argument("--dry-run", action="store_true", help="Print changelog without updating file")

    args = parser.parse_args()

    # Get commits
    commits = get_commits_since(since_date=args.since, since_tag=args.since_tag)

    if not commits:
        print("No commits found")
        return 1

    print(f"Found {len(commits)} commits")

    # Format entry
    entry = format_changelog_entry(commits, args.version, args.date)

    if args.dry_run:
        print("\n" + "=" * 60)
        print("CHANGELOG ENTRY (dry run):")
        print("=" * 60)
        print(entry)
        return 0

    # Update changelog
    repo_root = Path(__file__).parent.parent
    changelog_path = repo_root / "CHANGELOG.md"

    update_changelog(entry, changelog_path)
    print(f"\n✅ Updated {changelog_path}")
    print("\nNew entry:")
    print(entry)

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
