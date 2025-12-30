# SOURCES — размещение исходников

## Категории
- `sources/gost/` — ГОСТ стандарты и учебные материалы (meta: `sources/gost/meta.yaml`)
- `sources/iso/` — материалы по системе ISO и суффиксам (meta: `sources/iso/meta.yaml`)
- `sources/analogs/` — документ с таблицей аналогов ГОСТ ↔ ISO (meta: `sources/analogs/meta.yaml`)
- `sources/brands/` — каталоги производителей (NSK/NTN/FAG/INA/Schaeffler и др.) (meta: `sources/brands/meta.yaml`)
- `sources/skf/` — каталоги SKF (meta: `sources/skf/meta.yaml`)

## Проверка статусов
- Каждый `meta.yaml` содержит статус `unverified`/`verified`. При добавлении нового источника обновляйте статус и цель (`purpose`).
- Источники из корня и `tests/` перенесены в соответствующие подпапки `sources/`.

## Как использовать
1. Добавьте новый PDF/DOCX в нужный каталог `sources/<category>/`.
2. Обновите `meta.yaml` (название файла, purpose, status).
3. Запустите `python scripts/update_repo.py` для пересборки CSV.
4. Зафиксируйте изменения вместе с новым отчётом в `data/reports/`.
