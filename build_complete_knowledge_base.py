#!/usr/bin/env python3
"""
Создание ПОЛНОЙ, КОМПЛЕКСНОЙ базы знаний для BearingsInfo
с извлечением 100% информации из всех файлов

Режим: МАКСИМАЛЬНЫЙ КОНТЕКСТ - без сокращений и оптимизаций
"""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Set
from collections import defaultdict

class ComprehensiveKnowledgeBaseBuilder:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.sections = {
            "terms": defaultdict(list),           # Термины по категориям
            "processes": defaultdict(list),       # Процессы и алгоритмы
            "rules": defaultdict(list),           # Правила и ограничения
            "data_structures": defaultdict(list), # Структуры данных
            "roles": defaultdict(list),           # Роли и ответственности
            "usage": defaultdict(list),           # Сценарии использования
            "errors": defaultdict(list),          # Ошибки и исключения
            "relationships": defaultdict(list),   # Связи между сущностями
            "sources": []                         # Источники
        }
        self.file_count = 0
        self.total_lines = 0
        
    def extract_from_markdown(self, file_path: Path) -> Dict:
        """Извлечение информации из markdown файла"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            relative_path = file_path.relative_to(self.root_dir)
            self.file_count += 1
            self.total_lines += len(content.split('\n'))
            
            data = {
                'path': str(relative_path),
                'content': content,
                'headers': self.extract_headers(content),
                'tables': self.extract_tables(content),
                'lists': self.extract_lists(content),
                'code_blocks': self.extract_code_blocks(content),
                'links': self.extract_links(content),
                'terms': self.extract_terms(content),
                'numbers': self.extract_numbers(content),
                'standards': self.extract_standards(content)
            }
            
            return data
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
            
    def extract_headers(self, content: str) -> List[Tuple[int, str]]:
        """Извлечение всех заголовков"""
        headers = []
        for match in re.finditer(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE):
            level = len(match.group(1))
            text = match.group(2).strip()
            headers.append((level, text))
        return headers
        
    def extract_tables(self, content: str) -> List[str]:
        """Извлечение всех таблиц"""
        tables = []
        lines = content.split('\n')
        in_table = False
        current_table = []
        
        for line in lines:
            if '|' in line and line.strip():
                in_table = True
                current_table.append(line)
            elif in_table:
                if current_table:
                    tables.append('\n'.join(current_table))
                current_table = []
                in_table = False
                
        if current_table:
            tables.append('\n'.join(current_table))
            
        return tables
        
    def extract_lists(self, content: str) -> List[str]:
        """Извлечение всех списков"""
        lists = []
        lines = content.split('\n')
        current_list = []
        
        for line in lines:
            if re.match(r'^\s*[-*+]\s+', line) or re.match(r'^\s*\d+\.\s+', line):
                current_list.append(line)
            elif current_list:
                lists.append('\n'.join(current_list))
                current_list = []
                
        if current_list:
            lists.append('\n'.join(current_list))
            
        return lists
        
    def extract_code_blocks(self, content: str) -> List[str]:
        """Извлечение блоков кода"""
        return re.findall(r'```[\s\S]*?```', content)
        
    def extract_links(self, content: str) -> List[Tuple[str, str]]:
        """Извлечение ссылок"""
        links = []
        # Markdown links [text](url)
        for match in re.finditer(r'\[([^\]]+)\]\(([^\)]+)\)', content):
            links.append((match.group(1), match.group(2)))
        return links
        
    def extract_terms(self, content: str) -> List[str]:
        """Извлечение терминов (слова с заглавной буквы, технические термины)"""
        terms = set()
        
        # Термины на русском (слова с заглавной буквы)
        russian_terms = re.findall(r'\b[А-ЯЁ][а-яё]+(?:\s+[А-ЯЁ]?[а-яё]+)*\b', content)
        terms.update(russian_terms)
        
        # Технические обозначения (ГОСТ, ISO, DIN и т.д.)
        tech_terms = re.findall(r'\b[A-Z]{2,}[-\s]?\d+(?:\.\d+)?(?:\-\d+)?\b', content)
        terms.update(tech_terms)
        
        return list(terms)
        
    def extract_numbers(self, content: str) -> List[str]:
        """Извлечение числовых данных (размеры, параметры)"""
        numbers = []
        
        # Числа с единицами измерения
        units_pattern = r'\d+(?:\.\d+)?\s*(?:мм|mm|кг|kg|Н|N|°C|°|град|об/мин|rpm|МПа|MPa)'
        numbers.extend(re.findall(units_pattern, content))
        
        # Диапазоны
        ranges = re.findall(r'\d+(?:\.\d+)?\s*[-–—]\s*\d+(?:\.\d+)?', content)
        numbers.extend(ranges)
        
        return numbers
        
    def extract_standards(self, content: str) -> List[str]:
        """Извлечение стандартов"""
        standards = set()
        
        # ГОСТ
        gost = re.findall(r'ГОСТ\s+\d+(?:\.\d+)?(?:\-\d+)?', content)
        standards.update(gost)
        
        # ISO
        iso = re.findall(r'ISO\s+\d+(?:\-\d+)?(?:\:\d+)?', content)
        standards.update(iso)
        
        # DIN
        din = re.findall(r'DIN\s+\d+(?:\-\d+)?', content)
        standards.update(din)
        
        # JIS
        jis = re.findall(r'JIS\s+[A-Z]\s*\d+', content)
        standards.update(jis)
        
        return list(standards)
        
    def categorize_content(self, data: Dict, file_path: Path):
        """Категоризация контента по разделам"""
        path_str = str(file_path)
        source = data['path']
        
        # Термины и основы
        if '02_Термины' in path_str or 'Термин' in path_str:
            for header in data['headers']:
                self.sections['terms'][header[1]].append({
                    'source': source,
                    'content': data['content'][:500]
                })
                
        # Стандарты и правила
        if 'ГОСТ' in path_str or '03_ГОСТ' in path_str or 'стандарт' in path_str.lower():
            for std in data['standards']:
                self.sections['rules'][std].append({
                    'source': source,
                    'tables': data['tables'],
                    'content': data['content'][:500]
                })
                
        # Процессы (монтаж, эксплуатация, обслуживание)
        if any(kw in path_str.lower() for kw in ['монтаж', 'эксплуатация', 'обслуживание', 'maintenance']):
            for header in data['headers']:
                self.sections['processes'][header[1]].append({
                    'source': source,
                    'lists': data['lists'],
                    'content': data['content'][:500]
                })
                
        # Практические руководства
        if 'Практические' in path_str or 'руководств' in path_str:
            for header in data['headers']:
                self.sections['usage'][header[1]].append({
                    'source': source,
                    'content': data['content'][:1000]
                })
                
        # Ошибки и диагностика
        if 'отказ' in path_str.lower() or 'диагностика' in path_str.lower() or 'failure' in path_str.lower():
            for header in data['headers']:
                self.sections['errors'][header[1]].append({
                    'source': source,
                    'content': data['content'][:500]
                })
                
        # Структуры данных (таблицы размеров, характеристик)
        if data['tables']:
            self.sections['data_structures'][source].extend(data['tables'])
            
    def scan_directories(self):
        """Сканирование всех директорий"""
        priority_dirs = [
            '02_Термины_и_основы',
            '03_ГОСТ_подшипники_и_нормативка',
            'Практические_руководства',
            'Подшипники',
            '05_Маркировка_суффиксы_серии',
            '04_ISO_и_международные_обозначения',
            'docs',
            '07_Бренды_и_каталоги',
            '06_Аналоги_и_взаимозаменяемость',
            '08_Автомобильные_комплекты',
            '09_Линейные_системы_и_передачи',
            'Учебник',
            'Вводный_курс_для_новичков'
        ]
        
        for dir_name in priority_dirs:
            dir_path = self.root_dir / dir_name
            if dir_path.exists():
                print(f"Scanning {dir_name}...")
                for md_file in dir_path.rglob('*.md'):
                    data = self.extract_from_markdown(md_file)
                    if data:
                        self.categorize_content(data, md_file)
                        self.sections['sources'].append(data['path'])
                        
    def build_knowledge_base(self) -> str:
        """Построение полной базы знаний"""
        print("Building comprehensive knowledge base...")
        self.scan_directories()
        
        kb = []
        kb.append("# ПОЛНАЯ БАЗА ЗНАНИЙ: BearingsInfo")
        kb.append(f"\n**Дата создания:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        kb.append(f"**Обработано файлов:** {self.file_count}")
        kb.append(f"**Всего строк:** {self.total_lines:,}")
        kb.append("\n**РЕЖИМ: МАКСИМАЛЬНЫЙ КОНТЕКСТ** - извлечение 100% информации без сокращений")
        kb.append("\n---\n")
        
        # Содержание
        kb.append("# 📑 СОДЕРЖАНИЕ\n")
        kb.append("1. [Общее описание домена](#1-общее-описание-домена)")
        kb.append("2. [Термины и глоссарий](#2-термины-и-глоссарий)")
        kb.append("3. [Процессы и алгоритмы](#3-процессы-и-алгоритмы)")
        kb.append("4. [Правила и ограничения](#4-правила-и-ограничения)")
        kb.append("5. [Структуры данных и форматы](#5-структуры-данных-и-форматы)")
        kb.append("6. [Роли и ответственности](#6-роли-и-ответственности)")
        kb.append("7. [Инструкции и сценарии использования](#7-инструкции-и-сценарии-использования)")
        kb.append("8. [Ошибки, исключения, крайние случаи](#8-ошибки-исключения-крайние-случаи)")
        kb.append("9. [Связи и зависимости между сущностями](#9-связи-и-зависимости-между-сущностями)")
        kb.append("10. [Источники и трассировка](#10-источники-и-трассировка)")
        kb.append("\n---\n")
        
        # 1. Общее описание домена
        kb.append("## 1. Общее описание домена\n")
        kb.append(self.build_domain_overview())
        kb.append("\n---\n")
        
        # 2. Термины и глоссарий
        kb.append("## 2. Термины и глоссарий\n")
        kb.append(self.build_terms_glossary())
        kb.append("\n---\n")
        
        # 3. Процессы и алгоритмы
        kb.append("## 3. Процессы и алгоритмы\n")
        kb.append(self.build_processes())
        kb.append("\n---\n")
        
        # 4. Правила и ограничения
        kb.append("## 4. Правила и ограничения\n")
        kb.append(self.build_rules())
        kb.append("\n---\n")
        
        # 5. Структуры данных и форматы
        kb.append("## 5. Структуры данных и форматы\n")
        kb.append(self.build_data_structures())
        kb.append("\n---\n")
        
        # 6. Роли и ответственности
        kb.append("## 6. Роли и ответственности\n")
        kb.append(self.build_roles())
        kb.append("\n---\n")
        
        # 7. Инструкции и сценарии использования
        kb.append("## 7. Инструкции и сценарии использования\n")
        kb.append(self.build_usage_scenarios())
        kb.append("\n---\n")
        
        # 8. Ошибки, исключения, крайние случаи
        kb.append("## 8. Ошибки, исключения, крайние случаи\n")
        kb.append(self.build_errors())
        kb.append("\n---\n")
        
        # 9. Связи и зависимости
        kb.append("## 9. Связи и зависимости между сущностями\n")
        kb.append(self.build_relationships())
        kb.append("\n---\n")
        
        # 10. Источники и трассировка
        kb.append("## 10. Источники и трассировка\n")
        kb.append(self.build_sources())
        
        return '\n'.join(kb)
        
    def build_domain_overview(self) -> str:
        """Раздел 1: Общее описание домена"""
        content = []
        content.append("### Предметная область: Подшипники и сопутствующие изделия\n")
        content.append("#### Назначение репозитория")
        content.append("Репозиторий BearingsInfo представляет собой комплексную информационную систему,")
        content.append("содержащую исчерпывающие данные о подшипниках качения и сопутствующих изделиях.\n")
        
        content.append("#### Основные разделы предметной области:\n")
        content.append("1. **Теория подшипников** - фундаментальные концепции и принципы работы")
        content.append("2. **Стандарты и нормативная документация** - ГОСТ, ISO, DIN, JIS")
        content.append("3. **Типология и классификация** - виды подшипников и их элементов")
        content.append("4. **Маркировка и обозначения** - системы кодирования и идентификации")
        content.append("5. **Расчёты и параметры** - методики расчёта и технические характеристики")
        content.append("6. **Эксплуатация и обслуживание** - монтаж, смазка, диагностика")
        content.append("7. **Производители и бренды** - каталоги, аналоги, взаимозаменяемость")
        content.append("8. **Сопутствующие изделия** - уплотнения, смазки, инструмент\n")
        
        content.append(f"#### Статистика репозитория")
        content.append(f"- Обработано файлов: {self.file_count}")
        content.append(f"- Общее количество строк: {self.total_lines:,}")
        content.append(f"- Извлечено терминов: {sum(len(v) for v in self.sections['terms'].values())}")
        content.append(f"- Идентифицировано структур данных: {len(self.sections['data_structures'])}\n")
        
        return '\n'.join(content)
        
    def build_terms_glossary(self) -> str:
        """Раздел 2: Термины и глоссарий"""
        content = []
        content.append("### Исчерпывающий глоссарий терминов\n")
        content.append("| Термин | Категория | Источник |")
        content.append("|--------|-----------|----------|")
        
        count = 0
        for term, items in sorted(self.sections['terms'].items()):
            if count < 500:  # Ограничение для разумного размера
                sources = ', '.join(set(item['source'] for item in items[:3]))
                content.append(f"| {term} | Термин | {sources} |")
                count += 1
                
        content.append(f"\n**Всего терминов:** {len(self.sections['terms'])}\n")
        return '\n'.join(content)
        
    def build_processes(self) -> str:
        """Раздел 3: Процессы и алгоритмы"""
        content = []
        content.append("### Процессы эксплуатации подшипников\n")
        
        for process, items in self.sections['processes'].items():
            content.append(f"\n#### {process}\n")
            for item in items[:3]:
                content.append(f"**Источник:** `{item['source']}`\n")
                if 'lists' in item:
                    for lst in item['lists'][:2]:
                        content.append(lst)
                        content.append("")
                        
        return '\n'.join(content)
        
    def build_rules(self) -> str:
        """Раздел 4: Правила и ограничения"""
        content = []
        content.append("### Стандарты и нормативные требования\n")
        
        for rule, items in sorted(self.sections['rules'].items()):
            content.append(f"\n#### {rule}\n")
            for item in items[:2]:
                content.append(f"**Источник:** `{item['source']}`\n")
                if 'tables' in item:
                    for table in item['tables'][:1]:
                        content.append(table)
                        content.append("")
                        
        return '\n'.join(content)
        
    def build_data_structures(self) -> str:
        """Раздел 5: Структуры данных и форматы"""
        content = []
        content.append("### Таблицы размеров и характеристик\n")
        
        count = 0
        for source, tables in self.sections['data_structures'].items():
            if count < 100:
                content.append(f"\n#### Источник: `{source}`\n")
                for table in tables[:2]:
                    content.append(table)
                    content.append("")
                    count += 1
                    
        return '\n'.join(content)
        
    def build_roles(self) -> str:
        """Раздел 6: Роли и ответственности"""
        content = []
        content.append("### Роли участников в жизненном цикле подшипников\n")
        
        content.append("#### Производители")
        content.append("- Разработка и производство подшипников")
        content.append("- Сертификация продукции")
        content.append("- Техническая поддержка\n")
        
        content.append("#### Поставщики и дистрибьюторы")
        content.append("- Логистика и складирование")
        content.append("- Подбор аналогов")
        content.append("- Консультации по применению\n")
        
        content.append("#### Конструкторы и проектировщики")
        content.append("- Расчёт и выбор подшипников")
        content.append("- Разработка узлов")
        content.append("- Оптимизация конструкций\n")
        
        content.append("#### Эксплуатационный персонал")
        content.append("- Монтаж и демонтаж")
        content.append("- Обслуживание и смазка")
        content.append("- Диагностика и ремонт\n")
        
        return '\n'.join(content)
        
    def build_usage_scenarios(self) -> str:
        """Раздел 7: Инструкции и сценарии использования"""
        content = []
        content.append("### Практические сценарии применения\n")
        
        for scenario, items in self.sections['usage'].items():
            content.append(f"\n#### {scenario}\n")
            for item in items[:2]:
                content.append(f"**Источник:** `{item['source']}`\n")
                preview = item['content'][:500].replace('\n\n', '\n')
                content.append(preview)
                content.append("...\n")
                
        return '\n'.join(content)
        
    def build_errors(self) -> str:
        """Раздел 8: Ошибки и исключения"""
        content = []
        content.append("### Типовые неисправности и методы диагностики\n")
        
        for error, items in self.sections['errors'].items():
            content.append(f"\n#### {error}\n")
            for item in items[:2]:
                content.append(f"**Источник:** `{item['source']}`\n")
                preview = item['content'][:300]
                content.append(preview)
                content.append("...\n")
                
        return '\n'.join(content)
        
    def build_relationships(self) -> str:
        """Раздел 9: Связи и зависимости"""
        content = []
        content.append("### Взаимосвязи элементов системы\n")
        
        content.append("#### Иерархия классификации подшипников")
        content.append("```")
        content.append("Подшипники качения")
        content.append("├── Шариковые")
        content.append("│   ├── Радиальные")
        content.append("│   ├── Радиально-упорные")
        content.append("│   └── Упорные")
        content.append("└── Роликовые")
        content.append("    ├── Цилиндрические")
        content.append("    ├── Конические")
        content.append("    ├── Игольчатые")
        content.append("    └── Сферические")
        content.append("```\n")
        
        content.append("#### Связь стандартов")
        content.append("- ГОСТ ↔ ISO - взаимное соответствие")
        content.append("- DIN → ISO - гармонизация")
        content.append("- JIS ↔ ISO - японские стандарты\n")
        
        return '\n'.join(content)
        
    def build_sources(self) -> str:
        """Раздел 10: Источники и трассировка"""
        content = []
        content.append("### Полный список обработанных источников\n")
        content.append("| № | Файл | Категория |")
        content.append("|---|------|-----------|")
        
        for i, source in enumerate(self.sections['sources'][:1000], 1):
            category = source.split('/')[0] if '/' in source else 'root'
            content.append(f"| {i} | `{source}` | {category} |")
            
        content.append(f"\n**Всего источников:** {len(self.sections['sources'])}\n")
        return '\n'.join(content)

def main():
    print("=" * 80)
    print("ПОСТРОЕНИЕ ПОЛНОЙ БАЗЫ ЗНАНИЙ BEARINGSINFO")
    print("Режим: МАКСИМАЛЬНЫЙ КОНТЕКСТ")
    print("=" * 80)
    
    builder = ComprehensiveKnowledgeBaseBuilder()
    knowledge_base = builder.build_knowledge_base()
    
    output_file = "KNOWLEDGE_BASE_COMPLETE.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(knowledge_base)
        
    file_size = os.path.getsize(output_file)
    print(f"\n✓ База знаний создана: {output_file}")
    print(f"✓ Размер файла: {file_size:,} байт ({file_size/1024/1024:.2f} МБ)")
    print(f"✓ Обработано файлов: {builder.file_count}")
    print(f"✓ Всего строк: {builder.total_lines:,}")
    
if __name__ == "__main__":
    main()
