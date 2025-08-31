from .base import BaseConfig


class MainViewConfig(BaseConfig):
    """Настройки главнго окна приложения."""

    TITLE: str = 'Табель учёта рабочего времени'
    HEAD_LABLE: str = 'Табель учёта рабочего времени'
    GET_CALENDAR_BUTTON_TEXT: str = 'Календарь'
    EMPLOYEES_BUTTON_TEXT: str = 'Сотрудники'
    TABLE_BUTTON_TEXT: str = 'Табели'
