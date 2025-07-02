class Settings():
    """Класс общих настроек приложения."""

    DB_PATH: str = 'data/db/'
    LOG_PATH: str = 'data/log/'
    LOG_ENCODING: str = 'utf-8'


# Экземпляр общих настроек приложения.
settings = Settings()
