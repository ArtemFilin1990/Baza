-- Bearing Reference Database Schema
-- Version 1.0
-- Created: 2026-01-20

-- ======================================================
-- Table: bearings (Master catalog)
-- Description: Main bearing catalog with all designations
-- ======================================================

CREATE TABLE IF NOT EXISTS bearings (
    id SERIAL PRIMARY KEY,
    gost_designation VARCHAR(50),
    iso_designation VARCHAR(50) NOT NULL,
    skf_designation VARCHAR(50),
    fag_designation VARCHAR(50),
    nsk_designation VARCHAR(50),
    ntn_designation VARCHAR(50),
    koyo_designation VARCHAR(50),
    bearing_type VARCHAR(100) NOT NULL,
    bore_diameter_d DECIMAL(10,3) NOT NULL,
    outer_diameter_D DECIMAL(10,3) NOT NULL,
    width_B DECIMAL(10,3) NOT NULL,
    chamfer_r_min DECIMAL(10,3),
    weight_kg DECIMAL(10,6),
    dynamic_load_C_kN DECIMAL(10,3),
    static_load_C0_kN DECIMAL(10,3),
    limiting_speed_rpm INTEGER,
    reference_speed_rpm INTEGER,
    category VARCHAR(50),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_bearings_gost ON bearings(gost_designation);
CREATE INDEX idx_bearings_iso ON bearings(iso_designation);
CREATE INDEX idx_bearings_type ON bearings(bearing_type);
CREATE INDEX idx_bearings_dimensions ON bearings(bore_diameter_d, outer_diameter_D, width_B);

-- ======================================================
-- Table: manufacturers
-- Description: Bearing manufacturers and brands
-- ======================================================

CREATE TABLE IF NOT EXISTS manufacturers (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(100) NOT NULL UNIQUE,
    country VARCHAR(100) NOT NULL,
    company_name VARCHAR(255) NOT NULL,
    manufacturer_type VARCHAR(50),
    quality_level VARCHAR(50),
    specialization TEXT,
    website VARCHAR(255),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_manufacturers_brand ON manufacturers(brand);
CREATE INDEX idx_manufacturers_country ON manufacturers(country);
CREATE INDEX idx_manufacturers_quality ON manufacturers(quality_level);

-- ======================================================
-- Table: analogs
-- Description: Bearing analogs and cross-references
-- ======================================================

CREATE TABLE IF NOT EXISTS analogs (
    id SERIAL PRIMARY KEY,
    source_standard VARCHAR(20) NOT NULL,
    source_designation VARCHAR(50) NOT NULL,
    target_standard VARCHAR(20) NOT NULL,
    target_designation VARCHAR(50) NOT NULL,
    bearing_type VARCHAR(100),
    is_direct_analog BOOLEAN DEFAULT TRUE,
    limitations TEXT,
    notes TEXT,
    source_reference VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_analogs_source ON analogs(source_standard, source_designation);
CREATE INDEX idx_analogs_target ON analogs(target_standard, target_designation);

-- ======================================================
-- Table: additional_designations
-- Description: Additional suffixes and modifiers
-- ======================================================

CREATE TABLE IF NOT EXISTS additional_designations (
    id SERIAL PRIMARY KEY,
    gost_suffix VARCHAR(20),
    iso_suffix VARCHAR(20),
    skf_suffix VARCHAR(20),
    fag_suffix VARCHAR(20),
    nsk_suffix VARCHAR(20),
    ntn_suffix VARCHAR(20),
    description TEXT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_additional_gost ON additional_designations(gost_suffix);
CREATE INDEX idx_additional_iso ON additional_designations(iso_suffix);

-- ======================================================
-- Table: tolerance_classes
-- Description: Tolerance and precision classes
-- ======================================================

CREATE TABLE IF NOT EXISTS tolerance_classes (
    id SERIAL PRIMARY KEY,
    gost_class VARCHAR(10) NOT NULL,
    iso_class VARCHAR(10) NOT NULL,
    abec_class VARCHAR(10),
    description TEXT,
    applications TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_tolerance_gost ON tolerance_classes(gost_class);
CREATE INDEX idx_tolerance_iso ON tolerance_classes(iso_class);

-- ======================================================
-- Table: tn_ved_codes
-- Description: Customs codes (HS codes) for bearings
-- ======================================================

CREATE TABLE IF NOT EXISTS tn_ved_codes (
    id SERIAL PRIMARY KEY,
    code VARCHAR(20) NOT NULL UNIQUE,
    description TEXT NOT NULL,
    bearing_type VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_tn_ved_code ON tn_ved_codes(code);

-- ======================================================
-- Table: bearing_units
-- Description: Bearing housing units (UCP, UCF, etc.)
-- ======================================================

CREATE TABLE IF NOT EXISTS bearing_units (
    id SERIAL PRIMARY KEY,
    unit_type VARCHAR(20) NOT NULL,
    series VARCHAR(50),
    description TEXT,
    housing_type VARCHAR(100),
    shaft_fixing VARCHAR(100),
    typical_applications TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_units_type ON bearing_units(unit_type);

-- ======================================================
-- Table: standards
-- Description: GOST and ISO standards
-- ======================================================

CREATE TABLE IF NOT EXISTS standards (
    id SERIAL PRIMARY KEY,
    standard_type VARCHAR(20) NOT NULL,
    standard_number VARCHAR(50) NOT NULL,
    standard_year INTEGER,
    title TEXT NOT NULL,
    scope TEXT,
    status VARCHAR(20),
    replaces VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_standards_type ON standards(standard_type);
CREATE INDEX idx_standards_number ON standards(standard_number);

-- ======================================================
-- Views for common queries
-- ======================================================

-- View: Full bearing information with all analogs
CREATE OR REPLACE VIEW v_bearing_full AS
SELECT 
    b.id,
    b.gost_designation,
    b.iso_designation,
    b.skf_designation,
    b.fag_designation,
    b.nsk_designation,
    b.ntn_designation,
    b.koyo_designation,
    b.bearing_type,
    b.bore_diameter_d AS d,
    b.outer_diameter_D AS D,
    b.width_B AS B,
    b.chamfer_r_min AS r,
    b.weight_kg,
    b.dynamic_load_C_kN,
    b.static_load_C0_kN,
    b.limiting_speed_rpm,
    b.reference_speed_rpm,
    b.category,
    b.status
FROM bearings b
WHERE b.status = 'Active';

-- View: Manufacturer directory
CREATE OR REPLACE VIEW v_manufacturers AS
SELECT 
    m.brand,
    m.country,
    m.company_name,
    m.quality_level,
    m.specialization,
    m.website
FROM manufacturers m
ORDER BY m.quality_level DESC, m.brand;

-- ======================================================
-- Sample data insertion
-- ======================================================

-- Insert sample tolerance classes
INSERT INTO tolerance_classes (gost_class, iso_class, abec_class, description, applications) VALUES
('Р0', 'P0', 'ABEC-1', 'Класс точности 0 (нормальный)', 'Общее применение'),
('Р6', 'P6', 'ABEC-3', 'Класс точности 6 (повышенный)', 'Электродвигатели средней точности'),
('Р5', 'P5', 'ABEC-5', 'Класс точности 5 (высокий)', 'Станки средней точности'),
('Р4', 'P4', 'ABEC-7', 'Класс точности 4 (прецизионный)', 'Шпиндели станков'),
('Р2', 'P2', 'ABEC-9', 'Класс точности 2 (сверхпрецизионный)', 'Высокоточные шпиндели')
ON CONFLICT DO NOTHING;

-- Insert sample standards
INSERT INTO standards (standard_type, standard_number, standard_year, title, scope, status) VALUES
('GOST', '520', 2002, 'Подшипники качения. Общие технические условия', 'Общие требования к подшипникам качения', 'Active'),
('GOST', '3189', 1989, 'Подшипники шариковые и роликовые. Система условных обозначений', 'Система обозначений подшипников', 'Active'),
('ISO', '15', 1998, 'Rolling bearings - Radial bearings - Boundary dimensions', 'Размеры радиальных подшипников', 'Active'),
('ISO', '355', 2007, 'Rolling bearings - Tapered roller bearings', 'Конические роликовые подшипники', 'Active'),
('ISO', '492', 2014, 'Rolling bearings - Radial bearings - Geometrical product specifications (GPS) and tolerance values', 'Допуски и технические требования', 'Active')
ON CONFLICT DO NOTHING;

-- ======================================================
-- Functions for data validation
-- ======================================================

-- Function to validate bearing designation format
CREATE OR REPLACE FUNCTION validate_bearing_designation(designation VARCHAR)
RETURNS BOOLEAN AS $$
BEGIN
    -- Basic validation: not empty and reasonable length
    RETURN designation IS NOT NULL AND LENGTH(designation) > 0 AND LENGTH(designation) <= 50;
END;
$$ LANGUAGE plpgsql;

-- Function to find analogs
CREATE OR REPLACE FUNCTION find_analogs(
    p_designation VARCHAR,
    p_standard VARCHAR DEFAULT 'GOST'
)
RETURNS TABLE (
    analog_standard VARCHAR,
    analog_designation VARCHAR,
    is_direct BOOLEAN,
    notes TEXT
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        a.target_standard,
        a.target_designation,
        a.is_direct_analog,
        a.notes
    FROM analogs a
    WHERE a.source_standard = p_standard
    AND a.source_designation = p_designation
    ORDER BY a.is_direct_analog DESC, a.target_standard;
END;
$$ LANGUAGE plpgsql;

-- ======================================================
-- Comments for documentation
-- ======================================================

COMMENT ON TABLE bearings IS 'Основной каталог подшипников с размерами и характеристиками';
COMMENT ON TABLE manufacturers IS 'Справочник производителей и брендов подшипников';
COMMENT ON TABLE analogs IS 'Таблица аналогов и кросс-референсов между стандартами';
COMMENT ON TABLE additional_designations IS 'Дополнительные обозначения (суффиксы и модификаторы)';
COMMENT ON TABLE tolerance_classes IS 'Классы точности ГОСТ/ISO/ABEC';
COMMENT ON TABLE tn_ved_codes IS 'Коды ТН ВЭД для таможенного оформления';
COMMENT ON TABLE bearing_units IS 'Подшипниковые узлы в корпусах';
COMMENT ON TABLE standards IS 'Справочник стандартов ГОСТ и ISO';

-- ======================================================
-- Grant permissions (adjust as needed)
-- ======================================================

-- GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_user;
-- GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO readwrite_user;
-- GRANT ALL ON ALL TABLES IN SCHEMA public TO admin_user;

-- ======================================================
-- End of schema
-- ======================================================
