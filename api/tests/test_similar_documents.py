"""
Тесты для похожих документов
"""
import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.api import app

client = TestClient(app)


def test_similar_documents():
    """Тест получения похожих документов"""
    # Сначала получаем ID документа через поиск
    search_response = client.get("/search?q=подшипник&limit=1")
    assert search_response.status_code == 200
    
    search_data = search_response.json()
    if search_data['results']:
        doc_id = search_data['results'][0]['id']
        
        # Получаем похожие документы
        response = client.get(f"/similar/{doc_id}")
        assert response.status_code in [200, 404]  # 404 если нет похожих
        
        if response.status_code == 200:
            data = response.json()
            assert 'similar' in data
            assert len(data['similar']) <= 5  # По умолчанию максимум 5


def test_similar_documents_with_limit():
    """Тест с ограничением количества похожих документов"""
    # Используем фиксированный ID для теста
    doc_id = "doc_0"
    limit = 3
    
    response = client.get(f"/similar/{doc_id}?limit={limit}")
    
    if response.status_code == 200:
        data = response.json()
        assert len(data['similar']) <= limit


def test_similar_documents_not_found():
    """Тест для несуществующего документа"""
    response = client.get("/similar/nonexistent_doc_id")
    assert response.status_code == 404


def test_search_with_similar_included():
    """Тест поиска с включением похожих документов"""
    response = client.get("/search?q=подшипник&include_similar=true&limit=3")
    assert response.status_code == 200
    
    data = response.json()
    
    # Проверяем, что похожие документы включены в результаты
    for result in data['results']:
        assert 'similar_documents' in result
        # similar_documents может быть пустым списком, если нет похожих


def test_search_without_similar():
    """Тест поиска без похожих документов"""
    response = client.get("/search?q=подшипник&include_similar=false&limit=3")
    assert response.status_code == 200
    
    data = response.json()
    
    # Похожие документы не должны быть включены
    for result in data['results']:
        # Ключ может быть, но список должен быть пустым, или ключа не должно быть
        if 'similar_documents' in result:
            assert result['similar_documents'] == []


def test_similar_documents_structure():
    """Тест структуры ответа похожих документов"""
    doc_id = "doc_0"
    
    response = client.get(f"/similar/{doc_id}")
    
    if response.status_code == 200:
        data = response.json()
        assert 'document_id' in data
        assert 'similar' in data
        assert 'count' in data
        
        for sim_doc in data['similar']:
            assert 'id' in sim_doc
            assert 'title' in sim_doc
            assert 'path' in sim_doc
            assert 'similarity' in sim_doc
            assert 0 <= sim_doc['similarity'] <= 1  # Схожесть должна быть от 0 до 1


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
