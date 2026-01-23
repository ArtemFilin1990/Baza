"""Configuration management module."""

import json
from pathlib import Path
from typing import Any, Dict

import yaml


class Config:
    """Configuration manager."""
    
    def __init__(self, config_dir: Path = None):
        """Initialize configuration.
        
        Args:
            config_dir: Path to configuration directory
        """
        if config_dir is None:
            config_dir = Path(__file__).parent.parent / 'config'
        
        self.config_dir = Path(config_dir)
        self._app_config = None
        self._brand_aliases = None
        self._parsing_rules = None
    
    def load_app_config(self) -> Dict[str, Any]:
        """Load application configuration.
        
        Returns:
            Application configuration dictionary
        """
        if self._app_config is None:
            config_file = self.config_dir / 'app.yaml'
            with open(config_file, 'r', encoding='utf-8') as f:
                self._app_config = yaml.safe_load(f)
        return self._app_config
    
    def load_brand_aliases(self) -> Dict[str, str]:
        """Load brand aliases mapping.
        
        Returns:
            Brand aliases dictionary
        """
        if self._brand_aliases is None:
            aliases_file = self.config_dir / 'brand_aliases.json'
            with open(aliases_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self._brand_aliases = data.get('aliases', {})
        return self._brand_aliases
    
    def load_parsing_rules(self) -> Dict[str, Any]:
        """Load parsing rules configuration.
        
        Returns:
            Parsing rules dictionary
        """
        if self._parsing_rules is None:
            rules_file = self.config_dir / 'parsing_rules.json'
            with open(rules_file, 'r', encoding='utf-8') as f:
                self._parsing_rules = json.load(f)
        return self._parsing_rules
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key path.
        
        Args:
            key: Key path (e.g., 'watcher.mode')
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        config = self.load_app_config()
        keys = key.split('.')
        
        value = config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
