#!/usr/bin/env python3
"""
Tests for Knowledge Base Builder

Tests the functionality of the knowledge base builder script.
"""

import os
import tempfile
import shutil
from pathlib import Path
import sys

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from build_knowledge_base import KnowledgeBaseBuilder


def test_file_type_detection():
    """Test that file type detection works correctly."""
    builder = KnowledgeBaseBuilder(".")

    test_cases = [
        (Path("test.md"), "Markdown"),
        (Path("test.py"), "Python"),
        (Path("test.json"), "JSON"),
        (Path("test.yaml"), "YAML"),
        (Path("test.csv"), "CSV"),
        (Path("test.xlsx"), "Excel"),
        (Path("test.pdf"), "PDF"),
        (Path("test.txt"), "Text"),
        (Path("test.unknown"), "Other (.unknown)"),
    ]

    for file_path, expected_type in test_cases:
        result = builder.get_file_type(file_path)
        assert result == expected_type, f"Expected {expected_type} for {file_path}, got {result}"

    print("✅ File type detection test passed")


def test_should_process_file():
    """Test file exclusion logic."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        builder = KnowledgeBaseBuilder(str(tmpdir))

        # Create test files
        test_md = tmpdir / "test.md"
        test_md.write_text("# Test")

        scripts_dir = tmpdir / "scripts"
        scripts_dir.mkdir()
        test_py = scripts_dir / "test.py"
        test_py.write_text("# Test")

        git_dir = tmpdir / ".git"
        git_dir.mkdir()
        git_config = git_dir / "config"
        git_config.write_text("test")

        pycache_dir = tmpdir / "__pycache__"
        pycache_dir.mkdir()
        test_pyc = pycache_dir / "test.pyc"
        test_pyc.write_text("test")

        # Should process
        assert builder.should_process_file(test_md)
        assert builder.should_process_file(test_py)

        # Should not process (excluded directories)
        assert not builder.should_process_file(git_config)
        assert not builder.should_process_file(test_pyc)

        print("✅ File exclusion test passed")


def test_term_extraction():
    """Test term extraction from Markdown."""
    builder = KnowledgeBaseBuilder(".")

    markdown_content = """
# Основы подшипников

**Подшипник качения** - это опора или направляющая.

## Типы

**Радиальный подшипник** - воспринимает радиальные нагрузки.
**Упорный подшипник** - воспринимает осевые нагрузки.
    """

    terms = builder.extract_terms_from_markdown(markdown_content, Path("test.md"))

    # Should extract at least the main terms
    term_names = [term for term, _ in terms]
    assert "Подшипник качения" in term_names
    assert "Радиальный подшипник" in term_names
    assert "Упорный подшипник" in term_names

    print(f"✅ Term extraction test passed (extracted {len(terms)} terms)")


def test_builder_with_sample_files():
    """Test the builder with a sample directory structure."""
    # Create temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        # Create sample files
        (tmpdir / "README.md").write_text("# Test Project\n\n**Term** - definition", encoding="utf-8")
        (tmpdir / "test.py").write_text(
            "def test_function():\n    pass\n\nclass TestClass:\n    pass", encoding="utf-8"
        )
        (tmpdir / "data.json").write_text('{"key": "value"}', encoding="utf-8")

        # Create subdirectory with file
        (tmpdir / "docs").mkdir()
        (tmpdir / "docs" / "guide.md").write_text("# Guide\n\n**Important** - note", encoding="utf-8")

        # Build knowledge base
        builder = KnowledgeBaseBuilder(str(tmpdir), "TEST_KB.md")
        builder.scan_repository()

        # Verify scan results
        assert len(builder.file_inventory) == 4, f"Expected 4 files, got {len(builder.file_inventory)}"
        assert len(builder.terms_glossary) >= 2, f"Expected at least 2 terms, got {len(builder.terms_glossary)}"

        # Generate knowledge base
        builder.generate_knowledge_base()

        # Verify output file exists
        kb_file = tmpdir / "TEST_KB.md"
        assert kb_file.exists(), "Knowledge base file was not created"

        # Verify content
        content = kb_file.read_text(encoding="utf-8")
        assert "# База знаний" in content
        assert "README.md" in content
        assert "test.py" in content

        print(f"✅ Builder integration test passed")
        print(f"   - Files processed: {len(builder.file_inventory)}")
        print(f"   - Terms extracted: {len(builder.terms_glossary)}")
        print(f"   - KB file size: {kb_file.stat().st_size} bytes")


def test_code_structure_extraction():
    """Test extraction of code structures."""
    builder = KnowledgeBaseBuilder(".")

    python_code = """
class MyClass:
    def __init__(self):
        pass
    
    def method1(self):
        pass

def function1():
    pass

def function2(arg1, arg2):
    return arg1 + arg2
    """

    structures = builder.extract_code_structures(python_code, "Python")

    assert "Class: MyClass" in structures
    assert "Function: method1" in structures or "Function: __init__" in structures
    assert "Function: function1" in structures
    assert "Function: function2" in structures

    print(f"✅ Code structure extraction test passed (found {len(structures)} structures)")


def run_all_tests():
    """Run all tests."""
    print("=" * 70)
    print("  Running Knowledge Base Builder Tests")
    print("=" * 70)
    print()

    tests = [
        test_file_type_detection,
        test_should_process_file,
        test_term_extraction,
        test_code_structure_extraction,
        test_builder_with_sample_files,
    ]

    for test in tests:
        try:
            test()
        except Exception as e:
            print(f"❌ {test.__name__} failed: {e}")
            import traceback

            traceback.print_exc()
            return False

    print()
    print("=" * 70)
    print("  ✅ All tests passed!")
    print("=" * 70)
    return True


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
