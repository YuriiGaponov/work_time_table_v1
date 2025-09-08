"""
Модуль настроек окон для работы с сотрудниками.
"""

import tkinter as tk
from tkinter import ttk
from typing import List, Tuple

from app.employees import Employee
from app.gui.views.base import BaseConfig


class EmployeeManagerViewConfig(BaseConfig):
    """Настройки окна работы со списком сотрудников."""

    TITLE: str = 'Список сотрудников'
    HEAD_LABLE: str = 'Список сотрудников'
    ADD_EMPLOYEE_BUTTON_TEXT: str = 'Добавить сотрудника'
    SEARCH_EMPLOYEE_BUTTON_TEXT: str = 'Найти сотрудника'


class CRUDEmployeeBaseViewConfig(BaseConfig):
    """Настройки окна создания нового сотрудника."""

    NAME_ENTRY_LABLE_TEXT: str = 'Имя'
    PATRONYMIC_ENTRY_LABLE_TEXT: str = 'Отчество'
    SURNAME_ENTRY_LABLE_TEXT: str = 'Фамилия'
    DEPARTMENT_ENTRY_LABLE_TEXT: str = 'Отдел'
    CLEAN_BUTTON_TEXT: str = 'Очистить'


class SearchEmployeeViewConfig(CRUDEmployeeBaseViewConfig):
    """Настройки окна поиска сотрудника."""

    TITLE: str = 'Найти сотрудника'
    HEAD_LABLE: str = 'Введите один или несколько параметров поиска'
    COMFIRM_BUTTON_TEXT: str = 'Найти'


class ShowEmployeeListViewConfig(BaseConfig):
    """Настройки окна отображения списка сотрудников."""

    TITLE: str = 'Список сотрудников'
    HEAD_LABLE: str = 'Результаты поиска сотрудников'
    TREE_COLUMNS: Tuple[str] = ('Имя', 'Отчество', 'Фамилия', 'Отдел')
    TREE_SHOW: str = 'headings'

    def configure_tree(tree: ttk.Treeview) -> None:
        """Установить настройки области отображения списка сотрудников."""
        tree.heading("Имя", text="Имя")
        tree.heading("Отчество", text="Отчество")
        tree.heading("Фамилия", text="Фамилия")
        tree.heading("Отдел", text="Отдел")

    def add_employees(tree: ttk.Treeview, employees: List[Employee]) -> None:
        """Добавить список сотрудников в область отображения."""
        for employee in employees:
            tree.insert(
                "", tk.END,
                values=(
                    employee.name,
                    employee.patronymic or "",
                    employee.surname,
                    employee.department
                )
            )


class CreateEmployeeViewConfig(CRUDEmployeeBaseViewConfig):
    """Настройки окна создания нового сотрудника."""

    TITLE: str = 'Добавление сотрудника'
    HEAD_LABLE: str = 'Введите фамилию, имя, отчество (при наличии), отдел'
    COMFIRM_BUTTON_TEXT: str = 'Добавить'


class EmployeeErrorViewConfig(BaseConfig):
    """
    Настройки информационного окна с сообщением об ошибке
    создания сотрудника с вводимыми данными.
    """

    TITLE: str = 'Ошибка создания сотрудника.'
