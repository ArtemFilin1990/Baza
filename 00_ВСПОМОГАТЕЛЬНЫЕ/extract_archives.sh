#!/bin/bash

# Скрипт для автоматической распаковки всех архивов в корень проекта

# Цвета для вывода
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Получаем директорию скрипта
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "=================================================="
echo "Распаковка архивов в корень проекта"
echo "=================================================="
echo ""

# Счетчики
total=0
success=0
failed=0

# Проверяем наличие утилит распаковки
if ! command -v unzip &> /dev/null; then
    echo -e "${RED}Ошибка: утилита unzip не найдена${NC}"
    exit 1
fi

# Ищем все архивы в корне проекта
cd "$SCRIPT_DIR"

# Обрабатываем ZIP архивы
for archive in *.zip; do
    if [ -f "$archive" ]; then
        total=$((total + 1))
        echo -e "${YELLOW}Обработка: $archive${NC}"
        
        # Проверяем содержимое архива
        if unzip -t "$archive" > /dev/null 2>&1; then
            # Распаковываем архив в корень проекта
            if unzip -o "$archive" -d "$SCRIPT_DIR"; then
                echo -e "${GREEN}✓ Успешно распакован: $archive${NC}"
                success=$((success + 1))
            else
                echo -e "${RED}✗ Ошибка при распаковке: $archive${NC}"
                failed=$((failed + 1))
            fi
        else
            echo -e "${RED}✗ Поврежденный архив: $archive${NC}"
            failed=$((failed + 1))
        fi
        echo ""
    fi
done

# Обрабатываем TAR.GZ архивы
for archive in *.tar.gz *.tgz; do
    if [ -f "$archive" ]; then
        total=$((total + 1))
        echo -e "${YELLOW}Обработка: $archive${NC}"
        
        if tar -tzf "$archive" > /dev/null 2>&1; then
            if tar -xzf "$archive" -C "$SCRIPT_DIR"; then
                echo -e "${GREEN}✓ Успешно распакован: $archive${NC}"
                success=$((success + 1))
            else
                echo -e "${RED}✗ Ошибка при распаковке: $archive${NC}"
                failed=$((failed + 1))
            fi
        else
            echo -e "${RED}✗ Поврежденный архив: $archive${NC}"
            failed=$((failed + 1))
        fi
        echo ""
    fi
done

# Обрабатываем TAR архивы
for archive in *.tar; do
    if [ -f "$archive" ]; then
        total=$((total + 1))
        echo -e "${YELLOW}Обработка: $archive${NC}"
        
        if tar -tf "$archive" > /dev/null 2>&1; then
            if tar -xf "$archive" -C "$SCRIPT_DIR"; then
                echo -e "${GREEN}✓ Успешно распакован: $archive${NC}"
                success=$((success + 1))
            else
                echo -e "${RED}✗ Ошибка при распаковке: $archive${NC}"
                failed=$((failed + 1))
            fi
        else
            echo -e "${RED}✗ Поврежденный архив: $archive${NC}"
            failed=$((failed + 1))
        fi
        echo ""
    fi
done

# Выводим итоговую статистику
echo "=================================================="
echo "Итоги:"
echo "=================================================="
echo "Всего архивов: $total"
echo -e "${GREEN}Успешно распаковано: $success${NC}"
if [ $failed -gt 0 ]; then
    echo -e "${RED}Не удалось распаковать: $failed${NC}"
fi
echo "=================================================="

# Возвращаем код выхода
if [ $failed -gt 0 ]; then
    exit 1
else
    exit 0
fi
