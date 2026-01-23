"""Registry module for tracking processed files."""

import json
from pathlib import Path
from typing import Dict, Set

from app.utils import atomic_write


class Registry:
    """Registry for tracking processed files by SHA256 hash."""

    def __init__(self, registry_path: Path):
        """Initialize registry.

        Args:
            registry_path: Path to registry JSON file
        """
        self.registry_path = registry_path
        self.hashes: Set[str] = set()
        self.load()

    def load(self):
        """Load registry from file."""
        if not self.registry_path.exists():
            self.hashes = set()
            return

        with open(self.registry_path, encoding="utf-8") as f:
            data = json.load(f)
            self.hashes = set(data.get("processed_hashes", []))

    def save(self):
        """Save registry to file."""
        self.registry_path.parent.mkdir(parents=True, exist_ok=True)
        data = {"processed_hashes": sorted(list(self.hashes))}
        content = json.dumps(data, ensure_ascii=False, indent=2)
        atomic_write(self.registry_path, content, mode="w", encoding="utf-8")

    def is_processed(self, sha256: str) -> bool:
        """Check if a file hash is already processed.

        Args:
            sha256: SHA256 hash of the file

        Returns:
            True if already processed
        """
        return sha256 in self.hashes

    def mark_processed(self, sha256: str):
        """Mark a file hash as processed.

        Args:
            sha256: SHA256 hash of the file
        """
        self.hashes.add(sha256)
        self.save()
