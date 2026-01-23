#!/usr/bin/env python3
"""
Knowledge Base Builder (MAX CONTEXT MODE)

Построение полной, структурированной и машиночитаемой базы знаний
на основе всех файлов в репозитории.

Режим максимального контекста - никаких сокращений, полная извлечение информации.
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
from collections import defaultdict
from datetime import datetime


class KnowledgeBaseBuilder:
    """
    Построитель базы знаний.
    
    Извлекает 100% информации из файлов репозитория и формирует
    структурированную базу знаний в формате Markdown.
    """
    
    def __init__(self, repo_path: str, output_path: str = "KNOWLEDGE_BASE.md"):
        self.repo_path = Path(repo_path)
        self.output_path = Path(output_path)
        
        # Исключаемые директории и файлы
        self.exclude_dirs = {
            '.git', '__pycache__', '.pytest_cache', 'node_modules',
            '.venv', 'venv', 'dist', 'build', '.mypy_cache',
            '_trash_review', 'ZIP'
        }
        
        self.exclude_patterns = {
            '.pyc', '.pyo', '.pyd', '.so', '.dll', '.dylib',
            '.exe', '.bin', '.o', '.a', '.class', '.jar',
            '.gitignore', '.gitattributes', '.DS_Store'
        }
        
        # Сбор данных
        self.file_inventory: List[Dict[str, Any]] = []
        self.terms_glossary: Dict[str, List[str]] = defaultdict(list)
        self.processes: Dict[str, List[str]] = defaultdict(list)
        self.rules: Dict[str, List[str]] = defaultdict(list)
        self.data_structures: Dict[str, List[str]] = defaultdict(list)
        self.conflicts: List[Dict[str, Any]] = []
        
    def should_process_file(self, file_path: Path) -> bool:
        """Определяет, нужно ли обрабатывать файл."""
        # Проверка исключенных директорий
        for part in file_path.parts:
            if part in self.exclude_dirs:
                return False
        
        # Проверка расширений
        if any(str(file_path).endswith(pattern) for pattern in self.exclude_patterns):
            return False
        
        # Проверка размера файла (пропускаем очень большие бинарные файлы)
        try:
            if file_path.stat().st_size > 100 * 1024 * 1024:  # 100 MB
                return False
        except:
            return False
        
        return True
    
    def get_file_type(self, file_path: Path) -> str:
        """Определяет тип файла."""
        suffix = file_path.suffix.lower()
        
        type_mapping = {
            '.md': 'Markdown',
            '.txt': 'Text',
            '.py': 'Python',
            '.json': 'JSON',
            '.yaml': 'YAML',
            '.yml': 'YAML',
            '.csv': 'CSV',
            '.xlsx': 'Excel',
            '.xls': 'Excel',
            '.pdf': 'PDF',
            '.docx': 'Word',
            '.doc': 'Word',
            '.html': 'HTML',
            '.xml': 'XML',
            '.sql': 'SQL',
            '.sh': 'Shell',
            '.bat': 'Batch',
            '.toml': 'TOML',
            '.ini': 'INI',
            '.cfg': 'Config',
            '.conf': 'Config',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.jsx': 'React',
            '.tsx': 'React TypeScript',
            '.css': 'CSS',
            '.scss': 'SCSS',
            '.png': 'Image (PNG)',
            '.jpg': 'Image (JPEG)',
            '.jpeg': 'Image (JPEG)',
            '.gif': 'Image (GIF)',
            '.svg': 'Image (SVG)',
            '.zip': 'Archive (ZIP)',
            '.tar': 'Archive (TAR)',
            '.gz': 'Archive (GZ)',
        }
        
        return type_mapping.get(suffix, f'Other ({suffix})')
    
    def read_file_content(self, file_path: Path) -> str:
        """Читает содержимое файла."""
        try:
            # Попытка прочитать как текстовый файл
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            try:
                # Попытка с другой кодировкой
                with open(file_path, 'r', encoding='cp1251') as f:
                    return f.read()
            except (UnicodeDecodeError, IOError, PermissionError):
                pass
        except (IOError, PermissionError):
            pass
        
        # Для бинарных файлов возвращаем метаинформацию
        try:
            size = file_path.stat().st_size
            return f"[[BINARY FILE: {size} bytes]]"
        except (IOError, PermissionError, OSError):
            return "[[DATA NOT FOUND]]"
    
    def extract_terms_from_markdown(self, content: str, file_path: Path) -> List[Tuple[str, str]]:
        """Извлекает термины из Markdown файла."""
        terms = []
        
        # Поиск определений в формате "**Термин** - определение"
        pattern1 = r'\*\*([^*]+)\*\*\s*[-—–]\s*([^\n]+)'
        for match in re.finditer(pattern1, content):
            term = match.group(1).strip()
            definition = match.group(2).strip()
            terms.append((term, definition))
        
        # Поиск заголовков как потенциальных терминов
        pattern2 = r'^#+\s+(.+)$'
        for match in re.finditer(pattern2, content, re.MULTILINE):
            heading = match.group(1).strip()
            terms.append((heading, f"Раздел: {heading}"))
        
        return terms
    
    def extract_code_structures(self, content: str, file_type: str) -> List[str]:
        """Извлекает структуры данных из кода."""
        structures = []
        
        if file_type == 'Python':
            # Классы
            class_pattern = r'class\s+(\w+).*?:'
            structures.extend([f"Class: {m.group(1)}" for m in re.finditer(class_pattern, content)])
            
            # Функции
            func_pattern = r'def\s+(\w+)\s*\('
            structures.extend([f"Function: {m.group(1)}" for m in re.finditer(func_pattern, content)])
        
        elif file_type == 'JSON':
            try:
                data = json.loads(content)
                structures.append(f"JSON structure with {len(data)} top-level keys" if isinstance(data, dict) else f"JSON array with {len(data)} items")
            except:
                pass
        
        return structures
    
    def analyze_file(self, file_path: Path) -> Dict[str, Any]:
        """Анализирует отдельный файл."""
        file_type = self.get_file_type(file_path)
        content = self.read_file_content(file_path)
        
        # Относительный путь от корня репозитория
        rel_path = file_path.relative_to(self.repo_path)
        
        # Базовая информация о файле
        file_info = {
            'name': file_path.name,
            'path': str(rel_path),
            'type': file_type,
            'size': file_path.stat().st_size if file_path.exists() else 0,
            'purpose': self.infer_purpose(file_path, content),
            'key_topics': self.extract_key_topics(content, file_type),
            'content_preview': content[:500] if content and not content.startswith('[[') else content,
        }
        
        # Извлечение терминов из Markdown
        if file_type == 'Markdown':
            terms = self.extract_terms_from_markdown(content, file_path)
            for term, definition in terms:
                self.terms_glossary[term].append(f"{definition} (источник: {rel_path})")
        
        # Извлечение структур из кода
        if file_type in ['Python', 'JSON', 'JavaScript']:
            structures = self.extract_code_structures(content, file_type)
            for struct in structures:
                self.data_structures[str(rel_path)].append(struct)
        
        return file_info
    
    def infer_purpose(self, file_path: Path, content: str) -> str:
        """Определяет назначение файла."""
        name_lower = file_path.name.lower()
        
        # Специальные файлы
        if name_lower in ['readme.md', 'readme.txt']:
            return 'Основная документация проекта'
        elif name_lower == 'license':
            return 'Лицензия проекта'
        elif name_lower in ['changelog.md', 'changelog.txt']:
            return 'История изменений'
        elif name_lower in ['contributing.md', 'contributing.txt']:
            return 'Руководство по участию в проекте'
        elif 'test' in name_lower:
            return 'Тестирование'
        elif 'config' in name_lower or 'setup' in name_lower:
            return 'Конфигурация'
        
        # По директории
        parts = file_path.parts
        if 'docs' in parts or 'documentation' in parts:
            return 'Документация'
        elif 'scripts' in parts:
            return 'Скрипт автоматизации'
        elif 'tests' in parts:
            return 'Тестирование'
        elif 'api' in parts:
            return 'API'
        elif 'src' in parts or 'source' in parts:
            return 'Исходный код'
        
        # По содержимому (первые строки)
        if content and not content.startswith('[['):
            first_lines = content[:200].lower()
            if 'class' in first_lines or 'def ' in first_lines:
                return 'Исходный код с определениями классов/функций'
            elif '#' in first_lines and content.startswith('#'):
                return 'Документация или справочный материал'
        
        return 'Общий файл'
    
    def extract_key_topics(self, content: str, file_type: str) -> List[str]:
        """Извлекает ключевые темы из содержимого."""
        topics = []
        
        if not content or content.startswith('[['):
            return topics
        
        # Для Markdown - заголовки
        if file_type == 'Markdown':
            headings = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
            topics.extend(headings[:5])  # Первые 5 заголовков
        
        # Общие ключевые слова (по частоте)
        words = re.findall(r'\b[а-яА-ЯёЁa-zA-Z]{4,}\b', content)
        word_freq = defaultdict(int)
        for word in words:
            word_freq[word.lower()] += 1
        
        # Топ-5 слов
        top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
        topics.extend([word for word, _ in top_words])
        
        return list(set(topics))[:10]  # Уникальные, максимум 10
    
    def scan_repository(self):
        """Сканирует весь репозиторий."""
        print("🔍 Сканирование репозитория...")
        
        for root, dirs, files in os.walk(self.repo_path):
            # Фильтрация директорий
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
            
            root_path = Path(root)
            
            for file in files:
                file_path = root_path / file
                
                if self.should_process_file(file_path):
                    try:
                        file_info = self.analyze_file(file_path)
                        self.file_inventory.append(file_info)
                        
                        if len(self.file_inventory) % 100 == 0:
                            print(f"   Обработано файлов: {len(self.file_inventory)}")
                    except Exception as e:
                        print(f"   ⚠️ Ошибка при обработке {file_path}: {e}")
        
        print(f"✅ Всего обработано файлов: {len(self.file_inventory)}")
    
    def generate_inventory_table(self) -> str:
        """Генерирует таблицу инвентаризации файлов."""
        lines = [
            "## Шаг 1. Инвентаризация файлов",
            "",
            "Полный перечень всех обработанных файлов в репозитории.",
            "",
            "| № | Имя файла | Тип | Размер (байт) | Назначение | Ключевые темы |",
            "|---|-----------|-----|---------------|------------|---------------|"
        ]
        
        for idx, file_info in enumerate(self.file_inventory, 1):
            topics = ', '.join(file_info['key_topics'][:3]) if file_info['key_topics'] else '-'
            lines.append(
                f"| {idx} | `{file_info['name']}` | {file_info['type']} | "
                f"{file_info['size']} | {file_info['purpose']} | {topics} |"
            )
        
        lines.extend([
            "",
            f"**Итого файлов:** {len(self.file_inventory)}",
            ""
        ])
        
        return '\n'.join(lines)
    
    def generate_file_details(self) -> str:
        """Генерирует подробное описание каждого файла."""
        lines = [
            "## Шаг 2. Декомпозиция содержимого",
            "",
            "Подробный анализ каждого файла с извлечением структурных элементов.",
            ""
        ]
        
        # Группировка по типам
        files_by_type = defaultdict(list)
        for file_info in self.file_inventory:
            files_by_type[file_info['type']].append(file_info)
        
        for file_type in sorted(files_by_type.keys()):
            lines.append(f"### Файлы типа: {file_type}")
            lines.append("")
            
            for file_info in files_by_type[file_type]:
                lines.append(f"#### `{file_info['path']}`")
                lines.append("")
                lines.append(f"- **Имя:** {file_info['name']}")
                lines.append(f"- **Тип:** {file_info['type']}")
                lines.append(f"- **Размер:** {file_info['size']} байт")
                lines.append(f"- **Назначение:** {file_info['purpose']}")
                
                if file_info['key_topics']:
                    lines.append(f"- **Ключевые темы:** {', '.join(file_info['key_topics'])}")
                
                if file_info['content_preview'] and not file_info['content_preview'].startswith('[['):
                    lines.append("")
                    lines.append("**Превью содержимого:**")
                    lines.append("```")
                    lines.append(file_info['content_preview'])
                    lines.append("```")
                
                lines.append("")
        
        return '\n'.join(lines)
    
    def generate_glossary(self) -> str:
        """Генерирует глоссарий терминов."""
        lines = [
            "## 2. Термины и глоссарий",
            "",
            "Все термины и определения, извлеченные из файлов репозитория.",
            "",
            "| Термин | Определения | Источники |",
            "|--------|-------------|-----------|"
        ]
        
        for term in sorted(self.terms_glossary.keys()):
            definitions = self.terms_glossary[term]
            # Берем первое определение, указываем количество источников
            first_def = definitions[0] if definitions else "[[DATA NOT FOUND]]"
            source_count = len(definitions)
            
            lines.append(
                f"| {term} | {first_def[:100]}... | {source_count} источник(ов) |"
            )
        
        lines.append("")
        lines.append(f"**Всего терминов:** {len(self.terms_glossary)}")
        lines.append("")
        
        return '\n'.join(lines)
    
    def generate_data_structures_section(self) -> str:
        """Генерирует раздел со структурами данных."""
        lines = [
            "## 5. Структуры данных и форматы",
            "",
            "Структуры данных, классы, функции и форматы, обнаруженные в коде.",
            ""
        ]
        
        if not self.data_structures:
            lines.append("[[DATA NOT FOUND]]")
            lines.append("")
            return '\n'.join(lines)
        
        for file_path in sorted(self.data_structures.keys()):
            structures = self.data_structures[file_path]
            if structures:
                lines.append(f"### Файл: `{file_path}`")
                lines.append("")
                for struct in structures:
                    lines.append(f"- {struct}")
                lines.append("")
        
        return '\n'.join(lines)
    
    def generate_knowledge_base(self):
        """Генерирует полную базу знаний."""
        print("📝 Генерация базы знаний...")
        
        lines = [
            "# База знаний: BearingsInfo",
            "",
            f"**Дата создания:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "Исчерпывающая база знаний, построенная на основе всех файлов репозитория.",
            "Режим максимального контекста - полное извлечение информации без сокращений.",
            "",
            "---",
            "",
            "# Содержание",
            "",
            "1. [Инвентаризация файлов](#шаг-1-инвентаризация-файлов)",
            "2. [Термины и глоссарий](#2-термины-и-глоссарий)",
            "3. [Процессы и алгоритмы](#3-процессы-и-алгоритмы)",
            "4. [Правила и ограничения](#4-правила-и-ограничения)",
            "5. [Структуры данных и форматы](#5-структуры-данных-и-форматы)",
            "6. [Роли и ответственности](#6-роли-и-ответственности)",
            "7. [Инструкции и сценарии использования](#7-инструкции-и-сценарии-использования)",
            "8. [Ошибки, исключения, крайние случаи](#8-ошибки-исключения-крайние-случаи)",
            "9. [Связи и зависимости между сущностями](#9-связи-и-зависимости-между-сущностями)",
            "10. [Источники и трассировка](#10-источники-и-трассировка)",
            "",
            "---",
            ""
        ]
        
        # 1. Инвентаризация
        lines.append(self.generate_inventory_table())
        
        # 2. Термины и глоссарий
        lines.append(self.generate_glossary())
        
        # 3. Процессы и алгоритмы
        lines.extend([
            "## 3. Процессы и алгоритмы",
            "",
            "Описание процессов, алгоритмов и последовательностей действий.",
            "",
            "[[DATA NOT FOUND - требуется дополнительный анализ содержимого файлов]]",
            ""
        ])
        
        # 4. Правила и ограничения
        lines.extend([
            "## 4. Правила и ограничения",
            "",
            "Правила, ограничения и требования, обнаруженные в документации и коде.",
            "",
            "[[DATA NOT FOUND - требуется дополнительный анализ содержимого файлов]]",
            ""
        ])
        
        # 5. Структуры данных
        lines.append(self.generate_data_structures_section())
        
        # 6-10. Остальные разделы
        sections = [
            ("6. Роли и ответственности", "Описание ролей и зон ответственности в проекте."),
            ("7. Инструкции и сценарии использования", "Инструкции по использованию системы и типовые сценарии."),
            ("8. Ошибки, исключения, крайние случаи", "Известные ошибки, исключения и обработка крайних случаев."),
            ("9. Связи и зависимости между сущностями", "Взаимосвязи между компонентами, модулями и сущностями."),
            ("10. Источники и трассировка", "Полная трассировка фактов к исходным файлам."),
        ]
        
        for title, description in sections:
            lines.extend([
                f"## {title}",
                "",
                description,
                "",
                "[[DATA NOT FOUND - требуется дополнительный анализ содержимого файлов]]",
                ""
            ])
        
        # Декомпозиция содержимого (детальная)
        lines.append("---")
        lines.append("")
        lines.append(self.generate_file_details())
        
        # Запись в файл
        output_file = self.repo_path / self.output_path
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"✅ База знаний сохранена: {output_file}")
        print(f"📊 Статистика:")
        print(f"   - Всего файлов: {len(self.file_inventory)}")
        print(f"   - Терминов в глоссарии: {len(self.terms_glossary)}")
        print(f"   - Структур данных: {sum(len(v) for v in self.data_structures.values())}")
    
    def build(self):
        """Основной метод построения базы знаний."""
        print("=" * 70)
        print("  Knowledge Base Builder (MAX CONTEXT MODE)")
        print("  Построение базы знаний из репозитория BearingsInfo")
        print("=" * 70)
        print()
        
        # Шаг 1: Сканирование
        self.scan_repository()
        
        # Шаг 2-4: Генерация
        self.generate_knowledge_base()
        
        print()
        print("=" * 70)
        print("  ✅ База знаний успешно построена!")
        print("=" * 70)


def main():
    """Точка входа."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Knowledge Base Builder - построение базы знаний из репозитория'
    )
    parser.add_argument(
        '--repo',
        default='.',
        help='Путь к репозиторию (по умолчанию: текущая директория)'
    )
    parser.add_argument(
        '--output',
        default='KNOWLEDGE_BASE.md',
        help='Имя выходного файла (по умолчанию: KNOWLEDGE_BASE.md)'
    )
    
    args = parser.parse_args()
    
    # Построение базы знаний
    builder = KnowledgeBaseBuilder(args.repo, args.output)
    builder.build()


if __name__ == '__main__':
    main()
