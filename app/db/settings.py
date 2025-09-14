from app.core import app_settings


class DBSettings():
    """Класс настроек базы данных."""

    def __init__(self, db_path):
        self.db_path = db_path

    DIALECT: str = 'sqlite'
    DB_NAME: str = 'worktimetable.db'

    def get_db_connection(self) -> str:
        """Возвращает строку с данными для подключения к базе данных."""
        return f'{self.DIALECT}:///{self.db_path}{self.DB_NAME}'


# Экземпляр настроек базы данных.
db_settings = DBSettings(app_settings.get_db_path())
