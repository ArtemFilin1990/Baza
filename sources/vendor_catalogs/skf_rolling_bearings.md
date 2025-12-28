# SKF Rolling Bearings (offline snapshot)

## Purpose
Описание локального хранения официального каталога SKF Rolling Bearings без использования внешних ссылок.

## Classification
- Официальный PDF каталог производителя.
- Основной источник граничных размеров и обозначений ISO.

## Designation
- `SNAP_SRC_SKF_PDF` — файл `skf_rolling_bearings.pdf` (ожидаемый бинарный PDF) + данный `.md` с метаданными.

## Prefixes/Suffixes
- Префикс `SNAP_SRC_` — идентификатор офлайн-слепка.
- Суффикс `_PDF` — указывает на PDF-файл.

## Examples
- При загрузке сохранить `skf_rolling_bearings.pdf` в ту же директорию и зафиксировать контрольную сумму SHA256 в этом файле.

## Notes & Limitations
- Прямая загрузка с домена skf.com через прокси вернула HTTP 403; требуется офлайн-загрузка и ручное добавление файла.
- До появления PDF используйте другие подтверждённые источники для валидации размеров.

## Standard References
- Домен источника: skf.com (Rolling Bearings catalogue, номер 17000_1-EN).
- Локальные файлы: `skf_rolling_bearings.pdf` (нет в репозитории), `skf_rolling_bearings.md` (этот файл).
