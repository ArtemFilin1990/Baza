# Каталоги производителей (PDF)

Эта директория содержит локальные копии официальных каталогов производителей подшипников в формате PDF. Все файлы доступны офлайн без необходимости подключения к интернету.

## Структура каталогов

### SKF (Швеция)

#### Obshchii_-katalog-podshipnikov-SKF.pdf (20 MB)
- **SHA256:** `03eedc232dff7e7223e9647c04c3ab6976b7ff2d8a7b98a417037bd9096003e3`
- **Описание:** Общий каталог подшипников качения SKF
- **Содержание:** 
  - Все типы подшипников (шариковые, роликовые, игольчатые)
  - Технические характеристики и размеры
  - Системы обозначений ISO/SKF
  - Грузоподъемность и предельные обороты
- **Метаданные:** [sources/vendor_catalogs/skf_rolling_bearings.md](../vendor_catalogs/skf_rolling_bearings.md)

#### Igolchatye-podshipniki-SKF.pdf (6.5 MB)
- **SHA256:** `e2c40dba6eb7eb5d52c0c6d516d8fbedd52a0c38db49aa090c20a64eddcd1457`
- **Описание:** Специализированный каталог игольчатых подшипников
- **Содержание:**
  - Игольчатые радиальные подшипники
  - Подшипники с сепаратором и без внутреннего кольца
  - Области применения в компактных узлах
- **Метаданные:** [sources/vendor_catalogs/skf_needle_bearings.md](../vendor_catalogs/skf_needle_bearings.md)

#### Katalog-Besshponochnye-Vtulki-FX-SKF.pdf (1.3 MB)
- **SHA256:** `4445c0b2148df787e1197771d4dd7de197b9696c3f9a69fd604fc9fc53343536`
- **Описание:** Бесшпоночные втулки серии FX для крепления
- **Содержание:**
  - Принцип работы бесшпоночных соединений
  - Технические характеристики и размеры
  - Инструкции по монтажу
- **Метаданные:** [sources/vendor_catalogs/skf_keyless_bushings.md](../vendor_catalogs/skf_keyless_bushings.md)

#### Katalog-Silovye-Privodnye-Remni-SKF.pdf (7.2 MB)
- **SHA256:** `eb0aa42213d01d08af7eb583d568c44a6e39e1f944343117b30970f67d330832`
- **Описание:** Каталог силовых приводных ремней
- **Содержание:**
  - Клиновые, поликлиновые и зубчатые ремни
  - Методы подбора по мощности
  - Шкивы и натяжители
- **Метаданные:** [sources/vendor_catalogs/skf_power_transmission.md](../vendor_catalogs/skf_power_transmission.md)

### NSK (Япония)

#### Karmannyy-spravochnik-po-tekhnicheskomu-obsluzhivaniyu-podshipnikov-ot-NSk.pdf (3.2 MB)
- **SHA256:** `5edc26f22bff6199b4556d7a0080b0aa89ff1cabfbd9d30b5568a67ba8f7233c`
- **Описание:** Карманный справочник по техническому обслуживанию
- **Содержание:**
  - Правила установки (холодный и горячий монтаж)
  - Рекомендации по смазке
  - Диагностика неисправностей
  - Расчет ресурса
- **Метаданные:** [sources/vendor_catalogs/nsk_maintenance_guide.md](../vendor_catalogs/nsk_maintenance_guide.md)

#### Katalog-instrumentov-dlya-montazha-podshipnikov-NSK.pdf (3.3 MB)
- **SHA256:** `5f1b4c32e395bf86bf39c240063c1ba73bcb86df6c948c7b27cb07779c136bf5`
- **Описание:** Каталог инструментов для монтажа и демонтажа
- **Содержание:**
  - Механические и гидравлические съемники
  - Индукционные нагреватели
  - Монтажные оправки и приспособления
- **Метаданные:** [sources/vendor_catalogs/nsk_tools_catalog.md](../vendor_catalogs/nsk_tools_catalog.md)

#### Oboznacheniya-podshipnikov-NSK.pdf (1014 KB)
- **SHA256:** `f4ffcd93d224a246ebb0f815f1012725123737b1063644f02ba97c5a3ca3d4cb`
- **Описание:** Система обозначений и маркировки NSK
- **Содержание:**
  - Структура обозначений NSK
  - Префиксы и суффиксы
  - Соответствие NSK ↔ ISO ↔ ГОСТ
  - Примеры расшифровки
- **Метаданные:** [sources/vendor_catalogs/nsk_designations.md](../vendor_catalogs/nsk_designations.md)

### Schaeffler (Германия)

#### Induktsionnye_nagrevateli_podshipnikov_Schaeffler_HEATER.pdf (2.1 MB)
- **SHA256:** `cdcf6d38107d49bab2b5f507bab529b9be2461a7fbd84de30a9602e20905611f`
- **Описание:** Индукционные нагреватели для термического монтажа
- **Содержание:**
  - Принцип работы индукционного нагрева
  - Модельный ряд HEATER
  - Технические характеристики
  - Инструкции по эксплуатации
- **Метаданные:** [sources/vendor_catalogs/schaeffler_heaters.md](../vendor_catalogs/schaeffler_heaters.md)

## Проверка целостности файлов

Для проверки целостности PDF-файлов используйте контрольные суммы SHA256:

```bash
cd sources/catalogs
sha256sum *.pdf
```

Сравните выходные данные с контрольными суммами, указанными выше.

## Использование

Все PDF-файлы можно открыть в любом современном просмотрщике PDF. Рекомендуется:
- Adobe Acrobat Reader
- Foxit Reader
- Sumatra PDF (Windows)
- Evince (Linux)
- Preview (macOS)
- Браузеры с встроенным просмотром PDF

## Лицензия и авторские права

Все каталоги являются собственностью соответствующих производителей:
- SKF © SKF Group
- NSK © NSK Ltd.
- Schaeffler © Schaeffler AG

Файлы предоставлены исключительно в справочных целях и для обучения. Для коммерческого использования обратитесь к официальным дистрибьюторам.

## Обновления

При получении новых версий каталогов:
1. Сохраните новый PDF в эту директорию
2. Вычислите SHA256 контрольную сумму
3. Обновите метаданные в `sources/vendor_catalogs/`
4. Обновите `sources/literature.md`
5. Обновите этот README.md

## Связанные документы

- [sources/literature.md](../literature.md) — полный список источников и литературы
- [sources/vendor_catalogs/](../vendor_catalogs/) — метаданные каталогов
- [README.md](../../README.md) — главная страница базы знаний
