"""
API endpoints для работы с подшипниками.

Определяет REST API endpoints для:
- Поиска подшипников
- Получения информации о подшипниках
- Работы с аналогами
- Доступа к справочным данным
"""

import io
import json
import re
from datetime import datetime

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse, StreamingResponse

from .export_utils import AnalogsExporter, SearchResultsExporter
from .logic import AutocompleteEngine, DocumentSearchEngine, SearchHistory


def _sanitize_filename(text: str, max_length: int = 50) -> str:
    """Sanitize text for safe use in filenames"""
    # Remove or replace filesystem-sensitive characters
    sanitized = re.sub(r'[<>:"/\\|?*]', "_", text)
    # Remove leading/trailing whitespace and dots
    sanitized = sanitized.strip(". ")
    # Limit length
    return sanitized[:max_length] if sanitized else "export"


# Инициализация приложения
app = FastAPI(
    title="Справочник подшипников - API поиска",
    description="API для поиска подшипников с автодополнением, похожими документами, историей и экспортом",
    version="1.0.0",
)

# Инициализация движков
autocomplete_engine = AutocompleteEngine()
search_engine = DocumentSearchEngine()
search_history = SearchHistory()


@app.get("/")
async def root():
    """Корневой endpoint"""
    return {
        "message": "API справочника подшипников",
        "version": "1.0.0",
        "endpoints": {
            "autocomplete": "/autocomplete",
            "search": "/search",
            "similar": "/similar/{document_id}",
            "history": "/history",
            "export": "/search/export",
        },
    }


@app.get("/autocomplete")
async def autocomplete(
    q: str = Query(..., min_length=1, description="Префикс для поиска (минимум 1 символ)"),
    limit: int = Query(10, ge=1, le=50, description="Количество предложений"),
    types: list[str] | None = Query(None, description="Типы: term, bearing_code, brand, series"),
):
    """
    Автодополнение поисковых запросов

    Примеры:
    - /autocomplete?q=под → ["подшипник", "подшипники качения", "подшипниковые узлы"]
    - /autocomplete?q=620 → ["6205", "6206", "6207", "6208"]
    - /autocomplete?q=SK → ["SKF", "SKF Y-типа"]

    Возвращает:
    {
      "query": "под",
      "suggestions": [
        {
          "value": "подшипник",
          "type": "term",
          "frequency": 1240,
          "highlight": "<b>под</b>шипник"
        }
      ]
    }
    """
    suggestions = autocomplete_engine.suggest(q, limit=limit, types=types)

    return {"query": q, "suggestions": suggestions, "count": len(suggestions)}


@app.get("/autocomplete/popular")
async def get_popular_autocomplete(limit: int = Query(10, ge=1, le=50, description="Количество результатов")):
    """Получить самые популярные термины для автодополнения"""
    popular = autocomplete_engine.get_popular_searches(limit=limit)

    return {"popular": popular, "count": len(popular)}


@app.get("/search")
async def search(
    q: str = Query(..., min_length=1, description="Поисковый запрос"),
    include_similar: bool = Query(True, description="Добавить похожие документы"),
    limit: int = Query(20, ge=1, le=100, description="Количество результатов"),
    user_id: str | None = Query(None, description="Токен пользователя (опционально)"),
    session_id: str | None = Query(None, description="ID сессии"),
):
    """
    Поиск документов

    Возвращает:
    {
      "total": 45,
      "results": [
        {
          "id": "doc_123",
          "title": "Подшипник 6205",
          "path": "...",
          "excerpt": "...",
          "relevance": 0.95,
          "similar_documents": [
            {
              "id": "doc_456",
              "title": "Подшипник 6206",
              "similarity": 0.85
            }
          ]
        }
      ]
    }
    """
    # Выполнить поиск
    results = search_engine.search(q, limit=limit)

    # Добавить похожие документы
    if include_similar:
        for result in results:
            similar_docs = search_engine.get_similar_documents(result["id"], limit=3)
            result["similar_documents"] = similar_docs

    # Сохранить в историю
    if user_id:
        search_history.add_search(user_id, q, len(results), session_id)

    return {"query": q, "total": len(results), "results": results}


@app.get("/similar/{document_id}")
async def get_similar_documents(
    document_id: str, limit: int = Query(5, ge=1, le=20, description="Количество похожих документов")
):
    """
    Получить похожие документы для конкретного документа

    Пример: /similar/doc_123

    Возвращает список документов отсортированных по схожести
    """
    similar = search_engine.get_similar_documents(document_id, limit=limit)

    if not similar:
        raise HTTPException(status_code=404, detail="Документ не найден или нет похожих документов")

    return {"document_id": document_id, "similar": similar, "count": len(similar)}


@app.get("/history")
async def get_search_history(
    user_id: str = Query(..., description="ID пользователя"),
    limit: int = Query(50, ge=1, le=200, description="Количество записей"),
):
    """
    Получить историю поиска пользователя

    Возвращает:
    {
      "history": [
        {
          "query": "подшипник 6205",
          "timestamp": "2026-01-19T12:00:00Z",
          "results_count": 45
        }
      ]
    }
    """
    history = search_history.get_user_history(user_id, limit=limit)

    return {"user_id": user_id, "history": history, "count": len(history)}


@app.delete("/history")
async def clear_search_history(user_id: str = Query(..., description="ID пользователя")):
    """Очистить историю поиска"""
    search_history.clear_user_history(user_id)

    return {"message": f"История пользователя {user_id} очищена", "status": "success"}


@app.get("/history/popular")
async def get_popular_queries(limit: int = Query(10, ge=1, le=50, description="Количество запросов")):
    """
    Получить самые популярные поисковые запросы (без привязки к пользователю)

    Используется для:
    - Показа популярных запросов на главной странице
    - Улучшения автодополнения
    - Аналитики
    """
    popular = search_history.get_popular_queries(limit=limit)

    return {"popular": popular, "count": len(popular)}


@app.get("/analytics/search")
async def get_search_analytics(period: str = Query("7d", regex="^(1d|7d|30d)$", description="Период: 1d, 7d, 30d")):
    """
    Аналитика поисковых запросов

    Возвращает:
    {
      "total_searches": 1240,
      "unique_queries": 456,
      "top_queries": [...],
      "zero_results_queries": [],
      "avg_results_per_query": 12.5
    }
    """
    # Заглушка для аналитики
    # В реальной системе здесь должна быть работа с БД

    return {
        "period": period,
        "total_searches": len(search_history.history),
        "unique_queries": len(set(h["query"] for h in search_history.history)),
        "top_queries": search_history.get_popular_queries(limit=10),
        "zero_results_queries": [],
        "avg_results_per_query": 0,
    }


@app.get("/search/export")
async def export_search_results(
    q: str = Query(..., description="Поисковый запрос"),
    export_format: str = Query("json", regex="^(json|csv|xlsx)$", description="Формат: json, csv, xlsx"),
    limit: int = Query(100, ge=1, le=1000, description="Количество результатов"),
):
    """
    Экспорт результатов поиска

    Примеры:
    - /search/export?q=подшипник&export_format=json
    - /search/export?q=6205&export_format=csv
    - /search/export?q=SKF&export_format=xlsx

    Возвращает файл для скачивания
    """
    # Выполняем поиск
    results = search_engine.search(q, limit=limit)

    # Sanitize query for filename
    safe_query = _sanitize_filename(q, max_length=20)

    if export_format == "json":
        json_data = SearchResultsExporter.to_json(results, pretty=True)
        return JSONResponse(content=json.loads(json_data))

    elif export_format == "csv":
        csv_data = SearchResultsExporter.to_csv(results)
        return StreamingResponse(
            io.BytesIO(csv_data.encode("utf-8-sig")),  # BOM для корректного отображения в Excel
            media_type="text/csv; charset=utf-8",
            headers={"Content-Disposition": f"attachment; filename=search_results_{safe_query}.csv"},
        )

    elif export_format == "xlsx":
        excel_data = SearchResultsExporter.to_excel(results)
        if excel_data is None:
            raise HTTPException(status_code=500, detail="Ошибка при создании Excel файла")

        return StreamingResponse(
            excel_data,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename=search_results_{safe_query}.xlsx"},
        )


@app.get("/analogs/{bearing_code}/export")
async def export_analogs(
    bearing_code: str,
    export_format: str = Query("json", regex="^(json|csv|xlsx)$", description="Формат: json, csv, xlsx"),
):
    """
    Экспорт списка аналогов

    Форматы:
    - JSON: структурированный объект
    - CSV: таблица с колонками [code, standard, manufacturer, compatibility]
    - XLSX: Excel файл с форматированием
    """
    # Заглушка для аналогов
    # В реальной системе здесь должна быть работа с БД
    analogs = [
        {
            "code": bearing_code,
            "standard": "ГОСТ",
            "manufacturer": "SKF",
            "compatibility": "100%",
            "notes": "Прямой аналог",
        }
    ]

    # Sanitize bearing_code for filename
    safe_code = _sanitize_filename(bearing_code)

    if export_format == "json":
        return JSONResponse(content=analogs)

    elif export_format == "csv":
        csv_data = AnalogsExporter.to_csv(analogs)
        return StreamingResponse(
            io.BytesIO(csv_data.encode("utf-8-sig")),
            media_type="text/csv; charset=utf-8",
            headers={"Content-Disposition": f"attachment; filename=analogs_{safe_code}.csv"},
        )

    elif export_format == "xlsx":
        excel_data = AnalogsExporter.to_excel(analogs)
        return StreamingResponse(
            excel_data,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename=analogs_{safe_code}.xlsx"},
        )


@app.post("/export/batch")
async def export_batch(
    queries: list[str], export_format: str = Query("xlsx", regex="^(json|xlsx)$", description="Формат: json, xlsx")
):
    """
    Массовый экспорт результатов для списка запросов

    Body:
    {
      "queries": ["6205", "6305", "6405"]
    }

    Создает Excel файл с отдельным листом для каждого запроса
    """
    if not queries:
        raise HTTPException(status_code=400, detail="Список запросов не может быть пустым")

    # Выполняем поиск для каждого запроса
    batch_results = {}
    for query in queries:
        results = search_engine.search(query, limit=50)
        batch_results[query] = results

    if export_format == "json":
        return JSONResponse(content=batch_results)

    elif export_format == "xlsx":
        excel_data = SearchResultsExporter.create_batch_excel(batch_results)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"batch_export_{timestamp}.xlsx"
        return StreamingResponse(
            excel_data,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )


# Обработчик ошибок
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """
    Global exception handler that logs errors server-side and returns
    a generic error message to avoid leaking sensitive information.
    """
    # In production, log the full exception details server-side
    # import logging
    # logging.error(f"Unhandled exception: {exc}", exc_info=True)

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": "An unexpected error occurred. Please contact support if the problem persists.",
        },
    )
