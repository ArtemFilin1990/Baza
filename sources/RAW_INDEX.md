# RAW index of source files

This directory contains raw reference materials used to compile the knowledge base. Each file is kept in its original form and is not intended for direct consumption; please refer to the curated markdown files in the knowledge base for summarized information.

- **аналоги узлов.docx** – Таблицы взаимных соответствий корпусных узлов между различными производителями (NTN, SKF, FAFNIR, INA и др.).
- **АНАЛОГИ.pdf** – Сводные таблицы аналогов подшипников по стандартам ГОСТ и ISO с примерами.
- **БРЭНДЫ.docx** – Материал с классификацией импортных брендов по соотношению цена–качество и обзором рынка.
- **Подшипники ISO.pdf** – Учебное пособие по конструкции и обозначениям подшипников ISO.
- **Подшипники SKF.docx** – Руководство по продукции SKF; содержит классификацию, обозначения и примеры применения.
- **Таблица аналагов.docx** – Дополнительные таблицы аналогов подшипников с примерами соответствия.
- **Суффиксы ISO.docx** – Таблица распространённых суффиксов и префиксов ISO с пояснениями.
- **aprom_brands.json** – JSON-выгрузка (284 записи) с брендами подшипников и сопутствующих товаров с [aprom.by/brands.php](https://aprom.by/brands.php).
- **aprom_table_scraper.py** – CLI-скрипт для выгрузки всех страниц из [aprom.by/table.php](https://aprom.by/table.php) с поддержкой пагинации и таймаутов; используется для построения сырых таблиц (выходной JSON сохраняется в `sources/aprom_table_data.json`).
