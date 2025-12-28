# Offline catalog snapshots

## Purpose
Зафиксировать локальные точки хранения данных, чтобы не зависеть от внешних ссылок при работе с каталогами подшипников и таблицами ГОСТ/ISO.

## Classification
- **Официальные PDF каталоги**: SKF, Timken, архивы sacom.lt.
- **Интерактивные каталоги**: NTN Bearing Finder, NSK Global.
- **Независимые справочники/таблицы**: podshipnik.info, IRBIS, podshipnikon.ru, kugellager-express.de, 2rs.com.ua, planetapodshipnik.ru.

## Designation
- `SNAP_SRC_SKF_PDF` → `sources/vendor_catalogs/skf_rolling_bearings.md` (+ ожидаемый `skf_rolling_bearings.pdf`)
- `SNAP_SRC_TIMKEN_PDF` → `sources/vendor_catalogs/timken_tapered_roller_bearing_catalog.md` (+ ожидаемый PDF)
- `SNAP_SRC_SACOM_ARCHIVE` → `sources/vendor_catalogs/sacom_catalog_index.md`
- `SNAP_SRC_NTN_FINDER` → `sources/vendor_catalogs/ntn_bearing_finder.md`
- `SNAP_SRC_NSK_GLOBAL` → `sources/vendor_catalogs/nsk_catalog_overview.md`
- `SNAP_SRC_PODSHIPNIK_INFO` → `sources/vendor_catalogs/podshipnik_info_snapshot.md`
- `SNAP_SRC_IRBIS_TABLE` → `sources/vendor_catalogs/irbis_table_snapshot.md`
- `SNAP_SRC_KUGELLAGER_EXPRESS` → `sources/vendor_catalogs/kugellager_express_snapshot.md`
- `SNAP_SRC_2RS_SELECTOR` → `sources/vendor_catalogs/2rs_selector_snapshot.md`
- `SNAP_SRC_PODSHIPNIKON_REF` → `sources/vendor_catalogs/podshipnikon_snapshot.md`
- `SNAP_SRC_PLANETA_ISO_GOST` → `sources/vendor_catalogs/planeta_iso_gost_snapshot.md`

## Prefixes/Suffixes
- Префикс `SNAP_SRC_` — идентификатор офлайн-слепка источника.
- Суффикс `_PDF` — ожидаемый бинарный PDF-файл.
- Суффикс `_SNAPSHOT`/`_INDEX`/`_FINDER` — текстовое описание или выгрузка параметров для последующей репликации.

## Examples
- Для SKF: разместить файл `sources/vendor_catalogs/skf_rolling_bearings.pdf` с контрольной суммой и датой скачивания; версия из skf.com (Rolling Bearings, 17000_1-EN). Метаданные фиксировать в `sources/vendor_catalogs/skf_rolling_bearings.md`.
- Для podshipnik.info: сохранить статичную HTML/CSV-выгрузку в `sources/vendor_catalogs/podshipnik_info_snapshot.md` с фиксацией полей d/D/B, обозначения и массы.
- Для NTN Bearing Finder: экспортировать результат поиска (скриншоты/CSV) и описать параметры фильтра в `sources/vendor_catalogs/ntn_bearing_finder.md`.

## Notes & Limitations
- Прямые загрузки через прокси могут блокироваться (наблюдался HTTP 403); в таком случае требуется офлайн-загрузка и ручное добавление файлов в указанные пути.
- Для PDF-файлов фиксировать дату скачивания и контрольную сумму (SHA256) в соответствующем `.md`.
- Файлы должны храниться внутри `sources/vendor_catalogs/` без внешних URL.

## Standard References
- SKF Rolling Bearings (официальный PDF) — метаданные `sources/vendor_catalogs/skf_rolling_bearings.md`, ожидаемый PDF `skf_rolling_bearings.pdf`.
- Timken Tapered Roller Bearing Catalog (официальный PDF) — метаданные `sources/vendor_catalogs/timken_tapered_roller_bearing_catalog.md`, ожидаемый PDF в той же директории.
- NTN Bearing Finder — ожидаемый слепок в `sources/vendor_catalogs/ntn_bearing_finder.md`.
- NSK Global Catalog — ожидаемый слепок в `sources/vendor_catalogs/nsk_catalog_overview.md`.
- podshipnik.info — ожидаемый слепок в `sources/vendor_catalogs/podshipnik_info_snapshot.md`.
- irbis.ua — ожидаемый слепок в `sources/vendor_catalogs/irbis_table_snapshot.md`.
- kugellager-express.de — ожидаемый слепок в `sources/vendor_catalogs/kugellager_express_snapshot.md`.
- 2rs.com.ua — ожидаемый слепок в `sources/vendor_catalogs/2rs_selector_snapshot.md`.
- podshipnikon.ru — ожидаемый слепок в `sources/vendor_catalogs/podshipnikon_snapshot.md`.
- planetapodshipnik.ru — ожидаемый слепок в `sources/vendor_catalogs/planeta_iso_gost_snapshot.md`.
- sacom.lt архив — ожидаемый индекс в `sources/vendor_catalogs/sacom_catalog_index.md`.
