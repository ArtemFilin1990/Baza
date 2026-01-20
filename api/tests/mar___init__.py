"""
Тесты для API.

Проверяют базовые healthcheck/endpoints и функционал поиска.
"""

from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_root() -> None:
    """Root endpoint должен возвращать статус и версию."""
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ready" or "message" in payload
    assert "version" in payload or "message" in payload


def test_health() -> None:
    """Health endpoint должен возвращать ok статус."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
