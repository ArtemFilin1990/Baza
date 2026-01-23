#!/usr/bin/env python3
"""
Example: Using the Knowledge Base Builder

This example demonstrates how to use the Knowledge Base Builder
to create a comprehensive knowledge base from your repository.
"""

from pathlib import Path
import sys

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from build_knowledge_base import KnowledgeBaseBuilder


def example_programmatic_access():
    """
    Example: Programmatic access to extracted data.
    """
    print("\n")
    print("=" * 70)
    print("Example: Programmatic Access to Extracted Data")
    print("=" * 70)
    
    # Create builder
    builder = KnowledgeBaseBuilder(repo_path='.')
    
    # Scan repository
    builder.scan_repository()
    
    # Access extracted data
    print(f"\n📊 Statistics:")
    print(f"   - Total files: {len(builder.file_inventory)}")
    print(f"   - Terms in glossary: {len(builder.terms_glossary)}")
    print(f"   - Data structures: {sum(len(v) for v in builder.data_structures.values())}")
    
    # Access specific file types
    markdown_files = [f for f in builder.file_inventory if f['type'] == 'Markdown']
    python_files = [f for f in builder.file_inventory if f['type'] == 'Python']
    
    print(f"\n📁 File Types:")
    print(f"   - Markdown files: {len(markdown_files)}")
    print(f"   - Python files: {len(python_files)}")
    
    # Show some sample terms
    print(f"\n📖 Sample Terms (first 5):")
    for idx, (term, definitions) in enumerate(list(builder.terms_glossary.items())[:5], 1):
        print(f"   {idx}. {term}: {len(definitions)} definition(s)")
    
    print("\n✅ Data extracted successfully")


if __name__ == '__main__':
    print("\nKnowledge Base Builder - Example Usage\n")
    example_programmatic_access()
