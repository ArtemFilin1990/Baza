#!/usr/bin/env python3
"""
Построение поискового индекса и вычисление схожести документов
"""

import os
import json
import re
from typing import Dict


class SearchIndexBuilder:
    """Построитель поискового индекса"""

    def __init__(self, repo_root: str = None):
        self.repo_root = repo_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.documents = {}
        self.similarity_matrix = {}

    def extract_documents(self) -> Dict:
        """Извлечь все документы из репозитория"""
        print("Извлечение документов...")

        doc_id = 0
        for root, dirs, files in os.walk(self.repo_root):
            # Пропускаем служебные директории
            dirs[:] = [
                d
                for d in dirs
                if not d.startswith(".") and d not in ["node_modules", "__pycache__", "api", "scripts", "data"]
            ]

            for file in files:
                if file.endswith(".md") and file not in ["README.md"]:
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()

                            # Извлекаем заголовок
                            title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                            title = title_match.group(1) if title_match else file.replace(".md", "")

                            # Относительный путь от корня репозитория
                            rel_path = os.path.relpath(file_path, self.repo_root)

                            self.documents[f"doc_{doc_id}"] = {
                                "id": f"doc_{doc_id}",
                                "title": title,
                                "path": rel_path,
                                "content": content,
                                "word_count": len(content.split()),
                            }
                            doc_id += 1
                    except Exception as e:
                        print(f"Ошибка при чтении {file_path}: {e}")

        print(f"Извлечено {len(self.documents)} документов")
        return self.documents

    def compute_document_similarity(self):
        """
        Вычислить схожесть между документами методом TF-IDF + косинусное расстояние

        Для каждого документа найти 5 наиболее похожих
        """
        print("Вычисление схожести документов...")

        try:
            from sklearn.feature_extraction.text import TfidfVectorizer
            from sklearn.metrics.pairwise import cosine_similarity
            import numpy as np
        except ImportError:
            print("Для вычисления схожести требуются библиотеки scikit-learn и numpy")
            print("Установите их: pip install scikit-learn numpy")
            return {}

        if not self.documents:
            self.extract_documents()

        # Подготовка текстов
        doc_ids = list(self.documents.keys())
        texts = [self.documents[doc_id]["content"] for doc_id in doc_ids]

        # Построение TF-IDF матрицы
        print("Построение TF-IDF матрицы...")
        vectorizer = TfidfVectorizer(
            max_features=1000,
            stop_words=None,  # Для русского языка нужен отдельный список стоп-слов
            ngram_range=(1, 2),
        )

        try:
            tfidf_matrix = vectorizer.fit_transform(texts)
        except Exception as e:
            print(f"Ошибка при построении TF-IDF матрицы: {e}")
            return {}

        # Вычисление косинусного расстояния
        print("Вычисление косинусного расстояния...")
        similarity_matrix = cosine_similarity(tfidf_matrix)

        # Для каждого документа сохранить топ-5 похожих
        for i, doc_id in enumerate(doc_ids):
            # Получаем индексы похожих документов (исключая сам документ)
            similar_indices = similarity_matrix[i].argsort()[::-1][1:6]  # Топ-5, исключая себя

            similar_docs = []
            for idx in similar_indices:
                if idx < len(doc_ids):  # Проверка границ
                    similar_doc_id = doc_ids[idx]
                    score = float(similarity_matrix[i][idx])

                    # Добавляем только если score > 0.1
                    if score > 0.1:
                        similar_docs.append(
                            {
                                "doc_id": similar_doc_id,
                                "title": self.documents[similar_doc_id]["title"],
                                "score": round(score, 4),
                            }
                        )

            self.similarity_matrix[doc_id] = {"similar": similar_docs}

        print(f"Вычислена схожесть для {len(self.similarity_matrix)} документов")
        return self.similarity_matrix

    def save_similarity_matrix(self, output_path: str):
        """
        Сохранить матрицу схожести:
        {
          "doc_123": {
            "similar": [
              {"doc_id": "doc_456", "title": "...", "score": 0.85},
              {"doc_id": "doc_789", "title": "...", "score": 0.72}
            ]
          }
        }
        """
        print("Сохранение матрицы схожести...")

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(self.similarity_matrix, f, ensure_ascii=False, indent=2)

        print(f"Матрица схожести сохранена в {output_path}")

    def save_document_index(self, output_path: str):
        """Сохранить индекс документов"""
        print("Сохранение индекса документов...")

        # Убираем полный контент для экономии места
        index = {}
        for doc_id, doc in self.documents.items():
            index[doc_id] = {
                "id": doc["id"],
                "title": doc["title"],
                "path": doc["path"],
                "word_count": doc["word_count"],
                "excerpt": doc["content"][:200] + "..." if len(doc["content"]) > 200 else doc["content"],
            }

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False, indent=2)

        print(f"Индекс документов сохранен в {output_path}")


def main():
    """Основная функция"""
    print("=" * 60)
    print("Построение поискового индекса")
    print("=" * 60)

    builder = SearchIndexBuilder()

    # Извлекаем документы
    builder.extract_documents()

    # Вычисляем схожесть
    builder.compute_document_similarity()

    # Сохраняем результаты
    data_dir = os.path.join(builder.repo_root, "data")
    builder.save_similarity_matrix(os.path.join(data_dir, "similarity_matrix.json"))
    builder.save_document_index(os.path.join(data_dir, "document_index.json"))

    print("=" * 60)
    print("Готово!")
    print("=" * 60)


if __name__ == "__main__":
    main()
