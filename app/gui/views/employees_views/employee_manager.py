"""
Модуль главного окна работы с данными сотрудников.
"""

from tkinter import ttk

from app.gui.commands import open_modal_view
from app.gui.views.base import BaseModalView, base_grid
from .config import EmployeeManagerViewConfig
from .crud_employee import CreateEmployeeView, SearchEmployeeView


class EmployeeManagerView(BaseModalView):
    """Окно операций для работы со списком сотрудников."""

    def __init__(self, top_view):
        """Инициализация окна."""
        super().__init__(top_view)
        self.root.title(EmployeeManagerViewConfig.TITLE)
        self.root_head_lable.config(text=EmployeeManagerViewConfig.HEAD_LABLE)

        self.add_employee_button = ttk.Button(
            self.root_content_frame,
            text=EmployeeManagerViewConfig.ADD_EMPLOYEE_BUTTON_TEXT,
            command=self.add_employee
        )
        self.search_employee_button = ttk.Button(
            self.root_content_frame,
            text=EmployeeManagerViewConfig.SEARCH_EMPLOYEE_BUTTON_TEXT,
            command=self.search_employee
        )

        # Расположение виджетов.
        base_grid(self.add_employee_button, 0, 0, EmployeeManagerViewConfig)
        base_grid(self.search_employee_button, 1, 0, EmployeeManagerViewConfig)

    def add_employee(self) -> None:
        """Открыть окно добавления сотрудника в БД."""
        open_modal_view(self, CreateEmployeeView)

    def search_employee(self) -> None:
        """Открыть окно поиска сотрудника в БД."""
        open_modal_view(self, SearchEmployeeView)
