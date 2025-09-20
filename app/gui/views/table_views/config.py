"""
Модуль настроек окон для работы с табелями.
"""

import tkinter as tk
from tkinter import ttk
from typing import List

from app.calendar.models import CalendarDay
from app.gui.views.base import BaseConfig


class TableViewConfig(BaseConfig):
    """Настройки окна отображения табеля."""

    TITLE: str = 'Табель учета рабочего времени'
    HEAD_LABLE: str = 'Табель учета рабочего времени'

    COLUMN_WIDTH: int = 50

    def configure_tree(tree: ttk.Treeview, columns: List[CalendarDay]) -> None:
        """Установить настройки области отображения табеля."""
        for column in columns:
            tree.column(column, anchor=tk.CENTER,
                        width=TableViewConfig.COLUMN_WIDTH)
            tree.heading(column, text=column.day)


class TableSelectorViewConfig(BaseConfig):
    """Настройки окна выбора параметров табеля."""

    TITLE: str = 'Открыть табель'
    HEAD_LABLE: str = 'Выберите год, месяц, отдел'
    YEAR_ENTRY_LABEL_TEXT: str = 'Выберите год'
    MONTH_ENTRY_LABEL_TEXT: str = 'Выберите месяц'
    DEPARTMENT_ENTRY_LABEL_TEXT: str = 'Выберите отдел'
    OPEN_TABLE_BUTTON_TEXT: str = 'Открыть табель'
    CLEAN_BUTTON_TEXT: str = 'Очистить'
