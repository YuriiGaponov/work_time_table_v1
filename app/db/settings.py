from ..core import app_settings


class DBSettings():
    """Класс настроек базы данных."""

    def __init__(self, db_path):
        self.db_path = db_path

    dialect: str = 'sqlite'
    db_name: str = 'worktimetable.db'

    def get_db_connection(self) -> str:
        """Возвращает строку с данными для подключения к базе данных."""
        return f'{self.dialect}:///{self.db_path}{self.db_name}'


# Экземпляр общих настроек приложения.
db_settings = DBSettings(app_settings.db_path)
