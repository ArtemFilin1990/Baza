"""
Тесты для экспорта результатов
"""
import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.api import app

client = TestClient(app)


def test_export_json():
    """Тест экспорта в JSON"""
    response = client.get("/search/export?q=6205&format=json")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    
    # Проверяем, что это валидный JSON
    data = response.json()
    assert isinstance(data, list)


def test_export_csv():
    """Тест экспорта в CSV"""
    response = client.get("/search/export?q=6205&format=csv")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
    assert "Content-Disposition" in response.headers
    assert "attachment" in response.headers["Content-Disposition"]
    
    # Проверяем, что контент это текст
    assert len(response.content) > 0


def test_export_xlsx():
    """Тест экспорта в XLSX"""
    response = client.get("/search/export?q=6205&format=xlsx")
    assert response.status_code == 200
    assert "spreadsheet" in response.headers["content-type"]
    assert "Content-Disposition" in response.headers
    
    # Проверяем, что контент не пустой
    assert len(response.content) > 0


def test_export_invalid_format():
    """Тест с невалидным форматом"""
    response = client.get("/search/export?q=6205&format=invalid")
    assert response.status_code == 422  # Validation error


def test_export_with_limit():
    """Тест экспорта с ограничением количества результатов"""
    limit = 10
    response = client.get(f"/search/export?q=подшипник&format=json&limit={limit}")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) <= limit


def test_export_analogs_json():
    """Тест экспорта аналогов в JSON"""
    bearing_code = "6205"
    response = client.get(f"/analogs/{bearing_code}/export?format=json")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    
    data = response.json()
    assert isinstance(data, list)


def test_export_analogs_csv():
    """Тест экспорта аналогов в CSV"""
    bearing_code = "6205"
    response = client.get(f"/analogs/{bearing_code}/export?format=csv")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]


def test_export_analogs_xlsx():
    """Тест экспорта аналогов в XLSX"""
    bearing_code = "6205"
    response = client.get(f"/analogs/{bearing_code}/export?format=xlsx")
    assert response.status_code == 200
    assert "spreadsheet" in response.headers["content-type"]


def test_batch_export_json():
    """Тест массового экспорта в JSON"""
    queries = ["6205", "6305"]
    
    response = client.post(
        "/export/batch?format=json",
        json=queries
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Проверяем, что есть результаты для каждого запроса
    for query in queries:
        assert query in data


def test_batch_export_xlsx():
    """Тест массового экспорта в XLSX"""
    queries = ["6205", "6305"]
    
    response = client.post(
        "/export/batch?format=xlsx",
        json=queries
    )
    
    assert response.status_code == 200
    assert "spreadsheet" in response.headers["content-type"]
    assert len(response.content) > 0


def test_batch_export_empty_queries():
    """Тест массового экспорта с пустым списком"""
    response = client.post(
        "/export/batch?format=json",
        json=[]
    )
    
    assert response.status_code == 400  # Bad request


def test_export_filename_in_headers():
    """Тест наличия имени файла в заголовках"""
    response = client.get("/search/export?q=test&format=csv")
    assert response.status_code == 200
    
    content_disposition = response.headers.get("Content-Disposition", "")
    assert "filename=" in content_disposition


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
