import tkinter as tk

from app.gui.commands import create_employee, open_list_employee
from app.gui.views.base import BaseListView
from .config import (
    CreateEmployeeViewConfig,
    SearchEmployeeViewConfig,
    ShowEmployeeListViewConfig
)
from .crud_base_employee import CRUDEmployeeBaseView


class SearchEmployeeView(CRUDEmployeeBaseView):
    """Окно поиска сотрудника."""

    def __init__(self, top_view):
        """Инициализация окна."""
        super().__init__(top_view)
        self.root.title(SearchEmployeeViewConfig.TITLE)
        self.root_head_lable.config(
            text=SearchEmployeeViewConfig.HEAD_LABLE
        )
        self.confirm_button.config(
            text=SearchEmployeeViewConfig.COMFIRM_BUTTON_TEXT
        )

    def confirm(self):
        """Найти сотрудника."""
        open_list_employee(self, super().confirm())


class ShowEmployeeListView(BaseListView):
    """Окно отображения списка сотрудников."""

    def __init__(self, top_view, items=None):
        """Инициализация окна."""
        super().__init__(top_view, items)
        self.root.title(ShowEmployeeListViewConfig.TITLE)
        self.root_head_lable.config(
            text=ShowEmployeeListViewConfig.HEAD_LABLE
        )
        self.listbox.config(
            width=ShowEmployeeListViewConfig.LISTBOX_WIDTH
        )

        for item in self.items:
            self.listbox.insert(
                tk.END, f'{item.name} {item.patronymic} '
                f'{item.surname} {item.department}'
            )


class CreateEmployeeView(CRUDEmployeeBaseView):
    """Окно создания нового сотрудника."""

    def __init__(self, top_view):
        """Инициализация окна."""
        super().__init__(top_view)
        self.root.title(CreateEmployeeViewConfig.TITLE)
        self.root_head_lable.config(
            text=CreateEmployeeViewConfig.HEAD_LABLE
        )
        self.confirm_button.config(
            text=CreateEmployeeViewConfig.COMFIRM_BUTTON_TEXT
        )

    def confirm(self):
        """Создать сотрудника."""
        create_employee(self, super().confirm())
