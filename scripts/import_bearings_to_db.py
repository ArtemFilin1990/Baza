#!/usr/bin/env python3
"""
Скрипт импорта данных справочника подшипников в PostgreSQL
Использование: python import_bearings_to_db.py
"""

import os
import sys
import psycopg2
import pandas as pd
from pathlib import Path

# Настройки подключения к базе данных
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "bearings_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
}

# Путь к каталогу с данными
DATA_DIR = Path(__file__).parent.parent / "data"


def connect_db():
    """Подключение к базе данных"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print(f"✅ Подключено к базе данных: {DB_CONFIG['database']}")
        return conn
    except Exception as e:
        print(f"❌ Ошибка подключения к БД: {e}")
        sys.exit(1)


def create_schema(conn):
    """Создание схемы базы данных"""
    schema_file = DATA_DIR / "schema" / "bearings_db_schema.sql"

    if not schema_file.exists():
        print(f"❌ Файл схемы не найден: {schema_file}")
        return False

    try:
        with open(schema_file, "r", encoding="utf-8") as f:
            schema_sql = f.read()

        cursor = conn.cursor()
        cursor.execute(schema_sql)
        conn.commit()
        cursor.close()

        print("✅ Схема базы данных создана")
        return True
    except Exception as e:
        print(f"❌ Ошибка создания схемы: {e}")
        return False


def import_csv_to_table(conn, csv_file, table_name, column_mapping=None):
    """
    Импорт CSV файла в таблицу

    Args:
        conn: Подключение к БД
        csv_file: Путь к CSV файлу
        table_name: Имя таблицы
        column_mapping: Словарь соответствия столбцов CSV -> БД
    """
    if not csv_file.exists():
        print(f"⚠️  Файл не найден: {csv_file}")
        return False

    try:
        # Чтение CSV
        df = pd.read_csv(csv_file, encoding="utf-8")

        # Переименование столбцов если нужно
        if column_mapping:
            df = df.rename(columns=column_mapping)

        # Подготовка данных для вставки
        cursor = conn.cursor()

        # Формирование SQL запроса
        columns = ", ".join(df.columns)
        placeholders = ", ".join(["%s"] * len(df.columns))
        insert_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        # Вставка данных
        rows_inserted = 0
        for _, row in df.iterrows():
            try:
                cursor.execute(insert_sql, tuple(row))
                rows_inserted += 1
            except Exception as e:
                print(f"⚠️  Ошибка вставки строки: {e}")
                continue

        conn.commit()
        cursor.close()

        print(f"✅ Импортировано {rows_inserted}/{len(df)} записей в {table_name}")
        return True

    except Exception as e:
        print(f"❌ Ошибка импорта {csv_file.name}: {e}")
        return False


def import_all_data(conn):
    """Импорт всех данных из CSV файлов"""

    print("\n📊 Начало импорта данных...")

    # 1. Импорт классов точности
    import_csv_to_table(
        conn,
        DATA_DIR / "csv" / "tolerance_classes.csv",
        "tolerance_classes",
        {
            "GOST": "gost_class",
            "ISO": "iso_class",
            "ABEC": "abec_class",
            "Описание": "description",
            "Применение": "applications",
        },
    )

    # 2. Импорт производителей СНГ
    import_csv_to_table(
        conn,
        DATA_DIR / "brands" / "manufacturers_cis.csv",
        "manufacturers",
        {
            "Brand": "brand",
            "Country": "country",
            "Company": "company_name",
            "Type": "manufacturer_type",
            "Quality_Level": "quality_level",
            "Specialization": "specialization",
            "Website": "website",
            "Notes": "notes",
        },
    )

    # 3. Импорт производителей Европы
    import_csv_to_table(
        conn,
        DATA_DIR / "brands" / "manufacturers_europe.csv",
        "manufacturers",
        {
            "Brand": "brand",
            "Country": "country",
            "Company": "company_name",
            "Type": "manufacturer_type",
            "Quality_Level": "quality_level",
            "Specialization": "specialization",
            "Website": "website",
            "Notes": "notes",
        },
    )

    # 4. Импорт производителей Азии
    import_csv_to_table(
        conn,
        DATA_DIR / "brands" / "manufacturers_asia.csv",
        "manufacturers",
        {
            "Brand": "brand",
            "Country": "country",
            "Company": "company_name",
            "Type": "manufacturer_type",
            "Quality_Level": "quality_level",
            "Specialization": "specialization",
            "Website": "website",
            "Notes": "notes",
        },
    )

    # 5. Импорт производителей Китая
    import_csv_to_table(
        conn,
        DATA_DIR / "brands" / "manufacturers_china.csv",
        "manufacturers",
        {
            "Brand": "brand",
            "Country": "country",
            "Company": "company_name",
            "Type": "manufacturer_type",
            "Quality_Level": "quality_level",
            "Specialization": "specialization",
            "Website": "website",
            "Notes": "notes",
        },
    )

    # 6. Импорт аналогов ГОСТ -> ISO
    import_csv_to_table(
        conn,
        DATA_DIR / "analogs" / "gost_to_iso.csv",
        "analogs",
        {
            "GOST": "source_designation",
            "ISO": "target_designation",
            "Type": "bearing_type",
            "Notes": "notes",
            "Source": "source_reference",
        },
    )

    # Добавить source_standard и target_standard для аналогов
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE analogs 
        SET source_standard = 'GOST', target_standard = 'ISO'
        WHERE source_standard IS NULL AND target_standard IS NULL
    """)
    conn.commit()
    cursor.close()

    # 7. Импорт дополнительных обозначений
    import_csv_to_table(
        conn,
        DATA_DIR / "analogs" / "additional_designations.csv",
        "additional_designations",
        {
            "GOST_Suffix": "gost_suffix",
            "ISO_Suffix": "iso_suffix",
            "SKF": "skf_suffix",
            "FAG": "fag_suffix",
            "NSK": "nsk_suffix",
            "NTN": "ntn_suffix",
            "Description": "description",
            "Notes": "notes",
        },
    )

    # 8. Импорт кодов ТН ВЭД
    import_csv_to_table(
        conn,
        DATA_DIR / "csv" / "tn_ved_codes.csv",
        "tn_ved_codes",
        {"Code": "code", "Description": "description", "Type": "bearing_type", "Notes": "notes"},
    )

    # 9. Импорт подшипниковых узлов
    import_csv_to_table(
        conn,
        DATA_DIR / "csv" / "bearing_units.csv",
        "bearing_units",
        {
            "Unit_Type": "unit_type",
            "Series": "series",
            "Description": "description",
            "Housing_Type": "housing_type",
            "Shaft_Fixing": "shaft_fixing",
            "Typical_Applications": "typical_applications",
        },
    )

    # 10. Импорт основного каталога подшипников
    # Этот импорт более сложный, так как нужно объединить данные из master_catalog и bearing_dimensions
    try:
        master = pd.read_csv(DATA_DIR / "csv" / "master_catalog.csv")
        dimensions = pd.read_csv(DATA_DIR / "dimensions" / "bearing_dimensions.csv")

        # Объединение по ISO обозначению
        combined = master.merge(
            dimensions[
                ["Designation", "Dynamic_Load_C_kN", "Static_Load_C0_kN", "Limiting_Speed_rpm", "Reference_Speed_rpm"]
            ],
            left_on="ISO",
            right_on="Designation",
            how="left",
        )

        cursor = conn.cursor()

        for _, row in combined.iterrows():
            try:
                cursor.execute(
                    """
                    INSERT INTO bearings (
                        gost_designation, iso_designation, skf_designation,
                        fag_designation, nsk_designation, ntn_designation,
                        koyo_designation, bearing_type, bore_diameter_d,
                        outer_diameter_D, width_B, chamfer_r_min, weight_kg,
                        dynamic_load_C_kN, static_load_C0_kN,
                        limiting_speed_rpm, reference_speed_rpm, category, status
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                    (
                        row["GOST"],
                        row["ISO"],
                        row["SKF"],
                        row["FAG"],
                        row["NSK"],
                        row["NTN"],
                        row["KOYO"],
                        row["Type"],
                        row["d"],
                        row["D"],
                        row["B"],
                        row["r_min"],
                        row["Weight_kg"],
                        row.get("Dynamic_Load_C_kN"),
                        row.get("Static_Load_C0_kN"),
                        row.get("Limiting_Speed_rpm"),
                        row.get("Reference_Speed_rpm"),
                        row["Category"],
                        row["Status"],
                    ),
                )
            except Exception as e:
                print(f"⚠️  Ошибка вставки подшипника {row['ISO']}: {e}")
                continue

        conn.commit()
        cursor.close()
        print(f"✅ Импортировано подшипников в основной каталог: {len(combined)}")

    except Exception as e:
        print(f"❌ Ошибка импорта основного каталога: {e}")

    print("\n✅ Импорт данных завершён!")


def main():
    """Главная функция"""
    print("=" * 60)
    print("Импорт данных справочника подшипников в PostgreSQL")
    print("=" * 60)

    # Подключение к БД
    conn = connect_db()

    try:
        # Создание схемы
        if create_schema(conn):
            # Импорт данных
            import_all_data(conn)

        print("\n" + "=" * 60)
        print("✅ Процесс завершён успешно!")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")

    finally:
        conn.close()
        print("\n🔌 Подключение к БД закрыто")


if __name__ == "__main__":
    main()
