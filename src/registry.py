"""Registry management for tracking processed files."""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional


class Registry:
    """Manage registry of processed files."""
    
    def __init__(self, registry_file: Path):
        """Initialize registry.
        
        Args:
            registry_file: Path to registry JSON file
        """
        self.registry_file = registry_file
        self.registry_file.parent.mkdir(parents=True, exist_ok=True)
        self._data: Dict[str, Dict] = {}
        self._load()
    
    def _load(self) -> None:
        """Load registry from file."""
        if self.registry_file.exists():
            try:
                with open(self.registry_file, 'r', encoding='utf-8') as f:
                    self._data = json.load(f)
            except (json.JSONDecodeError, IOError):
                self._data = {}
        else:
            self._data = {}
    
    def _save(self) -> None:
        """Save registry to file atomically."""
        temp_file = self.registry_file.with_suffix('.tmp')
        
        try:
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(self._data, f, indent=2, ensure_ascii=False)
            temp_file.replace(self.registry_file)
        except Exception:
            if temp_file.exists():
                temp_file.unlink()
            raise
    
    def is_processed(self, file_hash: str) -> bool:
        """Check if file has been processed.
        
        Args:
            file_hash: SHA256 hash of file
            
        Returns:
            True if file has been processed
        """
        return file_hash in self._data
    
    def add_entry(
        self,
        file_hash: str,
        original_name: str,
        processed_name: str,
        n_records: int,
        status: str = 'success'
    ) -> None:
        """Add entry to registry.
        
        Args:
            file_hash: SHA256 hash of file
            original_name: Original filename
            processed_name: Processed filename
            n_records: Number of records processed
            status: Processing status
        """
        self._data[file_hash] = {
            'original_name': original_name,
            'processed_name': processed_name,
            'n_records': n_records,
            'status': status,
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        }
        self._save()
    
    def get_entry(self, file_hash: str) -> Optional[Dict]:
        """Get registry entry for a file.
        
        Args:
            file_hash: SHA256 hash of file
            
        Returns:
            Registry entry or None
        """
        return self._data.get(file_hash)
    
    def get_all_entries(self) -> Dict[str, Dict]:
        """Get all registry entries.
        
        Returns:
            All registry entries
        """
        return self._data.copy()
