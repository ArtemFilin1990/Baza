-- Инициализация базы данных для каталога подшипников
-- Placeholder для SQL из bearing-api/sql/init_catalog.sql

-- Создание основных таблиц

-- Таблица подшипников
CREATE TABLE IF NOT EXISTS bearings (
    id SERIAL PRIMARY KEY,
    designation VARCHAR(100) NOT NULL UNIQUE,
    bearing_type VARCHAR(50),
    inner_diameter DECIMAL(10, 3),
    outer_diameter DECIMAL(10, 3),
    width DECIMAL(10, 3),
    manufacturer VARCHAR(100),
    standard VARCHAR(20),
    dynamic_capacity DECIMAL(10, 3),
    static_capacity DECIMAL(10, 3),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица аналогов
CREATE TABLE IF NOT EXISTS analogs (
    id SERIAL PRIMARY KEY,
    original_designation VARCHAR(100) NOT NULL,
    analog_designation VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(100),
    standard VARCHAR(20),
    compatibility DECIMAL(3, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(original_designation, analog_designation)
);

-- Таблица производителей
CREATE TABLE IF NOT EXISTS manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    country VARCHAR(100),
    website VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица стандартов
CREATE TABLE IF NOT EXISTS standards (
    id SERIAL PRIMARY KEY,
    code VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(255),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Индексы для оптимизации поиска
CREATE INDEX IF NOT EXISTS idx_bearings_designation ON bearings(designation);
CREATE INDEX IF NOT EXISTS idx_bearings_type ON bearings(bearing_type);
CREATE INDEX IF NOT EXISTS idx_bearings_manufacturer ON bearings(manufacturer);
CREATE INDEX IF NOT EXISTS idx_analogs_original ON analogs(original_designation);
CREATE INDEX IF NOT EXISTS idx_analogs_analog ON analogs(analog_designation);

-- Комментарии к таблицам
COMMENT ON TABLE bearings IS 'Каталог подшипников';
COMMENT ON TABLE analogs IS 'Таблица аналогов подшипников';
COMMENT ON TABLE manufacturers IS 'Производители подшипников';
COMMENT ON TABLE standards IS 'Стандарты (ГОСТ, ISO, DIN и др.)';
