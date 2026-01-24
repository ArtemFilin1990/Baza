# Руководство по миграции

Документация по объединению трех репозиториев в один.

*Дата миграции: 2026-01-19*

---

## Обзор миграции

### Исходные репозитории

1. **ArtemFilin1990/Mar** (текущий, Shell)
   - Справочная база знаний: 1,804+ файла
   - 13 разделов документации
   - Структура сохранена полностью

2. **ArtemFilin1990/Baza** (Python 98.1%)
   - Учебник-справочник: 122 статьи
   - CSV данные: 43,000+ записей
   - Python-скрипты обработки

3. **ArtemFilin1990/bearing-api** (Python 99.1%)
   - FastAPI приложение
   - PostgreSQL интеграция
   - Docker-контейнеризация

### Результат

Единый репозиторий **ArtemFilin1990/Mar** с:
- Полной справочной базой (сохранена)
- Учебными материалами (добавлено из Baza)
- API сервисом (добавлено из bearing-api)
- Структурированными данными (объединено)

---

## Структура нового репозитория

```
Mar/
├── 02_Термины_и_основы/              # [Mar] Сохранено
├── 03_ГОСТ_подшипники_и_нормативка/  # [Mar] Сохранено
├── 04_ISO_и_международные_обозначения/ # [Mar] Сохранено
├── 05_Маркировка_суффиксы_серии/     # [Mar] Сохранено
├── 06_Аналоги_и_взаимозаменяемость/  # [Mar] Сохранено
├── 07_Бренды_и_каталоги/             # [Mar] Сохранено
├── 08_Автомобильные_комплекты/       # [Mar] Сохранено
├── 09_Линейные_системы_и_передачи/   # [Mar] Сохранено
├── 10_Ремни_шкивы_цепи/              # [Mar] Сохранено
├── 11_РТИ_рукава_уплотнения/         # [Mar] Сохранено
├── 12_Прочее_сопутствующее/          # [Mar] Сохранено
├── 90_Приложения_таблицы_БД/         # [Mar] Сохранено
├── 99_IT_документация/               # [Mar] Сохранено
├── Подшипники/                       # [Mar] Сохранено
├── 00_ВСПОМОГАТЕЛЬНЫЕ/               # [Mar] Сохранено
│
├── knowledge-base/                   # [Baza] НОВОЕ
│   ├── part-i/                      # Основы и теория
│   ├── part-ii/                     # Типы подшипников
│   ├── part-iii/                    # Стандарты
│   ├── part-iv/                     # Сопутствующие
│   ├── appendix/                    # Приложения
│   ├── Учебник/                     # Практический курс
│   ├── Учебник_Академический/       # Академический курс
│   ├── Вводный_курс_для_новичков/   # Базовый курс
│   ├── Практические_руководства/    # Руководства
│   ├── Инструменты_и_справочники/   # Инструменты
│   ├── Карты_знаний_и_навигация/    # Навигация
│   ├── Каталоги/                    # Каталоги
│   ├── Изображения/                 # Изображения
│   ├── Тесты/                       # Тесты
│   ├── номенклатура/                # Номенклатура
│   └── docs/                        # Документация
│
├── api/                             # [bearing-api] НОВОЕ
│   ├── app/                         # FastAPI приложение
│   ├── scripts/                     # Скрипты импорта
│   ├── sql/                         # SQL скрипты
│   ├── tests/                       # Тесты
│   ├── main.py                      # Точка входа
│   ├── requirements.txt             # Зависимости
│   └── Dockerfile                   # Docker образ
│
├── data/                            # [Baza + bearing-api] НОВОЕ
│   ├── inbox/                       # Входящие файлы
│   ├── csv/                         # CSV данные
│   │   ├── gost/                   # Данные ГОСТ
│   │   ├── iso/                    # Данные ISO
│   │   ├── analogs/                # Аналоги
│   │   ├── brands/                 # Производители
│   │   └── reports/                # Отчеты
│   ├── schemas/                     # JSON схемы
│   └── sources/                     # Исходные данные
│
├── scripts/                         # [Baza] НОВОЕ
│   └── manage.py                    # Скрипт управления
│
├── docs-legacy/                     # НОВОЕ
│   ├── README-mar.md               # Старый README Mar
│   ├── README-baza.md              # Описание Baza
│   └── README-api.md               # Описание bearing-api
│
├── .github/workflows/               # Обновлено
│   ├── auto-extract-archives.yml   # [Mar] Сохранено
│   ├── data_pipeline.yml           # [bearing-api] Новое
│   ├── ci.yml                      # [Baza] Новое
│   └── security.yml                # [Baza] Новое
│
├── .gitignore                       # НОВОЕ (объединенный)
├── Dockerfile                       # НОВОЕ
├── docker-compose.yml               # НОВОЕ
├── README.md                        # Обновлено
└── MIGRATION_GUIDE.md              # Этот файл
```

---

## Что где находится теперь

### Из Mar (сохранено)

| Было | Сейчас | Статус |
|------|--------|--------|
| Все разделы 02-12, 90, 99 | Те же директории | ✅ Сохранено |
| README.md | README.md (обновлен) + docs-legacy/README-mar.md | ✅ Сохранено |
| extract_archives.sh | 00_ВСПОМОГАТЕЛЬНЫЕ/extract_archives.sh | ✅ Сохранено |
| .github/workflows/ | .github/workflows/ | ✅ Дополнено |

### Из Baza (добавлено)

| Было (в Baza) | Сейчас (в Mar) | Примечания |
|---------------|----------------|------------|
| part-i/ | knowledge-base/part-i/ | Перемещено |
| part-ii/ | knowledge-base/part-ii/ | Перемещено |
| part-iii/ | knowledge-base/part-iii/ | Перемещено |
| part-iv/ | knowledge-base/part-iv/ | Перемещено |
| appendix/ | knowledge-base/appendix/ | Перемещено |
| Учебник/ | knowledge-base/Учебник/ | Перемещено |
| data/ | data/csv/ | Реорганизовано |
| schemas/ | data/schemas/ | Перемещено |
| sources/ | data/sources/ | Перемещено |
| manage.py | scripts/manage.py | Перемещено |
| docs/ | knowledge-base/docs/ | Перемещено |

### Из bearing-api (добавлено)

| Было (в bearing-api) | Сейчас (в Mar) | Примечания |
|----------------------|----------------|------------|
| app/ | api/app/ | Перемещено |
| scripts/ | api/scripts/ | Перемещено |
| sql/ | api/sql/ | Перемещено |
| tests/ | api/tests/ | Перемещено |
| main.py | api/main.py | Перемещено |
| requirements.txt | api/requirements.txt | Перемещено |
| Dockerfile | api/Dockerfile | Скопировано |
| data/inbox/ | data/inbox/ | Перемещено |

---

## Изменения в путях

### Для разработчиков

#### Импорты Python

**Было (в Baza):**
```python
from manage import validate_structure
```

**Теперь:**
```python
# Из корня репозитория
from scripts.manage import validate_structure
```

**Было (в bearing-api):**
```python
from app.models import Bearing
```

**Теперь:**
```python
# Из api/ директории
from app.models import Bearing
```

#### Пути к данным

**Было (в Baza):**
```python
df = pd.read_csv('data/gost/bearings.csv')
```

**Теперь:**
```python
df = pd.read_csv('data/csv/gost/bearings.csv')
```

#### Команды запуска

**Было (в bearing-api):**
```bash
python main.py
```

**Теперь:**
```bash
cd api
python main.py
# или из корня:
python api/main.py
```

---

## Использование объединенного репозитория

### Для изучения

```bash
# Начните со справочной базы (Mar)
cd 02_Термины_и_основы/

# Изучайте учебник (Baza)
cd knowledge-base/Вводный_курс_для_новичков/

# Используйте практический курс
cd knowledge-base/Учебник/
```

### Для разработки

```bash
# Установите зависимости
pip install -r api/requirements.txt

# Запустите API
cd api
python main.py

# Обработайте данные
python scripts/manage.py validate
```

### С Docker

```bash
# Запустите весь стек
docker-compose up -d

# API доступен на http://localhost:8000
# PostgreSQL на порту 5432
# pgAdmin на http://localhost:5050 (профиль admin)
```

---

## Обратная совместимость

### Что не изменилось

✅ Все пути в существующих разделах Mar (02-12, 90, 99)
✅ Структура файлов в Подшипники/
✅ MANIFEST.csv и навигационные файлы
✅ Существующие скрипты в 00_ВСПОМОГАТЕЛЬНЫЕ/

### Что может потребовать обновления

⚠️ Абсолютные пути к новым директориям
⚠️ Импорты Python модулей
⚠️ Конфигурационные файлы с путями
⚠️ Скрипты CI/CD (обновлены)

---

## Переменные окружения

Создайте файл `.env` в корне:

```env
# PostgreSQL
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=bearings
POSTGRES_USER=bearing_user

# API
DATABASE_URL=postgresql://bearing_user:your_secure_password@localhost:5432/bearings
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=False

# pgAdmin (опционально)
PGADMIN_PASSWORD=admin_password
```

---

## GitHub Actions

### Новые workflows

1. **data_pipeline.yml** - обработка данных
   - Из bearing-api
   - Автоматическая обработка inbox/
   - Валидация структуры

2. **ci.yml** - непрерывная интеграция
   - Из Baza
   - Тестирование Python кода
   - Линтинг и форматирование

3. **security.yml** - проверки безопасности
   - Из Baza
   - Сканирование зависимостей
   - Проверка уязвимостей

### Сохраненные workflows

- **auto-extract-archives.yml** - из Mar

---

## FAQ

### Q: Где теперь учебные материалы из Baza?
**A:** В директории `knowledge-base/`

### Q: Как запустить API?
**A:** `cd api && python main.py` или через Docker

### Q: Сохранилась ли структура Mar?
**A:** Да, полностью. Все разделы 02-12, 90, 99 на месте.

### Q: Где CSV данные?
**A:** В `data/csv/` с подразделами gost/, iso/, analogs/, brands/

### Q: Как обновить данные?
**A:** Положите файлы в `data/inbox/` и запустите `python api/scripts/unpack_and_classify.py`

### Q: Нужно ли переписывать существующий код?
**A:** Нет для Mar. Да для импортов из Baza и bearing-api (обновите пути).

---

## Контакты и поддержка

- **Issues**: https://github.com/ArtemFilin1990/Mar/issues
- **Документация**: README.md
- **Legacy docs**: docs-legacy/

---

## История изменений

### 2026-01-19 - Объединение репозиториев
- ✅ Добавлена структура knowledge-base/ из Baza
- ✅ Добавлен API из bearing-api
- ✅ Объединены данные в data/
- ✅ Добавлены workflows CI/CD
- ✅ Создана Docker-инфраструктура
- ✅ Сохранена вся структура Mar

---

*Документ создан: 2026-01-19*
*Версия: 1.0*
