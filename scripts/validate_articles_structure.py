from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ARTICLES_DIR = REPO_ROOT / "docs" / "articles"
INDEX = ARTICLES_DIR / "INDEX.md"
SITEMAP = ARTICLES_DIR / "SITEMAP.md"

TEMPLATE_MARKERS = [
    "## Цель",
    "## Ключевые термины",
    "## Суть",
    "## Примеры",
    "## Связанные данные",
    "## Источники",
]

# Должно совпадать с генератором
EXPECTED: list[tuple[str, str]] = [
    ("docs/articles/bearings/1_1_designations_gost_iso_etu/1_1_1_gost_designation_system.md",
     "1.1.1 Система условных обозначений подшипников (ГОСТ)"),
    ("docs/articles/bearings/1_1_designations_gost_iso_etu/1_1_2_accuracy_classes_gost_iso_abec.md",
     "1.1.2 Класс точности подшипников (ГОСТ, ISO, ABEC)"),
    ("docs/articles/bearings/1_1_designations_gost_iso_etu/1_1_3_radial_clearances.md",
     "1.1.3 Радиальные зазоры в подшипниках качения"),
    ("docs/articles/bearings/1_1_designations_gost_iso_etu/1_1_4_friction_torque_designation.md",
     "1.1.4 Обозначение момента трения подшипников"),
    ("docs/articles/bearings/1_1_designations_gost_iso_etu/1_1_5_bearing_categories.md",
     "1.1.5 Обозначение категорий подшипников"),
    ("docs/articles/bearings/1_1_designations_gost_iso_etu/1_1_6_bore_diameter_designation.md",
     "1.1.6 Обозначение внутреннего диаметра подшипников"),
    ("docs/articles/bearings/1_1_designations_gost_iso_etu/1_1_7_dimension_series_designation.md",
     "1.1.7 Обозначение размерных серий подшипников"),
    ("docs/articles/bearings/1_1_designations_gost_iso_etu/1_1_8_bearing_types.md",
     "1.1.8 Типы подшипников"),
    ("docs/articles/bearings/1_1_designations_gost_iso_etu/1_1_9_cages.md",
     "1.1.9 Сепараторы подшипников качения"),
    ("docs/articles/bearings/1_1_designations_gost_iso_etu/1_1_10_lubrication.md",
     "1.1.10 Смазка подшипников"),
    ("docs/articles/bearings/1_1_designations_gost_iso_etu/1_1_11_designation_examples.md",
     "1.1.11 Примеры условного обозначения подшипников"),

    ("docs/articles/bearings/1_2_standards_and_codes/1_2_1_gost_standards.md",
     "1.2.1 ГОСТ. Подшипники. Стандарты"),
    ("docs/articles/bearings/1_2_standards_and_codes/1_2_2_iso_standards.md",
     "1.2.2 ISO. Стандарты подшипников"),
    ("docs/articles/bearings/1_2_standards_and_codes/1_2_3_analogs_gost_to_iso.md",
     "1.2.3 Аналоги подшипников ГОСТ → ISO"),
    ("docs/articles/bearings/1_2_standards_and_codes/1_2_4_analogs_iso_to_gost.md",
     "1.2.4 Аналоги подшипников ISO → ГОСТ"),
    ("docs/articles/bearings/1_2_standards_and_codes/1_2_5_additional_marks_analogs.md",
     "1.2.5 Аналоги дополнительных знаков ГОСТ ↔ ISO"),
    ("docs/articles/bearings/1_2_standards_and_codes/1_2_6_etu_100_500_tu.md",
     "1.2.6 Условные обозначения по ЕТУ-100, ЕТУ-500 и ТУ"),
    ("docs/articles/bearings/1_2_standards_and_codes/1_2_7_tnved_codes.md",
     "1.2.7 Коды ТН ВЭД на подшипники"),

    ("docs/articles/bearings/1_3_general_information/1_3_1_modifications_and_interchangeability.md",
     "1.3.1 Модификации подшипников и взаимозаменяемость"),
    ("docs/articles/bearings/1_3_general_information/1_3_2_bearing_components.md",
     "1.3.2 Из чего состоит подшипник"),
    ("docs/articles/bearings/1_3_general_information/1_3_3_how_bearings_are_made.md",
     "1.3.3 Как делают подшипники"),
    ("docs/articles/bearings/1_3_general_information/1_3_4_how_to_choose_bearing.md",
     "1.3.4 Как выбрать подшипник"),
    ("docs/articles/bearings/1_3_general_information/1_3_5_classification.md",
     "1.3.5 Классификация подшипников"),
    ("docs/articles/bearings/1_3_general_information/1_3_6_design_terminology.md",
     "1.3.6 Терминология конструкции подшипников"),
    ("docs/articles/bearings/1_3_general_information/1_3_7_terms_and_definitions.md",
     "1.3.7 Основные термины и определения"),
    ("docs/articles/bearings/1_3_general_information/1_3_8_loads.md",
     "1.3.8 Нагрузки на подшипники"),
    ("docs/articles/bearings/1_3_general_information/1_3_9_contact_angle.md",
     "1.3.9 Угол контакта (радиально-упорные)"),
    ("docs/articles/bearings/1_3_general_information/1_3_10_design_variants.md",
     "1.3.10 Конструктивные разновидности"),
    ("docs/articles/bearings/1_3_general_information/1_3_11_preload.md",
     "1.3.11 Предварительный натяг"),
    ("docs/articles/bearings/1_3_general_information/1_3_12_limiting_speed.md",
     "1.3.12 Предельная частота вращения"),
    ("docs/articles/bearings/1_3_general_information/1_3_13_duplex_sets.md",
     "1.3.13 Комплекты подшипников (дуплекс)"),
    ("docs/articles/bearings/1_3_general_information/1_3_14_marking.md",
     "1.3.14 Маркировка подшипников"),
    ("docs/articles/bearings/1_3_general_information/1_3_15_vibration_resistant.md",
     "1.3.15 Подшипники в виброустойчивом исполнении"),
    ("docs/articles/bearings/1_3_general_information/1_3_16_miniature.md",
     "1.3.16 Миниатюрные подшипники"),
    ("docs/articles/bearings/1_3_general_information/1_3_17_high_temperature.md",
     "1.3.17 Высокотемпературные подшипники"),
    ("docs/articles/bearings/1_3_general_information/1_3_18_installation.md",
     "1.3.18 Монтаж подшипников"),
    ("docs/articles/bearings/1_3_general_information/1_3_19_depreservation.md",
     "1.3.19 Переконсервация"),
    ("docs/articles/bearings/1_3_general_information/1_3_20_fits.md",
     "1.3.20 Посадки подшипников"),
    ("docs/articles/bearings/1_3_general_information/1_3_21_inspection.md",
     "1.3.21 Ревизия подшипников"),
    ("docs/articles/bearings/1_3_general_information/1_3_22_storage_and_packaging.md",
     "1.3.22 Хранение и упаковка"),
    ("docs/articles/bearings/1_3_general_information/1_3_23_damage_causes.md",
     "1.3.23 Причины повреждения подшипников"),
    ("docs/articles/bearings/1_3_general_information/1_3_24_defect_terminology.md",
     "1.3.24 Терминология дефектов"),
    ("docs/articles/bearings/1_3_general_information/1_3_25_electric_motors_failures.md",
     "1.3.25 Подшипники электродвигателей и причины отказов"),
    ("docs/articles/bearings/1_3_general_information/1_3_26_year_mark_decoding.md",
     "1.3.26 Таблица расшифровки года выпуска"),
    ("docs/articles/bearings/1_3_general_information/1_3_27_technical_literature.md",
     "1.3.27 Техническая литература по подшипникам"),

    ("docs/articles/bearings/1_4_types_and_modifications/1_4_1_spherical_roller.md",
     "1.4.1 Сферические роликовые подшипники"),
    ("docs/articles/bearings/1_4_types_and_modifications/1_4_2_spherical_plain_designations.md",
     "1.4.2 Шарнирные подшипники (Ш, ШЛ, ШС, ШП, ШСП и др.)"),
    ("docs/articles/bearings/1_4_types_and_modifications/1_4_3_needle_series_k_kk_ik.md",
     "1.4.3 Игольчатые подшипники (К, КК, ИК, ИКВ, КВК, КСК, АК)"),
    ("docs/articles/bearings/1_4_types_and_modifications/1_4_4_needle_stamped_ring_94_nk_nd.md",
     "1.4.4 Игольчатые подшипники с штампованным кольцом (94, НК, НД, СК, СН, ВК, ГК)"),
    ("docs/articles/bearings/1_4_types_and_modifications/1_4_5_combined_thrust_radial_rik.md",
     "1.4.5 Упорно-радиальные комбинированные (РИК, РИКБ и др.)"),
    ("docs/articles/bearings/1_4_types_and_modifications/1_4_6_rod_ends_cross_reference.md",
     "1.4.6 Шарнирные головки и наконечники (таблицы аналогов)"),
    ("docs/articles/bearings/1_4_types_and_modifications/1_4_7_bearings_with_roller_instead_of_inner_ring.md",
     "1.4.7 Подшипники с валиком вместо внутреннего кольца"),
    ("docs/articles/bearings/1_4_types_and_modifications/1_4_8_housed_units_ucf_ucp.md",
     "1.4.8 Подшипниковые узлы и корпусные подшипники (UCF, UCFL, UCP и др.)"),
    ("docs/articles/bearings/1_4_types_and_modifications/1_4_9_skf_y_bearings.md",
     "1.4.9 Подшипники SKF Y-типа (YEL, YET, YAR, YAT, YSA, YSP)"),
    ("docs/articles/bearings/1_4_types_and_modifications/1_4_10_universal_joints.md",
     "1.4.10 Крестовины карданного и рулевого вала"),
    ("docs/articles/bearings/1_4_types_and_modifications/1_4_11_hybrid_bearings.md",
     "1.4.11 Гибридные подшипники"),
    ("docs/articles/bearings/1_4_types_and_modifications/1_4_12_conveyor_rollers.md",
     "1.4.12 Конвейерные ролики"),
    ("docs/articles/bearings/1_4_types_and_modifications/1_4_13_bicycle_bearings.md",
     "1.4.13 Велосипедные подшипники"),
    ("docs/articles/bearings/1_4_types_and_modifications/1_4_14_spindle_bearings.md",
     "1.4.14 Шпиндельные подшипники"),

    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_1_cis_plants.md",
     "1.5.1 Заводы-изготовители подшипников СНГ"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_2_manufacturer_catalogs.md",
     "1.5.2 Каталоги производителей"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_3_online_catalogs.md",
     "1.5.3 Онлайн-каталоги производителей"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_4_mpz_designations.md",
     "1.5.4 Обозначения подшипников МПЗ"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_5_skf_designations.md",
     "1.5.5 Обозначения подшипников SKF"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_6_skf_explorer.md",
     "1.5.6 Подшипники SKF Explorer"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_7_fag_designations.md",
     "1.5.7 Обозначения подшипников FAG"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_8_nsk_designations.md",
     "1.5.8 Обозначения подшипников NSK"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_9_ntn_snr_designations.md",
     "1.5.9 Обозначения подшипников NTN-SNR"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_10_snfa_designations.md",
     "1.5.10 Обозначения подшипников SNFA"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_11_koyo_designations.md",
     "1.5.11 Обозначения подшипников KOYO"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_12_gmn_designations.md",
     "1.5.12 Обозначения подшипников GMN"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_13_barden_designations.md",
     "1.5.13 Обозначения подшипников BARDEN"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_14_fkl_designations.md",
     "1.5.14 Обозначения подшипников FKL"),
    ("docs/articles/bearings/1_5_brands_and_manufacturers/1_5_15_bbc_r_designations.md",
     "1.5.15 Обозначения подшипников BBC-R"),

    ("docs/articles/bearings/1_6_rolling_elements_nuts_sleeves/1_6_1_ball_designations.md",
     "1.6.1 Обозначение шариков"),
    ("docs/articles/bearings/1_6_rolling_elements_nuts_sleeves/1_6_2_roller_designations.md",
     "1.6.2 Обозначение роликов"),
    ("docs/articles/bearings/1_6_rolling_elements_nuts_sleeves/1_6_3_rolling_elements_applicability.md",
     "1.6.3 Тела качения и применяемость"),
    ("docs/articles/bearings/1_6_rolling_elements_nuts_sleeves/1_6_4_adapter_withdrawal_sleeves.md",
     "1.6.4 Закрепительные и стяжные втулки"),
    ("docs/articles/bearings/1_6_rolling_elements_nuts_sleeves/1_6_5_nuts.md",
     "1.6.5 Гайки"),

    ("docs/articles/bearings/1_7_plain_bushings/1_7_1_plain_bushings.md",
     "1.7.1 Втулки скольжения"),
    ("docs/articles/bearings/1_7_plain_bushings/1_7_2_plain_bearings.md",
     "1.7.2 Подшипники скольжения"),

    ("docs/articles/bearings/1_8_automotive/1_8_1_automotive_bearing_kits.md",
     "1.8.1 Комплекты SKF, FAG, SNR, TIMKEN, FERSA, QH"),
    ("docs/articles/bearings/1_8_automotive/1_8_2_skf_hub_selection_tips.md",
     "1.8.2 Советы SKF по выбору ступичных подшипников"),
    ("docs/articles/bearings/1_8_automotive/1_8_3_hub_failure_symptoms.md",
     "1.8.3 Симптомы неисправностей ступицы"),
    ("docs/articles/bearings/1_8_automotive/1_8_4_ac_compressor_bearings.md",
     "1.8.4 Подшипники автомобильных кондиционеров"),
    ("docs/articles/bearings/1_8_automotive/1_8_5_mixer_gearbox_bearings_and_seals.md",
     "1.8.5 Подшипники и сальники редукторов автобетоносмесителей"),

    ("docs/articles/bearings/1_9_misc/1_9_1_chinese_bearings.md",
     "1.9.1 Китайские подшипники"),
    ("docs/articles/bearings/1_9_misc/1_9_2_interesting.md",
     "1.9.2 Интересное о подшипниках"),
    ("docs/articles/bearings/1_9_misc/1_9_3_wooden_bearings.md",
     "1.9.3 Деревянные подшипники"),
    ("docs/articles/bearings/1_9_misc/1_9_4_english_terms.md",
     "1.9.4 Термины на английском языке"),
    ("docs/articles/bearings/1_9_misc/1_9_5_word_bearing_in_languages.md",
     "1.9.5 Слово «подшипник» на разных языках"),
    ("docs/articles/bearings/1_9_misc/1_9_6_humor.md",
     "1.9.6 С юмором о подшипниках"),

    ("docs/articles/2_ball_joints/2_1_ball_joint.md",
     "2.1 Шариковая опора"),
    ("docs/articles/3_linear_guides_and_ball_screws/3_1_linear_guides.md",
     "3.1 Линейные направляющие качения и скольжения"),
    ("docs/articles/3_linear_guides_and_ball_screws/3_2_ball_screw.md",
     "3.2 ШВП — шариковая винтовая передача"),
    ("docs/articles/3_linear_guides_and_ball_screws/3_3_roller_linear_supports.md",
     "3.3 Роликовые линейные опоры (РС, ЛОК, RUS, Р88, РОД, РОНА-120)"),
    ("docs/articles/4_rti_gost/4_1_rti_overview.md",
     "4.1 ГОСТ Резино-технические изделия (РТИ)"),
    ("docs/articles/5_drive_belts/5_1_drive_belts.md",
     "5.1 Приводные ремни"),
    ("docs/articles/5_drive_belts/5_2_belt_selection_by_size.md",
     "5.2 Подбор ремня по размеру"),
    ("docs/articles/5_drive_belts/5_3_belt_drive_failures.md",
     "5.3 Неисправности ременной передачи"),
    ("docs/articles/5_drive_belts/5_4_gost_vs_import_belt_sizes.md",
     "5.4 Размеры и аналоги (ГОСТ ↔ импорт)"),
    ("docs/articles/5_drive_belts/5_5_belt_length_calculation.md",
     "5.5 Расчёт длины ремня"),
    ("docs/articles/6_seals_and_cuffs/6_1_reinforced_rubber_seals.md",
     "6.1 Резиновые армированные манжеты (сальники)"),
    ("docs/articles/6_seals_and_cuffs/6_2_seal_selection_by_size.md",
     "6.2 Подбор сальника или манжеты по размерам"),
    ("docs/articles/7_hoses_and_rvd/7_1_industrial_hoses.md",
     "7.1 Промышленные рукава и шланги"),
    ("docs/articles/7_hoses_and_rvd/7_2_high_pressure_hoses_rvd.md",
     "7.2 Рукава высокого давления (РВД)"),
    ("docs/articles/8_o_rings/8_1_o_rings.md",
     "8.1 Кольца резиновые уплотнительные круглого сечения"),
    ("docs/articles/9_pulleys/9_1_pulleys_for_belts.md",
     "9.1 Шкивы для приводных ремней"),
    ("docs/articles/9_pulleys/9_2_skf_pulleys_for_narrow_v_belts.md",
     "9.2 Шкивы SKF для узких клиновых ремней"),
    ("docs/articles/10_chains_and_sprockets/10_1_drive_chains.md",
     "10.1 Приводные цепи"),
    ("docs/articles/10_chains_and_sprockets/10_2_chain_drive.md",
     "10.2 Цепная передача"),
    ("docs/articles/10_chains_and_sprockets/10_3_sprockets.md",
     "10.3 Звёздочки"),
    ("docs/articles/10_chains_and_sprockets/10_4_gost_chains_sprockets.md",
     "10.4 ГОСТ цепи и звёздочки"),
    ("docs/articles/11_accessories/11_1_circlips.md",
     "11.1 Стопорные кольца"),
    ("docs/articles/11_accessories/11_2_filters.md",
     "11.2 Фильтры"),
    ("docs/articles/11_accessories/11_3_technical_fluids.md",
     "11.3 Технические жидкости"),
    ("docs/articles/11_accessories/11_4_quick_couplings_camlock_fittings.md",
     "11.4 Быстроразъёмные соединения (БРС, CAMLOCK, фитинги)"),
    ("docs/articles/11_accessories/11_5_gear_pumps_nsh.md",
     "11.5 Насосы шестерённые НШ"),
    ("docs/articles/11_accessories/11_6_gearboxes.md",
     "11.6 Редукторы"),
    ("docs/articles/11_accessories/11_7_taper_bush.md",
     "11.7 Втулки TAPER BUSH"),
]


def fail(msg: str) -> None:
    raise SystemExit(f"ERROR: {msg}")


def read_first_h1(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def main() -> None:
    if not ARTICLES_DIR.exists():
        fail("docs/articles does not exist")

    if not INDEX.exists():
        fail("docs/articles/INDEX.md missing")
    if not SITEMAP.exists():
        fail("docs/articles/SITEMAP.md missing")

    # Check files exist and H1 matches
    for rel, expected_h1 in EXPECTED:
        p = REPO_ROOT / rel
        if not p.exists():
            fail(f"missing file: {rel}")
        actual_h1 = read_first_h1(p)
        if actual_h1 != expected_h1:
            fail(f"H1 mismatch in {rel}: '{actual_h1}' != '{expected_h1}'")

        content = p.read_text(encoding="utf-8")
        for marker in TEMPLATE_MARKERS:
            if marker not in content:
                fail(f"template marker '{marker}' missing in {rel}")

    # Validate SITEMAP: must be plain paths, one per line (no bullets)
    sitemap_lines = SITEMAP.read_text(encoding="utf-8").splitlines()
    if any(ln.startswith("- ") or ln.startswith("#") for ln in sitemap_lines if ln.strip()):
        fail("SITEMAP.md must contain only paths, no bullets and no headings")

    # Validate SITEMAP contains at least all expected files
    # SITEMAP paths are relative to docs/articles/, so we need to strip that prefix
    sitemap_set = {ln.strip() for ln in sitemap_lines if ln.strip()}
    for rel, _ in EXPECTED:
        # Convert "docs/articles/path" to "path" for comparison
        rel_without_prefix = rel.replace("docs/articles/", "")
        if rel_without_prefix not in sitemap_set:
            fail(f"SITEMAP.md missing path: {rel_without_prefix}")

    print("OK: articles structure validated")


if __name__ == "__main__":
    main()
