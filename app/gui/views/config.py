from .base import BaseConfig


class MainViewConfig(BaseConfig):
    """Настройки главнго окна приложения."""

    TITLE: str = 'Табель учёта рабочего времени'
    HEAD_LABLE: str = 'Табель учёта рабочего времени'
    GET_CALENDAR_BUTTON_TEXT: str = 'Скачать\nпроизводственный\nкалендарь'
    EMPLOYEES_BUTTON_TEXT: str = 'Список\nсотрудников'
