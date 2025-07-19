class Settings():
    """Класс общих настроек приложения."""

    DB_PATH: str = 'data/db/'
    LOG_PATH: str = 'data/log/'
    LOG_ENCODING: str = 'utf-8'

    # Диапазон лет, в пределах которого ведется парсинг
    MIN_PARSE_YEAR = 2017
    MAX_PARSE_YEAR = 2026


# Экземпляр общих настроек приложения.
settings = Settings()
