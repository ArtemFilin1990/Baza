# NSK Global bearing catalog (offline snapshot)

## Purpose
Фиксировать офлайн-слепки каталога NSK без размещения внешних ссылок.

## Classification
- Интерактивный/онлайн каталог производителя.
- Используется для валидации ISO-типоразмеров и обозначений.

## Designation
- `SNAP_SRC_NSK_GLOBAL` — текстовый/CSV экспорт ключевых разделов каталога.

## Related NSK Documents
В репозитории доступны следующие документы NSK:

1. **Карманный справочник по техническому обслуживанию подшипников NSK**
   - Метаданные: `sources/vendor_catalogs/nsk_maintenance_guide.md`
   - Файл: `sources/catalogs/Karmannyy-spravochnik-po-tekhnicheskomu-obsluzhivaniyu-podshipnikov-ot-NSk.pdf`
   - Содержание: Практическое руководство по установке, эксплуатации и обслуживанию

2. **Каталог инструментов для монтажа подшипников NSK**
   - Метаданные: `sources/vendor_catalogs/nsk_tools_catalog.md`
   - Файл: `sources/catalogs/Katalog-instrumentov-dlya-montazha-podshipnikov-NSK.pdf`
   - Содержание: Специализированный инструмент для монтажа и демонтажа

3. **Обозначения подшипников NSK**
   - Метаданные: `sources/vendor_catalogs/nsk_designations.md`
   - Файл: `sources/catalogs/Oboznacheniya-podshipnikov-NSK.pdf`
   - Содержание: Система обозначений и маркировки NSK

## Prefixes/Suffixes
- Префикс `SNAP_SRC_` — офлайн-слепок.
- Суффикс `_GLOBAL` — глобальный каталог.

## Examples
- Сохранить таблицу размеров (d/D/B) для серии 6200 и приложить контрольную сумму файла.

## Notes & Limitations
- Прямой онлайн-доступ недоступен (403), требуется офлайн-выгрузка.
- Указывать дату и версию каталога при каждом обновлении данных.
- Для практического применения используйте локальные PDF-документы NSK.

## Standard References
- Домен источника: nsk.com (глобальный каталог подшипников).
- Локальные файлы: этот `.md` + любые выгрузки таблиц в той же директории + PDF-документы в `sources/catalogs/`.
