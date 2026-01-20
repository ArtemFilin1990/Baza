# Автоматическая распаковка архивов / Automatic Archive Extraction

## Описание / Description

Этот проект содержит скрипт для автоматической распаковки всех архивов в корень проекта.

This project contains a script for automatic extraction of all archives to the project root.

## Использование / Usage

### Автоматическая распаковка / Automatic Extraction

Для распаковки всех архивов в корень проекта выполните:

To extract all archives to the project root, run:

```bash
bash extract_archives.sh
```

или / or:

```bash
./extract_archives.sh
```

### Поддерживаемые форматы / Supported Formats

Скрипт поддерживает следующие форматы архивов:

The script supports the following archive formats:

- `.zip` - ZIP архивы
- `.tar` - TAR архивы
- `.tar.gz` - Сжатые TAR архивы
- `.tgz` - Сжатые TAR архивы (альтернативное расширение)

### Что делает скрипт / What the Script Does

1. Сканирует корневую директорию проекта на наличие архивов
2. Проверяет целостность каждого архива
3. Распаковывает архивы в корень проекта
4. Выводит статистику выполнения
5. Возвращает код ошибки, если не удалось распаковать какие-либо архивы

---

1. Scans the project root directory for archives
2. Checks the integrity of each archive
3. Extracts archives to the project root
4. Displays execution statistics
5. Returns an error code if any archives failed to extract

### Пример вывода / Example Output

```
==================================================
Распаковка архивов в корень проекта
Extracting archives to project root
==================================================

Обработка / Processing: Материалы.zip
✓ Успешно распакован / Successfully extracted: Материалы.zip

Обработка / Processing: Каталоги.zip
✓ Успешно распакован / Successfully extracted: Каталоги.zip

==================================================
Итоги / Summary:
==================================================
Всего архивов / Total archives: 4
Успешно распакованоsuccessfully extracted: 4
==================================================
```

## Требования / Requirements

- `unzip` - для распаковки ZIP архивов / for extracting ZIP archives
- `tar` - для распаковки TAR архивов / for extracting TAR archives

На большинстве Linux систем эти утилиты уже установлены.

On most Linux systems, these utilities are already installed.

## Примечания / Notes

- Скрипт перезаписывает существующие файлы при распаковке (опция `-o` для unzip)
- Все архивы распаковываются в корень проекта
- Скрипт выводит цветные сообщения для удобства чтения

---

- The script overwrites existing files during extraction (`-o` option for unzip)
- All archives are extracted to the project root
- The script outputs colored messages for better readability
