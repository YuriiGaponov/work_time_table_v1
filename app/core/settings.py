from .utils import check_dir, get_path


class Settings():
    """Класс общих настроек приложения."""

    DB_PATH: str = 'data/db/'
    LOG_PATH: str = 'data/log/'
    LOG_ENCODING: str = 'utf-8'

    # Диапазон лет, в пределах которого ведется парсинг
    MIN_PARSE_YEAR = 2017
    MAX_PARSE_YEAR = 2026

    def get_db_path(self) -> str:
        """
        Возвращает путь к базе данных
        в зависимости от способа запуска приложения.
        """
        return get_path(self.DB_PATH)

    def get_log_path(self) -> str:
        """
        Возвращает путь к логам
        в зависимости от способа запуска приложения.
        """
        return get_path(self.LOG_PATH)

    def check_dirs(self) -> None:
        """Проверяет существование директорий и создает их, если нужно."""
        check_dir(self.get_db_path())
        check_dir(self.get_log_path())


# Экземпляр общих настроек приложения.
settings = Settings()
