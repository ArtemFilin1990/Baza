"""
<<<<<<< HEAD
Логика автодополнения и поиска
"""

import json
import os
from typing import List, Dict


class AutocompleteEngine:
    """Движок автодополнения поисковых запросов"""
    
    def __init__(self, dict_path: str = "data/autocomplete_dict.json"):
        self.dict_path = dict_path
        self.terms = []
        self.index = {}
        self.metadata = {}
        self.load_dictionary(dict_path)
    
    def load_dictionary(self, dict_path: str):
        """Загрузить словарь автодополнения"""
        if not os.path.exists(dict_path):
            print(f"Словарь автодополнения не найден: {dict_path}")
            return
        
        try:
            with open(dict_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.terms = data.get('terms', [])
                self.index = data.get('index', {})
                self.metadata = data.get('metadata', {})
        except Exception as e:
            print(f"Ошибка при загрузке словаря: {e}")
    
    def suggest(self, prefix: str, limit: int = 10, types: List[str] = None) -> List[Dict]:
        """
        Генерировать предложения по префиксу
        
        Алгоритм:
        1. Нормализовать запрос (lowercase, удалить спецсимволы)
        2. Найти в префиксном дереве
        3. Отсортировать по частотности
        4. Применить фильтры по типу
        5. Вернуть top-N результатов
        """
        if not prefix or len(prefix) < 1:
            return []
        
        # Нормализация запроса
        normalized_prefix = prefix.lower().strip()
        
        # Поиск в индексе
        candidates = self.index.get(normalized_prefix, [])
        
        # Если не найдено в индексе, ищем в полном списке терминов
        if not candidates:
            candidates = []
            for term in self.terms:
                if term['value'].lower().startswith(normalized_prefix):
                    candidates.append(term['value'])
        
        # Получаем полную информацию о кандидатах
        suggestions = []
        for candidate in candidates[:limit * 2]:  # Берем больше для фильтрации
            # Ищем в списке терминов
            term_info = next((t for t in self.terms if t['value'] == candidate), None)
            if term_info:
                # Фильтр по типу
                if types and term_info['type'] not in types:
                    continue
                
                # Подсветка совпадения
                highlighted = self._highlight_match(term_info['value'], prefix)
                
                suggestions.append({
                    'value': term_info['value'],
                    'type': term_info['type'],
                    'frequency': term_info['frequency'],
                    'highlight': highlighted
                })
        
        # Сортировка по частотности
        suggestions.sort(key=lambda x: x['frequency'], reverse=True)
        
        return suggestions[:limit]
    
    def _highlight_match(self, value: str, prefix: str) -> str:
        """Подсветка совпадающей части"""
        if not prefix:
            return value
        
        # Находим позицию совпадения (регистронезависимо)
        value_lower = value.lower()
        prefix_lower = prefix.lower()
        
        pos = value_lower.find(prefix_lower)
        if pos == -1:
            return value
        
        # Создаем подсвеченную версию
        highlighted = (
            value[:pos] + 
            '<b>' + value[pos:pos+len(prefix)] + '</b>' + 
            value[pos+len(prefix):]
        )
        
        return highlighted
    
    def get_popular_searches(self, limit: int = 10) -> List[Dict]:
        """Получить самые популярные поисковые запросы"""
        # Сортируем по частотности
        sorted_terms = sorted(self.terms, key=lambda x: x['frequency'], reverse=True)
        
        # Возвращаем топ-N
        return sorted_terms[:limit]


class DocumentSearchEngine:
    """Движок поиска документов"""
    
    def __init__(self, 
                 index_path: str = "data/document_index.json",
                 similarity_path: str = "data/similarity_matrix.json"):
        self.index_path = index_path
        self.similarity_path = similarity_path
        self.documents = {}
        self.similarity_matrix = {}
        self.load_data()
    
    def load_data(self):
        """Загрузить индекс документов и матрицу схожести"""
        # Загрузка индекса документов
        if os.path.exists(self.index_path):
            try:
                with open(self.index_path, 'r', encoding='utf-8') as f:
                    self.documents = json.load(f)
            except Exception as e:
                print(f"Ошибка при загрузке индекса документов: {e}")
        
        # Загрузка матрицы схожести
        if os.path.exists(self.similarity_path):
            try:
                with open(self.similarity_path, 'r', encoding='utf-8') as f:
                    self.similarity_matrix = json.load(f)
            except Exception as e:
                print(f"Ошибка при загрузке матрицы схожести: {e}")
    
    def search(self, query: str, limit: int = 20) -> List[Dict]:
        """
        Простой поиск по документам
        
        В реальной системе здесь должен быть полнотекстовый поиск
        (Elasticsearch, PostgreSQL Full-Text Search, etc.)
        """
        if not query:
            return []
        
        query_lower = query.lower()
        results = []
        
        for doc_id, doc in self.documents.items():
            # Простой поиск по названию и описанию
            if (query_lower in doc['title'].lower() or 
                query_lower in doc.get('excerpt', '').lower()):
                
                # Вычисление релевантности (упрощенно)
                relevance = 0.5
                if query_lower in doc['title'].lower():
                    relevance += 0.5
                
                results.append({
                    'id': doc_id,
                    'title': doc['title'],
                    'path': doc['path'],
                    'excerpt': doc.get('excerpt', ''),
                    'relevance': relevance
                })
        
        # Сортировка по релевантности
        results.sort(key=lambda x: x['relevance'], reverse=True)
        
        return results[:limit]
    
    def get_similar_documents(self, document_id: str, limit: int = 5) -> List[Dict]:
        """Получить похожие документы для конкретного документа"""
        if document_id not in self.similarity_matrix:
            return []
        
        similar = self.similarity_matrix[document_id].get('similar', [])
        
        # Дополняем информацией из индекса
        result = []
        for sim_doc in similar[:limit]:
            doc_id = sim_doc['doc_id']
            if doc_id in self.documents:
                result.append({
                    'id': doc_id,
                    'title': sim_doc.get('title', self.documents[doc_id]['title']),
                    'path': self.documents[doc_id]['path'],
                    'similarity': sim_doc['score']
                })
        
        return result


class SearchHistory:
    """Управление историей поиска (заглушка для работы без БД)"""
    
    def __init__(self):
        self.history = []
    
    def add_search(self, user_id: str, query: str, results_count: int, session_id: str = None):
        """Добавить запись в историю поиска"""
        from datetime import datetime
        
        self.history.append({
            'user_id': user_id,
            'query': query,
            'results_count': results_count,
            'session_id': session_id,
            'timestamp': datetime.now().isoformat()
        })
    
    def get_user_history(self, user_id: str, limit: int = 50) -> List[Dict]:
        """Получить историю поиска пользователя"""
        user_searches = [h for h in self.history if h['user_id'] == user_id]
        user_searches.sort(key=lambda x: x['timestamp'], reverse=True)
        return user_searches[:limit]
    
    def clear_user_history(self, user_id: str):
        """Очистить историю поиска пользователя"""
        self.history = [h for h in self.history if h['user_id'] != user_id]
    
    def get_popular_queries(self, limit: int = 10) -> List[Dict]:
        """Получить популярные поисковые запросы"""
        from collections import Counter
        
        queries = [h['query'] for h in self.history]
        counter = Counter(queries)
        
        popular = []
        for query, count in counter.most_common(limit):
            popular.append({
                'query': query,
                'count': count
            })
        
        return popular
=======
Бизнес-логика приложения.

Содержит логику обработки данных о подшипниках:
- Поиск и фильтрация
- Расчеты характеристик
- Определение аналогов
- Валидация данных
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class BearingLogic:
    """Класс с бизнес-логикой для работы с подшипниками."""

    @staticmethod
    def search_bearings(
        designation: Optional[str] = None,
        bearing_type: Optional[str] = None,
        inner_diameter: Optional[float] = None,
        outer_diameter: Optional[float] = None,
    ) -> List[Dict[str, Any]]:
        """
        Поиск подшипников по параметрам.

        Args:
            designation: Обозначение подшипника
            bearing_type: Тип подшипника
            inner_diameter: Внутренний диаметр
            outer_diameter: Наружный диаметр

        Returns:
            Список найденных подшипников
        """
        logger.error("Bearing search is not implemented yet")
        raise NotImplementedError("Bearing search is not implemented yet.")

    @staticmethod
    def find_analogs(designation: str) -> List[Dict[str, Any]]:
        """
        Найти аналоги подшипника.

        Args:
            designation: Обозначение подшипника

        Returns:
            Список аналогов
        """
        logger.error("Bearing analog search is not implemented yet")
        raise NotImplementedError("Bearing analog search is not implemented yet.")

    @staticmethod
    def calculate_capacity(
        bearing_type: str,
        dimensions: Dict[str, float],
    ) -> Dict[str, float]:
        """
        Расчет грузоподъемности подшипника.

        Args:
            bearing_type: Тип подшипника
            dimensions: Размеры подшипника

        Returns:
            Характеристики грузоподъемности
        """
        logger.error("Capacity calculation is not implemented yet")
        raise NotImplementedError("Capacity calculation is not implemented yet.")
>>>>>>> main
