# Правила участия в проекте

## Требования к контенту

### Источники данных
Принимаются **только**:
- ГОСТ (с номером и годом)
- ISO (с номером)
- DIN (с номером)
- Каталоги производителей (с указанием бренда и года)

### Запрещено
- ❌ Данные без источника
- ❌ «Приблизительные» значения
- ❌ Смешивание стандартов в одном файле
- ❌ Упрощённая маркировка

## Структура файлов

Каждый технический файл должен содержать:

```markdown
# [Название стандарта/типа]

## Назначение
[Для чего используется]

## Классификация
[Типы, группы, серии]

## Маркировка
[Структура обозначения по стандарту]

### Префиксы и суффиксы
[Расшифровка дополнительных символов]

## Примеры
### Пример 1: 6205-2RS
- **6** — тип (шариковый радиальный однорядный)
- **2** — серия диаметров (лёгкая)
- **05** — внутренний диаметр d = 05 × 5 = 25 мм
- **2RS** — суффикс (уплотнения с двух сторон)

**Источник**: ГОСТ 3478-2012, стр. 14

## Примечания
[Ограничения, особенности применения]

## Ссылки
- ГОСТ XXXX-YYYY
- ISO ZZZZ
- [Каталог производителя](URL)
```

## Структура репозитория

```
/
├── docs/bearings/
│   ├── designations/       # Системы обозначений ГОСТ и ISO
│   ├── analogues/          # Таблицы соответствия ГОСТ ↔ ISO
│   ├── brands/             # Информация о производителях
│   ├── standards/          # Стандарты и нормативы
│   ├── classification/     # Классификация подшипников
│   ├── catalog/            # Каталог подшипников
│   ├── faq/                # Часто задаваемые вопросы
│   └── training/           # Обучающие материалы
└── sources/                # Литература, каталоги, стандарты
```

### Правила размещения
- **docs/bearings/designations/** — файлы с маркировкой по ГОСТ и ISO
- **docs/bearings/analogues/** — таблицы эквивалентности с проверкой размеров
- **docs/bearings/brands/** — информация о производителях и брендах
- **docs/bearings/standards/** — стандарты ГОСТ и ISO
- **sources/** — PDF-ы, ссылки, библиография

## Процесс добавления данных

1. **Создать ветку**
   ```bash
   git checkout -b add-gost-6205
   ```

2. **Добавить файл** в правильную папку

3. **Следовать шаблону** (см. выше)

4. **Указать источник** для каждого факта

5. **Создать PR** с описанием: 
   ```
   Add GOST 6205 ball bearing classification
   
   - Added designation structure
   - Included suffix table
   - Verified examples against GOST 3478-2012
   ```

6. **Пройти автопроверку**
   - Структура файла
   - Наличие источников
   - Корректность маркировки

## Использование шаблонов

Репозиторий предоставляет стандартные шаблоны в `.github/templates/`:

### Для стандартов и спецификаций
```bash
cp .github/templates/bearing_standard_template.md docs/bearings/standards/new_standard.md
```

### Для таблиц аналогов
```bash
cp .github/templates/analogue_table_template.md docs/bearings/analogues/new_table.md
```

### Для информации о производителях
```bash
cp .github/templates/brand_info_template.md docs/bearings/brands/new_brand.md
```

Заполните шаблон, заменив все `[Placeholder]` на фактические данные.

## Коммиты

### Формат
```
<Action> <Object>

Examples:
- Add GOST 6205 bearing specification
- Fix ISO suffix table formatting
- Update analog table for 62-series
- Remove duplicate GOST entry
```

### Правила
- Одно действие = один коммит
- Технический язык
- Ссылка на стандарт в описании (если применимо)

## Таблицы аналогов

### Требования
- ✅ Совпадение внутреннего диаметра (d)
- ✅ Совпадение наружного диаметра (D)
- ✅ Совпадение ширины (B)
- ✅ Совпадение типа (шариковый/роликовый)
- ✅ Указание источника сопоставления

### Пример
```markdown
| ГОСТ    | ISO      | d   | D   | B   | Источник          |
|---------|----------|-----|-----|-----|-------------------|
| 180205  | 6205     | 25  | 52  | 15  | ГОСТ 3478-2012    |
| 180206  | 6206     | 30  | 62  | 16  | ГОСТ 3478-2012    |
```

## Проверка перед отправкой

- [ ] Файл в правильной папке
- [ ] Использован шаблон
- [ ] Указаны источники для всех данных
- [ ] Примеры расшифрованы полностью
- [ ] Нет смешивания стандартов
- [ ] Коммит-сообщение соответствует формату

## Тестирование и проверка

### Проверка Python-скриптов
```bash
# Проверка синтаксиса
python -m py_compile sources/table_scraper.py

# Запуск unit-тестов
python tests/test_table_scraper.py

# Или с pytest (если установлен)
python -m pytest tests/test_table_scraper.py -v
```

### Проверка JSON-файлов
```bash
# Валидация JSON синтаксиса
python -m json.tool sources/brands.json > /dev/null

# Или для всех JSON файлов
find . -name "*.json" -exec python -m json.tool {} \; > /dev/null
```

### Локальная проверка CI
При наличии GitHub Actions можно локально проверить:
- Структуру репозитория
- Наличие обязательных файлов
- Валидность Python и JSON файлов

См. `.github/workflows/ci.yml` для полного списка проверок.

## Работа с Git

### Рабочий процесс (Git Workflow)

1. **Синхронизация с основной веткой**
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Создание новой ветки**
   ```bash
   git checkout -b feature/add-bearing-data
   ```
   Используйте префиксы:
   - `feature/` - новая функциональность
   - `fix/` - исправление ошибок
   - `docs/` - изменения в документации
   - `data/` - обновление данных

3. **Внесение изменений**
   ```bash
   # Редактируйте файлы
   # Проверьте изменения
   git status
   git diff
   ```

4. **Валидация перед коммитом**
   ```bash
   # Запустите валидацию данных
   python scripts/validate/run_validations.py
   
   # Запустите тесты
   pytest tests/
   ```

5. **Коммит изменений**
   ```bash
   git add data/gost/bearings.csv
   git commit -m "Add bearing 6205 specification from GOST 3478-2012"
   ```

6. **Отправка в удалённый репозиторий**
   ```bash
   git push origin feature/add-bearing-data
   ```

7. **Создание Pull Request**
   - Перейдите на GitHub
   - Нажмите "New Pull Request"
   - Выберите вашу ветку
   - Заполните описание:
     - Что изменено
     - Зачем это нужно
     - Источники данных
     - Результаты тестирования

### Советы по работе с Git

- **Частые коммиты**: делайте коммиты небольшими и логически связанными
- **Описательные сообщения**: пишите понятные commit messages
- **Проверка перед push**: всегда проверяйте изменения локально
- **Синхронизация**: регулярно синхронизируйтесь с main
- **Конфликты**: при конфликтах слияния - разрешайте их аккуратно

### Пример полного цикла

```bash
# 1. Подготовка
git checkout main
git pull origin main
git checkout -b data/update-iso-suffixes

# 2. Изменения
# Редактируем data/iso/suffixes.csv
# Добавляем источник в sources/iso/

# 3. Проверка
python scripts/validate/run_validations.py
pytest tests/test_suffixes.py

# 4. Коммит
git add data/iso/suffixes.csv sources/iso/meta.yaml
git commit -m "Update ISO suffixes from ISO 15:2017

- Added 15 new suffix codes
- Updated descriptions for existing codes
- Source: ISO 15:2017 catalogue"

# 5. Отправка
git push origin data/update-iso-suffixes

# 6. Создание PR на GitHub
```

## CI/CD и автоматические проверки

### Требования к коду

Перед созданием Pull Request убедитесь, что:

1. **Код отформатирован**:
   ```bash
   make format  # Форматирование с black и ruff
   ```

2. **Линтеры пройдены**:
   ```bash
   make lint    # Проверка с ruff, mypy, black
   ```

3. **Тесты проходят**:
   ```bash
   make test    # Запуск всех тестов
   make test-cov  # С coverage
   ```

4. **Данные валидны**:
   ```bash
   make dedup    # Дедупликация nomenclature.csv
   make validate  # Валидация CSV файлов
   ```

### Pre-commit Hooks

После установки dev зависимостей (`make install-dev`):

```bash
pip install -r requirements-dev.txt
pre-commit install
```

Pre-commit hooks автоматически:
- Проверяют trailing whitespace
- Форматируют код с black
- Проверяют с ruff
- Валидируют YAML/JSON
- Запускают дедупликацию
- Валидируют CSV

### GitHub Actions

При создании Pull Request автоматически запускаются проверки:

1. **PR Checks Workflow** (`.github/workflows/pr-checks.yml`):
   - Проверка форматирования (black)
   - Линтинг (ruff)
   - Проверка типов (mypy)
   - Дедупликация nomenclature.csv
   - Валидация CSV
   - Тесты с coverage
   - Комментарий с результатами

2. **CI Workflow** (`.github/workflows/ci.yml`):
   - Тестирование на Python 3.11 и 3.12
   - Нормализация данных
   - Валидация структуры
   - Проверка ссылок в Markdown

3. **Security Workflow** (`.github/workflows/security.yml`):
   - Сканирование зависимостей (pip-audit)
   - Поиск секретов (Gitleaks)
   - CodeQL анализ
   - SBOM генерация

### Стиль кода

Следуйте этим правилам:

- **Python**: PEP 8, line-length=120
- **Форматтер**: black
- **Линтер**: ruff с правилами E, F, I, N, W, UP
- **Типы**: mypy (опционально, но рекомендуется)
- **Тесты**: pytest с минимум 80% coverage

### Commit Messages

Используйте [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

Типы:
- `feat`: новая функциональность
- `fix`: исправление бага
- `docs`: изменения в документации
- `style`: форматирование, без изменения логики
- `refactor`: рефакторинг кода
- `test`: добавление/изменение тестов
- `chore`: обновление зависимостей, настройки CI

Примеры:
```
feat(data): add ISO 15 suffixes from 2017 catalogue
fix(scripts): correct duplicate detection in nomenclature
docs(readme): update installation instructions
ci: add security scanning workflow
```

### Статусы проверок

- ✅ **Passed** - все проверки прошли успешно, PR готов к ревью
- ❌ **Failed** - есть ошибки, требуется исправление
- ⏳ **Running** - проверки выполняются

### Как исправить failing CI

Если CI упал:

1. **Посмотрите логи**
   - Откройте вкладку "Actions" в PR
   - Найдите упавшую проверку
   - Изучите сообщение об ошибке

2. **Исправьте локально**
   ```bash
   # Воспроизведите ошибку
   python scripts/validate/run_validations.py
   
   # Исправьте
   # ...
   
   # Проверьте
   pytest tests/
   ```

3. **Запушьте исправление**
   ```bash
   git add .
   git commit -m "Fix CSV validation errors"
   git push origin feature/your-branch
   ```

CI автоматически перезапустится с новыми изменениями.

#### Частые ошибки CI и их решения

**1. Black formatting failed**
```
Error: Files would be reformatted
```
**Решение:**
```bash
# Убедитесь, что используете ту же версию black, что и CI
pip install black==24.10.0

# Отформатируйте код
black scripts/ sources/ tests/

# Или используйте make
make format
```

**2. Ruff linting errors**
```
Error: Ruff found X issues
```
**Решение:**
```bash
# Автоматическое исправление (где возможно)
ruff check --fix .

# Проверка
make lint
```

**3. Mypy type errors**
```
Error: Incompatible types
```
**Решение:**
```bash
# Добавьте type hints
def process_data(data: dict) -> list[str]:
    ...

# Проверка
mypy scripts/ sources/
```

**4. CSV validation errors**
```
Error: Duplicate keys found
```
**Решение:**
```bash
# Запустите дедупликацию
python scripts/deduplicate_nomenclature.py

# Проверка
python scripts/validate/run_validations.py
```

**5. Test failures**
```
Error: X tests failed
```
**Решение:**
```bash
# Запустите тесты локально с подробным выводом
pytest tests/ -v

# Один конкретный тест
pytest tests/test_deduplication.py::test_name -v
```

### Локальная эмуляция CI

Чтобы проверить все до push:

```bash
# Создайте скрипт local_ci.sh
#!/bin/bash
set -e

echo "Running Python syntax checks..."
find . -name "*.py" -exec python -m py_compile {} \;

echo "Running JSON validation..."
find . -name "*.json" -exec python -m json.tool {} \; > /dev/null

echo "Running CSV validation..."
python scripts/validate/run_validations.py

echo "Running tests..."
pytest tests/ -v

echo "All checks passed!"
```

Запуск:
```bash
chmod +x local_ci.sh
./local_ci.sh
```

## Вопросы

Создать [Issue](../../issues) с тегом `question`.

### Контакты

- **GitHub Issues**: [создать вопрос](../../issues) - основной способ связи
- **Pull Requests**: для предложений по улучшению
- **Email**: support@example.com (для срочных вопросов)

### Процесс ревью Pull Requests

1. **Автоматические проверки** - CI должен пройти успешно
2. **Ревью кода** - проверка логики и стиля
3. **Проверка данных** - валидация источников и корректности
4. **Обсуждение** - комментарии и предложения
5. **Одобрение** - минимум 1 approving review
6. **Мердж** - объединение с main веткой

### Ожидаемое время ревью

- Простые изменения (опечатки, форматирование): 1-2 дня
- Добавление данных: 3-5 дней
- Новая функциональность: 5-10 дней

---

**Важно**: Репозиторий используется для инженерных расчётов. Недостоверные данные могут привести к ошибкам в проектах.