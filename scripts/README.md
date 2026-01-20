# Скрипты управления

Скрипты для управления и обслуживания репозитория.

---

## Структура

```
scripts/
├── manage.py              # Основной скрипт управления (из Baza)
└── README.md             # Этот файл
```

Также доступны:
- `api/scripts/import_to_postgres.py` - импорт в PostgreSQL (из bearing-api)
- `api/scripts/unpack_and_classify.py` - обработка файлов (из bearing-api)
- `00_ВСПОМОГАТЕЛЬНЫЕ/extract_archives.sh` - распаковка архивов (из Mar)

---

## manage.py

Основной скрипт управления базой знаний.

### Использование

```bash
python scripts/manage.py <command> [options]
```

### Команды

#### validate
Проверка структуры репозитория
```bash
python scripts/manage.py validate
```

#### report
Генерация отчета о содержимом
```bash
python scripts/manage.py report
```

#### update
Обновление данных
```bash
python scripts/manage.py update
```

#### help
Справка по командам
```bash
python scripts/manage.py help
```

### Опции

- `-v, --verbose` - подробный вывод

---

## Скрипты API

### import_to_postgres.py

Импорт данных из CSV в PostgreSQL.

```bash
python api/scripts/import_to_postgres.py
```

### unpack_and_classify.py

Обработка входящих файлов из `data/inbox/`.

```bash
python api/scripts/unpack_and_classify.py
```

---

## Shell скрипты

### extract_archives.sh

Распаковка архивов из Mar.

```bash
bash 00_ВСПОМОГАТЕЛЬНЫЕ/extract_archives.sh
```

---

## Зависимости

Python скрипты требуют:
- Python 3.8+
- Зависимости из `api/requirements.txt`

Установка:
```bash
pip install -r api/requirements.txt
```

---

## Автоматизация

Скрипты могут быть запущены через:
- GitHub Actions workflows
- Cron jobs
- Вручную

---

## Источники

- `manage.py` - из Baza
- `import_to_postgres.py`, `unpack_and_classify.py` - из bearing-api
- `extract_archives.sh` - из Mar

---

*Последнее обновление: 2026-01-19*
