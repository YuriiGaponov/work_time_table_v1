import os
import sys

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


def get_db_path(relative_path):
    """
    В зависимости от способа запуска приложения:
    - исполняемая папка / файл
    - через терминал на этапе разработки
    возвращает абсолютный путь до базы данных.
    """
    try:
        # Для исполняемого файла
        base_path = sys._MEIPASS
    except Exception:
        # Для разработки
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Экземпляр общих настроек приложения.
db_settings = DBSettings(get_db_path(app_settings.DB_PATH))
