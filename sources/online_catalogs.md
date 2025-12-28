# Онлайн каталоги и параметрические источники

## Purpose
Собрать проверенные онлайн-источники для верификации размеров подшипников, подборов по параметрам и поиска аналогов ГОСТ/ISO. Используются только каталоги производителей и инженерные справочники; приоритет — официальные данные.

## Classification
- **Официальные каталоги производителей**: SKF (PDF-справочник), NTN (Bearing Finder), NSK (глобальный каталог), Timken (конические роликовые подшипники), Sacom (архив PDF каталожных выпусков разных брендов).
- **Независимые каталоги и таблицы ГОСТ/ISO**: podshipnik.info (ГОСТ-таблицы), IRBIS (табличный каталог 2600+ типоразмеров), podshipnikon.ru (размерные справочники и поиск по диапазонам), planetapodshipnik.ru (таблица соответствий ISO↔ГОСТ).
- **Параметрические онлайн-поиски**: kugellager-express.de (международный каталог с фильтрами по d/D/B), 2rs.com.ua (подбор по d/D/B и типу подшипника).

## Designation
Идентификаторы источников для ссылок в базе:
- `SRC_SKF_PDF` — SKF Rolling Bearings PDF (официальный каталог).
- `SRC_NTN_FINDER` — NTN Bearing Finder (поиск + CAD).
- `SRC_NSK_GLOBAL` — NSK Global Bearing Catalog.
- `SRC_TIMKEN_PDF` — Timken Tapered Roller Bearing Catalog (PDF/online).
- `SRC_SACOM_PDF` — sacom.lt архив PDF-каталогов производителей.
- `SRC_PODSHIPNIK_INFO` — podshipnik.info каталог ГОСТ-подшипников.
- `SRC_IRBIS_TABLE` — irbis.ua таблица размеров подшипников.
- `SRC_KUGELLAGER_EXPRESS` — kugellager-express.de онлайн-каталог роликовых и шариковых подшипников.
- `SRC_2RS_SELECTOR` — 2rs.com.ua подбор подшипников по размерам.
- `SRC_PODSHIPNIKON_REF` — podshipnikon.ru размерные таблицы и поиск по диапазонам.
- `SRC_PLANETA_ISO_GOST` — planetapodshipnik.ru таблица маркировки ISO↔ГОСТ.

## Prefixes/Suffixes
- Префикс `SRC_` используется для ссылочных идентификаторов источников, чтобы отличать их от обозначений подшипников.
- Суффиксы `PDF`, `FINDER`, `TABLE`, `SELECTOR`, `REF` фиксируют формат/тип доступа (статический PDF, интерактивный поиск, табличный справочник).
- При интеграции данных из источников допускаются поля `d`, `D`, `B` (мм), `designation` (ISO/ГОСТ), `standard` (`ISO`/`ГОСТ`), `source_id` (одно из перечисленных идентификаторов).

## Examples
- Проверка типоразмера: брать обозначение (например, ISO **6204** = тип 6, серия 02, код отверстия 04 → 20 мм по ISO 15) → сверять граничные размеры по `SRC_SKF_PDF` и подтверждать совпадение в `SRC_PODSHIPNIK_INFO` или `SRC_KUGELLAGER_EXPRESS` через фильтр d/D/B.
- Подбор аналога ГОСТ↔ISO: использовать таблицу соответствий `SRC_PLANETA_ISO_GOST`, затем валидировать размеры через `SRC_IRBIS_TABLE` и любой официальный PDF (SKF/Timken/NSK/NTN).
- Кросс-проверка поставщика: при подборе по размерам в `SRC_2RS_SELECTOR` сверять обозначение и геометрию с `SRC_PODSHIPNIKON_REF`, чтобы исключить локальные маркетинговые индексы.

## Notes & Limitations
- Доступ к перечисленным сайтам может требовать интерактивной загрузки; при недоступности (HTTP 403/блокировка) следует выгружать каталоги офлайн и сохранять локальные копии в `sources/`.
- Всегда отдавать приоритет официальным каталогам производителей; независимые таблицы использовать только для быстрого поиска и дополнительной проверки.
- При импорте данных фиксировать дату скачивания и версию каталога (для PDF) в метаданных таблицы.

## Standard References
- podshipnik.info — каталог ГОСТ-подшипников (размеры, масса, маркировки); офлайн копия фиксируется в `sources/vendor_catalogs/podshipnik_info_snapshot.md` (см. `SNAP_SRC_PODSHIPNIK_INFO`).
- irbis.ua — таблица размеров подшипников (2600+ типоразмеров); офлайн копия фиксируется в `sources/vendor_catalogs/irbis_table_snapshot.md`.
- kugellager-express.de — международный онлайн-каталог роликовых/шариковых подшипников; офлайн копия фиксируется в `sources/vendor_catalogs/kugellager_express_snapshot.md`.
- 2rs.com.ua — подбор подшипника по d/D/B; офлайн копия фиксируется в `sources/vendor_catalogs/2rs_selector_snapshot.md`.
- podshipnikon.ru — размерные таблицы и поиск по диапазонам; офлайн копия фиксируется в `sources/vendor_catalogs/podshipnikon_snapshot.md`.
- planetapodshipnik.ru — таблица маркировки ISO и ГОСТ; офлайн копия фиксируется в `sources/vendor_catalogs/planeta_iso_gost_snapshot.md`.
- SKF Rolling Bearings — офлайн слепок в `sources/vendor_catalogs/skf_rolling_bearings.md` (+ ожидаемый PDF `skf_rolling_bearings.pdf`).
- NTN Bearing Finder — офлайн слепок в `sources/vendor_catalogs/ntn_bearing_finder.md`.
- NSK Global Catalog — офлайн слепок в `sources/vendor_catalogs/nsk_catalog_overview.md`.
- Timken Tapered Roller Bearing Catalog — офлайн слепок в `sources/vendor_catalogs/timken_tapered_roller_bearing_catalog.md` (+ ожидаемый PDF).
- sacom.lt архив PDF — индекс слепков в `sources/vendor_catalogs/sacom_catalog_index.md`.
