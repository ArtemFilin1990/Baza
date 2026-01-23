-- Минимальная схема для базы знаний (WIP)

CREATE TABLE IF NOT EXISTS kb_article (
    id SERIAL PRIMARY KEY,
    slug TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    section TEXT NOT NULL,
    subsection TEXT NOT NULL,
    status TEXT DEFAULT 'draft',
    updated_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS kb_alias (
    id SERIAL PRIMARY KEY,
    article_id INTEGER REFERENCES kb_article(id) ON DELETE CASCADE,
    alias TEXT NOT NULL,
    kind TEXT
);

CREATE TABLE IF NOT EXISTS ref_brand (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    country TEXT,
    tier TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS ref_manufacturer (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    country TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS ref_standard (
    id SERIAL PRIMARY KEY,
    code TEXT UNIQUE NOT NULL,
    title TEXT,
    body TEXT,
    year INTEGER
);

CREATE TABLE IF NOT EXISTS ref_tnved (
    id SERIAL PRIMARY KEY,
    code TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS map_gost_iso (
    id SERIAL PRIMARY KEY,
    gost_code TEXT NOT NULL,
    iso_code TEXT NOT NULL,
    match_type TEXT,
    confidence TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS map_suffix (
    id SERIAL PRIMARY KEY,
    standard_code TEXT NOT NULL,
    suffix TEXT NOT NULL,
    meaning TEXT
);

CREATE TABLE IF NOT EXISTS bearing_dimension (
    id SERIAL PRIMARY KEY,
    designation TEXT,
    d_mm NUMERIC(8,3),
    D_mm NUMERIC(8,3),
    B_mm NUMERIC(8,3),
    source TEXT
);
