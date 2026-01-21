# INDEX — навигация по базе

> **Последнее обновление:** 21 января 2026 г.

## 📚 Система энциклопедии (НОВОЕ!)

**Дата запуска:** 2026-01-21 — Структурированная система создания энциклопедических статей с обязательными таблицами ГОСТ ⇄ ISO

### Быстрая навигация
- 🚀 **[Быстрый старт](ENCYCLOPEDIA_QUICK_START.md)** — начните здесь!
- 📖 **[Индекс энциклопедии](ENCYCLOPEDIA_INDEX.md)** — главный навигатор по 14 разделам
- 🗺️ **[Roadmap](ROADMAP_ENCYCLOPEDIA.md)** — план развития, 60+ тем
- 📝 **[Шаблон статьи](_template-article.md)** — готовый шаблон (12 разделов)
- 📋 **[Руководство создания](PROMPT_ENCYCLOPEDIA_ASSISTANT.md)** — полное руководство
- 🔧 **[Детали реализации](ENCYCLOPEDIA_IMPLEMENTATION.md)** — технические детали

### Особенности системы
- ✅ Строгая трассируемость к файлам репозитория
- ✅ Обязательные таблицы ГОСТ ⇄ ISO в каждой статье
- ✅ Единая 12-секционная структура
- ✅ Запрет внешних источников
- ✅ Прозрачное указание недостающих данных

---

## Источники данных

📊 [**DATA_SOURCES.md**](DATA_SOURCES.md) - Полный обзор всех источников данных, статистика и рекомендации по расширению базы (43,000+ записей)

## Данные (CSV)
### ГОСТ
- [`data/gost/bearings.csv`](data/gost/bearings.csv) - Подшипники ГОСТ
- [`data/gost/dimensions.csv`](data/gost/dimensions.csv) - Размеры
- [`data/gost/series.csv`](data/gost/series.csv) - Серии
- [`data/gost/tolerances.csv`](data/gost/tolerances.csv) - Допуски

### ISO
- [`data/iso/bearings.csv`](data/iso/bearings.csv) - Подшипники ISO
- [`data/iso/dimensions.csv`](data/iso/dimensions.csv) - Размеры
- [`data/iso/prefixes.csv`](data/iso/prefixes.csv) - Префиксы
- [`data/iso/suffixes.csv`](data/iso/suffixes.csv) - Суффиксы

### Аналоги
- [`data/analogs/gost_iso.csv`](data/analogs/gost_iso.csv) - Таблица соответствий ГОСТ ↔ ISO
- [`data/analogs/units.csv`](data/analogs/units.csv) - Подшипниковые узлы
- [`data/analogs/housings.csv`](data/analogs/housings.csv) - Корпуса

### Бренды
- [`data/brands/brands.csv`](data/brands/brands.csv) - База производителей и брендов

### Отчёты
- [`data/reports/`](data/reports/) - Автоматически генерируемые отчёты об обновлениях

## Документация
### Основная документация
- Подшипники: [`docs/bearings/`](docs/bearings/) - Справочники, руководства, классификация
- Статьи: [`docs/articles/`](docs/articles/) - База знаний (122 статьи)
- Навигация: [`docs/NAVIGATION_GUIDE.md`](docs/NAVIGATION_GUIDE.md) - Полная навигация по репозиторию
- Индекс знаний: [`docs/EXTRACTED_KNOWLEDGE_INDEX.md`](docs/EXTRACTED_KNOWLEDGE_INDEX.md)

### Создание статей
- Промт: [`PROMPT_ARTICLE_CREATION.md`](PROMPT_ARTICLE_CREATION.md) - Полный промт для создания статей
- Руководство: [`docs/ARTICLE_CREATION_GUIDE.md`](docs/ARTICLE_CREATION_GUIDE.md) - Подробная инструкция
- Краткая памятка: [`docs/QUICK_REFERENCE.md`](docs/QUICK_REFERENCE.md) - Быстрый старт
- Примеры: [`docs/examples/`](docs/examples/) - Образцы готовых статей

### Специализированные промпты
- Энциклопедический ассистент: [`PROMPT_ENCYCLOPEDIA_ASSISTANT.md`](PROMPT_ENCYCLOPEDIA_ASSISTANT.md) - ГОСТ ⇄ ISO справочник с обязательными таблицами соответствий
- Google Ads: [`PROMPT_GOOGLE_ADS_COPYWRITER.md`](PROMPT_GOOGLE_ADS_COPYWRITER.md) - Создание рекламных заголовков для Google Ads
- SARD SRS: [`PROMPT_SARD_SRS.md`](PROMPT_SARD_SRS.md) - Генерация технических заданий (ТЗ) и SRS по методике SARD

### Стандарты и спецификации
- ГОСТ: [`docs/gost/`](docs/gost/) - Стандарты ГОСТ
- ISO: [`docs/iso/`](docs/iso/) - Стандарты ISO
- Аналоги: [`docs/analogs/`](docs/analogs/) - Таблицы аналогов
- Бренды: [`docs/brands/`](docs/brands/) - Информация о производителях

### Английская версия
- [`docs/en/`](docs/en/) - English documentation (in development)

## Источники
- Индекс источников: [`SOURCES.md`](SOURCES.md)
- Структура источников: [`sources/README.md`](sources/README.md)
- Метаданные: `sources/*/meta.yaml` (GOST, ISO, analogs, brands, SKF)
- Каталоги: `sources/gost/`, `sources/iso/`, `sources/analogs/`, `sources/brands/`, `sources/skf/`
- Извлечение данных: [`sources/pdf_text_extractor.py`](sources/pdf_text_extractor.py)
- Парсер таблиц: [`sources/table_scraper.py`](sources/table_scraper.py)

## Схемы данных
- ГОСТ: [`schemas/gost.yaml`](schemas/gost.yaml)
- ISO: [`schemas/iso.yaml`](schemas/iso.yaml)
- Аналоги: [`schemas/analogs.yaml`](schemas/analogs.yaml)
- Бренды: [`schemas/brands.yaml`](schemas/brands.yaml)

## Скрипты и проверки
### Обработка данных
- Нормализация: [`scripts/update_repo.py`](scripts/update_repo.py)
- Извлечение: [`scripts/extract/raw_datasets.py`](scripts/extract/raw_datasets.py)
- Валидация: [`scripts/validate/run_validations.py`](scripts/validate/run_validations.py)
- CSV валидатор: [`scripts/validate/csv_validator.py`](scripts/validate/csv_validator.py)

### Тесты
- Тесты: [`tests/`](tests/)
- Схемы: [`tests/test_schemas.py`](tests/test_schemas.py)
- Размеры: [`tests/test_dimensions.py`](tests/test_dimensions.py)
- Суффиксы: [`tests/test_suffixes.py`](tests/test_suffixes.py)
- Скрейпер: [`tests/test_table_scraper.py`](tests/test_table_scraper.py)

### CI/CD
- GitHub Actions: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

## Правила и процессы
- Форматы и допуски: [`RULES.md`](RULES.md)
- История изменений: [`CHANGELOG.md`](CHANGELOG.md)
- Руководство по вкладу: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Лицензия: [`LICENSE`](LICENSE)
- Агент GitHub: [`AGENT.md`](AGENT.md)
- README (русский): [`README.md`](README.md)
- README (English): [`README_en.md`](README_en.md)
