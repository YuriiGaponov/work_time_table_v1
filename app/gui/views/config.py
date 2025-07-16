from .base import BaseConfig


class MainViewConfig(BaseConfig):
    """Настройки главнго окна приложения."""

    TITLE: str = 'Табель учёта рабочего времени'
    HEAD_LABLE: str = 'Табель учёта рабочего времени'
    GET_CALENDAR_BUTTON_TEXT: str = 'Скачать\nпроизводственный\nкалендарь'


class ParserYearSelectorViewConfig(BaseConfig):
    """Настройки окон модуля парсинга календаря."""

    TITLE: str = 'Укажите год'
    HEAD_LABLE: str = 'Укажите год скачиваемого календаря'
    CONTENT_LABLE: str = 'Введите год'
    CONFIRM_BUTTON_TEXT: str = 'Подтвердить'
    CLEAN_BUTTON_TEXT: str = 'Очистить'
    STICKY: str = 'NSEW'
