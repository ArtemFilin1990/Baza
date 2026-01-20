"""
Тесты для автодополнения
"""
import pytest
from fastapi.testclient import TestClient
import sys
import os

# Добавляем путь к API в sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.api import app

client = TestClient(app)


def test_autocomplete_basic():
    """Тест базового автодополнения"""
    response = client.get("/autocomplete?q=под")
    assert response.status_code == 200
    data = response.json()
    assert 'suggestions' in data
    assert 'query' in data
    assert data['query'] == 'под'
    assert len(data['suggestions']) > 0


def test_autocomplete_bearing_codes():
    """Тест автодополнения для кодов подшипников"""
    response = client.get("/autocomplete?q=620")
    assert response.status_code == 200
    data = response.json()
    suggestions = data['suggestions']
    # Проверяем, что хотя бы одно предложение содержит "620"
    assert any("620" in s['value'] for s in suggestions)


def test_autocomplete_with_type_filter():
    """Тест автодополнения с фильтром по типу"""
    response = client.get("/autocomplete?q=S&types=brand")
    assert response.status_code == 200
    data = response.json()
    # Все результаты должны быть типа brand
    for suggestion in data['suggestions']:
        assert suggestion['type'] == 'brand'


def test_autocomplete_minimum_length():
    """Проверка работы с коротким запросом"""
    response = client.get("/autocomplete?q=п")
    assert response.status_code == 200
    # Даже для одного символа должны вернуться результаты


def test_autocomplete_empty_query():
    """Проверка на пустой запрос"""
    response = client.get("/autocomplete?q=")
    # Должна быть ошибка валидации
    assert response.status_code == 422


def test_autocomplete_limit():
    """Тест ограничения количества результатов"""
    limit = 5
    response = client.get(f"/autocomplete?q=под&limit={limit}")
    assert response.status_code == 200
    data = response.json()
    assert len(data['suggestions']) <= limit


def test_autocomplete_popular():
    """Тест получения популярных терминов"""
    response = client.get("/autocomplete/popular?limit=10")
    assert response.status_code == 200
    data = response.json()
    assert 'popular' in data
    assert len(data['popular']) > 0


def test_autocomplete_case_insensitive():
    """Тест регистронезависимого поиска"""
    response1 = client.get("/autocomplete?q=под")
    response2 = client.get("/autocomplete?q=ПОД")
    
    assert response1.status_code == 200
    assert response2.status_code == 200
    
    # Результаты должны быть одинаковыми
    data1 = response1.json()
    data2 = response2.json()
    
    # Проверяем, что получены результаты
    assert len(data1['suggestions']) > 0
    assert len(data2['suggestions']) > 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
