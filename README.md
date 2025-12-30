# Baza — машиночитаемая база подшипников ГОСТ/ISO

## Что внутри
- **Источники:** все PDF/DOCX лежат в `sources/` и каталогизированы по стандартам (`gost`, `iso`, `analogs`, `brands`, `skf`) с метаданными `meta.yaml`.
- **Данные:** нормализованные CSV в `data/` (`gost`, `iso`, `analogs`, `brands`) плюс отчёты `data/reports/YYYY-MM-DD_source.json`.
- **Схемы и проверки:** описания таблиц в `schemas/*.yaml`, валидаторы в `scripts/validate/`, тесты в `tests/`.
- **Документация:** обзорные файлы в `docs/` (по разделам ГОСТ/ISO/аналогам/брендам) без полноразмерных таблиц.

## Быстрый старт
```bash
python -m pip install -r requirements.txt
python scripts/update_repo.py --no-report     # нормализация CSV из сырых таблиц
python scripts/validate/run_validations.py    # проверка по схемам
python -m pytest -q                           # регрессионные тесты
```

## Где искать данные
- ГОСТ: `data/gost/bearings.csv`, `data/gost/dimensions.csv`, `data/gost/series.csv`, `data/gost/tolerances.csv`
- ISO: `data/iso/bearings.csv`, `data/iso/dimensions.csv`, `data/iso/prefixes.csv`, `data/iso/suffixes.csv`
- Аналоги: `data/analogs/gost_iso.csv`, `data/analogs/units.csv`, `data/analogs/housings.csv`
- Бренды: `data/brands/brands.csv`
- Индекс и правила: `INDEX.md`, `RULES.md`, `SOURCES.md`

## Обновление и контроль качества
- Единственный способ обновить CSV — `scripts/update_repo.py`; ручные правки строк запрещены.
- Уникальные ключи контролируются схемами: `(gost, iso)` для аналогов, `(code, manufacturer)` для суффиксов, `(designation, d, D, B)` для размеров.
- Формат: запятая как разделитель, числа с точкой, пустые значения — пустые строки, сортировка фиксирована и проверяется тестами.
- Любые новые данные сопровождаются отчётом в `data/reports/` с перечислением входных источников и статистикой строк.

## Документы-навигация
- `INDEX.md` — «пульт управления» по CSV, документации и источникам.
- `SOURCES.md` — краткий список ключевых PDF/DOCX и их размещение.
- `RULES.md` — требования к достоверности, форматам и процессу обновления.

## Лицензия и вклад
- Лицензия: MIT (`LICENSE`).
- Вклад и код-стайл: см. `CONTRIBUTING.md`; коммиты в формате «Add/Update/Fix …».
