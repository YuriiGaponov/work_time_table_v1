"""
Модуль настроек окон для работы с табелями.
"""

import tkinter as tk
from tkinter import ttk
from typing import List

from app.calendar import CalendarDay
from app.employees.models import Employee
from app.gui.views.base import BaseConfig


class TableViewConfig(BaseConfig):
    """Настройки окна отображения табеля."""

    TITLE: str = 'Табель учета рабочего времени'
    HEAD_LABLE: str = 'Табель учета рабочего времени'

    COLUMN_WIDTH: int = 25

    @classmethod
    def set_columns(cls, calendar_days: List[CalendarDay]) -> list:
        """
        Создает колонки табеля, первая для сотрудников,
        последующие для каждого дя месяца.
        """
        columns = ['employee'] + [day for day in calendar_days]
        return columns

    @classmethod
    def configure_columns(cls, tree: ttk.Treeview, columns: list) -> None:
        """Установить настройки столбцов табеля."""
        # Скрываем первый автоматический столбец
        tree.column("#0", width=0, stretch=tk.NO)
        # Установить заголовок для первого столбца
        tree.heading('employee', text='Сотрудник')

        for column in columns[1:]:
            tree.column(column, anchor=tk.CENTER,
                        width=cls.COLUMN_WIDTH)
            tree.heading(column, text=column.day)

    def add_employees(tree: ttk.Treeview, employees: List[Employee]) -> None:
        """Добавить список сотрудников в область отображения."""
        for employee in employees:
            tree.insert("", tk.END, values=(employee.initials(),))


class TableSelectorViewConfig(BaseConfig):
    """Настройки окна выбора параметров табеля."""

    TITLE: str = 'Открыть табель'
    HEAD_LABLE: str = 'Выберите год, месяц, отдел'
    YEAR_ENTRY_LABEL_TEXT: str = 'Выберите год'
    MONTH_ENTRY_LABEL_TEXT: str = 'Выберите месяц'
    DEPARTMENT_ENTRY_LABEL_TEXT: str = 'Выберите отдел'
    OPEN_TABLE_BUTTON_TEXT: str = 'Открыть табель'
    CLEAN_BUTTON_TEXT: str = 'Очистить'
