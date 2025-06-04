from ..core import app_settings


class DBSettings():
    """Класс настроек базы данных."""

    def __init__(self, db_path):
        self.db_path = db_path

    DIALECT: str = 'sqlite'
    DB_NAME: str = 'worktimetable.db'

    def get_db_connection(self) -> str:
        """Возвращает строку с данными для подключения к базе данных."""
        return f'{self.DIALECT}:///{self.db_path}{self.DB_NAME}'


# Экземпляр общих настроек приложения.
db_settings = DBSettings(app_settings.DB_PATH)
