#!/usr/bin/env python3
"""
Построение словаря для автодополнения из:
- Названий подшипников (6205, 180205, SKF 6205 и т.д.)
- Терминов (подшипник, сепаратор, зазор и т.д.)
- Брендов (SKF, FAG, NSK и т.д.)
- Серий (60, 62, 63 и т.д.)
"""

import os
import re
import json
from collections import defaultdict, Counter
from typing import Dict


class AutocompleteDictBuilder:
    """Построитель словаря автодополнения"""

    def __init__(self, repo_root: str = None):
        self.repo_root = repo_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.terms = Counter()
        self.bearing_codes = Counter()
        self.brands = Counter()
        self.series = Counter()

        # Известные бренды подшипников
        self.known_brands = {
            "SKF",
            "FAG",
            "NSK",
            "NTN",
            "TIMKEN",
            "INA",
            "KOYO",
            "NACHI",
            "THK",
            "SNR",
            "RHP",
            "ZVL",
            "URB",
            "GPZ",
            "UBC",
            "APTM",
            "HEIM",
        }

    def extract_terms_from_documents(self) -> Dict[str, int]:
        """Извлечь термины из всех документов"""
        print("Извлечение терминов из документов...")

        # Технические термины для подшипников
        technical_terms = [
            "подшипник",
            "подшипники",
            "подшипниковый",
            "подшипниковые",
            "сепаратор",
            "зазор",
            "посадка",
            "преднатяг",
            "шариковый",
            "роликовый",
            "игольчатый",
            "конический",
            "радиальный",
            "упорный",
            "упорно-радиальный",
            "уплотнение",
            "уплотнения",
            "уплотнительный",
            "втулка",
            "втулки",
            "вал",
            "корпус",
            "нагрузка",
            "скорость",
            "температура",
            "смазка",
            "монтаж",
            "демонтаж",
            "ресурс",
            "износ",
            "качение",
            "скольжение",
            "трение",
            "серия",
            "стандарт",
            "гост",
            "iso",
            "диаметр",
            "ширина",
            "высота",
            "размер",
            "аналог",
            "взаимозаменяемость",
            "замена",
            "каталог",
            "маркировка",
            "обозначение",
        ]

        for term in technical_terms:
            self.terms[term] += 100  # Базовый приоритет

        # Сканирование документов
        for root, dirs, files in os.walk(self.repo_root):
            # Пропускаем служебные директории
            dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ["node_modules", "__pycache__"]]

            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read().lower()
                            # Извлекаем слова
                            words = re.findall(r"\b[а-яё]{4,}\b", content)
                            for word in words:
                                if word in technical_terms:
                                    self.terms[word] += 1
                    except Exception as e:
                        print(f"Ошибка при чтении {file_path}: {e}")

        return dict(self.terms)

    def extract_bearing_codes(self) -> Dict[str, int]:
        """Извлечь коды подшипников из базы данных и документов"""
        print("Извлечение кодов подшипников...")

        # Паттерны для распознавания кодов подшипников
        patterns = [
            r"\b\d{4,7}\b",  # Простые числовые коды: 6205, 180205
            r"\b[A-Z]{2,4}\s*\d{4,7}\b",  # С префиксом бренда: SKF 6205
            r"\b\d{1,3}[A-Z]{1,2}\d{2,5}\b",  # Комбинированные: 62RS205
        ]

        for root, dirs, files in os.walk(self.repo_root):
            dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ["node_modules", "__pycache__"]]

            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            # Ищем коды подшипников
                            for pattern in patterns:
                                matches = re.findall(pattern, content)
                                for match in matches:
                                    # Фильтруем слишком общие числа
                                    if len(match) >= 4 and not match.isspace():
                                        self.bearing_codes[match] += 1
                    except Exception as e:
                        # Пропускаем файлы с ошибками чтения
                        print(f"Ошибка при чтении {file_path}: {e}")

        # Добавляем популярные серии подшипников
        common_series = [
            "6000",
            "6200",
            "6300",
            "6400",
            "6001",
            "6201",
            "6301",
            "6401",
            "6002",
            "6202",
            "6302",
            "6402",
            "6003",
            "6203",
            "6303",
            "6403",
            "6004",
            "6204",
            "6304",
            "6404",
            "6005",
            "6205",
            "6305",
            "6405",
            "6006",
            "6206",
            "6306",
            "6406",
            "6007",
            "6207",
            "6307",
            "6407",
            "6008",
            "6208",
            "6308",
            "6408",
            "6009",
            "6209",
            "6309",
            "6409",
            "6010",
            "6210",
            "6310",
            "6410",
        ]

        for code in common_series:
            self.bearing_codes[code] += 50

        return dict(self.bearing_codes)

    def extract_brands(self) -> Dict[str, int]:
        """Извлечь бренды из документов"""
        print("Извлечение брендов...")

        for brand in self.known_brands:
            self.brands[brand] += 100  # Базовый приоритет
            self.brands[brand.lower()] += 50

        # Сканирование для подсчета упоминаний
        for root, dirs, files in os.walk(self.repo_root):
            dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ["node_modules", "__pycache__"]]

            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            for brand in self.known_brands:
                                # Подсчет упоминаний бренда
                                count = len(re.findall(r"\b" + re.escape(brand) + r"\b", content, re.IGNORECASE))
                                if count > 0:
                                    self.brands[brand] += count
                    except Exception as e:
                        # Пропускаем файлы с ошибками чтения
                        continue

        return dict(self.brands)

    def extract_series(self) -> Dict[str, int]:
        """Извлечь серии подшипников"""
        print("Извлечение серий подшипников...")

        # Популярные серии подшипников
        common_series = ["60", "62", "63", "64", "160", "180", "618", "619"]

        for series in common_series:
            self.series[series] += 100

        return dict(self.series)

    def build_trie_structure(self) -> Dict:
        """Построить префиксное дерево для быстрого поиска"""
        print("Построение префиксного дерева...")

        index = defaultdict(list)

        # Индексируем термины
        for term, freq in self.terms.items():
            for i in range(1, len(term) + 1):
                prefix = term[:i].lower()
                if term not in [t["value"] for t in index[prefix]]:
                    index[prefix].append(term)

        # Индексируем коды подшипников
        for code, freq in self.bearing_codes.items():
            for i in range(1, len(code) + 1):
                prefix = code[:i].lower()
                if code not in [c for c in index[prefix]]:
                    index[prefix].append(code)

        # Индексируем бренды
        for brand, freq in self.brands.items():
            for i in range(1, len(brand) + 1):
                prefix = brand[:i].lower()
                if brand not in [b for b in index[prefix]]:
                    index[prefix].append(brand)

        # Индексируем серии
        for series, freq in self.series.items():
            for i in range(1, len(series) + 1):
                prefix = series[:i].lower()
                if series not in [s for s in index[prefix]]:
                    index[prefix].append(series)

        # Ограничиваем размер индекса для каждого префикса
        for prefix in index:
            index[prefix] = index[prefix][:50]

        return dict(index)

    def save_autocomplete_dict(self, output_path: str):
        """
        Сохранить словарь в JSON:
        {
          "terms": [
            {"value": "подшипник", "frequency": 1240, "type": "term"},
            {"value": "6205", "frequency": 890, "type": "bearing_code"},
            {"value": "SKF", "frequency": 456, "type": "brand"}
          ],
          "index": {
            "п": ["подшипник", "посадка", "преднатяг"],
            "6": ["6205", "6305", "6405"],
            "s": ["SKF", "сепаратор"]
          }
        }
        """
        print("Сохранение словаря автодополнения...")

        # Собираем все термины
        all_terms = []

        for term, freq in self.terms.items():
            all_terms.append({"value": term, "frequency": freq, "type": "term"})

        for code, freq in self.bearing_codes.items():
            all_terms.append({"value": code, "frequency": freq, "type": "bearing_code"})

        for brand, freq in self.brands.items():
            all_terms.append({"value": brand, "frequency": freq, "type": "brand"})

        for series, freq in self.series.items():
            all_terms.append({"value": series, "frequency": freq, "type": "series"})

        # Сортируем по частоте
        all_terms.sort(key=lambda x: x["frequency"], reverse=True)

        # Строим индекс
        index = self.build_trie_structure()

        # Формируем итоговый словарь
        result = {
            "terms": all_terms[:1000],  # Топ-1000 терминов
            "index": index,
            "metadata": {
                "total_terms": len(all_terms),
                "total_bearing_codes": len(self.bearing_codes),
                "total_brands": len(self.brands),
                "total_series": len(self.series),
            },
        }

        # Сохраняем
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"Словарь сохранен в {output_path}")
        print(f"Всего терминов: {len(all_terms)}")
        print(f"Всего кодов подшипников: {len(self.bearing_codes)}")
        print(f"Всего брендов: {len(self.brands)}")
        print(f"Всего серий: {len(self.series)}")


def main():
    """Основная функция"""
    print("=" * 60)
    print("Построение словаря автодополнения")
    print("=" * 60)

    builder = AutocompleteDictBuilder()

    # Извлекаем данные
    builder.extract_terms_from_documents()
    builder.extract_bearing_codes()
    builder.extract_brands()
    builder.extract_series()

    # Сохраняем словарь
    output_path = os.path.join(builder.repo_root, "data", "autocomplete_dict.json")
    builder.save_autocomplete_dict(output_path)

    print("=" * 60)
    print("Готово!")
    print("=" * 60)


if __name__ == "__main__":
    main()
