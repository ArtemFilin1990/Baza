"""Data parsing module for different file formats."""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd


class DataParser:
    """Parse data from various file formats."""
    
    def __init__(self, parsing_rules: Dict[str, Any], normalization_config: Dict[str, Any]):
        """Initialize parser.
        
        Args:
            parsing_rules: Parsing rules configuration
            normalization_config: Normalization configuration
        """
        self.parsing_rules = parsing_rules
        self.normalization_config = normalization_config
        self.column_mappings = parsing_rules.get('column_mappings', {})
    
    def parse_file(self, file_path: Path, file_type: str) -> pd.DataFrame:
        """Parse file based on type.
        
        Args:
            file_path: Path to file
            file_type: File type (csv, xlsx, json, txt)
            
        Returns:
            Parsed DataFrame
        """
        if file_type == 'csv':
            return self._parse_csv(file_path)
        elif file_type == 'xlsx':
            return self._parse_xlsx(file_path)
        elif file_type == 'json':
            return self._parse_json(file_path)
        elif file_type == 'txt':
            return self._parse_txt(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
    
    def _parse_csv(self, file_path: Path) -> pd.DataFrame:
        """Parse CSV file.
        
        Args:
            file_path: Path to CSV file
            
        Returns:
            DataFrame
        """
        # Try different encodings
        encodings = ['utf-8', 'cp1251', 'latin1']
        
        for encoding in encodings:
            try:
                df = pd.read_csv(file_path, encoding=encoding)
                return df
            except (UnicodeDecodeError, pd.errors.ParserError):
                continue
        
        raise ValueError(f"Could not parse CSV file with supported encodings: {file_path}")
    
    def _parse_xlsx(self, file_path: Path) -> pd.DataFrame:
        """Parse XLSX file.
        
        Args:
            file_path: Path to XLSX file
            
        Returns:
            DataFrame
        """
        df = pd.read_excel(file_path, engine='openpyxl')
        return df
    
    def _parse_json(self, file_path: Path) -> pd.DataFrame:
        """Parse JSON file.
        
        Args:
            file_path: Path to JSON file
            
        Returns:
            DataFrame
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Handle different JSON structures
        if isinstance(data, list):
            df = pd.DataFrame(data)
        elif isinstance(data, dict):
            # Try to find array in dict
            for key, value in data.items():
                if isinstance(value, list):
                    df = pd.DataFrame(value)
                    break
            else:
                # Single object, wrap in list
                df = pd.DataFrame([data])
        else:
            raise ValueError(f"Unsupported JSON structure: {type(data)}")
        
        return df
    
    def _parse_txt(self, file_path: Path) -> pd.DataFrame:
        """Parse TXT/MD file.
        
        Try to extract tabular data or structured text.
        
        Args:
            file_path: Path to TXT file
            
        Returns:
            DataFrame
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to parse as CSV (tab or comma separated)
        lines = content.strip().split('\n')
        
        # Try tab-separated
        if '\t' in lines[0]:
            try:
                df = pd.read_csv(file_path, sep='\t', encoding='utf-8')
                return df
            except Exception:
                pass
        
        # Try to extract dimension patterns
        rows = []
        for line in lines:
            row = self._extract_dimensions_from_text(line)
            if row:
                rows.append(row)
        
        if rows:
            return pd.DataFrame(rows)
        
        raise ValueError(f"Could not extract tabular data from TXT file: {file_path}")
    
    def _extract_dimensions_from_text(self, text: str) -> Optional[Dict[str, Any]]:
        """Extract dimensions from text line using regex patterns.
        
        Args:
            text: Text line
            
        Returns:
            Extracted data dictionary or None
        """
        patterns = self.parsing_rules.get('dimension_patterns', [])
        
        for pattern_config in patterns:
            regex = pattern_config.get('regex')
            groups = pattern_config.get('groups', [])
            
            match = re.search(regex, text)
            if match:
                result = {}
                for group in groups:
                    value = match.group(group)
                    if value:
                        result[group] = value
                
                # Try to extract артикул (first word/token before dimensions)
                before_match = text[:match.start()].strip()
                tokens = before_match.split()
                if tokens:
                    result['артикул'] = tokens[-1]
                
                return result
        
        return None
    
    def normalize_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Normalize column names to standard schema.
        
        Args:
            df: Input DataFrame
            
        Returns:
            DataFrame with normalized columns
        """
        # Create mapping from actual columns to target columns
        column_map = {}
        used_columns = set()
        
        # First pass: exact matches (case-sensitive)
        for target_col, variations in self.column_mappings.items():
            for actual_col in df.columns:
                if actual_col in used_columns:
                    continue
                # Exact match (case-sensitive)
                if actual_col in variations:
                    column_map[actual_col] = target_col
                    used_columns.add(actual_col)
                    break
        
        # Second pass: case-insensitive matches for remaining columns
        for target_col, variations in self.column_mappings.items():
            for actual_col in df.columns:
                if actual_col in used_columns:
                    continue
                # Case-insensitive match
                if actual_col.lower().strip() in [v.lower() for v in variations]:
                    column_map[actual_col] = target_col
                    used_columns.add(actual_col)
                    break
        
        # Rename columns
        df = df.rename(columns=column_map)
        
        return df
    
    def validate_required_fields(self, df: pd.DataFrame) -> pd.DataFrame:
        """Filter rows that have required fields.
        
        Args:
            df: Input DataFrame
            
        Returns:
            Filtered DataFrame
        """
        required = self.parsing_rules.get('required_fields', {})
        any_of = required.get('any_of', [])
        
        if not any_of:
            return df
        
        # Keep rows that have at least one of the required fields
        mask = pd.Series([False] * len(df))
        for field in any_of:
            if field in df.columns:
                mask |= df[field].notna() & (df[field] != '')
        
        return df[mask].copy()
