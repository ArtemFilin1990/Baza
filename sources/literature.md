# Источники и литература

## Стандарты ГОСТ

### Основные
- **ГОСТ 520-2002** — Подшипники качения. Общие технические условия
- **ГОСТ 3478-2012** — Основные нормы взаимозаменяемости. Подшипники качения. Обозначения
- **ГОСТ 24810-2013** — Подшипники качения. Внутренняя конструкция

### Допуски и посадки
- **ГОСТ 520-89** — Подшипники качения. Классы точности
- **ГОСТ 24853-81** — Подшипники качения. Посадки

## Стандарты ISO

- **ISO 15** — Rolling bearings — Radial bearings – Boundary dimensions
- **ISO 355** — Rolling bearings – Tapered roller bearings – Boundary dimensions
- **ISO 492** — Rolling bearings – Radial bearings – Geometrical product specifications
- **ISO 76** — Rolling bearings – Static load ratings

## Стандарты DIN

- **DIN 625** — Rolling bearings – Deep groove ball bearings
- **DIN 628** — Rolling bearings – Single row cylindrical roller bearings

## Каталоги производителей

### SKF
- SKF General Catalogue (2023)
- URL: https://www.skf.com/group/products/rolling-bearings

### FAG (Schaeffler)
- FAG Rolling Bearings Catalogue (2022)
- URL: https://www.schaeffler.com/en/products-and-solutions/industrial/

### NSK
- NSK Ball & Roller Bearings Catalogue (2023)
- URL: https://www.nskeurope.com/en/products/bearings.html

### NTN
- NTN Ball Bearing Catalogue (2022)
- URL: https://www.ntn.com/en/products/catalog/

### Timken
- Timken Bearing Catalogue (2023)
- URL: https://www.timken.com/products/bearings/

## Справочная литература

1. **Дунаев П. Ф., Леликов О.П.** — Конструирование узлов и деталей машин. М.: Академия, 2009
2. **Орлов П.И.** — Основы конструирования. Справочно-методическое пособие. М.: Машиностроение, 1988
3. **Анурьев В.И.** — Справочник конструктора-машиностроителя. М.: Машиностроение, 2001

## Онлайн-ресурсы

### Стандарты и нормативная документация
- [ГОСТ стандарты (docs.cntd.ru)](http://docs.cntd.ru/)
- [ISO стандарты (iso.org)](https://www.iso.org/standards.html)
- [Bearing Designation System Guide (medias.schaeffler.com)](https://medias.schaeffler.com/)

### Онлайн базы данных подшипников (использованы для наполнения репозитория)

**Справочные каталоги с размерными таблицами:**
- [podshipnik.info](https://podshipnik.info/catalog/katalog-podshipnikov-gost) — каталог подшипников ГОСТ
- [irbis.ua](https://www.irbis.ua/ru/production/podshipniki-optom/razmery-podshipnikov) — таблица размеров (2600+ типоразмеров)
- [kugellager-express.de](https://www.kugellager-express.de/Online-catalogue-of-roller-bearings) — международный каталог
- [2rs.com.ua](https://2rs.com.ua/ru/select-bearings/) — подбор по размерам d/D/B
- [podshipnikon.ru](https://podshipnikon.ru/razmeri-podshipnikov) — таблицы размеров

**Таблицы соответствий ISO ↔ ГОСТ:**
- [planetapodshipnik.ru](https://planetapodshipnik.ru/news/post/tablica-markirovki-podshipnikov-iso-i-gost) — таблица маркировки ISO и ГОСТ

**Официальные каталоги производителей:**
- [SKF Rolling Bearings PDF](https://www.skf.com/binaries/pub12/Images/0901d196802809de-Rolling-bearings---17000_1-EN_tcm_12-121486.pdf)
- [NTN Bearing Finder](https://bearingfinder.ntnamericas.com/) — интерактивный каталог с CAD
- [NSK Global](https://www.nsk.com/)
- [Timken Tapered Roller Bearing Catalog](https://www.timken.com/wp-content/uploads/2016/10/Timken-Tapered-Roller-Bearing-Catalog.pdf)
- [Sacom.lt Bearings Catalogs](https://sacom.lt/bearings-catalogs) — коллекция PDF каталогов

## Структурированные данные в репозитории

На основе вышеперечисленных источников в репозитории созданы следующие файлы с данными:

### JSON файлы с техническими характеристиками

**Радиальные шариковые подшипники (37 шт.):**
- **bearing_dimensions_6000_series.json** - серия 6000 (11 подшипников) - источники: SKF, NSK, podshipnik.info
- **bearing_dimensions_6200_series.json** - серия 6200 (13 подшипников) - источники: SKF, NSK, IRBIS
- **bearing_dimensions_6300_series.json** - серия 6300 (13 подшипников) - источники: SKF, NSK, каталог

**Роликовые подшипники (48 шт.):**
- **bearing_dimensions_cylindrical_rollers.json** - цилиндрические NU 200/300 (15 подшипников) - источники: SKF, NSK, веб-поиск
- **bearing_dimensions_tapered_rollers.json** - конические 30200/30300/32000 (18 подшипников) - источники: Timken, SKF, веб-поиск
- **bearing_dimensions_spherical.json** - сферические 1200/22200/22300 (15 подшипников) - источники: SKF, NSK, FBJ, веб-поиск

**Специальные подшипники (21 шт.):**
- **bearing_dimensions_angular_contact.json** - радиально-упорные 7200 (5 подшипников) - источники: SKF, NSK, каталог
- **bearing_dimensions_thrust.json** - упорные 51100/51200 (16 подшипников) - источники: SKF, NSK, веб-поиск

**Справочные данные:**
- **gost_iso_correspondence.json** - соответствия ГОСТ ↔ ISO (26 записей) - источники: planetapodshipnik.ru, podshipnik.info, Timken
- **aprom_brands.json** - база брендов производителей - источник: aprom.by

**Всего: 106 подшипников с полными техническими характеристиками**

Подробное описание структуры данных см. в [README.md](README.md)

---

**Правило**: Все данные в репозитории должны иметь ссылку на один из источников выше.