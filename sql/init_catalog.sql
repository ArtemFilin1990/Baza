-- Инициализация базы данных для каталога подшипников
-- Включает таблицы для истории поиска и аналитики

-- Таблица истории поиска
CREATE TABLE IF NOT EXISTS search_history (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255),      -- IP или user_token (опционально)
    query TEXT NOT NULL,
    results_count INTEGER,
    clicked_result_id VARCHAR(100),  -- Какой результат выбрал пользователь
    timestamp TIMESTAMP DEFAULT NOW(),
    session_id VARCHAR(100)
);

-- Индексы для оптимизации запросов
CREATE INDEX idx_search_history_user ON search_history(user_id);
CREATE INDEX idx_search_history_query ON search_history(query);
CREATE INDEX idx_search_history_timestamp ON search_history(timestamp);
CREATE INDEX idx_search_history_session ON search_history(session_id);

-- Таблица для кеширования популярных запросов
CREATE TABLE IF NOT EXISTS popular_queries (
    id SERIAL PRIMARY KEY,
    query TEXT NOT NULL UNIQUE,
    search_count INTEGER DEFAULT 0,
    last_searched TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_popular_queries_count ON popular_queries(search_count DESC);
CREATE INDEX idx_popular_queries_updated ON popular_queries(updated_at);

-- Таблица для хранения метаданных документов
CREATE TABLE IF NOT EXISTS documents (
    id VARCHAR(100) PRIMARY KEY,
    title TEXT NOT NULL,
    path TEXT NOT NULL,
    content_hash VARCHAR(64),
    word_count INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_documents_path ON documents(path);
CREATE INDEX idx_documents_title ON documents(title);

-- Таблица для хранения аналогов подшипников
CREATE TABLE IF NOT EXISTS bearing_analogs (
    id SERIAL PRIMARY KEY,
    original_code VARCHAR(50) NOT NULL,
    analog_code VARCHAR(50) NOT NULL,
    manufacturer VARCHAR(100),
    standard VARCHAR(50),
    compatibility_score DECIMAL(3,2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_bearing_analogs_original ON bearing_analogs(original_code);
CREATE INDEX idx_bearing_analogs_analog ON bearing_analogs(analog_code);
CREATE INDEX idx_bearing_analogs_manufacturer ON bearing_analogs(manufacturer);

-- Функция для автоматического обновления популярных запросов
CREATE OR REPLACE FUNCTION update_popular_queries()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO popular_queries (query, search_count, last_searched)
    VALUES (NEW.query, 1, NEW.timestamp)
    ON CONFLICT (query) 
    DO UPDATE SET 
        search_count = popular_queries.search_count + 1,
        last_searched = NEW.timestamp,
        updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Триггер для автоматического обновления популярных запросов
DROP TRIGGER IF EXISTS trigger_update_popular_queries ON search_history;
CREATE TRIGGER trigger_update_popular_queries
    AFTER INSERT ON search_history
    FOR EACH ROW
    EXECUTE FUNCTION update_popular_queries();

-- Представление для аналитики поиска
CREATE OR REPLACE VIEW search_analytics AS
SELECT 
    DATE(timestamp) as search_date,
    COUNT(*) as total_searches,
    COUNT(DISTINCT user_id) as unique_users,
    COUNT(DISTINCT query) as unique_queries,
    AVG(results_count) as avg_results_per_query,
    COUNT(CASE WHEN results_count = 0 THEN 1 END) as zero_result_searches
FROM search_history
GROUP BY DATE(timestamp)
ORDER BY search_date DESC;

-- Комментарии к таблицам
COMMENT ON TABLE search_history IS 'История поисковых запросов пользователей';
COMMENT ON TABLE popular_queries IS 'Кеш популярных поисковых запросов';
COMMENT ON TABLE documents IS 'Метаданные документов для поиска';
COMMENT ON TABLE bearing_analogs IS 'Таблица аналогов подшипников';
COMMENT ON VIEW search_analytics IS 'Аналитическое представление истории поиска';
