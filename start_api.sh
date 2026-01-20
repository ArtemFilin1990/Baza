#!/bin/bash
# Скрипт для запуска API сервера поиска

echo "=================================================="
echo "Запуск API сервера справочника подшипников"
echo "=================================================="
echo ""

# Проверка Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 не найден. Установите Python 3.8 или выше."
    exit 1
fi

echo "✓ Python найден: $(python3 --version)"

# Проверка виртуального окружения
if [ ! -d "venv" ]; then
    echo ""
    echo "Создание виртуального окружения..."
    python3 -m venv venv
    echo "✓ Виртуальное окружение создано"
fi

# Активация виртуального окружения
echo ""
echo "Активация виртуального окружения..."
source venv/bin/activate || . venv/Scripts/activate

# Установка зависимостей
echo ""
echo "Установка зависимостей..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

echo "✓ Зависимости установлены"

# Проверка наличия данных
if [ ! -f "data/autocomplete_dict.json" ] || [ ! -f "data/document_index.json" ]; then
    echo ""
    echo "=================================================="
    echo "Построение индексов (это может занять несколько минут)..."
    echo "=================================================="
    
    if [ ! -f "data/autocomplete_dict.json" ]; then
        echo ""
        echo "Построение словаря автодополнения..."
        python scripts/build_autocomplete_dict.py
    fi
    
    if [ ! -f "data/document_index.json" ]; then
        echo ""
        echo "Построение индекса документов..."
        python scripts/build_search_index.py
    fi
    
    echo ""
    echo "✓ Индексы построены"
fi

# Запуск сервера
echo ""
echo "=================================================="
echo "Запуск сервера..."
echo "=================================================="
echo ""
echo "API доступно по адресу: http://localhost:8000"
echo "Документация Swagger: http://localhost:8000/docs"
echo ""
echo "Для остановки нажмите Ctrl+C"
echo ""

uvicorn api.app.api:app --reload --host 0.0.0.0 --port 8000
