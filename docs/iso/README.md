# ISO база данных (машиночитаемая)

## Ссылки на данные
- `data/iso/bearings.csv` — базовые обозначения и расшифровка примеров (6205, 30205, 7205 BECBP, NU 305 E C3, 22215 CCK/W33).
- `data/iso/dimensions.csv` — размеры d/D/B для типовых ISO-кодов.
- `data/iso/prefixes.csv` — префиксы (N, NU, NJ, NUP, AH/AHX/AOHX, HM/HML/HMV и др.) из `ISO/префиксы.md`.
- `data/iso/suffixes.csv` — суффиксы производителей (NSK/NTN/KOYO/SKF) и общие коды точности и смазки.

## Структура обозначения
1. `[Префикс] [Основное обозначение] [Суффиксы]`
2. Внутренний диаметр: 00/01/02/03 → 10/12/15/17 мм; 04–96 → код × 5 мм; дробные обозначения для <10 мм и ≥500 мм.
3. Серия диаметров/ширины: особо лёгкая 18/19, лёгкая 02/62/63, средняя 03, тяжёлая 04.
4. Частные группы: 72xx/73xx (радиально-упорные), 511xx–513xx (упорные), 30x/32x/33x (конические).

## Использование префиксов/суффиксов
- **Префиксы**: N/NU/NJ/NUP/NH/NF описывают бурты цилиндрических роликов; H/HA/HE/HS/AH/AHX/AOH/AOHX — втулки и гайки HM/HML/HMV.
- **Суффиксы**: VV/DDU/ZZ (NSK), LLU/LLB (NTN), 2RS/2RU (KOYO), W33/VA405/P5 (SKF/ISO). Подробности и эквиваленты — в `data/iso/suffixes.csv`.
- Зазоры и точность кодируются C1–C5, P6/P5/P4/P2; смазка/температура — L, HT, VT, S1–S4, VA-серии.

## Контроль качества
- Уникальные ключи: `designation` в bearings, `(designation, d, D, B)` в dimensions, `code` в prefixes и `(code, manufacturer)` в suffixes.
- Все коды нормализованы в UPPERCASE без пробелов.
- Сортировка фиксирована и проверяется тестами `tests/test_dimensions.py` и `tests/test_suffixes.py`.

## Обновление
```bash
python scripts/update_repo.py --no-report   # перезапись CSV из сырых таблиц
python scripts/validate/run_validations.py  # проверка схем
```
Источники: `sources/iso/Суффиксы ISO.docx`, `sources/iso/Подшипники ISO.pdf`, каталоги SKF/NSK/NTN в `sources/brands` и `sources/skf`.
