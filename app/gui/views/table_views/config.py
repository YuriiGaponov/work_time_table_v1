"""
Модуль настроек окон для работы с табелями.
"""

from app.gui.views.base import BaseConfig


class TableViewConfig(BaseConfig):
    """Настройки окна отображения табеля."""

    TITLE: str = 'Табель учета рабочего времени'
    HEAD_LABLE: str = 'Табель учета рабочего времени'


class TableSelectorViewConfig(BaseConfig):
    """Настройки окна выбора параметров табеля."""

    TITLE: str = 'Открыть табель'
    HEAD_LABLE: str = 'Выберите год, месяц, отдел'
    YEAR_ENTRY_LABEL_TEXT: str = 'Выберите год'
    MONTH_ENTRY_LABEL_TEXT: str = 'Выберите месяц'
    DEPARTMENT_ENTRY_LABEL_TEXT: str = 'Выберите отдел'
