class Settings():
    """Класс общих настроек приложения."""

    DB_PATH: str = 'data/db/'
    LOG_PATH: str = 'data/log/'


# Экземпляр общих настроек приложения.
settings = Settings()
