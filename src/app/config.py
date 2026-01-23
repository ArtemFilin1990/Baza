"""Configuration loader for the automation pipeline."""

import json
from pathlib import Path
from typing import Any

import yaml


class Config:
    """Configuration manager for the pipeline."""

    def __init__(self, config_path: str = "config/app.yaml"):
        """Load configuration from YAML file.

        Args:
            config_path: Path to the YAML configuration file
        """
        self.config_path = Path(config_path)
        with open(self.config_path, encoding="utf-8") as f:
            self._data = yaml.safe_load(f)

        # Load brand aliases
        brand_aliases_path = Path("config/brand_aliases.json")
        with open(brand_aliases_path, encoding="utf-8") as f:
            self.brand_aliases = json.load(f)

        # Load parsing rules
        parsing_rules_path = Path("config/parsing_rules.json")
        with open(parsing_rules_path, encoding="utf-8") as f:
            self.parsing_rules = json.load(f)

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key.

        Args:
            key: Configuration key (can be dot-separated for nested values)
            default: Default value if key not found

        Returns:
            Configuration value
        """
        keys = key.split(".")
        value = self._data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default
        return value

    @property
    def paths(self) -> dict:
        """Get paths configuration."""
        return self._data.get("paths", {})

    @property
    def watcher(self) -> dict:
        """Get watcher configuration."""
        return self._data.get("watcher", {})

    @property
    def limits(self) -> dict:
        """Get limits configuration."""
        return self._data.get("limits", {})

    @property
    def normalization(self) -> dict:
        """Get normalization configuration."""
        return self._data.get("normalization", {})

    @property
    def parsing(self) -> dict:
        """Get parsing configuration."""
        return self._data.get("parsing", {})
