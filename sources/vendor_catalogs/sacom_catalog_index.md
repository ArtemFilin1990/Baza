# Sacom bearing catalogs archive (offline snapshot)

## Purpose
Зафиксировать доступ к архиву PDF-каталогов sacom.lt без внешних ссылок.

## Classification
- Архив PDF каталогов разных производителей.
- Используется как резервный источник PDF при блокировке прямых сайтов.

## Designation
- `SNAP_SRC_SACOM_ARCHIVE` — индекс и контрольные суммы скачанных PDF.

## Prefixes/Suffixes
- Префикс `SNAP_SRC_` — идентификатор слепка.
- Суффикс `_ARCHIVE` — агрегированный набор PDF.

## Examples
- При скачивании файлов добавлять список имен и SHA256 в этот файл.

## Notes & Limitations
- Скачивание напрямую недоступно из-за 403, требуется офлайн загрузка.
- Хранить PDF в `sources/vendor_catalogs/` рядом с этим файлом.

## Standard References
- Домен источника: sacom.lt/bearings-catalogs (архив).
- Локальные файлы: индекс в этом файле + соответствующие PDF после ручной загрузки.
